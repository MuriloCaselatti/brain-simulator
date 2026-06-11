# SPEC-009 — Visualização Neural (Three.js)

**Status:** ⏳ | **Modelo:** Sonnet 4.6 | **Depende de:** SPEC-002

## Objetivo
Servidor WebSocket em Python + cena 3D Three.js com 8 regiões cerebrais, arcos sinápticos e partículas de spike.

## Entregáveis
- `visualization/server.py` — FastAPI + WebSocket, streaming de estado a 30fps
- `visualization/static/index.html`
- `visualization/static/brain_scene.js` — cena Three.js principal
- `visualization/static/neural_objects.js` — BrainRegion, SynapticArc, SpikeParticle
- `visualization/static/controls.js` — play/pause/step/speed/isolate

## Encodings Visuais
- Cor da esfera → firing rate (azul=baixo → vermelho=alto, heatmap)
- Espessura do arco → força sináptica
- Partícula flash → spike event
- Halo global → nível de dopamina

## Critérios de Aceitação
- [ ] Browser renderiza 8 regiões em 3D com posições anatômicas
- [ ] Atualiza a ≥ 25fps com dados reais do engine
- [ ] Spike visível como partícula flash
- [ ] Controles play/pause/step funcionam via WebSocket bidirecional

## Prompt para Claude Code
```
Leia specs/CONTEXT.md e specs/SPEC-009-visualization.md.
O servidor Python faz streaming de snapshots via WebSocket a cada 33ms (~30fps).
O StateRenderer NÃO bloqueia o clock do SimulationEngine — é assíncrono.
Three.js usa GPU integrada (WebGL) — funciona sem CUDA.
Anatomia 3D das regiões está definida no BLUEPRINT.md seção 11.
```
