# Higgsfield Visual Factory — Soul-2 Powered

Template-library for the Recruitin Authority Campaign. Copy-paste these prompts into the Higgsfield UI (Soul 2 / Nano Banana 2 / Marketing Studio) or pass them through the Higgsfield MCP. No code here — humans (or the Ad Generator agent) consume these as plain-text strings.

> **Brand DNA = locked.** Every render must match the visual fingerprint below. Use `identity-lock-rules.md` as a pre-flight checklist before sending a batch to render.

---

## What is Higgsfield Soul-2?

Higgsfield **Soul-2** is a character-locked image-generation model. You train a "Soul" once on real photos of a person, and from that point forward every render automatically preserves face geometry, micro-expression range, skin texture, and hair pattern across new prompts. No more dual-reference fragility — no more uploading 2–3 anchor photos per render hoping for likeness.

**For this campaign:**

| Field | Value |
|-------|-------|
| **Soul-ID** | `948dbc10-ba8d-406c-b771-e15610ae8674` |
| **Soul name** | Ing W Arts Recruitment Engineer |
| **Status** | Trained + ready (May 2026) |

This Soul-ID **MUST** be passed in every Set-A hero portrait + every Set-C portrait-based ad. Set-B brand-visual-only assets (data-viz, typography-only carousel covers, abstract PDF cover) skip Soul and use **Nano Banana 2** instead — they don't need a face-lock.

### Why Soul-2 over dual-reference Nano Banana

- **Speed:** ~30 sec/render vs ~2 min with dual-reference upload + retry loops
- **Identity preservation:** locked at training-time, drift = near-zero across 100+ renders
- **Cost:** ~3–5 credits/render (Soul) vs 8–12 credits (dual-ref iterations)
- **Consistency across a campaign-set:** all 10 Set-A portraits feel like one shoot, not 10 different AI guesses

---

## How to invoke Soul-ID

### Higgsfield UI (manual)
1. Open Higgsfield → Soul 2 tab
2. Pick Soul `Ing W Arts Recruitment Engineer` from the dropdown (this auto-fills `soul_id: 948dbc10-...`)
3. Paste the prompt block from any Set-A template
4. Fill `[SETTING]` `[POSE]` `[LIGHTING]` `[CAMERA]` from the template's variables-matrix
5. Set aspect ratio per template
6. Render → check against `identity-lock-rules.md` checklist
7. Reject + regen if any locked element drifts

### Higgsfield MCP (programmatic)
Pass `soul_id` explicitly in the request payload:
```
{
  "tool": "soul2",
  "soul_id": "948dbc10-ba8d-406c-b771-e15610ae8674",
  "template": "setA.portrait-03",
  "variables": { "setting": "blueprint-tafel", "pose": "examining-blueprint" },
  "aspect": "4:5"
}
```

### Higgsfield API (curl-style)
```
POST /v1/soul2/generate
Headers: Authorization: Bearer <HIGGSFIELD_API_KEY>
Body: {
  "soul_id": "948dbc10-ba8d-406c-b771-e15610ae8674",
  "prompt": "<rendered prompt-string from Set-A template>",
  "negative_prompt": "<from template>",
  "aspect_ratio": "4:5"
}
```

---

## What's in this folder

| File | Tool | Use |
|------|------|-----|
| `SET-A-hero-portraits-soul.md` | Soul 2 | 10 hero portraits, Soul-ID locked. ALL portraits MUST reference Soul-ID `948dbc10-ba8d-406c-b771-e15610ae8674`. |
| `SET-A-hero-portraits.md` | Soul 2 (legacy) | Original dual-ref version. Kept for archive. New work = use SET-A-hero-portraits-soul.md. |
| `SET-B-brand-visuals.md` | Nano Banana 2 | 8 brand visuals: data-viz, quote-card template, carousel covers, PDF cover, LinkedIn banner. **No portraits → no Soul-ID.** |
| `SET-C-marketing-studio.md` | Marketing Studio (Soul-locked) | 8 ad-format-specific portrait creatives. Soul-ID required for every variant with a face. |
| `identity-lock-rules.md` | All | Reference checklist — what MUST stay consistent across every render |

