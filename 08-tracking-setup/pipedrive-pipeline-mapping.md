# Pipedrive Pipeline Mapping — Authority Leads

## Pipeline 16 — "Authority Leads — Stack 2026"

**Pipeline ID:** `16`
**Domain:** `recruitin.pipedrive.com`
**Auth:** Personal API Token (40-char hex, query-param `?api_token=...` — see `PIPEDRIVE_AUTH_REGEL`)

---

## Stages

| Stage ID | Name | Score-threshold | Description |
|----------|------|-----------------|-------------|
| `223` | Cold | 0-29 | New PDF download, no engagement signals yet |
| `224` | Engaged | 30-59 | Opened email + clicked OR returning visitor with UTM |
| `225` | Discovery | 60-79 | Multiple engagement-touches, ready voor outbound DM/call |
| `226` | Workshop | 80+ | Calendly clicked OR explicit workshop-inquiry — Wouter notify |

**Default stage on creation:** `223` (Cold).

---

## Field-mapping: Resend ↔ Pipedrive Person ↔ Pipedrive Deal

| Source field | Resend Audience | Pipedrive Person | Pipedrive Deal | Notes |
|--------------|-----------------|------------------|----------------|-------|
| Email | `email` (primary key) | `email[0].value` (label `work`) | n/a | Person-key |
| First name | `first_name` | `name` (auto-derived from email-local) | n/a | `emailToName(email)` in `subscribe.js` |
| UTM source | n/a | n/a | Note `utm_source` | Block in deal-note |
| UTM medium | n/a | n/a | Note `utm_medium` | Block in deal-note |
| UTM campaign | n/a | n/a | Note `utm_campaign` | Block in deal-note |
| UTM content | n/a | n/a | Note `utm_content` | Block in deal-note |
| Referrer | n/a | n/a | Note `referrer` | Block in deal-note |
| Source | tag (`source: landing`) | n/a | Title `Stack 2026 download — <email>` | Embedded in deal-title |
| Lead Score | n/a | Custom field `lead_score` (numeric) | Custom field `lead_score` (numeric) | Synced from scorer-cron |
| Engagement events | Webhook event-log | n/a | Activities (note per event) | `email.opened`, `email.clicked` etc. |

**LET OP:** Custom fields `lead_score` (Person + Deal) moeten **handmatig aangemaakt** worden in Pipedrive Settings → Data fields → Persons / Deals → "+ Custom field" → Numeric. Field-key wordt auto-gegenereerd (bv `9b9af9b8d8...`). Save de field-key in Vercel env als `PIPEDRIVE_LEAD_SCORE_FIELD_KEY` voor scorer-cron.

---

## Auto-stage movement triggers

Triggered by lead-scoring system (zie `lead-scoring-system.md`):

```
Score change                           → Stage move
─────────────────────────────────────────────────────────
PDF download created (initial)         → Stage 223 (Cold), score 20
Email open detected (Resend webhook)   → score +5 (max +15)
Email click detected (Resend webhook)  → score +10 (max +20)
                                       → Score >= 30: move to Stage 224 (Engaged)
Returning visit with UTM               → score +5
                                       → Score >= 60: move to Stage 225 (Discovery)
Calendly click detected (CAPI custom)  → score +25
                                       → Score >= 80: move to Stage 226 (Workshop)
                                       → Trigger Slack notification to Wouter
Workshop attended                      → score +30
                                       → Stay in Stage 226, add note "WORKSHOP DONE"
```

---

## Lead Score updates — implementation paths

### Path A — Pipedrive built-in Automation (recommended for v1)

Pipedrive Settings → Automations → Create automation:

**Automation 1: Cold → Engaged (score >= 30)**
- Trigger: Person updated → field `lead_score` changed
- Filter: `lead_score >= 30 AND deal.stage_id == 223`
- Action: Move associated deals to stage `224`

**Automation 2: Engaged → Discovery (score >= 60)**
- Trigger: Person updated → `lead_score` changed
- Filter: `lead_score >= 60 AND deal.stage_id == 224`
- Action: Move deals to stage `225`

**Automation 3: Discovery → Workshop (score >= 80)**
- Trigger: Person updated → `lead_score` changed
- Filter: `lead_score >= 80 AND deal.stage_id IN (223, 224, 225)`
- Action: Move deals to stage `226` + send Slack via webhook

### Path B — GH Actions cron (recompute daily)

Cron `.github/workflows/lead-scorer.yml` runs daily at 04:00 UTC:
1. Fetch all Pipedrive deals in pipeline 16 (paginated)
2. For each deal: fetch associated Resend audience-events (last 30 days)
3. Compute new score per `lead-scoring-system.md` formula
4. PATCH Pipedrive person + deal with new `lead_score`
5. Pipedrive Automation rules (Path A) move stages automatically

Stub: `07-automation-pipeline/auto-poster/scripts/lead_scorer.py`

---

## Deal-creation flow (current state, `subscribe.js`)

```
POST /api/subscribe
    ↓
Resend send email + add to audience
    ↓
Pipedrive: search person by email
    ↓ (not found)
Pipedrive: create person
    ↓
Pipedrive: create deal in pipeline 16, stage 223 (Cold)
    ↓
Pipedrive: add note with UTM-block
    ↓
Return success → client-side fbq('Lead'), lintrk('PDF_Download'), gtag('generate_lead')
```

**Currently NOT set in `subscribe.js`:**
- `lead_score = 20` op deal create — needs custom field key in env, then add to `dealBody`
- `pipeline_id = 16` — comes from env `PIPEDRIVE_PIPELINE_ID`
- `stage_id = 223` — comes from env `PIPEDRIVE_STAGE_ID`

**Required Vercel env-vars (verify):**
- `PIPEDRIVE_API_KEY` — Personal Token, 40-char hex
- `PIPEDRIVE_DOMAIN` — `recruitin` (default)
- `PIPEDRIVE_PIPELINE_ID` — `16`
- `PIPEDRIVE_STAGE_ID` — `223`
- `PIPEDRIVE_LEAD_SCORE_FIELD_KEY` — auto-gen by Pipedrive after custom-field create
- `SLACK_WEBHOOK_URL_RE_AUTHORITY` — voor Workshop-stage notifications (separate channel from KT/DGR)

---

## Apollo enrichment (manual, post-creation)

Voor leads die in Stage 224+ komen, run Apollo enrichment manueel:

1. Open deal in Pipedrive
2. Trigger Apollo workflow (Pipedrive Apollo MCP integration)
3. Apollo fills:
   - `company_name`, `company_size`, `company_industry`
   - `job_title`, `seniority`
   - LinkedIn URL
4. Score adjustments per `lead-scoring-system.md`:
   - Title match (HR Director / CEO): +15
   - Company size match (50-800 FTE): +10
   - Sector match (Oil&Gas/Constructie/Productie/Automation/Renewable): +10

Total possible "fit-score" boost: **+35 points** — pushes engaged leads to Discovery quickly.

---

## Sample-deal smoke-test (cleanup after)

```bash
curl -X POST https://recruitin.pipedrive.com/api/v1/deals?api_token=$PIPEDRIVE_API_KEY \
  -H "Content-Type: application/json" \
  -d '{
    "title": "SMOKE-TEST — Stack 2026 download — smoke@test.com",
    "pipeline_id": 16,
    "stage_id": 223,
    "status": "open",
    "visible_to": 3
  }'
```

Verify in UI → archive immediately after.
