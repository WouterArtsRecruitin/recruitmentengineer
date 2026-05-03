# Meta Pixel Events — recruitmentengineer.nl
## Configuration spec voor `238226887541404` (shared Recruitin pixel)

> **Pixel ID:** `238226887541404` (gedeelde Recruitin pixel — ook gebruikt op DGR/KT/APK/VK).
> **NIET initiëren op:** `660118697194302` (= FB Page ID, geen pixel — silent fail patroon).
> **Status:** v1 launch — `PageView` + `Lead` zijn LIVE per task A5. Spec hieronder voegt 5 events toe (3 standard + 2 custom).
> **Reference:** `feedback_meta_pixel_vs_page_id.md`

---

## 1. Event-flow overview

```
USER LANDS                  → PageView                 (LIVE)
USER SCROLLS PAST §02       → ViewContent              (NEW — D2)
USER CLICKS mailto: CTA     → AddToCart                (NEW — D2)
USER SUBMITS subscribe      → Lead + Stack2026Download (LIVE + NEW custom)
USER CLICKS Calendly URL    → WorkshopInquiry          (NEW custom)
USER COMPLETES STRIPE       → Purchase                 (PLACEHOLDER — wacht op Stripe checkout)
```

---

## 2. Already-fired (per task A5, LIVE)

### `PageView`
- **Trigger:** On every page load.
- **Code location:** `06-landing-page/public/index.html` — base pixel snippet in `<head>`.
- **Frequency:** ~100% sessions (baseline).
- **Payload:** Default Meta Pixel payload (URL, referrer, user-agent, timestamp).

### `Lead` — PRIMARY CONVERSION EVENT (LIVE per Phase 2 — N5)
- **Trigger:** On subscribe form-submit success (after `/api/subscribe` returns 200 OK).
- **Code location:** `06-landing-page/public/index.html` — inline JS na fetch-success.
- **Frequency:** ~5-10% sessions (baseline target).
- **Payload (LIVE):**
  ```js
  fbq('track', 'Lead', {
    content_name: 'stack-2026-pdf',
    content_category: 'lead_magnet',
    value: 5,
    currency: 'EUR'
  });
  fbq('trackCustom', 'StackPDFRequest', {
    source: 'recruitmentengineer.nl',
    campaign: 'stack-2026-leadmagnet'
  });
  ```
- **Why value=5:** soft estimate of average lead-magnet value. Lets Meta optimize for **value-aware lead-quality**, niet pure lead-count.

### ⚙️ AD-SET OPTIMIZATION RULE — LOCKED

**Cold + Warm + Hot ad-sets: optimize voor `Lead` event (OFFSITE_CONVERSIONS) — NIET voor LANDING_PAGE_VIEWS, LINK_CLICKS, of IMPRESSIONS.**

| Stage | Optimization Goal | Conversion Window | Why |
|-------|-------------------|-------------------|-----|
| Cold (PDF) | `OFFSITE_CONVERSIONS` op `Lead` | 7-day click + 1-day view | Skip de "first warmup op clicks"-fase. Met value-aware Lead haal je in 5-7 dagen voldoende signal voor conversion-optimization, ook bij €25-50/dag |
| Warm (Tier 1) | `OFFSITE_CONVERSIONS` op `Purchase` event | 7-day click + 1-day view | Tier 1 €97 — pixel `Purchase` event vuren post-Stripe-checkout |
| Hot (Tier 2) | `OFFSITE_CONVERSIONS` op `Purchase` (Tier 2 SKU) | 7-day click + 1-day view | Idem voor €497 |

⚠️ **Géén LANDING_PAGE_VIEWS-warmup-fase.** Reden: clicks ≠ leads. Algoritme dat op clicks of LP-views optimaliseert serveert aan scroll-clickers met lage intent → spend gaat naar zwakke leads. Lead-optimization (value-aware) duwt naar mensen die volledig converteren.

**Wat dit betekent in Ads Manager (per ad-set):**
- Performance Goal: "Maximize number of conversions"
- Conversion event: `Lead` (geselecteerd uit pixel `238226887541404`)
- Conversion window: 7-day click, 1-day view (default)
- NIET: "Maximize number of landing page views" / "Maximize link clicks" / "Maximize ThruPlay"

---

## 3. NEW — `ViewContent` (50% scroll past §02 stack-modules)

### Trigger condition
User scrollt **50% van de §02 stack-section voorbij**. §02 is de section met de 5 modules (M01-M05). Dit fire't voor "warm/engaged" users die niet bouncen, en kwalificeert ze als ViewContent voor retargeting-audience #8.

