# Brain Simulator — Contexto Vivo
> **Leia este arquivo no início de TODA sessão Claude Code.**
> Atualizado ao fim de cada sessão.

---

## Status Atual
**Fase:** 1 — Core (em progresso)
**Próxima sessão:** SPEC-003 (LIF + STDP + Learning Engine)
**Última atualização:** 2026-06-11 (SPEC-004 implementado fora de ordem — ver nota abaixo)

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

## O que está em progresso
- Nada em progresso (SPEC-002 e SPEC-004 fechados; aguardando início do SPEC-003)

## O que vem a seguir
1. **SPEC-003:** `core/neuron.py` (LIF vetorizado, Brian2), `core/synapse.py`
   (STDP), `core/learning_engine.py` (TD-Learning + PlasticityScheduler).
   Implementar como `CognitiveModule`s plugados no `SimulationEngine` via
   `add_module()` — **não alterar `core/interfaces.py` nem
   `core/brain_bus.py`/`core/simulation_engine.py` sem necessidade**.
   Após SPEC-003, validar integração dos módulos de memória (SPEC-004)
   no `SimulationEngine`.

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
**Status:** 🔜 Próxima (SPEC-002 concluído)
**Branch:** —
**Notas:** —

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
**Status:** ⏳ Aguarda SPEC-001, 002
**Branch:** —
**Notas:** —

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
