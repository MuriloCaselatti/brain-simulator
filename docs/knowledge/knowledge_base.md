# Brain Simulator Knowledge Base

## Base de Conhecimento em Neurociência para o Projeto Brain Simulator

**Versão:** 1.0 | **Data:** Junho 2026 | **Fonte:** NotebookLM "Neuroscience Study" (82 fontes)

---

## Resumo Executivo

Esta base de conhecimento sintetiza o conteúdo completo do projeto "Neuroscience Study" no Google NotebookLM, consolidando 82 fontes entre artigos científicos, PDFs, notas de pesquisa e materiais técnicos de neurociência. O objetivo é servir como fundação intelectual para o desenvolvimento do **Brain Simulator** — um simulador cognitivo computacional inspirado no funcionamento do cérebro humano.

O documento cobre 13 domínios principais: Fundamentos Biológicos, Cognição, Memória, Aprendizagem, Atenção, Linguagem, Emoções, Consciência, Tomada de Decisão, Neuroplasticidade, Processamento Preditivo, Redes Neurais Biológicas e Neurociência Computacional. Para cada domínio, são fornecidos conceitos fundamentais, mecanismos biológicos, teorias relevantes e **traduções diretas para arquitetura computacional/IA**.

### Principais Contribuições para o Brain Simulator

1. **Arquitetura Hierárquica com Processamento Preditivo** — o cérebro não processa passivamente, ele prediz. O Brain Simulator deve implementar fluxos descendentes (predição) e ascendentes (erro).  
2. **Plasticidade Sináptica via STDP** — aprendizado baseado em timing de spikes. Implementável como regras de atualização de pesos com janela temporal.  
3. **Memória Distribuída e Associativa** — padrão Hopfield: memória como atrator dinâmico. Completamento de padrões a partir de inputs parciais.  
4. **Módulos Especializados Interconectados** — CNN (visão), RNN (motor/temporal), Transformer (linguagem/contexto) conectados por "vias de substância branca" (pipelines de dados).  
5. **Aprendizado por Reforço com Dopamina** — sinais globais de recompensa modulando plasticidade de todas as sinapses ativas simultaneamente.

---

## Visão Geral da Neurociência Estudada

### Escopo do Projeto "Neuroscience Study"

O projeto cobre neurociência em amplitude e profundidade equivalentes a um currículo de pós-graduação. As 82 fontes abordam:

- **Neurobiologia molecular** — canais iônicos, neurotransmissores, receptores, sinalização intracelular  
- **Neuroanatomia sistêmica** — SNC/SNP, tronco encefálico, cerebelo, diencéfalo, telencéfalo  
- **Neurofisiologia** — potenciais de ação, transmissão sináptica, oscilações neurais  
- **Neurociência cognitiva** — memória, atenção, linguagem, emoções, tomada de decisão  
- **Neurociência computacional** — modelos formais do neurônio, redes de memória associativa, RL  
- **Neuroplasticidade** — LTP/LTD, STDP, reorganização cortical, neurogênese  
- **Neurologia clínica** — epilepsia, Alzheimer, Parkinson, TDAH, autismo, esquizofrenia  
- **Métodos de pesquisa** — fMRI, EEG, PET, optogenética, patch-clamp

### Organização Conceptual

NEUROCIÊNCIA

├── BIOLÓGICA (substrato físico)

│   ├── Molecular (íons, proteínas, genes)

│   ├── Celular (neurônios, glia)

│   └── Sistêmica (circuitos, regiões)

│

├── COGNITIVA (funções emergentes)

│   ├── Percepção e Atenção

│   ├── Memória e Aprendizagem

│   ├── Linguagem

│   ├── Emoções

│   ├── Tomada de Decisão

│   └── Consciência

│

└── COMPUTACIONAL (modelos formais)

    ├── Modelos de Neurônio

    ├── Modelos de Circuito

    └── Modelos de Cognição

---

## Mapa Conceitual Global

\[MUNDO EXTERNO\]

      |

      | (inputs sensoriais)

      v

\[SISTEMAS SENSORIAIS\] \--\> transducao \--\> representacao neural

      |

      | (processamento hierárquico)

      v

\[CÓRTEX SENSORIAL PRIMÁRIO\] \<--\> \[CÓRTEX ASSOCIATIVO\]

      |                                    |

      |                                    | (predicao/erro)

      v                                    v

\[ATENÇÃO\] \--\> seleciona \--\> \[MEMÓRIA DE TRABALHO\]

      |                          |

      |                          | (consolidacao)

      v                          v

\[HIPOCAMPO\] \<--\> \[MEMÓRIA DE LONGO PRAZO\]

      |

      | (contexto emocional)

      v

\[AMÍGDALA\] \<--\> \[SISTEMA LÍMBICO\]

      |

      | (avaliacao)

      v

\[CÓRTEX PRÉ-FRONTAL\] \--\> planeja \--\> \[TOMADA DE DECISÃO\]

      |

      | (acao)

      v

\[GÂNGLIOS DA BASE\] \--\> selecao \--\> \[CÓRTEX MOTOR\]

      |

      v

\[AÇÃO NO MUNDO\]

      |

      | (feedback/recompensa)

      v

\[DOPAMINA/REFORÇO\] \--\> modula \--\> \[PLASTICIDADE SINÁPTICA\]

---

## 1\. Fundamentos Biológicos

### 1.1 O Neurônio — Unidade Computacional Básica

#### Morfologia e Componentes

O neurônio é a célula nervosa especializada em processar e transmitir informação. Sua estrutura inclui:

- **Corpo celular (soma)**: contém núcleo com DNA e maquinaria metabólica; integra sinais de entrada  
- **Dendritos**: ramificações que recebem inputs de outros neurônios; espinhas dendríticas ampliam superfície de contato  
- **Axônio**: fibra de saída única; conduz potencial de ação; pode ter mielina para aumentar velocidade  
- **Terminais axônicos (botões sinápticos)**: liberam neurotransmissores na fenda sináptica

#### Eletrofisiologia — O Potencial de Ação

O potencial de ação é o mecanismo de disparo neural, com fases precisas:

| Fase | Evento Molecular | Voltagem Típica |
| :---- | :---- | :---- |
| Repouso | Canais K+ abertos, Na+ fechados | \-70 mV |
| Despolarização | Canais Na+ abrem em cascata | \+40 mV |
| Repolarização | Canais Na+ inativam, K+ abrem | volta a \-70 mV |
| Hiperpolarização | K+ tardam a fechar | abaixo de \-70 mV |
| Período refratário | Inativação absoluta → relativa | recuperação |

