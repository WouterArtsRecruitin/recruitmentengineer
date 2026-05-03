# LinkedIn Insight Tag Configuration

**Status:** TBD voor v1 launch — required om LinkedIn Ads retargeting te enablen in fase 3.

**Partner ID:** `LI_PARTNER_ID_PLACEHOLDER` (user fills via LinkedIn Campaign Manager → Account assets → Insight Tag)

---

## Hoe Insight Tag aan te maken

1. Ga naar https://www.linkedin.com/campaignmanager/
2. Selecteer Recruitin B.V. ad account (of maak nieuw account aan voor "Recruitin Authority")
3. Account assets (left nav) → Insight Tag
4. "I will install the tag myself" → Continue
5. **Note Partner ID** (6-7 digits) — bewaar in 1Password + replace `LI_PARTNER_ID_PLACEHOLDER` in deze doc en in `index.html`
6. Tag-code copy (ziet eruit als):

```html
<script type="text/javascript">
_linkedin_partner_id = "XXXXXXX";
window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
window._linkedin_data_partner_ids.push(_linkedin_partner_id);
</script>
<script type="text/javascript">
(function(l) {
  if (!l){window.lintrk = function(a,b){window.lintrk.q.push([a,b])};
  window.lintrk.q=[]}
  var s = document.getElementsByTagName("script")[0];
  var b = document.createElement("script");
  b.type = "text/javascript"; b.async = true;
  b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
  s.parentNode.insertBefore(b, s);
})(window.lintrk);
</script>
<noscript>
<img height="1" width="1" style="display:none;" alt=""
  src="https://px.ads.linkedin.com/collect/?pid=XXXXXXX&fmt=gif" />
</noscript>
```

7. Plaats in `06-landing-page/index.html` net voor `</head>` (na Meta Pixel)

---

## Conversies te configureren (2 stuks)

In Campaign Manager → Account assets → Conversions → Create conversion:

### Conversie 1 — PDF Download (primary)

| Field | Value |
|-------|-------|
| Name | `Stack 2026 PDF Download` |
| Type | `Lead` |
| Value | `49 EUR` (lead-value, niet pricing) |
| Conversion window — Click | 30 days |
| Conversion window — View-through | 7 days |
| Attribution model | `Last touch each campaign` |
| Tracking method | **Event-specific pixel** (recommended) |
| Conversion ID | LinkedIn auto-generates `CID_PDF_DOWNLOAD_PLACEHOLDER` |

**Implementation:** in form-handler na succesvolle `/api/subscribe` 200, fire:

```js
if (typeof window.lintrk === 'function') {
  window.lintrk('track', { conversion_id: CID_PDF_DOWNLOAD_PLACEHOLDER });
}
```

### Conversie 2 — Workshop Inquiry (secondary)

| Field | Value |
|-------|-------|
| Name | `Workshop Discovery Call` |
| Type | `Lead` |
| Value | `2500 EUR` (workshop-value) |
| Conversion window — Click | 30 days |
| Tracking method | URL-based |
| Trigger URL | Calendly thank-you page (when set up): `https://calendly.com/wouterarts/stack-2026-workshop/invitee_complete` |
| Conversion ID | LinkedIn auto-generates `CID_WORKSHOP_PLACEHOLDER` |

**Note:** Calendly account moet eerst opgezet worden — staat voor fase 2/3 (zie KPI scoring "Workshop inquiry +25").

---

## Audiences voor retargeting (fase 3 prep)

Na 30 dagen Insight Tag actief, custom audiences worden auto-populated:

| Audience | Definition | Min size |
|----------|------------|----------|
| `RE — landing visitors 30d` | Visited recruitmentengineer.nl/* in last 30 days | 300 |
| `RE — PDF downloaders` | Fired conversion `Stack 2026 PDF Download` | 300 |
| `RE — high-intent` | Visited > 2 pages OR scrolled > 75% | 300 |

LinkedIn requires min 300 members in an audience before it's usable for ads.

---

## LinkedIn Conversion ID placeholders in code

Gebruik deze placeholder-strings in `index.html` + form-handler — replace na partner-ID-creation:

| Placeholder | Replace with | Locatie |
|-------------|--------------|---------|
| `LI_PARTNER_ID_PLACEHOLDER` | 6-7 digit Partner ID | `<script>` block in `<head>` |
| `CID_PDF_DOWNLOAD_PLACEHOLDER` | `lintrk('track', { conversion_id: NNNNNNNN })` voor PDF download | form-success handler |
| `CID_WORKSHOP_PLACEHOLDER` | `lintrk('track', { conversion_id: NNNNNNNN })` voor Calendly | (later — fase 3) |

Voer een zoek-vervang via:
```bash
sed -i '' 's/LI_PARTNER_ID_PLACEHOLDER/1234567/g' 06-landing-page/index.html
```

---

## Verificatie

1. Install LinkedIn Insight Tag Helper Chrome extension
2. Open https://recruitmentengineer.nl in clean tab
3. Extension icon should turn green ("Tag detected")
4. Click extension → see Partner ID + last fire time
5. In Campaign Manager → Insight Tag → "Tag status" should show "Active" within 1-24h
6. Submit test form → check Conversions → conversion `Stack 2026 PDF Download` shows fire-event in real-time tab
