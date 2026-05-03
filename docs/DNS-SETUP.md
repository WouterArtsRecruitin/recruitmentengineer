# 🔌 DNS Setup — recruitmentengineer.nl

**Registrar:** Metaregistrar B.V. — log in op https://metaregistrar.com/customers (of via je reseller).  
**Zone-bestand status (3 mei 2026):** geen records — domein staat actief maar nameservers zonder A/MX.

---

## ✅ Stap 1 — Vercel A-record (= site live op https://recruitmentengineer.nl)

| Type | Host | Waarde | TTL |
|------|------|--------|-----|
| `A` | `@` | `76.76.21.21` | 3600 |
| `CNAME` | `www` | `cname.vercel-dns.com.` | 3600 |

> Na toevoegen ~5-15 min wachten op DNS-propagatie. Verifieer met:
> ```
> dig +short recruitmentengineer.nl
> # → 76.76.21.21
> dig +short www.recruitmentengineer.nl
> # → cname.vercel-dns.com.
> ```

Vercel SSL-cert wordt automatisch geprovisioned na verificatie van eigendom (~5 min).

---

## ✅ Stap 2 — Resend (= mailen vanaf wouter@recruitmentengineer.nl)

Records komen uit Resend dashboard nadat je domain toevoegt. **Jij voegt eerst** `recruitmentengineer.nl` toe op https://resend.com/domains, **kopieert dan** de exacte waarden hieronder en plakt ze in Metaregistrar:

| Type | Host | Waarde | TTL | Bron |
|------|------|--------|-----|------|
| `MX` | `send` | `feedback-smtp.eu-west-1.amazonses.com` (priority 10) | 3600 | Resend |
| `TXT` | `send` | `v=spf1 include:amazonses.com ~all` | 3600 | Resend |
| `TXT` | `resend._domainkey` | (DKIM-key — ~250 chars, kopieer 1-op-1 uit Resend) | 3600 | Resend |
| `TXT` | `_dmarc` | `v=DMARC1; p=none; rua=mailto:warts@recruitin.nl` | 3600 | optioneel |

> **Let op:** Metaregistrar splitst soms lange TXT-records in meerdere kwoot-blokjes — laat het systeem dit zelf doen, plak de DKIM als één string. Quotes (`"`) horen er **niet** bij.

Verifieer in Resend: status moet groen "Verified ✅" worden binnen 15-30 min.

Verificatie-curl als test:
```bash
dig +short TXT resend._domainkey.recruitmentengineer.nl
# → moet de DKIM-key returnen
```

---

## ✅ Stap 3 — Resend Audience aanmaken

Na domain-verify:
1. Resend → **Audiences** → **Create**
2. Name: `Stack 2026 Leads`
3. Kopieer de Audience ID (UUID-formaat: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`)
4. Geef ID door — Claude zet hem in `~/recruitin/.env` als `RESEND_AUDIENCE_ID` + in Vercel ENV.

---

## ✅ Stap 4 — Vercel custom-domain koppeling

Wordt door Claude gedaan via:
```bash
cd ~/projects/recruitmentengineer/06-landing-page
vercel domains add recruitmentengineer.nl
vercel alias <deploy-url> recruitmentengineer.nl
```

Vercel verifieert eigenaar via A-record uit Stap 1 — dus zorg dat Stap 1 eerst is gepropagteerd.

---

## 🔍 Smoke-test na alle DNS-records

```bash
# A-record
dig +short A recruitmentengineer.nl
# → 76.76.21.21

# www CNAME
dig +short CNAME www.recruitmentengineer.nl
# → cname.vercel-dns.com.

# Resend SPF
dig +short TXT send.recruitmentengineer.nl
# → "v=spf1 include:amazonses.com ~all"

# Resend MX
dig +short MX send.recruitmentengineer.nl
# → 10 feedback-smtp.eu-west-1.amazonses.com.

# Resend DKIM
dig +short TXT resend._domainkey.recruitmentengineer.nl
# → "k=rsa; p=MII..." (lange key)

# Live HTTP
curl -I https://recruitmentengineer.nl
# → HTTP/2 200, content-type: text/html

# Live API
curl -X POST https://recruitmentengineer.nl/api/subscribe \
  -H 'Content-Type: application/json' \
  -d '{"email":"warts+test@recruitin.nl","source":"smoke"}'
# → {"success":true}
```

---

## 🛟 Troubleshooting

| Probleem | Oorzaak | Fix |
|----------|---------|-----|
| Vercel toont "Invalid configuration" | A-record wijst nog naar oude waarde / cache | `dig @1.1.1.1 +short A recruitmentengineer.nl` om Cloudflare-cache te omzeilen — wacht 5 min |
| Resend status blijft "Pending" | DKIM TXT verkeerd geknipt / quotes erin | Open record in Metaregistrar UI, plak DKIM-string opnieuw zonder quotes |
| `curl POST /api/subscribe` → 500 | ENV niet geset op Vercel | `vercel env ls` — check of alle 6 vars (RESEND_API_KEY, RESEND_AUDIENCE_ID, PIPEDRIVE_API_KEY, PIPEDRIVE_DOMAIN, PIPEDRIVE_PIPELINE_ID, PIPEDRIVE_STAGE_ID) production-scope hebben |
| OG-preview LinkedIn → broken image | `og-image.jpg` niet in `public/` of niet committed | Verifieer `curl -I https://recruitmentengineer.nl/og-image.jpg` → moet 200 + image/jpeg returnen |
| `from: wouter@recruitmentengineer.nl` mail bounced | Domain nog niet verified bij Resend | Wacht tot status = green; in tussentijd: gebruik Resend testdomein `onboarding@resend.dev` |
