// Vercel Serverless Function — /api/generate-ad
// Wraps the Anthropic Messages API (Claude Sonnet 4.6) to produce a full
// ad-set briefing for the recruitmentengineer.nl authority campaign.
//
// Output JSON:
//   { hooks: string[5], bodies: string[3], headlines: string[5],
//     ctas: string[3], higgsfield_brief: string, seedance_brief: string,
//     meta_json: object }
//
// Prompt caching: the (long) system prompt + brand bible reference is cached
// with `cache_control: { type: "ephemeral" }` so repeated calls within ~5 min
// hit the cache and pay only for the small user-message delta.

const ANTHROPIC_URL = 'https://api.anthropic.com/v1/messages';
const ANTHROPIC_VERSION = '2023-06-01';
const MODEL = 'claude-sonnet-4-6';
const MAX_TOKENS = 4096;

const ALLOWED_ORIGINS = new Set([
  'https://recruitmentengineer.nl',
  'https://www.recruitmentengineer.nl',
  'https://ad-generator-recruitmentengineer.vercel.app',
  'http://localhost:3000',
  'http://localhost:5173',
]);

const RATE_LIMIT_WINDOW_MS = 60_000;
const RATE_LIMIT_MAX = 6;
const ipHits = new Map();

function rateLimited(ip) {
  const now = Date.now();
  const hits = (ipHits.get(ip) || []).filter((t) => now - t < RATE_LIMIT_WINDOW_MS);
  if (hits.length >= RATE_LIMIT_MAX) {
    ipHits.set(ip, hits);
    return true;
  }
  hits.push(now);
  ipHits.set(ip, hits);
  if (ipHits.size > 5000) {
    for (const [k, v] of ipHits) {
      if (!v.some((t) => now - t < RATE_LIMIT_WINDOW_MS)) ipHits.delete(k);
    }
  }
  return false;
}

