# SET B — Brand Visuals (Nano Banana Pro)

8 prompts for brand-asset rendering: 3 data-viz, 1 quote-card template (with `[QUOTE]` variable), 2 carousel covers (long-form LinkedIn + short Meta), 1 lead-magnet PDF cover, 1 LinkedIn cover banner.

> **Tool:** Nano Banana Pro (4K for banners + PDF cover, 1K for cards). Better text-rendering than Soul 2 — use this set for any asset where typography must be sharp.

> **Pre-flight:** read `identity-lock-rules.md`. Brand colors locked: `#FF6B1A` (orange), `#1E3A5F` (blueprint blue), `#00D4FF` (AI cyan), `#F5F0EB` (warm grey), `#1A1A1A` (deep black).

---

## B.1 — Data-viz: pipeline funnel (1:1, blueprint style)

```
Nano Banana Pro — 1K — 1:1

Editorial blueprint-style data visualization for recruitment pipeline
funnel. Background: deep blueprint blue #1E3A5F with subtle technical-
drawing grid pattern at 8% opacity (faint white lines, dimension
arrows, schematic markers).

Center: a 5-stage funnel diagram drawn as engineering schematic, top
to bottom:
  Stage 1 — "INTAKE" (1200 vacatures) — width 100%
  Stage 2 — "BOOLEAN MATCH" (340) — width 70%
  Stage 3 — "INMAIL-FIT" (89) — width 45%
  Stage 4 — "REPLY" (37) — width 25%
  Stage 5 — "GEPLAATST" (12) — width 12%

Each stage rendered as a horizontal bar in warm grey #F5F0EB with a
thin orange #FF6B1A right-edge accent. Numbers rendered in JetBrains
Mono Bold white. Stage labels in Inter Bold white, all caps, letter-
spaced. Conversion percentages between stages marked with small
orange "▼ 28%" indicators in JetBrains Mono.

Top-right corner: small JetBrains Mono uppercase 12pt:
"FIG. 03 / RECRUITMENT FUNNEL / 90D".

Bottom-right: small "Recruitin" wordmark white. Bottom-left: tiny
"Ing. W. Arts" attribution.

Engineering blueprint aesthetic, ultra-clean, high contrast, NOT
Powerpoint, NOT generic infographic.

NEGATIVE: misspelled text, decorative gradients, drop shadows,
cartoon, generic infographic style, Powerpoint feel, AI artifacts,
watermark, busy ornaments, multiple fonts beyond Inter + JetBrains.
```

---

## B.2 — Data-viz: throughput chart (1:1, blueprint style)

```
Nano Banana Pro — 1K — 1:1

Editorial blueprint-style throughput chart. Background: deep
blueprint blue #1E3A5F with technical grid pattern at 8% opacity.

Center: a horizontal time-series bar chart, 12 vertical bars
representing months Jan-Dec, plotted on a clean baseline. Y-axis
labeled "INVULTIJD (DAGEN)" in JetBrains Mono Bold white, X-axis
labeled "2025 → 2026". Bars rendered in warm grey #F5F0EB, with
the last 4 bars accented in orange #FF6B1A (showing improvement
after AI-stack rollout). Annotation arrow + JetBrains Mono note:
"AI STACK LIVE — JUL 2025" pointing at the inflection bar.
Numerical values floating above each bar in JetBrains Mono.

Top-right: "FIG. 07 / TIME-TO-HIRE / 12M" in JetBrains Mono uppercase.
Bottom-left: "Source: Recruitin internal dashboard / n=247 vacatures".
Bottom-right: small Recruitin wordmark in white.

Engineering documentation aesthetic, clean, factual, ZERO decoration.

NEGATIVE: misspelled text, decorative gradients, drop shadows,
cartoon, glowing 3D bars, Powerpoint, generic infographic, watermark,
multiple fonts.
```

---

## B.3 — Data-viz: before/after comparison (1:1, blueprint style)

```
Nano Banana Pro — 1K — 1:1

Editorial blueprint-style before/after comparison. Background: warm
grey #F5F0EB (light variant for high-readability data).

Layout: vertical split, two columns labeled "VOOR / NA" at top in
Inter Bold dark blueprint-blue. Left column ("VOOR"): 4 stacked stat
boxes in faint grey rendering bad numbers — "TIME TO HIRE: 84d",
"CTR: 0.4%", "REPLY RATE: 6%", "COST PER HIRE: €4.200". Right column
("NA"): same 4 stats in orange-accent boxes — "TIME TO HIRE: 38d",
"CTR: 1.9%", "REPLY RATE: 41%", "COST PER HIRE: €1.150".

Between columns: a thin vertical orange #FF6B1A divider with the
JetBrains Mono caption "+ AI RECRUITMENT STACK" running vertically
along it.

Top: header "CASE STUDY / VECO PLC PROGRAMMEUR" in JetBrains Mono.
Bottom: small footer "Q3 2025 — Q1 2026 / Ing. W. Arts" in JetBrains
Mono. Bottom-right: tiny Recruitin wordmark.

Engineering case-study report aesthetic, clean technical document.

NEGATIVE: misspelled text, decorative, glowing arrows, cartoon,
generic before/after weight-loss style, Powerpoint, AI artifacts,
watermark.
```

