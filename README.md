# Brain Simulator

> Arquitetura cognitiva computacional inspirada no cérebro humano.
> Motor SNN (Spiking Neural Networks) com visualização 3D em tempo real.

## Status
🔴 **Fase 0 — Fundação** | Blueprint aprovado | Implementação não iniciada

## Arquitetura
- **Engine:** Brian2 SNN (LIF + STDP) — CPU-first
- **Módulos:** 8 camadas cognitivas com interface abstrata (`CognitiveModule`)
- **Comunicação:** BrainBus síncrono por timestep (dt = 1ms)
- **Visualização:** Three.js/WebGL via WebSocket
- **Linguagem:** Claude API (módulo externo)

## Documentação
- [`specs/BLUEPRINT.md`](specs/BLUEPRINT.md) — Documento mestre
- [`specs/CONTEXT.md`](specs/CONTEXT.md) — Contexto vivo para sessões Claude Code
- [`specs/DECISIONS.md`](specs/DECISIONS.md) — Registro de decisões arquiteturais
- `specs/SPEC-00X-*.md` — Especificações por módulo

## Início Rápido
```bash
pip install brian2 numpy torch fastapi websockets
python -m pytest tests/
```

## Roadmap
| Fase | Descrição | Status |
|------|-----------|--------|
| 0 | Pesquisa + Blueprint | ✅ Completo |
| 1 | SPEC-001: Core + Interfaces | 🔜 Próxima |
| 2 | SPEC-002/003: BrainBus + SNN | ⏳ |
| 3 | SPEC-004/005: Memória + Atenção | ⏳ |
| 4 | SPEC-006/007: Preditivo + Raciocínio | ⏳ |
| 5 | SPEC-008: Neuromodulação | ⏳ |
| 6 | SPEC-009/010: Visualização 3D | ⏳ |
| 7 | SPEC-011/012/013: Linguagem + Testes | ⏳ |
