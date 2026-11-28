# Engineering evidence / Evidências de engenharia — 2026-11-28

Owner: João Victor da Silva (JustJao1). Evidence captured from GitHub Actions logs and workflow conclusions. Historical snapshot; check linked runs for details. Coverage percentages are coverage.py branch-inclusive TOTAL, not full application/UI coverage. Reports expire according to repository retention. No independent professional experience or personal proficiency is inferred from these automated changes.

| Project | Observed result | Source |
|---|---|---|
| Meu Ritmo | 12 Playwright tests passed (desktop and mobile); Node tests passed. Docker validation in progress. | [Technical notes](https://github.com/JustJao1/meu-ritmo/blob/engineering-quality/docs/engineering-quality.md) · [CI run](https://github.com/JustJao1/meu-ritmo/actions/runs/46110741076) |
| API Studio | 12 tests passed · 58% coverage · Docker validated. | [Technical notes](https://github.com/JustJao1/api-studio/blob/main/docs/engineering-quality.md) · [CI run](https://github.com/JustJao1/api-studio/actions/runs/46110525119) |
| Imovance | 15 tests passed · 91% coverage · Docker validated. | [Technical notes](https://github.com/JustJao1/imovance/blob/main/docs/engineering-quality.md) · [CI run](https://github.com/JustJao1/imovance/actions/runs/46110707421) |
| Doc Intelligence | 2 tests passed · 49% coverage · Docker validated. | [Technical notes](https://github.com/JustJao1/doc-intelligence/blob/main/docs/engineering-quality.md) · [CI run](https://github.com/JustJao1/doc-intelligence/actions/runs/46110644311) |
| FlowEngine | 2 tests passed · 61% coverage · Docker validated. | [Technical notes](https://github.com/JustJao1/flow-engine/blob/main/docs/engineering-quality.md) · [CI run](https://github.com/JustJao1/flow-engine/actions/runs/46110642208) |
| Pulse Monitor | 2 tests passed · 50% coverage · Docker validated. | [Technical notes](https://github.com/JustJao1/pulse-monitor/blob/main/docs/engineering-quality.md) · [CI run](https://github.com/JustJao1/pulse-monitor/actions/runs/46110648409) |
| Freight Connect | 2 tests passed · 43% coverage · Docker validated. | [Technical notes](https://github.com/JustJao1/freight-connect/blob/main/docs/engineering-quality.md) · [CI run](https://github.com/JustJao1/freight-connect/actions/runs/46110650940) |
| Traincore | Static checks and UI container passed; AI API is outside the container. | [Technical notes](https://github.com/JustJao1/traincore/blob/main/docs/engineering-quality.md) · [CI run](https://github.com/JustJao1/traincore/actions/runs/46110693946) |
| Meu Ritmo App | Existing workflow passed; native documentation. No new device validation. | [Technical notes](https://github.com/JustJao1/meu-ritmo-app/blob/main/docs/engineering-quality.md) · [CI run](https://github.com/JustJao1/meu-ritmo-app/actions/runs/46110698089) |
| LinkPilot | Experimental project documentation. Original source unavailable for new tests. | [Technical notes](https://github.com/JustJao1/linkpilot/blob/main/docs/engineering-quality.md) |

The Meu Ritmo core job and pre-existing Verify workflow passed; initial browser run had 10 passes and 2 failures ([initial run](https://github.com/JustJao1/meu-ritmo/actions/runs/46110567015)). After synchronization, the browser job passed all 12 tests. Docker validation remains pending. PR #71. No live payment, email or customer account was exercised. LinkPilot source is unavailable; Android device and release signing are not newly validated. Docker images use version tags; not bit-identical builds. Deployment workflows were preserved.
