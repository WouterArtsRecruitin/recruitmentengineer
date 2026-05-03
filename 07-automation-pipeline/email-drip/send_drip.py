#!/usr/bin/env python3
"""
Recruitment Engineering Stack 2026 — email nurture drip.

Reads the Resend audience, computes per-contact `days_since_signup`, and sends
mail2/3/4 when the contact falls into the configured day-window AND has not
already received that mail (state tracked in 09-launch/email-drip-state.json).

Usage:
    python send_drip.py                       # normal run (sends + writes state)
    python send_drip.py --dry-run             # log decisions, no sends, no state writes
    python send_drip.py --force-mail 2 --to me@example.com   # manual test send

Cron: triggered daily by .github/workflows/email-drip.yml at 09:00 UTC.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

AUDIENCE_ID = "703b9a1f-fc00-4796-8bf3-664350a89879"
FROM_EMAIL = "Wouter Arts <wouter@recruitmentengineer.nl>"
REPLY_TO = "warts@recruitin.nl"

REPO_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"
STATE_FILE = REPO_ROOT / "09-launch" / "email-drip-state.json"

RESEND_API = "https://api.resend.com"
RATE_LIMIT_SLEEP = 0.5  # seconds between sends (Resend = 2 req/s on free tier)

MAILS: list[dict[str, Any]] = [
    {
        "tag": "drip:2",
        "subject": "De fout die 90% van de recruiters maakt met boolean",
        "day_min": 1.5,
        "day_max": 2.5,
        "template": TEMPLATE_DIR / "mail2.html",
    },
    {
        "tag": "drip:3",
        "subject": "Hoe ik €519.000 stuck pipeline weer in beweging kreeg",
        "day_min": 4.5,
        "day_max": 5.5,
        "template": TEMPLATE_DIR / "mail3.html",
    },
    {
        "tag": "drip:4",
        "subject": "Wil je 30 min meedenken over je pipeline? (gratis)",
        "day_min": 7.5,
        "day_max": 8.5,
        "template": TEMPLATE_DIR / "mail4.html",
    },
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    print(f"[{ts}] {msg}", flush=True)


def load_state() -> dict[str, list[str]]:
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        log(f"WARN: state file is not valid JSON ({e}); starting empty.")
        return {}


def save_state(state: dict[str, list[str]]) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps(state, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def parse_created_at(raw: str) -> datetime:
    # Resend returns ISO-8601 with trailing 'Z' or offset.
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    return datetime.fromisoformat(raw)


def fetch_contacts(api_key: str) -> list[dict[str, Any]]:
    """Fetch all contacts in the audience, paginating if needed."""
    contacts: list[dict[str, Any]] = []
    url = f"{RESEND_API}/audiences/{AUDIENCE_ID}/contacts"
    params: dict[str, Any] = {}

    while True:
        resp = requests.get(
            url,
            headers={"Authorization": f"Bearer {api_key}"},
            params=params,
            timeout=30,
        )
        if resp.status_code != 200:
            log(f"ERROR: contacts list failed {resp.status_code}: {resp.text[:200]}")
            resp.raise_for_status()
        body = resp.json()
        batch = body.get("data") or []
        contacts.extend(batch)
        # Resend pagination: `has_more` + last id-based cursor. Fall back gracefully.
        if not body.get("has_more"):
            break
        if not batch:
            break
        params["after"] = batch[-1].get("id")
    return contacts


def send_email(
    api_key: str,
    to: str,
    subject: str,
    html: str,
    tag: str,
) -> tuple[bool, str]:
    resp = requests.post(
        f"{RESEND_API}/emails",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "from": FROM_EMAIL,
            "reply_to": REPLY_TO,
            "to": [to],
            "subject": subject,
            "html": html,
            "tags": [
                {"name": "campaign", "value": "stack-2026-leadmagnet"},
                {"name": "drip", "value": tag.replace(":", "-")},
            ],
        },
        timeout=30,
    )
    if resp.status_code in (200, 202):
        return True, resp.json().get("id", "")
    return False, f"{resp.status_code}: {resp.text[:200]}"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Log decisions, no sends, no state writes.")
    parser.add_argument("--force-mail", type=int, choices=[2, 3, 4], help="Send a specific mail right now.")
    parser.add_argument("--to", help="Email recipient for --force-mail.")
    args = parser.parse_args()

    api_key = os.environ.get("RESEND_API_KEY")
    if not api_key:
        log("ERROR: RESEND_API_KEY not set in environment.")
        return 2

    # ---- Force-mail manual path ------------------------------------------------
    if args.force_mail:
        if not args.to:
            log("ERROR: --force-mail requires --to EMAIL")
            return 2
        rule = next(r for r in MAILS if r["tag"] == f"drip:{args.force_mail}")
        html = rule["template"].read_text(encoding="utf-8")
        log(f"FORCE-SEND mail{args.force_mail} -> {args.to} (subject: {rule['subject']})")
        if args.dry_run:
            log("DRY-RUN: skipping send.")
            return 0
        ok, info = send_email(api_key, args.to, rule["subject"], html, rule["tag"])
        log(("OK " if ok else "FAIL ") + str(info))
        return 0 if ok else 1

    # ---- Normal cron path ------------------------------------------------------
    state = load_state()
    state_dirty = False
    counts = {"drip:2": 0, "drip:3": 0, "drip:4": 0}
    skipped = 0
    failures = 0

    log(f"Loading contacts from audience {AUDIENCE_ID}...")
    contacts = fetch_contacts(api_key)
    log(f"Loaded {len(contacts)} contacts. Dry-run={args.dry_run}.")

    now = datetime.now(timezone.utc)

    # Pre-load templates once
    templates = {r["tag"]: r["template"].read_text(encoding="utf-8") for r in MAILS}

    for contact in contacts:
        cid = contact.get("id")
        email = contact.get("email")
        unsubscribed = contact.get("unsubscribed", False)
        created_raw = contact.get("created_at")
        if not (cid and email and created_raw):
            continue
        if unsubscribed:
            continue
        try:
            created_at = parse_created_at(created_raw)
        except ValueError:
            log(f"WARN: cannot parse created_at={created_raw!r} for {email}; skipping.")
            continue

        days = (now - created_at).total_seconds() / 86400.0
        already = set(state.get(cid, []))

        for rule in MAILS:
            tag = rule["tag"]
            if tag in already:
                skipped += 1
                continue
            if not (rule["day_min"] <= days <= rule["day_max"]):
                continue

            log(f"-> {email} (days={days:.2f}) eligible for {tag}")
            if args.dry_run:
                # don't mutate state, don't send
                continue

            ok, info = send_email(api_key, email, rule["subject"], templates[tag], tag)
            if ok:
                counts[tag] += 1
                already.add(tag)
                state[cid] = sorted(already)
                state_dirty = True
                log(f"   sent ({info})")
            else:
                failures += 1
                log(f"   FAILED ({info})")
            time.sleep(RATE_LIMIT_SLEEP)

    if state_dirty and not args.dry_run:
        save_state(state)
        log(f"State written to {STATE_FILE}")

    log(
        "Summary: "
        f"Sent {counts['drip:2']} mail2, {counts['drip:3']} mail3, {counts['drip:4']} mail4. "
        f"Skipped {skipped} already-sent. Failures: {failures}."
    )
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
