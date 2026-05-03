# recruitmentengineer.nl

Authority-funnel voor [Wouter Arts](https://www.linkedin.com/in/wouter-arts) — Recruitin B.V. — gericht op de "Recruitment Engineering"-positionering.

## Wat zit er in deze repo

```
recruitmentengineer/
├── 01-prompts/                # 5 productie-prompts (Stack 2026 modules)
├── 02-launch-content/         # LinkedIn copy, hero-posts, brand bible, email-sequence
├── 03-lead-magnet/            # Stack 2026 PDF (12 pagina's)
├── 06-landing-page/           # Vercel deploy target — landing + serverless
│   ├── api/subscribe.js       # Resend (PDF email + audience) + Pipedrive (Person + Deal)
│   ├── index.html
│   ├── public/                # Static assets (favicon, og-image)
│   ├── stack-2026.pdf         # Lead magnet (kopie van /03-lead-magnet/)
│   ├── vercel.json
│   ├── package.json
│   └── README.md
└── docs/
    └── DNS-SETUP.md            # Metaregistrar copy-paste records
```

## Stack

- **Static landing** — single-file `index.html`, geen build-step, Inter + JetBrains Mono via Google Fonts
- **Vercel Serverless** — `/api/subscribe` (Node 20)
- **Resend** — email-send + audience-add ("Stack 2026 Leads")
- **Pipedrive** — pipeline 16 "Authority Leads — Stack 2026", deal in stage Cold (id 223) per submit
- **Brand** — orange `#FF6B1A` + blue `#1E3A5F` + cyan `#00D4FF` + warm-grey `#F5F0EB`

## Deploy state

| Stap | Status |
|------|--------|
| Repo lokaal | ✅ |
| GitHub repo (private) | ⏳ |
| Pipedrive pipeline + stages | ✅ (id 16, stages 223-226) |
| Resend domain verify | ⏳ user |
| Resend audience | ⏳ user |
| Higgsfield OG-image + LinkedIn banner | ⏳ user |
| Vercel deploy | ⏳ |
| Metaregistrar DNS (A + CNAME + Resend) | ⏳ user |
| Smoke test | ⏳ |
| LinkedIn launch (Day 1 manifesto) | ⏳ user |

## Quick links

- Landing live: https://recruitmentengineer.nl (na deploy)
- Pipedrive: https://recruitin.pipedrive.com/pipeline/16
- Resend: https://resend.com/audiences
- Vercel project: TBD na `vercel link`

## Owners

- Wouter Arts — `warts@recruitin.nl`
- Recruitin B.V. — KvK 75303647 — Doesburg
