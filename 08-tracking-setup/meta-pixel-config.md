# Meta Pixel Configuration

**Pixel ID:** `238226887541404` (Recruitin shared — same one used on DGR/KT/APK/VK)

**LET OP — geen verwarring:**
- `238226887541404` = **Pixel ID** (Events tracking)
- `660118697194302` = **FB Page ID** (NIET gebruiken voor `fbq('init')` — silent fail, zie `feedback_meta_pixel_vs_page_id.md`)

---

## Already-fired events (v1 launch)

Deze worden door `06-landing-page/index.html` gefired:

| Event | Trigger | Code-locatie | Status |
|-------|---------|--------------|--------|
| `PageView` | Auto on page load | `<head>` after `fbq('init', '238226887541404')` | LIVE |
| `Lead` | After form submit succes (`/api/subscribe` 200) | Inline `<script>` in form-handler | LIVE |

---

## To-add events (Day 1-7)

| Event | Trigger | Implementation |
|-------|---------|----------------|
| `ViewContent` | Scroll 50% on landing | gtag-style event, `content_name: 'stack-2026-landing'` |
| `AddToCart` | Click `mailto:warts@recruitin.nl` (warm hand-raise) | `onclick="fbq('track', 'AddToCart', {content_name: 'wouter-mailto'})"` |
| `Stack2026Download` (custom) | After successful PDF email-send | Server-side via CAPI gateway (post-deploy fase) |

### Code-snippet voor scroll-50

```html
<script>
  let scrollFired = false;
  window.addEventListener('scroll', () => {
    if (scrollFired) return;
    const scrolled = (window.scrollY + window.innerHeight) / document.body.scrollHeight;
    if (scrolled > 0.5) {
      scrollFired = true;
      if (typeof fbq === 'function') {
        fbq('track', 'ViewContent', {
          content_name: 'stack-2026-landing',
          content_category: 'lead-magnet'
        });
      }
    }
  }, { passive: true });
</script>
```

---

## CAPI server-side gating (post-deploy)

**Doel:** Lead-events server-side fire bypasses ad-blockers + iOS 14+ ITP. Use Meta CAPI Gateway voor Lead-event ipv pure client-side.

### Optie A — directe CAPI call (recommended)

In `api/subscribe.js`, na successful Resend-send:

```js
// CAPI fire
const META_CAPI_TOKEN = process.env.META_CAPI_TOKEN;
const META_PIXEL_ID = '238226887541404';

if (META_CAPI_TOKEN) {
  const hashedEmail = crypto.createHash('sha256').update(normalizedEmail).digest('hex');
  await fetch(`https://graph.facebook.com/v19.0/${META_PIXEL_ID}/events`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      data: [{
        event_name: 'Lead',
        event_time: Math.floor(Date.now() / 1000),
        action_source: 'website',
        event_source_url: 'https://recruitmentengineer.nl',
        user_data: {
          em: [hashedEmail],
          client_ip_address: ip,
          client_user_agent: req.headers['user-agent']
        },
        custom_data: {
          content_name: 'stack-2026',
          value: 49,
          currency: 'EUR'
        }
      }],
      access_token: META_CAPI_TOKEN,
      test_event_code: process.env.META_TEST_EVENT_CODE  // strip in prod
    })
  });
}
```

**Env-vars to add (Vercel):**
- `META_CAPI_TOKEN` — System User Token uit Business Settings → System Users → Recruitin → Generate New Token (Pixel: All)
- `META_TEST_EVENT_CODE` — alleen tijdens testing, zelf-gegenereerd via Events Manager → Test Events tab

### Optie B — Meta CAPI Gateway (later, AWS-based)

Skip voor v1. Overweeg in fase 3 als:
- > 1000 leads/maand
- Multi-pixel deduplication nodig (cross-product retargeting)
- iOS 17+ private relay overhead te groot wordt

---

## Event Test Tool steps voor verificatie

1. Events Manager → Pixel `238226887541404` → "Test events" tab
2. Genereer test event code (start met `TEST` — bv `TEST123ABC`)
3. Add `META_TEST_EVENT_CODE=TEST123ABC` to Vercel preview env
4. Deploy preview → submit form met test-email
5. Test events tab → Lead-event verschijnt binnen 30s met:
   - Match score > 80% (incl email hash)
   - Action source: `website`
   - User data: hashed email + IP + UA
6. Strip `META_TEST_EVENT_CODE` env voor productie deploy

---

## Verificatie checklist

- [ ] `fbq('init', '238226887541404')` aanwezig in `<head>` (NIET page-id 660118697194302)
- [ ] PageView fires automatically op load → check Real-time tab in Events Manager
- [ ] Lead event fires na form-submit → check binnen 60s
- [ ] CAPI server-side fires post-deploy via Test Events tab
- [ ] Pixel Helper Chrome extension shows green checkmark op recruitmentengineer.nl
- [ ] Custom audience "Stack 2026 Lead" auto-populates na 24u (min audience size 100)
