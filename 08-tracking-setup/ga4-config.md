# GA4 Configuration

**Status:** SKIPPED voor v1 launch (beslissing 30 apr 2026). Placeholder commented in `06-landing-page/index.html`. Activeren in fase 2 na eerste 100 leads.

**Reden voor skip:**
- GA4 setup goed doen kost 2-3 uur (property + Google Tag wrapper + cross-domain + filters + key events)
- Voor v1 (Day 0-14) hebben we alleen Pipedrive + Resend webhook-data nodig om KPIs te meten
- GA4 attribution wordt pas waardevol bij meerdere paid-channels (fase 3)
- Risico op `GA4_ORPHAN_MID_REGEL` bij haastige setup (zie `~/CLAUDE.md`)

---

## Activatie checklist (fase 2)

### 1. Nieuwe GA4 property aanmaken

**LET OP — niet hergebruiken:**
- Niet recruitin.nl property `403852433`
- Niet KT property `514956873`
- **Wel:** dedicated nieuwe property "Recruitment Engineer" onder Account `101673451`

**Stappen:**
1. analytics.google.com → Admin → Create Property
2. Naam: `Recruitment Engineer`
3. Reporting timezone: `Amsterdam (GMT+01:00)`
4. Currency: `EUR`
5. Industry: `Jobs & Education`
6. Business size: `Small (< 10 employees)`
7. Web stream → URL: `https://recruitmentengineer.nl` → Stream name: `recruitmentengineer.nl main`
8. Note Measurement ID `G-XXXXXXX` (volgens convention: `G-RE-XXXXXXX` is niet geldig voor GA4 — GA4 generates eigen format)

### 2. Google Tag wrapper aanmaken (KRITIEK)

**Waarom:** bare `gtag/js?id=G-XXX` URL geeft HTTP 404 zodra MID gewikkeld is in GT-tag (zie `GA4_ORPHAN_MID_REGEL`).

**Stappen:**
1. Tag → Manage tags (under stream config)
2. "Configure your tag and connections"
3. Bekijk auto-aangemaakte Google Tag (`GT-XXXXXXX`)
4. Documenteer GT-ID — dit is de ID die in `index.html` moet komen, NIET de bare measurement ID

### 3. Uncomment in landing page

Bestand: `06-landing-page/index.html` (regel-refs nog te bepalen — Restructure agent levert)

Voor commit: zoek `<!-- GA4_PLACEHOLDER` block, replace met:

```html
<!-- GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GT-XXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GT-XXXXXXX', {
    cookie_flags: 'SameSite=None;Secure',
    send_page_view: true
  });
</script>
```

### 4. Cross-domain config (v1)

Voor launch alleen `recruitmentengineer.nl` whitelisten. Andere domeinen (recruitin.nl, KT/DGR/etc.) NIET koppelen — die hebben eigen properties.

In Admin → Data Streams → recruitmentengineer.nl stream → "Configure tag settings" → "Configure your domains":
- `recruitmentengineer.nl`
- `www.recruitmentengineer.nl`

Match-type: `Contains`.

### 5. Internal traffic filter

Admin → Data Settings → Data Filters → Create filter "Internal Traffic":
- Filter name: `Thuis Wouter (Ziggo Doesburg)`
- Operation: `Exclude`
- Parameter: `traffic_type` = `internal`

Dan in stream-config → "Define internal traffic":
- Rule name: `Thuis Wouter`
- traffic_type value: `internal`
- Match type: `IP address equals`
- IP: `217.62.161.195`

### 6. Key Events (5 conversies)

Admin → Events → "Mark as key event":

| Event name | Trigger | Notes |
|------------|---------|-------|
| `page_view` | Auto (Enhanced Measurement) | Uitschakelen na launch — te ruis-rijk |
| `generate_lead` | Form submit success — fired by `index.html` after `/api/subscribe` 200 | Primary conversion |
| `file_download` | Auto (Enhanced Measurement) — voor `stack-2026.pdf` | Backup-attributie als email-attachment-flow ooit faalt |
| `scroll` | Auto — fires bij 90% scroll | Engagement-signal |
| `click` | Auto — outbound clicks (calendly + mailto) | Voor "warm hand-raise" detection |

**LET OP:** Custom events `cta_calendly_click` + `cta_mailto_click` moeten via gtag in `index.html` worden gefired (niet auto). Voorbeeld:

```html
<a href="mailto:warts@recruitin.nl"
   onclick="gtag('event', 'cta_mailto_click', {'cta_location': 'hero'})">
   Mail me direct
</a>
```

### 7. Enhanced Measurement

Admin → Data Streams → stream → "Enhanced measurement" gear icon:
- Page views: ON
- Scrolls: ON
- Outbound clicks: ON
- Site search: OFF (geen search-functie)
- Form interactions: ON
- Video engagement: OFF (geen embedded video v1)
- File downloads: ON

### 8. Server-side Measurement Protocol (later)

Niet voor v1. In fase 2 als consent-blocked browsers > 30% van traffic worden:
- Maak MP API secret in Admin → Data Streams → stream → "Measurement Protocol API secrets"
- Save als Vercel env `GA4_MP_SECRET_RE`
- Wire in `api/subscribe.js` server-side fire na succesvolle Pipedrive-deal (event: `generate_lead`)

---

## Verificatie

Na activatie, smoke-test:
```bash
curl -o /dev/null -w "%{http_code}" "https://www.googletagmanager.com/gtag/js?id=GT-XXXXXXX"
# Expect: 200
```

Realtime report → Admin → Realtime → eigen page-view zichtbaar binnen 60s.

Debug-mode: `?gtm_debug=1` → DebugView in Admin laat events live zien.
