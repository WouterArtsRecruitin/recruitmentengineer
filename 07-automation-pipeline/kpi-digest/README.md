# KPI digest — Stack 2026 funnel

Daily Slack digest covering the recruitmentengineer.nl Stack 2026 funnel:
audience size, Pipedrive pipeline 16 distribution, and email drip activity.

## Purpose

Give a one-glance picture every morning of:

1. **Audience growth** — Resend audience "Stack 2026 Leads" total + new (24h).
2. **Pipeline health** — Pipedrive pipeline 16 ("Authority Leads"): deals per
   stage (New Lead / PDF downloaded / Engaged / Discovery / Workshop), plus
   added/updated counts in the last 24h.
3. **Nurture activity** — mail2/3/4 sends in the last 24h, read from
   `09-launch/email-drip-state.json`.

Posted as a Slack block-kit message to the `#stack-2026` channel via
incoming webhook.

## Inputs

| Source     | Endpoint                                          | Notes                                              |
| ---------- | ------------------------------------------------- | -------------------------------------------------- |
| Resend     | `GET /audiences/<id>/contacts`                    | UA header set (default urllib hits Cloudflare 403) |
| Pipedrive  | `GET /v1/pipelines/16/deals` + `/v1/stages`       | Personal API Token via `?api_token=` (NOT Bearer)  |
| Drip state | `09-launch/email-drip-state.json`                 | Read-only; tolerates both list and dict shape      |

## Required env vars

| Name                  | Where it comes from                                |
| --------------------- | -------------------------------------------------- |
| `RESEND_API_KEY`      | GH secret · Resend dashboard                       |
| `PIPEDRIVE_API_TOKEN` | GH secret · Pipedrive Personal API Token (40-hex)  |
| `SLACK_WEBHOOK_URL`   | GH secret · webhook for `#stack-2026` (`C0AMP0SEUP5`) |
| `PIPEDRIVE_DOMAIN`    | Optional, defaults to `recruitin`                  |
| `PIPEDRIVE_PIPELINE_ID` | Optional, defaults to `16`                       |

Locally, source `~/recruitin/.env` (chmod 600).

## Commands

```bash
# Dry-run — prints the Slack payload, no POST
RESEND_API_KEY=... PIPEDRIVE_API_TOKEN=... \
  python3 07-automation-pipeline/kpi-digest/send_digest.py --dry-run --verbose

# Live — same env + SLACK_WEBHOOK_URL
python3 07-automation-pipeline/kpi-digest/send_digest.py
```

GH Actions trigger: `.github/workflows/kpi-digest.yml`, daily `0 7 * * *` UTC,
plus `workflow_dispatch` for manual runs.

## Reading the digest

- **Audience.Total** — cumulative; should only grow.
- **Audience.New (24h)** — daily lead count; benchmark against ad spend.
- **Stage distribution** — bottom-heavy (lots in 222/223) is normal early in
  the funnel. Watch for stalls — if 224 (Engaged) doesn't grow while 223 (PDF
  downloaded) keeps filling, the lead-scorer is under-promoting.
- **Email drip (24h)** — `mail2` should fire ~D+2 after a signup, `mail3` ~D+5,
  `mail4` ~D+8. Zeros early on are expected (cohorts haven't aged in yet).

## Troubleshooting

- **All zeros on Day 1** — expected. Audience may have <5 leads, no deals
  >24h old, no drip eligible yet. The digest still posts; this is the
  intended baseline.
- **`ERROR fetching Resend audience: 403`** — UA header missing or token
  rotated. Check `User-Agent` is set in `fetch_resend_contacts`.
- **`ERROR fetching Pipedrive pipeline: 401`** — wrong auth scheme. Personal
  API Tokens MUST go in `?api_token=`; Bearer fails silent here.
- **Stage IDs change** — fetched live from `/v1/stages?pipeline_id=16` each
  run, so renames in Pipedrive UI propagate automatically.
- **Slack 404 / no message** — webhook revoked or channel archived. Rotate
  via `~/recruitin/scripts/rotate_slack_webhook.sh`.
- **Drip count looks too high/low** — `send_drip.py` writes a list-shape
  state without per-mail timestamps; the digest counts list entries from a
  state file mtime'd in the last 24h. Switch the state writer to
  `{<email>: {mail2: ISO, mail3: ISO, ...}}` for precise daily counts.

## Related

- Email drip: `07-automation-pipeline/email-drip/send_drip.py`
- Lead scorer: `07-automation-pipeline/auto-poster/scripts/lead_scorer.py`
- Workflows: `.github/workflows/{email-drip,lead-scorer,kpi-digest}.yml`
