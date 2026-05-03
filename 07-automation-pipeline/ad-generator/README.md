# Ad Generator Agent — Component 1

> **Status:** v0.1 — werkend artifact, ready voor Vercel deploy
> **Onderdeel van:** `recruitmentengineer.nl` authority-campagne · `07-automation-pipeline`
> **Plek in flow:** Briefing → **[Ad Generator]** → Higgsfield → Seedance → Meta Ads

Een single-file HTML-artifact (`index.html`) + Vercel serverless function (`api/generate-ad.js`) die een
volledige ad-set genereert via Claude Sonnet 4.6 (`claude-sonnet-4-6`) op basis van 6 input-velden.

---

## Wat het doet

**Input** (form):
- **Thema** — dropdown met 10 voorgedefinieerde authority-thema's (van "AI in recruitment is overhyped" tot "Authority via productie-data")
- **Tone dominant** — radio · 5 modi (Rustig autoriteit / Brutaal direct / Specialist confronterend / Energiek bewijsdrang / Engineer logisch)
- **Tone secundair** — radio · zelfde 5 modi
- **Format** — radio · Reel 9:16 / Feed 1:1 / LinkedIn 16:9 / LinkedIn 4:5
- **Audience tier** — radio · TOFU / MOFU / BOFU
- **Klantbewijs** — checkbox · Veco / Beutech / Euromaster (multi-select; leeg = geen klantnamen in copy)

**Output** (JSON):

```json
{
  "hooks":      ["...", "...", "...", "...", "..."],   // 5 hooks, brutality 1→10
  "bodies":     ["...", "...", "..."],                  // 3 body-variants
  "headlines":  ["...", "...", "...", "...", "..."],    // 5 headlines, ≤40 chars
  "ctas":       ["...", "...", "..."],                  // 3 CTA's, tier-passend
  "higgsfield_brief": "...",                            // Soul 2 / Nano Banana 2 brief
  "seedance_brief":   "...",                            // 5-8s motion brief
  "meta_json":        { "campaign": {...}, "ad_set": {...}, "creative": {...}, "ab_test": {...} }
}
```

De UI rendert elke sectie inline met een **Copy**-knop per blok en een meta-bar bovenaan met de gebruikte input-parameters.

---

## Architectuur

```
[browser]
  ├── index.html          (vanilla HTML+CSS+JS, geen build-step)
  │     └── POST /api/generate-ad  { theme, tone_dominant, tone_secondary, format, tier, clients[] }
  │
  └── api/generate-ad.js  (Vercel serverless · Node 20)
        ├── Validate brief (whitelist on alle velden)
        ├── Rate limit per IP (6/min)
        ├── POST https://api.anthropic.com/v1/messages
        │     model:       "claude-sonnet-4-6"
        │     system:      [{ text: <SYSTEM_PROMPT>, cache_control: { type: "ephemeral" } }]
        │     messages:    [{ role: "user", content: "BRIEF: ..." }]
        ├── Parse JSON uit response (strip ``` fences, find {...})
        └── Shape & pad arrays → return { hooks, bodies, headlines, ctas, hf, sd, meta_json, _meta:{usage} }
```

### Prompt caching

De system prompt (~3KB, brand-bible + 8 schrijfregels + tone-mix + format-mapping + JSON-schema) staat
op een ephemeral cache breakpoint (`cache_control: { type: "ephemeral" }`, 5-min TTL).

- **Eerste call:** volledige system-prompt geüpload (`cache_creation_input_tokens` ≈ 1k)
- **Vervolgcalls binnen 5 min:** 90%+ goedkoper — alleen de korte user-message als input (`cache_read_input_tokens` ≈ 1k)

De serverless function geeft beide tellers terug in `_meta.usage` zodat je in DevTools kunt zien wat
gecached is.

---

## Brand styling

Locked tokens (matchen `06-landing-page/public/index.html`):

| Token | Hex | Gebruik |
|-------|-----|---------|
| Recruitin Oranje | `#FF6B1A` | CTA, accents, badges |
| Blueprint Blauw | `#1E3A5F` | Headers, autoriteit |
| AI Cyaan | `#00D4FF` | Tech-accent, dot-status |
| Warm Grijs | `#F5F0EB` | Body background |
| Diep Zwart | `#1A1A1A` | Body tekst |

Fonts via Google Fonts CDN: **Inter** (300-900) + **JetBrains Mono** (400-700).

UI-patronen overgenomen van de landing: `tech-header` met logo-mark + meta-rij, blueprint-grid background,
`mono`-class voor labels, oranje knipperende status-dot, geen abgeronde hoeken (corporate-tech feel).

---

## Deploy

### Optie A — Standalone Vercel project (aanbevolen voor v0.1)

```bash
cd /Users/wouterarts/projects/recruitmentengineer/07-automation-pipeline/ad-generator
vercel link        # nieuw project: ad-generator-recruitmentengineer
vercel env add ANTHROPIC_API_KEY   # plak je sk-ant-... key
vercel --prod
```

URL: `https://ad-generator-recruitmentengineer.vercel.app/`

CORS in `api/generate-ad.js` heeft die hostname al in de allowlist.

### Optie B — Onder bestaande landing mounten

Verplaats de bestanden naar de landing repo:

```bash
cp index.html               ../../06-landing-page/public/ad-generator/index.html
cp api/generate-ad.js       ../../06-landing-page/api/generate-ad.js
```