**Detection logic:**
1. IntersectionObserver op `<section id="stack-modules">` (zorg dat die ID bestaat in `index.html` — anders toevoegen aan §02 anchor)
2. Threshold: 0.5 (50% in viewport)
3. Single-fire per sessie via `sessionStorage.setItem('fbq_viewcontent_fired', '1')`

### Event payload
```js
fbq('track', 'ViewContent', {
  content_name: 'Stack 2026 Modules',
  content_category: 'lead_magnet_preview',
  content_ids: ['M01', 'M02', 'M03', 'M04', 'M05'],
  content_type: 'product_group',
  value: 0.00,
  currency: 'EUR'
});
```

### Code placement
**File:** `06-landing-page/public/index.html` — before `</body>`, na de base pixel snippet.

```html
<script>
  // Meta Pixel: ViewContent on §02 50% scroll
  (function() {
    if (sessionStorage.getItem('fbq_viewcontent_fired')) return;
    var target = document.querySelector('#stack-modules');
    if (!target || typeof IntersectionObserver === 'undefined') return;

    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting && entry.intersectionRatio >= 0.5) {
          if (typeof fbq === 'function') {
            fbq('track', 'ViewContent', {
              content_name: 'Stack 2026 Modules',
              content_category: 'lead_magnet_preview',
              content_ids: ['M01', 'M02', 'M03', 'M04', 'M05'],
              content_type: 'product_group',
              value: 0.00,
              currency: 'EUR'
            });
          }
          sessionStorage.setItem('fbq_viewcontent_fired', '1');
          observer.disconnect();
        }
      });
    }, { threshold: [0.5] });

    observer.observe(target);
  })();
</script>
```

### Estimated frequency
**~30-50% van sessies** (depth-readers). Higher dan `Lead` (~5-10%) omdat scroll-depth ≠ conversion.

---

## 4. NEW — `AddToCart` (mailto:warts@recruitin.nl click)

### Trigger condition
User klikt op een `mailto:warts@recruitin.nl`-link vanaf de landing — proxy voor "intent to buy" / "willing to engage 1:1". Specifiek voor de €97 workshop-CTA in `§04 NEXT STEPS` of footer.

**Detection logic:**
- `addEventListener('click', ...)` op alle `<a href^="mailto:warts@recruitin.nl">` elementen
- Single-fire per sessie via `sessionStorage` (zelfde patroon als ViewContent)

### Event payload
```js
fbq('track', 'AddToCart', {
  content_name: 'Vacature Intake Mastery Workshop',
  content_category: 'workshop',
  content_ids: ['workshop-97'],
  content_type: 'product',
  value: 97.00,
  currency: 'EUR'
});
```

### Code placement
**File:** `06-landing-page/public/index.html` — before `</body>`.

```html
<script>
  // Meta Pixel: AddToCart on mailto: CTA click
  document.addEventListener('click', function(e) {
    var anchor = e.target.closest('a[href^="mailto:warts@recruitin.nl"]');
    if (!anchor) return;
    if (sessionStorage.getItem('fbq_addtocart_fired')) return;

    if (typeof fbq === 'function') {
      fbq('track', 'AddToCart', {
        content_name: 'Vacature Intake Mastery Workshop',
        content_category: 'workshop',
        content_ids: ['workshop-97'],
        content_type: 'product',
        value: 97.00,
        currency: 'EUR'
      });
    }
    sessionStorage.setItem('fbq_addtocart_fired', '1');
  });
</script>
```

### Estimated frequency
**~1-3% van sessies** — high-intent micro-conversion. Voorlopig (pre-Stripe-checkout) is dit de beste proxy voor "warm prospect → workshop-buyer".

---

## 5. NEW — `Purchase` (Stripe checkout success — PLACEHOLDER)

### Trigger condition
User wordt redirected vanaf Stripe checkout success-URL terug naar `recruitmentengineer.nl/thank-you?session_id=...`. Stripe-integration is **nog niet gebouwd** voor Tier 1 (€97 workshop). Wanneer Stripe live gaat, fire dit event op de thank-you-page.

**Detection logic:**
- Op `/thank-you` route, check `URLSearchParams.get('session_id')` is aanwezig
- Verify Stripe session via API `/api/stripe-verify?session_id=...` (idempotent, geen double-fire)
- Fire `Purchase` event met session-data

