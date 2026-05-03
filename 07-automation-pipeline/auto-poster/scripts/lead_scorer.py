"""
Lead Scorer — Recruitment Engineer Authority pipeline.

Daily cron (GH Actions): recomputes lead_score for every deal in pipeline 16,
fetches Resend audience-events + Pipedrive notes, applies scoring formula
from `08-tracking-setup/lead-scoring-system.md`, then PATCHes Pipedrive
person + deal with new score.

STUB — not production-ready. Stage 1 implementation:
- Pipedrive deal-fetch + person-lookup ✓ scaffold
- Resend audience-events fetch ✗ TODO (Resend API doesn't expose per-contact event-log;
  alternative: parse webhook-events via local cache)
- Apollo enrichment ✗ TODO (manual for v1)
- Score calculation ✓ scaffold
- Pipedrive PATCH ✓ scaffold

Auth: Personal API Token (40-char hex), query-param style.
See PIPEDRIVE_AUTH_REGEL in ~/CLAUDE.md.
"""

import os
import sys
import json
from datetime import datetime, timezone
from urllib.parse import urlencode

import requests

# === Config ===
PIPEDRIVE_DOMAIN = os.getenv("PIPEDRIVE_DOMAIN", "recruitin")
PIPEDRIVE_API_KEY = os.getenv("PIPEDRIVE_API_KEY")
PIPEDRIVE_PIPELINE_ID = int(os.getenv("PIPEDRIVE_PIPELINE_ID", "16"))
PIPEDRIVE_LEAD_SCORE_FIELD_KEY = os.getenv("PIPEDRIVE_LEAD_SCORE_FIELD_KEY", "")
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
RESEND_AUDIENCE_ID = os.getenv("RESEND_AUDIENCE_ID")
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK_URL_RE_AUTHORITY", "")

PD_BASE = f"https://{PIPEDRIVE_DOMAIN}.pipedrive.com/api/v1"

# Stage IDs from pipedrive-pipeline-mapping.md
STAGE_COLD = 223
STAGE_ENGAGED = 224
STAGE_DISCOVERY = 225
STAGE_WORKSHOP = 226

# Score thresholds
THRESH_ENGAGED = 30
THRESH_DISCOVERY = 60
THRESH_WORKSHOP = 80


# === Pipedrive helpers ===
def pd_get(path, **params):
    params["api_token"] = PIPEDRIVE_API_KEY
    r = requests.get(f"{PD_BASE}{path}?{urlencode(params)}", timeout=30)
    r.raise_for_status()
    return r.json()


