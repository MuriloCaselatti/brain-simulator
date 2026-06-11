# SPEC-010 — Dashboard Científico

**Status:** ⏳ | **Modelo:** Sonnet 4.6 | **Depende de:** SPEC-009

## Objetivo
Overlays com raster plots, firing rate por módulo, pesos sinápticos e TD-error em tempo real.

## Entregáveis
- `visualization/static/hud.js` — métricas e overlays
- `visualization/static/charts.js` — raster plot, firing rate, pesos, TD-error

## Critérios de Aceitação
- [ ] Raster plot atualiza em tempo real para módulo selecionado
- [ ] Firing rate exibido por módulo (Hz, média da população)
- [ ] TD-error mostrado como sinal temporal
- [ ] Pausa/resume/replay funcionam sem corrupção de estado visual

## Prompt para Claude Code
```
Leia specs/CONTEXT.md e specs/SPEC-010-dashboard.md.
Construa sobre SPEC-009. Adicione HUD com: raster plot flutuante por módulo,
firing rate em tempo real (linha por módulo), TD-error como sinal temporal.
Use canvas 2D para os plots (não Three.js — WebGL é para a cena 3D).
```