### Event payload
```js
fbq('track', 'Purchase', {
  content_name: 'Vacature Intake Mastery Workshop',
  content_category: 'workshop',
  content_ids: ['workshop-97'],
  content_type: 'product',
  value: 97.00,
  currency: 'EUR'
});
```

**For Tier 2 (€497 course) wanneer live:**
```js
fbq('track', 'Purchase', {
  content_name: 'AI for Recruitment Course',
  value: 497.00,
  currency: 'EUR',
  content_ids: ['course-497']
});
```

### Code placement (PLACEHOLDER)
**File:** `06-landing-page/public/thank-you.html` (NOG TE BOUWEN — wacht op Stripe checkout setup)

```html
<script>
  (function() {
    var params = new URLSearchParams(window.location.search);
    var sessionId = params.get('session_id');
    if (!sessionId) return;

    fetch('/api/stripe-verify?session_id=' + encodeURIComponent(sessionId))
      .then(function(r) { return r.json(); })
      .then(function(data) {
        if (data.verified && typeof fbq === 'function') {
          fbq('track', 'Purchase', {
            content_name: data.product_name,
            content_category: data.product_category,
            content_ids: [data.product_id],
            content_type: 'product',
            value: data.amount,
            currency: 'EUR'
          });
        }
      })
      .catch(function() { /* silent */ });
  })();
</script>
```

### Blockers (not-yet-live)
1. ❌ Stripe checkout product setup — €97 workshop SKU + €497 course SKU + €1.997 bootcamp SKU
2. ❌ `/thank-you` route in landing-page repo
3. ❌ `/api/stripe-verify` Vercel function (verifies session via Stripe API, returns product+amount)
4. ❌ Stripe webhook → Pipedrive deal-stage update (handled separately in `funnel-tier-mapping.md`)

### Estimated frequency
**Pre-launch:** 0 events. **Post-Stripe go-live (target maand 3):** ~0.3-1% van sessies.

---

## 6. NEW — `Stack2026Download` (custom event — synonym for `Lead`)

