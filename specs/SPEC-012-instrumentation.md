# SPEC-012 — Instrumentação + Logs + Replay

**Status:** ⏳ | **Modelo:** Sonnet 4.6 | **Depende de:** SPEC-002

## Objetivo
Observabilidade completa: logs estruturados JSONL, snapshots HDF5, replay determinístico.

## Entregáveis
- `core/instrumentation.py` — logger estruturado por módulo/timestep
- `core/replay.py` — grava e reproduce simulações identicamente

## Critérios de Aceitação
- [ ] Simulação de 10s salva em HDF5 < 50MB
- [ ] Replay reproduz identicamente (seed fixo)
- [ ] Logs consultáveis por módulo_id e range de timestep

## Prompt para Claude Code
```
Leia specs/CONTEXT.md e specs/SPEC-012-instrumentation.md.
Instrumentation registra a cada N timesteps (configurável) para não saturar disco.
Replay usa seed para determinismo — importante para reprodutibilidade científica.
Formato HDF5: groups por módulo, datasets por variável (voltage, spikes, weights).
```
