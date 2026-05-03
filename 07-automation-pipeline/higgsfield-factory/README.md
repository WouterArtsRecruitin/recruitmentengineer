# Higgsfield Visual Factory

Template-library for the Recruitin Authority Campaign. Copy-paste these prompts into the Higgsfield UI (Soul 2, Nano Banana Pro, Marketing Studio) or pass them through the Higgsfield MCP. No code here — humans (or the Ad Generator agent) consume these as plain-text strings.

> **Brand DNA = locked.** Every render must match the visual fingerprint below. Use `identity-lock-rules.md` as a pre-flight checklist before sending a batch to render.

---

## What's in this folder

| File | Tool | Use |
|------|------|-----|
| `SET-A-hero-portraits.md` | Soul 2 | 10 hero portraits of Ing. W. Arts in industrial / authority settings |
| `SET-B-brand-visuals.md` | Nano Banana Pro | Data viz, quote cards, carousel covers, lead magnet cover, LinkedIn cover banner |
| `SET-C-marketing-studio.md` | Marketing Studio | Ad-format-specific creatives (9:16, 1:1, 16:9, 4:5) for Meta + LinkedIn |
| `identity-lock-rules.md` | All | Reference checklist — what MUST stay consistent across every render |

---

## Naming convention

Output files should follow: `{set}-{template-id}-{variable}-{date}.{ext}`

Examples:
- `setA-portrait-01-productiehal-arms-crossed-2026-05-03.png`
- `setB-quote-card-helft-werkt-niet-2026-05-03.png`
- `setC-reel-916-hook-card-cold-tofu-2026-05-03.png`

Store in `02-higgsfield-assets/` per existing repo convention. Each asset that becomes a Seedance input also lives in `seedance-inputs/` (mirrored copy).

---

## Brand-DNA constraints summary

**Colors (locked, every render must include or grade-toward at least 2 of these):**
- `#FF6B1A` — Recruitin oranje (accent / CTA only, max 15% of frame)
- `#1E3A5F` — Blueprint blauw (authority / type background)
- `#00D4FF` — AI cyaan (sparingly, only data-viz)
- `#F5F0EB` — Warm grijs (light backgrounds)
- `#1A1A1A` — Deep zwart (body type)

**Wouter visual DNA (locked across every Soul 2 render):**
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

## How to use (Higgsfield UI)

1. Open Soul 2 / Nano Banana Pro / Marketing Studio
2. Paste prompt block (everything between the triple-backticks)
3. Replace `[VARIABLES]` (e.g. `[SETTING]`, `[POSE]`, `[QUOTE]`) with the values from the template's "Variables to fill" list
4. Set aspect ratio per template
5. Run + check against `identity-lock-rules.md` checklist
6. Reject + regen if any locked element drifts

## How to use (programmatic via Ad Generator agent)

The agent writes a JSON brief like:
```json
{
  "tool": "soul2",
  "template": "setA.portrait-03",
  "variables": { "setting": "blueprint-tafel", "pose": "examining-blueprint" },
  "aspect": "4:5"
}
```
Then renders the prompt by substitution and submits via Higgsfield MCP.

---

## Total prompt-count in this factory

- Set A — 10 hero portraits
- Set B — 8 brand visuals (3 data-viz, 1 quote-card template, 2 carousel covers, 1 PDF cover, 1 LinkedIn banner)
- Set C — 8 marketing-studio ads (2 per format × 4 formats)
- **Total: 26 templates** + 1 identity-lock reference

---

## Version

v1.0 — Mei 2026 — initial library locked to brand bible v1.3 (light grey blazer + round acetate + salt-and-pepper).
