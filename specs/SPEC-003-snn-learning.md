# SPEC-003 — LIF Neuron + STDP + Learning Engine

**Status:** ✅ Concluído (2026-06-11) | **Modelo:** Sonnet 4.6 (impl) + Opus 4.8 (validação)
**Branch:** — | **Depende de:** SPEC-001

---

## Objetivo
Implementar o neurônio LIF vetorizado com Brian2, a sinapse STDP e o Learning Engine completo.

## Escopo
- `core/neuron.py` — LIFPopulation (vetorizado, Brian2)
- `core/synapse.py` — STDPSynapse
- `core/learning_engine.py` — STDP + Hebb + TD-Learning + PlasticityScheduler

## Parâmetros Biológicos Padrão
```
V_rest = -70.0 mV   V_thresh = -55.0 mV   V_reset = -70.0 mV
tau_m = 20.0 ms     t_refract = 2.0 ms
STDP: A+ = 0.01, A- = 0.0105, tau+ = tau- = 20ms
TD: alpha = 0.1, gamma = 0.95
```

## Validação Científica Obrigatória (Brian2 oracle)
- Firing rate: 10–100 Hz para corrente fisiológica
- STDP: curva assimétrica conforme Bi & Poo 1998
- Lei do tudo-ou-nada verificada

## Critérios de Aceitação
- [x] LIF dispara na faixa correta (10–100 Hz)
- [x] STDP aumenta peso para pré→pós e diminui para pós→pré
- [x] TD-error é positivo quando recompensa > esperada
- [x] `pytest tests/scientific/test_lif_validation.py` → pass

## Prompt para Claude Code
```
Leia specs/CONTEXT.md e specs/SPEC-003-snn-learning.md.
Implemente LIF vetorizado com Brian2 para populações de 500-2000 neurônios.
IMPORTANTE: valide contra literatura — use Brian2 para confirmar que firing rates
estão dentro do range biológico (10-100 Hz) e STDP replica Bi & Poo 1998.
Ao terminar: todos os testes científicos passam + atualizar CONTEXT.md.
```
