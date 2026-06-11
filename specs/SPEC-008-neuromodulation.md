# SPEC-008 — Neuromodulação

**Status:** ⏳ | **Modelo:** Sonnet 4.6 | **Depende de:** SPEC-002, SPEC-003

## Objetivo
Dopamina (TD-error broadcast), Noradrenalina (arousal/threshold), Acetilcolina (atenção/plasticidade).

## Entregáveis
- `modules/neuromodulation/dopamine.py` — TD-error → NeuromodulationSignal global
- `modules/neuromodulation/noradrenaline.py` — arousal → ajuste de V_thresh
- `modules/neuromodulation/acetylcholine.py` — sinal/ruído atencional

## Critérios de Aceitação
- [ ] Burst dopaminérgico aumenta LR de STDP em todos os módulos
- [ ] Silêncio dopaminérgico (omissão de recompensa) diminui pesos ativos
- [ ] Noradrenalina alta → V_thresh cai → neurônios mais responsivos
- [ ] Replica qualativamente Schultz 1997

## Prompt para Claude Code
```
Leia specs/CONTEXT.md e specs/SPEC-008-neuromodulation.md.
Os neuromoduladores são sinais GLOBAIS que o BrainBus broadcast para todos os módulos.
Dopamina ∝ TD-error: positivo = burst, negativo = silêncio, zero = basal (1.0).
Implemente NeuromodulatorSystem que centraliza os 3 sistemas.
```