---

## Naming convention

Output files: `{set}-{template-id}-{variable}-{date}.{ext}`

Examples:
- `setA-portrait-01-productiehal-arms-crossed-2026-05-03.png`
- `setB-quote-card-helft-werkt-niet-2026-05-03.png`
- `setC-reel-916-hook-card-cold-tofu-2026-05-03.png`

Store in `02-higgsfield-assets/` per existing repo convention. Each asset that becomes a Seedance input also lives in `seedance-factory/inputs/` (mirrored copy).

---

## Brand-DNA constraints summary

**Colors (locked, every render must include or grade-toward at least 2 of these):**
- `#FF6B1A` — Recruitin oranje (accent / CTA only, max 15% of frame)
- `#1E3A5F` — Blueprint blauw (authority / type background)
- `#00D4FF` — AI cyaan (sparingly, only data-viz)
- `#F5F0EB` — Warm grijs (light backgrounds)
- `#1A1A1A` — Deep zwart (body type)

**Wouter visual DNA (Soul-2 handles this — these notes describe what the trained Soul preserves):**
- Light grey wool blazer
- White shirt (no pattern)
- Black knit tie (textured)
- Round-frame matte black acetate glasses (statement piece, vintage intellectual)
- Salt-and-pepper hair, side-parted, neat
- 3-day stubble, salt-and-pepper
- Dutch male, late 40s, athletic-slim, light European complexion
- Calm authoritative gaze, mouth closed or barely-parted — **never broad smile, never toothy grin, never neutral-corporate face**
- No jewelry, no watch in frame unless setting demands it

**Composition / lighting:**
- 50–85mm equivalent, shallow DoF (f/2.0–f/2.8)
- Documentary-editorial style (Euromaster Sora reference)
- Teal-orange cinematic grade by default
- Real skin texture — never beauty-filter smooth
- Industrial / on-location settings, never generic stock office

**Trust markers (when contextual):** Veco · Beutech · Euromaster — typography-only, never actual logos. Use exactly once per asset, never duplicate.

**Forbidden in every render:**
- Aebi Schmidt anything (logos, machines, branding) — banned
- Casual hoodie / t-shirt
- Dark navy or black suit
- Generic stock-photo office / corporate boardroom
- Stock-photo grin / smiling-into-camera fake
- AI avatars / digital twins / phone-snapshot wide angle / beauty-filter smoothness
- Multiple people in hero portraits (unless template explicitly allows)
- Visible readable text on screens / whiteboards (intentionally illegible)

---

## Production flow

```
PICK TEMPLATE (Set A / Set B / Set C)
    ↓
FILL VARIABLES ([SETTING] / [POSE] / [LIGHTING] / [CAMERA] / [ASPECT])
    ↓
SUBMIT WITH SOUL-ID (Set A / Set C portrait variants only)
    ↓
RECEIVE IMAGE
    ↓
QA via identity-lock-rules.md checklist
    ↓
REJECT + REGEN if any locked element drifts
    ↓
EXPORT to 02-higgsfield-assets/<subfolder>/
    ↓
MIRROR to seedance-factory/inputs/ (if motion-bound)
```

---

## Total prompt-count in this factory

- Set A — 10 hero portraits (Soul-ID locked)
- Set B — 8 brand visuals (no portrait → Nano Banana 2)
- Set C — 8 marketing-studio ads (Soul-ID locked on portrait variants)
- **Total: 26 templates** + 1 identity-lock reference

---

## Version

v2.0 — Mei 2026 — Soul-ID-locked rewrite. Soul `948dbc10-ba8d-406c-b771-e15610ae8674` (Ing W Arts Recruitment Engineer) trained + production-ready. Replaces v1.0 dual-ref workflow.
