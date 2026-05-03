# Content Engine — Prompts Library

14 production prompts voor wekelijkse content-output. Copy-paste in Claude/ChatGPT/Gemini.

## Index

| # | Prompt | Use case |
|---|--------|----------|
| 01 | Hero post long-form | LinkedIn manifesto / 1500-2000 char post |
| 02 | Carousel 10 slides | LinkedIn carousel structure |
| 03 | Klantcase narrative | Veco/Beutech case → post format |
| 04 | Contrarian take | Hot take / industry-pushback post |
| 05 | Quote card | Visual quote-card brief (Higgsfield prompt) |
| 06 | Reply script | Comment-engagement responses |
| 07 | DM follow-up | Inbox outreach scripts |
| 08 | Newsletter tip | Wekelijks 1-tip e-mail body |
| 09 | X thread converter | LinkedIn long-form → X-thread split |
| 10 | Loom/YouTube script | Screen-recording script (45-90s) |
| 11 | Meta ad copy | Meta/IG ad-copy variants (5 hooks per brief) |
| 12 | Subject line A/B | Email subject-line generator |
| 13 | Pipedrive update | Deal-update template per stage |
| 14 | Engineer-Lens (Apify Monitor) | 6e generation-track op Trending Recruitment NL nieuws-items — Recruitment Engineer-stem voor LI-Wouter posts |

## Voor Sander (auto-poster pipeline)

Prompt 14 is bedoeld voor de bestaande Apify Monitor → Content Calendar (master) pipeline in Notion. Voeg toe als 6e generation-track. Trigger: `Topic ∈ {Arbeidsmarkt, Recruiter-tips, Salaris, Werkenbij}`. Output gaat naar Channel=`LI-Wouter`, Pijler=keuze LLM (A/B/D/Long-form), Status=`Drafted`.

Detail-spec: zie `14-engineer-lens.md` (volledige prompt + golden rules + verboden vocabulaire).
