"""
Lead Scorer — Recruitment Engineer Authority pipeline (Pipedrive 16).

Scoring rubric (0-100):
  +15  baseline (deal exists -> had a download)
  +5   note contains a UTM (`utm_source` or `UTM` block)
  +10  note contains >=3 UTM tokens (deeply tagged campaign visit)
  +5   deal_created < 14 days ago
  +20  note content mentions `pipeline` (engaged via DM)
  +15  person has 2+ deals in pipeline 16 (re-engagement)
  +10  per logged activity (call/email/meeting), capped at +30

Stage promotion thresholds:
  >=80 -> 226 Workshop
  >=60 -> 225 Discovery
  >=30 -> 224 Engaged
   <30 ->  stay at 223 Cold

Never auto-demote. If current stage > target stage, leave deal alone.

Auth: Pipedrive Personal API Token via `?api_token=` query param.
See PIPEDRIVE_AUTH_REGEL in ~/CLAUDE.md.

CLI:
  python3 lead_scorer.py --dry-run --verbose
  python3 lead_scorer.py --verbose         # live, will PUT stage moves
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from urllib.parse import urlencode

import requests

# --- Config ---
PIPEDRIVE_DOMAIN = os.getenv("PIPEDRIVE_DOMAIN", "recruitin")
PIPEDRIVE_API_TOKEN = (
    os.getenv("PIPEDRIVE_API_TOKEN")
    or os.getenv("PIPEDRIVE_API_KEY")
    or ""
)
PIPELINE_ID = int(os.getenv("PIPEDRIVE_PIPELINE_ID", "16"))

PD_BASE = f"https://{PIPEDRIVE_DOMAIN}.pipedrive.com/api/v1"

# Stage IDs — verified live 2026-05-03 against pipeline 16
STAGE_COLD = 223
STAGE_ENGAGED = 224
STAGE_DISCOVERY = 225
STAGE_WORKSHOP = 226

STAGE_NAMES = {
    STAGE_COLD: "Cold",
    STAGE_ENGAGED: "Engaged",
    STAGE_DISCOVERY: "Discovery",
    STAGE_WORKSHOP: "Workshop",
}

THRESH_ENGAGED = 30
THRESH_DISCOVERY = 60
THRESH_WORKSHOP = 80

UTM_RE = re.compile(r"utm_[a-z]+", re.IGNORECASE)


# --- Pipedrive HTTP helpers (Personal Token via query param) ---
def pd_get(path, **params):
    params["api_token"] = PIPEDRIVE_API_TOKEN
    r = requests.get(f"{PD_BASE}{path}?{urlencode(params)}", timeout=30)
    r.raise_for_status()
    return r.json()


def pd_put(path, body):
    r = requests.put(
        f"{PD_BASE}{path}?api_token={PIPEDRIVE_API_TOKEN}",
        json=body,
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def fetch_pipeline_deals(pipeline_id):
    """Paginated fetch of all deals in a pipeline.

    NOTE: `/v1/deals?pipeline_id=X` silently ignores the filter and returns
    deals from every pipeline. The reliable way to get only-this-pipeline
    deals is `/v1/pipelines/{id}/deals`.
    """
    deals = []
    start = 0
    limit = 100
    while True:
        data = pd_get(
            f"/pipelines/{pipeline_id}/deals",
            start=start,
            limit=limit,
        )
        items = data.get("data") or []
        # Defensive: only keep open deals (status field on every deal)
        deals.extend(d for d in items if d.get("status") == "open")
        more = (
            data.get("additional_data", {})
            .get("pagination", {})
            .get("more_items_in_collection")
        )
        if not more:
            break
        start += limit
    return deals


def fetch_deal_notes(deal_id):
    return pd_get("/notes", deal_id=deal_id, limit=100).get("data") or []


def fetch_deal_activities(deal_id):
    return pd_get("/activities", deal_id=deal_id, limit=100).get("data") or []


def count_person_deals_in_pipeline(person_id, pipeline_id):
    """Count deals (open + closed) for this person inside pipeline_id."""
    if not person_id:
        return 0
    data = pd_get(f"/persons/{person_id}/deals", limit=100)
    items = data.get("data") or []
    return sum(1 for d in items if d.get("pipeline_id") == pipeline_id)


# --- Scoring ---
def parse_add_time(s):
    if not s:
        return None
    # Pipedrive returns "YYYY-MM-DD HH:MM:SS" UTC
    try:
        return datetime.strptime(s, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def score_deal(deal, notes, activities, person_deal_count):
    """Return (score, breakdown_list)."""
    score = 0
    breakdown = []

    # Baseline: deal exists -> had a download
    score += 15
    breakdown.append(("baseline_download", 15))

    # UTM presence in any note
    note_blob = "\n".join((n.get("content") or "") for n in notes)
    utm_tokens = UTM_RE.findall(note_blob)
    unique_utms = {t.lower() for t in utm_tokens}
    if unique_utms:
        score += 5
        breakdown.append(("utm_present", 5))
        if len(unique_utms) >= 3:
            score += 10
            breakdown.append((f"utm_multi_{len(unique_utms)}", 10))

    # Recency: <14 days
    add_time = parse_add_time(deal.get("add_time"))
    if add_time:
        age_days = (datetime.now(timezone.utc) - add_time).days
        if age_days < 14:
            score += 5
            breakdown.append((f"recent_{age_days}d", 5))

    # Pipeline keyword in any note
    if any("pipeline" in (n.get("content") or "").lower() for n in notes):
        score += 20
        breakdown.append(("note_keyword_pipeline", 20))

    # Returning lead: 2+ deals in pipeline 16
    if person_deal_count >= 2:
        score += 15
        breakdown.append((f"reengaged_{person_deal_count}deals", 15))

    # Logged activities: +10 each, cap +30
    activity_pts = min(len(activities) * 10, 30)
    if activity_pts:
        score += activity_pts
        breakdown.append((f"activities_{len(activities)}", activity_pts))

    return min(score, 100), breakdown


def stage_for_score(score):
    if score >= THRESH_WORKSHOP:
        return STAGE_WORKSHOP
    if score >= THRESH_DISCOVERY:
        return STAGE_DISCOVERY
    if score >= THRESH_ENGAGED:
        return STAGE_ENGAGED
    return STAGE_COLD


# --- Main ---
def main():
    ap = argparse.ArgumentParser(description="Pipedrive lead scorer for pipeline 16.")
    ap.add_argument("--dry-run", action="store_true", help="Compute only, no PUT calls.")
    ap.add_argument("--verbose", action="store_true", help="Verbose per-deal logging.")
    args = ap.parse_args()

    if not PIPEDRIVE_API_TOKEN:
        print("ERROR: PIPEDRIVE_API_TOKEN not set", file=sys.stderr)
        sys.exit(1)

    if args.verbose:
        print(
            f"[lead-scorer] domain={PIPEDRIVE_DOMAIN} pipeline={PIPELINE_ID} "
            f"stages={STAGE_NAMES} dry_run={args.dry_run}"
        )

    deals = fetch_pipeline_deals(PIPELINE_ID)
    if args.verbose:
        print(f"[lead-scorer] fetched {len(deals)} open deals")

    report = {"scanned": 0, "moved": 0, "errors": 0, "details": []}

    for deal in deals:
        report["scanned"] += 1
        deal_id = deal["id"]
        try:
            person_id = (
                deal.get("person_id", {}).get("value")
                if isinstance(deal.get("person_id"), dict)
                else deal.get("person_id")
            )
            notes = fetch_deal_notes(deal_id)
            activities = fetch_deal_activities(deal_id)
            person_deal_count = count_person_deals_in_pipeline(person_id, PIPELINE_ID)

            score, breakdown = score_deal(deal, notes, activities, person_deal_count)
            current_stage = deal.get("stage_id")
            target_stage = stage_for_score(score)

            entry = {
                "deal_id": deal_id,
                "name": deal.get("title"),
                "old_stage": current_stage,
                "old_stage_name": STAGE_NAMES.get(current_stage, str(current_stage)),
                "new_stage": current_stage,
                "new_stage_name": STAGE_NAMES.get(current_stage, str(current_stage)),
                "score": score,
                "score_breakdown": breakdown,
                "action": "skip_already_correct",
            }

            if target_stage == current_stage:
                if args.verbose:
                    print(f"  deal {deal_id} score={score} stage={current_stage} (no move)")
            elif target_stage < current_stage:
                # Never auto-demote
                entry["action"] = "skip_no_demote"
                if args.verbose:
                    print(
                        f"  deal {deal_id} score={score} would demote "
                        f"{current_stage}->{target_stage} — skipped"
                    )
            else:
                entry["new_stage"] = target_stage
                entry["new_stage_name"] = STAGE_NAMES.get(target_stage, str(target_stage))
                entry["action"] = "promote"
                if args.dry_run:
                    if args.verbose:
                        print(
                            f"  [dry] deal {deal_id} score={score} "
                            f"{current_stage}->{target_stage}"
                        )
                else:
                    pd_put(f"/deals/{deal_id}", {"stage_id": target_stage})
                    if args.verbose:
                        print(
                            f"  deal {deal_id} score={score} "
                            f"PROMOTED {current_stage}->{target_stage}"
                        )
                report["moved"] += 1

            report["details"].append(entry)
        except Exception as e:
            report["errors"] += 1
            report["details"].append(
                {"deal_id": deal_id, "error": str(e), "action": "error"}
            )
            if args.verbose:
                print(f"  deal {deal_id} ERROR: {e}", file=sys.stderr)

    print(json.dumps(report, indent=2, default=str))
    print(
        f"[lead-scorer] summary: scanned={report['scanned']} "
        f"moved={report['moved']} errors={report['errors']} "
        f"dry_run={args.dry_run}"
    )


if __name__ == "__main__":
    main()