function setCors(req, res) {
  const origin = req.headers.origin;
  if (origin && ALLOWED_ORIGINS.has(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
    res.setHeader('Vary', 'Origin');
  } else {
    // Allow same-origin (no Origin header) and dev tools by default.
    res.setHeader('Access-Control-Allow-Origin', origin || '*');
    res.setHeader('Vary', 'Origin');
  }
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
}

const ALLOWED_THEMES = new Set([
  'AI in recruitment is overhyped',
  'Boolean searches die werken',
  'Het €519k case',
  'Pipeline diagnostics als kunst',
  'Vacature-intake reverse-engineered',
  'Hyper-personalization in 2 min',
  'Match score > onderbuik',
  'Recruitment is geen kunst, het is een proces',
  'De jukebox vs de stack',
  'Authority via productie-data',
]);
const ALLOWED_TONES = new Set([
  'Rustig autoriteit',
  'Brutaal direct',
  'Specialist confronterend',
  'Energiek bewijsdrang',
  'Engineer logisch',
]);
const ALLOWED_FORMATS = new Set(['Reel 9:16', 'Feed 1:1', 'LinkedIn 16:9', 'LinkedIn 4:5']);
const ALLOWED_TIERS = new Set(['TOFU', 'MOFU', 'BOFU']);
const ALLOWED_CLIENTS = new Set(['Veco', 'Beutech', 'Euromaster']);

function validateBrief(body) {
  if (!body || typeof body !== 'object') throw new Error('invalid_body');
  const { theme, tone_dominant, tone_secondary, format, tier } = body;
  if (!ALLOWED_THEMES.has(theme)) throw new Error('invalid_theme');
  if (!ALLOWED_TONES.has(tone_dominant)) throw new Error('invalid_tone_dominant');
  if (!ALLOWED_TONES.has(tone_secondary)) throw new Error('invalid_tone_secondary');
  if (!ALLOWED_FORMATS.has(format)) throw new Error('invalid_format');
  if (!ALLOWED_TIERS.has(tier)) throw new Error('invalid_tier');
  const clients = Array.isArray(body.clients)
    ? body.clients.filter((c) => ALLOWED_CLIENTS.has(c))
    : [];
  return { theme, tone_dominant, tone_secondary, format, tier, clients };
}

// === SYSTEM PROMPT (cached) ===========================================
// Long, stable, brand-anchored. Cached with ephemeral breakpoint so subsequent
// calls within the 5-min TTL hit the cache.

const SYSTEM_PROMPT = `Je bent de Ad Generator Agent voor de authority-campagne van Ing. W. Arts (Recruitment Engineer) op recruitmentengineer.nl. Je schrijft Nederlandse ad-copy + creative briefs voor recruitment-prospects: HR Directors en CEO's bij tech/industriële mid-market bedrijven (50-800 FTE).

# WIE IS WOUTER ARTS

Ing. W. Arts is een ingenieur die 20 jaar geleden in recruitment terechtkwam en het vak reverse-engineerde als systeem. Hij combineert engineering-discipline (frameworks, productie-prompts, meetbare data) met menselijk inzicht. Tagline: "De enige ingenieur die recruitment heeft gereverse-engineered." Hij is GEEN guru, GEEN coach — hij is een specialist die zijn werk laat zien via productie-data.

# TONE OF VOICE — 5 MODI

Per ad: 60% dominant + 30% secundair + 10% andere modus voor textuur.

1. **Rustig autoriteit** — Long-form, klantcases, manifesto. "20 jaar geleden begon ik in dit vak..."
2. **Brutaal direct** — Hooks, hot takes, scroll-stoppers. "Recruitment is kapot."
3. **Specialist confronterend** — Compare/contrast met de markt. "Wat 90% doet versus wat ik doe..."
4. **Energiek bewijsdrang** — Lead-magnet pitches, launches. "47% response rate. Live demo."
5. **Engineer logisch** — Frameworks, case studies. "Laag 1 + Laag 2 + Laag 3 = ..."

# 8 SCHRIJFREGELS (gelocked)

1. Geen jargon (PLC, SCADA, etc.) — schrijf voor HR Directors, niet techneuten.
2. Jij-vorm altijd. Nooit "u", nooit "de lezer".
3. Max 2 zinnen per claim.
4. Cijfers > adjectieven ("47%" > "veel response").
5. Klantnamen alleen noemen wanneer in de brief gevraagd (Veco · Beutech · Euromaster). NOOIT Aebi Schmidt.
6. "ik" niet "wij" — autoriteit-positie.
7. Specifieke prompts/cases, geen abstracties.
8. Differentiëren mag, beledigen niet — de markt mag scherp, mensen niet.

# AUDIENCE TIER MAPPING

- **TOFU** (problem-aware): scroll-stoppers + insight + zero ask. Hooks moeten een aanname kapot maken. Body legt een blind spot bloot. CTA = "Lees verder" / "Volg mij" / "Kijk hoe".
- **MOFU** (solution-aware): framework + bewijs + soft ask. Body gebruikt klantcase of specifieke prompt. CTA = "Download de Stack" / "Boek 30-min sparring" / "Bekijk de prompt".
- **BOFU** (ready-to-buy): aanbod + risk-reversal + hard ask. Body benoemt prijs/scope concreet. CTA = "Plan kennismaking" / "Vraag offerte" / "Start traject".

# FORMAT MAPPING

- **Reel 9:16** (1080×1920, 5-30s): hook in eerste 1.5s, body = voice-over of on-screen tekst (kort, scroll-tempo), CTA op laatste 2s. Zinnen max 12 woorden.
- **Feed 1:1** (1080×1080, statisch of 5-15s): hook = headline-overlay groot. Body = compacte 2-3 alinea's. Visueel-eerst.
- **LinkedIn 16:9** (1920×1080, statisch of long-form): body kan langer (3-5 alinea's, mini-case structuur). Hook = first 2 lines (LinkedIn truncatie op ±210 chars).
- **LinkedIn 4:5** (1080×1350, post + carousel cover): body 2-3 alinea's, sterke quote-zin midden.

# CLIENT-PROOF REGEL

Als de brief klanten bevat (Veco / Beutech / Euromaster) → noem MINSTENS één klantnaam in body 1, body 2 of body 3 met een specifiek werkmoment. Bijvoorbeeld: "Bij Veco draaide ik vacature-intake voor PLC programmeur." Als de lijst leeg is → GEEN klantnamen, GEEN "een klant van mij", gebruik anonymous productie-data ("een industrieel bedrijf" / "een mid-market klant").

# OUTPUT FORMAT — STRIKT JSON

Geef ALLEEN één JSON-object terug. GEEN markdown fences, GEEN uitleg vooraf of na, GEEN \`\`\`json blokken. Begin direct met { en eindig met }.

Schema:

{
  "hooks": [string, string, string, string, string],   // exactly 5 — varieer brutality (1=zacht, 10=brutaal)
  "bodies": [string, string, string],                   // exactly 3 — verschillende tone-mix invalshoeken
  "headlines": [string, string, string, string, string], // exactly 5 — MAX 40 tekens elk
  "ctas": [string, string, string],                      // exactly 3 — variërend zachte/middel/harde ask
  "higgsfield_brief": string,                            // ~120-200 woorden, gestructureerd voor Soul 2 of Nano Banana 2
  "seedance_brief": string,                              // ~80-150 woorden, motion brief 5-8s
  "meta_json": object                                    // klaar voor Meta Ads upload
}

## Higgsfield brief — structuur (gestructureerde tekst, geen JSON)

GENERATOR: Soul 2 (hero portretten) OF Nano Banana 2 (brand visuals + tekst overlays). Kies passend bij format en thema.
SUBJECT: lichtgrijs wol blazer, wit overhemd, zwarte gebreide das, ronde matte black acetate bril, warme open glimlach, oogcontact camera. Real skin texture, geen beauty-filter.
SETTING: kies één: productiehal / werkplaats / blueprint-tafel / monitor setup / klant-locatie / podium / industriële documentary setting.
POSE: kies één: arms crossed / pointing-at-screen / holding-laptop / in-conversation / looking-at-camera / three-quarter.
LIGHTING: soft window light, Rembrandt side-key, subtle teal-orange grading, light/warm environment (cream, light grey).
LENS: 50-85mm equivalent, shallow depth of field.
COMPOSITION: framing-instructies passend bij format (vertical/square/landscape).
NEGATIVE: no dark corporate office, no AI avatar look, no toothy fake smile, no stock-photo, geen Aebi Schmidt branding, no navy/donker pak.

## Seedance brief — structuur (motion brief 5-8s, image-to-video)

INPUT_IMAGE: verwijs naar de Higgsfield still hierboven.
DURATION: 5s (hero) of 7-8s (story-arc), vermeld concreet.
MOTION_TYPE: subtle push-in / slow zoom / parallax / handheld breath. Geen complexe cuts.
IDENTITY_LOCK: face + glasses + clothing identity preservation ON.
PACE: scroll-tempo (Reel) of contemplatief (LinkedIn).
ON_SCREEN_TEXT: kies één hook of headline om als tekst-overlay te tonen, vermeld timing (bijv. "headline pops in 1.0s, fades 4.5s").
NEGATIVE: no cutaway, no scene-change, no morphing, no extra people walking through.

## Meta Ads JSON — schema

{
  "campaign": { "objective": "OUTCOME_LEADS" | "OUTCOME_AWARENESS" | "OUTCOME_TRAFFIC", "name": "REC-AUTH-{theme-slug}-{tier}-{format-code}" },
  "ad_set": { "audience_tier": "TOFU"|"MOFU"|"BOFU", "geo": ["NL-GE","NL-OV","NL-NB"], "age_min": 30, "age_max": 60, "interests": [string], "exclusions": [string], "placement": [string], "daily_budget_eur": number, "url_tags": "utm_source=meta&utm_medium=paid&utm_campaign={campaign-slug}&utm_content={hook-id}" },
  "creative": { "format": string, "primary_text": string (= 1 van de bodies, kies de sterkste), "headline": string (= 1 van de headlines), "description": string (kort, ondersteunend), "cta": string (= 1 van de ctas), "destination_url": "https://recruitmentengineer.nl/?utm_source=meta..." },
  "ab_test": { "variants": 3, "rotation": "even", "kill_after_days": 7, "ctr_floor_pct": 1.2, "cpl_ceiling_eur": 8.0 }
}

Kies pragmatische defaults voor budget (TOFU €5-10/d, MOFU €8-12/d, BOFU €15-20/d), interests (HR Directors / Recruitment / Manufacturing leaders / Industrial automation), exclusions (recruiters/hr-bureaus om concurrent-spend te vermijden) en placements (Reels for 9:16, Feed for 1:1, LinkedIn Sponsored Content niet via Meta — markeer "platform": "linkedin" wanneer LinkedIn-format gekozen).

# KWALITEITSCHECKLIST (intern toepassen)

- Hooks: 5 stuks, brutality varieert (zacht → brutaal). Geen clichés ("ben jij die ene...?"), geen "1 ding dat...". Concrete cijfers waar mogelijk.
- Bodies: 3 stuks, elk een andere invalshoek (story / framework / data). Tone-mix gerespecteerd. Lengte past bij format.
- Headlines: 5 stuks, ELK ≤ 40 tekens (incl. spaties + leestekens). Tel mee.
- CTA's: 3 stuks. Tier-passend. Geen "Klik hier", geen "Meer info".
- Higgsfield brief: brand-DNA gelocked (lichtgrijs pak, ronde bril, warm-open). Geen Aebi Schmidt.
- Seedance brief: 5-8s, identity-lock ON, geen complexe cuts.
- Meta JSON: valideerbaar, slugs lowercase-hyphen, daily_budget passend bij tier.
- Geen markdown fences in output. Pure JSON.

LAATSTE INSTRUCTIE: Als het user-bericht een brief bevat, genereer DIRECT de JSON. Niet vragen om bevestiging, niet uitleggen wat je gaat doen.`;

async function callClaude(brief) {
  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) throw new Error('missing_anthropic_api_key');

  const userText = `BRIEF:
- Thema: ${brief.theme}
- Tone dominant (60%): ${brief.tone_dominant}
- Tone secundair (30%): ${brief.tone_secondary}
- Format: ${brief.format}
- Audience tier: ${brief.tier}
- Klantbewijs: ${brief.clients.length ? brief.clients.join(', ') : 'NONE — gebruik geen klantnamen'}

Genereer nu het ad-set JSON object volgens schema. Pure JSON, geen markdown.`;

  const requestBody = {
    model: MODEL,
    max_tokens: MAX_TOKENS,
    system: [
      {
        type: 'text',
        text: SYSTEM_PROMPT,
        cache_control: { type: 'ephemeral' },
      },
    ],
    messages: [
      { role: 'user', content: userText },
    ],
  };

  const res = await fetch(ANTHROPIC_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': apiKey,
      'anthropic-version': ANTHROPIC_VERSION,
    },
    body: JSON.stringify(requestBody),
  });

  if (!res.ok) {
    const errText = await res.text().catch(() => '');
    console.error('Anthropic API error:', res.status, errText);
    const err = new Error(`anthropic_${res.status}`);
    err.detail = errText.slice(0, 500);
    throw err;
  }

  const data = await res.json();
  const blocks = Array.isArray(data.content) ? data.content : [];
  const textBlock = blocks.find((b) => b.type === 'text');
  if (!textBlock || !textBlock.text) {
    throw new Error('empty_response');
  }
  return {
    text: textBlock.text,
    usage: data.usage || null,
  };
}

