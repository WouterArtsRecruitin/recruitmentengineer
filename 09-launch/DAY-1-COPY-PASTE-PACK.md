# 🚀 DAY-1 LAUNCH — COPY-PASTE PACK

> **Use:** Volg dit document van boven naar beneden op launch-dag.
> Alles is copy-paste-klaar. Geen edits nodig.
>
> **Volgorde:** Higgsfield rendert → LinkedIn updates → Hero Post 1 publish

---

## ⏱️ TIMELINE — 60 MIN PRE-LAUNCH + 1 PUBLISH-MOMENT

| T | Actie | Duur |
|---|-------|------|
| T-60min | Higgsfield: render OG-image + banner | 20 min |
| T-40min | Save banner naar Desktop, OG naar repo, push | 5 min |
| T-35min | LinkedIn: upload banner | 2 min |
| T-33min | LinkedIn: headline + about | 5 min |
| T-28min | LinkedIn: Featured items (3) | 5 min |
| T-23min | LinkedIn: contact-info check | 2 min |
| T-21min | Browser-test landing https://recruitmentengineer.nl | 3 min |
| T-18min | Final check: PDF download, form submit | 5 min |
| T-13min | Pre-flight check Hero Post 1 copy in clipboard | 1 min |
| T-12min | Wacht op publish-moment (08:00 of 17:30) | — |
| T0 | **Publish Hero Post 1** | — |
| T+5min | Comment 1 (link) | — |
| T+2u | Comment 2 (vraag) | — |

---

## 🎨 DEEL A — HIGGSFIELD (2 RENDERS)

### A1. OG-image (1200×630)

**Tool:** Higgsfield Soul-2
**Soul-ID:** `948dbc10-ba8d-406c-b771-e15610ae8674`
**Aspect ratio:** 1200×630 (horizontal)

**Prompt — Variant A "Industrial Authority":**

```
Editorial portrait, half-body, slight 3/4 angle, looking directly at camera, calm authoritative gaze. Subject: Dutch man late 40s, light grey wool blazer, white shirt, black knit tie, round-frame matte black acetate glasses, salt-and-pepper hair. Industrial out-of-focus background — machine park, blueprint blue/grey tones #1E3A5F base, warm side-light from upper right, cinematic low-key, Kodak Portra 400 grade. 1200x630 horizontal composition, subject left third, negative space right two-thirds for text overlay. Professional documentary style, NOT corporate stock photo. Sharp focus on glasses and eyes.
```

**Negative prompt:**
```
generic stock photo, smiling broadly, casual clothing, hoodie, navy suit, dark suit, cluttered background, multiple people, cartoon, illustration, low resolution
```

**After render — text overlay (in Higgsfield text-tool of Figma na export):**

| Layer | Content | Font | Size | Color |
|-------|---------|------|------|-------|
| Top label | `RECRUITIN.NL · STACK 2026` | JetBrains Mono Uppercase | 14pt | `#FF6B1A` |
| Headline L1 | `Recruitment` | Inter Black | 64pt | `#FFFFFF` |
| Headline L2 | `Engineering` | Inter Black | 64pt | `#FFFFFF` |
| Headline L3 | `Stack 2026` | Inter Black | 64pt | `#FF6B1A` |
| Rule | (4px bar, 80px wide) | — | — | `#FF6B1A` |
| Subtitle | `5 productie-prompts. 47% sneller. Gratis.` | Inter Regular | 18pt | `#E5E0D8` |
| Author tag | `Ing. W. Arts · Recruitment Engineer` | JetBrains Mono | 13pt | `#94A3B8` |

**Output:**
- Save als: `og-image.jpg` (JPEG 80%, target < 300 KB)
- Move naar: `/Users/wouterarts/projects/recruitmentengineer/06-landing-page/public/og-image.jpg`

**Commit + deploy:**
```bash
cd /Users/wouterarts/projects/recruitmentengineer
git add 06-landing-page/public/og-image.jpg
git commit -m "Add OG image for launch"
git push
cd 06-landing-page && vercel deploy --prod
```

---

### A2. LinkedIn banner (1584×396)

**Tool:** Higgsfield Soul-2
**Soul-ID:** `948dbc10-ba8d-406c-b771-e15610ae8674`
**Aspect ratio:** 1584×396 (LinkedIn 2026 spec)

