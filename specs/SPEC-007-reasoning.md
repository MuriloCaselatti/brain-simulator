# SPEC-007 — Sistema de Raciocínio

**Status:** ⏳ | **Modelo:** Sonnet 4.6 | **Depende de:** SPEC-004, SPEC-006

## Objetivo
PFC Executive (controle inibitório + planejamento), RL dual (model-based + model-free), DecisionGate.

## Entregáveis
- `modules/reasoning/pfc.py` — supervisor executivo, inibição de respostas impulsivas
- `modules/reasoning/model_based.py` — deliberação com modelo interno do mundo
- `modules/reasoning/model_free.py` — aprendizado habitual (gânglios da base)
- `modules/reasoning/decision_gate.py` — integra emoção + razão → ação

## Critérios de Aceitação
- [ ] Model-free converge em 2-armed bandit task (< 200 trials)
- [ ] Model-based supera model-free em tarefa com inversão de contingência
- [ ] PFC inibe resposta impulsiva quando recompensa > threshold de controle

## Prompt para Claude Code
```
Leia specs/CONTEXT.md e specs/SPEC-007-reasoning.md.
Implemente RL dual paralelo: model-free (rápido, inflexível) e model-based (lento, flexível).
Stress/urgência favorece model-free — implemente essa transição.
Valide com bandit task documentada em tests/scientific/.
```