function extractJson(text) {
  // Strip optional ```json fences just in case the model adds them.
  let s = text.trim();
  if (s.startsWith('```')) {
    s = s.replace(/^```[a-zA-Z]*\s*/, '').replace(/```\s*$/, '');
  }
  // Find the first { and last } in case of stray prose.
  const first = s.indexOf('{');
  const last = s.lastIndexOf('}');
  if (first === -1 || last === -1 || last <= first) {
    throw new Error('no_json_object');
  }
  const slice = s.slice(first, last + 1);
  return JSON.parse(slice);
}

function shapeOutput(parsed) {
  const out = {
    hooks: Array.isArray(parsed.hooks) ? parsed.hooks.slice(0, 5).map(String) : [],
    bodies: Array.isArray(parsed.bodies) ? parsed.bodies.slice(0, 3).map(String) : [],
    headlines: Array.isArray(parsed.headlines) ? parsed.headlines.slice(0, 5).map((h) => String(h).slice(0, 40)) : [],
    ctas: Array.isArray(parsed.ctas) ? parsed.ctas.slice(0, 3).map(String) : [],
    higgsfield_brief: typeof parsed.higgsfield_brief === 'string' ? parsed.higgsfield_brief : '',
    seedance_brief: typeof parsed.seedance_brief === 'string' ? parsed.seedance_brief : '',
    meta_json: parsed.meta_json && typeof parsed.meta_json === 'object' ? parsed.meta_json : {},
  };
  // Pad arrays to expected length so the UI stays stable.
  while (out.hooks.length < 5) out.hooks.push('');
  while (out.bodies.length < 3) out.bodies.push('');
  while (out.headlines.length < 5) out.headlines.push('');
  while (out.ctas.length < 3) out.ctas.push('');
  return out;
}

