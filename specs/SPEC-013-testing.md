# SPEC-013 — Testes e Validação Científica

**Status:** ⏳ | **Modelo:** Opus 4.8 | **Depende de:** Todos os módulos

## Objetivo
Suite completa de validação científica usando Brian2 como oracle de referência.

## Entregáveis
- `tests/scientific/test_lif_validation.py` — LIF vs. Brian2 oracle
- `tests/scientific/test_stdp_bi_poo.py` — STDP replica Bi & Poo 1998
- `tests/scientific/test_td_schultz.py` — TD-error replica Schultz 1997
- `tests/scientific/test_hopfield.py` — capacidade e completamento
- `tests/integration/test_full_pipeline.py` — pipeline completo 1 segundo
- `tests/performance/test_benchmarks.py` — limites de hardware

## Validações Científicas Obrigatórias

| Teste | Referência | Critério |
|-------|-----------|---------|
| LIF firing rate | Adrian 1926 | 10–100 Hz |
| STDP | Bi & Poo 1998 | Curva assimétrica Δw(Δt) |
| Hopfield capacidade | Hopfield 1982 | ≥ 0.14N padrões |
| TD-error | Schultz 1997 | Burst → recompensa inesperada |
| Working Memory | Compte 2000 | Persistência pós-stimulus |

## Benchmark de Performance (Acer Aspire 3)
```python
assert simulate_100ms(n_neurons=2000) < 5.0  # segundos
assert visualizer_fps() >= 25
assert memory_usage_mb() < 4096
```

## Prompt para Claude Code
```
Leia specs/CONTEXT.md e specs/SPEC-013-testing.md.
Use Opus 4.8 para revisar a corretude científica de cada teste antes de implementar.
Brian2 é o oracle: simule o mesmo cenário em Brian2 e compare com nossa implementação.
Tolerâncias: firing rate ±10%, STDP curve R² > 0.90, Hopfield capacity ±5%.
```
