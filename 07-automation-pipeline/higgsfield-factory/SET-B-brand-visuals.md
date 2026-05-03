# SET B — Brand Visuals (Nano Banana 2, no Soul-ID)

8 prompts for non-portrait brand assets: 3 data viz + 1 quote-card template + 2 carousel covers (long-form-LI vs short-Meta) + 1 PDF cover + 1 LinkedIn banner.

> **Tool:** Nano Banana 2 (sharper text rendering, 4K for banners + PDF cover, 1K for cards). **No Soul-ID needed** — these assets have no portrait. The LinkedIn banner uses a Soul-portrait LINK (rendered separately via Set-A then composited), not a Soul-rendered face inside this prompt.

> **Pre-flight:** read `identity-lock-rules.md`. Brand colors locked: `#FF6B1A` (orange), `#1E3A5F` (blueprint blue), `#00D4FF` (AI cyan), `#F5F0EB` (warm grey), `#1A1A1A` (deep black). Typography locked: **Inter** (display) + **JetBrains Mono** (data/labels).

---

## B.1 — Data-viz: pipeline-funnel (1:1, blueprint style)

```
Nano Banana 2 — 1K — 1:1

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
spaced 0.2em. Conversion percentages between stages marked with small
orange "▼ 28%" indicators in JetBrains Mono.

Top-right corner: small JetBrains Mono uppercase 12pt:
"FIG. 03 / RECRUITMENT FUNNEL / 90D".

Bottom-right: small "Recruitin" wordmark white. Bottom-left: tiny
"Ing. W. Arts" attribution.

Engineering blueprint aesthetic, ultra-clean, high contrast, NOT
Powerpoint, NOT generic infographic.
```

**NEGATIVE PROMPT:**
```
misspelled text, decorative gradients, drop shadows, cartoon, generic
infographic style, Powerpoint feel, AI artifacts, watermark, busy
ornaments, multiple fonts beyond Inter + JetBrains Mono, glow effects,
3D bevels, Aebi Schmidt branding.
```

---

## B.2 — Data-viz: throughput-chart (1:1, blueprint style)

```
Nano Banana 2 — 1K — 1:1

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
Inter Bold for labels, JetBrains Mono for all numerics.
```

**NEGATIVE PROMPT:**
```
misspelled text, decorative gradients, drop shadows, cartoon, glowing
3D bars, Powerpoint, generic infographic, watermark, multiple fonts,
AI artifacts, Aebi Schmidt branding.
```

---

## B.3 — Data-viz: before-after (1:1, blueprint style)

```
Nano Banana 2 — 1K — 1:1

Editorial blueprint-style before/after comparison. Background: warm
grey #F5F0EB (light variant for high-readability data).

Layout: vertical split, two columns labeled "VOOR / NA" at top in
Inter Bold dark blueprint-blue #1E3A5F. Left column ("VOOR"): 4
stacked stat boxes in faint grey rendering bad numbers — "TIME TO
HIRE: 84d", "CTR: 0.4%", "REPLY RATE: 6%", "COST PER HIRE: €4.200".
Right column ("NA"): same 4 stats in orange-accent boxes — "TIME TO
HIRE: 38d", "CTR: 1.9%", "REPLY RATE: 41%", "COST PER HIRE: €1.150".

Between columns: a thin vertical orange #FF6B1A divider with the
JetBrains Mono caption "+ AI RECRUITMENT STACK" running vertically
along it.

Top: header "CASE STUDY / VECO PLC PROGRAMMEUR" in JetBrains Mono.
Bottom: small footer "Q3 2025 — Q1 2026 / Ing. W. Arts" in JetBrains
Mono. Bottom-right: tiny Recruitin wordmark.

Engineering case-study report aesthetic, clean technical document.
Inter for labels, JetBrains Mono for numerics, NO decorative elements.
```

**NEGATIVE PROMPT:**
```
misspelled text, decorative, glowing arrows, cartoon, generic
before/after weight-loss style, Powerpoint, AI artifacts, watermark,
gradients, multiple fonts, Aebi Schmidt branding.
```

---

## B.4 — Quote-card template (1:1, with [QUOTE] variable)

```
Nano Banana 2 — 1K — 1:1

Editorial quote card design template. Background: solid blueprint
blue #1E3A5F with subtle blueprint-grid pattern at 5% opacity.

Centered text in clean white Inter Bold, 38pt, max 3 lines:
"[QUOTE]"

Below the quote, separated by a thin orange #FF6B1A horizontal rule
(80px wide), small attribution in orange:
"— Ing. W. Arts"

Below attribution, in JetBrains Mono uppercase 11pt white,
letter-spaced 0.2em:
"RECRUITIN.NL · RECRUITMENT ENGINEER"

Bottom-right corner: small Recruitin wordmark in white at 60% opacity.

Top-right corner: tiny tone-tag in JetBrains Mono uppercase 10pt
warm grey #F5F0EB at 50% opacity:
"TONE: [TONE_TAG]"

Editorial minimal engineering aesthetic. Sharp text rendering, NO
decorative ornaments, NO drop shadows.
```

