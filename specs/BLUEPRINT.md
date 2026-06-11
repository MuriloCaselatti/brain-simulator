# Brain Simulator — Blueprint Oficial de Desenvolvimento
**Versão:** 1.0 | **Data:** 2026-06-10 | **Status:** Aprovado

> Documento mestre do projeto. Fonte oficial de verdade.
> Toda decisão técnica, arquitetural e de execução deriva deste documento.

---

## Índice
1. [Diagnóstico Executivo](#1-diagnóstico-executivo)
2. [Auditoria de Conhecimento](#2-auditoria-de-conhecimento)
3. [Restrições e Hardware](#3-restrições-e-hardware)
4. [Blueprint Arquitetural](#4-blueprint-arquitetural)
5. [Estrutura de SPECs](#5-estrutura-de-specs)
6. [Organização das Sessões Claude Code](#6-organização-das-sessões-claude-code)
7. [Arquitetura de Desenvolvimento](#7-arquitetura-de-desenvolvimento)
8. [Estratégia de Contexto](#8-estratégia-de-contexto)
9. [Governança Técnica](#9-governança-técnica)
10. [Estratégia de Qualidade](#10-estratégia-de-qualidade)
11. [Plano de Visualização 3D](#11-plano-de-visualização-3d)
12. [Matriz de Uso dos Modelos de IA](#12-matriz-de-uso-dos-modelos-de-ia)
13. [Roadmap de Execução](#13-roadmap-de-execução)
14. [Riscos e Mitigações](#14-riscos-e-mitigações)

---

## 1. Diagnóstico Executivo

### O que é o Brain Simulator
Um sistema computacional bicamada que:
1. **Simula** dinâmicas cognitivas inspiradas no cérebro humano usando Spiking Neural Networks (SNN)
2. **Visualiza** atividade neural em tempo real em ambiente 3D via browser

O objetivo **não** é um chatbot nem um agente genérico de IA. O objetivo é uma plataforma de simulação cognitiva com rigor científico, onde comportamentos emergentes (memória, atenção, aprendizagem, tomada de decisão) resultam da interação de módulos neurobiologicamente fundamentados.

### Decisões Fundacionais Confirmadas

| Decisão | Escolha | Justificativa |
|---------|---------|---------------|
| Tipo de output | Engine Python + Visualização 3D | Permite experimentação científica e observação visual |
| Fidelidade biológica | SNN com LIF + STDP | Rigor científico + viabilidade em CPU |
| Arquitetura | Core Modular com Abstraction Layer | Evolutivo, testável por módulo, compatível com Claude Code |
| Runtime SNN | Brian2 (CPU) | Otimizado para CPU, gera C++, padrão acadêmico |
| Visualização | Three.js/WebGL no browser | Usa GPU integrada para renderização, fácil de iterar |
| Linguagem | Claude API (externo) | Offload total, sem custo computacional local |
| BrainBus | Síncrono por timestep (dt=1ms) | Causalidade biológica garantida |
| Dev | Solo + Claude Code | Arquitetura modular maximiza eficiência |

---

## 2. Auditoria de Conhecimento

### 2.1 O que está coberto (82 fontes — NotebookLM "Neuroscience Study")

| Domínio | Cobertura | Aplicação ao Projeto |
|---------|-----------|----------------------|
| Neurobiologia Molecular | ✅ Completo | Parâmetros LIF (V_rest, tau_m, canais iônicos) |
| Neurofisiologia | ✅ Completo | Potencial de ação, PEPS/PIPS, período refratário |
| Transmissão Sináptica | ✅ Completo | Implementação da sinapse STDP |
| Plasticidade (LTP/LTD/STDP) | ✅ Completo | Learning Engine |
| Memória (todas as formas) | ✅ Completo | MemoryModule: Working + Episódica + Semântica |
| Atenção (DAN/VAN) | ✅ Completo | AttentionModule |
| Processamento Preditivo | ✅ Completo | PredictiveCodingLayer (Rao & Ballard 1999) |
| Tomada de Decisão (RL dual) | ✅ Completo | ReasoningModule (model-free + model-based) |
| Dopamina (TD-error) | ✅ Completo | NeuromodulatorSystem |
| Sistema Límbico / Emoções | ✅ Completo | AmygdalaModule (valência + arousal) |
| Consciência (GWT, IIT) | ✅ Completo | GlobalWorkspace (fase avançada) |
| Redes Funcionais (DMN, DAN) | ✅ Completo | Módulos + oscilações como gating |
| SNN / Neurociência Computacional | ✅ Completo | Toda a camada de implementação |
| PLN / Linguagem | ✅ Parcial | Módulo de linguagem via Claude API |
| EEG / fMRI como validação | ✅ Parcial | Referência para testes científicos |

### 2.2 Lacunas identificadas

| Lacuna | Impacto | Ação |
|--------|---------|------|
| Cerebelo (controle motor fino) | Baixo para MVP | Fase futura |
| Glia (astrocitos, micróglia) | Médio | Pesquisar para fase 4+ |
| Desenvolvimento ontogenético | Baixo | Fase experimental |
| Oscilações Gamma detalhadas | Médio | Necessário para CTC (Communication Through Coherence) |
| Conectoma completo (Human Connectome Project) | Alto | Pesquisar antes do SPEC-001 |
| Parâmetros SNN validados para Brian2 | **Crítico** | Prototipar antes da implementação |

### 2.3 O que deve ser pesquisado antes de cada SPEC

- **Antes do SPEC-003 (SNN):** Parâmetros LIF calibrados em Brian2 para reproduzir padrões de firing documentados
- **Antes do SPEC-004 (Memória):** Implementação de Hopfield moderna (Ramsauer et al. 2020 — Modern Hopfield Networks)
- **Antes do SPEC-006 (Preditivo):** Implementação de referência de Predictive Coding em Python
- **Antes do SPEC-009 (Visualização):** Estudar Three.js + WebSocket streaming para dados neurais

---

## 3. Restrições e Hardware

### Ambiente de Desenvolvimento

| Item | Especificação |
|------|--------------|
| Máquina | Acer Aspire 3 |
| RAM | 12 GB |
| Armazenamento | 512 GB SSD |
| GPU | Integrada (sem CUDA) |
| Python | 3.10+ ✅ |
| Brian2 | Instalado ✅ |

### Implicações Arquiteturais

| Aspecto | Ajuste | Motivo |
|---------|--------|--------|
| Neurônios por módulo | 500–2.000 | Sem CUDA, CPU tem limite prático |
| Runtime SNN | Brian2 (CPU) | SpykeTorch exige CUDA |
| GPU da visualização | Integrada (WebGL) | Three.js usa GPU para renderização — funciona |
| Populações grandes (>50k) | Cloud / futuro | Colab GPU para experimentos maiores |
| Linguagem LLM | Claude API | Offload total — sem custo local |

### O que 500–2.000 neurônios por módulo consegue demonstrar
- Completamento de padrões (hipocampo Hopfield)
- Pattern separation (DG — Giro Denteado)
- Working memory como rede de atratores
- STDP convergindo para assemblies
- TD-error dopaminérgico modulando aprendizado

Isso é **cientificamente válido** e publicável. Escala é independente de comportamento emergente.

---

## 4. Blueprint Arquitetural

### 4.1 Visão Geral

```
┌─────────────────────────────────────────────────────┐
│                  BRAIN SIMULATOR                    │
│         SNN Core + 3D Browser Visualization         │
└─────────────────────────────────────────────────────┘

Camada de Percepção
  └── SensoryModule: encoding sensorial → spike trains

Camada de Atenção
  └── AttentionModule: DAN (top-down) + VAN (bottom-up)
  └── SaliencyMap: priorização de inputs

Camada de Memória
  └── WorkingMemory:  rede recorrente LIF (~7 atratores)
  └── EpisodicMemory: Hopfield (completamento de padrões)
  └── SemanticMemory: embeddings + grafo de conhecimento

Camada de Processamento Preditivo
  └── Hierarquia 3 níveis
  └── Erro de predição bottom-up
  └── Predição top-down

Camada de Raciocínio
  └── PFC Executive: planejamento + inibição
  └── Model-Based RL: deliberação (lento, flexível)
  └── Model-Free RL:  hábitos (rápido, rígido)

Camada de Modulação Global
  └── Dopamina:     TD-error → escala LR global
  └── Noradrenalina: arousal → ajuste de threshold
  └── Acetilcolina: atenção → plasticidade sináptica

Camada de Aprendizagem
  └── STDP por módulo
  └── Hebbiano (memória semântica)
  └── SynapticPruning + PlasticityPhases

                ↕ BrainBus (pub/sub · dt=1ms) ↕

Camada de Simulação
  └── SimulationEngine: TimeLoop + StateBuffer
  └── StateRenderer:    Three.js/WebGL via WebSocket
```

### 4.2 Interface Contratual Central

```python
# core/interfaces.py — IMUTÁVEL após SPEC-001 aprovado
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
import numpy as np

@dataclass
class ModuleInputs:
    spike_trains: np.ndarray      # [N_pre] spike mask
    attention_signal: float       # 0.0–1.0 (DAN top-down)
    neuromodulation: 'NeuromodulationSignal'
    timestamp_ms: float

@dataclass
class ModuleOutputs:
    spike_trains: np.ndarray      # [N_post]
    firing_rate: np.ndarray       # [N] spikes/s
    internal_state: dict          # para o BrainBus

@dataclass
class ModuleState:
    module_id: str
    n_neurons: int
    voltage: np.ndarray           # [N] mV
    firing_rate: np.ndarray       # [N] Hz
    mean_weight: float
    active_synapses: int
    timestamp_ms: float

@dataclass
class NeuromodulationSignal:
    dopamine: float       # 0.0–2.0 (1.0 = basal)
    noradrenaline: float  # 0.0–2.0
    acetylcholine: float  # 0.0–2.0

class CognitiveModule(ABC):
    module_id: str
    n_neurons: int

    @abstractmethod
    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        """Avança o módulo em dt milissegundos."""

    @abstractmethod
    def get_state(self) -> ModuleState:
        """Estado atual para BrainBus e visualizador."""

    @abstractmethod
    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        """Dopamina, noradrenalina, acetilcolina."""

    @abstractmethod
    def get_synaptic_targets(self) -> List['SynapticTarget']:
        """Sinapses disponíveis para STDP/Hebb."""

    @abstractmethod
    def reset(self) -> None:
        """Reinicia estado interno."""
```

### 4.3 BrainBus

```python
# core/brain_bus.py
class BrainBus:
    """
    Event broker síncrono. Roda dentro do mesmo processo que o engine.
    Todos os módulos publicam e assinam no mesmo timestep.
    """
    def publish(self, event: BusEvent) -> None: ...
    def subscribe(self, event_type: str, handler: Callable) -> None: ...
    def tick(self) -> BusSnapshot: ...          # snapshot completo do timestep
    def get_history(self, n_steps: int) -> List[BusSnapshot]: ...
```

**Ordem topológica de execução por tick:**
```
Sensory → Attention → WorkingMemory
       → EpisodicMemory → SemanticMemory
       → PredictiveCoding → Reasoning
       → Neuromodulators → LearningEngine
       → StateRenderer (async, não bloqueia o clock)
```

### 4.4 Camada de Persistência

| Dado | Formato | Localização |
|------|---------|-------------|
| Estado de simulação (runtime) | ndarray in-memory | RAM |
| Histórico recente (replay) | RingBuffer 10s | RAM |
| Snapshots de experimentos | HDF5 | `experiments/outputs/` |
| Pesos sinápticos (checkpoint) | NumPy .npz | `experiments/checkpoints/` |
| Logs de eventos | JSONL | `experiments/logs/` |
| Knowledge Graph semântico | NetworkX GraphML | `modules/memory/` |

### 4.5 Camada de Serviços (APIs internas)

| Serviço | Protocolo | Propósito |
|---------|-----------|-----------|
| SimulationEngine ↔ Módulos | Chamada direta Python | Sync, dentro do mesmo processo |
| Engine ↔ StateRenderer | WebSocket (localhost) | Streaming de estado para browser |
| Browser ↔ Controles | WebSocket bidirecional | play/pause/step/speed/isolate |
| Módulo de Linguagem ↔ Engine | Claude API (HTTP) | LLM externo sob demanda |

---

## 5. Estrutura de SPECs

Cada SPEC é uma unidade de desenvolvimento independente, executável em uma sessão Claude Code.

### SPEC-001 — Arquitetura Base + Interfaces
**Objetivo:** Criar o esqueleto do projeto: `CognitiveModule` ABC, tipos de dados, estrutura de pastas, testes de contrato.
**Dependências:** Nenhuma
**Entregáveis:** `core/interfaces.py`, `core/brain_bus.py` (stub), `tests/unit/test_interfaces.py`
**Critério de aceitação:** Todos os tipos importam sem erro; teste de contrato passa com módulo mock.

### SPEC-002 — BrainBus + SimulationEngine
**Objetivo:** Engine de simulação com clock global, BrainBus pub/sub, StateBuffer para replay.
**Dependências:** SPEC-001
**Entregáveis:** `core/brain_bus.py`, `core/simulation_engine.py`, `tests/unit/test_engine.py`
**Critério de aceitação:** Simula 100ms com 3 módulos mock, BrainBus publica corretamente, StateBuffer armazena histórico.

### SPEC-003 — LIF Neuron + STDP + Learning Engine
**Objetivo:** Neurônio LIF vetorizado (Brian2), sinapse STDP, TD-Learning, PlasticityScheduler.
**Dependências:** SPEC-001
**Entregáveis:** `core/neuron.py`, `core/synapse.py`, `core/learning_engine.py`, validação Brian2
**Critério de aceitação:** Neurônio dispara conforme lei do tudo-ou-nada; STDP converge em 1000 epochs; TD-error codifica recompensa.

### SPEC-004 — Sistema de Memória
**Objetivo:** WorkingMemory (rede recorrente de atratores), EpisodicMemory (Hopfield modernizado), SemanticMemory (embeddings + grafo).
**Dependências:** SPEC-001, SPEC-003
**Entregáveis:** `modules/memory/working.py`, `modules/memory/episodic.py`, `modules/memory/semantic.py`
**Critério de aceitação:** Working memory mantém 7±2 padrões; Episódica recupera padrão com 30% de ruído; Semântica busca por similaridade.

### SPEC-005 — Sistema de Atenção
**Objetivo:** DAN (top-down voluntário), VAN (bottom-up reflexivo), SaliencyMap.
**Dependências:** SPEC-001, SPEC-002
**Entregáveis:** `modules/attention/dan.py`, `modules/attention/van.py`, `modules/attention/saliency.py`
**Critério de aceitação:** DAN amplifica representações-alvo ≥2×; VAN interrompe processamento em <20ms simulados para input de alta saliência.

### SPEC-006 — Processamento Preditivo
**Objetivo:** Hierarquia preditiva de 3 níveis com erro bottom-up e predição top-down.
**Dependências:** SPEC-001, SPEC-004, SPEC-005
**Entregáveis:** `modules/predictive_coding/hierarchy.py`, `modules/predictive_coding/layer.py`
**Critério de aceitação:** Erro de predição diminui com treino; predição top-down modula representação sensorial.

### SPEC-007 — Sistema de Raciocínio
**Objetivo:** PFC Executive (inibição + planejamento), Model-Based RL, Model-Free RL, DecisionGate.
**Dependências:** SPEC-001, SPEC-004, SPEC-006
**Entregáveis:** `modules/reasoning/pfc.py`, `modules/reasoning/model_based.py`, `modules/reasoning/model_free.py`
**Critério de aceitação:** Model-free converge em bandit task; Model-based supera model-free em tarefa que exige planejamento.

### SPEC-008 — Neuromodulação
**Objetivo:** Dopamina (TD-error broadcast), Noradrenalina (arousal/threshold), Acetilcolina (atenção/plasticidade).
**Dependências:** SPEC-001, SPEC-002, SPEC-003
**Entregáveis:** `modules/neuromodulation/dopamine.py`, `modules/neuromodulation/noradrenaline.py`, `modules/neuromodulation/acetylcholine.py`
**Critério de aceitação:** Burst dopaminérgico aumenta LR globalmente; NA aumenta responsividade (threshold cai); ACh melhora sinal/ruído atencional.

### SPEC-009 — Visualização Neural (Three.js)
**Objetivo:** Servidor WebSocket + cena 3D Three.js com esferas por região, arcos sinápticos, spikes partícula.
**Dependências:** SPEC-002
**Entregáveis:** `visualization/server.py`, `visualization/static/brain_scene.js`, `visualization/static/index.html`
**Critério de aceitação:** Browser renderiza 8 regiões cerebrais em 3D; atualiza a 30fps com dados reais do engine; spike visível como flash.

### SPEC-010 — Dashboard Científico
**Objetivo:** Overlays com raster plots, firing rate, pesos sinápticos, TD-error em tempo real.
**Dependências:** SPEC-009
**Entregáveis:** `visualization/static/hud.js`, `visualization/static/charts.js`
**Critério de aceitação:** Raster plot atualiza em tempo real; firing rate por módulo visível; controles play/pause/step funcionam.

### SPEC-011 — Módulo de Linguagem (Claude API)
**Objetivo:** Integrar Claude API como módulo cognitivo de linguagem. Input: spike pattern semântico. Output: token sequence → spike encoding.
**Dependências:** SPEC-001, SPEC-002, SPEC-004
**Entregáveis:** `modules/language/claude_module.py`, `modules/language/encoder.py`
**Critério de aceitação:** Módulo recebe vetor semântico, gera resposta via API, retorna encoding de volta ao bus.

### SPEC-012 — Instrumentação + Logs + Replay
**Objetivo:** Sistema de observabilidade completo: logs estruturados, snapshots HDF5, replay de simulação.
**Dependências:** SPEC-002
**Entregáveis:** `core/instrumentation.py`, `core/replay.py`, formato HDF5 documentado
**Critério de aceitação:** Simulação de 10s pode ser salva e reproduzida identicamente; logs consultáveis por módulo/timestep.

### SPEC-013 — Testes e Validação Científica
**Objetivo:** Suite de testes que valida comportamentos cognitivos contra literatura (Brian2 como oracle).
**Dependências:** Todos os módulos
**Entregáveis:** `tests/scientific/`, `tests/integration/test_full_pipeline.py`, relatório de validação
**Critério de aceitação:** Firing rates dentro de ranges documentados; STDP converge conforme Bi & Poo 1998; TD-error replica Schultz 1997.

---

## 6. Organização das Sessões Claude Code

### Princípio Fundamental
**1 SPEC = 1 sessão Claude Code.**
Cada sessão começa lendo `specs/CONTEXT.md` e o SPEC correspondente. Termina atualizando `CONTEXT.md` com o que foi feito.

### Template de Início de Sessão

```
Leia specs/CONTEXT.md e specs/SPEC-00X-*.md antes de qualquer coisa.
Você é o engenheiro responsável pelo SPEC-00X.
Não implemente nada além do escopo do SPEC.
Ao terminar, atualize specs/CONTEXT.md com: o que foi feito, decisões tomadas, o que mudou.
```

### Template de Fim de Sessão

```
Antes de encerrar:
1. Todos os testes passam? (pytest tests/)
2. specs/CONTEXT.md está atualizado?
3. specs/DECISIONS.md tem novas entradas se houve decisões arquiteturais?
4. README.md reflete o status atual?
5. git commit com mensagem convencional
```

### Sessões por Fase

| Sessão | SPEC | Duração Estimada | Pré-requisito |
|--------|------|-----------------|---------------|
| S01 | SPEC-001 | 2–3h | — |
| S02 | SPEC-002 | 3–4h | S01 merged |
| S03 | SPEC-003 | 4–6h | S01 merged |
| S04 | SPEC-004 | 4–6h | S02, S03 merged |
| S05 | SPEC-005 | 3–4h | S02 merged |
| S06 | SPEC-006 | 4–5h | S04, S05 merged |
| S07 | SPEC-007 | 4–6h | S04, S06 merged |
| S08 | SPEC-008 | 3–4h | S02, S03 merged |
| S09 | SPEC-009 | 4–6h | S02 merged |
| S10 | SPEC-010 | 3–4h | S09 merged |
| S11 | SPEC-011 | 2–3h | S04 merged |
| S12 | SPEC-012 | 2–3h | S02 merged |
| S13 | SPEC-013 | 4–8h | Todos merged |

---

## 7. Arquitetura de Desenvolvimento

### Estrutura de Pastas

```
brain-simulator/
├── core/                        # Fundação — imutável após SPEC-001
│   ├── interfaces.py            # CognitiveModule ABC + dataclasses
│   ├── brain_bus.py             # Event broker
│   ├── simulation_engine.py     # TimeLoop + StateBuffer
│   ├── neuron.py                # LIF vetorizado
│   ├── synapse.py               # STDP
│   ├── learning_engine.py       # STDP + Hebb + TD
│   ├── neuromodulation.py       # Dopamina, NA, ACh
│   ├── instrumentation.py       # Logs + snapshots
│   └── replay.py                # Replay de simulação
│
├── modules/                     # Módulos cognitivos
│   ├── sensory/
│   │   └── sensory_module.py
│   ├── attention/
│   │   ├── dan.py               # Dorsal Attention Network
│   │   ├── van.py               # Ventral Attention Network
│   │   └── saliency.py
│   ├── memory/
│   │   ├── working.py
│   │   ├── episodic.py          # Hopfield
│   │   └── semantic.py          # Embeddings + grafo
│   ├── predictive_coding/
│   │   ├── layer.py             # Camada preditiva
│   │   └── hierarchy.py         # Hierarquia 3 níveis
│   ├── reasoning/
│   │   ├── pfc.py
│   │   ├── model_based.py
│   │   └── model_free.py
│   ├── neuromodulation/
│   │   ├── dopamine.py
│   │   ├── noradrenaline.py
│   │   └── acetylcholine.py
│   └── language/
│       ├── claude_module.py     # Claude API wrapper
│       └── encoder.py           # spike ↔ semantic
│
├── visualization/
│   ├── server.py                # FastAPI + WebSocket
│   └── static/
│       ├── index.html
│       ├── brain_scene.js       # Three.js cena principal
│       ├── neural_objects.js    # BrainRegion, SynapticArc, SpikeParticle
│       ├── hud.js               # Overlays e métricas
│       ├── charts.js            # Raster plots, firing rate
│       └── controls.js          # play/pause/step/speed
│
├── experiments/
│   ├── outputs/                 # HDF5 snapshots (gitignored)
│   ├── checkpoints/             # Pesos sinápticos (gitignored)
│   ├── logs/                    # JSONL (gitignored)
│   └── scenarios/               # Scripts de experimentos
│
├── tests/
│   ├── unit/                    # Por módulo, sem dependências
│   ├── integration/             # Pipeline completo
│   └── scientific/              # Validação contra literatura
│
├── specs/                       # Documentação do projeto
│   ├── BLUEPRINT.md             # Este documento
│   ├── CONTEXT.md               # Contexto vivo
│   ├── DECISIONS.md             # ADR log
│   └── SPEC-00X-*.md            # SPECs individuais
│
└── docs/                        # Documentação técnica adicional
```

---

## 8. Estratégia de Contexto

### 8.1 CONTEXT.md — Arquivo Vivo

`specs/CONTEXT.md` é o único arquivo que toda sessão Claude Code lê obrigatoriamente.
Contém: status atual, o que foi implementado, o que está em progresso, decisões recentes.

**Atualizado ao fim de cada sessão.**

### 8.2 DECISIONS.md — Registro de Decisões Arquiteturais (ADR)

Formato de cada entrada:
```markdown
## ADR-001 — [Título da Decisão]
**Data:** YYYY-MM-DD
**Status:** Aprovado | Supersedido | Em revisão
**Contexto:** Por que essa decisão foi necessária
**Decisão:** O que foi decidido
**Consequências:** O que muda
**Alternativas rejeitadas:** O que foi descartado e por quê
```

### 8.3 Outros Registros

| Arquivo | Propósito | Atualizado por |
|---------|-----------|----------------|
| `docs/hypotheses.md` | Hipóteses científicas a testar | Pesquisa + experimentos |
| `docs/experiments.md` | Log de experimentos realizados | Sessões de experimento |
| `docs/research.md` | Referências e notas de leitura | Sessões de pesquisa |
| `docs/dependencies.md` | Mapa de dependências externas | SPEC sessions |

---

## 9. Governança Técnica

### Nomeação

```
Arquivos Python:    snake_case.py
Classes:            PascalCase
Módulos cognitivos: [NomeFuncional]Module  (ex: HippocampusModule)
Interfaces:         [Nome]Base ou ABC      (ex: CognitiveModule)
Testes:             test_[arquivo].py
Experimentos:       YYYY-MM-DD_[descricao].py
```

### Commits (Conventional Commits)

```
feat(memory): implement Hopfield network pattern completion
fix(bus): correct timestep ordering in TopologicalSort
test(attention): add DAN amplification assertions
docs(spec): update SPEC-004 acceptance criteria
refactor(neuron): vectorize LIF update to NumPy batch
chore(deps): add brian2 to requirements.txt
```

### Branches

```
main          → código aprovado, sempre funcional
feat/spec-XXX → desenvolvimento de cada SPEC
fix/[issue]   → correções pontuais
exp/[nome]    → experimentos (nunca mergeia em main)
```

### Worktrees (para sessões paralelas)

```bash
# Quando trabalhar em SPEC-004 e SPEC-005 ao mesmo tempo:
git worktree add ../brain-sim-memory feat/spec-004
git worktree add ../brain-sim-attention feat/spec-005
```

### Pull Requests

Todo PR de SPEC deve conter:
- [ ] Todos os testes passam (`pytest tests/`)
- [ ] `specs/CONTEXT.md` atualizado
- [ ] `specs/DECISIONS.md` atualizado se houve decisão arquitetural
- [ ] Nenhum TODO não documentado no código
- [ ] Compatibilidade com `CognitiveModule` interface verificada

---

## 10. Estratégia de Qualidade

### Pirâmide de Testes

```
         /\
        /  \   Testes Científicos (13)
       /----\  Valida comportamentos contra literatura
      /      \ (Brian2 como oracle)
     /--------\
    /          \ Testes de Integração (30–50)
   /  Pipeline  \ Engine completo com módulos reais
  /--------------\
 /                \ Testes Unitários (100+)
/   Por módulo     \ Sem dependências externas
\------------------/
```

### Testes Científicos — Validações Obrigatórias

| Teste | Referência | Critério |
|-------|-----------|---------|
| LIF firing rate | Adrian 1926 | 10–100 Hz para I fisiológico |
| STDP convergência | Bi & Poo 1998 | Δw(Δt) segue curva assimétrica |
| Hopfield capacidade | Hopfield 1982 | ≥0.14N padrões sem erro |
| TD-error encoding | Schultz 1997 | Burst dopaminérgico → recompensa inesperada |
| Working Memory | Compte 2000 | Atividade persistente pós-stimulus |
| Pattern separation | O'Reilly & McClelland | Padrões 70% similares → representações ortogonais |

### Testes de Performance

```python
# Benchmark mínimo aceitável (Acer Aspire 3):
assert simulate_100ms(n_neurons=2000) < 5.0  # segundos de wall clock
assert visualizer_fps() >= 25                 # frames por segundo
assert memory_usage_mb() < 4096              # 4 GB RAM máximo
```

---

## 11. Plano de Visualização 3D

### Arquitetura Visual

```
Python SimulationEngine
    │
    │ WebSocket (localhost:8765)
    │ JSON: {timestamp, modules: [{id, firing_rate[], voltage[]}]}
    ▼
Three.js BrainScene (browser)
    │
    ├── BrainRegionMesh      → esfera por módulo
    │   ├── cor              → firing rate (azul→vermelho)
    │   ├── tamanho          → n_neurons
    │   └── posição          → anatomia aproximada
    │
    ├── SynapticArc          → curva entre regiões
    │   ├── espessura        → força sináptica média
    │   └── cor              → tipo (excitatório=verde / inibitório=vermelho)
    │
    ├── SpikeParticle        → flash saindo da região
    │   └── disparado        → quando firing_rate > threshold
    │
    └── DopamineHalo         → anel de luz global
        └── intensidade      → nível de dopamina
```

### Anatomia 3D das Regiões (posições Three.js)

```javascript
const BRAIN_REGIONS = {
  sensory:          { pos: [0, -1, 2],   color: 0x4fc3f7, radius: 0.6 },
  attention_dan:    { pos: [1.5, 1, 1],  color: 0xab47bc, radius: 0.5 },
  attention_van:    { pos: [-1.5, 1, 1], color: 0x7e57c2, radius: 0.5 },
  working_memory:   { pos: [0, 2, 0],    color: 0x26a69a, radius: 0.7 },
  episodic_memory:  { pos: [1, 0, -1],   color: 0x42a5f5, radius: 0.6 },
  semantic_memory:  { pos: [-1, 0, -1],  color: 0x5c6bc0, radius: 0.6 },
  pfc:              { pos: [0, 3, 0],    color: 0xef5350, radius: 0.8 },
  amygdala:         { pos: [1, -1, 0],   color: 0xff7043, radius: 0.4 },
};
```

### Controles de Simulação

| Controle | Ação |
|---------|------|
| ▶ Play | Inicia simulação contínua |
| ⏸ Pause | Para o clock |
| ▶▶ Step | Avança 1 timestep |
| ⏩ ×10 | Acelera simulação 10× |
| 🔍 Isolar | Zoom em módulo + silencia outros |
| 📊 Raster | Abre raster plot do módulo selecionado |
| ⏮ Replay | Reproduz últimos 10s |

---

## 12. Matriz de Uso dos Modelos de IA

> **Nota sobre Fable 5:** Não corresponde a um modelo Anthropic atual. Os modelos disponíveis são Opus 4.8, Sonnet 4.6 e Haiku 4.5. Fable 5 foi removido da matriz — não há caso de uso identificado para modelos de storytelling/roleplay num projeto de engenharia científica.

| Atividade | Sonnet 4.6 | Opus 4.8 | Haiku 4.5 | Recomendação |
|-----------|-----------|---------|----------|-------------|
| Design de interfaces / ABC | ⚠️ Risco de simplificar | ✅ Ideal | ❌ | **Opus 4.8** |
| Decisões arquiteturais | ⚠️ | ✅ Raciocínio profundo | ❌ | **Opus 4.8** |
| Pesquisa científica / validação | ✅ | ✅ Preferido | ❌ | **Opus 4.8** |
| Implementação de módulos SNN | ✅ Ideal | ✅ Excessivo | ❌ | **Sonnet 4.6** |
| Three.js / visualização | ✅ Ideal | ✅ Excessivo | ❌ | **Sonnet 4.6** |
| Testes unitários | ✅ Ideal | ✅ Excessivo | ✅ Simples | **Sonnet 4.6** |
| Documentação técnica | ✅ Ideal | ✅ | ✅ Rascunhos | **Sonnet 4.6** |
| Debugging / refatoração | ✅ Ideal | ✅ | ❌ Limite de contexto | **Sonnet 4.6** |
| Auditoria de código | ✅ | ✅ Preferido | ❌ | **Opus 4.8** |
| Experimentos e hipóteses | ✅ | ✅ Preferido | ❌ | **Opus 4.8** |
| Boilerplate / CRUD | ✅ | ❌ Desperdício | ✅ Ideal | **Haiku 4.5** |
| SPECs + prompts rápidos | ✅ Ideal | ✅ | ✅ | **Sonnet 4.6** |

### Quando trocar para Opus 4.8
- A interface `CognitiveModule` está sendo alterada
- Uma decisão arquitetural tem consequências em mais de 2 módulos
- Validação científica de comportamento emergente
- Raciocínio sobre papers com múltiplas variáveis

### Quando usar Haiku 4.5
- Geração de boilerplate (`__init__.py`, stubs, `dataclass` simples)
- Formatação de documentação
- Queries curtas sem complexidade técnica

---

## 13. Roadmap de Execução

### Fase 0 — Fundação (concluída)
- [x] Base científica (82 fontes)
- [x] Decisões arquiteturais
- [x] Blueprint aprovado
- [x] Repositório inicializado

### Fase 1 — Core (SPEC-001, 002, 003)
**Meta:** Engine funcional com 3 módulos mock simulando 1 segundo biológico
- SPEC-001: Interfaces + contratos
- SPEC-002: BrainBus + SimulationEngine
- SPEC-003: LIF + STDP + Learning
**Critério:** `python -m experiments.scenarios.basic_sim` roda 1s sem erro

### Fase 2 — Memória + Atenção (SPEC-004, 005, 008)
**Meta:** Hipocampo e PFC simulando working memory + atenção modulada por dopamina
- SPEC-004: WorkingMemory + Hopfield
- SPEC-005: DAN + VAN + SaliencyMap
- SPEC-008: Neuromodulação
**Critério:** Pattern completion funciona; atenção amplifica sinal-alvo

### Fase 3 — Processamento Preditivo + Raciocínio (SPEC-006, 007)
**Meta:** Hierarquia preditiva com erro de predição reduzindo com treino; RL dual funcional
- SPEC-006: PredictiveCodingHierarchy
- SPEC-007: PFC + Model-Based/Free RL
**Critério:** TD-error replica curva de Schultz 1997

### Fase 4 — Visualização (SPEC-009, 010, 012)
**Meta:** Browser mostra 8 regiões cerebrais em 3D com spikes visíveis em tempo real
- SPEC-009: Three.js + WebSocket
- SPEC-010: Dashboard + controles
- SPEC-012: Instrumentação + Replay
**Critério:** 30fps estável; controles funcionam; replay reproduz simulação

### Fase 5 — Linguagem + Validação (SPEC-011, 013)
**Meta:** Claude API integrado como módulo cognitivo; suite de validação científica completa
- SPEC-011: Claude API module
- SPEC-013: Validação científica (Brian2 oracle)
**Critério:** Todos os testes científicos passam; módulo de linguagem comunica via BrainBus

### Fase 6 — Experimentos e Evolução
- Experimentos com cenários cognitivos documentados
- Preparação para SNN de maior escala (cloud/GPU dedicada)
- Publicação de resultados / documentação científica

---

## 14. Riscos e Mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Performance insuficiente em CPU | Alta | Alto | Populações pequenas (500-2k); profile antes de otimizar |
| Divergência científica dos módulos | Média | Alto | Brian2 como oracle em SPEC-013 desde o início |
| Interface `CognitiveModule` mudando após SPEC-001 | Média | Crítico | Opus 4.8 para design; congelar após aprovação |
| Three.js latência alta com muitos dados | Média | Médio | Throttle do StateRenderer (não bloqueia clock) |
| Claude API rate limits no módulo de linguagem | Baixa | Médio | Cache de respostas; mock para testes |
| Scope creep (adicionar módulos prematuramente) | Alta | Médio | Auditoria de escopo antes de cada SPEC |
| Perda de contexto entre sessões Claude Code | Alta | Alto | CONTEXT.md obrigatório; protocolo de início de sessão |

---

*Blueprint gerado em: 2026-06-10*
*Projeto: Brain Simulator | Versão: 1.0*
*Próxima revisão: após conclusão da Fase 1*
