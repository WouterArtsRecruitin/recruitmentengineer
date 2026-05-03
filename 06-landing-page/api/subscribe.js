// Vercel Serverless Function — /api/subscribe
// Captures email, sends Stack 2026 PDF via Resend, syncs to Resend audience + Pipedrive (Person + Deal in Authority Leads pipeline)

import crypto from 'node:crypto';

const ALLOWED_ORIGINS = new Set([
  'https://recruitmentengineer.nl',
  'https://www.recruitmentengineer.nl',
  'http://localhost:3000',
]);

const RATE_LIMIT_WINDOW_MS = 60_000;
const RATE_LIMIT_MAX = 3;
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

function emailToName(email) {
  const local = email.split('@')[0].replace(/\+.*$/, '');
  return local
    .split(/[._-]+/)
    .filter(Boolean)
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase())
    .join(' ') || local;
}

function setCors(req, res) {
  const origin = req.headers.origin;
  if (origin && ALLOWED_ORIGINS.has(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
    res.setHeader('Vary', 'Origin');
  }
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
}

const EMAIL_HTML = `
  <div style="font-family: -apple-system, sans-serif; max-width: 600px; margin: 0 auto; padding: 24px; color: #1a1a1a;">
    <p>Hi,</p>
    <p>Bedankt voor je interesse in de <strong>Recruitment Engineering Stack 2026</strong>.</p>
    <p>De PDF zit als bijlage bij deze mail. Je vindt erin:</p>
    <ul>
      <li><strong>Module 1 — Sourcing Engineering:</strong> 4u → 25min boolean searches</li>
      <li><strong>Module 2 — Hyper-Personalization:</strong> 41% InMail response rate</li>
      <li><strong>Module 3 — Vacature Intake:</strong> 8u → 90min intake-werk</li>
      <li><strong>Module 4 — Match Score Calculator:</strong> 73% screening accuracy</li>
      <li><strong>Module 5 — Pipeline Diagnostician:</strong> €519k pipeline recovery case</li>
    </ul>
    <p>Komende dagen krijg je nog 3 mails van me met de losse productie-prompts (volledige tekst, copy-paste-klaar voor Claude/ChatGPT/Gemini).</p>
    <p>Vragen? Mail terug. Ik lees alles zelf.</p>
    <p style="margin-top: 32px;">
      Groet,<br>
      <strong>Ing. W. Arts</strong><br>
      <span style="color: #5a6573; font-size: 14px;">Recruitment Engineer · Recruitin B.V.</span>
    </p>
    <hr style="border: none; border-top: 1px solid #e5e0d8; margin: 32px 0;">
    <p style="font-size: 12px; color: #5a6573;">
      Je krijgt deze mail omdat je je hebt aangemeld op recruitmentengineer.nl.<br>
      <a href="{{{RESEND_UNSUBSCRIBE_URL}}}" style="color: #5a6573;">Uitschrijven</a>
    </p>
  </div>
`;

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

  const { email, source, utm_source, utm_medium, utm_campaign, utm_content, referrer } = req.body || {};
  if (typeof email !== 'string' || email.length > 254 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return res.status(400).json({ error: 'invalid_email' });
  }
  const normalizedEmail = email.trim().toLowerCase();

  // Sanitize UTM-set: trim, cap length, default to empty string
  const sanitize = (v) => (typeof v === 'string' ? v.trim().slice(0, 200) : '');
  const utm = {
    utm_source: sanitize(utm_source),
    utm_medium: sanitize(utm_medium),
    utm_campaign: sanitize(utm_campaign),
    utm_content: sanitize(utm_content),
    referrer: sanitize(referrer),
  };

  const RESEND_API_KEY = process.env.RESEND_API_KEY;
  const RESEND_AUDIENCE_ID = process.env.RESEND_AUDIENCE_ID;
  const PIPEDRIVE_API_KEY = process.env.PIPEDRIVE_API_KEY || process.env.PIPEDRIVE_API_TOKEN;
  const PIPEDRIVE_DOMAIN = process.env.PIPEDRIVE_DOMAIN || 'recruitin';
  const PIPEDRIVE_PIPELINE_ID = process.env.PIPEDRIVE_PIPELINE_ID;
  const PIPEDRIVE_STAGE_ID = process.env.PIPEDRIVE_STAGE_ID;

  if (!RESEND_API_KEY) {
    console.error('Subscribe error: RESEND_API_KEY missing');
    return res.status(500).json({ error: 'server_error' });
  }

  const idempotencyKey = crypto
    .createHash('sha256')
    .update(`${normalizedEmail}|${new Date().toISOString().slice(0, 10)}`)
    .digest('hex');
  const displayName = emailToName(normalizedEmail);

  try {
    const emailRes = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${RESEND_API_KEY}`,
        'Content-Type': 'application/json',
        'Idempotency-Key': idempotencyKey,
      },
      body: JSON.stringify({
        from: 'Wouter Arts <wouter@recruitmentengineer.nl>',
        reply_to: 'warts@recruitin.nl',
        to: [normalizedEmail],
        subject: '📥 Recruitment Engineering Stack 2026 — jouw download',
        html: EMAIL_HTML,
        attachments: [
          {
            filename: 'Recruitment-Engineering-Stack-2026.pdf',
            path: 'https://recruitmentengineer.nl/stack-2026.pdf',
          },
        ],
        tags: [
          { name: 'campaign', value: 'stack-2026-leadmagnet' },
          { name: 'source', value: (source || 'landing').slice(0, 32) },
        ],
      }),
    });

    if (!emailRes.ok) {
      const errText = await emailRes.text().catch(() => '');
      console.error('Resend send failed:', emailRes.status, errText);
      throw new Error('email_send_failed');
    }

    if (RESEND_AUDIENCE_ID) {
      try {
        const audRes = await fetch(
          `https://api.resend.com/audiences/${RESEND_AUDIENCE_ID}/contacts`,
          {
            method: 'POST',
            headers: {
              Authorization: `Bearer ${RESEND_API_KEY}`,
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              email: normalizedEmail,
              first_name: displayName,
              unsubscribed: false,
            }),
          }
        );
        if (!audRes.ok && audRes.status !== 409) {
          const errText = await audRes.text().catch(() => '');
          console.error('Resend audience add failed:', audRes.status, errText);
        }
      } catch (audErr) {
        console.error('Resend audience add error (non-blocking):', audErr);
      }
    }

    if (PIPEDRIVE_API_KEY) {
      try {
        await syncToPipedrive({
          email: normalizedEmail,
          name: displayName,
          source: source || 'landing',
          utm,
          apiKey: PIPEDRIVE_API_KEY,
          domain: PIPEDRIVE_DOMAIN,
          pipelineId: PIPEDRIVE_PIPELINE_ID,
          stageId: PIPEDRIVE_STAGE_ID,
        });
      } catch (pipeErr) {
        console.error('Pipedrive sync failed (non-blocking):', pipeErr);
      }
    }

    return res.status(200).json({ success: true });
  } catch (error) {
    console.error('Subscribe error:', error);
    return res.status(500).json({ error: 'server_error' });
  }
}

