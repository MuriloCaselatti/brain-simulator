# Brain Simulator — Contexto Vivo
> **Leia este arquivo no início de TODA sessão Claude Code.**
> Atualizado ao fim de cada sessão.

---

## Status Atual
**Fase:** 1 — Core (em progresso)
**Próxima sessão:** SPEC-004 (Memória — Modern Hopfield Networks)
**Última atualização:** 2026-06-11

---

## O que foi feito
- [x] Base científica consolidada (82 fontes, NotebookLM)
- [x] Decisões arquiteturais finalizadas (ver DECISIONS.md)
- [x] Blueprint aprovado (`specs/BLUEPRINT.md`)
- [x] Repositório inicializado com estrutura completa
- [x] 13 SPECs definidos e priorizados
- [x] **SPEC-001 — Arquitetura Base + Interfaces (concluído 2026-06-11)**
  - `core/interfaces.py`: `CognitiveModule` ABC + `ModuleInputs`, `ModuleOutputs`,
    `ModuleState`, `NeuromodulationSignal`, `SynapticTarget` — docstrings em inglês
    técnico, apenas stdlib + numpy, `INTERFACE_VERSION = "1.0.0"`.
  - `core/brain_bus.py`: stub (`publish`/`subscribe`/`tick`/`get_history` →
    `NotImplementedError` referenciando SPEC-002).
  - `core/__init__.py`: reexporta o contrato congelado.
  - `tests/unit/test_interfaces.py`: 13 testes de contrato (inclui rejeição de
    instanciação da ABC e de implementação incompleta) — **100% pass**.
  - **Interface `CognitiveModule` CONGELADA na v1.0.0** (ver ADR-008).
- **SPEC-002 — BrainBus + SimulationEngine (concluído 2026-06-11)**
  - `core/brain_bus.py`: `BrainBus` síncrono com `BusEvent`/`BusSnapshot`.
    `publish()` notifica subscribers (`subscribe(event_type, handler)`,
    incluindo `"*"` wildcard) sincronamente; `publish_state()` registra o
    `ModuleState` de cada módulo no tick atual; `tick(timestamp_ms)` fecha o
    timestep, arquiva o snapshot num `deque(maxlen=10_000)` (StateBuffer —
    10s de replay a dt=1ms) e limpa os buffers pendentes; `get_history(n)`
    retorna os últimos `n` snapshots (oldest-first).
  - `core/simulation_engine.py`: `SimulationEngine` com clock global
    `dt = 1.0ms`. `add_module(module, depends_on=[...])` registra módulos e
    dependências; `execution_order` calcula ordem topológica via Kahn
    (desempate pela ordem de inserção, preservando a cadeia padrão
    Sensory → Attention → Memory → ... → LearningEngine). `step()` executa
    cada módulo na ordem topológica, monta `ModuleInputs` a partir das
    saídas (`spike_trains` concatenados, `attention_signal` propagado via
    `internal_state["attention_signal"]`) publicadas pelas dependências
    *no mesmo tick*, publica `ModuleOutputs`/`ModuleState` no BrainBus e
    fecha o tick. `register_state_renderer(callback)` registra callbacks de
    StateRenderer notificados após cada tick — exceções são engolidas e
    **não bloqueiam o clock**. `run(duration_ms)`, `pause()`/`resume()`,
    `reset()` (reseta módulos, zera o clock e limpa o histórico do bus) e
    `get_history(n_steps)` (delegando ao BrainBus) completam a API.
  - `core/__init__.py`: reexporta `BrainBus`, `BusEvent`, `BusSnapshot`,
    `SimulationEngine`.
  - `tests/unit/test_engine.py`: 21 testes (BrainBus pub/sub/tick/history,
    StateBuffer com limite de 10.000 passos, ordenação topológica e detecção
    de ciclos, causalidade síncrona dentro do tick, cenário de aceitação de
    100ms com 3 módulos mock, StateRenderer não bloqueante, pause/resume,
    reset) — **100% pass** (34/34 com SPEC-001).