**Lei do Tudo ou Nada**: o potencial de ação tem amplitude constante; a intensidade de um sinal é codificada na **frequência** de disparos (código de taxa) ou no **padrão temporal** dos spikes.

#### Potenciais Pós-Sinápticos (PEPS/PIPS)

- **PEPS**: glutamato → despolarização local; empurra membrana em direção ao limiar  
- **PIPS**: GABA/glicina → hiperpolarização; afasta do limiar  
- **Integração**: soma espacial \+ soma temporal; se soma ultrapassar limiar (\~-55 mV), gera spike

**Relevância para o Brain Simulator**: cada neurônio artificial deve manter estado interno acumulando PEPS/PIPS; disparar quando estado ultrapassa limiar; resetar após disparo com período refratário opcional.

### 1.2 Neurotransmissores — Mensageiros Químicos

| Neurotransmissor | Tipo | Receptor Principal | Função Principal |
| :---- | :---- | :---- | :---- |
| Glutamato | Excitatório | AMPA, NMDA, mGluR | Transmissão rápida, LTP |
| GABA | Inibitório | GABA-A, GABA-B | Inibição, sincronização |
| Dopamina | Modulador | D1-D5 | Recompensa, motivação, saliência |
| Serotonina | Modulador | 5-HT1-7 | Humor, sono, apetite |
| Noradrenalina | Modulador | alpha, beta | Alerta, atenção, memória |
| Acetilcolina | Excitatório/Mod | nAChR, mAChR | Atenção, memória, movimento |

#### O Sistema Dopaminérgico — Sinal de Erro de Predição de Recompensa

A dopamina é o neurotransmissor mais crítico para o Brain Simulator:

- **VTA (Área Tegmental Ventral)**: principal origem de neurônios dopaminérgicos  
- **Núcleo Accumbens**: recebe projeções do VTA; crítico para motivação e vício  
- **Estriado**: recebe dopamina para seleção de ações nos gânglios da base  
- **PFC**: modulação dopaminérgica de memória de trabalho

**Regra de Erro de Predição Dopaminérgica** (Schultz et al., 1997):

- Recompensa ocorre como esperado → atividade basal (sem mudança)  
- Recompensa excede expectativa → burst dopaminérgico (sinal positivo)  
- Recompensa esperada não ocorre → silêncio dopaminérgico (sinal negativo)

**Aplicação Brain Simulator**: o módulo dopaminérgico é um sinal de modulação global que escala a taxa de aprendizado de todas as sinapses ativas em função do erro de predição de recompensa.

### 1.3 Neuroanatomia Sistêmica

#### Sistema Nervoso Central — Hierarquia Estrutural

ENCÉFALO

├── TELENCÉFALO (mais recente evolutivamente)

│   ├── Córtex Cerebral (neocórtex, 6 camadas)

│   │   ├── Lobo Frontal: planejamento, controle motor, funções executivas

│   │   ├── Lobo Parietal: integração somatossensorial, atenção espacial

│   │   ├── Lobo Temporal: audição, linguagem, memória

│   │   └── Lobo Occipital: visão

│   ├── Gânglios da Base: seleção de ação, aprendizado por reforço

│   └── Sistema Límbico: emoções, memória (hipocampo, amígdala)

│

├── DIENCÉFALO

│   ├── Tálamo: gateway sensorial, modulação atenção

│   └── Hipotálamo: homeostase, motivações primárias

│

├── MESENCÉFALO

│   ├── VTA: dopamina/recompensa

│   └── Colículos: reflexos visuais/auditivos

│

├── METENCÉFALO

│   ├── Ponte: relé, sono REM

│   └── Cerebelo: coordenação motora, timing, aprendizado motor

│

└── MIELENCÉFALO

    └── Bulbo: funções vitais (respiração, batimentos)

### 1.4 Oscilações Neurais e Ritmos Cerebrais

| Banda | Frequência | Estado Funcional | Função |
| :---- | :---- | :---- | :---- |
| Delta (d) | 0.5-4 Hz | Sono profundo (NREM) | Consolidação de memória |
| Theta (t) | 4-8 Hz | Sonolência, meditação | Memória episódica, navegação |
| Alpha (a) | 8-13 Hz | Relaxado, olhos fechados | Inibição cortical |
| Beta (b) | 13-30 Hz | Alerta ativo, motor | Cognição ativa, controle motor |
| Gamma (g) | 30-100 Hz | Processamento intenso | Binding perceptual, atenção focal |

**Binding Problem**: como atributos de um objeto percebidos por áreas separadas são unificados? Proposta: sincronização gamma (\~40 Hz) entre regiões.

---

## 2\. Cognição e Funções Executivas

### 2.1 Definição e Escopo

Cognição é o conjunto de processos mentais pelos quais o organismo adquire, transforma, armazena e utiliza informação:

- **Gnosias**: reconhecimento de objetos, pessoas, lugares  
- **Praxias**: execução de movimentos voluntários aprendidos  
- **Funções visuoespaciais**: percepção de relações espaciais, navegação  
- **Funções executivas**: planejamento, inibição, flexibilidade, metacognição

### 2.2 Funções Executivas — O "CEO" do Cérebro

Substrato principal: Córtex Pré-Frontal Dorsolateral (DLPFC)

**Componentes**:

1. **Controle Inibitório**: suprimir respostas automáticas inapropriadas (DLPFC, ACC)  
2. **Memória de Trabalho**: manter e manipular informação por curto período (DLPFC); capacidade \~7±2 itens  
3. **Flexibilidade Cognitiva**: mudar de perspectiva ou estratégia (ACC, OFC)  
4. **Planejamento**: organizar sequências de ações (DLPFC, córtex pré-motor)  
5. **Metacognição**: monitorar os próprios processos cognitivos (DLPFC medial, ACC)

**Aplicação Brain Simulator**: módulo supervisor/controlador que modula os demais módulos, implementando atenção top-down, manutenção de estado (memória de trabalho) e seleção de estratégias.

---

## 3\. Memória

### 3.1 Taxonomia da Memória

MEMÓRIA

├── DECLARATIVA (explícita) \-- Hipocampo/Lóbo Temporal Medial

│   ├── Episódica: eventos pessoais com contexto espaço-temporal

│   └── Semântica: fatos e conceitos gerais

│