export default async function handler(req, res) {
  setCors(req, res);
  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'method_not_allowed' });

  const ip =
    (req.headers['x-forwarded-for'] || '').split(',')[0].trim() ||
    req.socket?.remoteAddress ||
    'unknown';
  if (rateLimited(ip)) {
    return res.status(429).json({ error: 'rate_limited' });
  }

  let brief;
  try {
    brief = validateBrief(req.body);
  } catch (e) {
    return res.status(400).json({ error: e.message || 'invalid_body' });
  }

  try {
    const { text, usage } = await callClaude(brief);
    let parsed;
    try {
      parsed = extractJson(text);
    } catch (e) {
      console.error('JSON parse failed. Raw text:', text.slice(0, 500));
      return res.status(502).json({
        error: 'parse_failed',
        detail: 'Claude response was not valid JSON.',
        raw: text.slice(0, 1000),
      });
    }
    const shaped = shapeOutput(parsed);
    return res.status(200).json({
      ...shaped,
      _meta: {
        model: MODEL,
        usage,
        cached_input_tokens: usage?.cache_read_input_tokens || 0,
        cache_creation_tokens: usage?.cache_creation_input_tokens || 0,
      },
    });
  } catch (err) {
    console.error('generate-ad failed:', err);
    return res.status(500).json({
      error: err.message || 'server_error',
      detail: err.detail || null,
    });
  }
}
