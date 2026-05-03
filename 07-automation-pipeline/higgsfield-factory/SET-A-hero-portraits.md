# SET A — Hero Portraits (Soul 2)

10 hero portraits of Ing. W. Arts. Each portrait pairs one `[SETTING]` with one `[POSE]` from the matrices below. Use `soul_id` from your trained Soul character.

> **Pre-flight:** read `identity-lock-rules.md` first. Reject any render where a locked element drifts.

---

## Variables matrix

### `[SETTING]` (one per portrait, in order 01-10)
| # | Setting label | What's in frame |
|---|--------------|------------------|
| 01 | productiehal | Modern industrial production hall — CNC machines, overhead steel structure, cool blue light |
| 02 | werkplaats | Real metalworking workshop floor (Veco / Beutech vibe) — welding station, milling machine, sparks distance |
| 03 | blueprint-tafel | Wooden workbench with large engineering blueprints unfurled, mechanical pencils, coffee |
| 04 | monitor-setup | Dark wood desk, three monitors with data dashboards, recruitment analytics, code (illegible) |
| 05 | klant-locatie | On-location at client site — assembly line backdrop, hi-vis vests passing in soft blur |
| 06 | conferentie | Boardroom-style intake meeting — polished concrete table, seated, technical drawings on wall behind |
| 07 | podium | TED-talk-style stage mid-presentation, atmospheric haze, single warm spotlight |
| 08 | fabrieks-vloer | Wide industrial corridor between production halls, vertical steel beams, daylight windows |
| 09 | magazijn-rek | Logistics warehouse — high steel racking with parts bins, pallet jack visible in distance |
| 10 | kantoor-deurpost | Frame of doorway between meeting room and corridor — half in, half out, contemplative |

### `[POSE]` (one per portrait, vary across the set)
| # | Pose label | Body language |
|---|-----------|---------------|
| 01 | arms-crossed | Arms crossed at chest, standing, slight three-quarter angle to camera |
| 02 | pointing-at-screen | One hand pointing toward an off-screen monitor, head turned to indicate |
| 03 | holding-laptop | Laptop balanced on forearm, lid open, looking up from screen toward camera |
| 04 | in-conversation | Mid-gesture talking with off-screen counterpart, hand expressing point, eyes off-camera |
| 05 | looking-at-camera | Direct eye contact with camera, hands relaxed at sides, head straight or slight tilt |
| 06 | three-quarter | Body angled 45° to camera, head turned to look directly at lens |
| 07 | leaning-on-desk | Hands flat on desk/blueprint, leaning forward slightly, weight on arms |
| 08 | walking-away | Mid-stride moving away from camera, looking back over shoulder |
| 09 | examining-blueprint | Both hands on blueprint, head down slightly, examining a specific detail |
| 10 | conferring-with-engineer | Half-profile talking with another engineer (off-frame or out-of-focus), gesturing with one hand |

---

## Pairing matrix (these are the 10 final portraits)

| # | Setting | Pose | Aspect | Use |
|---|---------|------|--------|-----|
| 01 | productiehal | arms-crossed | 4:5 | LinkedIn hero, manifesto post |
| 02 | werkplaats | examining-blueprint | 4:5 | Long-form klantcase opener |
| 03 | blueprint-tafel | leaning-on-desk | 4:5 | Authority post / lead magnet |
| 04 | monitor-setup | pointing-at-screen | 16:9 | Banner / Reel cover |
| 05 | klant-locatie | three-quarter | 4:5 | Trust marker post (Veco) |
| 06 | conferentie | in-conversation | 16:9 | Boardroom authority / 16:9 ad |
| 07 | podium | looking-at-camera | 16:9 | Speaker bio / event pitch |
| 08 | fabrieks-vloer | walking-away | 16:9 | Wide hero / Seedance push-in input |
| 09 | magazijn-rek | holding-laptop | 1:1 | Profile photo alternate / square feed |
| 10 | kantoor-deurpost | conferring-with-engineer | 4:5 | Behind-the-scenes / nurture content |

---

## Master prompt template

Use this template, substitute `[SETTING]` + `[POSE]` from the matrix above. Lighting cues per setting are listed below — splice them into the prompt at `[LIGHTING]`.