async function syncToPipedrive({ email, name, source, utm, apiKey, domain, pipelineId, stageId }) {
  const base = `https://${domain}.pipedrive.com/api/v1`;
  const auth = `api_token=${encodeURIComponent(apiKey)}`;

  const searchRes = await fetch(
    `${base}/persons/search?term=${encodeURIComponent(email)}&fields=email&exact_match=true&${auth}`
  );
  if (!searchRes.ok) {
    console.error('Pipedrive person search failed:', searchRes.status);
    return;
  }
  const searchData = await searchRes.json();
  let personId = searchData?.data?.items?.[0]?.item?.id;

  if (!personId) {
    const personRes = await fetch(`${base}/persons?${auth}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name,
        email: [{ value: email, primary: true, label: 'work' }],
        visible_to: 3,
      }),
    });
    if (!personRes.ok) {
      const errText = await personRes.text().catch(() => '');
      console.error('Pipedrive person create failed:', personRes.status, errText);
      return;
    }
    const personData = await personRes.json();
    personId = personData?.data?.id;
  }
  if (!personId) return;

  const dealBody = {
    title: `Stack 2026 download — ${email}`,
    person_id: personId,
    status: 'open',
    visible_to: 3,
  };
  if (pipelineId) dealBody.pipeline_id = Number(pipelineId);
  if (stageId) dealBody.stage_id = Number(stageId);

  const dealRes = await fetch(`${base}/deals?${auth}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(dealBody),
  });
  if (!dealRes.ok) {
    const errText = await dealRes.text().catch(() => '');
    console.error('Pipedrive deal create failed:', dealRes.status, errText);
    return;
  }

  const dealData = await dealRes.json();
  const dealId = dealData?.data?.id;
  if (dealId) {
    // Build UTM-block — only include rows with values, skip empty ones for cleanliness
    const utmRows = utm
      ? [
          ['utm_source', utm.utm_source],
          ['utm_medium', utm.utm_medium],
          ['utm_campaign', utm.utm_campaign],
          ['utm_content', utm.utm_content],
          ['referrer', utm.referrer],
        ].filter(([, v]) => v && v.length > 0)
      : [];
    const utmBlock = utmRows.length
      ? `\n\n--- UTM / attribution ---\n${utmRows.map(([k, v]) => `${k}: ${v}`).join('\n')}`
      : '';

    await fetch(`${base}/notes?${auth}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        deal_id: dealId,
        person_id: personId,
        content: `Authority Lead — Stack 2026 download via recruitmentengineer.nl (source: ${source})${utmBlock}`,
      }),
    }).catch((e) => console.error('Pipedrive note add failed (non-blocking):', e));
  }
}