**Prompt — Variant A "Industrial Authority":**

```
Cinematic horizontal banner 4:1 ratio. Left 60%: dark industrial machine hall with PLC monitor screens out of focus, blueprint-blue ambient lighting #1E3A5F with subtle orange accent #FF6B1A from upper right. Right 40%: Dutch man late 40s in light grey wool blazer, white shirt, black knit tie, round matte black acetate glasses, salt-and-pepper hair, half-body, side-3/4 angle looking left across the frame toward the empty space. Documentary editorial style, Kodak Portra 400 grade, low-key warm side-lighting, sharp focus on subject. NOT a stock photo. Subject takes right third of frame, leaves left two-thirds open for text overlay.
```

**After render — text overlay (Figma/Photoshop):**

| Position | Content | Font | Size | Color |
|----------|---------|------|------|-------|
| Center-left, large | `Recruitment Engineering` | Inter Bold | 56pt | `#FFFFFF` |
| Below, smaller | `De enige ingenieur die recruitment heeft gereverse-engineered.` | Inter Regular | 22pt | `#00D4FF` |
| Bottom strip | `recruitin.nl  ·  recruitmentengineer.nl  ·  Veco · Beutech · Euromaster` | JetBrains Mono | 14pt | `#94A3B8` |

**Output:**
- Save als: `linkedin-banner.jpg` (JPEG 90%, target < 600 KB)
- Move naar: `~/Desktop/linkedin-banner.jpg` (niet in repo — privé asset voor LinkedIn upload)

---

## 💼 DEEL B — LINKEDIN PROFILE UPDATE

### B1. Banner upload
1. linkedin.com/in/wouter-arts → klik op huidige banner
2. Upload `~/Desktop/linkedin-banner.jpg`
3. Crop default → Apply

### B2. Headline (de aanbevolen — Optie 1)

**Copy-paste:**
```
Recruitment Engineer — Ik haal recruitment uit elkaar en bouw het herop met AI | Voor mid-market tech (50-800 FTE) | Veco · Beutech · Euromaster | Ing. W. Arts
```

### B3. About section

**Copy-paste:**
```
Ik ben de enige werktuigbouwkundig ingenieur die recruitment uit elkaar heeft gehaald en met AI heropgebouwd.

20 jaar geleden kwam ik per ongeluk in dit vak. Wat me opviel: iedereen werkte met onderbuik en templates. Niemand had een proces dat je kon meten, optimaliseren of schalen.

Nu, 2026, is AI zo ver dat het verschil tussen een "recruiter met ChatGPT" en een "recruitment engineer met een stack" gigantisch is geworden.

Concreet, de afgelopen 6 maanden bij mijn klanten Veco · Beutech · Euromaster:

→ Boolean searches: 4 uur → 25 minuten
→ InMails: 8% → 41% response rate
→ Vacature-intake: 8 uur → 90 minuten
→ CV screening: 20 min → 4 min per CV
→ Pipeline recovery: €519.000 stuck deals, 60% terug in beweging

Ik werk uitsluitend met technische bedrijven (50-800 FTE) waar recruitment al maanden achterloopt op hiring-targets en de directeur weet dat het niet aan de mensen ligt, maar aan het proces.

📥 Mijn complete stack staat gratis online:
recruitmentengineer.nl

📧 Direct contact:
warts@recruitin.nl

🛠️ Wat ik niet doe:
× Recruitment-trainingen
× Een AI-tool verkopen
× LinkedIn-engagement-pods
× Vrijblijvende koffie-afspraken
```

### B4. Featured items (3)

| # | Type | Title | Link |
|---|------|-------|------|
| 1 | Link | Recruitment Engineering Stack 2026 — gratis PDF | https://recruitmentengineer.nl |
| 2 | Link | Recruitin — voor de bedrijven die ik begeleid | https://recruitin.nl |
| 3 | Post | Hero Post 1 manifesto (URL invullen na publish) | (kopieer post-URL na T0) |

### B5. Contact info (Edit profile → Contact info)

| Field | Value |
|-------|-------|
| Email | warts@recruitin.nl |
| Website 1 | recruitin.nl (Company) |
| Website 2 | recruitmentengineer.nl (Portfolio) |
| Phone | (jouw mobiel) |