- **SPEC-003 — LIF + STDP + Learning Engine (concluído 2026-06-11)**
  - `core/neuron.py`: `LIFPopulation(CognitiveModule)` — população vetorizada
    de 500–2000 neurônios LIF sobre Brian2 (`NeuronGroup` + `SpikeMonitor` +
    `Network`/`Clock` próprios por instância, permitindo múltiplas populações
    independentes). Parâmetros biológicos padrão SPEC-003
    (`V_REST=-70mV, V_THRESH=-55mV, V_RESET=-70mV, TAU_M=20ms, T_REFRACT=2ms`).
    `prefs.codegen.target = "numpy"` fixado (sem dependência de compilador
    C++/CUDA — ADR-001). Passo de integração interno `0.1ms` (vs. dt=1ms do
    BrainBus). `update()` combina corrente externa
    (`set_input_current`), drive pré-sináptico (`spike_trains` somados ×
    `input_gain`) e ganho atencional (`attention_signal` × ganho de
    acetilcolina). `apply_neuromodulation`: noradrenalina desloca o limiar de
    disparo, acetilcolina escala o ganho atencional. `_compute_firing_rate`
    usa uma janela deslizante (`rate_window_ms`, padrão 100ms) sobre as
    *contagens* de disparos por neurônio (não apenas um booleano), para que
    `update()` com `dt` grande (ex.: validação científica) reporte taxas
    corretas mesmo com múltiplos disparos por neurônio no intervalo.
  - `core/synapse.py`: `STDPSynapse` — sinapse STDP vetorizada (NumPy puro,
    não é `CognitiveModule` — mutada in-place via `SynapticTarget.weight_matrix`
    por `LearningEngine`, conforme ADR-008). Regra par-a-par baseada em traços
    (`trace_pre`/`trace_post`) com `A_PLUS=0.01, A_MINUS=0.0105,
    TAU_PLUS=TAU_MINUS=20ms`; pesos clampados em `[w_min, w_max]`;
    `lr_scale` permite congelar/escalar a plasticidade; `reset()` restaura
    pesos iniciais e zera traços.
  - `core/learning_engine.py`: `LearningEngine(CognitiveModule)` +
    `PlasticityScheduler`. `register_projection(synapse, source_module,
    target_module)` registra projeções STDP; `update()` divide
    `inputs.spike_trains` por projeção (seguindo a ordem de inserção, que
    deve casar com `depends_on` no `SimulationEngine`/`_build_inputs`),
    aplica STDP apenas quando `PlasticityScheduler.is_plastic()` (gate por
    acetilcolina, threshold padrão 0.3). TD-Learning (`compute_td_error`,
    `apply_td_update`): `delta = reward + gamma*value_next - value_estimate`,
    `TD_ALPHA=0.1, TD_GAMMA=0.95`, taxa de aprendizado escalada por dopamina
    (`PlasticityScheduler.learning_rate_scale`, `max(0, dopamine)`).
  - `core/__init__.py`: reexporta `LIFPopulation`, `STDPSynapse`,
    `LearningEngine`, `PlasticityScheduler`.
  - **Validação científica (Brian2 como oracle)** —
    `tests/scientific/test_lif_validation.py`:
    - Firing rate de população LIF sob corrente fisiológica (20mV, acima do
      reobase de 15mV) cai em ~10–100Hz (Adrian 1926) — `dt=1000ms` num único
      `update()` para amortizar o overhead fixo (~70ms) de cada `net.run()`.
    - Lei do tudo-ou-nada: spike trains binários, voltagem sempre em
      `[V_RESET, V_THRESH]`, taxa de disparo cresce com a corrente mas a
      *forma* da resposta não muda.
    - STDP (`STDPSynapse`) validado contra um oráculo Brian2
      `Synapses`/`SpikeGeneratorGroup` com a mesma regra de traços
      (`A_PLUS/A_MINUS/TAU_PLUS/TAU_MINUS`): pré-antes-pós → LTP,
      pós-antes-pré → LTD, magnitude decai com `|Δt|` (Bi & Poo 1998),
      concordância de sinal e magnitude (`abs=2e-3`).
    - TD-error positivo quando `reward > value_estimate`, zero quando casam
      (Schultz 1997).
  - `tests/unit/test_neuron.py` (13), `tests/unit/test_synapse.py` (7),
    `tests/unit/test_learning_engine.py` (13) — contrato `CognitiveModule`,
    plasticidade, neuromodulação, reset.
  - **Suite completa: 79/79 testes passam** (`pytest tests/ -q`), incluindo
    11 testes científicos em `tests/scientific/test_lif_validation.py`.
  - **Nota não-bloqueante:** `pip install brian2` atualizou numpy para 2.4.6,
    gerando um `UserWarning` do scipy (`numpy<2.3,>=1.22.4 required`) — não
    afeta os testes, mas vale revisitar se `scipy`/`tensorflow-intel` forem
    usados diretamente em SPECs futuros.
  - `core/interfaces.py`, `core/brain_bus.py` e `core/simulation_engine.py`
    não foram alterados.

