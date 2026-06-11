# SPEC-008 — Neuromodulação

**Status:** ✅ Concluído (2026-06-11) | **Modelo:** Sonnet 4.6 | **Depende de:** SPEC-002, SPEC-003

## Objetivo
Dopamina (TD-error broadcast), Noradrenalina (arousal/threshold), Acetilcolina (atenção/plasticidade).

## Entregáveis
- `modules/neuromodulation/dopamine.py` — TD-error → NeuromodulationSignal global
- `modules/neuromodulation/noradrenaline.py` — arousal → ajuste de V_thresh
- `modules/neuromodulation/acetylcholine.py` — sinal/ruído atencional

## Critérios de Aceitação
- [x] Burst dopaminérgico aumenta LR de STDP em todos os módulos
- [x] Silêncio dopaminérgico (omissão de recompensa) diminui pesos ativos
- [x] Noradrenalina alta → V_thresh cai → neurônios mais responsivos
- [x] Replica qualativamente Schultz 1997

Validado em `tests/scientific/test_dopamine_validation.py` (4 testes) e
`tests/unit/test_neuromodulation.py` (26 testes). Suite: 192/192.

## Prompt para Claude Code
```
Leia specs/CONTEXT.md e specs/SPEC-008-neuromodulation.md.
Os neuromoduladores são sinais GLOBAIS que o BrainBus broadcast para todos os módulos.
Dopamina ∝ TD-error: positivo = burst, negativo = silêncio, zero = basal (1.0).
Implemente NeuromodulatorSystem que centraliza os 3 sistemas.
```