---

## B.4 — Quote-card template (1:1, with `[QUOTE]` variable)

```
Nano Banana Pro — 1K — 1:1

Editorial quote card design template. Background: solid blueprint
blue #1E3A5F with subtle blueprint-grid pattern at 5% opacity.

Centered text in clean white Inter Bold, 38pt, max 3 lines:
"[QUOTE]"

Below the quote, separated by a thin orange #FF6B1A horizontal rule
(80px wide), small attribution in orange:
"— Ing. W. Arts"

Below attribution, in JetBrains Mono uppercase 11pt white:
"RECRUITIN.NL · RECRUITMENT ENGINEER"

Bottom-right corner: small Recruitin wordmark in white at 60% opacity.

Top-right corner: tiny tone-tag in JetBrains Mono uppercase 10pt
warm grey #F5F0EB at 50% opacity:
"TONE: [TONE_TAG]"

Editorial minimal engineering aesthetic. Sharp text rendering, NO
decorative ornaments, NO drop shadows.

NEGATIVE: misspelled text, decorative ornaments, drop shadows,
gradients, glow, cartoon, generic motivational quote design,
multiple fonts beyond Inter + JetBrains, watermark, AI artifacts.
```

### Variables to fill

| Variable | Example values |
|----------|----------------|
| `[QUOTE]` | "Ik ben ingenieur. En recruiter." / "De helft van wat als best-practice geldt, werkt hier niet." / "Een vacature is geen tekst — het is een verkeerd ingesteld filter." / "Geen vacatures. Een systeem." / "47 prompts in productie. 23 zijn waardeloos. Hier is waarom." |
| `[TONE_TAG]` | RUSTIG AUTORITEIT / BRUTAAL DIRECT / SPECIALIST / ENERGIEK / ENGINEER LOGISCH |

Quote length budget: max 90 characters, max 3 lines on render. If a quote is longer, downsize to 32pt (and reflow to 4 lines max). Test legibility at thumbnail (400px).

---

## B.5 — Carousel cover: long-form LinkedIn (4:5, photo + headline)

```
Nano Banana Pro — 1K — 4:5

LinkedIn long-form carousel cover slide.

Top 60% of frame: cinematic editorial photo of Ing. W. Arts in
industrial setting (use Set A Portrait 02 or 04 as character
reference). Light grey wool blazer, white shirt, black knit tie,
round-frame matte black acetate glasses, salt-and-pepper hair.
Calm authoritative expression, examining-blueprint or pointing-at-
screen pose. Image slightly darkened/washed for text-overlay zone.

Bottom 40%: solid orange band #FF6B1A. Inside the band, large white
Inter Bold typography, 3 stacked lines, all caps, slightly letter-
spaced:
  "HOE IK
   VACATURE-INTAKE HEB
   GEREVERSE-ENGINEERED"

Below the headline, smaller white text:
"10 slides → Ing. W. Arts | Recruitin"

Bottom-right corner: small "swipe →" indicator in white JetBrains
Mono, pulsing-feel.

Top-left corner above photo: tiny JetBrains Mono uppercase 10pt
warm grey #F5F0EB at 70% opacity:
"FIG. 01 / 10 — LINKEDIN CAROUSEL"

Editorial documentary + engineering tag aesthetic. Carousel cover
that screams "open me" — clear hierarchy, premium feel, NOT
clickbait, NOT influencer.

NEGATIVE: misspelled text, generic LinkedIn carousel, plastic skin,
missing glasses, broad smile, fake influencer face, stock photo,
watermark, decorative ornaments.
```

---

## B.6 — Carousel cover: short Meta (1:1, typography-led)

```
Nano Banana Pro — 1K — 1:1

Meta / Instagram carousel cover slide. Typography-led, no portrait.

Background: pure deep black #1A1A1A with extremely faint blueprint
grid pattern at 3% opacity.

Massive top-left text in Inter Bold, all caps:
  "47 PROMPTS." (white, 90pt)
Below in Inter Bold orange #FF6B1A, smaller:
  "23 ZIJN WAARDELOOS." (60pt)
Below in white JetBrains Mono uppercase 14pt:
  "DE 5 DIE WERKEN — SWIPE →"

Bottom-right corner: small Recruitin wordmark in orange #FF6B1A.
Bottom-left: tiny "@ingwarts" in JetBrains Mono warm grey.

Maximum contrast, manifesto-style hook design. Engineered for
Meta feed thumbnail visibility — the numerical hook reads at 200px.

NEGATIVE: misspelled text, decorative ornaments, drop shadows,
gradients, generic motivational, cartoon, AI artifacts, watermark,
multiple fonts beyond Inter + JetBrains.
```

