# recruitmentengineer.nl — V3.2.1 Update

**Update datum:** 15 mei 2026  
**Versie:** V3.2.1 (incremental on V3.2.0)

---

## Wat is nieuw t.o.v. V3.2.0

### 1. §02 Stack — 5 Module UI screenshots geïntegreerd

| Module | UI | Source |
|---|---|---|
| **M01 Sourcing Engine** | Boolean query / radar dashboard | `module-ui/m01-sourcing.jpg` |
| **M02 Outreach Generator** | InMail composer interface | `module-ui/m02-outreach.jpg` |
| **M03 Intake Synthesizer** | Assessment scoring matrix | `module-ui/m03-assessment.jpg` |
| **M04 Screening Score** | Placement timeline UI | `module-ui/m04-placement.jpg` |
| **M05 Pipeline Diagnostic** | Analytics performance dashboard | `module-ui/m05-analytics.jpg` |

**Technical:**
- Generated via Higgsfield Nano Banana 2 (copper/navy palette, dark UI mockups)
- Web-optimized: 4.8 MB → 480 KB total (10× smaller)
- Lazy-loaded via IntersectionObserver (300px rootMargin)
- Gradient overlay onderaan voor leesbare module-label
- Fade-in on load via `.loaded` class

### 2. §05 CTA — Backend hook actief

**Voor:** `mailto:warts@recruitin.nl` als enige route  
**Nu:**
- `POST /api/subscribe` met JSON body `{ email, source, intent }`
- Source: `recruitmentengineer-v3.2`
- Intent: `stack-2026-pdf`
- Mailto fallback bij API failure (graceful degradation)
- Email validation regex
- Button disabled tijdens submit

---

## Files

| Path | Size | Wat |
|---|---|---|
| `index.html` | ~44 KB | V3.2.1 — alles in 1 file |
| `module-ui/m01-sourcing.jpg` | 108 KB | M01 UI mockup |
| `module-ui/m02-outreach.jpg` | 56 KB | M02 UI mockup |
| `module-ui/m03-assessment.jpg` | 108 KB | M03 UI mockup |
| `module-ui/m04-placement.jpg` | 104 KB | M04 UI mockup |
| `module-ui/m05-analytics.jpg` | 96 KB | M05 UI mockup |
| `videos/*` | ~5.0 MB | 6 hero acts + 6 posters + act07 static + doc-A + doc-B |

---

## Backend vereiste voor CTA

CTA verwacht `/api/subscribe` op zelfde domein:

- **Vercel** (productie recruitmentengineer.nl): bestaand `06-landing-page/api/subscribe.js` werkt as-is → Resend + Pipedrive integratie actief
- **Netlify** preview: endpoint bestaat niet → automatische mailto fallback (geen errors)

---

## Module UI generation kosten

| Item | Credits |
|---|---|
| 5× Nano Banana 2 UI mockups | ~40 cr |
| Re-rolls | 0 (first try succes) |
| **Subtotaal V3.2.1** | **~40 cr (~€4)** |
| Cumulatief project (V2+V3+video+UI) | **~870 cr (~€95)** |

---

## Wat NIET verandert

- Hero scrollytelling (7 acts) — identiek
- §01 Manifest copy + doc-A foto
- §03 Field Report + doc-B foto
- §04 Signal testimonial placeholder (toekomstige update)
- §06 Footer + alle module-stats

---

**Owner:** Ing. W. Arts · Recruitin · warts@recruitin.nl  
**Branch:** `v3.2-hero-video` (main blijft ongewijzigd)
