# Brain Simulator — Contexto Vivo
> **Leia este arquivo no início de TODA sessão Claude Code.**
> Atualizado ao fim de cada sessão.

---

## Status Atual
**Fase:** 4 — Visualização (concluída) / 5 — Instrumentação (concluída) / 6 — Linguagem (concluída) / 7 — Testes Científicos (concluída)
**Próxima sessão:** Higiene de branches / consolidação na `main` (todas as SPECs implementadas)
**Última atualização:** 2026-06-11 (SPEC-013 concluído)

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

- **SPEC-004 — Memória (concluído 2026-06-11, fora de ordem)**
  - `modules/memory/working.py`: `WorkingMemory` — rede recorrente de
    `N_ATTRACTORS = 7` pools mutuamente inibitórios (winner-take-all),
    cada um biestável (`gain=8`, `threshold=4`, dinâmica leaky com
    `tau_ms=20`). Um cue que sobrepõe fortemente um pool empurra seu
    `level` escalar para o ponto fixo alto (~0.98); sem input, o
    fixed-point alto é estável e o padrão persiste (testado por 500ms
    sem input).
  - `modules/memory/episodic.py`: `EpisodicMemory` — **Modern Hopfield
    Network** (Ramsauer et al. 2020), *não* o Hopfield clássico de 1982.
    Update `xi_new = X^T softmax(beta * X xi)` em `n_iters=1` passo,
    `beta=8.0`. Recupera padrões bipolares de dim 100 com 30% de ruído
    em uma única iteração (capacidade exponencial). FIFO em
    `max_patterns`.
  - `modules/memory/semantic.py`: `SemanticMemory` — grafo de conceitos
    (NetworkX) + embeddings via `sentence-transformers`
    (`all-MiniLM-L6-v2`, lazy-load com cache em nível de módulo);
    fallback determinístico por hashing se o modelo não puder ser
    carregado (offline/sem GPU). `query()` retorna top-k por similaridade
    de cosseno; `add_relation()` cria arestas tipadas/ponderadas
    consumidas por `get_synaptic_targets()`.
  - Todos os 3 módulos implementam `CognitiveModule` ABC (SPEC-001)
    sem alterações na interface congelada.
  - `tests/unit/test_memory.py`: 18 testes novos (contrato
    `CognitiveModule` para os 3 módulos, persistência de 500ms na
    WorkingMemory, recuperação com 30% de ruído na EpisodicMemory,
    busca top-5 e relações na SemanticMemory) — **100% pass** (52/52
    no total).
  - Dependência nova instalada: `sentence-transformers` (já listada em
    `requirements.txt`); upgrade incidental de `numpy` 2.4.6 → 2.2.6
    (ainda numpy 2.x, compatível com torch 2.9 — sem impacto nos testes
    existentes).
  - **Nota:** SPEC-004 declarava depender de SPEC-003, mas foi
    implementado a pedido do usuário antes do SPEC-003. Os 3 módulos de
    memória não dependem de `core/neuron.py`/`core/synapse.py` (ainda
    inexistentes) — operam em `numpy` puro sobre o contrato
    `CognitiveModule`. Quando o SPEC-003 for implementado, validar a
    integração via `SimulationEngine.add_module()`.

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
- **SPEC-006 — Processamento Preditivo (concluído 2026-06-11)**
  - `modules/predictive_coding/layer.py`: `PredictiveLayer` — um nível da
    hierarquia Rao & Ballard 1999. Neurônios de **predição** (`r`, geram
    `predict() = W·r` para a camada inferior) + neurônios de **erro**
    (`compute_error() = abaixo − predição`). Helper NumPy puro, **não** é
    `CognitiveModule` (mutado pela hierarquia, padrão `STDPSynapse`/ADR-008).
    Aprendizado Hebbiano guiado por erro `W += lr·(π·outer(ε,r) − decay·W)`
    (gradiente na energia livre precision-weighted), estabilizado com weight
    decay + norma de coluna limitada (`max_col_norm`) — evita a divergência
    do laço conjunto inferência/aprendizado.
  - `modules/predictive_coding/hierarchy.py`:
    `PredictiveCodingHierarchy(CognitiveModule)` — 3 níveis conectados
    (`level_sizes=(48,32,16)` sobre `input_size=64` por padrão). `update()`
    roda `n_inference_steps` iterações de settling (gradiente descendente:
    bottom-up `Wᵀ(π·ε)` − top-down `π·ε_acima` − leak), depois aplica
    aprendizado interno. Precisão `π = base·(1+ganho·attention_signal)·ACh`
    (acetilcolina via `apply_neuromodulation`) — a atenção do `DAN` (SPEC-005)
    escala o peso do erro. `set_top_down_prior()` injeta expectativa no topo
    (gancho p/ priming por `EpisodicMemory`/SPEC-004). Saídas
    spiking-compatíveis (taxas retificadas em Hz + máscara binária) +
    `internal_state` com `prediction_error_per_level`, `weighted_error_per_level`,
    `free_energy`, `precision`, `top_prediction`. Núcleo rate-based (híbrido:
    backing por `LIFPopulation` é ponto de extensão documentado, off por padrão).
  - `modules/predictive_coding/__init__.py`: reexporta
    `PredictiveCodingHierarchy`, `PredictiveLayer`.
  - `tests/unit/test_predictive_coding.py`: 14 testes — contrato
    `CognitiveModule`, e os 3 critérios de aceitação: erro cai com treino
    repetido (`< 0.5·` inicial; e **não** cai com plasticidade congelada),
    prior top-down modula a representação inferior, atenção/precisão escala o
    erro ponderado (e ACh=0 zera a precisão). **130/130 no total.**
  - Integração com `SimulationEngine`/`BrainBus` verificada via `add_module()`.
  - **Design matemático confirmado com Opus 4.8 antes de implementar.**

