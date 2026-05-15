# V3.2 — Hero Video Scrollytelling

> Status: **Live preview op `dashing-unicorn-22ba22.netlify.app`**. NIET de huidige productie-site (`recruitmentengineer.nl` = `06-landing-page/public/index.html` op Vercel). Dit is een experimenteel design dat de bestaande V3.1-narratief uitbreidt met een 7-act animated hero.

---

## Wat is nieuw t.o.v. de bestaande site

| Aspect | Huidig (`06-landing-page/`) | V3.2 (`12-v3.2-hero-video/`) |
|--------|-----------------------------|------------------------------|
| Hero | Statisch | **7-act scrollytelling** (6 video loops + 1 static finale) |
| Narratief | "Recruitment engineer" positioning | **Genesis-arc**: Oerknal → Eerste Principes → Industrieel → Tekenplank → Lopende Band → Digitaal → De Stack |
| Visual stijl | Orange `#FF6B1A` + blue `#1E3A5F` | Dark `#0a0908` + copper `#d97706` |
| Typografie | Inter + JetBrains Mono | Inter + **Instrument Serif** (italic accenten) + JetBrains Mono |
| Portretten | Geen | doc-A (raffinaderij, Oil & Gas) + doc-B (bouwplaats, Construction) |
| Stack modules | Korte features-rij | **M01-M05 detail** met stats: 25min · 41% · 5,3× · 87/100 · €519k |
| Case study | Generiek | **Veco HSE Engineer** — 11 dagen, €519k recovered, 60% recovery rate |
| Total payload | ~50 KB HTML + 6.5 MB assets | 42 KB HTML + 5.6 MB assets |

---

## Bestanden in deze folder

```
12-v3.2-hero-video/
├── README.md                    (dit bestand)
├── index.html                   42 KB — single-file, no build step
└── videos/                      5.5 MB totaal
    ├── act01_oerknal_observatorium.mp4         779 KB
    ├── act01_oerknal_observatorium_poster.jpg   78 KB
    ├── act02_eerste_principes_cave.mp4         992 KB
    ├── act02_eerste_principes_cave_poster.jpg  119 KB
    ├── act03_industrieel_stoom.mp4            1.0 MB
    ├── act03_industrieel_stoom_poster.jpg      81 KB
    ├── act04_tekenplank_blueprint.mp4          480 KB
    ├── act04_tekenplank_blueprint_poster.jpg   73 KB
    ├── act05_lopende_band_assembly.mp4         652 KB
    ├── act05_lopende_band_assembly_poster.jpg  66 KB
    ├── act06_digitaal_crt.mp4                  661 KB
    ├── act06_digitaal_crt_poster.jpg           59 KB
    ├── act07_destack_static.jpg                168 KB  (FINAL REVEAL — static)
    ├── doc-A-refinery.jpg                      208 KB  (§01 Manifest portrait)
    └── doc-B-construction.jpg                  160 KB  (§03 Field Report portrait)
```

Alle videos: h264, 720p, 10s loop, no audio, web-optimized (CRF 30, faststart, mobile-friendly).

---

## Site structuur (sections)

| § | Sectie | Inhoud |
|---|--------|--------|
| HERO | 7-act scrollytelling | IntersectionObserver-driven act-progression, smart play/pause (alleen actieve video speelt), progress dots rechts, iOS autoplay-safe |
| §01 | Manifest | "Recruitment is een *engineering vak.*" + 3 alinea's met €519k claim |
| §02 | The Stack | M01 Sourcing · M02 Outreach · M03 Intake · M04 Screening · M05 Pipeline — elk met stats + UI placeholder tegels |
| §03 | Field Report | Veco case: 11 dagen · €519k recovered · 60% rate · 3.6× SLA + pull-quote |
| §04 | Signal | Anonieme testimonial mid-market industrieel |
| §05 | CTA | Email capture → Stack 2026 PDF (mailto fallback) |
| §06 | Footer | REC-ENG-001 doc-meta + contact + network |

---

## Productie credits

- **6 video clips**: Seedance 2.0 (image-to-video) — ~270 cr ≈ €30
- **3 frame regens**: Nano Banana 2 (1k) — 6 cr ≈ €0.50
- **2 portretten (doc-A, doc-B)**: Soul Character v2 — uit eerdere sessie batch
- **Decision Act 07**: Static finale na 4× Seedance NSFW false positive — narrative-wise sterker (rust na 6 acts momentum)

Lessons learned uit deze productie staan in `recruitmentengineer-V3-retrospectief.md` (separate handover file).

---

## Deploy preview

Site staat **live op** https://dashing-unicorn-22ba22.netlify.app — deployed via Netlify API, niet via Vercel main pipeline. Vrij om te wijzigen zonder impact op `recruitmentengineer.nl`.

## Hoe live zetten op recruitmentengineer.nl

**Optie A — Vervang huidige hero in `06-landing-page/`**
1. Backup huidige `06-landing-page/public/index.html` → `index.v3.1.html`
2. Copy `12-v3.2-hero-video/index.html` → `06-landing-page/public/index.html`
3. Copy `12-v3.2-hero-video/videos/*` → `06-landing-page/public/videos/`
4. Test Vercel preview deploy
5. Merge naar main → live

**Optie B — Houd V3.2 als experimenteel pad**
1. Deploy V3.2 op subdomein zoals `v3.recruitmentengineer.nl` of `experience.recruitmentengineer.nl`
2. Link er naartoe vanaf de huidige site als "experimentele versie"
3. A/B test welke beter converteert

**Optie C — Stop V3.2 in een sub-route op huidige site**
1. Plaats V3.2 op `recruitmentengineer.nl/experience/`
2. Verwijs vanaf huidige site naar "/experience" voor de full storytelling

---

## Tech notes voor reviewer

- **No external deps** behalve Google Fonts (Inter, Instrument Serif, JetBrains Mono)
- **No JS framework** — vanilla IntersectionObserver, requestAnimationFrame
- **iOS Safari autoplay**: alleen Act 01 heeft `autoplay`, andere videos starten via JS op scroll/touch; alle videos hebben poster frames als fallback
- **Lighthouse**: te verwachten 95+ performance (small payload, lazy video loading, preload="none" voor non-active acts)
- **Accessibility**: `prefers-reduced-motion` respected, semantic HTML, alt-text op alle images
- **CTA form**: huidige `mailto:` fallback naar `warts@recruitin.nl` — moet later gekoppeld worden aan dezelfde Resend/Pipedrive flow als huidige site (`/api/subscribe.js`)

---

## Wat nog placeholder is

| Wat | Waar | Status |
|-----|------|--------|
| 5× Stack module UI screenshots | §02, `[ M0X · UI ]` grijze tegels | Te genereren als UI mockups in volgende ronde |
| Ronde testimonial portret | §04 cirkel | Kan ook anoniem blijven met initials |
| CTA backend | §05 form action | Mailto fallback nu — moet naar bestaande `/api/subscribe` |

---

**Owner:** Ing. W. Arts · `warts@recruitin.nl` · +31 6 14 31 45 93
**Branch:** `v3.2-hero-video`
**Build date:** 2026-05-15