def pd_patch(path, body):
    r = requests.put(
        f"{PD_BASE}{path}?api_token={PIPEDRIVE_API_KEY}",
        json=body,
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def pd_post(path, body):
    r = requests.post(
        f"{PD_BASE}{path}?api_token={PIPEDRIVE_API_KEY}",
        json=body,
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def fetch_pipeline_deals(pipeline_id):
    """Paginated fetch of all deals in pipeline."""
    deals = []
    start = 0
    limit = 100
    while True:
        data = pd_get(
            "/deals",
            pipeline_id=pipeline_id,
            status="open",
            start=start,
            limit=limit,
        )
        items = data.get("data") or []
        deals.extend(items)
        more = data.get("additional_data", {}).get("pagination", {}).get("more_items_in_collection")
        if not more:
            break
        start += limit
    return deals


def fetch_person(person_id):
    return pd_get(f"/persons/{person_id}").get("data") or {}


def fetch_deal_notes(deal_id):
    return pd_get("/notes", deal_id=deal_id).get("data") or []


# === Resend helpers (TODO — Resend API doesn't directly expose per-contact event log) ===
def fetch_email_events_for(email):
    """STUB: Resend API doesn't have per-recipient event-log endpoint.
    Alternative paths:
    1. Parse webhook-event log from local cache / D1 / Supabase
    2. Use Resend's `/emails` endpoint with from-filter and parse event status
    3. Skip — rely on Pipedrive notes (manual) for v1
    """
    return {
        "opens": 0,
        "clicks": 0,
    }


# === Apollo enrichment (TODO — manual for v1) ===
def fetch_apollo_enrichment(email):
    """STUB: For v1, Apollo enrichment is manual via Pipedrive UI.
    For v2: integrate Apollo MCP / API directly.
    """
    return None


# === Scoring ===
def score_lead(deal, person, notes, email_events, enrichment):
    """Apply scoring formula. Returns score 0-100."""
    score = 0
    breakdown = []

    # Engagement
    score += 20
    breakdown.append(("PDF download", 20))

    open_pts = min(email_events["opens"] * 5, 15)
    if open_pts:
        score += open_pts
        breakdown.append((f"Email opens ({email_events['opens']})", open_pts))

    click_pts = min(email_events["clicks"] * 10, 20)
    if click_pts:
        score += click_pts
        breakdown.append((f"Email clicks ({email_events['clicks']})", click_pts))

    # Returning visits — count "UTM" mentions in notes (rough proxy)
    utm_notes = sum(1 for n in notes if "UTM" in n.get("content", ""))
    return_pts = min(max(utm_notes - 1, 0) * 5, 10)
    if return_pts:
        score += return_pts
        breakdown.append((f"Returning visits (~{utm_notes - 1})", return_pts))

    # LinkedIn engagement (manual tag in note: "LINKEDIN_ENGAGEMENT")
    li_count = sum(1 for n in notes if "LINKEDIN_ENGAGEMENT" in n.get("content", ""))
    li_pts = min(li_count * 10, 20)
    if li_pts:
        score += li_pts
        breakdown.append((f"LinkedIn engagement ({li_count})", li_pts))

    # Conversion
    if any("CALENDLY_CLICK" in n.get("content", "") for n in notes):
        score += 25
        breakdown.append(("Calendly click", 25))

    if any("WORKSHOP_ATTENDED" in n.get("content", "") for n in notes):
        score += 30
        breakdown.append(("Workshop attended", 30))

    # ICP-fit (Apollo)
    if enrichment:
        if enrichment.get("title") in ("HR Director", "CEO", "Chief HR Officer", "VP HR"):
            score += 15
            breakdown.append(("Title match", 15))
        size = enrichment.get("company_size", 0)
        if 50 <= size <= 800:
            score += 10
            breakdown.append(("Size match", 10))
        if enrichment.get("sector") in (
            "oil-gas", "construction", "manufacturing", "automation", "renewable"
        ):
            score += 10
            breakdown.append(("Sector match", 10))

    return min(score, 100), breakdown


def stage_for_score(score):
    if score >= THRESH_WORKSHOP:
        return STAGE_WORKSHOP
    if score >= THRESH_DISCOVERY:
        return STAGE_DISCOVERY
    if score >= THRESH_ENGAGED:
        return STAGE_ENGAGED
    return STAGE_COLD


def update_score(person_id, deal_id, new_score, breakdown):
    """PATCH person + deal with new score, append history-note."""
    if not PIPEDRIVE_LEAD_SCORE_FIELD_KEY:
        print(f"  [WARN] No PIPEDRIVE_LEAD_SCORE_FIELD_KEY set — skipping field update")
        return
    body = {PIPEDRIVE_LEAD_SCORE_FIELD_KEY: new_score}
    pd_patch(f"/persons/{person_id}", body)
    pd_patch(f"/deals/{deal_id}", body)

    # Audit-trail note
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    breakdown_str = "\n".join(f"  - {label}: +{pts}" for label, pts in breakdown)
    pd_post("/notes", {
        "deal_id": deal_id,
        "person_id": person_id,
        "content": f"[{timestamp}] Lead Score: {new_score}/100\n{breakdown_str}",
    })


def slack_notify_hot(deal, person, score, breakdown):
    """Notify on score >= 80 (Workshop stage)."""
    if not SLACK_WEBHOOK:
        return
    deal_url = f"https://{PIPEDRIVE_DOMAIN}.pipedrive.com/deal/{deal['id']}"
    msg = (
        f"🔥 HOT LEAD — {person.get('name', '?')} ({person.get('email', [{}])[0].get('value', '?')})"
        f" — score {score} — {deal_url}"
    )
    requests.post(SLACK_WEBHOOK, json={"text": msg}, timeout=10)


# === Main ===
def main():
    if not PIPEDRIVE_API_KEY:
        print("ERROR: PIPEDRIVE_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    print(f"[{datetime.now(timezone.utc).isoformat()}] Lead-scorer cron run")
    deals = fetch_pipeline_deals(PIPEDRIVE_PIPELINE_ID)
    print(f"Fetched {len(deals)} open deals in pipeline {PIPEDRIVE_PIPELINE_ID}")

    updates = 0
    hot = 0
    for deal in deals:
        person_id = deal.get("person_id", {}).get("value") if isinstance(deal.get("person_id"), dict) else deal.get("person_id")
        if not person_id:
            continue
        person = fetch_person(person_id)
        email = (person.get("email") or [{}])[0].get("value")
        if not email:
            continue
        notes = fetch_deal_notes(deal["id"])
        email_events = fetch_email_events_for(email)
        enrichment = fetch_apollo_enrichment(email)
        score, breakdown = score_lead(deal, person, notes, email_events, enrichment)

        # Compare with current score
        current = (deal.get(PIPEDRIVE_LEAD_SCORE_FIELD_KEY) or 0) if PIPEDRIVE_LEAD_SCORE_FIELD_KEY else 0
        if abs(score - current) >= 5:
            print(f"  Updating deal {deal['id']} ({email}): {current} → {score}")
            update_score(person_id, deal["id"], score, breakdown)
            updates += 1
            if score >= THRESH_WORKSHOP and current < THRESH_WORKSHOP:
                slack_notify_hot(deal, person, score, breakdown)
                hot += 1

    print(f"Done. {updates} updated, {hot} new hot leads.")


if __name__ == "__main__":
    main()