└── NÃO-DECLARATIVA (implícita) \-- sistemas subcorticais

    ├── Procedural: habilidades motoras (cerebelo, estriado)

    ├── Hábitos: comportamentos habituais (gânglios da base)

    ├── Priming: facilitação por exposição prévia (neocórtex)

    └── Condicionamento: associações reflexas (amígdala, cerebelo)

**Caso H.M.** (validação experimental): após remoção bilateral do hipocampo, perdeu capacidade de formar novas memórias declarativas mas manteve memória procedural — demonstrando dissociação entre sistemas.

### 3.2 Estágios do Processamento de Memória

**Codificação**: transformação de experiência em representação neural. Fatores que melhoram: atenção, emoção, elaboração semântica, espaçamento.

**Consolidação Sináptica** (horas):

1. Ativação de receptores NMDA → influxo de Ca2+  
2. CaMKII ativada pelo Ca2+  
3. Fosforilação de receptores AMPA → aumento de condutância  
4. Inserção de novos receptores AMPA → potenciação (LTP)  
5. Ativação de CREB → síntese proteica → LTP tardio

**Consolidação Sistêmica** (semanas/anos):

- Hipocampo "indexa" e gradualmente transfere memórias para o neocórtex  
- Teoria do Indexamento Hipocampal: hipocampo mantém ponteiros para representações neocorticais distribuídas  
- Sono NREM: replay de memórias no hipocampo → transferência para neocórtex

**Papel do Sono**:

- NREM: replay episódico (ripples hipocampais \~100-200Hz \+ fusos talâmicos \+ ondas lentas corticais)  
- REM: consolidação emocional e procedural; integração de memórias novas com esquemas existentes

### 3.3 Mecanismos Moleculares da LTP

**Sequência de LTP Dependente de NMDA**:

1. Glutamato liberado pré-sinapticamente  
2. Receptor AMPA abre → despolarização parcial  
3. Receptor NMDA (bloqueado por Mg2+) desbloqueia com despolarização  
4. NMDA abre → influxo de Ca2+  
5. CaMKII ativada pelo Ca2+  
6. Fosforilação de AMPA → aumento de condutância  
7. Inserção de novos AMPA na membrana  
8. CREB ativado → genes de plasticidade (arc, zif268, BDNF)  
9. Síntese proteica → estruturas sinápticas novas (LTP tardio)

### 3.4 STDP — Spike-Timing-Dependent Plasticity

STDP é a versão biologicamente precisa do aprendizado Hebbiano:

Regra:

  dt \= t\_pos \- t\_pre

  Se dt \> 0 (pre antes pos): POTENCIAÇÃO

    dw \= A+ \* exp(-dt/tau+)

  Se dt \< 0 (pos antes pre): DEPRESSÃO

    dw \= \-A- \* exp(dt/tau-)

**Interpretação causal**:

- Pré→Pós: neurônio pré contribuiu para o disparo pós → relação causal → fortalecer  
- Pós→Pré: neurônio pré chegou tarde → relação anticausal → enfraquecer

**Exemplo experimental**: condicionamento no córtex auditivo com tom \+ choque elétrico. Conexões tom→medo potenciadas via STDP.

### 3.5 Redes de Hopfield — Memória Associativa

**Conceito Central**: memória não é localização, é padrão distribuído pelas conexões.

**Funcionamento**:

- **Armazenamento**: padrão gravado ajustando pesos via regra de Hebb  
- **Recuperação**: dado input parcial ou corrompido, rede evolui até padrão armazenado mais próximo (atrator)  
- **Capacidade**: \~0.14N padrões para rede de N neurônios

**Analogia biológica**: hipocampo CA3 (circuitos recorrentes excitadores) funciona como rede de Hopfield para completamento de padrões.

**Aplicação Brain Simulator**: módulo de memória de trabalho como rede recorrente com atratores; módulo hipocampal para armazenamento episódico com completamento de padrões.

---

## 4\. Aprendizagem

### 4.1 Tipos de Aprendizagem

**Condicionamento Clássico (Pavlov)**:

- EC pareado com EI → EC elicia RC  
- Substrato: amígdala (medo), cerebelo (reflexos), hipocampo (contexto)  
- Extinção \= nova aprendizagem inibitória (não apagamento do traço original)

**Condicionamento Operante (Skinner)**:

- Comportamento \+ reforço → aumento de probabilidade  
- Comportamento \+ punição → diminuição de probabilidade  
- Relação direta com Reinforcement Learning computacional

**Aprendizagem Procedural**:

- Fases: declarativa (consciente) → associativa (erros diminuem) → autônoma (automática)  
- Substrato: gânglios da base (inicial), cerebelo (timing), neocórtex (habilidades complexas)

### 4.2 Regras de Aprendizagem Biológicas

| Regra | Mecanismo | Tipo | Aplicação |
| :---- | :---- | :---- | :---- |
| Hebb | Atividade correlacionada → LTP | Não-supervisionado | Extração de características |
| STDP | Timing preciso de spikes | Não-supervisionado | Causalidade temporal |
| BCM | Limiar de modificação deslizante | Homeostático | Estabilidade \+ seletividade |
| TD-Error | Erro de predição dopaminérgico | Por reforço | Aprendizado de valor |

### 4.3 Fatores que Modulam Aprendizagem

1. **Atenção**: aumenta taxas de aprendizado — libera ACh e noradrenalina  
2. **Emoção**: amígdala modula hipocampo; eventos emocionais são melhor lembrados  
3. **Sono**: consolidação obrigatória para memória de longo prazo  
4. **Exercício**: BDNF aumentado → neurogênese hipocampal → melhor memória  
5. **Espaçamento**: prática distribuída melhor que prática maciça  
6. **Recuperação ativa**: testing \> releitura para consolidação

---

## 5\. Atenção

### 5.1 Tipos de Atenção

- **Seletiva**: foco em estímulo específico com supressão de outros  
- **Sustentada**: manutenção de alerta ao longo do tempo  
- **Dividida**: processamento simultâneo de múltiplas fontes  
- **Alternada**: mudança de foco entre tarefas (custo de task-switching)

### 5.2 Sistemas de Atenção

**Modelo de Posner (3 redes)**:

1. **Rede de Alerta**: prontidão e sensibilidade (SARA, tálamo, noradrenalina)  
2. **Rede de Orientação**: seleção de informação sensorial (córtex parietal, TPJ, FEF)  
3. **Rede Executiva**: resolução de conflito e controle (ACC, DLPFC, dopamina)

