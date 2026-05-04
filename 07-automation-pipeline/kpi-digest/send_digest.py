#!/usr/bin/env python3
"""
Recruitment Engineering Stack 2026 — daily KPI digest -> Slack.

Pulls three signals and posts one Slack-block-kit message:
  1. Resend audience size + new contacts in the last 24h.
  2. Pipedrive pipeline 16 ("Authority Leads") deals per stage + 24h velocity.
  3. Email drip sends in the last 24h (mail2/3/4) from local state file.

Auth:
  * Resend  - Bearer token via RESEND_API_KEY (UA header set; default urllib UA
              hits Cloudflare 403 on /audiences endpoints).
  * Pipedrive - Personal API Token via `?api_token=` query param, NOT Bearer
                (PIPEDRIVE_AUTH_REGEL).

Usage:
    python send_digest.py                # post to Slack
    python send_digest.py --dry-run      # print payload, no POST
    python send_digest.py --verbose      # debug logging

Cron: triggered daily by .github/workflows/kpi-digest.yml at 07:00 UTC.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

import requests

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

AUDIENCE_ID = "703b9a1f-fc00-4796-8bf3-664350a89879"  # "Stack 2026 Leads"

PIPEDRIVE_DOMAIN = os.getenv("PIPEDRIVE_DOMAIN", "recruitin")
PIPELINE_ID = int(os.getenv("PIPEDRIVE_PIPELINE_ID", "16"))

RESEND_API = "https://api.resend.com"
PD_BASE = f"https://{PIPEDRIVE_DOMAIN}.pipedrive.com/api/v1"

# Cloudflare blocks the default urllib UA on Resend audience endpoints.
USER_AGENT = "recruitmentengineer-kpi-digest/1.0 (+https://recruitmentengineer.nl)"

REPO_ROOT = Path(__file__).resolve().parents[2]
STATE_FILE = REPO_ROOT / "09-launch" / "email-drip-state.json"

LANDING_URL = "https://recruitmentengineer.nl"

DRIP_TAGS = ["drip:2", "drip:3", "drip:4"]


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

VERBOSE = False


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    print(f"[{ts}] {msg}", flush=True)


def vlog(msg: str) -> None:
    if VERBOSE:
        log(msg)


# ---------------------------------------------------------------------------
# Resend
# ---------------------------------------------------------------------------

def fetch_resend_contacts(api_key: str) -> list[dict[str, Any]]:
    contacts: list[dict[str, Any]] = []
    url = f"{RESEND_API}/audiences/{AUDIENCE_ID}/contacts"
    params: dict[str, Any] = {}
    while True:
        resp = requests.get(
            url,
            headers={
                "Authorization": f"Bearer {api_key}",
                "User-Agent": USER_AGENT,
            },
            params=params,
            timeout=30,
        )
        if resp.status_code != 200:
            log(f"ERROR: Resend list failed {resp.status_code}: {resp.text[:200]}")
            resp.raise_for_status()
        body = resp.json()
        batch = body.get("data") or []
        contacts.extend(batch)
        if not body.get("has_more") or not batch:
            break
        params["after"] = batch[-1].get("id")
    return contacts


def parse_iso(raw: str | None) -> datetime | None:
    if not raw:
        return None
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    try:
        return datetime.fromisoformat(raw)
    except ValueError:
        return None


def audience_stats(contacts: list[dict[str, Any]], cutoff: datetime) -> dict[str, int]:
    total = len(contacts)
    new_24h = 0
    unsub = 0
    for c in contacts:
        if c.get("unsubscribed"):
            unsub += 1
        created = parse_iso(c.get("created_at"))
        if created and created >= cutoff:
            new_24h += 1
    return {"total": total, "new_24h": new_24h, "unsubscribed": unsub}


# ---------------------------------------------------------------------------
# Pipedrive
# ---------------------------------------------------------------------------

def pd_get(token: str, path: str, **params: Any) -> dict[str, Any]:
    params["api_token"] = token
    r = requests.get(f"{PD_BASE}{path}?{urlencode(params)}", timeout=30)
    r.raise_for_status()
    return r.json()


def fetch_pipeline_stages(token: str) -> dict[int, str]:
    """Return {stage_id: stage_name} for the configured pipeline."""
    data = pd_get(token, f"/stages", pipeline_id=PIPELINE_ID)
    out: dict[int, str] = {}
    for stage in data.get("data") or []:
        sid = stage.get("id")
        name = stage.get("name") or str(sid)
        if sid is not None:
            out[int(sid)] = name
    return out


def fetch_pipeline_deals(token: str) -> list[dict[str, Any]]:
    deals: list[dict[str, Any]] = []
    start = 0
    limit = 100
    while True:
        data = pd_get(
            token,
            f"/pipelines/{PIPELINE_ID}/deals",
            start=start,
            limit=limit,
        )
        items = data.get("data") or []
        deals.extend(items)
        more = (
            data.get("additional_data", {})
            .get("pagination", {})
            .get("more_items_in_collection")
        )
        if not more:
            break
        start += limit
    return deals


def parse_pd_time(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.strptime(s, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def pipeline_stats(
    deals: list[dict[str, Any]],
    stages: dict[int, str],
    cutoff: datetime,
) -> dict[str, Any]:
    per_stage: dict[int, int] = {sid: 0 for sid in stages}
    updated_24h = 0
    added_24h = 0
    open_deals = 0
    for d in deals:
        sid = d.get("stage_id")
        if isinstance(sid, int):
            per_stage[sid] = per_stage.get(sid, 0) + 1
        if d.get("status") == "open":
            open_deals += 1
        if (added := parse_pd_time(d.get("add_time"))) and added >= cutoff:
            added_24h += 1
        if (updated := parse_pd_time(d.get("update_time"))) and updated >= cutoff:
            updated_24h += 1
    return {
        "per_stage": per_stage,
        "updated_24h": updated_24h,
        "added_24h": added_24h,
        "open": open_deals,
        "total": len(deals),
    }


# ---------------------------------------------------------------------------
# Email drip state
# ---------------------------------------------------------------------------

def load_drip_state() -> dict[str, Any]:
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        log(f"WARN: drip state file unreadable ({e}); treating as empty.")
        return {}


def drip_stats(state: dict[str, Any], cutoff: datetime) -> dict[str, int]:
    """Count drip sends in last 24h.

    Tolerates two state shapes:
      A. {"<contact_id>": ["drip:2", "drip:3", ...]}      (current send_drip.py)
      B. {"<email>": {"mail2": "ISO-ts", "mail3": "..."}}  (timestamped variant)

    For shape A there is no per-mail timestamp, so we count entries whose
    file mtime falls in the window — this gives a "today's send count" floor
    if and only if the file was updated by today's drip run. Shape B is
    counted precisely.
    """
    counts = {"mail2": 0, "mail3": 0, "mail4": 0}
    if not state:
        return counts

    # Detect shape
    sample = next(iter(state.values()), None)
    if isinstance(sample, dict):
        # Shape B — timestamped per-mail
        key_map = {"mail2": "mail2", "mail3": "mail3", "mail4": "mail4",
                   "drip:2": "mail2", "drip:3": "mail3", "drip:4": "mail4"}
        for entry in state.values():
            if not isinstance(entry, dict):
                continue
            for k, v in entry.items():
                bucket = key_map.get(k)
                if not bucket:
                    continue
                ts = parse_iso(v) if isinstance(v, str) else None
                if ts and ts >= cutoff:
                    counts[bucket] += 1
        return counts

    # Shape A — list of tags, no per-tag timestamp
    try:
        mtime = datetime.fromtimestamp(STATE_FILE.stat().st_mtime, tz=timezone.utc)
    except OSError:
        return counts
    if mtime < cutoff:
        return counts

    tag_map = {"drip:2": "mail2", "drip:3": "mail3", "drip:4": "mail4"}
    # Without per-mail timestamps the best we can do is count tags currently in
    # state. On the morning after a drip run this approximates "sends today";
    # on subsequent days the file is older than cutoff and we return zeros.
    for entry in state.values():
        if not isinstance(entry, list):
            continue
        for tag in entry:
            bucket = tag_map.get(tag)
            if bucket:
                counts[bucket] += 1
    return counts


# ---------------------------------------------------------------------------
# Slack payload
# ---------------------------------------------------------------------------

def build_blocks(
    audience: dict[str, int],
    pipeline: dict[str, Any],
    stages: dict[int, str],
    drip: dict[str, int],
    run_id: str,
) -> dict[str, Any]:
    date_nl = datetime.now(timezone.utc).astimezone().strftime("%a %d %b %Y")

    # Stage table — sorted by stage_id so order matches funnel direction.
    stage_lines = []
    for sid in sorted(stages.keys()):
        name = stages[sid]
        count = pipeline["per_stage"].get(sid, 0)
        stage_lines.append(f"`{count:>3}`  {name}  _(id {sid})_")
    stage_block = "\n".join(stage_lines) if stage_lines else "_no stages found_"

    audience_text = (
        f"*Total contacts:* {audience['total']}\n"
        f"*New (24h):* {audience['new_24h']}\n"
        f"*Unsubscribed:* {audience['unsubscribed']}"
    )

    pipeline_summary = (
        f"*Open deals:* {pipeline['open']} / {pipeline['total']}    "
        f"*Added (24h):* {pipeline['added_24h']}    "
        f"*Updated (24h):* {pipeline['updated_24h']}"
    )

    drip_text = (
        f"`mail2`  {drip['mail2']}    "
        f"`mail3`  {drip['mail3']}    "
        f"`mail4`  {drip['mail4']}"
    )

    blocks: list[dict[str, Any]] = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f":bar_chart: Stack 2026 KPI Digest — {date_nl}",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*Audience (Resend)*\n{audience_text}"},
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Pipeline 16 — Authority Leads*\n{pipeline_summary}",
            },
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*Stage distribution*\n{stage_block}"},
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*Email drip (last 24h)*\n{drip_text}"},
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"<{LANDING_URL}|recruitmentengineer.nl>  ·  run `{run_id}`",
                }
            ],
        },
    ]

    return {"blocks": blocks}


def post_to_slack(webhook: str, payload: dict[str, Any]) -> tuple[bool, str]:
    resp = requests.post(webhook, json=payload, timeout=30)
    if resp.status_code == 200 and resp.text.strip().lower() == "ok":
        return True, "ok"
    return False, f"{resp.status_code}: {resp.text[:200]}"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    global VERBOSE

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="Print payload, do not POST.")
    ap.add_argument("--verbose", action="store_true", help="Verbose debug logging.")
    args = ap.parse_args()

    VERBOSE = args.verbose

    resend_key = os.environ.get("RESEND_API_KEY", "")
    pd_token = os.environ.get("PIPEDRIVE_API_TOKEN") or os.environ.get("PIPEDRIVE_API_KEY", "")
    slack_webhook = os.environ.get("SLACK_WEBHOOK_URL", "")
    run_id = os.environ.get("GITHUB_RUN_ID", "local")

    missing = [
        name for name, val in (
            ("RESEND_API_KEY", resend_key),
            ("PIPEDRIVE_API_TOKEN", pd_token),
            ("SLACK_WEBHOOK_URL", slack_webhook if not args.dry_run else "ok"),
        ) if not val
    ]
    if missing:
        log(f"ERROR: missing env vars: {', '.join(missing)}")
        return 2

    cutoff = datetime.now(timezone.utc) - timedelta(hours=24)
    vlog(f"cutoff (24h): {cutoff.isoformat()}")

    # ---- Resend -------------------------------------------------------------
    try:
        contacts = fetch_resend_contacts(resend_key)
        audience = audience_stats(contacts, cutoff)
        vlog(f"audience: {audience}")
    except Exception as e:
        log(f"ERROR fetching Resend audience: {e}")
        audience = {"total": 0, "new_24h": 0, "unsubscribed": 0}

    # ---- Pipedrive ----------------------------------------------------------
    try:
        stages = fetch_pipeline_stages(pd_token)
        deals = fetch_pipeline_deals(pd_token)
        pipeline = pipeline_stats(deals, stages, cutoff)
        vlog(f"pipeline: open={pipeline['open']}/{pipeline['total']} "
             f"added24h={pipeline['added_24h']} updated24h={pipeline['updated_24h']}")
    except Exception as e:
        log(f"ERROR fetching Pipedrive pipeline {PIPELINE_ID}: {e}")
        stages = {}
        pipeline = {"per_stage": {}, "updated_24h": 0, "added_24h": 0, "open": 0, "total": 0}

    # ---- Drip state ---------------------------------------------------------
    state = load_drip_state()
    drip = drip_stats(state, cutoff)
    vlog(f"drip: {drip}")

    # ---- Slack --------------------------------------------------------------
    payload = build_blocks(audience, pipeline, stages, drip, run_id)

    if args.dry_run:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        log("DRY-RUN: not posted to Slack.")
        print(
            f"summary: leads={audience['total']} new24h={audience['new_24h']} "
            f"deals={pipeline['total']} open={pipeline['open']} "
            f"drip24h={sum(drip.values())} dry_run=true"
        )
        return 0

    ok, info = post_to_slack(slack_webhook, payload)
    if ok:
        log("Slack post: OK")
    else:
        log(f"Slack post FAILED: {info}")

    print(
        f"summary: leads={audience['total']} new24h={audience['new_24h']} "
        f"deals={pipeline['total']} open={pipeline['open']} "
        f"drip24h={sum(drip.values())} slack={'ok' if ok else 'fail'}"
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
