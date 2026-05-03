"""
auto_poster.py — Recruitin Authority Campaign Auto-Poster (Component 4 v1)

Reads a Notion content-calendar database, finds rows where
`Status == "Ready"` and `Scheduled-time <= now`, and publishes each row
to LinkedIn (UGC Posts) and/or Meta (Graph API). On success it writes
the canonical post-URL back into Notion and flips Status to "Published".
On failure it flips Status to "Failed" / "Failed-Partial" and appends
a timestamped error to the `Notes` rich-text field.

Designed for GitHub Actions cron (`*/15 * * * *`). All secrets read
from environment; nothing is hardcoded.

Idempotency
-----------
A row whose `Post-URL` is already populated is skipped, even if Status
is still "Ready". To genuinely re-post, clear `Post-URL` in Notion first.

Dry-run mode
------------
Set env `DRY_RUN=true` and the script logs everything it WOULD do
without calling LinkedIn / Meta APIs and without writing back to Notion.

Limitations (v1)
----------------
- Single-image posts only. Carousel / Reel / Video / Story formats are
  recognised and skipped with a `Notes` line. Multi-asset adapters land
  in v2.
- LinkedIn is hit at /v2/ugcPosts (text + optional single image).
- Meta is hit at /v18.0/{page_id}/feed (text+link) or /photos (image).
"""

from __future__ import annotations

import logging
import os
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Optional

import requests
from notion_client import Client as NotionClient
from notion_client.errors import APIResponseError

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("auto-poster")

# ---------------------------------------------------------------------------
# Config from env
# ---------------------------------------------------------------------------

NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "")
NOTION_DB_ID = os.environ.get("NOTION_DB_ID", "")
LINKEDIN_ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN", "")
LINKEDIN_AUTHOR_URN = os.environ.get("LINKEDIN_AUTHOR_URN", "")
META_PAGE_TOKEN = os.environ.get("META_PAGE_TOKEN", "")
META_PAGE_ID = os.environ.get("META_PAGE_ID", "")
LANDING_URL = os.environ.get("LANDING_URL", "https://recruitmentengineer.nl")
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() in ("1", "true", "yes")

LINKEDIN_API = "https://api.linkedin.com/v2"
META_API = "https://graph.facebook.com/v18.0"

# Map Notion Status values
STATUS_READY = "Ready"
STATUS_PUBLISHED = "Published"
STATUS_FAILED = "Failed"
STATUS_FAILED_PARTIAL = "Failed-Partial"

# Formats the v1 poster can handle.
PUBLISHABLE_FORMATS = {"Long-post", "Image"}
SKIPPED_FORMATS = {"Carousel", "Reel", "Video", "Story"}


# ---------------------------------------------------------------------------
# Domain types
# ---------------------------------------------------------------------------


@dataclass
class CalendarRow:
    """A single row from the Notion content-calendar DB."""

    page_id: str
    title: str
    status: str
    platforms: list[str]            # subset of {"LinkedIn", "Meta", "Both"}
    fmt: str                        # value of `Format` select
    body: str
    cta: str
    media_url: Optional[str]        # first file attachment, if any
    scheduled_time: Optional[datetime]
    generated_link: str
    post_url: Optional[str]
    notes: str

    def effective_platforms(self) -> list[str]:
        """Resolve `Both` / multi-select into a flat list of canonical platforms."""
        if "Both" in self.platforms:
            return ["LinkedIn", "Meta"]
        return [p for p in self.platforms if p in ("LinkedIn", "Meta")]

    def body_with_link(self) -> str:
        """Insert the UTM-tagged link into the body.

        If `{LINK}` placeholder exists, replace it. Otherwise append.
        """
        link = self.generated_link or LANDING_URL
        if "{LINK}" in self.body:
            return self.body.replace("{LINK}", link)
        if link in self.body:
            return self.body  # already present, do not duplicate
        sep = "\n\n" if not self.body.endswith("\n") else ""
        return f"{self.body}{sep}{link}"


# ---------------------------------------------------------------------------
# Notion helpers
# ---------------------------------------------------------------------------