- **SPEC-007 — Raciocínio (concluído 2026-06-11)**
  - `modules/reasoning/model_free.py`: `ModelFreeRL` — sistema habitual
    (gânglios da base). `q_values` por ação, atualizados por
    Rescorla-Wagner/TD(0) (`update_value`, `learning_rate=0.05` padrão,
    escalado por dopamina via `apply_neuromodulation`). Seleção de ação por
    softmax (`select_action`, `temperature=0.2`) — **rápido** (lookup
    direto), mas **inflexível** (taxa de aprendizado pequena e fixa, lento
    para reaprender após mudança de contingência).
  - `modules/reasoning/model_based.py`: `ModelBasedRL` — sistema
    deliberativo. Mantém `reward_model` (modelo de mundo explícito por
    ação), atualizado com `model_learning_rate=0.3` (maior que o do
    model-free → **flexível**, readapta em poucos trials após reversão).
    `deliberate()`/`select_action()` simulam o modelo (`n_simulations=20`,
    reportado em `internal_state["deliberation_steps"]`) antes de decidir →
    **lento** (custo computacional por decisão).
  - `modules/reasoning/pfc.py`: `PFCExecutive` — inibição executiva. Lê o
    vetor de valores do model-free; se o valor da ação mais tentadora excede
    `effective_threshold()` (= `control_threshold`, padrão 0.5), publica
    `internal_state["inhibit"]=True` e zera essa ação no `gate`. Estresse
    (`noradrenaline > 1.0`, via `inputs.neuromodulation`/
    `apply_neuromodulation`) eleva `effective_threshold` proporcionalmente a
    `noradrenaline_sensitivity` — sob estresse agudo o PFC deixa de inibir
    (Arnsten 2009).
  - `modules/reasoning/decision_gate.py`: `DecisionGate` — arbitragem final.
    Combina `[model_free_probs, model_based_probs]` via
    `w_model_free = sigmoid(stress_gain * (noradrenaline -
    baseline_noradrenaline))` (`baseline=1.0` → pesos iguais;
    `noradrenaline` alto → mais peso ao model-free — Schwabe & Wolf 2009).
    `set_inhibition_gate()` aplica o veto do PFC antes de renormalizar e
    escolher a ação final (`internal_state["action"]`).
  - Todos os 4 módulos implementam `CognitiveModule` ABC (SPEC-001) sem
    alterações na interface congelada; `get_synaptic_targets()` de PFC e
    DecisionGate retornam `[]` (não possuem sinapses aprendidas — apenas
    arbitram/gateiam).
  - `tests/unit/test_reasoning.py` (32 testes): contrato `CognitiveModule`
    para os 4 módulos, Rescorla-Wagner/atualização do modelo de recompensa,
    gating por dopamina/noradrenalina, inibição do PFC, arbitragem do
    DecisionGate, reset.
  - `tests/scientific/test_bandit_validation.py`: critérios de aceitação
    SPEC-007 — (1) model-free converge (>70% braço melhor) em 200 trials de
    bandit 2-braços; (2) model-based supera model-free após inversão de
    contingência (média de 30 seeds, `reward_model` flexível readapta mais
    rápido que `q_values` cacheados); (3) PFC inibe ação impulsiva quando
    `valor > control_threshold`; (4) pipeline completo (model_free +
    model_based + PFC + DecisionGate) — sob `noradrenaline=1.0` o PFC inibe
    a ação impulsiva e a decisão segue o model-based; sob
    `noradrenaline=2.0` o PFC deixa de inibir e a arbitragem favorece o
    model-free, que passa a vencer.
  - **Suite completa: 162/162 testes passam** (`pytest tests/ -q`).
  - `core/interfaces.py`, `core/brain_bus.py`, `core/simulation_engine.py` e
    os módulos das SPECs 002-006 não foram alterados.

