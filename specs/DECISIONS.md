# Brain Simulator — Registro de Decisões Arquiteturais (ADR)

---

## ADR-001 — Runtime SNN: Brian2 em vez de SpykeTorch
**Data:** 2026-06-10
**Status:** Aprovado

**Contexto:** O hardware disponível (Acer Aspire 3, GPU integrada) não suporta CUDA. SpykeTorch é GPU-first. Brian2 é otimizado para CPU via geração de código C++.

**Decisão:** Brian2 como runtime SNN principal. PyTorch (CPU) para camadas de embeddings semânticos.

**Consequências:** Populações limitadas a 500–2.000 neurônios por módulo. Experimentos de grande escala exigirão cloud.

**Alternativas rejeitadas:**
- SpykeTorch: exige CUDA
- NEST: difícil de integrar com stack Python/ML
- Implementação custom: manutenção excessiva para projeto solo

---

## ADR-002 — Arquitetura Core Modular com Abstraction Layer
**Data:** 2026-06-10
**Status:** Aprovado

**Contexto:** Três opções avaliadas: Monolítico SNN, Microserviços, Core Modular.

**Decisão:** Core Modular com `CognitiveModule` ABC. Cada módulo implementa a interface; BrainBus conecta todos de forma síncrona.

**Consequências:** Interface deve ser projetada com cuidado (Opus 4.8) e congelada após SPEC-001. Módulos são substituíveis sem quebrar o sistema.

**Alternativas rejeitadas:**
- Monolítico: difícil de desenvolver com Claude Code sessão a sessão
- Microserviços: latência artificial, over-engineering para fase inicial

---

## ADR-003 — BrainBus Síncrono (dt = 1ms)
**Data:** 2026-06-10
**Status:** Aprovado

**Contexto:** A alternativa assíncrona eliminaria bloqueios mas quebraria a causalidade biológica.

**Decisão:** BrainBus síncrono. Todos os módulos avançam no mesmo timestep. dt = 1ms (biológico).

**Consequências:** Módulos lentos bloqueiam o clock. Mitigação: StateRenderer é assíncrono (não bloqueia o clock).

---

## ADR-004 — Visualização via Browser (Three.js/WebGL)
**Data:** 2026-06-10
**Status:** Aprovado

**Contexto:** Alternativas avaliadas: Blender Python API, Unity, Godot, Three.js.

**Decisão:** Three.js no browser via WebSocket. GPU integrada é suficiente para renderização WebGL.

**Consequências:** Fidelidade gráfica menor que Unity/Unreal, mas iteração muito mais rápida. Sem instalação de engine necessária.

---

## ADR-005 — Linguagem via Claude API (módulo externo)
**Data:** 2026-06-10
**Status:** Aprovado

**Contexto:** LLM local exigiria ~8GB RAM e GPU dedicada — inviável no hardware disponível.

**Decisão:** Claude API como módulo de linguagem externo. Input: vetor semântico. Output: resposta → encoding de volta ao BrainBus.

**Consequências:** Dependência de conectividade e custos de API. Cache de respostas implementado para mitigar.

---

## ADR-006 — Fidelidade Biológica: LIF + STDP (não Hodgkin-Huxley)
**Data:** 2026-06-10
**Status:** Aprovado

**Contexto:** HH é biofisicamente mais preciso mas computacionalmente inviável em CPU para populações úteis.

**Decisão:** LIF (Leaky Integrate-and-Fire) com STDP. Arquitetura projetada para substituição futura por HH quando o hardware permitir.

**Consequências:** Menor fidelidade biofísica, mas comportamentos emergentes (completamento de padrões, RL, working memory) são plenamente demonstráveis em LIF. Isso é academicamente válido.

---

## ADR-007 — Modelos de IA: Opus 4.8 para arquitetura, Sonnet 4.6 para implementação
**Data:** 2026-06-10
**Status:** Aprovado

**Contexto:** Fable 5 não corresponde a modelo Anthropic disponível. Modelos reais: Opus 4.8, Sonnet 4.6, Haiku 4.5.

**Decisão:** Opus 4.8 para decisões arquiteturais e pesquisa científica. Sonnet 4.6 para implementação, testes e documentação. Haiku 4.5 para boilerplate.

---

## ADR-008 — Congelamento da Interface `CognitiveModule` (v1.0.0)
**Data:** 2026-06-11
**Status:** Aprovado

**Contexto:** SPEC-001 entrega o contrato central (`core/interfaces.py`) do qual
todos os SPECs subsequentes (002–013) dependem. A interface foi projetada com
Opus 4.8 conforme exigido pela matriz de modelos e pelo risco "Interface mudando
após SPEC-001 = Crítico".

**Decisão:** Congelar a superfície pública de `core/interfaces.py` na
`INTERFACE_VERSION = "1.0.0"`: nomes/tipos de campos de todos os dataclasses
(`ModuleInputs`, `ModuleOutputs`, `ModuleState`, `NeuromodulationSignal`,
`SynapticTarget`) e as assinaturas dos 5 métodos abstratos de `CognitiveModule`
(`update`, `get_state`, `apply_neuromodulation`, `get_synaptic_targets`,
`reset`). Restrição de import mantida: apenas stdlib + numpy.

**Consequências:** Qualquer alteração futura na interface exige nova ADR que
supersede esta e revisão com Opus 4.8, e bump de `INTERFACE_VERSION`. Adições de
campos com default são toleráveis (compatibilidade retroativa); remoções ou
mudanças de assinatura são breaking e exigem migração de todos os módulos.

**Notas de implementação:**
- `core/brain_bus.py` permanece stub (métodos → `NotImplementedError` apontando
  SPEC-002); `BusEvent`/`BusSnapshot` serão definidos no SPEC-002, fora deste
  contrato congelado.
- Validação numérica (shapes/ranges) foi deliberadamente deixada de fora dos
  dataclasses para mantê-los como contratos de dados puros (sem lógica).

**Alternativas rejeitadas:**
- Adicionar validação em `__post_init__`: introduz lógica no contrato, fora do
  escopo do SPEC-001.
- Métodos abstratos adicionais (ex.: `connect`, `save_state`): risco de
  over-specification antes de haver módulos concretos que os justifiquem.

---

*Novas ADRs são adicionadas aqui conforme surgem durante o desenvolvimento.*
*Formato: ADR-NNN — [Título] | Data | Status*
