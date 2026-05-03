# Launch Checklist — Fase 1

> Comprehensive Day 0 → Day 14 checklist. Synthesized from `MASTER-PLAN.md` (Day 14) + `06-hero-posts/PAD-B-LAUNCH-SCHEDULE.md` + `08-tracking-setup/`. **Total items: 53 pre-launch + 10 launch-day + 9 post-launch.**

---

## SECTION 1 — Domain + DNS (8 items)

- [ ] **1.1** A-record voor `recruitmentengineer.nl` → Vercel IP `76.76.21.21`
- [ ] **1.2** CNAME `www.recruitmentengineer.nl` → `cname.vercel-dns.com`
- [ ] **1.3** MX record voor `recruitmentengineer.nl` → Resend (`feedback-smtp.eu-west-1.amazonses.com` priority 10) — voor reply-to traffic + bounce-handling
- [ ] **1.4** SPF TXT record: `v=spf1 include:amazonses.com include:_spf.recruitin.nl ~all`
- [ ] **1.5** DKIM TXT records — 3 stuks (Resend genereert: `resend._domainkey`, `resend2._domainkey`, `resend3._domainkey`)
- [ ] **1.6** DMARC TXT record: `_dmarc.recruitmentengineer.nl` value `v=DMARC1; p=quarantine; rua=mailto:dmarc@recruitin.nl; pct=100`
- [ ] **1.7** DNS propagation check (24-48u after) — `dig +short recruitmentengineer.nl A` returns `76.76.21.21` from 3+ regions
- [ ] **1.8** SSL cert active in Vercel — `curl -I https://recruitmentengineer.nl` returns 200 + valid Let's Encrypt cert

---

## SECTION 2 — Resend (6 items)

- [ ] **2.1** Domain verified in Resend dashboard — all 3 DKIM keys green + SPF + Return-Path
- [ ] **2.2** Audience created: "Stack 2026 Leads" — note `RESEND_AUDIENCE_ID` (UUID v4)
- [ ] **2.3** `RESEND_AUDIENCE_ID` saved in Vercel env (Production scope) for `06-landing-page` project
- [ ] **2.4** `RESEND_API_KEY` saved in Vercel env (created via Resend → API Keys → "RE Vercel Production") — sending-permission only
- [ ] **2.5** Smoke-test send: `curl https://api.resend.com/emails -H "Authorization: Bearer $RESEND_API_KEY" -d ...` — landed in inbox + reply-to header is `warts@recruitin.nl`
- [ ] **2.6** Reply-to verify: send test mail, hit Reply, verify recipient is `warts@recruitin.nl` and not `wouter@recruitmentengineer.nl`

---

## SECTION 3 — Pipedrive (5 items)

- [ ] **3.1** Pipeline 16 "Authority Leads — Stack 2026" verified bestaat in `recruitin.pipedrive.com` (Settings → Pipelines)
- [ ] **3.2** Stage IDs verified: `223` Cold, `224` Engaged, `225` Discovery, `226` Workshop (visible via API: `GET /stages?pipeline_id=16`)
- [ ] **3.3** Custom field `lead_score` (numeric) created on Person + Deal → field-key noted in `PIPEDRIVE_LEAD_SCORE_FIELD_KEY` (Vercel env + GH secret)
- [ ] **3.4** Apollo enrichment trigger tested — pick one existing recruitin.nl lead, run Apollo, verify company-size + title fields populate
- [ ] **3.5** Sample-deal smoke-test (zie `pipedrive-pipeline-mapping.md` curl) — deal lands in Stage 223, archived after verification

---

## SECTION 4 — Tracking (10 items)

- [ ] **4.1** Meta Pixel `238226887541404` deployed in `<head>` of `index.html` — verify with Pixel Helper extension (green checkmark)
- [ ] **4.2** Meta Test Events tab — submit test form, Lead-event lands < 60s with hashed-email match-score > 80%
- [ ] **4.3** LinkedIn Insight Tag deployed — Partner ID replacement `LI_PARTNER_ID_PLACEHOLDER` → real 6-7 digit ID (per `linkedin-insight-tag.md`)
- [ ] **4.4** LinkedIn Insight Tag Helper extension — green "Tag detected" status on landing
- [ ] **4.5** GA4 SKIPPED for v1 — placeholder commented in `index.html` (verify comment-block syntactically valid, no JS error)
- [ ] **4.6** UTM scheme verified per `utm-scheme.md` — first 3 hero-posts have correct UTM tags applied
- [ ] **4.7** Conversion-events test: submit form via test-UTM URL → Pipedrive deal-note contains UTM block
- [ ] **4.8** Meta custom audience "RE — Stack 2026 Lead" created (size will populate after 24h, requires 100 members)
- [ ] **4.9** LinkedIn custom audiences placeholder created (3 stuks per `linkedin-insight-tag.md`) — populate after 30 days
- [ ] **4.10** Retargeting pixel-fire verified: open Test Events tab, scroll to 50% on landing → ViewContent fires

