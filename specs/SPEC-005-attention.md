# SPEC-005 — Sistema de Atenção

**Status:** ⏳ | **Modelo:** Sonnet 4.6 | **Depende de:** SPEC-001, SPEC-002

## Objetivo
DAN (top-down voluntário), VAN (bottom-up reflexivo), SaliencyMap para priorização de inputs.

## Entregáveis
- `modules/attention/dan.py` — amplifica representações-alvo via sinal PFC top-down
- `modules/attention/van.py` — interrupção reflexiva por alta saliência
- `modules/attention/saliency.py` — mapa de saliência computacional

## Critérios de Aceitação
- [ ] DAN amplifica representação-alvo ≥ 2× vs. distratores
- [ ] VAN interrompe processamento em < 20ms simulados para alta saliência
- [ ] Anticorrelação DAN-VAN implementada (quando um ativa, outro suprime)

## Prompt para Claude Code
```
Leia specs/CONTEXT.md e specs/SPEC-005-attention.md.
Implemente DAN, VAN e SaliencyMap. Todos implementam CognitiveModule ABC.
DAN recebe sinal do PFC (top-down) e modula ganho do módulo sensorial.
VAN responde a eventos de alta saliência e pode interromper o processamento atual.
```
