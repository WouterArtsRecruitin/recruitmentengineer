# 🖼️ OG IMAGE BRIEF — recruitmentengineer.nl

**Format:** 1200 × 630 px (LinkedIn / Twitter / Facebook OG)
**Output file:** `06-landing-page/public/og-image.jpg` (JPEG, 80% quality, < 300 KB)
**Tool:** Higgsfield (or Midjourney met `--ar 1200:630`)

---

## Brand-system (locked, zie `brand-bible-v1.3.md`)

| Token | Waarde |
|-------|--------|
| Primary accent | `#FF6B1A` (Recruitin Oranje) |
| Authority blue | `#1E3A5F` (Blueprint Blauw) |
| Tech accent | `#00D4FF` (AI Cyaan, sparingly) |
| Background | `#F5F0EB` (Warm Grijs) → OF dark `#0A1929` |
| Body text | `#1A1A1A` |
| Display font | Inter Bold 48–96pt |
| Mono labels | JetBrains Mono 12–14pt |

---

## Visual DNA (gelocked, zie brand bible)

**Wouter:**
- Lichtgrijs wol blazer / pak
- Wit overhemd, zwarte gebreide das (textured knit)
- Round-frame matte black acetate bril
- Rustige, autoritaire blik (geen lach, geen stock-photo-grin)

**Niet doen:**
- ❌ Donker pak / navy / zwart
- ❌ Casual / hoodie
- ❌ Aebi Schmidt branding (verboden)
- ❌ Generieke kantoor-foto's
- ❌ Stock-photo recruiters

---

## Variant A — "Industrial Authority" (default — recommended)

**Setting:** Halfportret Wouter, ¾ pose, kijkt naar camera. Industriële achtergrond out-of-focus (machinepark / fabriekshal, blueprint-tinten). Warme zijbelichting, low-key.

**Compositie 1200×630:**
- **Linkerhelft (~700px)** — portret Wouter, full bleed, head + schouder
- **Rechterhelft (~500px)** — donker overlay (`#0A1929` met 92% opacity)
  - Bovenaan, JetBrains Mono uppercase 14pt: `RECRUITIN.NL · STACK 2026`
  - Hoofdregel, Inter Black 64pt, wit: **Recruitment**<br>**Engineering**<br>**Stack 2026**
  - Onder hoofdregel, dunne oranje rule (`#FF6B1A`, 4px hoog, 80px breed)
  - Eronder, Inter Regular 18pt, lichtgrijs: "5 productie-prompts. 47% sneller. Gratis."
  - Linksonder, kleinere text 13pt: "Ing. W. Arts · Recruitment Engineer"

**Higgsfield prompt:**
```
Editorial portrait, half-body, slight 3/4 angle, looking directly at camera, calm authoritative gaze. Subject: Dutch man late 40s, light grey wool blazer, white shirt, black knit tie, round-frame matte black acetate glasses, salt-and-pepper hair. Industrial out-of-focus background — machine park, blueprint blue/grey tones (#1E3A5F base), warm side-light from upper right, cinematic low-key, Kodak Portra 400 grade. 1200x630 horizontal composition, subject left third, negative space right two-thirds for text overlay. Professional documentary style, NOT corporate stock photo.
```

---

## Variant B — "Blueprint" (alternatief, geen portret)

Wordmark + module-grid, geen Wouter:
- Background: technisch grid (`#1E3A5F`), subtle blueprint lines
- Centered: "Recruitment Engineering Stack 2026" (Inter Black 84pt, wit)
- Onder, 5 mini-cards horizontaal: `01 Sourcing` `02 Personalization` `03 Intake` `04 Match Score` `05 Pipeline`
- Mini-cards: warm-grey `#F5F0EB` bg, oranje cijfer, blauwe text
- Bottom-right: oranje accent-block met "GRATIS PDF →"

**Higgsfield prompt:**
```
Editorial wordmark composition, technical blueprint background in deep navy #1E3A5F with subtle white grid lines. Centered headline "Recruitment Engineering Stack 2026" in Inter Black white. Five small horizontal cards below labelled 01-05, in warm grey #F5F0EB with orange #FF6B1A accent numbers. Bottom-right: orange diagonal accent block "GRATIS PDF". 1200x630 horizontal, no people, professional editorial design style.
```

---

## Variant C — "Field Documentary" (most personal)

- Wouter aan een werkplek (laptop, koffie, notitieboek met handgeschreven boolean)
- POV: licht boven-de-schouder, niet recht in camera
- Notitieboek-pagina leesbaar: handwritten "(Java OR Spring) AND seniority:5+"
- Background dof, fabriek-licht door raam

**Higgsfield prompt:**
```
Documentary photography, over-the-shoulder POV of a Dutch recruitment engineer at workspace. Light grey wool blazer, round black acetate glasses. Open laptop, paper notebook with handwritten boolean search "(Java OR Spring) AND seniority:5+", coffee cup, mechanical pencil. Industrial loft window light from left, warm tone, Fujifilm Pro 400H grade. Shallow depth, focus on hands and notebook. 1200x630 horizontal. Cinematic, NOT stock photography.
```

---

## Render-checklist

- [ ] 1200 × 630 exact (geen downscale van 1024 / 1920)
- [ ] Geen Aebi Schmidt zichtbaar (logos, machines, branding)
- [ ] Brand colors aanwezig: oranje `#FF6B1A` + blauw `#1E3A5F` (minstens 1)
- [ ] Wordmark "Stack 2026" leesbaar bij thumbnail-grootte (200×105 op LinkedIn-feed)
- [ ] JPEG export 80% quality, < 300 KB
- [ ] Test op LinkedIn Post Inspector: https://www.linkedin.com/post-inspector/
- [ ] Test op Twitter Card Validator: https://cards-dev.twitter.com/validator

---

## Filenames

| Asset | Filename | Locatie |
|-------|----------|---------|
| OG image (1200×630) | `og-image.jpg` | `06-landing-page/public/og-image.jpg` |
| LinkedIn banner (1584×396) | `linkedin-banner.jpg` | `~/Desktop/` (upload naar LinkedIn, niet in repo) |
| Twitter alt (1200×675) | optioneel, hergebruik OG | n.v.t. |

OG-image is referenced in `index.html` als:
```html
<meta property="og:image" content="https://recruitmentengineer.nl/og-image.jpg">
<meta name="twitter:image" content="https://recruitmentengineer.nl/og-image.jpg">
```

Na deploy: zet OG-image online (Vercel pakt `public/og-image.jpg` automatisch op).