**Variables to fill:**

| Variable | Example values |
|----------|----------------|
| `[QUOTE]` | "Ik ben ingenieur. En recruiter." / "De helft van wat als best-practice geldt, werkt hier niet." / "Een vacature is geen tekst — het is een verkeerd ingesteld filter." / "Geen vacatures. Een systeem." / "47 prompts in productie. 23 zijn waardeloos. Hier is waarom." |
| `[TONE_TAG]` | RUSTIG AUTORITEIT / BRUTAAL DIRECT / SPECIALIST / ENERGIEK / ENGINEER LOGISCH |

Quote length budget: max 90 characters, max 3 lines on render. If a quote is longer, downsize to 32pt (and reflow to 4 lines max). Test legibility at thumbnail (400px).

**NEGATIVE PROMPT:**
```
misspelled text, decorative ornaments, drop shadows, gradients, glow,
cartoon, generic motivational quote design, multiple fonts beyond
Inter + JetBrains Mono, watermark, AI artifacts, photo elements, faces.
```

---

## B.5 — Carousel cover: long-form LinkedIn (4:5, photo + headline)

```
Nano Banana 2 — 1K — 4:5

LinkedIn long-form carousel cover slide.

Top 60% of frame: cinematic editorial photo placeholder zone for a
Soul-rendered portrait of Ing. W. Arts (composited from a Set A Soul-2
render — A02 werkplaats or A04 monitor-setup). Image slightly
darkened/washed for text-overlay zone. (Render this cover with a
neutral industrial backdrop; the actual portrait is composited in
afterward via masking.)

Bottom 40%: solid orange band #FF6B1A. Inside the band, large white
Inter Bold typography, 3 stacked lines, all caps, letter-spaced 0.02em:
  "HOE IK
   VACATURE-INTAKE HEB
   GEREVERSE-ENGINEERED"

Below the headline, smaller white Inter Regular 18pt:
"10 slides → Ing. W. Arts | Recruitin"

Bottom-right corner: small "swipe →" indicator in white JetBrains Mono.

Top-left corner above photo zone: tiny JetBrains Mono uppercase 10pt
warm grey #F5F0EB at 70% opacity, letter-spaced 0.2em:
"FIG. 01 / 10 — LINKEDIN CAROUSEL"

Editorial documentary + engineering tag aesthetic. Carousel cover
that screams "open me" — clear hierarchy, premium feel, NOT
clickbait, NOT influencer.
```

**NEGATIVE PROMPT:**
```
misspelled text, generic LinkedIn carousel template, plastic skin,
broad smile, fake influencer face, stock photo, watermark, decorative
ornaments, drop shadows, gradients, multiple fonts beyond Inter +
JetBrains Mono, Aebi Schmidt branding.
```

---

## B.6 — Carousel cover: short Meta (1:1, typography-led)

```
Nano Banana 2 — 1K — 1:1

Meta / Instagram carousel cover slide. Typography-led, no portrait.

Background: pure deep black #1A1A1A with extremely faint blueprint
grid pattern at 3% opacity.

Massive top-left text in Inter Black, all caps, letter-spaced 0.02em:
  "47 PROMPTS." (white, 90pt)
Below in Inter Black orange #FF6B1A, smaller:
  "23 ZIJN WAARDELOOS." (60pt)
Below in white JetBrains Mono uppercase 14pt, letter-spaced 0.2em:
  "DE 5 DIE WERKEN — SWIPE →"

Bottom-right corner: small Recruitin wordmark in orange #FF6B1A.
Bottom-left: tiny "@ingwarts" in JetBrains Mono warm grey #F5F0EB.

Maximum contrast, manifesto-style hook design. Engineered for
Meta feed thumbnail visibility — the numerical hook reads at 200px.
```

**NEGATIVE PROMPT:**
```
misspelled text, decorative ornaments, drop shadows, gradients, generic
motivational, cartoon, AI artifacts, watermark, multiple fonts beyond
Inter + JetBrains Mono, photo elements, faces.
```

---

## B.7 — PDF cover: Stack 2026 (A4, blueprint grid + Inter typography)