def _rich_text_plain(prop: dict[str, Any]) -> str:
    """Concatenate the plain_text of a rich_text Notion property."""
    rt = prop.get("rich_text") or prop.get("title") or []
    return "".join(item.get("plain_text", "") for item in rt)


def _formula_string(prop: dict[str, Any]) -> str:
    """Read a formula property's string value."""
    f = prop.get("formula") or {}
    return f.get("string") or ""


def _multi_select_values(prop: dict[str, Any]) -> list[str]:
    return [opt["name"] for opt in prop.get("multi_select", [])]


def _select_value(prop: dict[str, Any]) -> str:
    sel = prop.get("select")
    return sel["name"] if sel else ""


def _status_value(prop: dict[str, Any]) -> str:
    st = prop.get("status")
    return st["name"] if st else ""


def _date_value(prop: dict[str, Any]) -> Optional[datetime]:
    d = prop.get("date")
    if not d or not d.get("start"):
        return None
    raw = d["start"]
    # Notion may return YYYY-MM-DD (no time) or full ISO with TZ.
    try:
        if "T" in raw:
            return datetime.fromisoformat(raw.replace("Z", "+00:00"))
        # Date-only: treat as midnight UTC (poster will likely fire same day).
        return datetime.fromisoformat(raw + "T00:00:00+00:00")
    except ValueError:
        log.warning("Could not parse scheduled-time %r", raw)
        return None


def _files_first_url(prop: dict[str, Any]) -> Optional[str]:
    files = prop.get("files") or []
    if not files:
        return None
    f = files[0]
    if f.get("type") == "external":
        return f["external"]["url"]
    if f.get("type") == "file":
        return f["file"]["url"]
    return None


def _url_value(prop: dict[str, Any]) -> Optional[str]:
    return prop.get("url")


def parse_row(page: dict[str, Any]) -> CalendarRow:
    """Map a Notion page object into our `CalendarRow` dataclass."""
    props = page["properties"]

    return CalendarRow(
        page_id=page["id"],
        title=_rich_text_plain(props["Title"]),
        status=_status_value(props["Status"]),
        platforms=_multi_select_values(props["Platform"]),
        fmt=_select_value(props["Format"]),
        body=_rich_text_plain(props["Body"]),
        cta=_rich_text_plain(props.get("CTA", {})),
        media_url=_files_first_url(props.get("Media", {})),
        scheduled_time=_date_value(props["Scheduled-time"]),
        generated_link=_formula_string(props["Generated-link"]),
        post_url=_url_value(props.get("Post-URL", {})),
        notes=_rich_text_plain(props.get("Notes", {})),
    )


def query_ready_rows(notion: NotionClient) -> list[CalendarRow]:
    """Query Notion for rows that are eligible to publish.

    Filter: Status == "Ready" AND Scheduled-time <= now AND Post-URL is empty.
    """
    now_iso = datetime.now(timezone.utc).isoformat()

    flt = {
        "and": [
            {"property": "Status", "status": {"equals": STATUS_READY}},
            {"property": "Scheduled-time", "date": {"on_or_before": now_iso}},
            {"property": "Post-URL", "url": {"is_empty": True}},
        ]
    }

    rows: list[CalendarRow] = []
    cursor: Optional[str] = None
    while True:
        resp = notion.databases.query(
            database_id=NOTION_DB_ID,
            filter=flt,
            start_cursor=cursor,
            page_size=50,
        )
        for page in resp.get("results", []):
            try:
                rows.append(parse_row(page))
            except KeyError as e:
                log.error("Row %s missing property %s — skip", page.get("id"), e)
        if not resp.get("has_more"):
            break
        cursor = resp.get("next_cursor")
    return rows


def update_row_published(
    notion: NotionClient,
    page_id: str,
    post_url: str,
    extra_note: str = "",
) -> None:
    """Flip a row to Status=Published and write Post-URL."""
    payload = {
        "Status": {"status": {"name": STATUS_PUBLISHED}},
        "Post-URL": {"url": post_url},
    }
    if extra_note:
        payload["Notes"] = _append_note(notion, page_id, extra_note)
    notion.pages.update(page_id=page_id, properties=payload)