- **SPEC-005 — Atenção: DAN, VAN, SaliencyMap (concluído 2026-06-11)**
  - `modules/attention/_utils.py`: helpers compartilhados — `align_to`
    (pad/truncate para `n_neurons`, pois o `SimulationEngine` concatena os
    `spike_trains` de todas as dependências), `normalize` (escala para
    `[0, 1]`), `center_surround_contrast` (campo receptivo center-surround
    1D em anel).
  - `modules/attention/saliency.py`: `SaliencyMap(CognitiveModule)` —
    combina novidade temporal (média móvel exponencial,
    `novelty_tau_ms=50ms`) com contraste espacial center-surround
    (`contrast_weight=0.5`), normaliza para `[0, 1]`.
    `apply_neuromodulation`: noradrenalina escala o ganho de excitação
    (`_noradrenaline_gain`) aplicado à saliência bruta antes da
    normalização. Saída: `spike_trains`/`internal_state["saliency_map"]`
    (mapa contínuo `[0, 1]`), `internal_state["max_saliency"]` /
    `["max_saliency_index"]`.
  - `modules/attention/dan.py`: `DAN(CognitiveModule)` — recebe sinal
    top-down do PFC via `inputs.spike_trains` (vetor `[0, 1]` por posição) e
    produz `gain_map` (`internal_state["gain_map"]` /
    `outputs.spike_trains`) que modula o ganho do módulo sensorial:
    `gain = baseline_gain + pfc_signal * gain_amplification *
    acetylcholine_gain * van_suppression`. Com os defaults
    (`baseline_gain=1.0`, `gain_amplification=2.5`), o ganho no alvo
    (`pfc_signal=1.0`) é `3.5`, ou seja `>= 2x` o ganho do distrator
    (`baseline=1.0`) — critério de aceitação SPEC-005. Publica
    `internal_state["attention_signal"]` (consumido pelo
    `SimulationEngine` como `ModuleInputs.attention_signal` no tick
    seguinte) e `internal_state["dan_focus"]`.
    `apply_neuromodulation`: acetilcolina escala `gain_amplification`.
  - `modules/attention/van.py`: `VAN(CognitiveModule)` — consome o mapa de
    saliência via `inputs.spike_trains` (dependência de `SaliencyMap`); se
    `max(saliency) >= effective_threshold`
    (`interrupt_threshold + dan_focus * dan_suppression_strength`, escalado
    pela acetilcolina), dispara `internal_state["interrupt"]=True`,
    `["interrupt_location"]` e `["attention_signal"]=redirect_attention_signal`
    (redireciona o ganho atencional no tick seguinte). Como o BrainBus é
    síncrono em `dt=1ms`, a interrupção é decidida e publicada dentro do
    mesmo tick — `<< 20ms` simulados (critério de aceitação SPEC-005).
  - **Anticorrelação DAN-VAN** (critério de aceitação SPEC-005): acoplamento
    explícito via `DAN.set_van_activation(van.van_activation)` (suprime
    `gain_map`/`dan_focus` quando VAN dispara) e
    `VAN.set_dan_suppression(dan.dan_focus)` (eleva `effective_threshold`
    quando DAN está fortemente focado). Sem fiação automática no
    `SimulationEngine` — ambos os módulos expõem getters/setters para essa
    troca, a ser conectada por quem registra os módulos (ex.: SPEC-008/
    orquestração futura).
  - `modules/attention/__init__.py`: reexporta `DAN`, `VAN`, `SaliencyMap`.
  - `tests/unit/test_attention.py` (19 testes): contrato `CognitiveModule`,
    detecção de novidade/contraste, ganho >= 2x DAN, interrupção VAN em 1
    tick, gating por acetilcolina/noradrenalina, anticorrelação DAN-VAN
    round-trip, reset.
  - **Suite completa: 98/98 testes passam** (`pytest tests/ -q`).
  - `core/interfaces.py`, `core/brain_bus.py`, `core/simulation_engine.py`
    e os módulos do SPEC-003 não foram alterados.

## O que está em progresso
- Nada em progresso (SPEC-005 fechado; aguardando início do SPEC-004)

## O que vem a seguir
1. **SPEC-004:** Memória (Modern Hopfield Networks, Ramsauer 2020) —
   implementar como `CognitiveModule` plugado via `add_module()`, usando
   `LIFPopulation`/`STDPSynapse`/`LearningEngine` do SPEC-003 como base de
   conectividade e plasticidade onde aplicável.

---

## Decisões Críticas (resumo rápido)