### B6. Open To Work
**UITZETTEN** — je bent niet "open to work" als Authority Engineer. Je verkoopt advisering, geen baan.

---

## 📝 DEEL C — HERO POST 1 (PUBLISH T0)

**Publish-window:** Dinsdag/donderdag 08:00 of 17:30 NL.

### Main post copy

**Copy-paste:**
```
Vandaag herlanceer ik mezelf op LinkedIn als Recruitment Engineer.

Niet als grap.

20 jaar geleden kwam ik per ongeluk in recruitment terecht — opgeleid als werktuigbouwkundig ingenieur. Wat me opviel was vreemd: iedereen werkte met onderbuik en templates. Niemand had een proces dat je kon meten, optimaliseren of schalen.

Dat was 2005.

Nu, 2026, is AI zo ver dat het verschil tussen een "recruiter met ChatGPT" en een "recruitment engineer met een stack" gigantisch is geworden.

Concreet, in mijn werk bij Recruitin de afgelopen 6 maanden:

→ Boolean searches: van 4 uur naar 25 minuten
→ InMails: van 8% naar 41% response rate
→ Vacature-intake: van 8 uur naar 90 minuten
→ CV screening: van 20 min naar 4 min per CV
→ Pipeline recovery: €519.000 stuck deals, 60% terug in beweging

Ik publiceer mijn complete stack vandaag gratis. 12 pagina's PDF, 5 productie-prompts, copy-paste-klaar.

Geen mailing-database trucjes. Geen funnels die je vastzetten. Gewoon de prompts.

Link in de comments.

Reden waarom: het werk is te belangrijk om er een betaalmuur omheen te bouwen. Als jij 1 betere hire doet door deze stack, heeft mijn maandag al impact.

#RecruitmentEngineering #TechRecruitment #AI #Sourcing
```

### Comment 1 (T0 + 30s)
```
Hier de Stack 2026 → https://recruitmentengineer.nl

12 pagina's. 5 prompts. 0 bullshit.
```

### Comment 2 (T0 + 2u)
```
Question voor de mensen die dit lezen: welk van de 5 modules zou JOU het meeste tijd schelen?

1. Sourcing (boolean searches)
2. Outreach (InMails)
3. Intake (vacature-tekst genereren)
4. Screening (CV-matching)
5. Pipeline (stuck deals diagnose)

Reageer met het nummer — ik schrijf maandag een diepgaande post over de winnaar.
```

---

## ✅ DEEL D — POST-PUBLISH CHECKS (T0 + 5 MIN)

```bash
# 1. LinkedIn Post Inspector — check OG-preview op recruitmentengineer.nl
open "https://www.linkedin.com/post-inspector/inspect/https://recruitmentengineer.nl"

# 2. Real-time monitoring (open in second screen):
open "https://recruitin.pipedrive.com/pipeline/16"
open "https://resend.com/audiences/703b9a1f-fc00-4796-8bf3-664350a89879"

# 3. Vercel Analytics live:
open "https://vercel.com/wouters-projects-ee37b5d2/recruitmentengineer/analytics"
```

### Manual checks
- [ ] Post heeft de juiste OG-preview op LinkedIn (banner-image, title, description)
- [ ] Eerste comment toegevoegd binnen 60s na publish
- [ ] Profile-bezoekers zien banner + headline + Featured-items
- [ ] Form werkt (test 1× zelf vanuit een ander email)
- [ ] PDF wordt afgeleverd binnen 60s

### Engagement-bewaking eerste 4u
- Check elke 30 min: nieuwe comments → reageer binnen 5 min
- Save de top-3 reacties voor Day 2 storypost
- DM-flow: connecties die "interessant!" reageren krijgen DM met vraag naar specifieke usecase

---

## 🚨 ROLLBACK / EMERGENCY

**Als landing down gaat:**
```bash
vercel rollback recruitmentengineer-44dlb589k-wouters-projects-ee37b5d2.vercel.app
```

**Als email niet aankomt (Resend down):**
- Check https://status.resend.com
- Check `vercel logs https://recruitmentengineer.nl --follow` voor 500-errors

**Als Pipedrive faalt:**
- Niet-blokkerend (subscribe.js logt en gaat door) — fix achteraf

---

**EINDE — laatst bijgewerkt 3 mei 2026 16:35 NL**
