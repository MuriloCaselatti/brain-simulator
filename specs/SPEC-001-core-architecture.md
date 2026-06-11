# SPEC-001 — Arquitetura Base + Interfaces

**Status:** 🔜 Próxima | **Modelo recomendado:** Opus 4.8
**Branch:** `feat/spec-001` | **Depende de:** Nenhuma

---

## Objetivo
Criar o esqueleto imutável do projeto: tipos, contratos, interfaces abstratas e estrutura de pastas. Tudo que é implementado depois depende deste SPEC.

## Escopo
- `core/interfaces.py` — CognitiveModule ABC + todos os dataclasses
- `core/__init__.py`
- `modules/*/__init__.py` — stubs de cada módulo
- `tests/unit/test_interfaces.py` — testes de contrato
- `requirements.txt`

**Fora do escopo:** qualquer implementação real de módulo cognitivo.

## Entradas
- Blueprint aprovado (`specs/BLUEPRINT.md`)
- Decisões arquiteturais (`specs/DECISIONS.md`)

## Entregáveis
1. `core/interfaces.py` com `CognitiveModule`, `ModuleInputs`, `ModuleOutputs`, `ModuleState`, `NeuromodulationSignal`, `SynapticTarget`
2. `core/brain_bus.py` **stub apenas** (classe vazia com métodos `pass`)
3. `requirements.txt` com: `brian2`, `numpy`, `torch`, `fastapi`, `websockets`, `networkx`, `pytest`
4. `tests/unit/test_interfaces.py` com mock de `CognitiveModule` que implementa todos os métodos abstratos e valida contrato

## Arquitetura

```python
# Estrutura exata de core/interfaces.py:
@dataclass class ModuleInputs
@dataclass class ModuleOutputs
@dataclass class ModuleState
@dataclass class NeuromodulationSignal
@dataclass class SynapticTarget
class CognitiveModule(ABC):
    module_id: str
    n_neurons: int
    def update(self, dt, inputs) -> ModuleOutputs: ...
    def get_state(self) -> ModuleState: ...
    def apply_neuromodulation(self, signal) -> None: ...
    def get_synaptic_targets(self) -> List[SynapticTarget]: ...
    def reset(self) -> None: ...
```

## Regras
- **CRÍTICO:** Esta interface não pode ser alterada após aprovação sem ADR e Opus 4.8
- Todos os campos de dataclass têm type hints explícitos
- Nenhum import de Brian2 ou PyTorch neste arquivo (só stdlib + numpy)
- Sem implementação concreta neste SPEC

## Testes
```python
def test_mock_module_implements_contract():
    module = MockCognitiveModule("test", n_neurons=100)
    inputs = ModuleInputs(...)
    outputs = module.update(dt=1.0, inputs=inputs)
    assert isinstance(outputs, ModuleOutputs)
    state = module.get_state()
    assert isinstance(state, ModuleState)
    assert state.n_neurons == 100
```

## Critérios de Aceitação
- [ ] `from core.interfaces import CognitiveModule` importa sem erro
- [ ] Mock module passa todos os testes de contrato
- [ ] `pytest tests/unit/test_interfaces.py` → 100% pass
- [ ] Nenhum TODO não documentado
- [ ] `specs/CONTEXT.md` atualizado

## Prompt para Claude Code

```
Você é Principal Software Architect do projeto Brain Simulator.

Leia specs/CONTEXT.md e specs/SPEC-001-core-architecture.md antes de qualquer ação.

Sua missão é implementar SPEC-001: as interfaces abstratas e contratos do projeto.
A interface CognitiveModule é a fundação de tudo — será congelada após aprovação.

Regras obrigatórias:
- Siga exatamente a estrutura definida no SPEC
- Nenhum import de Brian2 ou PyTorch em core/interfaces.py
- Type hints em tudo
- Docstrings em inglês técnico
- Testes de contrato com mock module

Ao terminar:
1. pytest tests/unit/test_interfaces.py deve passar 100%
2. Atualize specs/CONTEXT.md com o que foi feito
3. git commit -m "feat(core): implement CognitiveModule interface and contracts"
```
