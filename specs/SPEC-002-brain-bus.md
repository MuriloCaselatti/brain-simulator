# SPEC-002 — BrainBus + SimulationEngine

**Status:** ⏳ Aguarda SPEC-001 | **Modelo:** Sonnet 4.6
**Branch:** `feat/spec-002` | **Depende de:** SPEC-001

---

## Objetivo
Implementar o engine de simulação com clock global e o BrainBus pub/sub síncrono.

## Escopo
- `core/brain_bus.py` — implementação completa
- `core/simulation_engine.py` — TimeLoop + StateBuffer + topological ordering

## Entregáveis
1. `BrainBus` com `publish()`, `subscribe()`, `tick()`, `get_history()`
2. `SimulationEngine` com `add_module()`, `run(duration_ms)`, `step()`, `pause()`, `reset()`
3. `StateBuffer` ring buffer para replay (últimos 10s = 10.000 timesteps)
4. `tests/unit/test_engine.py`

## Critérios de Aceitação
- [ ] Simula 100ms com 3 módulos mock
- [ ] BrainBus publica eventos na ordem topológica
- [ ] StateBuffer armazena e recupera histórico correto
- [ ] `pytest tests/unit/test_engine.py` → 100% pass

## Prompt para Claude Code
```
Leia specs/CONTEXT.md e specs/SPEC-002-brain-bus.md.
Implemente BrainBus e SimulationEngine conforme o Blueprint.
O BrainBus é síncrono: todos os módulos avançam no mesmo dt=1ms.
A ordem de execução é topológica (Sensory → Attention → Memory → ... → LearningEngine).
StateRenderer é notificado mas NÃO bloqueia o clock principal.
Ao terminar: pytest tests/unit/test_engine.py 100% pass + atualizar CONTEXT.md.
```
