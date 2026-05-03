# 04-landing-page (planning spec)

**Note on layout:** the live deploy lives at `/06-landing-page/` for legacy reasons — the Vercel project is linked to that path and renaming it would break the deploy. Treat this folder (`/04-landing-page/`) as the **planning spec** (briefs, copy variants, A/B test ideas, conversion notes) and `/06-landing-page/` as the **deploy target** (Next.js project + Vercel).

## Where things live

| What | Where |
|------|-------|
| Live deploy (Vercel) | `/06-landing-page/` |
| DNS setup notes | `/docs/DNS-SETUP.md` |
| OG image brief | `/02-higgsfield-assets/OG-IMAGE-BRIEF.md` |
| Hero copy / value prop iteration | here (TODO) |
| Landing page conversion tests | here (TODO) |

## Open TODOs (planning)

- [ ] Document current hero copy + 3 alternative hooks for A/B testing
- [ ] Conversion baseline measurements (Day 1-7 after launch)
- [ ] Mobile vs desktop conversion split
- [ ] Form flow audit: Jotform → Pipedrive → Resend
- [ ] Add LinkedIn Insight Tag (see `/08-tracking-setup/`)

## Why two folders?

Per master-plan layout the landing page belongs at `/04-landing-page/`. But the Vercel project ID + linked git path is on `/06-landing-page/` (initial commit `f59e835`). Renaming would require a fresh Vercel project link + DNS revalidation — not worth the risk for cosmetic consistency. Keep both: 04 = planning, 06 = deploy.