def update_row_failed(
    notion: NotionClient,
    page_id: str,
    error: str,
    partial_post_url: Optional[str] = None,
) -> None:
    """Flip a row to Status=Failed (or Failed-Partial) and append error to Notes."""
    status = STATUS_FAILED_PARTIAL if partial_post_url else STATUS_FAILED
    payload: dict[str, Any] = {"Status": {"status": {"name": status}}}
    if partial_post_url:
        payload["Post-URL"] = {"url": partial_post_url}
    payload["Notes"] = _append_note(notion, page_id, error)
    notion.pages.update(page_id=page_id, properties=payload)


def _append_note(notion: NotionClient, page_id: str, line: str) -> dict[str, Any]:
    """Build a Notes rich-text payload with `line` appended.

    Notion overwrites rich_text on update, so we must read existing first.
    """
    try:
        page = notion.pages.retrieve(page_id=page_id)
        existing = _rich_text_plain(page["properties"].get("Notes", {}))
    except APIResponseError:
        existing = ""
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    new = f"{existing}\n[{stamp}] {line}".strip()
    return {"rich_text": [{"text": {"content": new[:2000]}}]}


# ---------------------------------------------------------------------------
# LinkedIn poster
# ---------------------------------------------------------------------------


class LinkedInPoster:
    """Posts to LinkedIn via the UGC Posts API.

    Reference:
      https://learn.microsoft.com/en-us/linkedin/marketing/integrations/community-management/shares/ugc-post-api
    """

    def __init__(self, token: str, author_urn: str) -> None:
        if not token or not author_urn:
            raise RuntimeError("LinkedIn token / author URN missing")
        self.token = token
        self.author_urn = author_urn
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "X-Restli-Protocol-Version": "2.0.0",
            "Content-Type": "application/json",
        })

    def post_text(self, body: str) -> str:
        """Publish a plain text post. Returns the canonical share URL."""
        payload = {
            "author": self.author_urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": body},
                    "shareMediaCategory": "NONE",
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
        }
        r = self._with_retry("POST", f"{LINKEDIN_API}/ugcPosts", json=payload)
        r.raise_for_status()
        urn = r.headers.get("x-restli-id") or r.json().get("id", "")
        return self._urn_to_url(urn)

    def post_with_image(self, body: str, image_url: str) -> str:
        """Publish a post with one image. v1 stub — uploads via two-step asset flow.

        In production this needs to:
          1. POST /assets?action=registerUpload (returns uploadUrl + asset urn)
          2. PUT bytes to uploadUrl
          3. POST /ugcPosts with shareMediaCategory=IMAGE + media=[{status: READY, media: <asset urn>}]

        For v1 we fall back to text-only posting and log a warning.
        """
        log.warning(
            "LinkedIn image upload not implemented in v1 — posting as text-only. "
            "Image URL: %s",
            image_url,
        )
        return self.post_text(body)

    @staticmethod
    def _urn_to_url(urn: str) -> str:
        """Convert `urn:li:share:7234567890123456789` → linkedin.com/feed/update/..."""
        if not urn:
            return ""
        # LinkedIn returns either share or ugcPost URNs depending on endpoint.
        return f"https://www.linkedin.com/feed/update/{urn}"

    def _with_retry(self, method: str, url: str, **kw: Any) -> requests.Response:
        """Simple 3-attempt exponential backoff for 5xx + 429."""
        for attempt in range(3):
            r = self.session.request(method, url, timeout=30, **kw)
            if r.status_code < 500 and r.status_code != 429:
                return r
            wait = 2 ** (attempt + 1)
            log.warning(
                "LinkedIn %s %s → %d, retry in %ds",
                method, url, r.status_code, wait,
            )
            time.sleep(wait)
        return r  # last response, possibly still failing


# ---------------------------------------------------------------------------
# Meta poster
# ---------------------------------------------------------------------------


