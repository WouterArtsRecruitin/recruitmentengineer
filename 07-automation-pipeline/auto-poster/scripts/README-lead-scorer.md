# Lead Scorer — Pipedrive Authority pipeline (16)

Daily cron (`.github/workflows/lead-scorer.yml`, 09:30 UTC) that re-scores
every open deal in pipeline 16 and promotes deals to a higher stage when
their score crosses a threshold.

## Stage IDs (verified live 2026-05-03)

| ID  | Name      | Score threshold |
|-----|-----------|-----------------|
| 223 | Cold      | < 30 (default)  |
| 224 | Engaged   | >= 30           |
| 225 | Discovery | >= 60           |
| 226 | Workshop  | >= 80           |

## Scoring rubric (0-100)

| Signal                                                 | Pts |
|--------------------------------------------------------|-----|
| Deal exists (had a download)                           | +15 |
| Note contains a UTM token (`utm_source`, `utm_*`)      | +5  |
| Note contains 3+ unique UTM tokens                     | +10 |
| Deal created < 14 days ago                             | +5  |
| Note content contains keyword `pipeline` (DM trigger)  | +20 |
| Person has 2+ deals in pipeline 16 (re-engagement)     | +15 |
| Each logged activity (call/email/meeting), cap +30     | +10 |

Score is capped at 100.

## Stage move rules

- Never auto-demote. If a deal sits at Discovery (225) and the score drops
  to e.g. 28, it stays at Discovery — the workflow only promotes.
- Idempotent. If a deal is already at the correct stage for its score,
  no PUT call is made.

## Auth

Pipedrive **Personal API Token** via `?api_token=` query param. Bearer
header gives 401 with personal tokens — see `PIPEDRIVE_AUTH_REGEL` in
`~/CLAUDE.md`.

## Local dry-run

```bash
cd /Users/wouterarts/projects/recruitmentengineer
source ~/recruitin/.env   # exports PIPEDRIVE_API_TOKEN
python3 07-automation-pipeline/auto-poster/scripts/lead_scorer.py --dry-run --verbose
```

Output is a JSON report on stdout:

```json
{
  "scanned": N,
  "moved": M,
  "errors": E,
  "details": [
    {
      "deal_id": 123,
      "name": "...",
      "old_stage": 223, "old_stage_name": "Cold",
      "new_stage": 224, "new_stage_name": "Engaged",
      "score": 35,
      "score_breakdown": [["baseline_download", 15], ["note_keyword_pipeline", 20]],
      "action": "promote"
    }
  ]
}
```

`action` is one of: `promote`, `skip_already_correct`, `skip_no_demote`,
`error`.

## GitHub Actions secrets needed

- `PIPEDRIVE_API_TOKEN` — 40-char hex Personal API Token
- `PIPEDRIVE_DOMAIN` — optional, defaults to `recruitin`
