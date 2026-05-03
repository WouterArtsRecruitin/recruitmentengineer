# 08-tracking-setup

**Status:** v1 launch — minimal tracking. GA4 deliberately skipped for first launch wave to avoid GA4-orphan issues (see `GA4_ORPHAN_MID_REGEL` in main `~/CLAUDE.md`). Add later once we have first 100 leads and need attribution depth.

## What we DO have on launch

| Tracker | Status | Notes |
|---------|--------|-------|
| Pipedrive lead capture | LIVE | Jotform → Pipedrive via webhook (Recruitin pipeline) |
| Resend transactional email | LIVE | Lead-magnet delivery + nurture flow (`/03-lead-magnet/email-flow.md`) |
| UTM conventions | TODO | Document standard UTM tags per channel before first ad spend |
| Meta Pixel | TBD | Use shared Recruitin pixel `238226887541404` (same one used on DGR/KT/APK/VK). Don't init on FB Page ID `660118697194302` — that's silent fail (see `feedback_meta_pixel_vs_page_id.md`) |
| LinkedIn Insight Tag | TBD | Required for LinkedIn Ads retargeting in fase 3 |
| GA4 | SKIPPED for v1 | Add in fase 2 once we have first 100 leads and attribution patterns matter |

## TODO before fase 1 launch

- [ ] Document UTM conventions in `utm-conventions.md`
  - `utm_source`: linkedin / meta / email / direct
  - `utm_medium`: organic / paid / nurture
  - `utm_campaign`: stack-2026 / fase1-launch / hero-post-N
  - `utm_content`: post-1-manifesto / post-2-pipeline / etc.
- [ ] Install Meta Pixel `238226887541404` on landing page (06-landing-page)
- [ ] Install LinkedIn Insight Tag on landing page
- [ ] Verify Pipedrive webhook fires on every Jotform submit (smoke test)
- [ ] Set up Pipedrive "Authority Leads" pipeline + first 4 stages

## TODO fase 2 (post-launch)

- [ ] GA4 setup with proper Google Tag wrapper (NOT bare measurement ID — see `GA4_ORPHAN_MID_REGEL`)
- [ ] Cross-domain config: recruitmentengineer.nl + recruitin.nl + landing variants
- [ ] Internal traffic filter: home IP `217.62.161.195/32`
- [ ] Conversion events: `generate_lead` on form submit, `pdf_download` on Stack 2026 fetch
- [ ] Server-side Measurement Protocol fallback (consent-blocked browsers)

## Files in this folder (TBD)

- `utm-conventions.md`
- `meta-pixel-config.md`
- `linkedin-insight.md`
- `ga4-config.md` (fase 2)
- `pipedrive-pipeline.md`
