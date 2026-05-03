# recruitmentengineer.nl

Lead magnet landing page voor de Recruitment Engineering Stack 2026.

## Stack

- **Static HTML** (geen build step, deploy is instant)
- **Vercel Serverless Function** (`/api/subscribe`)
- **Resend** voor email + PDF attachment
- **Pipedrive** voor automatische lead-sync (Authority Lead label)

## Files

```
06-landing-page/
├── index.html          # Single-page landing met 2 email forms
├── api/
│   └── subscribe.js    # Serverless: email + Pipedrive sync
├── stack-2026.pdf      # Lead magnet (kopiëren uit /03-lead-magnet/)
├── vercel.json         # Vercel config
├── package.json        # Node deps + scripts
├── .env.example        # ENV variables template
└── README.md
```

## Deploy stappen

### 1. Setup Resend
- Maak account op resend.com
- **Verifieer domein `recruitmentengineer.nl`** (NIET recruitin.nl — die heeft geen DNS-toegang)
- Voeg deze records toe bij je DNS-provider voor `recruitmentengineer.nl`:
  - **MX**: `feedback-smtp.eu-west-1.amazonses.com` (priority 10)
  - **TXT (SPF)**: `v=spf1 include:amazonses.com ~all`
  - **TXT (DKIM)**: 3 records — Resend genereert deze in dashboard
  - **TXT (DMARC)** optioneel: `v=DMARC1; p=none;`
- Wacht 15-30 min tot verificatie groen wordt
- Genereer API key
- Kopieer naar `.env`

**Afzender flow:**
- `from:` = `wouter@recruitmentengineer.nl` (nieuw domein, geverifieerd)
- `reply_to:` = `warts@recruitin.nl` (jouw echte mailbox — reacties komen daar binnen)

### 2. Setup Pipedrive (optioneel)
- API key in Pipedrive → Personal Settings → API
- Domain = `recruitin` (uit `recruitin.pipedrive.com`)
- Voeg label "Authority Lead — Stack 2026" toe in Pipedrive (Persons)

### 3. PDF kopiëren
```bash
cp ../03-lead-magnet/stack-2026.pdf ./stack-2026.pdf
```

### 4. Deploy naar Vercel
```bash
npm install -g vercel
vercel login
vercel --prod
```

### 5. Custom domain
- Koop `recruitmentengineer.nl` (Namecheap / TransIP / Cloudflare)
- In Vercel project: Settings → Domains → Add `recruitmentengineer.nl`
- DNS A-record naar `76.76.21.21` (Vercel)

### 6. ENV variables in Vercel
- Project Settings → Environment Variables:
  - `RESEND_API_KEY`
  - `PIPEDRIVE_API_KEY`
  - `PIPEDRIVE_DOMAIN`

## Test lokaal

```bash
vercel dev
# Open http://localhost:3000
```

## Tracking

Voeg in `<head>` toe als je GA4/Plausible wil tracken:

```html
<!-- GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXX');
</script>
```

De landing roept al `gtag('event', 'lead_magnet_download')` aan bij submit.

## TODO na launch

- [ ] Open Graph image toevoegen (1200x630px hero)
- [ ] Favicon
- [ ] LinkedIn Insight Tag voor retargeting
- [ ] Meta Pixel voor warm audience
- [ ] A/B test: welke hero copy wint?
- [ ] Newsletter follow-up sequence (3 mails na download)

## Performance targets

- LCP < 1.5s (single HTML, geen JS frameworks)
- CLS < 0.1 (alle dimensies fixed)
- TTI < 2s
- Mobile Lighthouse score 95+