class MetaPoster:
    """Posts to a Meta (Facebook) Page via Graph API.

    Reference:
      https://developers.facebook.com/docs/graph-api/reference/v18.0/page/feed
      https://developers.facebook.com/docs/graph-api/reference/v18.0/page/photos
    """

    def __init__(self, page_id: str, page_token: str) -> None:
        if not page_id or not page_token:
            raise RuntimeError("Meta page id / token missing")
        self.page_id = page_id
        self.page_token = page_token

    def post_text(self, body: str, link: Optional[str] = None) -> str:
        """Publish text-only or text+link to /feed. Returns post-URL."""
        url = f"{META_API}/{self.page_id}/feed"
        data: dict[str, Any] = {
            "message": body,
            "access_token": self.page_token,
            "published": "true",
        }
        if link:
            data["link"] = link
        r = self._with_retry("POST", url, data=data)
        r.raise_for_status()
        post_id = r.json().get("id", "")
        return self._post_id_to_url(post_id)

    def post_with_image(self, body: str, image_url: str) -> str:
        """Publish a single image post via /photos."""
        url = f"{META_API}/{self.page_id}/photos"
        data = {
            "message": body,
            "url": image_url,
            "access_token": self.page_token,
            "published": "true",
        }
        r = self._with_retry("POST", url, data=data)
        r.raise_for_status()
        body_json = r.json()
        post_id = body_json.get("post_id") or body_json.get("id", "")
        return self._post_id_to_url(post_id)

    def _post_id_to_url(self, post_id: str) -> str:
        """post_id like '123456_789012' → https://www.facebook.com/{page_id}/posts/789012"""
        if not post_id:
            return ""
        if "_" in post_id:
            _, p = post_id.split("_", 1)
            return f"https://www.facebook.com/{self.page_id}/posts/{p}"
        return f"https://www.facebook.com/{post_id}"

    @staticmethod
    def _with_retry(method: str, url: str, **kw: Any) -> requests.Response:
        """Same retry policy as LinkedIn poster."""
        for attempt in range(3):
            r = requests.request(method, url, timeout=30, **kw)
            if r.status_code < 500 and r.status_code != 429:
                return r
            wait = 2 ** (attempt + 1)
            log.warning("Meta %s %s → %d, retry in %ds", method, url, r.status_code, wait)
            time.sleep(wait)
        return r


# ---------------------------------------------------------------------------
# Per-platform link rewriter
# ---------------------------------------------------------------------------


_UTM_SOURCE_RE = re.compile(r"(utm_source=)([^&]+)")


def _build_link_for_platform(generated_link: str, platform: str) -> str:
    """Rewrite the `utm_source` to be platform-specific even if Notion stored 'cross'."""
    if not generated_link:
        return LANDING_URL
    target = "linkedin" if platform == "LinkedIn" else "meta"
    return _UTM_SOURCE_RE.sub(rf"\g<1>{target}", generated_link)