In de landing `index.html` link je toe via `/ad-generator`. De `vercel.json` van de landing accepteert
`api/generate-ad.js` automatisch (Vercel scant de `api/` directory). Voeg dan in Vercel UI
`ANTHROPIC_API_KEY` toe als env-var.

> ⚠️ De UI is `noindex, nofollow` (intern gebruik). Wil je het echt publiek maken: zet de robots-tag uit
> én voeg authentication toe (Vercel Password Protection of een eenvoudig HTTP-basic header check).

---

## Environment variabelen

| Var | Verplicht | Doel |
|-----|-----------|------|
| `ANTHROPIC_API_KEY` | ✅ | `sk-ant-...` voor Anthropic Messages API |

Geen andere env-vars nodig. Geen Resend/Pipedrive/Supabase — Component 1 is puur copy-generation.

---

## Sample input → output

**Input:**
```json
{
  "theme": "Het €519k case",
  "tone_dominant": "Rustig autoriteit",
  "tone_secondary": "Engineer logisch",
  "format": "LinkedIn 4:5",
  "tier": "MOFU",
  "clients": ["Euromaster"]
}
```

**Verwachte output (afgekort):**
```json
{
  "hooks": [
    "€519k aan verloren pipeline. In één Excel.",
    "Een klant verloor €519k aan slecht-getimede vacatures. Hier is wat ik vond.",
    "...",
    "...",
    "..."
  ],
  "bodies": [
    "Bij Euromaster opende ik de pipeline-data van Q3.\n\nWat ik vond: 7 vacatures die >90 dagen openstonden...",
    "...",
    "..."
  ],
  "headlines": [
    "€519k pipeline diagnostiek",
    "Pipeline lekken meten",
    "Pipeline > onderbuik",
    "519k verlies, 1 fix",
    "Diagnose voor je pipeline"
  ],
  "ctas": [
    "Boek 30-min pipeline-audit",
    "Lees de case",
    "Download de Stack 2026"
  ],
  "higgsfield_brief": "GENERATOR: Soul 2\nSUBJECT: lichtgrijs wol blazer, wit overhemd, zwarte gebreide das, ronde matte black acetate bril...\nSETTING: blueprint-tafel met laptop en print-outs van pipeline-funnel...\n...",
  "seedance_brief": "INPUT_IMAGE: Higgsfield still hierboven\nDURATION: 7s\nMOTION_TYPE: subtle push-in van 12% over 7s, parallax op blueprint-papier...\n...",
  "meta_json": {
    "campaign": { "objective": "OUTCOME_LEADS", "name": "REC-AUTH-519k-case-MOFU-LI4x5" },
    "ad_set": {
      "audience_tier": "MOFU",
      "geo": ["NL-GE", "NL-OV", "NL-NB"],
      "age_min": 30, "age_max": 60,
      "interests": ["HR Director", "Recruitment", "Industrial automation"],
      "exclusions": ["Recruitment agencies"],
      "placement": ["linkedin_feed"],
      "daily_budget_eur": 10,
      "url_tags": "utm_source=linkedin&utm_medium=paid&utm_campaign=519k-case&utm_content=hook-1"
    },
    "creative": {
      "format": "LinkedIn 4:5",
      "primary_text": "<bodies[0]>",
      "headline": "€519k pipeline diagnostiek",
      "description": "Recruitment Engineering — Stack 2026",
      "cta": "Boek 30-min pipeline-audit",
      "destination_url": "https://recruitmentengineer.nl/?utm_source=linkedin&..."
    },
    "ab_test": { "variants": 3, "rotation": "even", "kill_after_days": 7, "ctr_floor_pct": 1.2, "cpl_ceiling_eur": 8.0 }
  }
}
```

---

## Tests / smoke check

Lokaal:
```bash
vercel dev   # http://localhost:3000
```

Open `http://localhost:3000/`, vul het formulier in, klik **Genereer ad-set**. Output verschijnt rechts.

Curl-only test van de API:
```bash
curl -X POST http://localhost:3000/api/generate-ad \
  -H "Content-Type: application/json" \
  -d '{"theme":"Het €519k case","tone_dominant":"Rustig autoriteit","tone_secondary":"Engineer logisch","format":"LinkedIn 4:5","tier":"MOFU","clients":["Euromaster"]}' | jq
```

Validatie-fouten geven HTTP 400 met `error: "invalid_<veld>"`. Anthropic-fouten geven HTTP 500 met `detail`.
JSON-parse-fouten geven HTTP 502 met `raw` (eerste 1000 chars van Claude's response).

---

## Open follow-ups

- [ ] **Streaming output** — nu wacht UI ~6-12s op volledige response. Switchen naar SSE met
      Anthropic streaming endpoint zou hooks/bodies progressief renderen.
- [ ] **Brief-history / favorites** — localStorage opslag van laatste 10 briefs zodat je snel kunt
      itereren op dezelfde input.
- [ ] **Direct-to-Higgsfield handoff** — knop "Verstuur naar Higgsfield" die `higgsfield_brief` + format
      naar de Higgsfield MCP server stuurt (Component 2).
- [ ] **Direct-to-Meta upload** — knop "Push naar Meta" die `meta_json` valideert + via Meta Marketing API
      een paused ad-set aanmaakt (Component 4).
- [ ] **Tone-mix slider** — i.p.v. dropdown per tone een 60/30/10 visuele slider.
- [ ] **Multi-language** — voeg EN-versie toe (alleen system prompt aanpassen, UI labels in i18n-object).
- [ ] **Response cache layer** — Vercel KV om identieke briefs binnen 24u uit cache te serveren.
