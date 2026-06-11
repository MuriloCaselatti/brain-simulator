# SPEC-004 — Sistema de Memória

**Status:** ⏳ | **Modelo:** Sonnet 4.6 | **Depende de:** SPEC-001, SPEC-003

## Objetivo
WorkingMemory (rede recorrente de atratores), EpisodicMemory (Hopfield modernizado), SemanticMemory (embeddings + grafo).

## Entregáveis
- `modules/memory/working.py` — ~7 atratores, atividade persistente pós-stimulus
- `modules/memory/episodic.py` — Modern Hopfield Network (Ramsauer 2020)
- `modules/memory/semantic.py` — sentence-transformers + NetworkX

## Critérios de Aceitação
- [ ] WorkingMemory: mantém padrão por 500ms sem input
- [ ] EpisodicMemory: recupera padrão com 30% de ruído
- [ ] SemanticMemory: busca por similaridade retorna top-5 corretos
- [ ] Todos implementam `CognitiveModule` ABC

## Pesquisa Pré-Implementação
Estudar: Ramsauer et al. 2020 "Hopfield Networks is All You Need"

## Prompt para Claude Code
```
Leia specs/CONTEXT.md e specs/SPEC-004-memory.md.
Implemente os 3 módulos de memória. TODOS implementam CognitiveModule ABC.
EpisodicMemory usa Modern Hopfield Network (não o clássico de 1982).
Ao terminar: pytest tests/unit/test_memory.py + atualizar CONTEXT.md.
```
