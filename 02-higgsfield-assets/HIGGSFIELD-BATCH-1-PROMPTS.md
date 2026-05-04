# 🎨 Higgsfield Batch-1 — Quick Launch Pack

> **Doel:** binnen 1 sessie de 12 visuele assets renderen die nodig zijn voor launch. Alle prompts copy-paste-ready, geen interpretatie nodig.
>
> **Bron:** dit is de actie-versie van `VISUAL-SPRINT-BRIEF.md`. Dat document bevat alle 18 assets met volledige uitleg. **Dit document = de prioriteit-12 voor launch.**
>
> **Soul-ID:** `948dbc10-...` (al getraind — gebruik bestaande Soul 2 character "Ing W Arts Recruitment Engineer")
>
> **Plan:** Higgsfield Ultra · ~2625 credits beschikbaar · batch-1 verbruikt ~400 cr · ~2225 cr buffer voor batch-2/3

---

## 🚦 RENDER VOLGORDE (in deze volgorde uitvoeren)

```
P1  Studio Authority (LinkedIn profile photo)         25 cr · 1:1
P2  OG-image hero portrait (replace placeholder JPG)  25 cr · 16:9
P3  Industrial Authority banner (LinkedIn cover)      30 cr · 21:9
P4  Engineer in Production Hall (Day 1 hero post)     25 cr · 4:5
P5  Blueprint Table Authority (Day 2 carousel cover)  25 cr · 4:5
P6  Walking the Floor (Day 3 reel still)              25 cr · 16:9
P7  Quote Card 1 — "Ik ben ingenieur. En recruiter."  10 cr · 1:1
P8  Quote Card 2 — "47 prompts. Hier zijn er 5."      10 cr · 1:1
P9  Quote Card 5 — "GEEN VACATURES. EEN SYSTEEM."     10 cr · 1:1
P10 Banner 2 — Studio Minimal (alt LinkedIn cover)    30 cr · 21:9
P11 Carousel Cover 1 — "Reverse-Engineering"          10 cr · 4:5
P12 Multi-Monitor Strategist (versatile 16:9 hero)    25 cr · 16:9
                                                     -------
TOTAL                                                ~250 cr
```

Buffer voor regen / variants: ~150 cr. Stop na P12 — batch-2 start na launch-week feedback.

---

## P1 — Studio Authority (LinkedIn profile photo) · 1:1

**Tool:** Soul 2 · Soul-ID: `948dbc10-...` · Aspect: 1:1 · Credits: ~25

```
Editorial studio portrait of Ing. W. Arts. Wearing dark charcoal blazer
over white crew neck, modern dark rectangular glasses. Frontal pose,
slight head turn three-quarter, looking directly into camera with calm
authoritative gaze — closed-mouth slight smile (subtle, not toothy).
Tight headshot crop from upper chest. Background: deep matte gray
seamless studio backdrop with subtle orange Recruitin accent gradient
on right side. Three-point studio lighting: soft key from front-left,
fill from right, hair light from above. Sharp focus, hyperrealistic 8K,
85mm portrait lens at f/2.8. Editorial commercial style — for LinkedIn
profile photo.

NEGATIVE: text, watermark, broad toothy smile, plastic skin, missing
glasses, multiple people, AI artifacts, generic LinkedIn headshot.
```

**Save as:** `02-higgsfield-assets/hero-portraits/P1-studio-authority.jpg`
**Use:** LinkedIn profile photo · Email signature · Author block on landing pages

---

## P2 — OG-image hero portrait · 16:9

**Tool:** Soul 2 · Soul-ID: `948dbc10-...` · Aspect: 16:9 · Credits: ~25

```
Wide editorial hero image of Ing. W. Arts at three-quarter angle
foreground-left, occupying left 35% of frame. Wearing dark charcoal
blazer, white crew neck, modern dark rectangular glasses, calm
confident expression looking slightly off-camera-right. Right 65% of
frame: deep blueprint-blue (#1E3A5F) gradient with subtle technical-
drawing line patterns at 8% opacity. Strong rim light from upper-right.
Cinematic teal-orange grade. Composition leaves negative space top-
right for text overlay (will be added in post: "Recruitment Engineer
2026" + tagline). Hyperrealistic 8K, 50mm lens at f/2.8.

NEGATIVE: text on image, watermark, smile, plastic skin, missing
glasses, multiple people, AI artifacts, busy background.
```