**DAN/VAN**:

- **DAN (Dorsal Attention Network)**: atenção top-down, voluntária (IPS \+ FEF)  
- **VAN (Ventral Attention Network)**: atenção bottom-up, reflexiva (TPJ \+ frontal inf.)  
- Anticorrelação: DAN ativo suprime VAN; VAN pode interromper DAN para reorientar

### 5.3 Mecanismos Neurais

**Spotlight Atencional**: amplifica representações relevantes, suprime irrelevantes.

**Supressão Competitiva**: objetos competem por representação; atenção modifica pesos da competição.

**Top-Down vs. Bottom-Up**:

- Top-down: objetivos guiam atenção (PFC → córtex sensorial)  
- Bottom-up: saliência física captura atenção reflexivamente

**Aplicação Brain Simulator**:

- Top-down: módulo PFC envia sinais amplificando/suprimindo representações em módulos sensoriais  
- Bottom-up: mapa de saliência computacional pode interromper processamento atual

---

## 6\. Linguagem

### 6.1 Componentes

| Componente | Definição | Substrato Neural |
| :---- | :---- | :---- |
| Fonologia | Sons da linguagem | Córtex auditivo, Wernicke |
| Morfologia | Estrutura de palavras | Broca, temporal posterior |
| Sintaxe | Regras de combinação | Broca, temporal posterior |
| Semântica | Significado | Temporal inferior, frontal ventral |
| Pragmática | Uso contextual | PFC, TPJ, hemisfério direito |

### 6.2 Neuroanatomia

**Área de Broca** (Giro Frontal Inferior, BA44/45):

- Produção da fala, formulação sintática  
- Lesão → Afasia de Broca: fala não-fluente, telegráfica

**Área de Wernicke** (Giro Temporal Superior Posterior, BA22):

- Compreensão da linguagem  
- Lesão → Afasia de Wernicke: fala fluente mas incoerente

**Fascículo Arqueado**: conecta Broca ↔ Wernicke

- Lesão → Afasia de Condução: repetição gravemente comprometida

**Modelo Dual-Stream contemporâneo**:

- Via Dorsal: mapeamento som-articulação, sintaxe (temporal→parietal→frontal)  
- Via Ventral: mapeamento som-significado, acesso lexical (temporal inferior)

### 6.3 Aplicação Brain Simulator

Módulo de linguagem baseado em Transformer, com representações multimodais:

- Via dorsal \= processamento sequencial/sintático  
- Via ventral \= acesso semântico/conceitual  
- Período crítico \= fase de alta plasticidade no treinamento

---

## 7\. Emoções

### 7.1 Componentes da Emoção

1. **Subjetivo**: sentimento (qualia emocional)  
2. **Fisiológico**: ativação do SNA (frequência cardíaca, sudorese, cortisol)  
3. **Motor**: expressão facial, postura, vocalização  
4. **Cognitivo**: avaliação (appraisal) e atenção seletiva

### 7.2 Sistemas Neurais

**Circuito de Papez**: Hipocampo → Corpos Mamilares → Tálamo Anterior → Córtex Cingulado → Córtex Entorrinal → Hipocampo

**Sistema Límbico**: Amígdala \+ Hipocampo \+ Córtex Cingulado \+ Hipotálamo

#### A Amígdala

**Via Rápida (Low Road, LeDoux)**: Tálamo → Amígdala (\~20ms)

- Reação automática a ameaças antes da consciência

**Via Lenta (High Road)**: Tálamo → Córtex Sensorial → Amígdala (\~300ms)

- Avaliação elaborada; pode modular resposta rápida

**Núcleos**:

- Complexo Basolateral (BLA): recebe inputs sensoriais; associação estímulo-emoção  
- Núcleo Central: saída para respostas autonômicas e comportamentais

**Condicionamento de Medo**: EC \+ EI → resposta condicionada. Plasticidade LTP-dependente no BLA.

**Extinção**: não apagamento do traço original, mas nova aprendizagem inibitória (PFC vmPFC inibe amígdala).

### 7.3 Sistema de Recompensa

**Circuito**: VTA → Núcleo Accumbens (via mesolímbica) → PFC

**Distinção wanting/liking** (Berridge):

- Wanting (querer): dopamina → motivação, busca  
- Liking (gostar): opioides endógenos → hedonia, prazer

**Aplicação Brain Simulator**: módulo amigdalar como sistema de avaliação de valência (positivo/negativo) e arousal (intensidade) que escala a taxa de aprendizado baseado em saliência emocional.

---

## 8\. Consciência

### 8.1 O Problema

**Problema Fácil**: explicar funções cognitivas (atenção, memória, reporte verbal). Abordável.

**Problema Difícil** (Chalmers): explicar por que há experiência subjetiva (qualia). Sem solução consensual.

### 8.2 Teorias Principais

#### Teoria do Espaço de Trabalho Global (GWT — Baars, Dehaene)

**Premissa**: consciência \= broadcast global de informação.

**Mecanismo**:

- Processamento inconsciente: informação em módulos especializados isolados  
- Limiar de consciência: "ignição" — informação enviada para todo o cérebro via rede fronto-parietal  
- Marcador: late burst em frontoparietal (P3b \~300ms)

**Correlatos Neurais**: PFC \+ Parietal \= workspace global; Tálamo \= gateway de consciência.

#### Teoria da Informação Integrada (IIT — Tononi)

**Premissa**: consciência \= integração irredutível de informação.

**Medida Phi (Φ)**:

- Φ \> 0: sistema tem alguma consciência  
- Φ elevado: consciência rica  
- Φ \= 0: sistema sem consciência (feedforward puro)

**Crítica aos Transformers**: arquitetura feedforward → Φ baixo. Loops recorrentes → Φ alto.

#### Teorias de Ordem Superior (HOT — Rosenthal)

Estar consciente de X requer ter pensamento de "estou percebendo X". Somente metarrepresentações (PFC) tornam estados conscientes.

### 8.3 Aplicação Brain Simulator

Operacionalizar consciência como:

- **Broadcast global**: ativo quando módulo tem acesso a todos os demais  
- **Grau de integração**: métricas de informação mútua entre módulos (aproximação de Φ)  
- **Auto-representação**: módulo metacognitivo que modela o estado interno do sistema

---

## 9\. Tomada de Decisão

### 9.1 Framework Neuroeconomia