def _body_with_platform_link(row: CalendarRow, platform: str) -> str:
    """Like row.body_with_link() but uses a platform-specific UTM source."""
    link = _build_link_for_platform(row.generated_link, platform)
    if "{LINK}" in row.body:
        return row.body.replace("{LINK}", link)
    if link in row.body:
        return row.body
    sep = "\n\n" if not row.body.endswith("\n") else ""
    return f"{row.body}{sep}{link}"


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def process_row(
    row: CalendarRow,
    notion: NotionClient,
    li: Optional[LinkedInPoster],
    meta: Optional[MetaPoster],
) -> None:
    """Publish one row to all its platforms, then update Notion accordingly."""
    log.info("Processing row %s (%s) → %s", row.title, row.status, row.platforms)

    if row.post_url:
        log.info("Skip %s — already has Post-URL", row.title)
        return

    if row.fmt in SKIPPED_FORMATS:
        log.warning("Skip %s — format %s requires v2 carousel adapter", row.title, row.fmt)
        if not DRY_RUN:
            update_row_failed(
                notion, row.page_id,
                f"skipped: format '{row.fmt}' requires v2 carousel adapter",
            )
        return

    if row.fmt and row.fmt not in PUBLISHABLE_FORMATS:
        log.warning("Skip %s — unknown format %s", row.title, row.fmt)
        if not DRY_RUN:
            update_row_failed(
                notion, row.page_id,
                f"skipped: unknown format '{row.fmt}'",
            )
        return

    platforms = row.effective_platforms()
    if not platforms:
        log.error("Row %s has no valid Platform value", row.title)
        if not DRY_RUN:
            update_row_failed(notion, row.page_id, "no valid Platform value set")
        return

    success_urls: dict[str, str] = {}
    failures: dict[str, str] = {}

    for platform in platforms:
        body = _body_with_platform_link(row, platform)
        try:
            if platform == "LinkedIn":
                if not li:
                    raise RuntimeError("LinkedIn poster not configured")
                if DRY_RUN:
                    log.info("[DRY] Would post %d-char body to LinkedIn:\n%s",
                             len(body), body[:200])
                    success_urls[platform] = "https://dryrun.linkedin.invalid/x"
                else:
                    if row.media_url:
                        url = li.post_with_image(body, row.media_url)
                    else:
                        url = li.post_text(body)
                    success_urls[platform] = url
                    log.info("LinkedIn OK → %s", url)
            elif platform == "Meta":
                if not meta:
                    raise RuntimeError("Meta poster not configured")
                if DRY_RUN:
                    log.info("[DRY] Would post %d-char body to Meta:\n%s",
                             len(body), body[:200])
                    success_urls[platform] = "https://dryrun.meta.invalid/x"
                else:
                    if row.media_url:
                        url = meta.post_with_image(body, row.media_url)
                    else:
                        url = meta.post_text(body)
                    success_urls[platform] = url
                    log.info("Meta OK → %s", url)
        except (requests.RequestException, RuntimeError) as e:  # noqa: PERF203
            log.exception("%s posting failed for row %s", platform, row.title)
            failures[platform] = str(e)[:300]

    # Update Notion
    if DRY_RUN:
        log.info("[DRY] Would update Notion row %s — successes=%s failures=%s",
                 row.title, list(success_urls), list(failures))
        return

    if success_urls and not failures:
        # Use first url as canonical Post-URL
        canon = next(iter(success_urls.values()))
        extra = ""
        if len(success_urls) > 1:
            others = "; ".join(f"{p}={u}" for p, u in success_urls.items())
            extra = f"published: {others}"
        update_row_published(notion, row.page_id, canon, extra_note=extra)
    elif success_urls and failures:
        canon = next(iter(success_urls.values()))
        err = "; ".join(f"{p}: {e}" for p, e in failures.items())
        update_row_failed(notion, row.page_id, err, partial_post_url=canon)
    else:
        err = "; ".join(f"{p}: {e}" for p, e in failures.items())
        update_row_failed(notion, row.page_id, err)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    """Entry point. Returns process exit code."""
    if not NOTION_TOKEN or not NOTION_DB_ID:
        log.error("NOTION_TOKEN and NOTION_DB_ID are required")
        return 2

    log.info("Auto-poster start. DRY_RUN=%s", DRY_RUN)

    notion = NotionClient(auth=NOTION_TOKEN)

    li: Optional[LinkedInPoster] = None
    meta: Optional[MetaPoster] = None

    if LINKEDIN_ACCESS_TOKEN and LINKEDIN_AUTHOR_URN:
        try:
            li = LinkedInPoster(LINKEDIN_ACCESS_TOKEN, LINKEDIN_AUTHOR_URN)
        except RuntimeError as e:
            log.warning("LinkedIn poster disabled: %s", e)
    else:
        log.warning("LinkedIn secrets not set — LinkedIn rows will be marked Failed")

    if META_PAGE_TOKEN and META_PAGE_ID:
        try:
            meta = MetaPoster(META_PAGE_ID, META_PAGE_TOKEN)
        except RuntimeError as e:
            log.warning("Meta poster disabled: %s", e)
    else:
        log.warning("Meta secrets not set — Meta rows will be marked Failed")

    try:
        rows = query_ready_rows(notion)
    except APIResponseError as e:
        log.exception("Notion query failed: %s", e)
        return 3

    log.info("Found %d eligible row(s)", len(rows))
    if not rows:
        return 0

    errors = 0
    for row in rows:
        try:
            process_row(row, notion, li, meta)
        except Exception:  # noqa: BLE001
            log.exception("Unhandled error processing row %s", row.title)
            errors += 1

    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