**Save as:** `02-higgsfield-assets/hero-portraits/P2-og-image-hero.jpg`
**Use:** Replace `06-landing-page/public/og-image.jpg` (current = HTML/CSS-templated fallback)
**Post-render:** Crop to 1200×630, add text overlay via Figma/Photoshop, export as JPG quality 85

---

## P3 — Industrial Authority banner (LinkedIn cover) · 21:9

**Tool:** Nano Banana Pro · 4K · Aspect: 21:9 · Credits: ~30
**Reference:** use P4 (Production Hall) once rendered, OR re-prompt standalone:

```
Wide cinematic LinkedIn cover banner: Left 60% = Dutch male engineer
early 40s in dark navy zipper sweater and modern dark rectangular
glasses standing in industrial workshop, calm confident expression,
looking to camera-right. Right 40% = engineering blueprint diagram
fading into deep blueprint-blue gradient.

TEXT OVERLAY (rendered in image):
- Top-right: "Ing. W. Arts" (large, white, Inter Bold)
- Below: "Recruitment Engineer for Tech & Industry" (smaller, orange #FF6B1A)
- Bottom-right corner: small "Recruitin" wordmark in white

Strong teal-orange cinematic grade. Industrial documentary feel.
Hyperrealistic, sharp typography rendering, professional editorial
quality.

NEGATIVE: misspelled text, generic LinkedIn banner, plastic skin,
missing glasses, multiple people, watermark.
```

**Save as:** `02-higgsfield-assets/banners/P3-industrial-authority.jpg`
**Crop to:** 1584×396 (LinkedIn cover spec)
**Use:** LinkedIn personal profile cover image (Wouter)

---

## P4 — Engineer in Production Hall (Day 1 hero) · 4:5

**Tool:** Soul 2 · Soul-ID: `948dbc10-...` · Aspect: 4:5 · Credits: ~25

```
Editorial documentary portrait of Ing. W. Arts standing in a modern
industrial production facility. Wearing a dark navy turtleneck under
a charcoal blazer, modern dark rectangular glasses. Medium shot from
waist up, body angled three-quarter, head turned to face camera with
calm authoritative expression. Background: out-of-focus CNC machines
and overhead steel structure with cool blue industrial lighting, warm
amber accent on right creating teal-orange cinematic grade. Hands
relaxed, one casually in pocket. Sharp focus on face, shallow depth
of field f/2.8, 85mm prime lens. Documentary editorial style,
hyperrealistic 8K. NOT smiling broadly — calm grounded confidence.

NEGATIVE: text on image, watermark, fake smile, plastic skin, multiple
people, cartoon, AI artifacts, deformed hands, generic corporate stock
photo, missing glasses.
```

**Save as:** `02-higgsfield-assets/hero-portraits/P4-production-hall.jpg`
**Use:** Day 1 LinkedIn manifesto post (hero image) · website "About" section

---

## P5 — Blueprint Table Authority · 4:5

**Tool:** Soul 2 · Soul-ID: `948dbc10-...` · Aspect: 4:5 · Credits: ~25

```
Editorial portrait of Ing. W. Arts leaning forward over a large
engineering blueprint laid on a wooden workbench. Wearing dark
charcoal blazer over white crew neck, modern dark glasses. Hands
flat on the blueprint, body angled three-quarter to camera, looking
directly into camera with focused intelligent gaze — no smile.
Background: warm-toned engineering office with diffused tungsten
lighting, soft amber bokeh. Architectural drawings and a cup of
black coffee visible on table. Cinematic teal-orange grade,
shallow depth of field f/2.0, 50mm lens. Hyperrealistic editorial
style.

NEGATIVE: text, watermark, smile, plastic skin, missing glasses,
generic stock photo, multiple people, AI artifacts.
```

**Save as:** `02-higgsfield-assets/hero-portraits/P5-blueprint-table.jpg`
**Use:** Day 2 LinkedIn carousel cover · Vacature Intake Mastery page (replace WA placeholder)

---

## P6 — Walking the Floor (Day 3 reel still) · 16:9

**Tool:** Soul 2 · Soul-ID: `948dbc10-...` · Aspect: 16:9 · Credits: ~25