| Área | Função |
| :---- | :---- |
| OFC | Codificação de valor de estímulos; comparação de opções |
| VMPFC | Valor subjetivo de escolhas; integração de emoção em decisão |
| ACC | Seleção de ação; monitoramento de conflito; custo de ação |
| DLPFC | Deliberação racional; inibição de respostas impulsivas |
| Estriado | Aprendizado de valor; seleção de ação habitual |
| Amígdala | Valor emocional; risco e aversão a perda |

### 9.2 RL Biológico — Algoritmo de Diferença Temporal

V(t+1) \= V(t) \+ alpha \* delta(t)

delta(t) \= r(t) \+ gamma \* V(t+1) \- V(t)  \[TD-error \= sinal dopaminérgico\]

alpha \= taxa de aprendizado

gamma \= fator de desconto temporal

**Mapeamento Neural**:

- delta(t) \= atividade de neurônios dopaminérgicos do VTA  
- V(t) \= atividade do estriado ventral e OFC  
- Política \= atividade do estriado dorsal e PFC

**Sistemas Paralelos**:

1. **Habitual (model-free)**: gânglios da base, rápido, inflexível  
2. **Deliberativo (model-based)**: PFC, lento, flexível, usa modelo interno do mundo  
3. Estresse, sobrecarga cognitiva, urgência → favorece sistema habitual

### 9.3 Vieses Cognitivos

- **Aversão à Perda**: perder X dói mais que ganhar X (amígdala \+ vmPFC)  
- **Desconto Hiperbólico**: preferência por recompensas imediatas vs. futuras  
- **Efeito de Enquadramento**: framing positivo/negativo gera escolhas diferentes  
- **Ancoragem**: primeiro número apresentado influencia julgamentos posteriores

**Aplicação Brain Simulator**: RL com dois sistemas paralelos (model-free \+ model-based) e sinal dopaminérgico como modulador de aprendizado global.

---

## 10\. Neuroplasticidade

### 10.1 Formas

**Plasticidade Sináptica**:

- LTP: aumento de eficácia sináptica  
- LTD: diminuição de eficácia; necessária para seletividade  
- Homeostase: escalamento sináptico para manter atividade estável

**Plasticidade Estrutural**:

- Espinhas dendríticas: surgem e desaparecem em horas-dias  
- Sinaptogênese: formação de novas sinapses (BDNF, atividade, exercício)  
- Poda Sináptica: eliminação de sinapses fracas (micróglia; sono)

**Neurogênese Adulta**:

- Hipocampo (Giro Denteado): novos neurônios continuamente; promovida por exercício  
- Comprometida por estresse crônico

**Reorganização Cortical**:

- Mapas corticais são plásticos: privação de input → expansão de áreas vizinhas  
- Cegos de nascença: córtex visual reconvertido para tato e audição

### 10.2 Períodos Críticos

Janelas de maior plasticidade determinadas por:

- Abertura: maturação de interneurônios GABAérgicos \+ sinaptogênese  
- Fechamento: PNNs (Perineuronal Nets) que "estabilizam" circuitos

**Aplicação Brain Simulator**:

- Implementar fases de desenvolvimento: alta plasticidade inicial → estabilização  
- Poda sináptica como regularização: eliminar sinapses abaixo de threshold  
- BDNF computacional: fator de plasticidade modulado por atividade geral

---

## 11\. Processamento Preditivo

### 11.1 O Cérebro como Máquina de Previsão

**Tese Central**: o cérebro não processa informação passivamente. Ele gera predições top-down e usa input sensorial apenas para corrigir erros de predição.

**Analogia**: o córtex visual não "vê" — ele imagina e verifica. Percepção é alucinação controlada.

### 11.2 Hierarquia Preditiva

Nível N+1 (abstrato):

    ↓ Predição (top-down)    ↑ Erro de predição (bottom-up)

Nível N (intermediário):

    ↓ Predição               ↑ Erro de predição

Nível N-1 (sensorial):

    ↓ Predição               ↑ Erro de predição

Input Sensorial

**Em cada nível**:

- Neurônios de predição: geram predição para nível inferior  
- Neurônios de erro: calculam diferença entre predição e input real; enviam erro ao nível superior  
- Pesos atualizam conforme erro diminui

### 11.3 Princípio da Energia Livre (Friston)

**Energia Livre \= Surpresa \= \-log P(dados|modelo)**

O cérebro minimiza surpresa em duas formas:

1. **Inferência Perceptual**: atualizar modelo interno para melhor explicar dados  
2. **Ação Ativa**: mover-se para que dados confirmem predições

**Unifica**: percepção (inferência bayesiana) \+ ação (minimizar erro motor) \+ aprendizado (atualizar parâmetros) \+ atenção (modular precisão dos erros)

### 11.4 Sinal Dopaminérgico de Erro de Predição

**Schultz (1997)** demonstrou que dopamina do VTA codifica TD-error:

Fase Naive: spike de dopamina no SUCO

Aprendendo: spike na LUZ (antecipação); reduzido no SUCO

Aprendido: spike na LUZ; sem spike no SUCO

Omissão: spike na LUZ; SILÊNCIO no momento esperado do SUCO

### 11.5 Implementação Brain Simulator

class PredictiveCodingLayer:

    def forward(self, bottom\_up\_input, top\_down\_prediction):

        \# Calcular erro de predicao

        error \= bottom\_up\_input \- top\_down\_prediction

        \# Propagar erro para camada superior

        return error

    

    def update(self, error, learning\_rate, precision=1.0):

        \# Precisao \= quanto confiar neste erro (atencao)

        weighted\_error \= error \* precision

        self.prediction\_weights \-= learning\_rate \* weighted\_error

---

## 12\. Redes Neurais Biológicas

### 12.1 Organização Cortical

**Coluna Cortical** (Mountcastle): unidade funcional do neocórtex, \~100 neurônios agrupados verticalmente em 6 camadas:

- Camada IV: recebe input do tálamo  
- Camada II/III: comunicação lateral e inter-áreas  
- Camada V: projeção para estruturas subcorticais  
- Camada VI: feedback para tálamo

**Tipos de Interneurônios GABAérgicos**:

- Basket cells: inibem corpo celular (controle de saída)  
- Chandelier cells: inibem axônio inicial (veto de ação)  
- Somatostatin cells: inibem dendritos (modulam inputs)  
- VIP cells: inibem inibidores (desinibição)

### 12.2 Conectoma e Redes de Larga Escala

**Princípios de Organização**:

1. Modularidade: clusters com alta conectividade interna  
2. Hubs: regiões altamente conectadas  
3. Rich Club: hubs se interconectam densamente  
4. Hierarquia: processamento em cascata primário → associativo

**Redes Funcionais (fMRI)**:

- DMN (Default Mode Network): PFC medial \+ parietal \+ hipocampo → pensamento interno  
- DAN: IPS \+ FEF → atenção voluntária  
- Salience Network: ínsula \+ ACC → detecção de relevância  
- CEN (Central Executive Network): DLPFC \+ parietal → controle cognitivo

**Anticorrelação DMN-DAN**: tarefa externa (DAN ativo) desativa DMN. Dificuldade nessa alternância em TDAH, depressão.

### 12.3 Comunicação entre Áreas — CTC

**Communication Through Coherence** (Fries): áreas cerebrais se comunicam quando oscilações estão em fase. Coerência gamma \= vias ativas.

**Aplicação Brain Simulator**: oscilações como mecanismo de gating entre módulos. Módulos sincronizados trocam informação; fora de fase são "silenciados".

---

## 13\. Neurociência Computacional

### 13.1 Modelos Formais do Neurônio

#### Integrate-and-Fire (I\&F)

tau\_m \* dV/dt \= \-(V \- V\_rest) \+ R \* I(t)

Disparo: V \>= V\_thresh

Reset: V \<- V\_reset

Período refratário: tau\_ref

Parâmetros: V\_rest=-70mV, V\_thresh=-55mV, tau\_m=20ms

#### Hodgkin-Huxley (HH)

Modelo biofisicamente preciso com canais Na+/K+:

C\_m \* dV/dt \= I\_ext \- g\_Na\*m3h\*(V-E\_Na) \- g\_K\*n4\*(V-E\_K) \- g\_L\*(V-E\_L)

Computacionalmente caro para redes grandes; mais preciso biologicamente.

### 13.2 Redes Neurais Artificiais como Modelos do Cérebro

**CNNs como Córtex Visual**:

- V1 \= primeira camada convolucional (bordas, orientações)  
- IT Temporal \= camadas profundas (objetos, faces)  
- Ativações de CNNs correlacionam com respostas neurais em V4/IT

**RNNs como Sistemas Temporais/Motores**:

- Córtex motor: integração temporal de sequências  
- LSTM \= análogo de memória de trabalho

**Transformers como Linguagem/Contexto**:

- Mecanismo de atenção \= seleção top-down em memória de trabalho  
- Multi-head \= múltiplos focos atencionais simultâneos  
- Hipocampo pode ser modelado como Transformer com atenção esparsa

### 13.3 Spiking Neural Networks (SNN)

**Vantagens sobre ANNs**:

- Processamento temporal (timing preciso dos spikes)  
- Eficiência energética (computação esparsa)  
- Suportam STDP nativamente

**Desafios**: gradiente não-diferenciável; treinamento mais difícil (surrogate gradients)

**Frameworks**: Brian2, NEST (simulação), SpykeTorch (ML com spikes)

---

## 14\. Aplicações para o Brain Simulator

### 14.1 Arquitetura Proposta — Brain Simulator v0.1

BRAIN SIMULATOR

├── MÓDULO SENSORIAL

│   ├── Visual (CNN-like)

│   ├── Auditório (tonotópico)

│   └── Somatossensorial

│

├── MÓDULO DE ATENÇÃO

│   ├── DAN (top-down voluntário)

│   ├── VAN (bottom-up reflexivo)

│   └── Mapa de Saliência

│

├── MÓDULO DE MEMÓRIA

│   ├── Trabalho (rede recorrente, \~7 slots)

│   ├── Episódica (Hopfield, completamento de padrões)

│   └── Semântica (embeddings \+ grafos)

│

├── MÓDULO DE EMOÇÃO

│   ├── Amígdala (valência \+ arousal)

│   └── Sistema de Recompensa (dopamina VTA)

│

├── MÓDULO COGNITIVO

│   ├── Processamento Preditivo (hierarquia top-down/bottom-up)

│   ├── Tomada de Decisão (RL model-free \+ model-based)

│   └── Funções Executivas (PFC supervisor)

│

├── MÓDULO DE LINGUAGEM

│   └── Transformer (sintaxe \+ semântica)

│

└── MODULAÇÃO GLOBAL

    ├── Dopamina (TD-error, plasticidade)

    ├── Noradrenalina (alerta, threshold)

    └── Acetilcolina (atenção, plasticidade)

### 14.2 Prioridades de Implementação

**Prioridade 1 — Core**:

- [ ] Neurônio I\&F com PEPS/PIPS e threshold  
- [ ] Rede de neurônios pulsáteis (SNN básico)  
- [ ] Regra de aprendizado STDP  
- [ ] Módulo de memória associativa (Hopfield)  
- [ ] Sinal de erro de predição (TD-error / dopamina)

**Prioridade 2 — Cognitivo**:

- [ ] Módulo de atenção com DAN/VAN  
- [ ] Memória de trabalho (rede recorrente com atratores)  
- [ ] Hierarquia preditiva (2-3 níveis)  
- [ ] RL model-free \+ model-based paralelos

**Prioridade 3 — Avançado**:

- [ ] Módulo de linguagem (Transformer)  
- [ ] Módulo emocional (valência \+ arousal)  
- [ ] Consciência como broadcast global  
- [ ] Consolidação por replay ("sono sintético")

### 14.3 Especificações Técnicas Principais

#### Neurônio Base

class BrainSimNeuron:

    V\_rest \= \-70.0      \# mV

    V\_thresh \= \-55.0    \# mV

    V\_reset \= \-70.0     \# mV

    tau\_m \= 20.0        \# ms

    t\_refract \= 2.0     \# ms

    def update(self, dt, excitatory\_input, inhibitory\_input,

               dopamine\_level=1.0, noradrenaline\_level=0.0):

        if self.in\_refractory\_period:

            return 0

        

        \# Modulacao de threshold por noradrenalina

        effective\_threshold \= self.V\_thresh \- 2.0 \* noradrenaline\_level

        

        \# Integracao

        dV \= (-(self.V \- self.V\_rest) \+ excitatory\_input \- inhibitory\_input) / self.tau\_m

        self.V \+= dV \* dt

        

        if self.V \>= effective\_threshold:

            self.V \= self.V\_reset

            self.in\_refractory\_period \= True

            return 1  \# spike

        return 0