---

## SECTION 5 — Landing (8 items)

- [ ] **5.1** v3 design deployed — verify hero, sections 1-5, footer all render per Restructure agent's wireframe
- [ ] **5.2** OG-image present + 1200×630px PNG — verify via `https://www.opengraph.xyz/url/https%3A%2F%2Frecruitmentengineer.nl`
- [ ] **5.3** Favicon present (16×16 + 32×32 + 180×180 apple-touch) — `<link rel="icon">` resolves to 200
- [ ] **5.4** Mobile-test (iPhone Safari + Android Chrome) — hero CTA visible above-fold, form works without zoom
- [ ] **5.5** Lighthouse score > 95 (Performance + Accessibility + Best Practices + SEO) — run via `npx lighthouse https://recruitmentengineer.nl --view`
- [ ] **5.6** Dark-mode SKIPPED voor v1 (light-mode only — confirm CSS doesn't `@media (prefers-color-scheme: dark)` block visibility)
- [ ] **5.7** `prefers-reduced-motion` respected — `@media (prefers-reduced-motion: reduce)` disables animations on hero
- [ ] **5.8** Smoke-form-submit: `warts+smoke-launch@recruitin.nl` → 200 response + email arrives + Pipedrive deal created (full pipeline test, see `smoke-test-protocol.md`)

---

## SECTION 6 — Higgsfield assets (6 items)

- [ ] **6.1** OG image rendered (1200×630 — Higgsfield Marketing Studio with brand visual)
- [ ] **6.2** LinkedIn banner rendered (1584×396 — Soul 2 hero + brand wordmark)
- [ ] **6.3** Hero-portraits 10 stuks delivered in `02-higgsfield-assets/hero-portraits/` (Soul 2, identity-locked)
- [ ] **6.4** Brand visuals delivered (Nano Banana 2 — quote cards 5 + carousel covers 3 + landing-hero visual)
- [ ] **6.5** Marketing studio outputs per format — 9:16 reel cover, 1:1 feed, 16:9 LinkedIn, 4:5 Meta carousel
- [ ] **6.6** Identity-lock rules verified — clothing-style, glasses, hairstyle continuity across all 10 hero-portraits (no Soul 2 drift)

---

## SECTION 7 — LinkedIn launch (10 items)

- [ ] **7.1** LinkedIn banner uploaded (Higgsfield asset 6.2) — preview correct on mobile (no text-clipping in lower 22% safe-zone)
- [ ] **7.2** LinkedIn headline locked (220 char max, brutal-direct modus per `MASTER-PLAN.md`) — review by Wouter
- [ ] **7.3** About section updated — long-form, autoriteit + bewijs + CTA (incl. `recruitmentengineer.nl` link)
- [ ] **7.4** 3 Featured items added: (1) Stack 2026 PDF link, (2) recruitmentengineer.nl, (3) one anchor-case (Veco/Beutech/Euromaster)
- [ ] **7.5** Hero post 1 (manifesto) published Day 1 09:00 — see `06-hero-posts/post-1-linkedin-manifesto.md`
- [ ] **7.6** Comment 1 (landing-page link) posted within 60s after Hero Post 1
- [ ] **7.7** Comment 2 (engagement question — "which of 5 modules will you start with?") posted at 11:00
- [ ] **7.8** Comment 3 (engagement-boost — manual reaction on first 3 niche-posts within 60min)
- [ ] **7.9** DM-templates ready — 3 variants saved in `05-profiles/linkedin-content.md`: (a) thank-sharer, (b) reply-to-question, (c) cold-DM-template
- [ ] **7.10** Pipedrive deal-watcher active + KPI baseline captured — open `KPI-baseline.md`, fill Day 0 baseline numbers (followers count, profile views from last 30d, etc.)

---

## SECTION 8 — Day 1 Launch (10 items)

- [ ] **8.1** 08:00 — Profile published (banner + headline + about + featured all live, screenshot saved as Day 0 baseline)
- [ ] **8.2** 09:00 — Hero Post 1 (manifesto) published
- [ ] **8.3** 09:01 — Comment 1 with landing page link posted within 60s (UTM: `utm_source=linkedin&utm_medium=organic&utm_campaign=stack-2026-launch&utm_content=day-1-manifesto-li`)
- [ ] **8.4** 11:00 — Comment 2 (engagement question)
- [ ] **8.5** Reply to ALL comments within 4h (algorithm-boost window)
- [ ] **8.6** DM thank-you to anyone who shares or comments meaningfully
- [ ] **8.7** 3 reactions on other posts in niche within 60min after publish
- [ ] **8.8** End-of-day check: views > 500, PDF downloads > 5, Pipedrive leads > 1
- [ ] **8.9** Slack `#recruitin-authority-hot` channel monitored — react to any Workshop-stage notification within 1h
- [ ] **8.10** Day 1 evening — fill `KPI-baseline.md` Day 1 row with actuals

---

## Day 2-5 — Content cadence

| Day | Post | Time | Key check |
|-----|------|------|-----------|
| Day 2 (Wed) | Hero Post 2 — €519k story | 17:30 | Comment 1 link posted in 60s |
| Day 3 (Thu) | Hero Post 3 — Boolean tip | 08:00 | Engagement reply within 4h |
| Day 4 (Fri) | Hero Post 4 — Contrarian take | 09:00 | Polarisatie OK, beledigend NIET |
| Day 5 (Mon) | Hero Post 5 — Day 1-4 results | 08:00 | Honest numbers, no inflation |

**Per-post checklist** (every day):
- [ ] Publish at scheduled time
- [ ] First comment with landing link within 60s (with correct UTM)
- [ ] Reply to all comments within 4h
- [ ] DM thanks to sharers
- [ ] 3 reactions on niche posts within 60min

---

## SECTION 9 — Post-launch (Day 1 evening + Day 2-7) — 9 items

- [ ] **9.1** Day 1 evening — capture screenshots of Hero Post 1 metrics (views, reactions, comments) for trend baseline
- [ ] **9.2** Day 2 09:00 — review Day 1 numbers vs targets in `KPI-baseline.md`. If views < 500 → diagnose algorithm-suppression, engage on 5 niche-posts before Day 2 publish
- [ ] **9.3** Day 2-5 — daily 18:00 KPI capture (views/reactions/PDF-DLs/leads) into per-post tracking table
- [ ] **9.4** Day 3 — first lead-scorer cron run (manual trigger via `gh workflow run re-lead-scorer.yml`) — verify scores update in Pipedrive
- [ ] **9.5** Day 5 — Apollo enrichment manueel runnen voor alle Discovery-stage leads (>= 60 score)
- [ ] **9.6** Day 7 — first-week review: KPI-baseline.md Day 7 column filled, diagnose any red metrics per `launch-checklist.md` diagnose-table
- [ ] **9.7** Day 7 — DM-outreach 5 high-engagement non-converters (commented but didn't download)
- [ ] **9.8** Day 14 — final Fase 1 KPI review against MASTER-PLAN targets — fill `09-launch/KPI-baseline.md` "End of Fase 1" row
- [ ] **9.9** Day 14 — handoff doc `10-handoff/fase-2-prep.md` filled in with status, open issues, fase 2 prep tasks

---

## Day 7 — First-week review

### KPI check vs `KPI-baseline.md`
- [ ] Total post views (target: 5.000+)
- [ ] Total reactions (target: 200+)
- [ ] New followers (target: 20+)
- [ ] PDF downloads (target: 50+)
- [ ] Pipedrive leads (target: 5+)

### Diagnose if targets missed
- Views < 2.000 → algorithm suppression. Engage earlier on other posts.
- Followers < 10 → headline/banner unclear. Revise.
- Downloads < 20 → CTA in posts too weak. Make explicit.
- Leads < 2 → landing page conversion issue. A/B test.

---

## Day 14 — End of fase 1

### Hard KPIs (per MASTER-PLAN)
- [ ] LinkedIn followers +50 (vs Day 0 baseline)
- [ ] Lead magnet downloads: 25
- [ ] Pipedrive Authority Leads: 10
- [ ] Hero post engagement rate > 3%

### Deliverables check
- [ ] Automation pipeline working (`/07-automation-pipeline/`)
- [ ] Ad Generator Agent (React artifact) tested
- [ ] Higgsfield templates locked
- [ ] Seedance pipeline tested with 3 scenes
- [ ] Notion calendar + Zapier auto-poster live
- [ ] Meta Ads MCP + LinkedIn Ads MCP integrated
- [ ] KPI baseline dashboard live (`KPI-baseline.md`)
- [ ] Handoff document for fase 2 prepared

**If KPIs missed → diagnose + correct BEFORE starting fase 2.**

---

## Fallbacks

| Failure | Fallback |
|---------|----------|
| Banner not right from Higgsfield | Make in Canva (15 min, free template "LinkedIn Banner") |
| Day 1 post < 500 views after 2h | DM 5 close connections for feedback, react on 5 niche posts |
| No PDF downloads after Day 1 | Test landing on mobile, test form flow with test email, check Resend delivery logs |
| Pipedrive webhook silent | Re-send test from Jotform, verify webhook URL, check pipeline-stage trigger |
| Lead-scorer cron failing | Run `lead_scorer.py` locally with `PIPEDRIVE_API_KEY` from .env, check stdout for HTTP errors |
| Slack hot-lead notify silent | Verify `SLACK_WEBHOOK_URL_RE_AUTHORITY` env-var set, smoke-test via curl POST |

---

## Owner & state

- **Owner:** Ing. W. Arts
- **Trigger conditions to start:** domain live + Resend verified + first Higgsfield banner chosen
- **Status:** scaffold — fill in checklist boxes as you progress
- **Total items:** 53 pre-launch + 10 launch-day + 9 post-launch = **72 items**
