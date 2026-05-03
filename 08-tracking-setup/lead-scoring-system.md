# Lead Scoring System — Authority Leads (0-100)

**Goal:** Quantify lead-quality signal so we can auto-route to right pipeline-stage and trigger Wouter's attention only for hot leads.

**Range:** 0-100 (capped, never negative)
**Field:** Pipedrive Person + Deal custom field `lead_score` (numeric)

---

## Score components

| Component | Punten | Bron | Trigger | Cap |
|-----------|--------|------|---------|-----|
| **Engagement signals** | | | | |
| PDF download | +20 | `subscribe.js` → Deal create | Auto on form-submit success | One-time |
| Email open (any) | +5 per open | Resend webhook → Pipedrive Note + score-update | Per `email.opened` event | Max +15 (3 opens) |
| Email click (any link) | +10 per click | Resend webhook → Pipedrive Note + score-update | Per `email.clicked` event | Max +20 (2 clicks) |
| Returning visit (UTM-tagged) | +5 per visit | UTM in subsequent submissions OR cookie-based session | Auto via `subscribe.js` re-submit detection | Max +10 |
| LinkedIn engagement (like/comment) | +10 | Manual tag of LinkedIn-API integration | Per engagement on Wouter's posts | Max +20 |
| **Conversion signals** | | | | |
| Workshop inquiry (Calendly click) | +25 | Pixel custom-event → Pipedrive note | Auto via CAPI fire on `calendly.com` outbound click | One-time |
| Workshop attended | +30 | Calendly webhook → Pipedrive | Auto on `calendly_event.scheduled` confirmed | One-time |
| **ICP-fit signals (manual or Apollo)** | | | | |
| Job-title match (HR Director / CEO) | +15 | Apollo enrichment | Manual on enrich | One-time |
| Company size match (50-800 FTE) | +10 | Apollo enrichment | Manual | One-time |
| Sector match (Oil&Gas / Constructie / Productie / Automation / Renewable) | +10 | Apollo enrichment | Manual | One-time |

**Theoretical max score: 165** — clamped at 100.

**Realistic distribution (calibrated against KT/DGR baselines):**
- 50% leads stuck < 30 (PDF download only, no email engagement)
- 30% leads at 30-59 (Engaged: opened + clicked)
- 15% leads at 60-79 (Discovery: ICP-fit + multiple touches)
- 5% leads at 80+ (Workshop: hot, hand-raise via Calendly)

---

## Auto-stage movement (Pipedrive Automation rules)

| Threshold | Stage move |
|-----------|------------|
| score >= 30 | Cold (223) → Engaged (224) |
| score >= 60 | Engaged (224) → Discovery (225) |
| score >= 80 | Discovery (225) → Workshop (226) + Slack notify |

**Slack notification** (score >= 80):
- Channel: `#recruitin-authority-hot` (TBD create)
- Webhook: `SLACK_WEBHOOK_URL_RE_AUTHORITY` (Vercel env)
- Format: `🔥 HOT LEAD — <name> (<email>) — score <score> — <utm_campaign>/<utm_content> — Pipedrive: <deal-url>`

---

## Implementation architecture

### Option A — GH Actions cron daily (recommended for v1)

Workflow: `.github/workflows/re-lead-scorer.yml`
- Schedule: `0 4 * * *` (04:00 UTC daily)
- Manual trigger: `workflow_dispatch`
- Steps:
  1. Checkout repo
  2. Setup Python 3.11
  3. Install deps (`requests`, `python-dateutil`)
  4. Run `scripts/lead_scorer.py`
  5. Slack-notify on errors

Script: `07-automation-pipeline/auto-poster/scripts/lead_scorer.py` (stub created — see below)

### Option B — Real-time via Resend webhook → Vercel API route

For v2 (post-launch). Setup:
- Resend → Webhooks → Add endpoint `https://recruitmentengineer.nl/api/resend-webhook`
- Sign with `RESEND_WEBHOOK_SECRET`
- On event: `email.opened` / `email.clicked` / `email.bounced`
- Vercel function: parse → look up Pipedrive person by email → fetch current score → recompute → PATCH

Skip voor v1: webhook-server-overhead niet waard zolang volume < 25 leads/week.

### Option C — Pipedrive built-in Automation (lightweight)

Pipedrive Settings → Automations → no-code rules:
- Trigger: Note created on Person → if note contains "EMAIL_CLICK" → increment `lead_score` by 10
- Trigger: Activity completed (type: email) → increment `lead_score` by 5

**Limitation:** Pipedrive Automations cannot do percentage-cap or max-N-per-day logic. Use für simple 0-3 increments only.

---

## Sample scoring-logic (Python)

See full stub in `07-automation-pipeline/auto-poster/scripts/lead_scorer.py`.

Pseudo-code:

```python
def score_lead(person_email):
    score = 0

    # Engagement
    if has_pdf_download(person_email):
        score += 20
    score += min(count_email_opens(person_email) * 5, 15)
    score += min(count_email_clicks(person_email) * 10, 20)
    score += min(count_returning_visits(person_email) * 5, 10)
    score += min(count_linkedin_engagements(person_email) * 10, 20)

    # Conversion
    if has_calendly_click(person_email):
        score += 25
    if has_workshop_attended(person_email):
        score += 30

    # ICP-fit (manual after Apollo enrichment)
    enrichment = get_apollo_enrichment(person_email)
    if enrichment:
        if enrichment.get('title') in ('HR Director', 'CEO', 'Chief HR Officer'):
            score += 15
        if 50 <= enrichment.get('company_size', 0) <= 800:
            score += 10
        if enrichment.get('sector') in ('oil-gas', 'construction', 'manufacturing', 'automation', 'renewable'):
            score += 10

    return min(score, 100)
```

---

## Score history (audit trail)

For debugging and pattern-detection, keep score-history in Pipedrive deal-notes:

```
[2026-05-04 09:23] Score: 20 (initial — PDF download)
[2026-05-04 14:15] Score: 30 (+10 — email click on mail-2)
[2026-05-05 11:42] Score: 45 (+15 — Apollo: HR Director match)
[2026-05-06 08:30] Score: 70 (+25 — Calendly click)
```

`lead_scorer.py` should append a note-entry on every score-change > 5 points.

---

## Calibration (Day 30 review)

Re-tune thresholds after first 30 days:
- If > 30% leads cluster in Engaged (224) without progressing → lower Discovery threshold to 50
- If < 5% reach Workshop (226) → lower threshold to 70 or lower Calendly-click signal to +20
- If false-positive rate (Workshop-stage but no real interest) > 20% → require BOTH Calendly-click AND email-engagement (compound rule)

Track in `09-launch/KPI-baseline.md` (add Day 30 row).
