# Fase 2 Prep — Handoff Document

> Filled in on **Day 14** based on Fase 1 actuals. Triggers Fase 2 planning sessie.

---

## 1. Status van Fase 1 KPI's per Day 14

| KPI | Target | Actual | Status |
|-----|--------|--------|--------|
| LinkedIn followers groei | +50 | — | TBD |
| Lead magnet downloads | 25 | — | TBD |
| Pipedrive Authority Leads | 10 | — | TBD |
| Hero post engagement rate | > 3% | — | TBD |

**Verdict (R/A/G):** TBD — fill in op Day 14.

If RED → diagnose-root-cause + correction-plan BEFORE fase 2 starts (zie `09-launch/launch-checklist.md` Day 7 + Day 14 diagnose).

---

## 2. Wat moet voor Fase 2 worden voorbereid

**Fase 2 scope (per MASTER-PLAN.md):**
1. **Paid scaling** — Meta Ads + LinkedIn Ads campagne setup (€1k/mnd LinkedIn + €500/mnd Meta budget)
2. **Calendly + workshop-funnel** — discovery-call booking + workshop-pricing
3. **GA4 activatie** — fase 1 SKIPPED, nu activeren met Google Tag wrapper
4. **Lead-scorer cron live** — switch van handmatig naar daily GH Actions
5. **Apollo MCP integratie** — auto-enrichment ipv handmatig
6. **Email nurture mail-3-7** — uitbouw van 3-mail naar 7-mail flow
7. **Hero post 6-15** — content-pipeline op cadance van 1 post per 2 dagen

---

## 3. Handoff-checklist

- [ ] Fase 1 KPI rapport opgeleverd (`09-launch/KPI-baseline.md` Day 14 row gevuld)
- [ ] Open issues gedocumenteerd in sectie 4 hieronder
- [ ] Lead-scorer cron stub ge-promoot naar live workflow (zie `lead_scorer.py` + GH Actions yml)
- [ ] GA4 property aangemaakt + Google Tag wrapper actief (zie `08-tracking-setup/ga4-config.md`)
- [ ] Custom field `lead_score` field-key gepropageerd naar Vercel env + GH secret
- [ ] Meta Custom Audiences > 100 leden voor LAL-creatie
- [ ] LinkedIn Insight Tag > 30 dagen actief voor retargeting-audiences
- [ ] Calendly account + workshop-product live → `CID_WORKSHOP_PLACEHOLDER` vervangen door echte conversion-ID
- [ ] CAPI server-side Lead-fire wired in `subscribe.js`
- [ ] Higgsfield + Seedance pipeline templates gevalideerd op echte content (Day 1-14 lessons learned)

---

## 4. Open issues om mee te nemen

(In te vullen op Day 14 — voorbeelden:)

- [ ] _Voorbeeld: Lighthouse SEO < 95 — fix ondertitels + alt-tags voor og-image_
- [ ] _Voorbeeld: Mobile form input zoom-bug op iOS — fix font-size 16px op input fields_
- [ ] _Voorbeeld: Resend audience first_name parsing kapt plus-tags — accepteer of fix in `emailToName()`_
- [ ] _Voorbeeld: Pipedrive deal-naam te lang voor mobile-view — truncate email-domain_

---

## 5. Fase 2 trigger

**Start fase 2 alleen ALS:**
- All 4 KPIs Fase 1 ≥ 80% van target (oranje OK, rood NIET)
- Smoke-test pipeline groen
- Open issues sectie 4 < 3 P0-bugs
- Wouter goedkeuring expliciet

---

**Owner:** Ing. W. Arts | Status: scaffold | Last updated: Day 14 (TBD)