#### Sinapse STDP

class STDPSynapse:

    A\_plus \= 0.01    \# amplitude de potenciacao

    A\_minus \= 0.01   \# amplitude de depressao

    tau\_plus \= 20.0  \# ms

    tau\_minus \= 20.0 \# ms

    def update\_weight(self, t\_pre, t\_post, dopamine\_signal=1.0):

        dt \= t\_post \- t\_pre

        if dt \> 0:    \# pre antes pos \-\> potenciacao

            dw \= self.A\_plus \* exp(-dt / self.tau\_plus)

        elif dt \< 0:  \# pos antes pre \-\> depressao

            dw \= \-self.A\_minus \* exp(dt / self.tau\_minus)

        else:

            dw \= 0

        

        dw \*= dopamine\_signal  \# neuromodulacao

        self.w \= clip(self.w \+ dw, self.w\_min, self.w\_max)

#### Módulo Dopaminérgico (TD-Error)

class DopaminergicModule:

    gamma \= 0.95  \# desconto temporal

    alpha \= 0.1   \# taxa de aprendizado

    def compute\_td\_error(self, state, next\_state, reward):

        """TD-error \= sinal dopaminergico"""

        V\_s \= self.value\_function.get(state, 0\)

        V\_s\_next \= self.value\_function.get(next\_state, 0\)

        

        td\_error \= reward \+ self.gamma \* V\_s\_next \- V\_s

        self.value\_function\[state\] \= V\_s \+ self.alpha \* td\_error

        

        return td\_error  \# positivo \= burst, negativo \= silencio

    def get\_dopamine\_signal(self, td\_error):

        baseline \= 1.0

        return max(0, baseline \+ td\_error)

---

## 15\. Sistemas Sensoriais

### 15.1 Princípios Gerais

**Transdução**: conversão de energia física em sinal elétrico pelos receptores sensoriais.

**Codificação Neural**:

- Rate Coding: intensidade codificada na frequência de spikes  
- Temporal Coding: informação no timing preciso dos spikes

### 15.2 Sistema Visual

**Percurso**: Retina → NGL → V1 → Via Dorsal (ONDE/ação) / Via Ventral (O QUÊ/reconhecimento)

**V1**: detectores de bordas orientadas; organização retinotópica; base para CNNs convolucionais

### 15.3 Sistema Auditório

**Tonotopia**: organização por frequência desde a cóclea até A1.

**Especialização hemisférica**:

- Esquerdo: processamento rápido/fonológico (fala)  
- Direito: processamento lento/espectral (melodia, prosódia)

---

## 16\. Relações Entre os Conceitos

### 16.1 Hierarquia Temporal do Processamento

| Escala Temporal | Processo | Mecanismo |
| :---- | :---- | :---- |
| \~1ms | Spike individual | Despolarização Na+/K+ |
| \~10ms | STDP window | Timing pré-pós |
| \~100ms | Integração cortical, binding | Sincronização gamma |
| \~300ms | Entrada na consciência | Late component P3b |
| \~1s | Consolidação sináptica inicial | CaMKII, AMPA insertion |
| \~6h | Síntese proteica | CREB, arc, BDNF |
| \~90min | Ciclo de sono NREM/REM | Replay hipocampal |
| \~dias | Consolidação sistêmica | Transferência neocortical |
| \~anos | Expertise | Reorganização cortical |

### 16.2 Interdependências Principais

NEUROPLASTICIDADE

   ├── LTP/LTD (molecular) ──────→ MEMÓRIA

   ├── STDP (temporal) ──────────→ APRENDIZAGEM

   └── Reorganização Cortical ───→ PERÍODOS CRÍTICOS

PROCESSAMENTO PREDITIVO

   ├── Hierarquia top-down ──────→ ATENÇÃO

   ├── Erro de Predição ──────────→ APRENDIZAGEM

   └── Free Energy Principle ────→ AÇÃO/PERCEPÇÃO

SISTEMA DOPAMINÉRGICO

   ├── TD-Error ─────────────────→ APRENDIZAGEM/RL

   ├── Motivação ────────────────→ EMOÇÕES

   └── Modulação PFC ────────────→ ATENÇÃO/FUNÇÕES EXEC.

HIPOCAMPO

   ├── Codificação Episódica ────→ MEMÓRIA DECLARATIVA

   ├── Indexação ────────────────→ CONSOLIDAÇÃO

   ├── Replay (sono) ────────────→ TRANSFERÊNCIA NEOCORTICAL

   └── CA3 Recorrente ───────────→ COMPLETAMENTO DE PADRÕES

---

## 17\. Insights Estratégicos

### 17.1 Para o Desenvolvimento do Brain Simulator

1. **Loop básico primeiro**: sensação → representação → ação → feedback, antes de adicionar emoções, linguagem ou consciência.  
     
2. **Multiescala é essencial**: o cérebro opera em ms (spikes) a anos (expertise) simultaneamente. O Brain Simulator precisa de mecanismos de múltiplas escalas temporais.  
     
3. **Inibição é tão crítica quanto excitação**: sistemas apenas excitatórios divergem. Interneurônios GABAérgicos são críticos para seletividade, sincronização, normalização de ganho.  
     
4. **Contexto muda tudo**: a mesma informação processada em contextos diferentes gera resultados diferentes. Moduladores (dopamina, ACh, NA) são os "parâmetros de contexto" do cérebro.  
     
5. **Erros são os dados mais valiosos**: o cérebro aprende primariamente de erros de predição. Todo sistema de aprendizado deve priorizar o sinal de erro.  
     
6. **Especialização \+ Integração**: módulos especializados são eficientes, mas inteligência emerge das *conexões* entre eles. O conectoma é tão importante quanto os módulos.  
     
7. **O inconsciente processa a maior parte**: 95%+ do processamento é inconsciente. Consciência é cara — reservar para decisões importantes.

### 17.2 Lições da Neurologia Clínica

- **Caso H.M.**: implementar memórias procedurais e episódicas em módulos separados  
- **Split-Brain**: modularidade pode criar "sub-agentes" independentes  
- **Phineas Gage**: sem PFC, sistema tem boa percepção mas mau julgamento social  
- **Neglect Unilateral**: memória de trabalho visuoespacial é distinta da verbal  
- **Afasias**: compreensão e produção da linguagem são dissociáveis

---

## 18\. Hipóteses para Futuras Pesquisas

### 18.1 Questões em Aberto na Neurociência

