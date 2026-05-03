#!/usr/bin/env python3
"""
Export Resend audience contacts to a Meta Custom Audience CSV.

Reads contacts from a Resend audience, hashes emails (SHA256, lowercased)
per Meta's spec, and writes a CSV with `email,email_sha256` columns.

Meta Ads Manager flow:
  Ads Manager -> Audiences -> Create Custom Audience -> Customer List ->
  Upload CSV -> map `email_sha256` column to Email (hashed).

Hash spec: https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences/#hash

Env:
  RESEND_API_KEY (required) - source ~/recruitin/.env

Usage:
  python3 scripts/export_audience_meta.py
  python3 scripts/export_audience_meta.py --audience <id>
  python3 scripts/export_audience_meta.py --output /tmp/audience.csv
  python3 scripts/export_audience_meta.py --no-plaintext
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import json

DEFAULT_AUDIENCE_ID = "703b9a1f-fc00-4796-8bf3-664350a89879"  # "Stack 2026 Leads"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "09-launch" / "audience-exports"
RESEND_BASE = "https://api.resend.com"


def _resend_get(path: str, api_key: str, params: dict | None = None) -> dict:
    url = f"{RESEND_BASE}{path}"
    if params:
        url = f"{url}?{urlencode(params)}"
    req = Request(url, headers={
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        # Resend sits behind Cloudflare which bans the default urllib UA.
        "User-Agent": "recruitmentengineer-audience-exporter/1.0 (+https://recruitin.nl)",
    })
    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Resend API error {e.code} on {path}: {body}") from None
    except URLError as e:
        raise SystemExit(f"Resend API connection error on {path}: {e.reason}") from None


def fetch_contacts(audience_id: str, api_key: str) -> list[dict]:
    """Fetch all contacts for the audience.

    Resend's GET /audiences/{id}/contacts currently returns a flat
    {data: [...]} list (no pagination tokens documented). We defensively
    handle a `has_more` flag with `offset` if the API ever exposes it.
    """
    contacts: list[dict] = []
    offset = 0
    while True:
        params: dict = {}
        if offset:
            params["offset"] = offset
        payload = _resend_get(
            f"/audiences/{audience_id}/contacts",
            api_key=api_key,
            params=params or None,
        )
        batch = payload.get("data") or []
        contacts.extend(batch)
        if not payload.get("has_more"):
            break
        if not batch:
            break
        offset += len(batch)
    return contacts


def hash_email(email: str) -> str:
    return hashlib.sha256(email.strip().lower().encode("utf-8")).hexdigest()


def normalize(contacts: Iterable[dict]) -> list[tuple[str, str]]:
    """Skip unsubscribed and missing emails. Returns list of (email_lower, sha256)."""
    out: list[tuple[str, str]] = []
    for c in contacts:
        if c.get("unsubscribed"):
            continue
        email = (c.get("email") or "").strip().lower()
        if not email or "@" not in email:
            continue
        out.append((email, hash_email(email)))
    return out


def write_csv(rows: list[tuple[str, str]], path: Path, include_plaintext: bool) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if include_plaintext:
            writer.writerow(["email", "email_sha256"])
            for email, h in rows:
                writer.writerow([email, h])
        else:
            writer.writerow(["email_sha256"])
            for _, h in rows:
                writer.writerow([h])
    return path.stat().st_size


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Export Resend audience to Meta Custom Audience CSV")
    p.add_argument("--audience", default=DEFAULT_AUDIENCE_ID,
                   help=f"Resend audience ID (default: {DEFAULT_AUDIENCE_ID})")
    p.add_argument("--output", default=None,
                   help="Output CSV path (default: 09-launch/audience-exports/audience-meta-YYYY-MM-DD.csv)")
    plaintext = p.add_mutually_exclusive_group()
    plaintext.add_argument("--include-plaintext", dest="include_plaintext",
                           action="store_true", default=True,
                           help="Include plaintext email column (default)")
    plaintext.add_argument("--no-plaintext", dest="include_plaintext",
                           action="store_false",
                           help="Only write the email_sha256 column")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    api_key = os.environ.get("RESEND_API_KEY")
    if not api_key:
        print("ERROR: RESEND_API_KEY not set. Run `source ~/recruitin/.env` first.",
              file=sys.stderr)
        return 1

    if args.output:
        output_path = Path(args.output).expanduser().resolve()
    else:
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        output_path = DEFAULT_OUTPUT_DIR / f"audience-meta-{date_str}.csv"

    contacts = fetch_contacts(args.audience, api_key)
    rows = normalize(contacts)
    size = write_csv(rows, output_path, include_plaintext=args.include_plaintext)

    print(f"Audience:       {args.audience}")
    print(f"Total fetched:  {len(contacts)}")
    print(f"Exported rows:  {len(rows)} (skipped {len(contacts) - len(rows)} unsubscribed/invalid)")
    print(f"Columns:        {'email,email_sha256' if args.include_plaintext else 'email_sha256'}")
    print(f"Output:         {output_path}")
    print(f"Size:           {size} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
