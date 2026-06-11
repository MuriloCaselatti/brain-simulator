# SPEC-006 — Processamento Preditivo

**Status:** ⏳ | **Modelo:** Opus 4.8 (design) + Sonnet 4.6 (impl) | **Depende de:** SPEC-004, SPEC-005

## Objetivo
Hierarquia preditiva de 3 níveis: erro de predição bottom-up, predição top-down, precisão modulada por atenção.

## Base Científica
Rao & Ballard 1999 (Predictive Coding in the Visual Cortex)
Friston 2010 (Free Energy Principle)

## Entregáveis
- `modules/predictive_coding/layer.py` — camada individual com neurônios de predição + erro
- `modules/predictive_coding/hierarchy.py` — hierarquia de 3 níveis conectados

## Critérios de Aceitação
- [ ] Erro de predição diminui com treinamento repetido do mesmo estímulo
- [ ] Predição top-down modula representação na camada inferior
- [ ] Precisão (attention) escala o peso do erro

## Prompt para Claude Code
```
Leia specs/CONTEXT.md e specs/SPEC-006-predictive-coding.md.
Use Opus 4.8 para confirmar o design matemático da hierarquia antes de implementar.
Cada camada tem: neurônios de predição (geram predição para camada inferior)
e neurônios de erro (calculam diferença entre predição e input real).
```
