# Launch Checklist — Fase 1

> Synthesized from `MASTER-PLAN.md` (Day 14) + `06-hero-posts/PAD-B-LAUNCH-SCHEDULE.md` (Day 0-5).

---

## Day 0 — Pre-launch (must be 100% green before Day 1)

### Identity & assets
- [ ] Brand bible locked (see `/01-brand-bible/brand-bible.md`)
- [ ] Hero portraits delivered (10 stuks, Higgsfield Soul 2)
- [ ] LinkedIn banner chosen + uploaded (1584×396, < 8 MB, no text-clipping on mobile)
- [ ] Meta cover image ready
- [ ] Quote-card templates (5) ready
- [ ] Carousel cover templates (3) ready

### Lead magnet
- [ ] Stack 2026 PDF live at `/03-lead-magnet/stack-2026.pdf`
- [ ] All 5 prompts production-ready + tested (`/03-lead-magnet/prompts/`)
- [ ] 3 video walkthroughs rendered (Soul 2 + Seedance)
- [ ] Notion template prepared
- [ ] Email confirmation flow live (Resend, 3-mail nurture — see `email-flow.md`)

### Landing page
- [ ] Domain live: recruitmentengineer.nl
- [ ] DNS A/CNAME records propagated (see `/docs/DNS-SETUP.md`)
- [ ] Vercel deploy green (`/06-landing-page/`)
- [ ] Mobile load < 2s
- [ ] Jotform → Pipedrive webhook fires (smoke test)
- [ ] Resend delivers test email to warts@recruitin.nl
- [ ] Meta Pixel `238226887541404` installed (see `/08-tracking-setup/`)
- [ ] LinkedIn Insight Tag installed
- [ ] OG image renders correctly on LinkedIn share preview

### LinkedIn profile (Day 8 prep)
- [ ] Headline updated (220 char max, brutal-direct modus)
- [ ] About section rewritten (long, autoriteit + bewijs + CTA)
- [ ] Featured section: Stack 2026 PDF + Recruitin website + top case
- [ ] Contact info: warts@recruitin.nl + recruitin.nl + recruitmentengineer.nl
- [ ] Activity reset done

---

## Day 1 (Tuesday) — RELAUNCH

- [ ] 08:00 — Profile published (banner + headline + about + featured all live)
- [ ] 09:00 — Hero Post 1 (manifesto) published
- [ ] 09:01 — Comment 1 with landing page link posted within 60s
- [ ] 11:00 — Comment 2 (engagement question — which of 5 modules)
- [ ] Reply to ALL comments within 4h (algorithm-boost)
- [ ] DM thank-you to anyone who shares or comments meaningfully
- [ ] 3 reactions on other posts in niche within 60min after publish

**Smoke targets end of Day 1:** > 500 views, > 5 PDF downloads, > 1 Pipedrive lead.

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
- [ ] First comment with landing link within 60s
- [ ] Reply to all comments within 4h
- [ ] DM thanks to sharers
- [ ] 3 reactions on niche posts within 60min

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

---

## Owner & state

- **Owner:** Ing. W. Arts
- **Trigger conditions to start:** domain live + Resend verified + first Higgsfield banner chosen
- **Status:** scaffold — fill in checklist boxes as you progress