```
Cinematic wide editorial shot of Ing. W. Arts walking through an
industrial corridor between production halls, mid-stride. Wearing
dark navy zipper jacket over dark gray crew neck, modern glasses.
Carrying a leather portfolio under his arm, looking forward with
purposeful focused expression. Slight motion blur on background,
sharp on subject. Cool blue overhead industrial lighting with warm
amber accents from side openings. Strong teal-orange cinematic
grade. Mid-shot capturing full upper body, slight low angle for
hero feel. Hyperrealistic 8K, 35mm lens at f/4 with subtle motion
capture aesthetic.

NEGATIVE: text, watermark, posing, smile, plastic skin, missing
glasses, AI artifacts, generic walking shot.
```

**Save as:** `02-higgsfield-assets/hero-portraits/P6-walking-floor.jpg`
**Use:** Day 3 LinkedIn video reel — first frame still + thumbnail

---

## P7 — Quote Card 1 "Ik ben ingenieur. En recruiter." · 1:1

**Tool:** Nano Banana Pro · 1K · Aspect: 1:1 · Credits: ~10

```
Square quote card design. Solid blueprint-blue background (#1E3A5F).
Centered text in clean white Inter Bold: "Ik ben ingenieur. En
recruiter." (38pt). Below in smaller orange (#FF6B1A): "— Ing. W. Arts"
(16pt). Subtle blueprint-grid pattern at 5% opacity. Bottom-right:
small Recruitin wordmark in white.

Editorial minimal, engineering aesthetic. Sharp text rendering.

NEGATIVE: misspelled, decorative, ornaments, watermark.
```

**Save as:** `02-higgsfield-assets/quote-cards/P7-manifesto-quote.jpg`
**Use:** Day 1 manifesto support image · Slack/email signature visual · Insta post

---

## P8 — Quote Card 2 "47 prompts. Hier zijn er 5. Gratis." · 1:1

**Tool:** Nano Banana Pro · 1K · Aspect: 1:1 · Credits: ~10

```
Square card. Warm gray background (#F5F0EB). Massive number "47" in
JetBrains Mono Bold dark blueprint-blue, top-left aligned, treated as
technical specification with measurement arrows alongside. Below:
clean text "prompts in productie." (Inter Regular, dark). Small
horizontal orange line. Bottom: "Hier zijn er 5. Gratis." (Inter Bold
dark). Small "recruitmentengineer.nl" in corner.

Clean engineering specification aesthetic.

NEGATIVE: misspelled, decorative, watermark.
```

**Save as:** `02-higgsfield-assets/quote-cards/P8-numerical-hook.jpg`
**Use:** Lead-magnet hero on landing page (alternative) · Day 2 carousel slide 3 · Meta ad creative

---

## P9 — Quote Card 5 "GEEN VACATURES. EEN SYSTEEM." · 1:1

**Tool:** Nano Banana Pro · 1K · Aspect: 1:1 · Credits: ~10

```
Square card. Pure black background (#1A1A1A). Massive text "GEEN
VACATURES." (Inter Bold White, top-left) and below "EEN SYSTEEM."
(Inter Bold orange #FF6B1A). Small text bottom-right: "Ing. W. Arts |
Recruitment Engineer".

Maximum contrast, manifesto-style.

NEGATIVE: misspelled, decorative, watermark.
```

**Save as:** `02-higgsfield-assets/quote-cards/P9-manifesto-bold.jpg`
**Use:** Day 5 LinkedIn manifesto re-post · Meta ad creative · Slack header

---

## P10 — Studio Minimal banner (alt LinkedIn cover) · 21:9

**Tool:** Nano Banana Pro · 4K · Aspect: 21:9 · Credits: ~30
**Reference:** P1 Studio Authority

```
Wide cinematic LinkedIn banner with deep charcoal-to-blueprint-blue
gradient background. Left 35% = engineer subject in studio shot
(dark blazer, white crew, dark glasses, calm authoritative). Right
65% = clean typography zone.

TEXT OVERLAY (rendered in image):
- Top: "Ing. W. Arts" (white, large, Inter Bold)
- Below: "RECRUITMENT ENGINEER" (orange #FF6B1A, smaller, all caps,
  letter-spaced)
- Bottom italic tagline: "De enige ingenieur die recruitment heeft
  gereverse-engineered." (white, light weight)

Subtle blueprint-grid overlay at 5% opacity in background. Sharp
typography, professional editorial banner quality.

NEGATIVE: misspelled text, generic banner, plastic skin, missing
glasses, watermark, busy background.
```

**Save as:** `02-higgsfield-assets/banners/P10-studio-minimal.jpg`
**Use:** Alternative LinkedIn cover · Email-newsletter header · Twitter/X header (crop to 3:1)

