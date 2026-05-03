# UTM Scheme — Recruitment Engineer

## Naming convention

```
?utm_source=<platform>&utm_medium=<channel>&utm_campaign=<name>&utm_content=<post-id>
```

**Rules:**
- All-lowercase, no spaces (use hyphens)
- `utm_source`: WHERE the click came from (platform)
- `utm_medium`: HOW it got there (organic, paid, email, offline)
- `utm_campaign`: WHICH campaign-bucket (high-level grouping)
- `utm_content`: WHICH specific post / asset (granular)

**Optional:** `utm_term` — only voor paid search keywords. Niet voor organic social.

---

## Per-platform table

| Platform | utm_source | utm_medium | utm_campaign | utm_content example |
|----------|------------|------------|--------------|----------------------|
| LinkedIn organic | `linkedin` | `organic` | `stack-2026-launch` | `day-1-manifesto-li` |
| LinkedIn paid (sponsored) | `linkedin` | `paid` | `stack-2026-launch` | `ad-set-1-manifesto` |
| LinkedIn DM | `linkedin` | `dm` | `stack-2026-launch` | `dm-cold-week-1` |
| Meta organic | `meta` | `organic` | `stack-2026-launch` | `reel-day-3` |
| Meta paid (FB+IG) | `meta` | `paid` | `stack-2026-launch` | `reel-pattern-interrupt-9-16` |
| Email — Resend nurture | `resend` | `email` | `stack-2026-nurture` | `mail-2-boolean` |
| Email — outbound 1:1 | `outbound` | `email` | `stack-2026-launch` | `cold-outreach-veco-week-2` |
| QR / direct (offline) | `qr` | `offline` | `stack-2026-launch` | `conferentie-recruitment-summit` |
| Direct (no UTM) | n/a | n/a | n/a | n/a — falls under Direct/None bucket |
| Pipedrive auto-followup | `pipedrive` | `automation` | `stack-2026-nurture` | `stage-engaged-followup-1` |

---

## utm_campaign buckets

| Campaign-name | Used for | Lifespan |
|---------------|----------|----------|
| `stack-2026-launch` | Day 0-14 hero posts, ads, organic launch traffic | Fase 1 |
| `stack-2026-nurture` | Email-drips, Pipedrive follow-ups | Ongoing |
| `stack-2026-retargeting` | Meta + LinkedIn retargeting voor PDF non-converters | Fase 3 |
| `stack-2026-workshop` | Workshop-inquiry CTAs (calendly clicks) | Fase 2+ |
| `re-evergreen` | Quote-cards, generic posts zonder time-binding | Ongoing |

---

## 10 voorbeeld-URLs (copy-paste)

```
1. LinkedIn manifesto post (Day 1):
https://recruitmentengineer.nl/?utm_source=linkedin&utm_medium=organic&utm_campaign=stack-2026-launch&utm_content=day-1-manifesto-li

2. LinkedIn carousel post (Day 2):
https://recruitmentengineer.nl/?utm_source=linkedin&utm_medium=organic&utm_campaign=stack-2026-launch&utm_content=day-2-carousel-pipeline

3. LinkedIn video (Day 3):
https://recruitmentengineer.nl/?utm_source=linkedin&utm_medium=organic&utm_campaign=stack-2026-launch&utm_content=day-3-video-47-prompts

4. Meta Reel (Day 4):
https://recruitmentengineer.nl/?utm_source=meta&utm_medium=organic&utm_campaign=stack-2026-launch&utm_content=day-4-reel-pattern-interrupt

5. Meta carousel (Day 5):
https://recruitmentengineer.nl/?utm_source=meta&utm_medium=organic&utm_campaign=stack-2026-launch&utm_content=day-5-carousel-leadmagnet

6. Email mail 2 — Resend nurture:
https://recruitmentengineer.nl/?utm_source=resend&utm_medium=email&utm_campaign=stack-2026-nurture&utm_content=mail-2-boolean

7. Email mail 3 — Resend nurture:
https://recruitmentengineer.nl/?utm_source=resend&utm_medium=email&utm_campaign=stack-2026-nurture&utm_content=mail-3-pipeline-case

8. QR-code op conferentie:
https://recruitmentengineer.nl/?utm_source=qr&utm_medium=offline&utm_campaign=stack-2026-launch&utm_content=conferentie-recruitment-summit

9. LinkedIn paid ad (fase 3):
https://recruitmentengineer.nl/?utm_source=linkedin&utm_medium=paid&utm_campaign=stack-2026-launch&utm_content=ad-set-1-manifesto

10. Meta retargeting ad (fase 3):
https://recruitmentengineer.nl/?utm_source=meta&utm_medium=paid&utm_campaign=stack-2026-retargeting&utm_content=reel-non-converter-9-16
```

---

## UTM-capture in pipeline

UTM's worden client-side gelezen en server-side verwerkt:

1. **Client-side** (`index.html`): bij page-load reads `URLSearchParams` van `window.location.search` → stores in `sessionStorage` (zodat ze persisteren tussen navigations binnen sessie)
2. **Form submit**: form-handler reads van sessionStorage → POSTs naar `/api/subscribe` met `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `referrer`
3. **Server-side** (`api/subscribe.js`): sanitized + cap'd op 200 chars → opgeslagen in Pipedrive deal-note onder "UTM / attribution" block (zie `subscribe.js` regel 266-288)

**LET OP:** UTM's worden NU al gecaptured maar niet als Pipedrive custom-fields, alleen als note-text. Voor strakke filtering in Pipedrive views: zie `pipedrive-pipeline-mapping.md` voor custom-field mapping (post-launch enhancement).

---

## Wat NIET te doen

- ❌ `UTM_SOURCE=LinkedIn` (caps) — gebruik all-lowercase
- ❌ `utm_campaign=Stack 2026 Launch` (spaces) — gebruik hyphens
- ❌ Verschillende `utm_campaign` waardes voor zelfde bucket (bv `stack2026` vs `stack-2026-launch`) — pick één conventie
- ❌ UTM's op interne nav-clicks binnen recruitmentengineer.nl — die maken referrer-data corrupt
- ❌ UTM's in email-onderwerp — alleen in body-links

---

## QA-script

```bash
# Verifieer dat een URL correct gevormd is
URL="https://recruitmentengineer.nl/?utm_source=linkedin&utm_medium=organic&utm_campaign=stack-2026-launch&utm_content=day-1-manifesto-li"
echo "$URL" | grep -E "utm_source=[a-z-]+&utm_medium=[a-z-]+&utm_campaign=[a-z0-9-]+&utm_content=[a-z0-9-]+"
# Should print the URL — als geen output, spelling error
```