1. **Binding Problem**: como features visuais são integradas em objetos coerentes? Sincronização gamma é suficiente?  
2. **Problema Difícil da Consciência**: por que processos neurais geram experiência subjetiva?  
3. **Replay e Criatividade**: durante DMN ativo, o cérebro "remixa" memórias. É isso que gera insights?  
4. **Cognição Incorporada**: cognição sem corpo é possível?

### 18.2 Hipóteses para o Brain Simulator

1. **H1 — Emergência de Self**: sistema com suficiente complexidade e auto-representação desenvolvará modelo de si mesmo.  
2. **H2 — Criatividade como Replay Perturbado**: ruído nos replays durante "sono sintético" gera associações novas → insight.  
3. **H3 — Hierarquia Preditiva e Compreensão**: suficientes níveis preditivos convergirão para representações causais, não correlacionais.  
4. **H4 — Limiar de Consciência por Φ**: aumento de integração modular aumenta Φ → comportamentos análogos à consciência emergirão.  
5. **H5 — Currículo Ótimo de Treinamento**: ordem ótima espelha desenvolvimento humano: reflexos → percepção → imitação → linguagem → abstração.

---

## 19\. Glossário Técnico

| Termo | Definição |
| :---- | :---- |
| **AMPA Receptor** | Receptor ionotrópico de glutamato; media transmissão rápida; fosforilável para aumentar condutância (LTP) |
| **BDNF** | Brain-Derived Neurotrophic Factor; proteína que promove sobrevivência, crescimento e plasticidade neuronal |
| **Binding Problem** | Como representações neurais distribuídas de atributos distintos são integradas em percepção coerente |
| **CaMKII** | Ca2+/calmodulina kinase II; enzima chave na cascata de LTP |
| **Conectoma** | Mapa completo de conexões neurais de um organismo ou região |
| **CREB** | Fator de transcrição ativado por plasticidade; necessário para LTP tardio e memória de longo prazo |
| **DAN** | Dorsal Attention Network; atenção voluntária (IPS \+ FEF) |
| **DLPFC** | Córtex Pré-Frontal Dorsolateral; crítico para memória de trabalho e funções executivas |
| **DMN** | Default Mode Network; ativa durante repouso/devaneio |
| **Energia Livre** | Na teoria de Friston, medida de surpresa que o cérebro minimiza |
| **GABA** | Principal neurotransmissor inibitório do SNC |
| **GWT** | Global Workspace Theory; consciência como broadcast global (Baars, Dehaene) |
| **Homeostase Sináptica** | Ajuste homeostático de força sináptica via escalamento |
| **IIT** | Integrated Information Theory; consciência \= Φ (phi) de informação integrada (Tononi) |
| **LTD** | Long-Term Depression; diminuição duradoura de eficácia sináptica |
| **LTP** | Long-Term Potentiation; aumento duradouro de eficácia sináptica; base da memória |
| **Neuromodulador** | Substância (dopamina, serotonina, ACh, NA) que modifica processamento neural em volume |
| **NMDA Receptor** | Detector de coincidência; bloqueado por Mg2+ em repouso; crítico para LTP |
| **OFC** | Córtex Orbitofrontal; codifica valor; crítico para tomada de decisão |
| **Phi (Φ)** | Medida de integração de informação (Tononi/IIT) |
| **Potencial de Ação** | Sinal elétrico propagado pelo axônio; tudo-ou-nada |
| **Processamento Preditivo** | Framework: predições top-down \+ erros bottom-up (Rao, Ballard, Friston) |
| **SARA** | Sistema Ativador Reticular Ascendente; regula vigilância e sono |
| **SNN** | Spiking Neural Network; rede de neurônios pulsáteis; mais próxima da biologia |
| **STDP** | Spike-Timing-Dependent Plasticity; plasticidade baseada em timing preciso de spikes |
| **TD-Error** | Temporal Difference Error; sinal de erro de predição de recompensa \= dopamina |
| **VAN** | Ventral Attention Network; atenção involuntária/reflexiva (TPJ \+ frontal inf.) |
| **VTA** | Área Tegmental Ventral; principal origem de neurônios dopaminérgicos mesolímbicos |

---

## 20\. Referências Utilizadas

### Artigos Científicos Fundamentais

1. Bi, G., & Poo, M. (1998). Synaptic modifications in cultured hippocampal neurons. *J Neuroscience*, 18(24). — **STDP**  
2. Schultz, W., Dayan, P., & Montague, P.R. (1997). A neural substrate of prediction and reward. *Science*, 275\. — **Dopamina como TD-Error**  
3. Rao, R.P., & Ballard, D.H. (1999). Predictive coding in the visual cortex. *Nature Neuroscience*, 2(1). — **Processamento Preditivo**  
4. Friston, K. (2010). The free-energy principle: a unified brain theory? *Nat Rev Neuroscience*, 11(2). — **Free Energy**  
5. Tononi, G. (2008). Consciousness as integrated information. *Biological Bulletin*, 215(3). — **IIT**  
6. Hopfield, J.J. (1982). Neural networks with emergent collective computational abilities. *PNAS*, 79(8). — **Hopfield Networks**  
7. Hebb, D.O. (1949). *The Organization of Behavior*. Wiley. — **Regra de Hebb**  
8. Hodgkin, A.L., & Huxley, A.F. (1952). A quantitative description of membrane current. *J Physiology*, 117\. — **Modelo HH**  
9. LeDoux, J.E. (2000). Emotion circuits in the brain. *Annu Rev Neuroscience*, 23\. — **Amígdala**  
10. Posner, M.I., & Petersen, S.E. (1990). The attention system of the human brain. *Annu Rev Neuroscience*, 13\. — **Atenção**

### Livros de Referência

11. Kandel, E.R. et al. (2013). *Principles of Neural Science* (5th ed.). McGraw-Hill.  
12. Dayan, P., & Abbott, L.F. (2001). *Theoretical Neuroscience*. MIT Press.  
13. Sutton, R.S., & Barto, A.G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.  
14. Gazzaniga, M. et al. (2018). *Cognitive Neuroscience: The Biology of the Mind* (5th ed.). Norton.  
15. O'Reilly, R.C., & Munakata, Y. (2000). *Computational Explorations in Cognitive Neuroscience*. MIT Press.

---

*Documento gerado em: Junho 2026* *Projeto: Brain Simulator | Fase: Fundação de Conhecimento* *Próxima revisão: após implementação do Core (Prioridade 1\)*  
