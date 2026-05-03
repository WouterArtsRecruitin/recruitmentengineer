# Seedance Motion Factory

Template-library for **Seedance 2.0** (image-to-video, accessed via Higgsfield MCP). Takes Higgsfield Soul-2 stills as input and generates 5–8s videos with identity preservation. No code here — these are prompt templates for humans (or the Ad Generator agent) to copy-paste.

> **Tool:** Seedance 2.0 — image-to-video, 5–8s clips, identity preservation across frames, locked motion-types only (no complex montage in Fase 1).

> **Pre-flight:** read `identity-preservation-rules.md` before submitting. The whole point of this factory is that Wouter's face / hair / blazer / glasses do NOT drift between frame 1 and frame 240.

---

## Workflow

```
HIGGSFIELD SOUL-2 STILL (Soul-ID 948dbc10-ba8d-406c-b771-e15610ae8674)
    ↓ approved + QA-checked
SEEDANCE INPUT (mirrored to seedance-factory/inputs/)
    ↓
SELECT MOTION TEMPLATE (M1–M6) per format-cheatsheet.md
    ↓
SUBMIT: still + motion prompt + identity-preservation string
    ↓
RENDER: 5–8s video clip, 24fps or 30fps
    ↓
QA: pre-flight identity-preservation checklist (rules.md)
    ↓
EXPORT: 9:16 / 1:1 / 16:9 / 4:5 per ad-format
    ↓
HANDOFF to Meta Ads MCP / LinkedIn Ads
```

The Soul-2 still acts as **frame 1**. Seedance generates 5–8 seconds of subtle motion forward from that frame, preserving the face/wardrobe via the still as anchor.

**Output budget per clip:** 5–8 seconds. Subtle motion only — push-in, slow zoom, parallax, gaze-shift, tool-in-hand, environmental. **No cutaway scenes, no complex montage** in Fase 1.

---

## What's in this folder

| File | Use |
|------|-----|
| `motion-templates.md` | 6 locked motion templates (M1–M6) — push-in, zoom-out, parallax, subject-shift, tool-in-hand, environmental |
| `identity-preservation-rules.md` | Hard rules + sample failure modes to reject (face-morph, blazer-shift, mouth-open-when-shouldn't-be) |
| `format-cheatsheet.md` | Which template fits which ad-format and audience tier (Reel / Feed / LinkedIn × TOFU / MOFU / BOFU) |
| `inputs/` | Mirror folder for approved Higgsfield Soul-2 stills used as motion inputs (created on first use) |

---

## Template index (motion-templates.md)

| ID | Motion | Duration | Best for |
|----|--------|----------|----------|
| M1 | Push-in slow | 6s | BOFU LinkedIn 16:9 (authority) |
| M2 | Slow zoom-out reveal | 7s | LinkedIn case-study 16:9 |
| M3 | Parallax pan | 6s | TOFU Reel 9:16 / Feed-large 4:5 |
| M4 | Subject-shift gaze | 5s | MOFU Feed 1:1 (engagement) |
| M5 | Tool-in-hand | 6s | MOFU/BOFU 4:5 portrait+stat |
| M6 | Environmental motion | 8s | TOFU Feed 1:1 typography ads |

---

## Naming convention

Output files: `{format}-{template}-{tier}-{variant}-{date}.{ext}`

Examples:
- `reel916-M3-parallax-tofu-cold-2026-05-03.mp4`
- `linkedin169-M1-pushin-bofu-leadmagnet-2026-05-03.mp4`
- `feed11-M6-environmental-tofu-typography-2026-05-03.mp4`

Store in `02-higgsfield-assets/seedance-clips/` (or via the Ad Generator's automated pipeline output).

---

## Output format recommendations

| Format | Resolution | Container | Codec | Bitrate | Audio |
|--------|-----------|-----------|-------|---------|-------|
| 9:16 Reel | 1080×1920 | MP4 | H.264 | 6–8 Mbps | None (silent), or 48kHz AAC stereo if voice-over |
| 1:1 Feed | 1080×1080 | MP4 | H.264 | 4–6 Mbps | None |
| 16:9 LinkedIn | 1920×1080 | MP4 | H.264 | 8–10 Mbps | None or 48kHz AAC stereo |
| 4:5 Feed-large | 1080×1350 | MP4 | H.264 | 6–8 Mbps | None |

**Frame rate:** 30fps default for social. 24fps acceptable for cinematic LinkedIn long-form. Stay consistent within a campaign-set.

**Loop-friendly endings** for Reel/Feed: end frame should match start frame visually (subtle motion, no jump-cut at loop point).

---

## Brand-DNA constraints (inherited from Higgsfield factory)

All Seedance outputs MUST preserve:
- Light grey wool blazer (no color drift toward navy/black/brown)
- White shirt + black knit tie (no pattern, no silk-shift)
- Round-frame matte black acetate glasses (always present, never wire/rectangular)
- Salt-and-pepper hair, side-parted (no buzz, no slick)
- 3-day salt-and-pepper stubble
- Calm authoritative expression (mouth closed or barely-parted, **NEVER broad smile** appearing mid-clip)
- Real skin texture (no beauty-filter morph)
- Teal-orange cinematic grade matching the source still

See `identity-preservation-rules.md` for full reject-criteria.

---

## Identity preservation — vergelijk SET-A locked-DNA

The Soul-2 still already has the right Soul-ID baked in. Seedance's job is to NOT mess that up. Common failures:
- **Face morph mid-clip** (frame 1 looks right, frame 120 looks like a different person)
- **Mouth-open when shouldn't be** (motion adds a "talking" frame even though the prompt is silent)
- **Blazer-color shift** (frame 1 light grey → frame 180 navy because of motion-blur color bleed)
- **Hand-anatomy errors** (extra fingers appearing on motion frames where they weren't in the still)
- **Glasses-frame change** (round acetate becomes thin-wire on rapid motion frames)

Hard reject any clip with face morph, blazer drift, or mouth-state break. See `identity-preservation-rules.md`.

---

## Version

v1.0 — Mei 2026 — initial library, locked to brand bible v1.4, mirrors higgsfield-factory v2.0 (Soul-ID `948dbc10-ba8d-406c-b771-e15610ae8674`).