---

## P11 — Carousel Cover "Reverse-Engineering" · 4:5

**Tool:** Nano Banana Pro · 1K · Aspect: 4:5 · Credits: ~10
**Reference:** use P4 (Production Hall) once rendered

```
LinkedIn carousel cover. Top 60%: cinematic engineer subject (dark
blazer, modern glasses, industrial setting, slightly washed/darkened).
Bottom 40%: orange band (#FF6B1A).

TEXT IN ORANGE BAND (rendered in image):
- Large white text: "HOE IK VACATURE-INTAKE HEB GEREVERSE-ENGINEERED"
  (Inter Bold, 3 lines stacked)
- Below in small white: "10 slides → Ing. W. Arts"
- Bottom-right: small "swipe →" indicator

Editorial documentary + engineering tag aesthetic. Carousel cover
that screams "open me".

NEGATIVE: misspelled, generic carousel, plastic skin, missing glasses,
watermark.
```

**Save as:** `02-higgsfield-assets/carousel-covers/P11-reverse-engineering.jpg`
**Use:** Day 2 LinkedIn carousel — slide 1 (cover)

---

## P12 — Multi-Monitor Strategist · 16:9

**Tool:** Soul 2 · Soul-ID: `948dbc10-...` · Aspect: 16:9 · Credits: ~25

```
Wide editorial shot of Ing. W. Arts seated at a sleek dark wood desk
with three large monitors showing data dashboards, recruitment
analytics, and code. Wearing dark gray cashmere sweater, modern dark
rectangular glasses. Body turned slightly to camera in three-quarter
profile, hands resting on desk, looking up from screens with thoughtful
focused expression. Soft warm key light from front-left, cool monitor
glow on face. Background: minimal modern home office with engineering
bookshelf softly out of focus, single amber pendant light. Cinematic
teal-orange grade. Documentary editorial style, hyperrealistic 8K,
35mm lens at f/4.

NEGATIVE: text on screens (keep them illegible/blurred for legal
safety), watermark, smiling at camera, plastic skin, missing glasses,
AI artifacts, deformed hands.
```

**Save as:** `02-higgsfield-assets/hero-portraits/P12-multi-monitor.jpg`
**Use:** Versatile 16:9 hero · Meta ad creative · YouTube thumbnail · website hero alternative

---

## ✅ POST-RENDER CHECKLIST

Per asset, na render:

- [ ] Glasses present? (LOCK: modern rectangular dark frames, ALWAYS)
- [ ] No fake/toothy smile? (Default: closed-mouth slight smile or neutral)
- [ ] Skin not plastic-perfect? (Hyperrealistic, NOT AI-glossy)
- [ ] Hands correct (5 fingers, no morphing)?
- [ ] Background not busy/distracting?
- [ ] Text rendering correct? (No misspellings — common AI fail-mode)
- [ ] Brand colors correct? (#1E3A5F navy, #FF6B1A orange, #00D4FF cyan accent)

Als 2+ checks fail → regenerate (1 retry per asset budgeted in 150-cr buffer).

---

## 📦 SAVE & SYNC

Na alle 12 renders:

```bash
# Optimaliseer voor web (JPEG quality 85, max 1920px lange zijde)
cd ~/projects/recruitmentengineer/02-higgsfield-assets
for dir in hero-portraits banners quote-cards carousel-covers; do
  for f in $dir/P*.jpg; do
    sips -s format jpeg -s formatOptions 85 --resampleWidth 1920 "$f" 2>/dev/null
  done
done

# Replace OG-image
cp hero-portraits/P2-og-image-hero.jpg ../06-landing-page/public/og-image.jpg

# Commit
cd ~/projects/recruitmentengineer
git add 02-higgsfield-assets/ 06-landing-page/public/og-image.jpg
git commit -m "feat: add Higgsfield batch-1 visual assets (12 items)"
git push
```

---

## ⏭️ BATCH 2 (post-launch)

Na batch-1 + 1 week launch-feedback, render:
- P13-P17: hero portraits 3, 5, 6, 7, 9 (uit VISUAL-SPRINT-BRIEF.md)
- P18-P19: banners 3, 4
- P20-P22: quote cards 3, 4 + carousel covers 2, 3

Buffer: ~250 cr. Trigger: na 3+ launch posts gepubliceerd, eerste lead-data binnen.