### Why a custom event next to `Lead`
- `Lead` is een **standard event** — gedeeld met andere Recruitin-products op de pixel (DGR-leads, KT-leads, APK-leads).
- `Stack2026Download` is een **custom event** specifiek voor deze landing — gebruikt voor product-specifieke Custom Audiences (audience #4 + #6 in audience architecture).
- Fire **beide** events parallel op subscribe-success.

### Trigger condition
Same as `Lead`: na succesvolle `/api/subscribe` POST → 200 OK.

### Event payload
```js
fbq('trackCustom', 'Stack2026Download', {
  email_hash: '<sha256-hashed-email>',  // optional, voor matching
  utm_source: utmSource,
  utm_medium: utmMedium,
  utm_campaign: utmCampaign,
  product: 'stack-2026'
});
```

### Code placement
**File:** `06-landing-page/public/index.html` — same fetch-success block waar `Lead` al fire't. Add direct daarna:

```js
// Custom event for product-specific Custom Audience
fbq('trackCustom', 'Stack2026Download', {
  utm_source: data.utm_source || '',
  utm_medium: data.utm_medium || '',
  utm_campaign: data.utm_campaign || '',
  product: 'stack-2026'
});
```

### Estimated frequency
Same as `Lead` (~5-10% sessies). 1:1 mirror.

---

## 7. NEW — `WorkshopInquiry` (custom event — Calendly URL clicks)

### Trigger condition
User klikt op een Calendly-URL ergens op de landing (workshop-booking, intake-call CTA). Calendly-integration is **nog niet ingericht** — wanneer live, fire bij elke Calendly-click.

**Detection logic:**
- `addEventListener('click', ...)` op alle `<a href*="calendly.com">` elementen
- Single-fire per sessie

### Event payload
```js
fbq('trackCustom', 'WorkshopInquiry', {
  content_name: 'Workshop Intake Call',
  calendly_url: anchor.href,
  source_section: '<which page section>',
  value: 97.00,
  currency: 'EUR'
});
```

### Code placement
**File:** `06-landing-page/public/index.html` — before `</body>`.

```html
<script>
  document.addEventListener('click', function(e) {
    var anchor = e.target.closest('a[href*="calendly.com"]');
    if (!anchor) return;
    if (sessionStorage.getItem('fbq_workshopinquiry_fired')) return;

    if (typeof fbq === 'function') {
      fbq('trackCustom', 'WorkshopInquiry', {
        content_name: 'Workshop Intake Call',
        calendly_url: anchor.href,
        source_section: anchor.closest('section')?.id || 'unknown',
        value: 97.00,
        currency: 'EUR'
      });
    }
    sessionStorage.setItem('fbq_workshopinquiry_fired', '1');
  });
</script>
```

### Estimated frequency
**~0.5-2% van sessies** (very high-intent). Voor BOFU audience #11.

---

## 8. Summary table — alle events

| Event | Type | Trigger | Frequency | Status | Audience-use |
|-------|------|---------|-----------|--------|--------------|
| `PageView` | Standard | Page load | 100% | LIVE | TOFU retargeting (audience #5) |
| `Lead` | Standard | Subscribe success | 5-10% | LIVE | Lookalike-source (audience #4) |
| `ViewContent` | Standard | 50% scroll past §02 | 30-50% | NEW | Engaged retargeting (audience #8) |
| `AddToCart` | Standard | mailto: click | 1-3% | NEW | High-intent retargeting (audience #9) |
| `Purchase` | Standard | Stripe success | 0% (pre-launch) | PLACEHOLDER | Customer / lookalike (#13, #14, #15) |
| `Stack2026Download` | Custom | Subscribe success | 5-10% | NEW | Product-specific Lookalike (#4) + downloaders 30d (#6) |
| `WorkshopInquiry` | Custom | Calendly click | 0.5-2% | NEW | BOFU workshop audience (#11) |

---

## 9. Implementation checklist

### Phase 1 — Already-live (LIVE per A5)
- [x] Base pixel snippet `<head>` met `238226887541404`
- [x] `PageView` automatisch via base snippet
- [x] `Lead` op subscribe form-submit success

### Phase 2 — Add now (D2 spec implementeren)
- [ ] Add `id="stack-modules"` to §02 section in `index.html` (verify exists)
- [ ] Implement `ViewContent` IntersectionObserver
- [ ] Implement `AddToCart` mailto-click listener
- [ ] Implement `Stack2026Download` custom event in subscribe-success block
- [ ] Implement `WorkshopInquiry` Calendly-click listener (skeleton, fire't 0× tot Calendly URLs in page komen)

### Phase 3 — Post-Stripe go-live (later)
- [ ] Bouw `/thank-you` route + `thank-you.html` template
- [ ] Bouw `/api/stripe-verify` Vercel function
- [ ] Implement `Purchase` event op `/thank-you`
- [ ] Test Stripe webhook → Meta CAPI server-side fallback (consent-blocked browsers)

### Phase 4 — Validation (post-go-live)
- [ ] Meta Events Manager → Test Events tool: trigger elk event handmatig + verify
- [ ] Meta Events Manager → Diagnostics: check voor "Match Quality" warnings (email_hash matching)
- [ ] Pipedrive: verify dat `Lead` events 1:1 mappen naar nieuwe deals in "Authority Leads" pipeline
- [ ] Privacy: documenteer alle events in `cookie-policy.md` + cookie-banner consent vereisten

---

## 10. Privacy + consent (Recruitin in-house banner)

Per `project_dgr_consent_migration.md` + `feedback_cookiebot_constraints.md`:

**Marketing pixel (Meta) ALLEEN fire'n na consent:**
- Wrap alle `fbq(...)` calls in een `if (window.RecruitinConsent && window.RecruitinConsent.marketing) { ... }` check
- Listen voor `RecruitinConsentReady` event om events te queuen tot consent-decision
- In-house banner spec staat in `06-landing-page/` (consistent met DGR/KT/APK pattern post 26 apr 2026)

**Required addition to all 5 NEW events:**
```js
function fireFbq(eventName, payload, isCustom) {
  if (typeof fbq !== 'function') return;
  if (!window.RecruitinConsent?.marketing) {
    // Queue for after consent
    window.addEventListener('RecruitinConsentReady', function() {
      if (window.RecruitinConsent.marketing) {
        isCustom ? fbq('trackCustom', eventName, payload) : fbq('track', eventName, payload);
      }
    }, { once: true });
    return;
  }
  isCustom ? fbq('trackCustom', eventName, payload) : fbq('track', eventName, payload);
}
```

---

> **Status:** ✅ Spec compleet. Ready voor implementatie in `06-landing-page/public/index.html`.
> **Owner:** Ing. W. Arts
> **Blockers:** Stripe checkout setup (Purchase event placeholder), Calendly account setup (WorkshopInquiry skeleton fire't 0×).
