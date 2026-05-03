# 07-automation-pipeline

**Status:** scaffold — content to be filled in by parallel agents during build-out.

Per the MASTER-PLAN, this is "the real lever" of the campaign — once the pipeline is in place, content + ads run on auto-pilot in fases 2-4.

## Planned files

| File | Purpose |
|------|---------|
| `ad-generator-agent.jsx` | React artifact for the Claude API ad generator (input form → hooks/copy/headlines/CTAs/visual brief/motion brief/Meta JSON) |
| `higgsfield-templates.md` | Soul 2 + Nano Banana 2 prompt templates (hero portraits, brand visuals, marketing studio ads) |
| `seedance-templates.md` | Image-to-video prompts (5-8s, identity preservation, 9:16/1:1/16:9/4:5) |
| `zapier-flow-config.md` | Notion publish-status "Ready" → auto-post LinkedIn + Meta with UTM injection |

## The flow (from MASTER-PLAN.md)

```
CLAUDE BRIEFING (input form)
    ↓
CLAUDE generates: copy + visual brief + motion brief
    ↓
HIGGSFIELD MCP (Soul 2 / Nano Banana 2 / Marketing Studio)
    ↓
SEEDANCE 2.0 (image-to-video, identity preservation)
    ↓
CLAUDE post-production (5x hooks, 5x headlines, 3x CTAs)
    ↓
META ADS MCP / LINKEDIN ADS (auto-upload, A/B framework)
    ↓
MAANDAG 09:00 — Performance Monitor (Agent 3, already built)
```

**Target:** briefing → live ad in 30-45 minutes (vs 8 hours manual).

## TODO

- [ ] Build ad-generator-agent.jsx (React artifact)
- [ ] Lock Higgsfield templates (reuse Euromaster Sora templates from chat history)
- [ ] Test Seedance pipeline with 3 sample scenes
- [ ] Configure Notion content calendar + Zapier auto-poster
- [ ] Wire Meta Ads MCP + LinkedIn Ads MCP
