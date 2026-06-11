# SPEC-011 — Módulo de Linguagem (Claude API)

**Status:** ⏳ | **Modelo:** Sonnet 4.6 | **Depende de:** SPEC-001, SPEC-004

## Objetivo
Integrar Claude API como módulo cognitivo de linguagem. Bidirecional: spike patterns → linguagem → spike encoding.

## Entregáveis
- `modules/language/claude_module.py` — CognitiveModule que chama Claude API
- `modules/language/encoder.py` — conversão vetor semântico ↔ spike pattern

## Critérios de Aceitação
- [ ] ClaudeModule implementa CognitiveModule ABC
- [ ] Recebe vetor semântico da SemanticMemory, envia para API, retorna encoding
- [ ] Cache de respostas evita calls repetidas
- [ ] Mock disponível para testes sem API key

## Prompt para Claude Code
```
Leia specs/CONTEXT.md e specs/SPEC-011-language.md.
ClaudeModule é um CognitiveModule que, quando ativado, converte o estado semântico
atual em prompt, chama Claude API (model="claude-sonnet-4-6"), e converte a resposta
de volta em spike encoding para o BrainBus.
Implemente um mock que não exige API key para testes.
```