- **SPEC-008 — Neuromodulação (concluído 2026-06-11)**
  - `modules/neuromodulation/dopamine.py`: `DopamineSystem` — canal de
    reward-prediction error (Schultz 1997). Mapeia TD-error → nível fásico
    centrado no basal `1.0`: `level = clip(1.0 + gain·drive, 0, 2)`. TD>0 →
    **burst** (>1), TD<0 → **silêncio/dip** (<1), TD=0 → basal. O drive
    relaxa exponencialmente (`tau_ms=50`) de volta ao basal (resposta
    fásica). Helper NumPy puro, **não** é `CognitiveModule` (padrão
    `STDPSynapse`/ADR-008).
  - `modules/neuromodulation/noradrenaline.py`: `NoradrenalineSystem` —
    canal de arousal (locus coeruleus, Aston-Jones & Cohen 2005).
    `level = clip(1.0 + gain·arousal, 0, 2)`, arousal∈[0,1]. Consumido por
    `LIFPopulation.apply_neuromodulation`: nível acima do basal **baixa o
    V_thresh** → neurônios mais responsivos. Decay `tau_ms=200`.
  - `modules/neuromodulation/acetylcholine.py`: `AcetylcholineSystem` —
    canal de SNR atencional/plasticidade (forebrain basal, Yu & Dayan 2005).
    `level = clip(1.0 + att_gain·(attention−0.5) + unc_gain·uncertainty, 0, 2)`.
    Consumido por `LIFPopulation` (ganho de SNR) e `PlasticityScheduler`
    (gate de STDP, threshold 0.3). Decay para baseline neutro.
  - `modules/neuromodulation/system.py`:
    `NeuromodulatorSystem(CognitiveModule)` — centraliza os 3 canais e emite
    o `NeuromodulationSignal` **global**. Nó tardio na cadeia
    (`Reasoning → Neuromodulators → LearningEngine`). Drivers via
    `set_td_error`/`observe_reward` (dopamina), `set_arousal`
    (noradrenalina), `set_attention`/`set_uncertainty` (acetilcolina; ACh
    usa `inputs.attention_signal` por padrão). `connect_learning_engine()`
    puxa `last_td_error` automaticamente a cada tick (fecha o laço
    dopamina→LR). `current_signal` property exposta ao engine.
    `apply_neuromodulation` é no-op (é a *fonte*, não um *sink*).
  - **Wiring no `SimulationEngine` (aditivo, gancho do SPEC-008):**
    `register_neuromodulator(module_id)` designa o módulo-fonte. Quando
    registrado, `step()` (a) chama `apply_neuromodulation(self.neuromodulation)`
    em **todos** os módulos antes do tick e (b) atualiza `self.neuromodulation`
    a partir do `current_signal` da fonte após ela rodar — sinal emitido no
    tick N é broadcast no tick N+1 (latência síncrona de 1 tick do BrainBus).
    Sem neuromodulador registrado, o engine mantém o sinal basal e **não**
    chama `apply_neuromodulation` (comportamento pré-SPEC-008 preservado;
    resolve a pendência #3 do CONTEXT).
  - `modules/neuromodulation/__init__.py`: reexporta `DopamineSystem`,
    `NoradrenalineSystem`, `AcetylcholineSystem`, `NeuromodulatorSystem`.
  - `tests/unit/test_neuromodulation.py` (26 testes): canais isolados,
    contrato `CognitiveModule`, drivers, `current_signal`, reset, integração
    com o engine (broadcast no tick seguinte; basal sem registro).
  - `tests/scientific/test_dopamine_validation.py` (4 testes — critérios de
    aceitação SPEC-008): (1) burst aumenta a LR de STDP em múltiplas
    projeções; (2) silêncio dopaminérgico (omissão, TD<0) deprime sinapses
    ativas via regra three-factor `dw = lr·(DA−1)·elegibilidade`
    (Reynolds & Wickens 2002); (3) noradrenalina alta baixa o V_thresh →
    firing rate maior (validado contra o backend Brian2 LIF); (4) replicação
    qualitativa de Schultz 1997 (burst/none/dip).
  - **Suite completa: 192/192 testes passam** (`pytest tests/ -q`).
  - `core/interfaces.py` não foi alterado (contrato congelado intacto).
    `core/simulation_engine.py` recebeu mudanças **aditivas** (sem quebrar
    APIs existentes).

- **SPEC-009 — Visualização Three.js (concluído 2026-06-11)**
  - `visualization/server.py`: FastAPI + WebSocket. `SimulationRunner` roda o
    `SimulationEngine` num **thread daemon** ("sim-clock"), paceado por
    `speed` (1 sim-ms por `1/speed` wall-ms). O StateRenderer registrado via
    `engine.register_state_renderer()` **não bloqueia o clock**: o callback
    `_on_snapshot` só serializa um resumo pequeno (mean/max firing rate por
    região, voltagem média, flag de spike) sob lock, *throttled* a 30fps; o
    engine já engole exceções de renderer. Um `_broadcast_loop` async lê o
    último frame ~30×/s e faz push para todos os WebSockets. Comandos do
    browser (`play`/`pause`/`step`/`speed`/`isolate`/`clear_isolate`/`reset`)
    chegam pelo mesmo socket e são aplicados via `handle_command` (flags
    atômicas + lock para o set `isolated`). `serialize_layout`/`serialize_frame`
    são JSON-safe (sem escalares numpy vazando). Endpoints: `GET /` (index),
    `GET /api/layout`, `WS /ws`, `/static`. Rodar: `python -m visualization.server`.
  - `visualization/demo_brain.py`: `DemoRegion(CognitiveModule)` — população
    rate-based leve (Poisson não-homogêneo, oscilação intrínseca + drive
    proporcional à fração de aferentes ativos; NA escala excitabilidade, ACh
    o ganho de drive atendido). `build_demo_brain()` monta as **8 regiões**
    anatômicas do BLUEPRINT §11 num **DAG** (`EXECUTION_DEPENDENCIES`, sem
    ciclos para o Kahn) + um `NeuromodulatorSystem` (registrado como fonte via
    `register_neuromodulator`, anima o halo de dopamina e propaga NA/ACh).
    `REGION_LAYOUT` (pos/cor/raio) e `REGION_CONNECTIONS` (arcos visuais,
    incluindo feedback top-down cosmético) alimentam o frontend. **Decisão de
    escopo:** SPEC-009 é visualização — os módulos cognitivos reais (Brian2 LIF
    ~70ms/run, sentence-transformers) são pesados demais p/ 1000 ticks/s em
    tempo real, então a viz roda `DemoRegion` *através do engine/BrainBus reais*
    (dado genuíno do pipeline; só a dinâmica por-região é simplificada). Trocar
    por módulo real = outra chamada `add_module`.
  - `visualization/static/`: `index.html` (importmap apontando p/ Three.js r160
    **vendorizado** em `static/vendor/three/` — funciona 100% offline, sem CDN),
    `neural_objects.js`
    (`BrainRegion` esfera+heatmap+pulse, `SynapticArc` tubo curvo exc/inib,
    `SpikeParticle` flash aditivo, `DopamineHalo` anel), `brain_scene.js`
    (renderer/câmera/OrbitControls, render loop independente da taxa de dados,
    FPS counter, raycast p/ isolar região por clique), `controls.js` (cliente
    WebSocket + fiação dos botões, reconexão automática).
  - `tests/unit/test_visualization.py` (14 testes): contrato `CognitiveModule`
    da `DemoRegion`, demo brain sem ciclo + 8 estados de região, propagação de
    atividade source→downstream, serialização JSON-safe de layout/frame,
    `SimulationRunner` (step/play-pause/speed clamp/isolate toggle/reset/thread
    rodando), renderer não-bloqueante. Smoke E2E via `TestClient`: layout no
    connect → comandos `play`/`speed` → stream de frames com 8 regiões.
  - **Suite completa: 206/206 testes passam** (`pytest tests/ -q`).
  - `core/` intacto (contrato congelado; nenhuma alteração no engine/bus).

- **SPEC-010 — Dashboard Científico (concluído 2026-06-11)**
  - `visualization/server.py`: `RASTER_NEURONS = 64` e `TD_ERROR_TAU_MS = 50.0`
    (mesmo tau do `DopamineSystem`). `_subsample_spikes(spikes, n)` reduz/expande
    a máscara de spikes de cada região para exatamente `n` entradas 0/1 (raster
    leve a 30fps). `serialize_frame()` ganhou `td_error: float` (kw-only) e cada
    região no payload ganhou `"raster": [0/1]*RASTER_NEURONS`. `SimulationRunner`
    mantém `_last_td_error` (decai exponencialmente em `_drive_neuromodulators`,
    recebe o retorno de `observe_reward()` no burst de recompensa ~1x/s);
    `reset` zera `_last_td_error`.
  - `visualization/static/charts.js` (novo): `RasterPlot` (canvas 2D,
    `getImageData`/`putImageData` para scroll horizontal de colunas de spikes) e
    `LineChart` genérico (múltiplas séries, auto-scale de eixo Y com padding 15%
    ou `yMin`/`yMax` fixos, grid, linha de zero opcional).
  - `visualization/static/hud.js` (novo): `class Hud` — monta o seletor de
    módulo (`#raster-select`), legenda de cores (`#rate-legend`), e instancia
    `RasterPlot` (módulo selecionado) + `LineChart` para firing rate (8 séries,
    `yMax=60Hz`) + `LineChart` para TD-error (1 série, zero-line). `applyFrame()`
    deduplica por `timestamp_ms` (ignora frames repetidos durante pause) e detecta
    reset (`timestamp_ms` menor que o anterior) para limpar os 3 charts —
    satisfaz o critério "pause/resume/replay sem corrupção visual".
  - `visualization/static/index.html`: painel flutuante `#hud-charts`
    (`top:300px; right:16px`, abaixo do `#legend`) com raster plot + seletor,
    firing rate (linha por módulo) e TD-error.
  - `visualization/static/controls.js`: parâmetro renomeado `hud` → `chartHud`
    (colidia com o objeto local `hud` de stats de texto pré-existente — causava
    `SyntaxError` que quebrava o módulo inteiro e impedia a cena 3D/WebSocket de
    inicializar). `brain_scene.js` agora instancia `new Hud()` e passa para
    `setupControls(scene, hud)`.
  - `tests/unit/test_visualization.py`: 2 testes novos
    (`test_runner_drives_td_error_signal`, `test_runner_reset_clears_td_error`)
    + asserções de `raster`/`td_error` em `test_serialize_frame_is_json_safe_and_complete`.
    **208/208 testes passam** (`pytest tests/ -q`).
  - Verificado no browser via preview: status "connected", 8 regiões no
    seletor, raster/firing-rate/TD-error desenhando ao vivo, TD-error com picos
    periódicos (~1/s) decaindo, pause mantém estado, reset+step limpa os 3
    charts corretamente. `core/` intacto.

- **SPEC-011 — Módulo de Linguagem (Claude API) (concluído 2026-06-11)**
  - `modules/language/encoder.py`: `SpikeCodec` — codec determinístico
    semântico↔spike (NumPy puro, offline). `vector_to_spikes` rate-codeia um
    vetor denso em máscara binária `[n_neurons]` + taxas em Hz (min-max →
    `[0,1]`, threshold → spikes, `×max_rate_hz`); `spikes_to_vector` lê
    spikes/rates de volta a um vetor `embedding_dim` (inverso aproximado);
    `encode_text`/`embed_text` embute texto via `embed_fn` injetado (ex.:
    `SemanticMemory.embed`) ou fallback de hashing dependency-free.
  - `modules/language/claude_module.py`:
    - `ClaudeModule(CognitiveModule)` — região de linguagem. `update()` decodifica
      `inputs.spike_trains` para ativação; **gateia** a chamada ao Claude por
      (a) `activation_threshold` (acetilcolina baixa o threshold efetivo via
      `apply_neuromodulation`) e (b) `min_call_interval_ms` de tempo simulado
      entre calls. Quando ativado, monta prompt a partir de `set_context()`
      (ex.: top concepts da `SemanticMemory`) ou do padrão de ativação, chama o
      cliente, e re-encoda a resposta em spikes via `SpikeCodec`. Fora de
      ativação, decai para o silêncio. `get_synaptic_targets()` → `[]` (sem
      sinapses plásticas, como o PFC). `reset()` limpa estado + cache.
    - `ClaudeClient` (Protocol `complete(prompt)->str`), `AnthropicClient`
      (SDK oficial `anthropic`, **lazy import**, model SPEC-011
      `claude-sonnet-4-6`), `MockClaudeClient` (determinístico, **sem API key,
      sem rede** — default do módulo), `ResponseCache` (LRU `prompt→response`).
  - **Segurança:** **nenhuma API key no código/repo.** `AnthropicClient` lê
    `ANTHROPIC_API_KEY` do ambiente (como o SDK), levanta `RuntimeError` claro
    se ausente; `.env` já está no `.gitignore`. Default offline (mock) →
    testes/CI não precisam de key. **A chave colada no prompt da sessão foi
    exposta em texto plano e deve ser ROTACIONADA no console da Anthropic.**
  - `tests/unit/test_language.py`: 17 testes — contrato `CognitiveModule`,
    codec roundtrip/determinismo, gating por ativação + intervalo mínimo, cache
    (LRU + reuso evita call repetida), gate por acetilcolina, mock sem key,
    `AnthropicClient` levanta sem key, integração com `SimulationEngine`.
    **225/225 no total** (`pytest tests/ -q`).
  - `core/` intacto (contrato congelado). Pendência SPEC-004↔003 não tocada.

- **SPEC-012 — Instrumentação + Replay (concluído 2026-06-11)**
  - `core/instrumentation.py`: `InstrumentationConfig` (`output_dir`, `run_name`,
    `log_every_n_steps` padrão `10`, `compression="gzip"`, `dtype=float32`) +
    `InstrumentationLogger` — StateRenderer (`register_state_renderer(logger.record)`,
    portanto não bloqueia o clock; exceções são engolidas pelo engine como nos
    demais renderers). A cada tick amostrado (`tick % log_every_n_steps == 0`)
    grava: (1) `<run_name>.jsonl` — uma linha por `(step, module_id)` com
    `mean_voltage`, `mean_firing_rate`, `mean_weight`, `active_synapses`,
    `n_spikes`, `metadata` (sanitizado via `_json_safe` para tipos numpy); (2)
    `<run_name>.h5` — um group por `module_id`, datasets resizable
    (`maxshape=(None, n_neurons)`, `chunks=True`, gzip) por variável:
    `timestamps`, `voltage`, `firing_rate`, `spikes` (de
    `ModuleOutputs.spike_trains` via `BusEvent("module_output")`),
    `mean_weight`, `active_synapses`. `set_seed()` grava o seed como atributo
    HDF5 (provenance). `iter_logs(jsonl_path, module_id=, start_step=,
    end_step=)` consulta os logs; `list_modules`/`read_module_series` leem o
    HDF5 de volta.
  - `core/replay.py`: `run_seeded(factory, seed, n_steps)` constrói um engine
    via `factory(seed)` (factory deve recriar **todos** os módulos
    estocásticos a partir do seed — `DemoRegion`/`ModelFreeRL`/etc. já aceitam
    `seed`/`rng`, SPEC-006/007/009) e roda `n_steps` ticks. `verify_replay(...)`
    roda duas vezes a partir do mesmo seed e compara `ModuleState.voltage`/
    `firing_rate`/`mean_weight`/`active_synapses` tick-a-tick — lista vazia de
    `ReplayMismatch` = replay determinístico (critério de aceitação SPEC-012).
    `ReplayRecorder` (context manager) registra um `InstrumentationLogger` no
    engine e grava o `seed` como provenance; `ReplayPlayer` lê o HDF5 gravado
    de volta como uma sequência de frames por tick (sem re-simular) — útil
    para alimentar a visualização em "modo replay".
  - `core/__init__.py`: reexporta `InstrumentationConfig`,
    `InstrumentationLogger`, `iter_logs`, `list_modules`, `read_module_series`,
    `ReplayMismatch`, `ReplayPlayer`, `ReplayRecorder`, `run_seeded`,
    `verify_replay`.
  - `tests/unit/test_instrumentation.py` (6 testes): sampling a cada N ticks,
    shapes/dtype dos datasets HDF5 (`voltage`/`spikes` = `[n_sampled, n_neurons]`,
    `float32`), provenance do seed, `iter_logs` filtrando por `module_id` e
    range de `step`, `verify_replay` determinístico com `build_demo_brain`
    (SPEC-009, seed fixo) — incluindo um teste de sanidade de que seeds
    diferentes *divergem* (a checagem de diff não é vácua) — e round-trip
    `ReplayRecorder`/`ReplayPlayer`.
  - `tests/scientific/test_instrumentation_validation.py` (1 teste, critério de
    aceitação SPEC-012): simulação completa de 10s (10.000 ticks,
    `build_demo_brain(n_neurons=50)`, `log_every_n_steps=10` → 1000 amostras)
    grava HDF5 < 50MB. Roda à parte de `tests/unit/` (~2min) por ser uma
    execução real de 10k ticks — mesmo padrão de
    `tests/scientific/test_bandit_validation.py`.
  - **Suite completa após merge com SPEC-011: 232/232 testes passam**
    (`pytest tests/ -q`; 212 em `tests/unit/` + 20 em `tests/scientific/`,
    incluindo o teste de 10s/10k-ticks deste SPEC).
  - **Nota de design:** `ModuleState` (interface congelada SPEC-001) expõe
    apenas `mean_weight` (escalar), não a matriz de pesos completa — o dataset
    HDF5 `weights` é portanto a série temporal de `mean_weight` por módulo, não
    a matriz `[N_pre, N_post]`. Para inspecionar pesos completos seria preciso
    um hook adicional fora do contrato `CognitiveModule` (fora de escopo
    SPEC-012).
  - `core/interfaces.py`, `core/brain_bus.py`, `core/simulation_engine.py` não
    foram alterados.

## O que está em progresso
- Nada em progresso (SPEC-001 a 013 fechados — **todas as SPECs implementadas**).
- **Ação pendente do usuário:** rotacionar a API key da Anthropic exposta em
  texto plano no prompt da sessão SPEC-011 (ver nota de segurança acima).

## O que vem a seguir
1. **SPEC-013:** ✅ concluído nesta sessão (suite científica + integração +
   benchmarks, Brian2 como oracle).
2. **Pendência (não-bloqueante):** validar a integração dos módulos de
   memória (SPEC-004) com `LIFPopulation`/`STDPSynapse`/`LearningEngine`
   (SPEC-003) via `SimulationEngine.add_module()` — os três módulos de
   memória ainda foram testados isoladamente, em `numpy` puro.
3. **Resolvido no SPEC-008:** a `SimulationEngine` agora chama
   `apply_neuromodulation` automaticamente em todos os módulos quando um
   `NeuromodulatorSystem` é registrado via `register_neuromodulator()`. Os
   módulos do SPEC-007 que também leem `inputs.neuromodulation` em `update()`
   continuam funcionando (o sinal chega pelas duas vias).
4. **Higiene de branches:** SPEC-004/005/006/007 vivem nesta branch, ainda
   **fora da `main`**. Consolidar na `main` em ordem via PRs.

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
**Status:** ✅ Concluído (2026-06-11, fora de ordem — ver nota em "O que foi feito")
**Branch:** —
**Notas:** `WorkingMemory` (7 atratores biestáveis), `EpisodicMemory`
(Modern Hopfield Network, Ramsauer 2020 — recupera padrões com 30% de
ruído), `SemanticMemory` (sentence-transformers + NetworkX, com fallback
de hashing offline). 18 testes novos em `tests/unit/test_memory.py`,
52/52 no total. Integração com `SimulationEngine`/SPEC-003 ainda não
validada.

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
**Status:** ✅ Concluído (2026-06-11)
**Branch:** `claude/cranky-morse-cae97f`
**Notas:** `PredictiveLayer` + `PredictiveCodingHierarchy`
(`modules/predictive_coding/`). Hierarquia Rao & Ballard 1999 de 3 níveis:
predição top-down `W·r`, erro `abaixo − predição`, inferência por gradiente na
energia livre, precisão `π = base·(1+ganho·attention)·ACh` (atenção do DAN
escala o erro), aprendizado Hebbiano interno guiado por erro (estabilizado com
weight decay + norma de coluna). Substrato híbrido (núcleo rate-based + saídas
spiking). Design confirmado com Opus 4.8. 14 testes novos, 130/130 no total.

### SPEC-007 — Raciocínio
**Status:** ✅ Concluído (2026-06-11)
**Branch:** `claude/admiring-morse-8c5809`
**Notas:** RL dual paralelo (`modules/reasoning/`): `ModelFreeRL`
(Rescorla-Wagner, rápido/inflexível) + `ModelBasedRL` (modelo de mundo
explícito, lento/flexível). `PFCExecutive` inibe ação impulsiva acima de
`control_threshold`; estresse (noradrenalina) eleva o threshold (PFC menos
eficaz) e desloca a arbitragem do `DecisionGate` para o model-free
(Schwabe & Wolf 2009, Arnsten 2009). 32 testes novos, 162/162 no total.
Validação científica em `tests/scientific/test_bandit_validation.py`
(bandit 2-braços, inversão de contingência, inibição PFC, transição por
estresse).

### SPEC-008 — Neuromodulação
**Status:** ✅ Concluído (2026-06-11)
**Branch:** `claude/ecstatic-fermi-b697b3`
**Notas:** 3 canais globais (`modules/neuromodulation/`): `DopamineSystem`
(TD-error → burst/silêncio/basal, Schultz 1997), `NoradrenalineSystem`
(arousal → baixa V_thresh) e `AcetylcholineSystem` (atenção/incerteza → SNR +
gate de plasticidade). `NeuromodulatorSystem(CognitiveModule)` centraliza os 3
e emite o `NeuromodulationSignal` global; `connect_learning_engine()` fecha o
laço dopamina→LR. `SimulationEngine.register_neuromodulator()` faz o broadcast
aditivo (apply_neuromodulation em todos os módulos + refresh do sinal, latência
1 tick). 30 testes novos (26 unit + 4 científicos, critérios de aceitação),
192/192 no total. `core/interfaces.py` intacto.

### SPEC-009 — Visualização Three.js
**Status:** ✅ Concluído (2026-06-11)
**Branch:** `claude/admiring-swirles-fd8b9f`
**Notas:** `visualization/server.py` (FastAPI + WebSocket, `SimulationRunner` em
thread, StateRenderer throttled a 30fps **não-bloqueante**, broadcaster async,
comandos bidirecionais play/pause/step/speed/isolate/reset), `demo_brain.py`
(8 regiões anatômicas BLUEPRINT §11 como `DemoRegion(CognitiveModule)` num DAG +
`NeuromodulatorSystem` p/ halo de dopamina, rodando pelo engine/BrainBus reais),
`static/` (Three.js r160 via importmap: `BrainRegion`/`SynapticArc`/
`SpikeParticle`/`DopamineHalo`, heatmap firing rate, raycast p/ isolar). 14
testes novos + smoke E2E `TestClient`. 206/206 no total. `core/` intacto.
Critérios de aceitação: 8 regiões 3D nas posições anatômicas ✅, stream de dados
reais do engine ✅, spike como flash de partícula ✅, controles play/pause/step
via WebSocket bidirecional ✅. Three.js **vendorizado** (`static/vendor/three/`,
offline). **Fix Windows:** `.js` era servido como `text/plain` (registro do
Windows) e o browser recusa ES modules com MIME errado (strict checking) — o
servidor agora força `mimetypes.add_type("text/javascript", ".js"/".mjs")` no
startup. **Pendência leve:** FPS≥25 a verificar no browser do hardware-alvo.

### SPEC-010 — Dashboard Científico
**Status:** ✅ Concluído (2026-06-11)
**Branch:** `claude/ecstatic-mclaren-853bad`
**Notas:** HUD canvas2D sobre a cena 3D (`static/charts.js` + `static/hud.js`):
`RasterPlot` (scroll de spikes via `getImageData`/`putImageData`, 64 neurônios
subamostrados por região) e `LineChart` genérico (firing rate por módulo,
TD-error com zero-line). `serialize_frame` ganhou `raster`/`td_error` por
região; `SimulationRunner._last_td_error` decai com `tau=50ms` (igual ao
`DopamineSystem`) e recebe burst de `observe_reward()` ~1x/s. Dedup por
`timestamp_ms` + detecção de reset (timestamp menor) limpam os charts sem
corrupção visual. **Fix colateral:** `controls.js` tinha colisão de identificador
`hud` (parâmetro novo vs. objeto local de stats) que quebrava o módulo inteiro
via `SyntaxError` — renomeado para `chartHud`. 2 testes novos, 208/208 no total.
Verificado end-to-end no browser (preview).

### SPEC-011 — Módulo de Linguagem
**Status:** ✅ Concluído (2026-06-11)
**Branch:** —
**Notas:** `ClaudeModule` + `SpikeCodec` (`modules/language/`). Região de
linguagem bidirecional (spike→prompt→Claude→spike) com gating por ativação +
intervalo mínimo, cache LRU de respostas, e `MockClaudeClient` offline (default,
sem API key). `AnthropicClient` usa o SDK oficial (model `claude-sonnet-4-6`) e
lê `ANTHROPIC_API_KEY` do ambiente — **nenhuma key no código** (`.env` no
gitignore). 17 testes novos, 225/225 no total. **Ação pendente do usuário:
rotacionar a API key exposta no prompt da sessão.**

### SPEC-012 — Instrumentação + Replay
**Status:** ✅ Concluído (2026-06-11)
**Branch:** —
**Notas:** `core/instrumentation.py` (`InstrumentationLogger` — StateRenderer
não-bloqueante, JSONL + HDF5 amostrados a cada `log_every_n_steps`, groups por
módulo/datasets por variável, `iter_logs` consultável por `module_id`/range de
`step`) + `core/replay.py` (`verify_replay`/`run_seeded` — re-execução
determinística a partir de um seed via `factory(seed)`; `ReplayRecorder`/
`ReplayPlayer` para gravação com provenance de seed + playback sem
re-simulação). 6 testes novos em `tests/unit/test_instrumentation.py` + 1
teste de aceitação (10s/10k ticks → HDF5 < 50MB) em
`tests/scientific/test_instrumentation_validation.py`. 215/215 no total.
`core/interfaces.py`/`brain_bus.py`/`simulation_engine.py` não alterados.

### SPEC-013 — Testes Científicos
**Status:** ✅ Concluído (2026-06-11)
**Branch:** `claude/unruffled-wing-a9de7a`
**Notas:** Suite de validação científica com **Brian2 como oracle**. Corretude
de cada teste revisada com Opus 4.8 antes de implementar (calibração empírica
das tolerâncias sensíveis). Entregáveis:
- `tests/scientific/test_stdp_bi_poo.py` (5 testes): reconstrói a curva
  Δw(Δt) completa (14 offsets, ±40ms), valida assimetria LTP/LTD (Bi & Poo
  1998), decaimento exponencial monotônico, e **R² > 0.90** vs. (a) oráculo
  Brian2 `Synapses` (mesmas equações de traço) e (b) janela analítica
  `A±·exp(-|Δt|/τ)`; fit log-linear do ramo LTP recupera τ+≈20ms.
- `tests/scientific/test_td_schultz.py` (5 testes): protocolo de
  condicionamento de estado único (γ=0) — burst no reward inesperado
  (TD>0), **transferência/decaimento** do TD a ~0 conforme o valor aprende a
  prever (V→reward), ausência de resposta ao reward predito, e **dip** (TD<0)
  na omissão; integra `DopamineSystem` (burst>1/basal≈1/dip<1) e o desconto γ.
  (Schultz 1997.)
- `tests/scientific/test_hopfield.py` (6 testes): **oráculo Hopfield clássico**
  (W=ΣξξᵀN, diagonal zero, dinâmica de sinal síncrona) reproduz a transição de
  fase — recall ~perfeito abaixo de 0.10N, colapso catastrófico acima de
  0.25N — e capacidade crítica medida (cruzamento de overlap m≈0.96) em
  ≈0.138N (±10%; nota: ±5% do SPEC é o limite termodinâmico, finite-N
  síncrono dá ~0.13–0.14). A `EpisodicMemory` (**Modern Hopfield**, Ramsauer
  2020) cumpre o piso de 0.14N e o **excede** (recall perfeito a load 1.0–2.0
  sob 30% ruído / 50% cue parcial), recuperando onde o clássico colapsa.
- `tests/scientific/test_working_memory.py` (3 testes): persistência de
  atividade pós-estímulo (Compte 2000) — cue de 50ms leva o atrator ao ponto
  fixo alto, atividade persiste ≥500ms **sem input** (level>0.8, mesmo
  atrator); silêncio sem cue; seletividade a distratores fracos
  (sub-`match_threshold`).
- `tests/integration/test_full_pipeline.py` (5 testes): pipeline de **módulos
  reais leves** (sensory→saliency→DAN, working/episodic memory, predictive
  coding, neuromodulators) num `SimulationEngine` real, 1000 ticks (1s):
  ordem topológica válida, estado finito (sem NaN/Inf) em todo tick,
  broadcast de neuromodulação a todos os módulos (`apply_neuromodulation`),
  histórico de replay completo, e **determinismo** bit-a-bit dado o seed
  (pré-condição do replay SPEC-012). `LIFPopulation` fica fora do loop de
  1000 ticks (overhead fixo ~70-100ms/`net.run`) — validada à parte.
- `tests/performance/test_benchmarks.py` (3 testes, marca `performance`):
  `simulate_100ms(n=2000) < 5s` (avanço de 100ms de tempo biológico num único
  `update`, ~0.3s; o caminho amortizado — stepping a 1ms tem overhead fixo do
  Brian2 e é medido indiretamente); `visualizer_fps() >= 25` via proxy de
  backend (taxa de produção+serialização de frames do demo brain, ~800/s; o
  FPS WebGL real é verificado manualmente no hardware-alvo); `memory_usage_mb()
  < 4096` (RSS ~170MB com LIF 2000 + demo brain). Hardware desta sessão é
  representativo do alvo (Windows 11).
- **Interpretação científica registrada:** o critério Hopfield "≥0.14N" é o
  piso clássico (Hopfield 1982/AGS 1985); nossa memória episódica é uma rede
  de Hopfield *moderna* (capacidade exponencial) e o supera. A tolerância ±5%
  de capacidade refere-se ao limite N→∞.
- **Suite completa após SPEC-013: 259/259 testes passam** (`pytest tests/ -q`,
  ~5min — inclui os 27 novos: 19 científicos + 5 integração + 3 performance, e
  o teste de 10s/10k-ticks do SPEC-012).
- `core/` intacto (contrato congelado). Nenhum módulo de implementação alterado
  — apenas testes novos (a suite expôs só edge-cases de harness de teste:
  tempos de spike e ruído de ponto flutuante, corrigidos nos testes).