```
Nano Banana 2 — 4K — A4 portrait (or 8.5×11 ratio)

Editorial PDF cover for "De Recruitment Engineering Stack 2026"
(12-page lead magnet). Premium editorial feel — like an Indesign-
quality industry report, NOT a free e-book.

Background: warm grey #F5F0EB with a precise blueprint grid pattern
at 6% opacity (deep blueprint-blue #1E3A5F linework, 32px grid
spacing, dimension markers in corners).

Top-third: large blueprint-blue #1E3A5F block (60% width, 40% height)
positioned top-left. Inside the block, JetBrains Mono uppercase 14pt
warm grey #F5F0EB, letter-spaced 0.2em:
"RECRUITIN.NL · STACK 2026 · v1.0"

Center, dominating typography zone — Inter Black 96pt blueprint-blue
#1E3A5F, 3 lines, left-aligned, letter-spaced -0.04em:
  "Recruitment
   Engineering
   Stack 2026"

Below hoofdtitel, dunne 6px hoge oranje rule (#FF6B1A), 120px breed.

Onder de rule, Inter Regular 18pt deep zwart #1A1A1A:
"5 productie-prompts. 47 getest. 12 pagina's. Gratis."

Bottom-left: kleinere text 13pt JetBrains Mono blueprint-blue:
"Ing. W. Arts · Ingenieur + Recruiter · 20 jaar tech sector"

Bottom-right: oranje accent-block #FF6B1A 80×30px met witte text
"GRATIS PDF" in Inter Bold, plus pijl-icoon.

Corner technical-drawing markers (dimension arrows in JetBrains Mono
9pt blueprint-blue at 30% opacity) for editorial-engineering vibe.

Editorial industrial-report aesthetic, blueprint-grid foundation.
NO photo elements (this is a typography-only cover).
```

**NEGATIVE PROMPT:**
```
misspelled text, generic e-book cover, stock photo, faces, plastic
skin, broad smile, fake AI grin, decorative ornaments, drop shadows,
gradients, multiple fonts beyond Inter + JetBrains Mono, watermark,
Aebi Schmidt branding, glow effects.
```

---

## B.8 — LinkedIn banner 1584×396 (Soul-portrait link + wordmark right)

```
Nano Banana 2 — 4K — 21:9 (crop to 1584×396 in post)

Wide cinematic LinkedIn cover banner. Composite layout: Soul-portrait
on left (linked from Set A render — A01 productiehal or A05 klant-
locatie), brand typography on right.

Left third (~530px wide of 1584): editorial portrait composite zone.
The portrait itself is rendered separately in Set A (Soul-ID
948dbc10-ba8d-406c-b771-e15610ae8674) and masked into this banner.
For Nano Banana 2 render: leave a soft-feathered industrial backdrop
in this zone with blueprint-blue #1E3A5F and warm grey #F5F0EB tones,
out-of-focus machine-park silhouettes, ready for portrait composite.

Center two-thirds: dark gradient overlay from blueprint-blue #1E3A5F
at left edge fading to deep black #1A1A1A at right. Subtle blueprint-
grid pattern at 6% opacity.

Right two-thirds typography zone:

Top (just left of horizontal center), JetBrains Mono uppercase 16pt
warm grey #F5F0EB at 70% opacity, letter-spaced 0.2em:
"RECRUITIN.NL · RECRUITMENT ENGINEERING"

Hoofdregel, Inter Black 64pt white, letter-spaced -0.03em:
  "Ing. W. Arts"

Below, Inter Bold 32pt orange #FF6B1A, all caps, letter-spaced 0.02em:
"RECRUITMENT ENGINEER"

Below, dunne 4px oranje rule, 100px breed.

Eronder, Inter Regular Italic 18pt warm grey:
"De enige ingenieur die recruitment heeft gereverse-engineered."

Bottom-right corner of banner: tiny Recruitin wordmark in orange
#FF6B1A.

Cinematic editorial banner. Sharp typography, NOT generic LinkedIn
cover, NOT motivational, NOT AI-generated avatar inside this prompt.
```

**NEGATIVE PROMPT:**
```
misspelled text, generic LinkedIn cover template, plastic skin,
broad smile, fake influencer face, stock photo, watermark, decorative
ornaments, drop shadows, gradients on type, multiple fonts beyond
Inter + JetBrains Mono, Aebi Schmidt branding, fake portrait inside
the banner (Soul-portrait composited separately, NOT generated here).
```

---

## Output handoff

After approval, copy to:
- `02-higgsfield-assets/data-viz/setB-{01,02,03}-{label}-{date}.png`
- `02-higgsfield-assets/quote-cards/setB-04-quote-{quote-slug}-{date}.png`
- `02-higgsfield-assets/carousel-covers/setB-{05,06}-{platform}-{date}.png`
- `03-lead-magnet/cover/setB-07-stack2026-cover-{date}.{png,pdf}`
- `02-higgsfield-assets/banners/setB-08-linkedin-cover-{date}.png` (composite Soul-portrait from Set A in post → crop to 1584×396)

---

## Why no Soul-ID in Set B

Set B is for non-portrait assets. Data-viz, typography-only covers, the PDF cover, and the LinkedIn banner (where the portrait is a *composited link* to a Set-A render, not a face generated inside this prompt) — none need a face-locked Soul.

If a future Set-B asset DOES need an embedded portrait inside the prompt itself, move that asset to Set A (Soul) or Set C (Marketing Studio Soul) instead. Don't try to dual-reference a face into Nano Banana 2 — Soul-2 is faster + more consistent.