---

## B.7 — Lead magnet PDF cover (8.5×11, "Stack 2026")

```
Nano Banana Pro — 4K — A4 portrait (or 8.5×11 ratio)

Editorial PDF cover for "De Recruitment Engineering Stack 2026"
(12-page lead magnet). Premium editorial feel — like an Indesign-
quality industry report, NOT a free e-book.

Top half (60%): cinematic editorial photo of Ing. W. Arts in a
blueprint-tafel setting (use Set A Portrait 03 as reference).
Light grey wool blazer, white shirt, black knit tie, round-frame
matte black acetate glasses, salt-and-pepper hair. Three-quarter
pose, leaning over engineering blueprint, focused intelligent
gaze. Strong teal-orange cinematic grade. Image bleeds to edges
with subtle vignette darkening at the bottom for text-overlay.

Bottom half (40%): warm grey band #F5F0EB. Inside:

Top of band, JetBrains Mono uppercase 14pt blueprint-blue:
"RECRUITIN.NL · STACK 2026 · v1.0"

Hoofdtitel, Inter Black 72pt blueprint-blue #1E3A5F:
  "Recruitment
   Engineering
   Stack 2026"

Onder hoofdtitel, dunne 6px hoge oranje rule (#FF6B1A), 120px breed.

Eronder, Inter Regular 18pt deep zwart #1A1A1A:
"5 productie-prompts. 47 getest. 12 pagina's. Gratis."

Bottom-left: kleinere text 13pt JetBrains Mono blueprint-blue:
"Ing. W. Arts · Ingenieur + Recruiter · 20 jaar tech sector"

Bottom-right: oranje accent-block #FF6B1A 80×30px met witte text
"GRATIS PDF" in Inter Bold, plus pijl-icoon.

Editorial industrial-report aesthetic. NOT e-book template, NOT
generic lead-magnet, NOT motivational fluff.

NEGATIVE: misspelled text, generic e-book cover, stock photo,
plastic skin, missing glasses, broad smile, fake AI grin,
decorative ornaments, drop shadows, gradients, multiple fonts,
watermark, Aebi Schmidt branding.
```

---

## B.8 — LinkedIn cover banner (1584×396, hero portrait + wordmark)

```
Nano Banana Pro — 4K — 21:9 (crop to 1584×396 in post)

Wide cinematic LinkedIn cover banner.

Left third (~530px wide): editorial portrait of Ing. W. Arts in
industrial setting (use Set A Portrait 01 or 04 as reference).
Light grey wool blazer, white shirt, black knit tie, round-frame
matte black acetate glasses, salt-and-pepper hair. Three-quarter
pose, calm authoritative gaze toward camera-right. Industrial
out-of-focus background — machine park or production hall, blueprint
blue/grey tones. Strong teal-orange cinematic grade.

Center two-thirds: dark gradient overlay from blueprint-blue
#1E3A5F at left edge fading to deep black #1A1A1A at right.
Subtle blueprint-grid pattern at 6% opacity.

Right two-thirds typography zone:

Top (just left of horizontal center), JetBrains Mono uppercase 16pt
warm grey #F5F0EB at 70% opacity:
"RECRUITIN.NL · RECRUITMENT ENGINEERING"

Hoofdregel, Inter Black 64pt white:
  "Ing. W. Arts"

Below, Inter Bold 32pt orange #FF6B1A, all caps, letter-spaced:
"RECRUITMENT ENGINEER"

Below, dunne 4px oranje rule, 100px breed.

Eronder, Inter Regular Italic 18pt warm grey:
"De enige ingenieur die recruitment heeft gereverse-engineered."

Bottom-right corner of banner: tiny Recruitin wordmark in orange
#FF6B1A.

Cinematic editorial banner. Sharp typography, NOT generic LinkedIn
cover, NOT motivational, NOT AI-generated avatar.

NEGATIVE: misspelled text, generic LinkedIn cover, plastic skin,
missing glasses, broad smile, fake influencer face, stock photo,
watermark, decorative ornaments, drop shadows, multiple fonts.
```

---

## Output handoff

After approval, copy to:
- `02-higgsfield-assets/data-viz/setB-{01,02,03}-{label}-{date}.png`
- `02-higgsfield-assets/quote-cards/setB-04-quote-{quote-slug}-{date}.png`
- `02-higgsfield-assets/carousel-covers/setB-{05,06}-{platform}-{date}.png`
- `03-lead-magnet/cover/setB-07-stack2026-cover-{date}.{png,pdf}`
- `02-higgsfield-assets/banners/setB-08-linkedin-cover-{date}.png` + crop to 1584×396 in post