```
Soul 2 — soul_id: [TRAINED_SOUL_ID]
Aspect: [ASPECT]

Editorial documentary portrait of Ing. W. Arts in [SETTING_DESCRIPTION].
Wearing a light grey wool blazer over a white shirt with a textured
black knit tie, round-frame matte black acetate glasses (thick rim,
vintage intellectual statement piece). Salt-and-pepper hair, side-
parted neat. 3-day salt-and-pepper stubble. [POSE_DESCRIPTION].
Calm authoritative gaze, mouth closed or barely-parted, mid-thought
neutral-engaged expression — NOT smiling, NO toothy grin, NO stock-
photo grin.

[LIGHTING]

Color grade: teal-orange cinematic, subtle Recruitin orange (#FF6B1A)
warm accent in highlights, blueprint-blue (#1E3A5F) cool tones in
shadows. Real skin texture visible, pores, micro-detail.

Lens: 85mm portrait equivalent, shallow depth of field f/2.0–f/2.8.
Documentary editorial style, hyperrealistic 8K. Trust-marker context:
Veco / Beutech / Euromaster vibe (typography-only if any text appears,
intentionally illegible / out-of-focus, no actual brand logos).

NEGATIVE: Aebi Schmidt branding, navy or black blazer, hoodie, casual,
rectangular glasses, wire-rim, no glasses, broad smile, toothy grin,
fake influencer face, plastic skin, beauty-filter, generic stock
office, generic LinkedIn headshot, multiple people in foreground,
deformed hands, extra fingers, AI artifacts, watermark, readable
text, brown beard, full beard, clean-shaven, slick-back hair, buzz
cut, navy turtleneck, dark suit.
```

---

## Per-portrait specifics

### Portrait 01 — productiehal × arms-crossed (4:5)

```
SETTING_DESCRIPTION: a modern industrial production hall, with out-
of-focus CNC machines and overhead steel structure receding into
shallow background

POSE_DESCRIPTION: standing centered, arms crossed at chest, slight
three-quarter angle to camera, head turned to face lens

LIGHTING: Cool blue overhead industrial fluorescent fill, warm amber
key light from upper-right (orange #FF6B1A practical accent), strong
teal-orange cinematic grade, slight haze in background.
```

### Portrait 02 — werkplaats × examining-blueprint (4:5)

```
SETTING_DESCRIPTION: a real metalworking workshop floor (Veco /
Beutech-style), out-of-focus welding station and milling machine
in the distance, faint orange welding glow far background

POSE_DESCRIPTION: bent slightly forward over a large unfurled
engineering blueprint laid on a workbench, both hands flat on
the paper, head down examining a specific schematic detail,
glasses catching light

LIGHTING: Cool industrial overhead fill (#1E3A5F-ish blueprint blue),
warm orange welding glow accent on right side (#FF6B1A), Rembrandt
side-key on face from window-left, strong teal-orange grade.
```

### Portrait 03 — blueprint-tafel × leaning-on-desk (4:5)

```
SETTING_DESCRIPTION: a warm-toned engineering office with a wooden
workbench unfurled with a large blueprint, mechanical pencils, an
espresso cup, architectural drawings pinned softly out-of-focus
behind

POSE_DESCRIPTION: leaning forward, both hands flat on the blueprint,
weight on arms, body angled three-quarter, head turned directly to
camera with focused intelligent gaze

LIGHTING: Diffused tungsten warm key from upper-left (3200K), soft
amber fill, cool blue rim light from window-right (#1E3A5F accent).
Warm cinematic grade, subtle teal in shadows only.
```

### Portrait 04 — monitor-setup × pointing-at-screen (16:9)

```
SETTING_DESCRIPTION: a sleek dark wood desk with three large monitors
showing data dashboards, recruitment analytics, abstract code (text
intentionally illegible / blurred), engineering bookshelf softly out
of focus behind

POSE_DESCRIPTION: seated, body turned three-quarter to camera, one
hand pointing toward the central monitor, head turned to indicate
the data, gaze following the gesture

LIGHTING: Soft warm key from front-left, cool monitor glow on face
(#00D4FF cyan accent picked up subtly), single amber pendant light
above desk, cinematic teal-orange grade, deep shadows.
```