| Decisão | Escolha |
|---------|---------|
| Runtime SNN | Brian2 (CPU) |
| Neurônio base | LIF + STDP |
| Neurônios por módulo | 500–2.000 |
| Timestep | dt = 1ms |
| BrainBus | Síncrono por timestep |
| Visualização | Three.js/WebGL no browser |
| Linguagem | Claude API (módulo externo) |
| Interface base | `CognitiveModule` ABC — **CONGELAR após SPEC-001** |

---

## Hardware Alvo
- Acer Aspire 3 · 12GB RAM · GPU integrada (sem CUDA)
- Python 3.10+ · Brian2 instalado

---

## Regras de Ouro para Sessões
1. **Não implementar fora do escopo do SPEC da sessão**
2. **Interface `CognitiveModule` é sagrada — não alterar sem Opus 4.8 + aprovação**
3. **Atualizar este arquivo ao terminar**
4. **Todo módulo implementa `CognitiveModule` ABC sem exceção**
5. **Testes antes de fechar a sessão**

---

## Contexto por SPEC (atualizar conforme implementado)

### SPEC-001 — Arquitetura Base
**Status:** ✅ Concluído (2026-06-11)
**Branch:** `feat/spec-001`
**Notas:** Interface `CognitiveModule` congelada na v1.0.0 (ADR-008). 13 testes
de contrato passam. Apenas stdlib + numpy em `core/interfaces.py`.

### SPEC-002 — BrainBus + SimulationEngine
**Status:** ✅ Concluído (2026-06-11)
**Branch:** —
**Notas:** `BrainBus` síncrono (`BusEvent`/`BusSnapshot`, StateBuffer
`deque(maxlen=10_000)`) + `SimulationEngine` (Kahn topológico, TimeLoop
dt=1ms, StateRenderer não bloqueante, pause/resume/reset). 21 testes novos,
34/34 no total. `core/interfaces.py` não foi alterado.

### SPEC-003 — LIF + STDP + Learning
**Status:** ✅ Concluído (2026-06-11)
**Branch:** —
**Notas:** `LIFPopulation` (Brian2, numpy backend, 500-2000 neurônios),
`STDPSynapse` (traços, Bi & Poo 1998), `LearningEngine` + `PlasticityScheduler`
(TD-Learning, gate por acetilcolina, escala por dopamina). Validado contra
oráculo Brian2 (firing rate 10-100Hz, STDP assimétrico, TD-error). 79/79
testes passam. `core/interfaces.py`/`brain_bus.py`/`simulation_engine.py`
não alterados.

### SPEC-004 — Memória
**Status:** 🔜 Próxima (SPEC-001, 003 concluídos)
**Branch:** —
**Notas:** Estudar Modern Hopfield Networks (Ramsauer 2020) antes

### SPEC-005 — Atenção
**Status:** ✅ Concluído (2026-06-11)
**Branch:** —
**Notas:** `DAN`/`VAN`/`SaliencyMap` (`modules/attention/`). DAN amplifica
alvo `>= 2x` distrator (`gain=3.5` vs `1.0` com defaults); VAN interrompe em
1 tick (`<<20ms`) para saliência acima de `effective_threshold`;
anticorrelação DAN-VAN via `set_van_activation`/`set_dan_suppression`
(acoplamento manual, sem fiação automática no `SimulationEngine`). 19 testes
novos, 98/98 no total.

### SPEC-006 — Processamento Preditivo
**Status:** ⏳ Aguarda SPEC-004, 005
**Branch:** —
**Notas:** Estudar Rao & Ballard 1999 antes

### SPEC-007 — Raciocínio
**Status:** ⏳ Aguarda SPEC-004, 006
**Branch:** —
**Notas:** —

### SPEC-008 — Neuromodulação
**Status:** ⏳ Aguarda SPEC-002, 003
**Branch:** —
**Notas:** —

### SPEC-009 — Visualização Three.js
**Status:** ⏳ Aguarda SPEC-002
**Branch:** —
**Notas:** —

### SPEC-010 — Dashboard Científico
**Status:** ⏳ Aguarda SPEC-009
**Branch:** —
**Notas:** —

### SPEC-011 — Módulo de Linguagem
**Status:** ⏳ Aguarda SPEC-004
**Branch:** —
**Notas:** Exige chave da Claude API

### SPEC-012 — Instrumentação + Replay
**Status:** ⏳ Aguarda SPEC-002
**Branch:** —
**Notas:** —

### SPEC-013 — Testes Científicos
**Status:** ⏳ Aguarda todos
**Branch:** —
**Notas:** Brian2 como oracle de validação
