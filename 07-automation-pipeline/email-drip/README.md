# Email Nurture Drip — Stack 2026

Day-2 / Day-5 / Day-8 follow-up sequence for leads who downloaded the Recruitment
Engineering Stack 2026. Mail 1 (welcome + PDF) is already sent inline by
`/api/subscribe.js` on signup; this directory handles mails 2-4.

## How it works

1. GitHub Actions cron `.github/workflows/email-drip.yml` runs daily at
   **09:00 UTC**.
2. The job runs `send_drip.py`, which:
   - Lists all contacts in Resend audience `703b9a1f-fc00-4796-8bf3-664350a89879`
     (paginating via `has_more`).
   - Computes `days_since = now - created_at` per contact.
   - For each of the three mail rules (mail2 / mail3 / mail4) checks whether the
     contact lands in the day-window AND has not received that mail before.
   - Sends via Resend `POST /emails` (rate-limited 2 req/s) and logs the send
     into the state file.
3. The state file is committed back to the repo so the next cron run knows what
   was already delivered.

## Day windows

| Mail | Window           | Subject                                                              |
|------|------------------|----------------------------------------------------------------------|
| 2    | 1.5 - 2.5 days   | De fout die 90% van de recruiters maakt met boolean                  |
| 3    | 4.5 - 5.5 days   | Hoe ik €519.000 stuck pipeline weer in beweging kreeg                |
| 4    | 7.5 - 8.5 days   | Wil je 30 min meedenken over je pipeline? (gratis)                   |

Windows are 24h-wide so a once-daily cron is guaranteed to catch every contact
regardless of which hour they signed up.

## State file (load-bearing — DO commit)

`09-launch/email-drip-state.json`

```json
{
  "contact_id_abc": ["drip:2", "drip:3"],
  "contact_id_def": ["drip:2"]
}
```

This file is the **idempotency ledger**. It MUST be committed to git so each
cron run inherits the full send-history. The repo's `.gitignore` excludes
audience exports but explicitly does not exclude this state file.

If the file is lost or corrupted, contacts will receive duplicate mails on
their next eligible day. To recover: hand-build the JSON from Resend's email
log, or accept the duplicates and start fresh with `{}`.

## Running locally

```bash
# Source env + dry run (safe — no sends, no state writes)
source ~/recruitin/.env
cd /Users/wouterarts/projects/recruitmentengineer
python3 07-automation-pipeline/email-drip/send_drip.py --dry-run

# Real run (sends + persists state)
python3 07-automation-pipeline/email-drip/send_drip.py

# Manual test send (use this to verify rendering / spam score)
python3 07-automation-pipeline/email-drip/send_drip.py \
    --force-mail 2 --to warts@recruitin.nl
```

`--force-mail` does NOT update state — useful for QA without polluting the
ledger.

## Templates

`templates/mail2.html`, `mail3.html`, `mail4.html` — inline-styled HTML,
600px max-width, brand tokens: Inter, body `#1a1a1a`, accent `#FF6B1A`,
footer 12px gray. Match the look of `EMAIL_HTML` in `06-landing-page/api/subscribe.js`.

Mail 4 currently routes the CTA to a free 30-min Calendly Pipeline-check.
**TODO** (in HTML comment): swap to the €97 `/vacature-intake-mastery/`
landing page once that Tier-1 product page is live.

## Secrets

- `RESEND_API_KEY` — set as a GitHub Actions repo secret AND in `~/recruitin/.env`
  for local runs.

## Cost / Rate limits

Resend free tier = 2 req/s, 3000 emails/month. The script sleeps 0.5s between
sends. Even at 100 leads/day this finishes in ~50 seconds.