### Portrait 05 — klant-locatie × three-quarter (4:5)

```
SETTING_DESCRIPTION: on-location at a client industrial site, deep
out-of-focus assembly line backdrop with hi-vis-vest workers passing
in soft motion blur, large factory windows letting in cool daylight

POSE_DESCRIPTION: standing grounded, body angled 45° to camera, head
turned to look directly at lens, hands relaxed at sides, leather
portfolio under one arm

LIGHTING: Cool daylight from large factory windows (#1E3A5F blue
tones), warm amber tungsten practicals overhead, Rembrandt key on
face, strong teal-orange cinematic grade.
```

### Portrait 06 — conferentie × in-conversation (16:9)

```
SETTING_DESCRIPTION: boardroom-style client intake meeting, polished
concrete table, technical drawings pinned to wall behind softly out
of focus, modern industrial loft aesthetic

POSE_DESCRIPTION: seated at table angled to camera, mid-gesture
explaining a point with one hand, looking off-camera-left toward
an off-frame counterpart, focused engaged expression

LIGHTING: Diffused soft key from upper-left (cool daylight), warm
amber backlight from window behind subject creating rim on shoulders
(#FF6B1A accent), shadows hold blueprint-blue.
```

### Portrait 07 — podium × looking-at-camera (16:9)

```
SETTING_DESCRIPTION: TED-talk-style dark stage mid-presentation,
"Recruitment Engineering" projected text on screen behind subject
(small, blurred, intentionally illegible), atmospheric haze

POSE_DESCRIPTION: standing center-stage, body half-profile to camera,
one hand gesturing at chest height, head turned directly to lens,
clicker in opposite hand, calm authoritative direct gaze

LIGHTING: Single warm spotlight from above-front catching face and
shoulders (#FF6B1A warm accent), atmospheric haze, deep blueprint-
blue stage shadows, high-contrast cinematic grade f/2.0.
```

### Portrait 08 — fabrieks-vloer × walking-away (16:9)

```
SETTING_DESCRIPTION: wide industrial corridor between production
halls, vertical steel beams, large factory windows letting in cool
daylight, slight haze

POSE_DESCRIPTION: mid-stride, walking away from camera, looking back
over shoulder toward lens with focused expression, leather portfolio
under one arm — captures forward motion + the look-back

LIGHTING: Cool blue overhead industrial fill, warm amber accents
from side-corridor openings (#FF6B1A), motion-capture aesthetic,
slight motion blur on background, sharp on subject.
```

### Portrait 09 — magazijn-rek × holding-laptop (1:1)

```
SETTING_DESCRIPTION: logistics warehouse aisle with high steel
racking, parts bins receding into shallow background, pallet jack
visible in distance, soft cool light

POSE_DESCRIPTION: standing, laptop balanced on forearm with lid
open, looking up from screen directly at camera with engaged
focused expression, free hand resting on the laptop edge

LIGHTING: Cool overhead warehouse fluorescent fill (#1E3A5F-leaning),
warm amber practical light from end of aisle, Rembrandt side-key
softening face, teal-orange cinematic grade.
```

### Portrait 10 — kantoor-deurpost × conferring-with-engineer (4:5)

```
SETTING_DESCRIPTION: in the frame of a doorway between a meeting
room and an industrial corridor — half in, half out — production
floor visible softly out-of-focus through the door behind

POSE_DESCRIPTION: standing in doorway, half-profile to camera,
talking with another engineer (out-of-focus shoulder visible at
frame edge), gesturing with one hand to make a point, glasses
catching light

LIGHTING: Warm tungsten interior light spilling from meeting room
behind (#FF6B1A warm), cool industrial daylight from corridor
(#1E3A5F blue), Rembrandt split-key on face from contrast between
the two zones, strong teal-orange cinematic grade.
```

---

## Output handoff

After approval, copy each rendered still to:
- `02-higgsfield-assets/hero-portraits/setA-portrait-{NN}-{setting}-{pose}-{date}.png`
- `07-automation-pipeline/seedance-factory/inputs/` (mirrored — these are the still inputs for Set M motion templates)
