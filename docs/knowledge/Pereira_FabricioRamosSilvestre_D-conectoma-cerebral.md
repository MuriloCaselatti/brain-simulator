iiiv
Informações para Biblioteca Digital
Título em outro idioma: Brain connectome : aplications of nuclear magnetic resonance
imaging in neurosciences
Palavras-chave em inglês:
Neurosciences
Magnetic resonance imaging
Brain function mapping
Brain connectivity
Connectome
Titulação: Doutor em Ciências
Banca examinadora:
Gabriela Castellano [Orientador]
Florindo Stella
Renato Cabral Rezende
Paulo Cesar Centoducatte
Mauro Antonio Pires Dias da Silva
Data de defesa: 22-07-2013
Programa de Pós-Graduação: Fisiopatologia Médica
Ficha catalográfica
Universidade Estadual de Campinas
Biblioteca da Faculdade de Ciências Médicas
Maristella Soares dos Santos - CRB 8/8402
Pereira, Fabricio Ramos Silvestre, 1975-
P414c PerConectoma cerebral : aplicações de imageamento por ressonância magnética
nuclear em neurociências / Fabricio Ramos Silvestre Pereira. – Campinas, SP :
[s.n.], 2013.
```
PerOrientador: Gabriela Castellano.
```
```
PerTese (doutorado) – Universidade Estadual de Campinas, Faculdade de
```
Ciências Médicas.
Per1. Neurociências. 2. Imageamento por ressonância magnetica nuclear. 3.
Mapeamento de funções cerebrais. 4. Conectividade cerebral. 5. Conectoma. I.
Castellano, Gabriela,1970-. II. Universidade Estadual de Campinas. Faculdade de
Ciências Médicas. III. Título.
```
Powered by TCPDF (www.tcpdf.org)
```
vvivii
Dedico esta tese aos trabalhadores do MST e da Via
Campesina. Pela coragem com que enfrentam a legislação
em busca de justiça social.
Quem me dera, ao menos uma vez,
Que o mais simples fosse visto como o mais importante
Renato Russo
viiiix
Agradecimentos
Quem me dera, ao menos uma vez,
Ter de volta todo o ouro que entreguei
A quem conseguiu me convencer
Que era prova de amizade
Se alguém levasse embora até o que eu não tinha.
Neste trabalho desejo agradecer ao leitor que tomou essa brochura para se entreter.
Seja pela curiosidade ou por interesse acadêmico, o fato é que agora tem acesso a um pouco
de minha vida discente. Mas me parece insuficiente apresentá-la sem dar os devidos créditos
aos muitos que permitiram que ela se materializasse.
```
Diferente da maioria dos trabalhos, meus agradecimentos (ainda que menores)
```
também são direcionados a alguns adversário pois me permitiram, não sem sofrimento,
entender que colegas podem se tornar inimigos quando interesses além da academia ficam
expostos. Contudo, como relatei na dissertação de mestrado, publicado há pouco mais de dois
anos, os agradecimentos mais fervorosos são dirigidos aos trabalhadores, que entendo ser os
```
verdadeiros mantenedores dos aparatos de Estado (como as universidades públicas) apesar da
```
hegemonia dos governantes desmerecerem esse crédito.
Meus agradecimento também são direcionados a meus tios Mário e Roseli, pois
apesar de eu não os ter mencionado na publicação anterior, ambos figuraram entre os mais
importantes personagens de minha formação discente e patrocinaram meu interesse pela
linguagem, função humana que vim a trabalhar de relance nessa tese. Agradeço também a
Ana Raquel, uma personagem nova em minha vida que mesmo sem fazer qualquer ação
propositiva, fez-me ponderar sobre as opções em minha vida. Profundo agradecimento teço
aos professor Geraldo pois foi ele que no momento mais difícil de minha carreira, acreditou
em minhas potencialidades e em meus valores éticos. A ele se deve o posto que fora ocupado
na mestrado pelo Professor Pélico, mentor e suporte para minhas ideias e produções.
x
Por fim, mas não menos importante, a meus pais que mais se orgulham dessa
```
produção do eu próprio; às minhas saudosas avós que em sua humildade e simplicidade
```
conseguiram esculpir as lições mais importantes dessa tese – a honestidade, ausente em
```
diversos espaços da academia; à Gabriela, minha amiga, que foi convertida em orientadora, e
```
ficou incumbida da árdua tarefa em me cobrar a apresentação desse trabalho apesar das
inúmeras evasivas que eu sempre promovia. A ela devo mais que minha gratidão e desculpas,
devo-lhe uma menção ilustre por ter-me aceitado como aluno em um momento difícil de
minha formação e de minha vida pessoal. O fato deste trabalho de doutorado, um calhamaço
com quase duas centenas de páginas, ter sido concluído em dois anos sem que eu tivesse
qualquer bolsa institucional mas que contra as expectativas já produziu meia dúzia de artigos
```
científicos em revistas indexadas (com elevado Fator de Impacto) e, inclusive, alguns já
```
terem sido citados por outros pesquisadores internacionais é prova da competência que
reconheço em minha orientadora.
Finalmente, quero agradecer à Fabiana, minha companheira de estrada há quase duas
décadas. A pessoa solidária que me confortou nos momentos delicados vividos no último
ano. Quem me trouxe sobriedade nos tempos de incertezas e que me apoia na nova e
promissora etapa que se abre.
..
xii
SUMÁRIO
RESUMO!...........................................................................................................................!xix!
ABSTRACT!...................................................................................................................!xxiii!
INTRODUÇÃO!.................................................................................................................!27!
```
Conectividade!Anatômica!(acMRI)!.....................................................................................!32!
```
```
Conectividade!Funcional!(fcMRI)!........................................................................................!46!
```
```
Homogeneidade regional ( ReHo – regional homogeneity )!......................................................!48!
```
```
Análise por componente independente ( ICA – independent component analysis )!...........!50!
```
```
Análise por clusterização temporal ( TCA – temporal clustering analysis )!........................!52!
```
```
Conectividade!Efetiva!(ecMRI)!.............................................................................................!55!
```
```
Modelagem de equações estruturais ( SEM – structural equation modelling)!....................!57!
```
```
Modelagem causal dinâmica (DCM – Dinamc Causal Modelling)!.........................................!65!
```
OBJETIVOS!......................................................................................................................!69!
Objetivos!Gerais:!.......................................................................................................................!70!
Objetivos!Específicos:!..............................................................................................................!70!
METODOLOGIA!.............................................................................................................!71!
Experimento!1!–!Conectividade!efetiva:!SEM!aplicado!à!plasticidade!etária!e!
codificação!de!palavras!com!conteúdos!emocionais.!...................................................!72!
Experimento!2!–!Conectividade!efetiva:!SEM!aplicado!a!ELTM!esquerdo!com!
codificação!de!palavras!neutras!e!abstratas!...................................................................!79!
Experimento!3!–!Modulação!de!conectividade!efetiva!por!codificação!de!
palavras!neutras!e!abstratas!.................................................................................................!92!
Experimento!4!–!Análise!de!imageamento!por!tensor!de!difusão!em!pacientes!
idosos!com!e!sem!diagnóstico!de!depressão!...................................................................!96!
xiii
Experimento!5!–!Anormalidade!em!substância!branca!e!cinzenta!em!pacientes!
com!mutação!do!gene!SPG11.!............................................................................................!103!
Experimento!6!–!Alterações!de!substância!branca!em!pacientes!com!doença!de!
Alzheimer!e!transtorno!cognitivo!leve.!..........................................................................!109!
Experimento!7!–!Alterações!neuropsiquiátricas!associados!com!danos!de!redes!
funcionais!em!pacientes!com!doença!de!Alzheimer!e!transtorno!cognitivo!leve.
!......................................................................................................................................................!120!
Experimento!8!–!Pasticidade!cerebral!em!codificação!de!memória!verbal!e!
visual!de!pacientes!com!epilepsia!medial!temporal.!.................................................!130!
Experimento!9!–!Redes!neurais!de!pacientes!obesos!com!disfunção!
hipotalâmica.!...........................................................................................................................!144!
DISCUSSÃO!...................................................................................................................!151!
SEM!aplicado!à!plasticidade!etária!e!codificação!verbal!..........................................!155!
SEM!aplicado!a!ELTM!esquerdo!com!codificação!verbal!..........................................!156!
DCM!aplicado!a!ELTM!unilateral!com!codificação!verbal!........................................!157!
CONSIDERAÇÕES FINAIS!.......................................................................................!159!
REFERÊNCIA BIBLIOGRÁFICA!...........................................................................!163!
xiv
LISTA DE ABREVIATURAS
AAL Atlas anatômico automatizado / Automated Anatomical Labeling
AD Difusividade Axial / Axial Diffusivity
BDI Inventário de Depressão de Beck / Beck Depression Inventory
BOLD Nível de oxigenação dependente / Blood Oxygenation Level Dependence
CBF Fluxo sanguíneo cerebral / Cerebral Blood Flow
CBV Volume sanguíneo cerebral / Cerebral Blood Bolume
CMRO2 Taxa de metabolismo cerebral de oxigênio / Cerebral Metabolic Rate of Oxygen
COUHES Comitê sobre uso de humanos como sujeitos experimentais / Committe on the Use of
Humans as Experimental Subjects
CT Tomografia Computadorizada / Computer Tomography
DCM Modelagem Causal Dinâmica / Dinamic Causal Modelling
dOHb Deoxi-hemoglobina / Deoxyhemoglobin
Doppler Efeito Doppler
DTI Imageamento por Tensor de Difusão / Diffusion Tensor Image
DWI Imageamento ponderado por difusão / Diffusion-weithted image
EEG Eletroencefalografia
efMRI Conectividade Efetiva / Effective Connectivity
ELT Epilepsia de Lobo Temporal
ELTM Epilepsia de Lobo Temporal Mesial
EPI Imagem Echo-Planar / Echo Planar Image
F2 Giro Frontal Médio
F3-OPER Giro Frontal Inferior – porção opercular
xv
F3-TRIANG Giro Frontal Inferior – porção triangular
FA Anisotropia Fracional / Fractional Anisotropy
fcMRI Conectividade Funcional / Functional Connectivity
fMRI Ressonância Magnética Funcional / Functional Magnetic Resonance Image
FOV Campo de visão / Field of view
HIP Hipocampo / Hippocampus
ICA Análise por Componente Independente / Independent Component Analysis
ICA Análise por Componente Independente / Independent Component Analysis
MD Difusividade Média / Mean Diffusivity
MEG Magnetoencefalografia
MIT Instituto de Tecnologia de Massachusetts / Massachusetts Institute of Technology
ML Máximo Verossímil / Maximun Likelihood
MLE Estimativa de Máximo Verossímil / Maximun Likelihood Estimation
MLF Função de Máximo Verossímil / Maximun Likelihood Function
MNI Instituto Neurológico de Montreal / Montreal Neurologic Institute
MRI Imageamento por Ressonância Magnétcia / Magnetic Resonance Image
OHb Oxi-hemoglobina / Oxyhemoglobin
PCA Análise por Componente Principal / Principal Component Analysis
PDF Função de distribuição de probabilidade / Probabilistic distribution function
PET Tomografia por emissão de pósitron / Positron Emition Tomography
PHIP Parahipocampo / Parahippocampus
PLS Quadrado Mínimo Parcial / Partial Least Squere
xvi
PPI Iteração Psico-fisiológica / Psico-Physiologic Interaction
rCBF Taxa do fluxo sanguíneo cerebral / rate of Cerebral Blood Flow
RD Difusividade Radial / Radial Diffusivity
ReHo Homogeneidade Regional / Regional Homogeneity
RM Ressonância Magnética
SEM Modelagem por Equação Estrutural / Structural Equation Modelling
SPECT Tomografia por emissão de fóton único / Single Photon Emition Computer Tomography
SVD Decomposição em valore singular / Singular Value Decomposition
TMS Estimulação Magnética Transcranial / Transcranial Magnetic Stimulation
VBM Volumetria baseada em voxel / Voxel Based Morphometry
xvii
LISTA DE TABELAS
Tabela 1: Lista das estruturas seguimentadas automaticamente no FreeSurfer
Tabela 2: Lista de palavras e não-palavra utilizada na emulação de memória verbal
Tabela 3: Lista de figuras e “não-figura” utilizada na emulação de memória visual
Tabela 4: Parâmetros de conectividade funcional entre regiões frontais e temporais
xviii
LISTA DE FIGURAS
Figura 1: Ilustração de imagens ponderadas por difusão em 6 direções.
Figura 2: Representação da difusão da molécula de água
Figura 3: Representação dos tensores de difusão
```
Figura 4: Espectro de índices de difusão (FA, MD e RD)
```
Figura 5: Exemplo de valores de índices de difusividade em regiões cerebrais
Figura 6: Visualização dos tratos cerebrais
Figura 7: Representação da definição de voxeis “vizinhos”
Figura 8: Redes funcionais identificas pelas técnicas de separação de componentes
Figura 9: Etapas de processamento da técnica de TCA
Figura 10: Grupos de codificação de palavras com conteúdo emocional
Figura 11: Ilustração de estruturas seguimentadas pelo Freesurfer.
```
Figura 12: Modelo anatômico: Hipocampos – Amídalas (estático).
```
Figura 13: Parâmetros de conectividade: Modelo Hipocampos – Amídalas.
Figura 14: Paradigma de codificação e evocação imediata: memória verbal
Figura 15: Paradigma de resting state
Figura 16: Paradigma de evocação tardia e reconhecimento: memória verbal
Figura 17: Paradigma de codificação e evocação imediata: memória visual
Figura 18: Paradigma de evocação tardia e reconhecimento: memória visual.
```
Figura 19: Modelo estrutural de ecMRI de regiões frontais e temporais (estático) .
```
Figura 20: Parâmetros de conectividade efetiva: controles vs pacientes ELTM esquerda
```
Figura 21: Modelo anatômico com modulação de conectividade efetiva (dinâmico)
```
Figura 22: Parâmetros de conectividade efetiva modulados pela codificação verbal
xix
RESUMO
xxxxi
O conectoma cerebral refere-se ao mapeamento dos circuitos neurais com os objetivos
```
de 1) identificar regiões que dão suporte às atividades mentais e comportamentais, e 2)
```
detectar alterações nesses circuitos que levam a distúrbios de ordem psiquiátrica e
neurológica. Na prática, os estudos de conectoma cerebral consistem na integração de
```
técnicas multimodais de imageamento como ressonância magnética (RM),
```
```
eletroencefalograma (EEG) e magnetoencefalograma (MEG) com o intuito de estimar os
```
tipos e os níveis de conexão entre regiões cerebrais remotas. Essa “conectividade” entre
regiões cerebrais é geralmente classificada em três tipos: anatômica, funcional e efetiva.
No presente trabalho, as técnicas de conectividade, usando dados de MR, foram
aplicadas na comparação de grupos saudáveis e patológicos.
Pela técnica de conectividade anatômica observou-se anomalias na substância branca
de pacientes com mutação no gene SPG11. Essa anomalias foram detectadas através da
```
redução da anisotropia fracional (FA) e aumento da difusividade média (MD), difusividade
```
```
radial (RD) e difusividade axial (AD) em regiões subcorticais dos lobos temporal e frontal,
```
bem como no giro do cíngulo, cuneus striatum, corpo caloso e tronco cerebral. Tais achados
indicam que o dano neuronal é mais difuso do que indicava a literatura. Um segundo estudo
de conectividade anatômica demonstrou que esses índices de difusividade não foram robustos
para diferenciar idosos com e sem diagnóstico de depressão indicando a necessidade de
avanços na formulação de novos índices com maior sensibilidade.
A técnica de conectividade funcional foi empregada em três estudos. No primeiro,
observou-se que pacientes com epilepsia de lobo temporal medial unilateral apresentam
redução da conectividade funcional durante a execução de tarefas de memória verbal e visual.
Essa redução foi predominantemente ipslateral à lesão e associada ao material-específico
utilizado no teste de memória. No segundo estudo, verificou-se uma redução dos padrões de
conectividade funcional hipotalâmica em sujeitos obesos e a sua parcial elevação após a
xxii
cirurgia bariátrica concomitantemente à redução de indicadores bioquímicos de inflamação.
No terceiro estudo, observou-se que pacientes com doença de Alzheimer apresentaram
```
elevação dos níveis de conectividade funcional na rede saliente (Salience Network) e redução
```
```
na rede de modo padrão (Default-mode network). Adicionalmente, verificou-se nos pacientes
```
a correlação positiva da síndrome hiperativa com os níveis de conectividade funcional no
cíngulo anterior e em áreas da ínsula direita. O conjunto desses resultados ilustra um possível
significado clínico para futuro diagnóstico e tratamento da doença de Alzheimer.
Pela técnica de conectividade efetiva observou-se que em função do envelhecimento
sadio há uma mudança dos parâmetros de conectividade durante a codificação de palavras
com conteúdo emocional. A influência do hipocampo sobre a amígdala ipslateral é reduzida
nos sujeitos mais velhos enquanto a influência da amígdala direita sobre o hipocampo direito
é elevada. Tais achados reforçam a tese da ininterrupta plasticidade etária e da dinâmica
cerebral normal. Essa mesma técnica foi também empregada para demonstrar os diferentes
padrões de influência entre os lobos frontal e temporal de pacientes com ELTM esquerda e
sujeitos controle. Encontrou-se alteração nos padrões de conectividade efetiva dos pacientes,
indicando que estes podem ser potenciais biomarcadores para a epilepsia.
xxiii
ABSTRACT
xxivxxv
Connectome refers to the neural circuitry mapping aiming to identify brain
regions that support mental and behavioral functions as well as to detect circuit
changes that are linked to psychiatric or neurologic disorders. In practice, connectome
studies link several neuroimaging approaches such as MRI, EEG and MEG by means
of the estimation of connections among remote brain regions. This “connectivity”
among brain regions is usually classified as anatomic, functional or effective.
In this work, the technique of connectivity, using MR data, was applied to
compare healthy and pathological groups.
By means of the anatomical connectivity abnormalities in the white matter of
patients with SPG11 mutation were observed. These abnormalities were expressed as
```
the reduction of the levels of fractional anisotropy (FA) and the increase in mean
```
```
(MD) and radial diffusivities (RD) in sub-cortical regions of temporal and frontal lobe
```
as well as in cingulated gyrus, cuneus, striatum, corpus callosum and brainstem.
These findings suggest that neuronal damage/dysfunction is more widespread than
previously recognized in this condition. Another anatomical connectivity study
showed that such indices of diffusivity were not robust to statistically differentiate
between old subjects with and without depression. This lacking on finding differences
between both groups indicates that new indices of diffusivity have to emerge in order
to provide complementary information about brain subtle microstructures.
Functional connectivity was applied to three studies. In the first study, it was
observed that patients with unilateral medial temporal lobe epilepsy presented lower
levels of functional connectivity during visual or verbal memory tasks. Such
reduction was ipsilateral to the side of the lesion and associated to the specific-
material used in the memory task. In the second work, the levels of functional
connectivity were reduced in hypothalamic regions of obese patients but a partial
xxvi
reversibility of hypothalamic dysfunction was observed after bariatric surgery. In the
third, patients with Alzheimer disease presented higher values of functional
connectivity in the salience network and a reduction of connectivity values in the
default-mode network. Also in these patients, significant correlations between the
levels of hyperactivity syndrome and the salience network were observed in the
anterior cingulate cortex and right insula areas. These results indicate the potential
clinical significance of resting state alterations in future diagnosis and therapy of
Alzheimer disease.
The effective connectivity approaches demonstrated that old and young
subjects have significant differences when encoding words with emotional contents.
The influence of the hippocampus on the ipsilateral amygdale was lower for older
subjects whereas the influence of the right amygdale on the right hippocampus was
increased for these subjects. These findings suggest that brain plasticity also happens
as function of age. The same approach was used to estimate the influence from frontal
to temporal lobes in patients with left MTLE compared to healthy subjects. The
patterns of effective connectivity were changed in patients and may be potentially
considered as biomarkers for epilepsy.
27
INTRODUÇÃO
2829
O estudo da dinâmica cerebral normal e patológica tem despertado interesse
```
da humanidade há milhares de anos (Feldman and Goodrich, 1999, Minagar et al.,
```
```
2003), contudo, foi no final do século passado que esses estudos ganharam impulso
```
vigoroso graças ao advento de técnicas mais apuradas de imageamento cerebral. As
técnicas como MEG, EEG, MRI, CT, SPECT, Doppler, PET entre outras, são
algumas das modalidades capazes de apresentar sinais fisiológicos em forma de
gráficos ou imagens. Cada técnica tem limitações, apesar de também possuir
```
vantagens. O imageamento por ressonância magnética (MRI), em particular,
```
congrega duas importantes vantagens: a possibilidade de imageamento estrutural com
elevada resolução anatômica e a capacidade de detecção indireta da atividade
cerebral.
Regiões cerebrais em atividade elevam o consumo metabólico e requisitam
```
maior aporte de oxigênio no local (Paulson et al., 2010). Para isso, um complexo
```
arranjo neuronal e vascular deve ser acionado para abastecer essas regiões.
```
Mecanismos como o aumento de fluxo sanguíneio (Chaigneau et al., 2007), a
```
```
dilatação de vasos (Glielmi et al., 2009), a elevação da extração de oxigênio pelos
```
```
tecidos (Herman et al., 2009), entre outras respostas fisiológicas, representam apenas
```
uma pequena parcela da intricada, porém harmônica, dinâmica cerebral.
Durante a atividade neural e o excessivo aporte de oxigênio, a concentração
```
venosa de oxi-hemoglobina (OHb) eleva-se. No entanto, em decorrência das
```
```
propriedades diamagnéticas dessa molécula (Savicki et al., 1984, Pauling, 1977), a
```
conformação magnética resultante no local não é alterada. Por outro lado,
```
simultaneamente, a molécula de desoxi-hemoglobina (dOHb) tende a ficar mais
```
diluída no interior do vaso, apesar de sua quantidade absoluta sofrer um pequeno
```
aumento. neste caso, as propriedades paramagnéticas da dOHb (Pauling and Coryell,
```
30
```
1936, Zborowski et al., 2003) aumentam proporcionalmente sua participação na
```
determinação da componente magnética resultante. Essa variação nas concentrações
de ambos os estados moleculares da hemoglobina pode ser observada
```
qualitativamente na RM (Ogawa et al., 1990), de forma que uma diminuição na
```
concentração de dOHb resulta num aumento do sinal de RM.
Finda a atividade neuronal, a relação oxi/desoxi hemoglobina retorna aos
padrões basais, restaurando a componente magnética associada com o este estado.
```
Esse comportamento em conjunto é conhecido como fenômeno BOLD (Blood
```
```
Oxygenation Level Dependent). Ele fornece indícios da dinâmica cerebral e tem sido
```
```
largamente empregado para se inferir funções cerebrais (Engel et al., 1994, Greene et
```
```
al., 2001, Abbott et al., 2010), uma vez que a atividade elétrica neuronal relaciona-se
```
```
com o sinal BOLD (Logothetis et al., 2001).
```
O sinal hemodinâmico também pode ser utilizado para detectar regiões
cerebrais funcionalmente conectadas. Determinadas áreas remotas apresentam
sincronia nas flutuações do fluxo sanguíneo local. Estas flutuações hemodinâmicas,
de baixas frequências e sincronizadas, foram observadas sem que o indivíduo realize
alguma tarefa a ele sugerido. As informações oriundas do imageamento ao longo do
```
tempo (fMRI), bem como sua análise espectral, carregam significados fisiológicos
```
capazes de serem traduzidos em mapas estatísticos. No estudo de conectividade, esses
```
mapas dizem respeito a possíveis interações funcionais entre regiões remotas (Cordes
```
```
et al., 2001, Goelman, 2004, Kruger and Glover, 2001). Entretanto, as séries
```
temporais que constituem as aquisições de fMRI são coletadas juntamente com ruídos
de fundo. Os ruídos de baixas frequências sobrepostos ao sinal BOLD provocam
distorções na observação do suposto fenômeno neural. Tais perturbações magnéticas
juntamente com o sinais genuinamente biológicos expõem a polêmica sobre o tema.
31
```
Alguns estudos chegam a considerá-lo apenas um fenômeno elusivo (Fingelkurts and
```
```
Kahkonen, 2005, Horwitz, 2003), destacando: a enorme variabilidade existente entre
```
```
as distintas atividades cerebrais (Waldvogel et al., 2000), entre indivíduos (Della-
```
```
Justina et al., 2008), e entre algoritmos de pós processamento da imagem (Friston et
```
```
al., 1993b, Zhao et al., 2004), bem como a elevada capacidade plástica do cérebro
```
```
para realizar conexões (Das and Gilbert, 1995, Hyde and Knudsen, 2002, Roder et al.,
```
```
2002, Webster et al., 1995) e as diferentes escalas de tempos em que ocorre o
```
fenômeno neural e a aquisição do dado é feita.
Assim como as propriedades funcionais do cérebro são inferidas in vivo pelo
acoplamento da atividade neuronal com a flutuação magnética local, propriedades
micro-estruturais dos tratos cerebrais são estimadas pela difusividade da molécula de
```
água no tecido (Le Bihan et al., 1986). Os tratos cerebrais, constituídos pelos
```
axônios dos neurônios, possuem características particulares devido à forma alongada.
Graças a essa forma, as moléculas de água tendem a deslocar-se prioritariamente ao
```
longo do eixo principal (difusividade axial) dos axônios, enquanto há uma maior
```
limitação para deslocamento dessas moléculas nas direções perpendiculares a esses
```
eixos (difusividade radial). A propriedade de difusão da água em uma direção
```
prioritária é conhecida como anisotropia e pode ser estimada com imagens tensoriais
revelando possíveis danos neuronais na micro-estrutura da substância branca.
32
```
Conectividade Anatômica (acMRI)
```
Depreende-se por conectividade anatômica a detecção das vias físicas que
interligam áreas cerebrais remotas. O conceito pressupõe a combinação inseparável
com a conectividade funcional, dado que, o surgimento de novas conexões neurais,
bem como a deleção de outras existentes, é mediado em grande parte pela própria
atividade neural. As novas conexões anatômicas são estabelecidas levando-se em
```
consideração: 1) os axônios e as sinapses que tomam parte na competição (deleção ou
```
```
criação) da via; 2) definindo em qual tipo de competição (excitação ou inibição) as
```
```
estruturas estarão envolvidas; e 3) regulamentando as normas (especialização ou
```
```
generalização, convergente ou divergente, etc) seguida pela atividade eletrofisiológica
```
```
(van Ooyen, 2001). Estudos pregressos (Ridge and Betz, 1984) em ratos
```
demonstraram que neurônio de unidade neuro-motoras, após séries de estimulações
crônicas, possuem maior vantagem competitiva que os neurônios não estimulados,
reforçando a tese da indissociabilidade entre conectividade anatômica e funcional,
entretanto não se tem estudos conclusivos em humanos.
As formas de imageamento utilizada para se estudar a conectividade
```
anatômica são a técnica de imageamento por tensores de difusão (DTI – Diffusion
```
```
Tensor Image) e a técnica conhecida como Molecular Imaging. Esta última utiliza
```
traçadores biofármacos que interagem com as fibras neurais e as expõem sobre forma
```
de imagem (Frost, 2003) e sua natureza pode ser radioativa, magnética ou metabólica,
```
a primeira baseia-se em princípios de difusividade.
```
A DTI envolve a aquisição de imagens ponderadas por difusão (DWI –
```
```
Diffusion-Weithted Image) que são sensibilizadas em vários gradientes, de diferentes
```
```
direções, no mínimo de 6 para imagens em 3 dimensões (Chen and Hsu, 2005).
```
Calcula-se a diagonalização do tensor de difusão em cada voxel, elegendo o autovetor
33
```
para representar a orientação local (Basser et al., 1994). Dado que a molécula de água
```
no interior das fibras neurais tem uma orientação prioritária, que segue ao longo da
fibra, a tratografia utiliza o princípio da anisotropia para estabelecer a conectividade
anatômica.
Todo fluído possui a propriedade intrínseca de difusão D, que reflete a
mobilidade das moléculas em um ambiente microscópico. As moléculas de água
podem ser sensibilizadas pela técnica de MRI em intervalos de tempo que variam
desde milissegundos até poucos segundos, e em deslocamentos que estendem-se de
10-8 a 10-4 metros. Essa distância é da mesma ordem que a dimensão da célula e, deste
modo, a quantificação da constante D nos diferentes tecidos oferece informações
sobre os mesmos.
A difusão da água in vivo é afetada pela dinâmica do transporte celular através
de sub-compartimentos celulares ou por membranas impermeáveis, o que torna
possível caracterizar os tecidos a partir do tempo de difusão, pois há, por exemplo,
diferentes padrões de difusão entre as substâncias cinzenta e branca.
Cada molécula em uma amostra comporta-se independentemente. Colisões
entre moléculas provocam deslocamentos randômicos, sem direções prioritárias,
através do trecho conhecido como “caminho livre”. Dado um intervalo de tempo, é
possível estimar a distância difundida, contudo, não é possível determinar as direções
que a molécula percorreu. Apesar desse processo ser de caráter randômico, há
mecanismos físicos que o dirigem. Em fluídos com diferentes concentrações, esta
grandeza geralmente é utilizada para descrever tais processos, entretanto, em tecidos
biológicos, a principal grandeza a ser considerada é a agitação térmica, geralmente
```
expressa como a probabilidade (P) de se encontrar uma partícula em determinada
```
```
posição (R) em um dado intervalo de tempo (t).
```
34
Em analogia à segunda lei da difusão de Fick, o mecanismo pode ser descrito
```
por:
```
Equação 1
∂P
∂t
= D∇2P
D ≡ coeficiente de difusão
Para as situações em que o ambiente não oferece uma direção prioritária de
```
deslocamento da molécula de água (isotropia), a solução da Equação 1 assume a
```
distribuição gaussiana em três dimensões equivalente a:
Equação 2
```
PX,t( ) =
```
1
D4π t
exp
−R2
4D t
"
#
$
%
&
'
R ≡ Deslocamento espacial
O caminho médio livre pode ser calculado em termos da constante de difusão:
Equação 3
```
R2 = R2P R ,t( )dR = 6D t∫
```
R ≡ Vetor distância percorrida pela molécula de água no tempo t
O processo de difusão também pode ser modelado assumindo que as partículas
escolhem caminhos randômicos feitos por n sucessivos deslocamentos de tamanhos ξ
e em intervalos de tempo constates τ sobre o tempo total de:
35
Equação 4
```
t = nτ
```
τ ≡ intervalo de tempo constante
Após cada deslocamento, há uma nova colisão e uma nova orientação
randômica. Deste modo pode-se escrever o caminho médio livre por:
Equação 5
```
R2 = nξ2 =
```
tξ2
τ
ξ ≡ tamanho do deslocamento
Combinando as Equação 3 e Equação 5, tem-se o coeficiente de difusão
obtido pelo comportamento do caminho médio livre. Esta equação, conhecida como
equação de Einstein, é expressa por:
Equação 6
```
D =
```
ξ2
6τ
D ≡ coeficiente de difusão
Quando o ambiente oferecer diferentes propriedades de difusão, a depender da
escolha de uma direção específica, o coeficiente de difusão deverá ser expresso em
sua forma tensorial. Considerando que a probabilidade de deslocamento da molécula
ainda possa ser estimada a partir da distribuição gaussiana, o tensor de difusão será
caracterizado por:
36
Equação 7
```
D =
```
DXX DXY DXZ
DYX DYY DYZ
DZX DZY DZZ
"
#
$
$
$
%
&
'
'
'
D ≡ coeficiente de difusão
Considerando constante cada elemento da matriz da Equação 7, pode-se
aplicar a segunda lei de Fick para o caso anisotrópico.
Equação 8
∂ C
∂ t
= Dij
∂2C
∂i∂j
∑
D ≡ coeficiente de difusão
No caso particular, em que as moléculas não possuam carga elétrica resultante,
```
como as moléculas de água, a matriz do tensor de difusão é simetrico (Dij = Dji),
```
portanto, D pode ser completamente descrito por Dxx, Dyy, Dzz, Dxy, Dxz e Dyz que
representam a difusividade em 6 direções, referenciadas no equipamento de
ressonância magnética. A Figura 1 ilustra o tensor de difusão D em um estudo de
```
imageamento por tensor de difusão (DTI).
```
37
Figura 1: Tensor de difusão D estimado por imagens ponderadas por difusão que foram
obtida por RM com gradiente em 32 direções.
Conhecida essas 6 diferentes componentes do tensor de difusão, é possível
transformá-lo em outro tensor com elementos nulos excetuando-se a diagonal, pois
esta representaria as propriedades intrínsecas da amostra, independentemente do
sistema de coordenadas em que ela foi medida. A operação consiste em escolher um
sistema de eixo que anula os elementos do tensor que não fazem parte da diagonal
```
principal. Como resultado, um conjunto de autovalores (λ1, λ2 e λ3) e autovetores (ε1,
```
38
```
ε2 e ε3) do tensor D é produzido. A representação geometricamente tradicional desse
```
autovalores e autovetores é sob a forma de uma elipsóide em cujos eixos possuem
```
tamanho identificados por (λ1, λ2 e λ3). A Figura 2 ilustra o caminho médio livre
```
```
percorrido pela molécula de água no espaço anisotrópico (Figura 2A), a comparação
```
```
qualitativa desse deslocamento nos meios isotrópico e anisotrópico (Figuras 2B) e a
```
representação geométrica da elipsóide que quantifica os índices de anisotropia
```
(Figura 2C).
```
```
Figura 2: Representação da difusão da molécula de água. A) caminho médio livre
```
```
(vermelho) e sucessivos trechos de choque (azul). B) Ilustração da difusão nos meios
```
39
```
isotrópico (primeiro) e anisotrópico (segundo). C) Representação geométrica e
```
quantificação do índice de anisotropia.
```
A parametrização de uma elipsóide (como aquela descrita na Figura 2C) pode
```
ser feira em relação aos autovalores encontrados na diagonalização da matriz D de
acordo com a Equação 9 abaixo.
Equação 9
```
Pθ ,ϕ( ) =
```
```
λ3cosθ( )senϕ( )
```
```
λ2senθ( )senϕ( )
```
```
λ1senϕ( )
```
%
&
'
'
'
```
(
```
```
)
```
*
*
*
λ1,λ2 eλ3 ≡ Autovalores
θ eφ ≡ ângulos sobre as superfície da elipsóide
Deste modo, diferentes tensores de difusão produzem, em cada voxel da
imagem, representações elipsoidais distintas. A Figura 3 abaixo exemplifica a
dependência geométrica para alguns valores de tensor de difusão.
40
```
Figura 3: Representação de tensores de difusão. A) geometria isotrópica. B) geometria
```
```
anisotrópica com grau de isotropia no plano horizontal. C) geometria anisotrópica.
```
Obs.: Os eixos ortogonais não são os eixos do ressonador, e estão orientados nas
```
direções póstero-anterior (x), látero-lateral (y) e ínfero-superior (z).
```
O grau de anisotropia é computado por índices relacionados aos autovalores.
Diversos índices podem ser utilizados entretanto, os mais comuns são a anisotropia
```
fracional (FA) definida na Equação 10, a difusividade média (MD) definida na
```
```
Equação 11 e a difusividade radial (RD) definida na Equação 12.
```
Equação 10
```
FA =
```
1
2
```
λ1 −λ2( )
```
2
```
+λ1 −λ3( )
```
2
```
+λ2 −λ3( )
```
2
λ12 +λ22 +λ32
$
%
&
&
'
```
(
```
```
)
```
```
)
```
FA ≡ índice de anisotropia fracional
λ1,λ2 eλ3 ≡ Autovalores
41
Equação 11
```
MD =
```
λ1 +λ2 +λ3
3
MD ≡ índice de difusividade média
λ1,λ2 eλ3 ≡ Autovalores
Equação 12
```
RD =
```
λ2 +λ3
2
RD ≡ índice de difusividade radial
λ2 eλ3 ≡ Autovalores
O índice FA possui valores adimensionais variando entre 0 e 1. O valor 0
```
(zero) é característico de geometrias completamente isotrópicas enquanto o valor 1
```
```
(um) representa geometrias completamente anisotrópicas. Os índices MD e RD têm
```
valores adimensionais variando de 0 ao infinito e representam respectivamente a
difusividade média em uma dada região e a difusividade perpendicular ao eixo de
maior difusão. A Figura 4 apresenta o espectro dos valores de FA e a respectiva
representação geométrica.
43
Figura 5: Representação elipsoidal e respectivos valores de FA, MD e RD estimados pelo
```
com Tensor de Difusão “D” na (A) Radiação Talâmica Anterior, no (B) Pólo Frontal, no
```
```
(C) Fórceps Maior, no (D) Liquido Cefalorraquidiano e no (E) Corpo Caloso.
```
```
Coordenadas registradas no espaço padrão do Instituto Neurológico de Montreal (MNI).
```
Obs.: Os eixos ortogonais não são os eixos do ressonador, e estão orientados nas
```
direções póstero-anterior (x), látero-lateral (y) e ínfero-superior (z).
```
44
Os índices de difusividade refletem as características de anisotropia local e, no
cérebro, essas características dizem respeito às informações micro-estruturais do
tecido. Regiões com alto índice de anisotropia, como os tratos, podem ser
concatenados para permitir o rastreamento das vias que ligam duas regiões remotas. A
Figura 6 ilustra a fisiologia do trato, com elevado alto índice de anisotropia.
```
Propriedade que permite seu rastreamento (tratografia) através do cerebral.
```
45
Figura 6: Visualização dos tratos cerebrais. Modelo da fisiologia micro-estrutural dos
```
tratos revelando propriedades anisotrópicas ao longo do feixe (A). Ilustração das direções
```
```
dos feixes neuronais sobre um corte coronal (B) com detalhe sobre o corpo caloso (C).
```
Reconstrução dos tratos no hemisfério direito e as respectivas projeções para o
```
hemisfério direito – tratografia (D). Registro de tratos conectando cérebro e coluna
```
espinhal através da ponte. Tons em vermelho representam a direção látero-lateral. Tons
em verde indicam direção ânterio-posterior. Tons de azul significa direção ínfero-
superior.
46
```
Conectividade Funcional (fcMRI)
```
A definição de conectividade funcional é dada pela correlação entre eventos
```
neurofisiológicos remotos (Friston et al., 1993b). O conceito, apesar de oferece
```
informações sobre sincronia entre as regiões corticais envolvidas na emulação de
eventos neurofisiológicos, não lida diretamente com a relação de causa-efeito desses
eventos.
Os processos neurais não seguem necessariamente padrões gaussianos
entretanto, pode-se caracterizá-los em termos da dependência estatística de segunda
```
ordem, e assim, utilizar correlações para estimar a conectividade funcional (Friston,
```
```
2007). Ao assumir que as medidas neurofisiológicas dispersam-se conforme a
```
distribuição Gaussiana basta estimar os valores da covariância para se obter os
parâmetros de conectividade funcional. O índice de correlação é representado pela
covariância normalizada.
O ponto crítico para evoluir a análise da conectividade funcional está
associado com o fato de que a simples correlação de um voxel com os demais não é
de grande interesse no estudo, a menos que a série temporal descritas por único voxel
seja representativa de uma região de interesse ou de uma estrutura cerebral, ou ainda,
que nele expresse-se um valor significativo de mapas estatísticos oriundos de análises
prévias, como mapas estatísticos de fMRI. Apenas absorvendo estas considerações é
que a série temporal de um único voxel pode ser suficiente para se entender
fenômenos fisiológicos.
Tratando-se da estrutura de covariância, o mais importante aspecto é a
estimativa de padrões de atividade, correlacionados em um grande número de pares
co-variantes. Diversas estratégias podem ser empregadas para se mensurar tais
padrões, desde as mais elementares, como a média das séries temporais de uma região
47
de interesse, até as mais elaboradas, como estratégias não-lineares. Um maior
aprofundamento dessa técnica pode ser obtido na dissertação mestrado publicada pelo
```
autor há dois anos (Pereira, 2011).
```
Dentre as diversas metodologias disponíveis para se estimar o padrões de
conectividade funcional, três em especial têm se destacado na literatura por não
requisitarem informações a priori sobre o sistema. A primeira, denominada, Regional
```
Homogeneity (ReHo), aborda aspectos locais na busca por de homogeneidade nas
```
flutuações hemodinâmicas enquanto a segunda, Independent Component Analysis
```
(ICA) é capaz de separar redes neurais que foram originadas por uma mesma fonte de
```
frenquência, como as próprias oscilações hemodinâmicas. Uma terceira metodologia
```
denominada Temporal Clustering Analysis (TCA) também tem sido utilizada para
```
extrair uma série temporal sem hipótese definida à prior mas que se relaciona com a
resposta hemodinâmica e consequentemente, passível de modelagem com as imagens
de fMRI.
48
```
Homogeneidade regional ( ReHo – regional homogeneity )
```
Os parâmetros de homogeneidade regional são estimados pelo coeficiente de
```
correlação de kendall (Kendall and Gibbons, 1990) definidos pela Equação13. Esse
```
teste avalia a similaridade entre séries temporais encapsuladas pelos voxeis vizinhos.
Usa-se estatística não paramétrica sob a forma de ordenamento discreto para cada
ponto no tempo das séries temporais e produzem valores entre 0 e 1. A Figura 7
ilustras a definição de voxeis vizinhos para uma dada aquisição em EPI.
Equação 13
```
KCC =
```
Ri2 − nR 2∑
1
12
```
K 2 n3 − n( )
```
R ≡
```
n +1( )K
```
2
KCC ≡ coeficiente de correlação de Kendall
Ri ≡ soma do ordenamento em cada i-nésimo ponto temporal
```
K ≡número de séries temporais avaliadas (voxels vizinhos).
```
n ≡total de pontos no tempo
49
Figura 7: Representação de uma aquisição de série temporal em EPI. Voxels
```
apresentados em nivies de cinza (A). Definição de “vizinhos” para um determinado
```
```
voxel (vermelho). Cada voxel tem seis vizinhos nas faces, doze vizinhos nas arestas e
```
```
oito vizinhos nos vértices (B).
```
50
```
Análise por componente independente ( ICA – independent component analysis )
```
O método de ICA é uma potente ferramenta empregada para separar fontes
```
(flutuações hemodinâmicas) independentes que estejam linearmente misturadas.
```
```
Consiste em representar um sistema matricial (e.g. Figura 7A) sem manter
```
necessariamente a ortogonalidade entre esses eixos. Mais informação sobre separação
de componentes podem ser obtidos na dissertação de mestrado do autor, em especial
uma ferramenta semelhante ao ICA denominada Principal Componente Analysis
```
(PCA).
```
Diversas redes funcionais foram identificadas nos cérebro de jovens controles.
As mais utilizadas na literatura com objetivo de investigação em sistemas patológico
são apresentadas na Figura 8.
51
Figura 8: Principais redes funcionais humanas identificadas pela técnica de
```
separação de componentes. Redes de saliência anterior (A) e posterior (B), de modo
```
```
padrão dorsal (C) e ventral (D), de controle executivo direito (E) e esquerdo (F), de
```
```
audição (G), do gânglios da base (H), visual superior (I) e primária (J), de linguagem
```
```
(K), sensoriomotor (L), pré-cuneus (M) e visoespacial (N).
```
52
```
Análise por clusterização temporal ( TCA – temporal clustering analysis )
```
```
Por fim, a metodologia de Temporal Clustering Analysis (TCA) computa uma
```
série temporal a partir dos dados de fMRI. Essa técnica consiste em três fazes:
identificar o maior valor de intensidade de sinal para cada série temporal, zerar todos
os pontos no tempo da respectiva série temporal que não possuem esse valor máximo
e somar todos os valores remanescentes em um dado ponto no tempo.
Matematicamente, as operações empregada no TCA são as seguintes:
Seja as séries temporais descritas pela Equação 14.
Equação 14
```
F x,y,z,t( )
```
F ≡ intensidade do sinal em um dado ponto no espaço e tempo
x,y,z ≡ coordenadas espaciais relacionadas ao voxel
t ≡coordenada temporal
Aplica-se uma transformada na Equação 14 para converter diretamente o
```
espaço de quatro dimensões (x,y,z,t) em duas (s,t) descritas pela Equação 15. Na
```
operação ℜ4 ⇒ ℜ2 o número de voxel permanece constante calculado pelo
```
produto dos números de voxeis nas três dimensões espaciais (x,y,z).
```
Equação 15
```
⊕F x,y,z,t( ) = G s,t( )
```
⊕ ≡ operador espacial
53
s ≡ coordenada espacial relacionadas ao voxel
S ≡X.Y.Z
Desse modo, a matriz de dados transformados G pode ser escrita como
apresentado na Equação 16.
Equação 16
```
G s,t( ) =
```
G1,1 G1,2 … G1,T
G2,1 G2,2 … G2,T
   
GS,1 GS,2 … GS,T
!
"
#
#
#
#
#
$
%
&
&
&
&
&
A primeira etapa do TCA caracteriza-se pela identificação dos valores
máximos em cada serie temporal. Essa etapa pode ser representada pela Equação 17.
Equação 17
```
H s( ) =
```
```
max G1,1, G1,2, ... G1,T( )
```
```
max G2,1, G2,2, ... G2,T( )
```

```
max GS,1, GS,2, ... GS,T( )
```
"
#
$
$
$
$
$
%
&
'
'
'
'
'
=
H1
H2

HS
"
#
$
$
$
$
%
&
'
'
'
'
A segunda etapa do TCA anula os valores para cada ponto no tempo da
respectiva série temporal que não possuem valores máximos. Essa etapa é descrita
pela Equação 18.
Equação 18
55
```
Conectividade Efetiva (ecMRI)
```
O conceito de conectividade efetiva foi definido como a influência que um
```
sistema neural exerce sobre outro, de forma direta ou indireta (Friston et al., 1993a,
```
```
Aertsen et al., 1991, Friston, 1994). Trata-se da estimativa de parâmetros associados a
```
modelos estruturais. Esses parâmetros expressam relações de causa-efeito sejam
acionadas por estímulos externos que atuam sobre os sistemas neurais, sejam apenas
operados entre os próprios sistemas onde, tanto a causa como o efeito são elementos
exclusivos da rede neuronal. Os parâmetros apontam quantidades dinâmicas utilizadas
para identificar os níveis de influência sobre um sistema físico em respostas às forças,
ações ou estímulos externos, bem como repercussões secundárias no sistema neural
causada anteriormente por um outro elemento desse sistema.
Nas dimensões do neurônio, o conceito traduz-se em como a atividade pré-
sináptica influencia a resposta pós-sináptica, fenômeno também conhecido como
eficácia sináptica. Na escala temporal operada pela fMRI, o conceito deve ser
entendido em como a resposta hemodinâmica de uma determinada região é perturbada
pela ação de outra série temporal, seja esta, de uma estrutura cerebral remota ou de
um estímulo externo. Ambas as opções exigem, a priori, um modelo estrutural em
que se busca estimar os parâmetros de conectividade.
A técnica ainda permite tanto identificar mudanças na influência entre as
componentes cerebrais interconectadas bem como selecionar modelos estruturais mais
adequados aos fenômenos neurais estudados. Aquele, surje como uma medida indireta
de plasticidade ou de modulação por uma função cerebral enquanto esta, fazendo-se
uso de inferências bayesianas, responde pela otimização do modelo estrutural.
Em resumo, no estudo de conectividade efetiva é possível obter as seguintes
```
informações: 1) como uma região de interesse influencia outra – medida estática; 2)
```
56
```
como um estímulo modula a interação entre regiões de interesse – medida dinâmica e;
```
```
3) qual o modelo estrutural mais apropriado dentre um conjunto de opções –
```
inferência bayesiana.
57
```
Modelagem por equações estruturais ( SEM – structural equation modelling)
```
Uma forma de estimar os parâmetros de conectividade é através de regressões
```
na estrutura da matriz de variância-covariância (Buchel and Friston, 1997, McIntosh
```
```
and Gonzalez-Lima, 1994). Compara-se a matriz de covariância representada no
```
```
modelo estrutural (matriz predita) com a matriz de covariância oriunda diretamente
```
```
das séries temporais (matriz observada). A obtenção dos coeficientes utilizando
```
```
modelos de equações estruturais (SEM – Structural Equation Modelling) implica em
```
assumir que a conectividade efetiva seja constante em toda observação. Este é um
fator limitante, e é incapaz de propiciar abordagens de experiências cujo cerne esteja
```
focado na dinâmica das conectividades neurais (e.g. estudos de aprendizado, de
```
```
plasticidade cerebral, etc) a menos que os dados sejam padronizados, o que leva a
```
perda significativa de informações. Para contornar metodologicamente esta limitação,
```
alguns trabalhos têm proposto parâmetros de regressão variáveis (Buchel and Friston,
```
```
1997, Buchel and Friston, 1998) outros, a aplicação de filtros aos dados (e.g. Filtros
```
```
de kalman (Garbade, 1977) em seus casos especiais (Kalman, 1960)). Se por um lado
```
há a desvantagem na análise por SEM de interpretar o modelo estrutural de forma
estática, por outro a mesma análise é eficiente para comparar o mesmo modelo
anatômico em grupos distintos, como pacientes versus controles.
De forma geral, as equações do modelo estrutural podem ser expressas na
seguinte forma matricial:
Equação 20
```
η ≡ variáveis latentes endógenas (vetor coluna com m elementos)
```
η =α +βη + Γξ +ζ
58
```
ξ ≡ variáveis latentes exógenas (vetor coluna com n elementos)
```
```
ζ ≡ termo residual (vetor coluna com m elementos)
```
```
MÉDIA(ξ)= κ; COVARIÂNCIA(ξ) = Φ
```
```
MÉDIA(ζ)= 0; COVARIÂNCIA(ζ) = Ψ
```
Os termos ξ e ζ são considerados independentes e, portanto, com covariância
```
nula; os parâmetros α, Β e Γ são respectivamente: o termo constante, que pode ser
```
```
eliminado na simplificação do modelo estrutural; os coeficientes estruturais que
```
```
relacionam as variáveis latentes endógenas e; os coeficientes estruturais que
```
relacionam as variáveis latentes exógenas.
```
Isolando η e substituindo (Ι − Β)-1 por Α tem-se que:
```
Equação 21
```
Α ≡ (Ι − Β)-1
```
A média das variáveis latentes endógenas pode ser expressa por:
Equação 22
```
κ ≡ média das variáveis latentes exógenas (ξ)
```
A matriz predita pode ser expressa pela a covariância das variáveis latentes
endógenas representada por:
Equação 23
```
η = A (α + Γξ +ζ )
```
```
μη = A (α + Γκ)
```
59
Γ ≡ coeficientes estruturais relacionados às variáveis latentes exógenas
Φ ≡ covariância das variáveis latentes exógenas
Ψ ≡ covariância dos termos residuais
As equações que representam as variáveis observadas podem ser expressas na
seguinte forma matricial:
Equação 24
```
y ≡ variáveis endógenas observadas (vetor p elementos)
```
```
x ≡ variáveis exógenas observadas (vetor q elementos)
```
```
E(ε)= 0; COV(ε) = Θy
```
```
E(δ)= 0; COV(δ) = Θx
```
A matriz y representa um vetor com p elementos das variáveis endógenas
```
observadas; x representa o vetor com q elementos das variáveis exógenas observadas;
```
```
ε e δ são os erros medidos respectivamente em y e x; τy e τx são termos constantes
```
```
associados respectivamente a y e x; Λy e Λx são os parâmetros das variáveis
```
observadas endógena e exógena.
As médias dessas variáveis são expressas por:
Equação 25
```
COV(η) = A Γ Φ ΓT + Ψ( ) AT
```
```
y =τ y + Λyη +ε
```
```
x =τ x + Λxξ +δ
```
60
μy ≡ média das variáveis endógenas observadas
μy ≡ média das variáveis exógenas observadas
A matriz de variâncias e covariâncias é:
Equação 26
Σ ≡ matriz de covariância predita
```
Esta matriz (Σ), também chamada de “predita”, contém os parâmetros de
```
```
conectividade a serem comparados com a matriz de covariância (S), calculada a partir
```
das séries temporais.
Raros modelos estruturais podem ser resolvidos analiticamente dado que a
inclusão de componentes e de parâmetros, que aproximam o modelo anatômico do
fenômeno neural, incorre na definição de equações de ordem superior. Outra
consequência bastante comum desta inserção é a não convergência dos parâmetros,
nas estimativas baseadas em cálculo numérico. Os modelos estruturais não
convergentes são imprestáveis para solucionar as equações estruturais e,
consequentemente, incapaz de explicar o fenômeno neural. A solução numérica
```
oferecida pelo Máximo Verossímil (ML – Maximun Likelihood) tem sido empregada
```
```
μy =τ y + Λy A (α + Γκ) ;
```
μx =τ x + Λxκ
```
∑yy = Λy [A (ΓΦΓT + Ψ) AT ] ΛyT + Θy ;
```
```
∑xx = ΛxΘΛxT + Θx ;
```
∑yx = ∑xy = Λy AΓΘΛxT
∑ =
∑xx ∑xy
∑yx ∑yy
#
$
%
&
'
```
(
```
61
largamente, mas há outras propostas de soluções numéricas para as equações
estruturais, como quadrados mínimos e a livre distribuição assintótica.
```
A Função de Máximo Verossímil (MLF – Maximun Likelihood Function) é
```
um método estatístico interativo utilizado principalmente para ajustar um modelo
matemático em um conjunto de dados. O método consiste em estimar o valor que
```
maximiza a função de densidade de probabilidade (PDF – Probability Density
```
```
Function) para um valor que faz os dados observados mais parecidos.
```
Sejam os dados representados por um vetor Y com m medidas independentes
entre si. Considere que as medidas seguem distribuição gaussiana com média μ e
variância σ2. Matematicamente pode-se escrever:
Equação 27
```
Y = y1, y2, y3, ... , ym( ) ≈ Nμ,σ 2( )
```
```
N(μ,σ2) ≡ Distribuição normal
```
```
μ ≡ Média;σ2 ≡ variância
```
```
Y ≡ vetor representando as medidas (eventos)
```
yi ≡ eventos independentes
m ≡ número total de eventos
```
Seja p(Y | μ, σ2) a função densidade de probabilidade que especifica a
```
probabilidade de encontrar os dados Y para determinados parâmetros μ e σ2. Pode-se
escrever a função como:
Equação 28
62
```
p y( ) = 1
```
σ 2π
```
exp − y −μ( )
```
2
2σ 2
p ≡ Função densidade de probabilidade normal
```
Como cada evento (yi) é estatisticamente independente entre si e, de acordo
```
com a teoria da probabilidade, a função da densidade de probabilidade do vetor Y, ou
```
seja, p(Y), pode ser expressa como a multiplicação das densidades de probabilidades
```
de cada evento. Portanto:
Equação 29
```
p y = y1 , y 2 , y 3 , ... , y m( ) |μ,σ 2( ) = p y1 |μ,σ 2( ) p y 2 |μ,σ 2( ) p y 3 |μ,σ 2( ) ... p y m |μ,σ 2( ) = p y i |μ,σ 2( )
```
```
i=1
```
m
∏
p ≡ Função densidade de probabilidade normal
Na prática, tem-se um conjunto de eventos, sob os quais se deseja estimar os
parâmetros μ e σ2 de uma população, em uma função específica, ou seja, tem-se o
problema inverso ao apresentado nas Equações 27, 28 e 29. A função que descreve
```
esse problema inverso é denominada Função de Máximo Verossímil (MLF),
```
representada matematicamente por:
Equação 30
```
Lμ,σ 2 | Y( ) = p Y |μ,σ 2( ) = p y i |μ,σ 2( )
```
```
i=1
```
m
∏
```
L(μ,σ2 | Y) ≡ Função de máximo verossímil (MLF)
```
Ambas as funções, PDF e MLF, tratam dos mesmos elementos, entretanto, os
parâmetros em uma são os eventos da outra. Ademais, as duas funções são definidas
63
em abscissas diferentes, por isso não são diretamente comparáveis. Especificamente,
por um lado a PDF é uma função que descreve o comportamento dos eventos para um
dado conjunto de parâmetros. Por outro lado, a MLF é uma função que descreve o
comportamento dos parâmetros dado um conjunto de elementos. Esta função é
```
definida na escala (abscissa) dos parâmetros enquanto aquela na escala dos dados.
```
Extraindo o logaritmo neperiano na Equação 30, a fim de converter a função
produtória em somatória, tem-se que:
Equação 31
ln L = ln pi = ln pi
```
i=1
```
m
∑
```
i=1
```
m
∏
```
L ≡ Função de máximo verossímil (MLF)
```
```
As funções ln L (log-likelihood) e L são monotonicamente relacionadas entre
```
si, e por isso, a maximização de uma refere-se também à outra. Assumindo que a
função log-likelihood seja diferenciável, somente se existir um conjunto de
```
parâmetros (w) que satisfaçam a seguinte equação diferencial:
```
Equação 32
```
∂ ln L w | Y( )
```
∂ w j
= 0
w ≡ Conjunto de parâmetros
j ≡ índice de parâmetros
O ponto de inflexão obtido pela Equação 32 pode ser de mínimo ou de
máximo, assim faz-se necessário impor uma segunda condição para garantir que o
ponto de inflexão almejado seja de máximo.
64
Equação 33
```
∂2 ln L w | Y( )
```
∂ w j2
< 0
w ≡ Conjunto de parâmetros
j ≡ índice de parâmetros
Na prática, nem sempre é possível obter analiticamente a solução das
Equações 32 e 33, como por exemplo, quando os modelos envolvem muitos
parâmetros. Nestes casos, a PDF geralmente é ‘muito não-linear’. Para se estimar os
parâmetros nestas ocasiões, faz-se uso de processos numéricos como sucessivas
interações.
Portanto, a comparação entre Σ e S é feita pela escolha interativa dos
parâmetros em Σ que maximizam o valor ML da seguinte equação:
Equação 34
```
trace ≡ soma dos elementos da diagonal principal;
```
p ≡ número de variáveis medidas
O método da SEM é uma técnica cuja característica principal é confirmatória
```
(não exploratória). Sua aplicação em fMRI é comumente empregada com a
```
eliminação dos termos latentes da equação geral acima apresentada, preservando
apenas os termos observados e suas respectivas relações. Esta simplificação é
conhecida como Path Analysis.
```
ML = ln Σ( ) - ln S( ) - trace SΣ-1( ) - p
```
65
```
Modelagem causal dinâmica (DCM – Dinamc Causal Modelling)
```
Outra forma de caracterizar os parâmetros de conectividade é através da
```
modelagem causal dinâmica (DCM – Dinamic Causal Modelling) (Friston et al.,
```
```
2003). O DCM faz distinção entre os níveis neuronal e hemodinâmico, modelando as
```
interações de populações de neurônio, no nível cortical, a partir de séries temporais
```
(hemodinâmica – no fMRI, ou eletrofisiológicas – no EEG). Essa tarefa é realizada
```
com o auxílio de modelos suplementares que sugerem a forma de como a atividade
neuronal é transformada na resposta medida, permitindo que os parâmetros do modelo
neuronal sejam estimados através dos dados observados. Esquematicamente, a
```
informação flui partindo dos estímulos de entrada (input) – constituídos por funções
```
```
convencionais codificadas no desenho experimental, passando ao estado neural (state)
```
– representado pelas atividades neuronais e outras variáveis neurofisiológicas e
```
biofísicas e, finalmente, sendo medidas (output). Os estímulos de entrada induzem
```
respostas neurais de duas formas. Primeira, eles podem induzir respostas através de
```
influências diretas sobre uma região de interesse no modelo estrutural (estímulo
```
```
intrínseco). Segunda, eles podem modular conexões existentes no modelo estrutural
```
```
(estímulo contextual) (Friston and Buchel, 2000). Ao se observar mudanças de
```
conectividade em função de um longo período de tempo, pode-se obter a outra
vantagem do método: a medida indireta de plasticidade neural. A classe de estímulos
contextuais emula respostas claramente não lineares cuja modelagem, nas equações
do DCM, são representadas por aproximações em sistemas bilineares.
Resumidamente, o DCM é um procedimento de identificação de padrões em sistemas
não-lineares usando a estimativa Bayesiana em parâmetros de um sistema dinâmico e
determinista tipo input-state-output.
66
Matematicamente, as equações de estado neuronal são definidas como:
Equação 35
z ≡ conjunto de estados neuronais
zi ≡ estado neuronal da região i
```
i ≡ número total de regiões (nós no modelo estrutural)
```
Como o DCM é um método dinâmico, a derivada temporal do conjunto dos
```
estados neuronais (z) recai na função neuronal que será aproximada. Portanto:
```
Equação 36
F ≡ Função neuronal não linear
u ≡ inputs
θ ≡ Parâmetros
A função F é a função não-linear que descreve a influência neurofisiológica
```
sofrida pelo conjunto de regiões (z) e estímulos externos (u). Os parâmetros expressos
```
em θ são utilizados na inferência bayesiana. Como, a função F será aproximada da
equação bilinear, as componentes z, u e θ serão novamente parametrizados em
termos de conectividade efetiva. A aproximação bilinear pode ser expressa por:
Equação 37
```
z = z1, z2, z3, ... , zi[ ]
```
T
∂ z
∂ t
= z
•
```
= F z, u,θ( )
```
67
```
A ≡ Parâmetros de conectividade intrínsecos (na ausência de inputs)
```
```
B ≡ Parâmetros de conectividade modulatória (regulam as conexões)
```
```
C ≡ Parâmetros de conectividade extrínsecas (associadas diretamente aos inputs)
```
j ≡ Número de inputs
Os parâmetros A, B e C podem ser obtidos a partir das seguintes derivadas
```
parciais: x
```
Equação 38
```
A ≡ Parâmetros de conectividade intrínsecos (na ausência de inputs)
```
```
B ≡ Parâmetros de conectividade modulatória (regulam as conexões)
```
```
C ≡ Parâmetros de conectividade extrínsecas (associadas diretamente aos inputs)
```
A pode ser entendida como o acoplamento intrínseco entre as regiões cerebrais
na ausência de inputs. Pela Equação 38 pode-se observar que A representa a
conectividade de primeira ordem. B representa o conjunto dos parâmetros que
modificam as conectividades intrínsecas. Com a Equação 38 observa-se que a
z
•
```
≈ Az + uj Bj z + Cu∑ = A + uj Bj∑( ) z + Cu
```
```
A =
```
∂ F
∂ z
=
∂ z
•
∂ z
```
;
```
```
Bj =
```
∂2 F
∂x∂uj
=
∂
∂uj
∂ z
•
∂ x
```
;
```
```
C =
```
∂ F
∂ u
68
obtenção destes parâmetros pode ser feita pela derivada de segunda ordem. C
representa o conjunto de parâmetros associados diretamente aos inputs que levam a
atividade neuronal. O conjunto dos parâmetros A, B e C, ou simplesmente matriz de
acoplamento θc, define a arquitetura e as interações no nível neuronal a serem
estimadas.
Esse três níveis de conectividade cerebral podem ser utilizados para explorar
diversas condições neuropsiquiátricas e podem constitui-se em um importante
marcador para esses transtornos. O potencial dessas técnicas eleva-se ainda mais por
serem metodologias não invasivas e com poucas contra indicações. Esses conceitos
tomados conjuntamente, motivaram o desenvolvimento dessas técnica no intuito de se
observar padrões ainda não conhecidos de diversas doenças cerebrais e transtornos
mentais.
69
OBJETIVOS
70
Objetivos Gerais:
• Estudar e estimar conectoma cerebral com imageamento por ressonância
magnética nuclear
• Modelar interações cerebrais em distintas condições cerebrais e mentais
Objetivos Específicos:
• Correlacionar mapas estáticos de ressonância magnética funcional e de
```
conectividade anatômica, funcional e efetiva;
```
• Estabelecer metodologia inovadora para aquisição, processamento e análise de
```
fMRI, acMRI, fcMRI e ecMRI;
```
• Estimar mapas de conectividade e comparar grupos de indivíduos controle e
pacientes com epilepsia mesial temporal unilateral para as tarefas:
```
! Memória verbal (codificação, reconhecimento e evocações imediata e tardia);
```
```
! Memória visual (codificação, reconhecimento e evocações imediata e tardia) e
```
```
! Repouso (resting state)
```
• Avaliar a conectividade nas regiões mediais temporais com dependência do
envelhecimento e codificação de palavras com conteúdo emocional positivas,
negativas e neutras.
• Estimar mapas de conectividade anatômica e comparar grupos de controles,
sujeitos idosos com depressão e pacientes portadores de mutação no gene SPG11.
• Comparar mapas de conectividade de sujeitos controles, pacientes com doença de
Alzheimer e déficit cognitivo leve e correlacionar esses mapas com perfis
neuropsicológicos.
71
METODOLOGIA
72
Em razão de cada experimento deter métodos e resultados específicos, ambas as
etapas serão descritas em cada experimento. O trabalhos que se tornaram artigos publicados
em revistas indexadas são apresentados na sequência.
Experimento 1 – Conectividade efetiva: SEM aplicado à plasticidade etária e
codificação de palavras com conteúdos emocionais.
MATERIAIS E MÉTODOS
Sujeitos
```
Participaram deste trabalho 44 indivíduos adultos sadios (22 mulheres) idade média
```
```
de 21,98±3,82 e 23 sujeitos mais velhos sadios (15 mulheres) idade média de 71,91±7,06.
```
Rastreou-se a existência de eventos patológicos de ordens neurológica, cardiovascular ou
```
presença de depressão. A média do inventário de depressão de Beck (Beck Depression
```
```
Inventory - BDI)(Beck, 1979) foi estimada em 1,31±1,98 para os indivíduos adultos jovens,
```
```
enquanto a escala de depressão geriátrica (Geriatric Depression Scale – GDS) (Yesavage et
```
```
al., 1983, Sheikh et al., 1991) foi calculada em 2,72±2,32 para os sujeitos mais velhos. A
```
média de escolaridade foi de 14,94±1,92 nos jovens e de 17,09±2,22 nos mais velhos. Testes
de vocabulário foram aplicados aos participantes. Os adultos jovens obtiveram a pontuação
média de 56,71±5,71 enquanto os adultos mais velhos pontuaram a média de 57,74±4,59.
Nenhum participante estava sob a administração de medicamentos que comprometesse
funções cognitivas ou de atenção.
Ética
Os participantes receberam o termo de consentimento para fazerem parte do estudo e
```
foram pagos em $25,00 (vinte e cinco dólares) por hora pelo tempo empregado despendido
```
no experimento. O estudo foi revisado e aprovado pelo comitê sobre uso de humanos como
73
```
sujeitos experimentais (Committe on the Use of Humans as Experimental Subjects –
```
```
COUHES) do Instituto de Tecnologia de Massachusetts (Massachusetts Institute of
```
```
Technology – MIT).
```
Aquisição de dados
```
Imagens em eco planar (EPI) foram coletadas utilizando o sistema Trio 3T da
```
Siemens em dimensões isotrópicas de 5mm, FOV 200x200, tempo de repetição 2000ms e
tempo de eco 30ms.
Codificação
```
Foram extraídas 324 palavras das “normas afetivas de palavras inglesas” (The
```
```
affective norms for engish words - ANEW)(Bradley and Lang, 1999) cujo conteúdo
```
```
emocional poderia ser classificado exclusivamente como negativo (102 palavras), neutro (116
```
```
palavras) ou positivo (102 palavras); formando 2 conjuntos, cada um com 52, 58 e 52
```
palavras respectivamente aos conteúdos emocionais relacionados. Durante a codificação,
```
cada participante viu um dos grupos de 162 palavras (52 negativas, 58 neutras e 52 positivas).
```
Adicionalmente, 16 palavras foram utilizadas para intercalar eventos e controlar os efeitos de
apresentações recentes. Os participantes compuseram um dos 8 grupos para realizarem a
tarefa de codificação, ilustrados pela Figura 10.
Codificação 1
NEU
POS Conjunto 1
Conjunto 2
Conjunto 2NEG
Codificação 2
NEU
POS Conjunto 1
Conjunto 1
NEG Conjunto 2
Codificação 3
NEU Conjunto 2
POS Conjunto 1
Conjunto 1NEG
Codificação 4
NEU
POS Conjunto 2
Conjunto 2
Conjunto 2NEG
Codificação 5
NEU
POS Conjunto 1
Conjunto 1
Conjunto 1NEG
Codificação 6
NEU
POS Conjunto 2
Conjunto 2
Conjunto 1
NEG
Codificação 7
NEU
POS Conjunto 2
Conjunto 2
NEG Conjunto 1
Codificação 8
NEU
POS Conjunto 2
Conjunto 1
Conjunto 1NEG
74
```
Figura 10 – Oito grupos de codificação de palavras com conteúdo emocional (positiva, neutra ou
```
```
negativa), fracionados em dois conjuntos.
```
As palavras foram projetadas dentro da bobina do aparelho de ressonância magnética
e visualizadas através de um espelho colocado sobre a bobina de crânio. O teste foi
fracionado em duas aquisições com 81 palavras, respeitando o tamanho e a freqência no
idioma inglês. As palavras foram apresentadas durante dois segundos para os indivíduos
jovens e de três segundos para os adultos mais velhos. Foi solicitado aos participantes para
julgarem as palavras em concretas, abstratas ou incertas com o propósito de intensificar a
codificação. Os participantes manifestaram esse julgamento a partir de um botão colocado em
sua mão direita. A ordem de apresentação das palavras foi randomizada. Solicitou-se aos
indivíduos lembrarem das palavras pois estes seriam testados mais tarde em outro
experimento.
Pré-processamento das imagens funcionais
Todas as imagens foram pré-processadas com o software FreeSurfer
```
(www.surfer.nmr.mgh.harvard.edu) associado ao software FSL (www.fmrib.ox.ac.uk/fsl/) de
```
```
acordo com os seguintes passos: correção de movimento por modelo de corpo rígido (Singh
```
```
et al., 1998); normalização espacial para o padrão do MNI (Carmack et al., 2004) e
```
suavização espacial com função gaussiana tridimensional de FWHM de 10mm. O pré-
processamento objetivou a preparação das imagens individuais para que possam alimentar a
comparação os entre grupos.
Análise dos dados
```
Definição dos volumes anatômicos de interesse (AVOI)
```
```
Foram criados mapas probabilísticos estruturais (Fischl et al., 2004, Fischl et al.,
```
75
```
2008, Fischl et al., 2002, Deskan et al., 2006), de ambos os hemisférios, das estruturas
```
apresentadas na Tabela 1 e ilustradas na Figura 11.
```
Figura 11 – Ilustração de substâncias cinzenta (A) e branca (B) seguimentadas pelo programa
```
76
Freesurfer.
Tabela 1: Lista das estruturas seguimentadas no FreeSurfer
Regiões parceladas no FreeSurfer
LÓBO TEMPORAL LÓBO PARIETAL
Superfície medial Giro pós-central
córtex entorhinal Giro supramarginal
giro parahipocampal córtex parietal superior
pólo temporal córtex parietal inferior
giro fusiforme córtex percuneus
Superfície lateral
giro temporal superior LÓBO OCIPITAL
giro temporal médio Giro lingual
giro temporal inferior córtex pericalcanino
córtex temporal transverso córtex do cúneos
córtex ocipital lateral
LÓBO FRONTAL
giro frontal superior OUTRAS ESTRUTURAS
giro frontal médio giro do cíngulo
parte rostral divisão rostral anterior
parte caudal divisão caudal anterior
giro frontal inferior divisão posterior
parte opercular divisão do ístimo
parte triangular tálamo
parte orbital núcleo caudato
córtex orbitofrontal núcleo putamen
divisão lateral núcleo pálido
divisão médial hipocampo
pólo frontal amídala
giro pré-central
lóbulo paracentral
```
Rotinas desenvolvidas em Matlab (www.mathworks.com) foram desenvolvidas para
```
```
calcular a componente principal (PCA) em cada volume anatômico de interesse (AVOI)
```
```
(Wang et al., 2006). Cada vetor, relacionado univocamente com uma das estruturas descritas
```
```
na tabela 1, foi utilizado para na regressão de quadrados mínimos parcial (parrtial least
```
```
squere – PLS) (Rayens and Andersen, 2006) para cada indivíduo separadamente. As duas
```
77
estruturas mais significativamente correlacionadas foram os hipocampos e as amídalas. Esses
quatro vetores foram utilizados como semente na estimativa dos parâmetros de conectividade
efetiva.
Modelo anatômico de conectividade efetiva
Guiados pelo resultados obtidos pela aplicação da técnica de PLS, definiu-se o
modelo anatômico de inter-relação hipocampo-amídala, ipsilateral em ambos os hemisférios
```
(Figura 12) . Os parâmetros de conectividade efetiva foram estimados através da técnica de
```
```
modelagem de equação estrutural (Structural Equation Modelling – SEM) (Astolfi et al.,
```
```
2004) utilizando o programa Lisrel versão 8.8 (www.ssicentral.com).
```
Figura 12 – Modelo anatômico utilizado na modelagem de equação estrutural para se estimar os
```
parâmetros de conectividade (de par.1 a par.4) entre os hipocampos e amídalas.
```
RESULTADOS
```
Foram encontrados basicamente três importantes resultados. Primeiro; verificou-se
```
que os parâmetros de conectividade efetiva, na direção das amídalas para os hipocampos
ipsilaterais, alcançaram valores superiores àqueles em sentido contrário, sugerindo o
```
predomínio da influência das amídalas sobre o hipocampo, em ambos os grupos (jovens e
```
D
78
```
mais velhos sadios), durante a tarefa com conteúdo emocional (Gallagher and Chiba, 1996).
```
```
Segundo; quantitativamente, a influência dos hipocampos sobre as amídalas foi
```
significativamente maior no grupo de indivíduos jovens que no grupo de indivíduos mais
```
velhos. Terceiro; ao se comparar os parâmetros de conectividade nos hemisférios esquerdo e
```
direito, percebeu-se não haver diferença significativa entre ambos os hemisférios para o
grupo de indivíduos jovens enquanto uma significativa distinção ocorreu nos indivíduos mais
velhos, cujos parâmetros de conectividade expressaram-se maiores à direita. Esses resultados
estão ilustrados na Figura 13 abaixo.
```
Figura 13 –Parâmetros de conectividade entre os hipocampos e amídalas (ipsilaterais) nos grupos
```
```
de indivíduos jovens e indivíduos mais velhos. (*p<0.001)
```
D
79
Experimento 2 – Conectividade efetiva: SEM aplicado a epilepsia de lobo temporal
medial esquerdo com codificação de palavras neutras e abstratas
MATERIAIS E MÉTODOS
Sujeitos
```
Participaram deste trabalho 7 indivíduos com ELTM esquerda (6 mulheres; idade
```
```
média de 38,57±8,75; escolaridade média de 9,57±3,55) e 7 indivíduos controles (5
```
```
mulheres; idade média de 33,00±10,75; escolaridade média de 10,67±4,59). Os pacientes
```
foram selecionados com base em evidências clínicas, exames físicos e por investigações por
MRI e EEG. O diagnóstico de epilepsia foi baseado no critério da liga internacional contra
```
epilepsia (ILAE) (ILAE, 1989). Investigou-se a lateralização das crises com bases na história
```
clínica, exames de EEG interictal e vídeo-EEG. Para constituírem o grupo de pacientes com
ELTM esquerda, crises consistentes com a lateralização foram observadas em pelo menos 6
EEGs interictais e 2 crises no vídeo-EEG. Ademais, análises visuais de imagens estruturais
```
em RM demonstraram atrofia hipocampal unilateral (Wieser, 2004) à esquerda, bem como
```
sinais de esclerose hipocampal unilateral também à esquerda. Os pacientes foram
considerados refratários à medicação. O grupo controle foi constituído de indivíduos sem
prévias manifestações anormais neurológicas nem cardíacas.
Ética
Todos os participantes do trabalho receberam orientações pertinentes aos riscos
potenciais e às contra-indicações, bem como assinaram o termo de consentimento
apresentado no Anexo A, que foi aprovado pelo comitê da ética da faculdade de ciências
```
médicas (CEP/FCM/UNICAMP) em 4 de dezembro de 2006, no parecer número 678/2006 e
```
```
no certificado de apresentação para apreciação de ética (CAAE) de número 0546.0.146.000-
```
80
06. Concomitante à aquisição dos dados de RM, uma equipe formada por uma neurologista,
uma psicóloga, uma enfermeira e uma biomédica colocava-se à disposição para eventuais
ocorrências com os indivíduos.
Aquisição de dados
```
Foram coletadas imagens funcionais em protocolo de eco planar (EPI) utilizando o
```
```
sistema Prestige da Elscint 2T. Cada volume foi composto de 20 cortes axiais (interleaved
```
```
botton-up) com FOV (Field of View) de 3x3mm, espessura de 6mm sem gap, ângulo de
```
excitação de 90º, matriz de 128x72, TR de 2s e TE de 45ms.
Imagens estruturais, ponderadas por T1, foram adquiridas no mesmo sistema de
ressonância, em cortes sagitais isotrópicos de 1mm sem gap, utilizando sequência de pulso
em gradiente eco com TR de 22ms, TE de 9ms, ângulo de excitação de 35º e matrix 256x256.
Simultaneamente à aquisição das imagens funcionais, foram coletados dados de EEG
com resolução de 32 canais e alta frequência de amostragem.
Durante a aquisição das imagens funcionais, foi solicitado ao individuo a realização
de uma determinada tarefa, cujo resultado era expresso através de um botão, colocado na mão
direita deste indivíduo. Deste modo, a recepção das respostas emitidas durante o exame fez
parte da etapa de aquisição dos dados.
Paradigmas
```
As aquisições das imagens funcionais foram particionadas em duas etapas (com
```
```
intervalos de tempo idênticos) em referência ao material específico a ser investigado. Na
```
primeira etapa, buscou-se investigar aspectos de memória verbal enquanto na segunda, de
memória visual. Nesta, utilizou-se figuras abstratas em preto e branco, naquela, a
intermediação foi alcançada com uso de palavras abstratas, sendo projetadas em letras
brancas com fundo preto. Cada etapa foi adquirida de forma ininterrupta. Didaticamente,
81
```
dividiu-se cada etapa em três fases: 1) uma aquisição de codificação e evocação imediata; 2)
```
```
5 aquisições em resting state e 3) uma aquisição de evocação tardia e reconhecimento. Entre
```
as duas etapas, o indivíduo era retirado da máquina de RM para um breve descanso de 30
minutos e para ajustar as impedâncias do sistema de EEG, que foi acoplado no início da
aquisição. Após este intervalo, o indivíduo retornava à máquina de RM para prosseguir com
as aquisições da segunda etapa. Cada etapa durou 47 minutos e 14 segundos,
desconsiderando o breve intervalo entre as aquisições.
Memória verbal: codificação e evocação imediata
A Figura 14 ilustra o paradigma desenvolvido nesta fase.
Codificação
OFF
```
Tempo (s)
```
Imagens saturadas
Linha de base
Não-palavra
Palavra Evocação verbal
Figura 14 – Paradigma de codificação e evocação imediata para memória verbal.
```
Apenas uma aquisição (run) foi obtida em cada indivíduo, de acordo com a seguinte
```
```
ordem: 5 volumes iniciais, a serem descartados no processo de análise (Saturadas); 39
```
```
volumes, sem que o indivíduo desempenhe tarefa a ele sugerida (OFF); 5 repetições, cada
```
uma contendo 17 volumes, com apresentação visual de uma não-palavra intercalada com 4
repetições de 17 palavras. A taxa de apresentação das palavras foi de 2 segundos por palavra
82
enquanto uma única não-palavra estimulou o indivíduo por 34 segundos em cada
```
apresentação. O processo de codificação totalizou 153 volumes (Codificação). A lista das
```
palavras e a não-palavra estão apresentadas na Tabela 2. Seguiu-se com a aquisição de 60
volumes que objetivaram dois itens, primeiro, o completo decaimento da resposta
hemodinâmica originada com a tarefa de codificação e segundo, a promoção de um pequeno
intervalo de tempo para evitar conflitos entre codificação e evocação. Por fim, uma fraca
mensagem luminosa, com duração de 2 segundos, solicitava do participante o início da tarefa
de evocação imediata, a qual se estendeu por 30 volumes. Durante toda esta fase foram feitos
os registros de EEG dos indivíduos participantes. A fase de codificação e evocação imediata
durou 9 minutos e 34 segundos.
Tabela 2: Lista de palavras e não-palavra utilizada na emulação de memória verbal
Palavras utilizadas
na codificação
Palavras utilizadas
no reconhecimento
Não-palavra utilizada
na codificação e
reconhecimento
HONRA ACASO FAVOR SERVIÇO ARLTIP
OPINIÃO SIMPATIA TEORIA MORAL
PROBLEMA ORGULHO VALOR FAMA
DEVER DECISÃO RAZÃO SERMÃO
INTERESSE CRITÉRIO EXAME DEFESA
PACIÊNCIA SISTEMA LUXO LEALDADE
ALMA VIDA SEGREDO PROSA
LEI MÉTODO ASPECTO ORDEM
OPÇÃO ESQUEMA
Memória verbal: resting state
A Figura 15 explica o paradigma utilizado nesta segunda fase.
83
Resting state
```
Tempo (s)
```
Imagens saturadas Linha de base
Figura 15 – Paradigma de resting state.
Imediatamente após a fase de codificação e evocação imediata, foram realizadas 5
```
aquisições (runs) em resting state de cada indivíduo. Os 5 volumes iniciais de cada aquisição
```
```
(Saturadas) foram obtidos com o propósito de serem descartados na análise dos dados. Os
```
```
180 volumes restantes (Resting state) foram adquiridos sem que o indivíduo desempenhasse
```
alguma tarefa a ele sugerida e sem receber qualquer estímulo externo. Igualmente à fase
anterior, registros de EEG foram obtidos simultaneamente com a aquisição das imagens em
EPI. A fase de resting state, que inclui as 5 aquisições, durou 30 minutos e 50 segundos,
desconsiderando o breve intervalo entre uma e outra aquisição.
Memória verbal: evocação tardia e reconhecimento
A Figura 16 descreve o paradigma aplicado nesta terceira fase
84
SaturadasOFF
ReconhecimentoEstímulo neutroUso do botãoEvocação tardia
```
Tempo (s)
```
010156190250254390
Ajuste
410
Imagens saturadas
Linha de base
Não-palavra
Evocação verbal
Reconhecimento verbal
Figura 16 – Paradigma de evocação tardia e reconhecimento.
```
Uma única aquisição (run) foi obtida para cada indivíduo, de acordo com a seguinte
```
```
sequência: 5 volumes iniciais, descartados durante a análise dos dados (Saturadas); 73
```
```
volumes, sem que o indivíduo desenvolvesse alguma tarefa a ele sugerida (OFF); 17 volumes
```
com a apresentação visual da mesma não-palavra apresentada na primeira fase – descrita na
```
Tabela 2, (Estímulo neutro); 30 volumes adquiridos, sem estímulo externo, em que o
```
indivíduo tentava recuperar as palavras a ele apresentadas durante a fase de codificação
```
(Evocação tardia); 2 volumes coletados durante o momento em que o participante recebia
```
uma mensagem, com fraca luminosidade, informando que deveria apertar o botão que foi
previamente colocado em sua mão direita, quando reconhecesse uma palavra da lista
```
apresentada durante a codificação (Uso do botão); seguiu-se com a obtenção de 68 volumes
```
```
dos quais o participante respondia afirmativamente (apertando o botão) caso a palavra
```
```
projetada pertencesse à lista de palavras da primeira fase (Reconhecimento). A taxa de
```
apresentação das palavras foi de 1 a cada 2 segundos, o que totalizou 34 palavras
```
apresentadas, 17 destas compunham a lista inicial (da primeira fase) enquanto as demais
```
85
representam nova lista. Para evitar adaptação, a ordem de apresentação das palavras, de
ambos as listas, foi randomizada. A Tabela 2 contém ambas as listas de palavras. Por fim,
seguiu-se com a aquisição de 10 volumes sem que o indivíduo recebesse alguma estimulação
```
externa nem que desempenhasse alguma tarefa (Ajuste). Estes 10 volumes finais objetivaram
```
o completo decaimento da resposta hemodinâmica originada com o reconhecimento. Durante
toda esta fase foram feitos os registros de EEG. Esta fase durou 6 minutos e 50 segundos.
Memória visual: codificação e evocação imediata
A Figura 17 ilustra o paradigma desenvolvido nesta fase.
Codificação
EvocaçãoImediata
Descanso
Saturadas
OFF
```
Tempo (s)
```
01088122156190224258292326360394514574
Imagens saturadas
Linha de base
Não-figura
Figura Evocação visual
Figura 17 – Paradigma de codificação e evocação imediata para memória visual.
```
Apenas uma aquisição (run) foi obtida para cada indivíduo, de acordo com a seguinte
```
```
ordem: 5 volumes iniciais, descartados na análise (Saturadas); 39 volumes, sem que o
```
```
indivíduo desempenhasse alguma tarefa a ele sugerida (OFF); 5 repetições, cada uma
```
```
contendo 17 volumes, com apresentação visual de uma “não-figura” (cruz) intercalada com 4
```
repetições de 17 figuras. A taxa de apresentação das figuras foi de 2 segundos para cada
86
figura enquanto a única “não-figura” estimulou o indivíduo por 34 segundos em cada
```
apresentação. O processo de codificação totalizou 153 volumes (Codificação). A lista das
```
figuras e da “não-figura” está apresentada na Tabela 3.
Seguiu-se com a aquisição de 60 volumes que objetivaram o completo decaimento da
resposta hemodinâmica originada com a tarefa de codificação bem como a promoção de um
pequeno intervalo de tempo para evitar conflitos entre codificação e evocação. Por fim, uma
fraca mensagem luminosa solicitava do participante o início da tarefa de evocação imediata, a
qual se estendeu por 30 volumes. Em toda esta fase, que durou 9 minutos e 34 segundos,.
foram feitos registros de EEG.
Tabela 3: Lista de figuras e “não-figura” utilizada na emulação de memória visual
Figuras utilizadas
na codificação
Figuras utilizadas
no reconhecimento
“Não-figura” utilizada
na codificação e
reconhecimento
Memória visual: resting state
87
Esta etapa foi idêntica àquela relatada na fase de resting state durante a etapa de
memória verbal. Ilustrado na Figura 15.
Memória visual: evocação tardia e reconhecimento
A Figura 18 descreve o paradigma aplicado nesta terceira fase
SaturadasOFF
ReconhecimentoEstímulo neutroUso do botãoEvocação tardia
Ajuste
```
Tempo (s)
```
010156190250254390410
Imagens saturadas
Linha de base
Não-figura
Evocação visual
Reconhecimento visual
Figura 18 – Paradigma de evocação tardia e reconhecimento.
```
Uma única aquisição (run) foi obtida em cada indivíduo, de acordo com a seguinte
```
```
sequência: 5 volumes iniciais, descartados durante a análise dos dados (Saturadas); 73
```
```
volumes, sem que o participante desenvolvesse alguma tarefa a ele designada (OFF); 17
```
```
volumes com a apresentação visual da mesma “não-figura” (cruz) apresentada na primeira
```
```
fase – descrita na Tabela 3, (Estímulo neutro); 30 volumes adquiridos, sem estímulo externo,
```
em que o indivíduo tentava recuperar as figuras a ele apresentadas durante a fase de
```
codificação (Evocação tardia); 2 volumes coletados durante o momento em que o participante
```
88
recebia uma mensagem, com fraca luminosidade, informando que deveria apertar o botão,
```
quando reconhecesse uma figura da lista apresentada durante a codificação (Uso do botão);
```
seguiu-se com a obtenção de 68 volumes, dos quais, o participante respondia afirmativamente
```
(apertando o botão) caso a figura projetada pertencesse à lista da primeira fase
```
```
(Reconhecimento). A taxa de apresentação das figuras foi de uma a cada 2 segundo, o que
```
```
totalizou 34 figuras apresentadas, 17 destas compunham a lista inicial (da primeira fase)
```
enquanto as demais representam nova lista. Para evitar adaptação, a ordem de apresentação
das figuras, de ambos as listas, foi embaralhada. A Tabela 3 contém ambas as listas de
figuras. Por fim, seguiu-se com a aquisição de 10 volumes sem que o indivíduo recebesse
```
alguma estimulação externa e nem que desempenhasse alguma tarefa (Ajuste). Estes 10
```
volumes finais objetivaram o completo decaimento da resposta hemodinâmica originada com
o reconhecimento. Durante toda esta fase, que durou 6 minutos e 50 segundos, foram feitos
registros de EEG.
Pré-processamento das imagens funcionais
As imagens funcionais foram coletadas no espaço k, reconstruídas para espaço
```
anatômico (Mccoll et al., 1992) utilizando rotinas locais desenvolvidas no software matlab
```
```
(www.matworks.com) e reordenadas em formato DICOM. Posteriormente foram convertidas
```
```
para o formato ANALYZE utilizando o software MRIcro (www.sph.sc.edu/comd/rorden). Os
```
5 primeiros volumes de cada aquisição foram descartados dos processamentos seguintes.
```
Utilizando o software SPM5 (www.fil.ion.ucl.ac.uk/spm) as imagens foram orientadas
```
```
temporalmente (slice timing), realinhadas com o modelo de corpo rígido (Singh et al., 1998),
```
```
normalizadas para o espaço padrão do MNI (Carmack et al., 2004) e suavizadas
```
espacialmente com função gaussiana tridimensional de FWHM de 6mm.
Análise dos dados
89
```
Definição dos volumes anatômicos de interesse (AVOI)
```
A análise de grupo dos dados de fMRI dos controles, considerando o contrate na fase
de codificação da etapa de memória verbal, revelou áreas frontais e temporais como regiões
```
significativamente correlacionadas ao paradigma expresso na Figura 14 (p<0,001 com
```
```
correção de Bonferroni). Com o atlas binário automated anatomical labeling – AAL
```
```
(Tzourio-Mazoyer et al., 2002), provido pelo software MRIcro, foram selecionadas as
```
```
seguintes regiões no hemisfério esquerdo: hipocampo (HIP), giro parahipocampal (PHIP),
```
```
giro frontal médio (F2), porção opercular do giro frontal inferior (F3-Oper) e porção
```
```
triangular do giro frontal inferior (F3-Triang). A seguir, rotinas escritas em matlab
```
permitiram extrair a série temporal de maior significância em cada uma destas regiões para
cada indivíduo.
Conectividade funcional e modelo estrutural
A conectividade funcional intra e inter-regiões frontais e temporais foi estabelecida
calculando-se o índice de correlação de peason das séries temporais das AVOIs, duas a duas.
A média dos valores de conectividade funcional, estimada no grupo controle, foi utilizada
para desenhar o modelo estrutural apresentado na Figura 18. Os valores dos parâmetros de
conectividade efetiva deste modelo estrutural foram estimados utilizando o software Lisrel.
HIP
PHIP
F3-triang F3-oper
F2
90
Figura 19 – Modelo estrutural de conectividade efetiva inter e intra-regiões frontais e mesiais
temporais no hemisfério esquerdo para codificação de memória verbal.
RESULTADOS
Foram encontrados resultados de duas ordens que diferenciam o grupo de controles
do grupo de indivíduos com ELTM esquerda durante a codificação de palavras. A primeira
diferença foi detectada em termos de conectividade funcional. Nos controles, o padrão de
conectividade funcional entre as regiões frontais e mesiais temporais expressaram valores
negativos, enquanto nos pacientes, esse padrão foi expresso positivamente. A tabela 4
apresenta todos os resultados de conectividade funcional estabelecidos entre as AVOIs de
ambos os grupos de indivíduos.
Tabela 4 – Parâmetros de conectividade funcional estimados entre regiões frontais e mesiais
```
temporais para os grupo de controles (azul) e de pacientes com ELTM esquerda (vermelho).
```
HIP PHIP F3-oper F2
68±18HIP
PHIP
F3-oper
F2
-21±29
F3-triang
-19±18
-13±33
-14±20
88±09
-32±31
-26±26
60±22
47±28
71±15
01±32
09±37
06±16
11±22
13±28
08±13
68±23
60±22 48±25
C ontrole
Pa c ie nte
X
X
X
X
X
F3-triang
```
Legenda (hemisfério esquerdo): hipocampo (HIP); giro parahipocampal (PHIP); porção
```
```
opercular do giro frontal inferior (F3-oper); porção triangular do giro frontal inferior (F3-
```
```
triang) e giro frontal médio (F2).
```
Valores expressos em 10-2.
A segunda diferença entre o grupo de controles e o de pacientes com ELTM esquerda
foi detectada em termos de conectividade efetiva. Nos controles, o padrão de conectividade
91
efetiva apresentou valores relativamente mais intensos que o padrão dos pacientes, inclusive
quando a influência era negativa. A Figura 20 apresenta todos os parâmetros de
conectividade efetiva estabelecidos com o modelo estrutural apresentado na Figura 19.
HIP
PHIP
F3-triang F3-oper
F2
0,80±0,24 [C]
0,67±0,33 [P]
-0,18±0,20 [C]
0,03±0,16 [P]
-0,40±0,48 [C]
-0,05±0,37 [P]
0,83±0,33 [C]
0,54±0,36 [P]
-0,51±0,46 [C]
-0,10±0,17 [P]
0,22±0,31 [C]
0,41±0,58 [P]
Controle [C]
Paciente [P]
Figura 20 – Parâmetros de conectividade efetiva em sujeitos controles e pacientes com ELTM
esquerda.
92
Experimento 3 – Modulação de conectividade efetiva por codificação de palavras
neutras e abstratas
MATERIAIS E MÉTODOS
Sujeitos
```
Participaram deste trabalho 9 sujeitos controle (4 mulheres; idade média de
```
```
33,00±9,37) e 9 indivíduos com ELTM direita (5 mulheres; idade média de 39,67±6,22) e 9
```
```
indivíduos com ELTM esquerda (8 mulheres; idade média de 35,67±9,91). Os pacientes
```
foram selecionados seguindo os mesmos critérios estabelecidos no experimento 2 com a
ressalva de que cada grupo de pacientes apresentou esclerose hipocampal unilateral e
ipsilateral com a lateralização dos focos epileptogênicos. O grupo controle, por sua vez, foi
constituído de forma idêntica ao apresentado no experimento 2.
Todos os participantes apresentaram dominância hemisférica esquerda para linguagem
determinada através de teste de audição dicótica além de serem considerados destros pelo
```
inventário de Edinburgh (Oldfield, 1971).
```
Ética
Idem ao experimento 2.
Aquisição de dados
Idem ao experimento 2.
Paradigmas
Utilizou-se o paradigma de codificação de memória verbal ilustrado pela Figura 14.
Pré-processamento das imagens
93
Os processos de preparação das imagens para serem analisadas seguiram caminhos
semelhantes àqueles descritos no experimento 2, entretanto, as etapas de orientação temporal
```
(slice timeming), correção de movimento, normalização para o espaço padrão e suavização
```
```
das imagens funcionais foram realizadas com o software SPM8 (www.fil.ion.ucl.ac.uk/spm).
```
Após a etapa de pré-processamento, as imagens funcionais apresentaram resolução isométrica
de 1mm3, enquanto a resolução no experimento anterior foi de 2mm3 isométricos.
Análise dos dados
```
Definição dos volumes anatômicos de interesse (AVOI)
```
Para verificar a modulação na conectividade efetiva provocada pela codificação de
palavras, utilizaram-se as seguintes AVOIs do hemisfério esquerdo: área visual primária
```
(área de Brodmann 17 – AB17), porção caudal do giro temporal superior (área de Wernicke
```
```
ou área de Brodmann 22 – AB22), córtex pré-frontal dorsolateral (área de Brodmann 46 –
```
```
AB46) e o hipocampo (HIP). Estas regiões foram descritas previamente como
```
```
correlacionadas à memória episódica (Dupont et al., 2000) bem como foram observadas na
```
análise de grupo dos dados de fMRI dos controles na fase de codificação da etapa de
memória verbal, cujo paradigma está ilustrado na Figura 15.
```
Analisadas as imagens funcionais dos três grupos individualmente (contraste na
```
```
codificação), elegeu-se o voxel de maior significância em cada uma das regiões
```
anteriormente mencionadas. As posições destes voxels foram utilizadas para marcar o centro
```
de uma esfera (5mm de raio) nas imagens funcionais dos indivíduos em seus respectivos
```
grupos. Extraiu-se cada série temporal encapsulada pela esfera e calculou-se sua componente
```
principal (PCA). Esses vetores, 4 para cada indivíduo, foram utilizados para se estimar a
```
conectividade efetiva e a modulação provocada pela codificação verbal em cada indivíduo.
Modulação por codificação verbal.
94
Com o propósito de se verificar a modulação dos parâmetros de conectividade efetiva
```
(intrínseco, modulatório e extrínseco) provocada pela realização da tarefa de codificação
```
verbal, estimou-se o modelo anatômico apresentado na Figura 21 utilizando a modelagem
causal dinâmica.
AB 17
HIP AB 46
AB 22
P
P
P
Parâmetros de conectividade intrínseco [A]
Parâmetros de conectividade modulatório [B]
Parâmetros de conectividade extrínseco [C]
P Palavra
Desenho do paradigma
```
Figura 21 – Modelo anatômico com as áreas de Brodmann 17, 46 e 22 (AB17,AB46 e AB22
```
```
respectivamente) e hipocampo (HIP). Parâmetros de conectividade (A,B e C) da equação 14.
```
RESULTADOS
Foram observadas diferenças, em termos de conectividade efetiva, na maioria das
conexões estabelecidas entre as regiões apresentadas na Figura 21 para o grupo controle
versus os grupos de pacientes. O parâmetro de conectividade da área visual primária ao
95
hipocampo esquerdo foi significativamente maior nos controles que nos pacientes. O mesmo
padrão, mas com sinal oposto, foi observado entre a porção dorsolateral do córtex pré-frontal
e o hipocampo esquerdo. Encontrou-se também que a conectividade modulatória, produzida
pela codificação verbal, foi significativamente pronunciada nos controles mas não nos
pacientes. A Figura 22 ilustra detalhadamente de forma quantitativa esses resultados.
AB 17
HIP AB 46
AB 22
P
P
P
0,044
0,026
0,055
0,230
0,064
0,091
- 0,036
0,012
- 0,008
- 0,037
0,014
- 0,007
- 0,017
0,005
- 0,037
- 0,181
0,000
- 0,001
0,236
0,061
- 0,055
Grupo controleX ELTM direitaX ELTM esquerdaX
Figura 22 – Parâmetros de conectividade efetiva modulados pela codificação verbal em
```
indivíduos controles (preto) e pacientes com ELTM direita (azul) e esquerda (vermelho).
```
96
Experimento 4 – Análise de imageamento por tensor de difusão em pacientes idosos
com e sem diagnóstico de depressão
DTI voxelwise analysis did not differentiate older depressed patients from older
subjects without depression
Diana Moitinho Bezerra a,*, Fabrício R.S. Pereira b, Fernando Cendes b, Marcel Parolin Jackowski c,
Eduardo Y. Nakano d, Marco A.A. Moscoso a, Salma R.I. Ribeiz a, Renata Ávila a, Cláudio Campi de Castro e,
Cássio M.C. Bottino a
a Old Age Research Group e PROTER, Institute and Department of Psychiatry, University of São Paulo, São Paulo, Brazilb Neurology Department, Neuroimaging Laboratory, University of Campinas e UNICAMP, Campinas, São Paulo, Brazil
c Computer Science, Institute of Mathematics and Statistics, University of São Paulo, São Paulo, Brazild Department of Statistics, University of Brasília e UnB, Brasília, Brazil
e Department of Diagnostic Imaging, Heart Institute e InCor, Hospital das Clínicas at University of São Paulo, São Paulo, Brazil
a r t i c l e i n f o
Article history:Received 13 June 2012
Received in revised form19 August 2012
Accepted 1 September 2012
```
Keywords:Elderly
```
Major depressive disorderDiffusion tensor imaging
Fractional anisotropyTract-based spatial statistics
Voxelwise analysis
a b s t r a c t
```
Introduction: Neuroimaging has been widely used in studies to investigate depression in the elderlybecause it is a noninvasive technique, and it allows the detection of structural and functional brain
```
```
alterations. Fractional anisotropy (FA) and mean diffusivity (MD) are neuroimaging indexes of themicrostructural integrity of white matter, which are measured using diffusion tensor imaging (DTI). The
```
```
aim of this study was to investigate differences in FA or MD in the entire brain without a previouslydetermined region of interest (ROI) between depressed and non-depressed elderly patients.
```
```
Method: Brain magnetic resonance imaging scans were obtained from 47 depressed elderly patients,diagnosed according to DSM-IV criteria, and 36 healthy elderly patients as controls. Voxelwise statistical
```
```
analysis of FA data was performed using tract-based spatial statistics (TBSS).Results: After controlling for age, no significant differences among FA and MD parameters were observed
```
in the depressed elderly patients. No significant correlations were found between cognitive performanceand FA or MD parameters.
```
Conclusion: There were no significant differences among FA or MD values between mildly or moderatelydepressed and non-depressed elderly patients when the brain was analyzed without a previously
```
determined ROI.Ó 2012 Elsevier Ltd. All rights reserved.
1. Introduction
Depression is the most common psychiatric disorder found inelderly patients, and prevalence rates range from 4.7 to 36.8%,
```
considering different forms and severities of depression (Barcelos-Ferreira et al., 2009).
```
```
Depression is clearly associated with cognitive and functionaldeficits (Blazer et al., 1991), even when the symptoms are moderate
```
```
(Kiosses et al., 2000), and these are usually present during thedepressive episode and after remission of the same (Butters et al.,
```
```
2000; Alexopoulos et al., 1993). Furthermore, the degree of cogni-tive impairment seems to follow the severity of symptoms (Baudic
```
```
et al., 2004). Recent research suggests that changes in white matterintegrity throughout life are associated with cognitive impairments
```
```
too (Schiavone et al., 2009).Diffusion tensor imaging (DTI) is a variation of structural
```
```
magnetic resonance imaging (MRI) examination that measures therate and determines the direction of water diffusion in tissues,
```
which permits the quantification of brain tissue microstructures.DTI is commonly used to study the organization of brain regions
```
such as white matter and neuronal tract fibers because it is able todetect subtle changes in white matter (Taylor et al., 2004a; Mori and
```
```
Zhang, 2006). Fractional anisotropy (FA) is a measure of direction-ally dependent restriction of water diffusion and mean diffusivity
```
```
(MD) is the average of water diffusion in all directions (Mettenburget al., 2012). These two measurements combined may assist in an
```
indirect way the characterization of tissue integrity. DTI abnor-malities typically manifest as increased MD and/or reduced FA.
Several DTI studies on major depressive disorder have showedthat abnormalities in frontal-subcortical circuits are common and
- Corresponding author. Faculty of Medicine, University of São Paulo, R. Dr. OvídioPires de Campos, 785, 3 andar sala 14, Caixa Postal 3671, CEP 01060-970,
```
São Paulo e SP, Brazil. Tel.: þ55 11972877087.E-mail address: di_piparoti@yahoo.com.br (D.M. Bezerra).
```
Contents lists available at SciVerse ScienceDirect
Journal of Psychiatric Research
j o u r n a l h o m e p a g e : w w w . e l s e v i e r . c o m / l o c a t e / p s y c h i r e s
0022-3956/$ e see front matter Ó 2012 Elsevier Ltd. All rights reserved.http://dx.doi.org/10.1016/j.jpsychires.2012.09.001
```
Journal of Psychiatric Research 46 (2012) 1643e1649
```
97
```
may play an important role in the pathophysiology of this disorder(Nobuhara et al., 2004, 2006; Shimony et al., 2009; Taylor et al.,
```
```
2004b; Yang et al., 2007).Recent evidence demonstrated significant correlation between
```
```
DTI parameters and decreased global cognition in elderly patients(Vernooij et al., 2009).
```
```
Generally, DTI images may be analyzed by examining one ormore regions of interest (ROI) or by voxel-based analysis (VBA).
```
```
Analysis by ROI is a manual or semiautomated method that analysespredetermined regions of the brain (Sexton et al., 2009), whereas
```
```
VBA analysis is an observer-independent method that explores theentire brain without a previous hypothesis (Smith et al., 2006,
```
```
2007). Voxel-based morphometry (VBM) is one of the most widelyused VBA approaches to study the volume of white and gray matter
```
```
(Ashburner and Friston, 2000). However, this method has signifi-cant limitations in processing anisotropic parameters (Smith et al.,
```
```
2006; Afzali et al., 2011).Smith et al. (2006) have recently suggested a new automatized
```
```
method, tract-based space statistics (TBSS), as a part of the FSLprogram. This tool is expected to improve objectivity and simplicity
```
in the interpretation of DTI analysis because it utilizes diffusionparameters for image registration.
Most of the studies investigating diffusion parameters anddepression in the elderly have used the ROI method for image
```
evaluation and observed changes mainly in frontal and temporalregions of brain (Nobuhara et al., 2004, 2006; Shimony et al., 2009;
```
```
Taylor et al., 2004b; Yang et al., 2007). However, becauseresearchers have only analyzed predetermined areas of the brain,
```
the existence of difference in unevaluated regions remainsunknown. Conversely, studies investigating alterations in the entire
```
white matter through DTI in depressed elderly patients are scarceand inconclusive (Dalby et al., 2010; Yuan et al., 2007).
```
```
The objective of this study was to investigate changes in whitematter through fractional anisotropy (FA) and mean diffusivity
```
```
(MD), using voxelwise analysis of DTIs in depressed and non-depressed elderly patients. The study also aimed to investigate
```
correlations among FA and MD data to scores obtained fromcognitive and functional evaluations.
2. Methods
2.1. Sample
Forty-seven elderly patients aged 60 years and over who werediagnosed with major depression or depressive episodes according
```
to the diagnostic criteria of the Diagnostic and Statistical Manual-IV(DSM-IV) (APA, 1994) participated in this study. The study subjects
```
were selected from a pool of outpatients treated by the Old AgeResearch Group at the Institute of Psychiatry, “Hospital das Clíni-
```
cas” at School of Medicine at the University of São Paulo (HC-FMUSP). Of the 47 elderly with depressive disorders, 8 (17.0%)
```
```
received some type of antidepressant and 8 (17.0%) were takingbenzodiazepines.
```
```
We included elderly patients who met the DSM-IV criteriafor depressive disorders, based on a diagnostic interview (CAM-
```
```
DEX) (Bottino et al., 1999) administered by two trained geriatricpsychiatrists, who also applied the cognitive tests and depression
```
scales. The clinical evaluation and MRI scanning occurred in twoweeks.
```
The exclusion criteria for the elderly depressed group were:diagnoses of dementia or other organic mental disorders; and
```
```
DSM-IV criteria-based diagnoses of any psychiatric disorder otherthan depression (although patients with anxiety disorders comor-
```
```
bid to depression were not excluded) or the inability to perform anMR examination.
```
To ensure that any subjects with incipient dementia would beexcluded from the elderly depressed group, the Bayer Activities of
```
Daily Living Scale (B-ADL) (Lehfeld et al., 1997) was applied toinformants. According to a previous study with Brazilian patients
```
```
(Folquitto et al., 2007), the cutoff point of B-ADL  3.12 providesadequate sensitivity, specificity, positive and negative predictive
```
values to discriminate patients with mild to moderate dementiafrom non-demented elderly subjects. Patients were monitored for
a year to guarantee that no dementia cases were included in thedepressed elderly group. Cognitive evaluations were performed
every three months, and none of the patients developed dementiaduring this period.
Thirty-six elderly patients aged 60 years and over withoutdepression or any other psychiatric disorders were also included in
this study as the control group. Members of control group wererecruited from Geriatric Department at HC-FMUSP. No member of
control group was taking psychotropic medications. The followingexclusion criteria were used for the control group: current DSM-IV
```
criteria-based diagnoses of any psychiatric disorders; and previoushistory of depressive disorders at any point in their lives; dementia
```
```
syndrome; another organic brain syndrome and the inability toperform an MR examination.
```
All of the participants gave their written informed consentfollowing a detailed description of study’s procedures. This study
was approved by the Institute of Psychiatry’s Ethics Committee ofHC-FMUSP.
2.2. Clinical, cognitive and functional assessment
The following instruments were used to evaluate cognitiveaspects: Cambridge Examination for Mental Disorders of the
```
Elderly (CAMDEX) (Roth et al., 1986; Bottino et al., 1999), whichincludes CAMCOG (Cambridge Cognitive Test) and Mini-Mental
```
```
State Examination (MMSE) (Folstein et al., 1975). To measuredepressive symptomatology, the MontgomeryeAsberg Depression
```
```
Rating Scale (MADRS) (Montgomery and Asberg, 1979) and Ham-ilton Rating Scale of Depression (HAM-D) (Hamilton, 1960) were
```
```
utilized. Bayer Activities of Daily Living Scale (B-ADL) (Lehfeld et al.,1997) was used to evaluate functional activity. Finally, clinical
```
```
comorbidities were measured using Cumulative Illness Rating Scale(CIRS) (Linn et al., 1968).
```
```
Patients with late onset depression (LOD) (after age 60) morefrequently present structural and functional abnormalities in the
```
```
brain in comparison to early onset depression (EOD) (Blazer, 2003).Because of this, an analysis to verify the existence of significant
```
DTI alterations between EOD, LOD and the control group will beperformed.
2.3. DTI acquisition
```
Structural MR examinations were performed at the DiagnosticImaging Division of the Heart Institution (INCOR) of HC-FMUSP
```
```
using a GE 1.5 T (Signa, GE Medical Systems, Horizon, LX) MRinstrument.
```
```
Diffusion protocol used to produce DTI images consisted ofa diffusion sequence in 25 directions (b ¼ 0 and b ¼ 1000 s/mm2),
```
```
echo time (TE) of 100 ms, repetition time (TR) of 10,000 ms, field ofview of 26, a 128 # 128 matrix, and 5.0 mm slice thickness.
```
2.4. Image processing
```
DTI data processing and analysis were performed using softwaretools from FMRIB Software Library (FSL) 4.1 (http://www.fmrib.ox.
```
```
ac.uk/fsl/) (Smith et al., 2004). The main tool used for voxel-to-voxel comparison of diffusion data was TBSS (Smith et al., 2006) v1.2.
```
```
D.M. Bezerra et al. / Journal of Psychiatric Research 46 (2012) 1643e16491644
```
98
All images were initially aligned to the reference image at b ¼ 0so that the sequence created a mask. The main objective in using
```
the mask was to extract all of the elements that were not a part ofthe brain (for example, the eye socket) to identify exactly which
```
voxels should be included in the analysis. This was referred to as thepreprocessing stage.
FA and MD maps, three auto-values and three auto-vectors wereestimated. In next step, the parameters for normalization of these
data into a common space of 1 " 1 " 1 mm were calculated.The results using these parameters were applied to the images
through linear and nonlinear transformations to complete thenormalization. These parameters corrected differences caused by
slight movements during image acquisition along with slightdistortions due to field induction in different acquisitional direc-
tions caused by MR coil itself. FMRIB58_FA atlas was used as thereference for normalization. This step was necessary to ensure that
```
all of the individuals were in the same space (compatible withMontreal Neurological Institute (MNI) atlas (Mazziotta et al., 2001),
```
```
assuming that FMRIB58_FA anisotropy atlas possessed the samecoordinates as MNI atlas) for future statistical comparisons. This
```
stage was referred to as “Registration”.The next step was to calculate the average FA to create a mean FA
skeleton. This mean FA skeleton was formed using the averagepoints of the FA tracts. Once created, the mean FA skeleton was
```
applied to each patient to produce individual mean FA skeletons.The threshold selected for the creation of mean skeletons was 0.2;
```
therefore, the program used every voxel with an FA greater than 0.2to calculate the mean skeleton. The final result obtained from this
```
process was used for statistical analysis; thus, only the voxelsbelonging to the skeleton were considered for statistics.
```
In the next step, voxel-to-voxel comparisons were performedamong the groups, and statistical maps were generated.
2.5. Statistical analysis
The following tests were used to analyze clinical and socio-demographic data: MADRS, HAM-D, B-ADL, CIRS, age and education.
Student’s t-test was used to compare means when variables werenormally distributed. ManneWhitney U-test was used to compare
groups when normality could not be established. Normality of thedata was tested using KolmogoroveSmirnov nonparametric test.
```
Pearson’s Chi-square test was used to compare frequencies forgender and civil status. Finally, analysis of covariance (ANCOVA) was
```
used for MMSE and CAMDEX variables controlling for educationbecause an initial analysis revealed that these parameters differed
between the groups.Voxel-to-voxel statistical comparisons were performed to
```
compare the entire white matter skeleton of the groups (patients
```
```
vs. controls) using the TBSS tool from FSL program and theStudent’s t-test. Statistical maps were created to show anatomical
```
```
brain location of the clusters of significantly different voxelsbetween the groups (p < 0.001). The statistical maps were created
```
using a statistical threshold corrected for 1000 multiple compari-sons. Pearson’s correlation coefficient was used to measure asso-
ciations among anisotropy parameters and clinical data.
3. Results
Sociodemographic data of the subjects are shown in Table 1.“Education” was the only sociodemographic variable that differed
significantly between groups.The results obtained from cognitive evaluations, depressive
symptom scales, functional activity and clinical comorbidities areshown in Table 2.
Nonsignificant differences were observed between the twogroups following the analysis of diffusivity, which was quantified
by FA, and the diffusion of water molecules in every direction,which was quantified by MD.
```
Regarding the possible association between anisotropy param-eters and cognitive evaluation (CAMDEX and MMSE) nonsignificant
```
```
findings were observed. Similar results were observed for theassociation among functional activity (measured by B-ADL scale)
```
and FA or MD parameters.The analysis performed between EOD, LOD and control group
showed nonsignificant differences, same results were obtainedbetween EOD and LOD without the control group.
Statistical maps obtained from the results revealed nonsignifi-cant reductions in FA nor increases in MD in depressed elderly
```
patients and a nonsignificant association between MMSE and FAreduction in the whole sample (Figs. 1e3).
```
4. Discussion
The present study showed nonsignificant differences in FAneither MD parameters between depressed and non-depressed
elderly patients. Although previous studies have demonstratedconflicting results, it should be noted that among studies reviewed
```
that investigated depression and anisotropy parameters in theelderly (Alexopoulos et al., 1993; Bae et al., 2006; Dalby et al., 2010;
```
```
Nobuhara et al., 2004, 2006; Shimony et al., 2009; Taylor et al.,2004b; Yang et al., 2007; Yuan et al., 2007), only one utilized an
```
```
evaluation similar to the current study (Dalby et al., 2010). Dalbyet al. (2010) used voxel-based non-morphometric analysis to
```
investigate these parameters between depressed and non-depressed elderly patients and obtained results consistent with
our study. They reported nonsignificant differences in anisotropy
Table 1Sample data.
```
Variable Depressed elderly (n ¼ 47) Non-depressed elderly (n ¼ 36) Statistical test and p-valueGender
```
```
n (%)M 11 (23.4%) 9 (25.0%) c2 ¼ 0.028(fd ¼ 1)p ¼ 0.866F 36 (76.6%) 27 (75.0%)
```
```
AgeMean (SD)70.94 (6.98) 69.39 (7.21) t ¼ 0.992(fd ¼ 81)
```
p ¼ 0.324Education
```
Mean (SD)6.31 (5.60) 9.08 (4.75) t ¼ #2.378(fd ¼ 81)p ¼ 0.020
```
```
Number of previous depressive episodesa 1.45 (2.33) e eAge of onset of symptomsa LOD ¼ 17 (36.2%)
```
```
EOD ¼ 30 (63.8%)e e
```
```
n ¼ number of patients; F ¼ female; M ¼ male; LOD ¼ Late-onset depression; EOD ¼ Early-onset depression; c2: Pearson’s chi-square; t: Student’s t-test; p-value. Bold meansthe only significance difference found in (p < 0.05).
```
a These variables refer only to patients.
```
D.M. Bezerra et al. / Journal of Psychiatric Research 46 (2012) 1643e1649 1645
```
99
```
parameters between groups. Yuan et al. (2007) used morphometricanalysis of FA to investigate the association between remission and
```
changes in anisotropy parameters and to compare depressedelderly patients who achieved remission to non-depressed controls.
```
In a study conducted by Alexopoulos et al. (2008), VBA analysis wasused to compare elderly patients who achieved remission from
```
depressive symptoms to elderly patients who did not achieveremission. In the remaining studies, investigations were conducted
```
by delineating ROI (Bae et al., 2006; Nobuhara et al., 2004, 2006;Shimony et al., 2009; Taylor et al., 2004b; Yang et al., 2007).
```
```
Kieseppä et al. (2010) did not observe changes betweendepressed and non-depressed patients while investigating
```
```
depression and anisotropy parameters using the same processingmethodology used in our study (TBSS). However, this group
```
```
(Kieseppä et al., 2010) investigated younger patients with a meanage of 40 years. Study conducted with even younger individuals
```
```
(mean age of 20 years), who were not yet medicated for depressionand were experiencing their first depressive episode, showed
```
```
significant differences in the anterior part of internal capsule andparahippocampal gyrus using TBSS analysis (Zhu et al., 2011).
```
Table 3 displays data obtained from studies published to date onthe study of depressed and non-depressed elderly patients using
anisotropy parameters.The same participants used in this study were previously
```
investigated regarding changes in white and gray matter density aspart of another research project (Avila et al., 2011). In this study,
```
```
Fig. 1. Nonsignificant reduction of FA in the splenium of the corpus callosum in depressed elderly compared to non-depressed elderly (p ¼ 0.48).
```
Table 2Cognitive and functional assessment, severity of depressive symptoms and clinical
comorbidity.
```
Variable Depressed elderly(n ¼ 47)Non-depressed elderly(n ¼ 36)Statistical testand p-value
```
```
MMSE 25.21 (") 3.74 27.86 (") 1.99 F ¼ 8.612(fd ¼ 1;80)
```
```
p ¼ 0.004aCAMDEX 82.94 (") 13.95 90.83 (") 8.88 F ¼ 5.352
```
```
(fd ¼ 1;80)p ¼ 0.017a
```
```
B-ADL 2.25 (") 1.01 1.32 (") 0.56 t ¼ 4.966(fd ¼ 81)
```
```
p < 0.001bMADRS 23.23 (") 8.60 1.39 (") 1.20 t ¼ 15.111
```
```
(fd ¼ 81)p < 0.001b
```
```
HAM-D 18.64 (") 6.17 2.67 (") 1.57 t ¼ 15.151p < 0.001b
```
```
CIRS-index 0.65 (") 0.92 0.56 (") 0.97 U ¼ 754.0p ¼ 0.427c
```
```
CIRS-severity 1.23 (") 0.21 1.25 (") 0.22 U ¼ 790.5p ¼ 0.724c
```
```
MMSE ¼ Mini-Mental State Examination; CAMDEX ¼ Cambridge Examination forMental Disorders of the Elderly; B-ADL ¼ Bayer Activities of Daily Living Scale;
```
```
HAM-D ¼ Hamilton Depression Scale; MADRS ¼ MontgomeryeAsberg DepressionRating Scale; CIRS ¼ Cumulative Illness Rating Scale. fd ¼ freedom degree p-value.
```
```
Bold means significance (p < 0.05) and italics means differentiate the symbol ofstatistical test.
```
```
a Analysis of covariance (ANCOVA) controlling for years of education.b Student’s t-test.
```
c ManneWhitney U-test.
```
D.M. Bezerra et al. / Journal of Psychiatric Research 46 (2012) 1643e16491646
```
100
```
Fig. 2. Nonsignificant increase in MD at the posterior limb of the right internal capsule in depressed elderly compared to non-depressed elderly (p ¼ 0.45).
```
```
Fig. 3. Nonsignificant positive associations between FA in temporal regions and cognition through MMSE data (p ¼ 0.35). The association between the anisotropy parameters andthe other tests and scales did not result in statistical maps and was not significant.
```
```
D.M. Bezerra et al. / Journal of Psychiatric Research 46 (2012) 1643e1649 1647
```
101
nonsignificant differences were observed between depressed andnon-depressed elderly following VBM analysis of the entire brain.
A possible explanation for the absence of significant differencesbetween groups in this present study is the similar profiles of these
groups regarding clinical comorbidities and cardiovascular factors,such as hypertension, diabetes and heart diseases, which involve
```
major changes in white and gray matter (de Toledo Ferraz Alveset al., 2010).
```
Another aspect that may partially explain these findings is thesmall number of previous depressive episodes among the study
```
population. Most of the patients (40.4%) were being treated fortheir first depressive episode, and a significant portion (25.5%) was
```
experiencing their second depressive episode. Although no studiesabout the association between number of depressive episodes and
diffusion parameters were found in the literature, a relationshipbetween greater numbers of episodes and greater brain atrophy has
```
been suggested (Janssen et al., 2007).The present study did not observe an association between
```
anisotropy parameters and cognitive evaluation. Although a previousstudy demonstrated significant correlation between microstructural
```
white matter damage measured by diffusivity parameters anddecreased global cognition in elderly patients (Vernooij et al., 2009),
```
```
the relationship between white matter integrity and cognitivefunction has not been clearly established (Madden et al., 2004).
```
```
The current study has some important limitations: the slicewidth in MR examination; group heterogeneity regarding educa-
```
```
tion; a majority of patients with mild to moderate depressivesymptoms and a lack of data concerning duration of disease and
```
duration of the antidepressant therapy of patients.However, regarding abovementioned limitations, the same slice
```
width of 5.0 mm (Abe et al., 2010; Kieseppä et al., 2010) or verysimilar slice widths (4.0 mm) (Ma et al., 2007; Wu et al., 2011; Yuan
```
```
et al., 2007; Zhu et al., 2011) were used in several studies thatinvestigated depression and anisotropy parameters. About severity
```
```
of depressive symptoms, Dalby et al. (2010) reported a positivecorrelation between severity of depressive symptoms and FA
```
changes in fiber tracts affected by deep white matter lesions,however, no association was observed in a study that correlated
```
depression severity and FA values in younger patients (Abe et al.,2010). Moreover, when considering duration of disease, no rela-
```
```
tionships between FA parameters and the duration of depressivedisorders were observed (Ma et al., 2007).
```
The discrepancy in the results of neuroimaging studies of majordepressive disorder may reflect the clinical heterogeneity of the
samples and also possible heterogeneities intrinsic to the patho-physiology of the disorder itself.
5. Conclusion
```
Data obtained from this study suggest that there is nonsignifi-cant difference in diffusion parameters (FA and MD) between mild
```
to moderately depressed and non-depressed elderly patients.It may also be concluded that diffusion parameters in the elderly
```
(both FA and MD) are not associated with cognitive function.
```
Role of funding source
```
This study received financial support from “Fundação deAmparo à Pesquisa do Estado de Sao Paulo” (FAPESP), grant no. 04/
```
09586-9. Diana M. Bezerra was particularly supported by the“Coordenação de Aperfeiçoamento de Pessoal de Nível Superior”
```
(CAPES).
```
Contributors
Authors Cássio Machado de Campos Bottino and Diana MoitinhoBezerra designed the study.
Authors Cássio Machado de Campos Bottino, Diana MoitinhoBezerra, Fabrício Ramos Silvestre Pereira, Fernando Cendes, Marcel
Parolin Jackowski wrote the protocol.Authors Diana Moitinho Bezerra, Marco Antonio Aparício
Moscoso, Salma R. I. Ribeiz, Renata Ávila, Cláudio Campi managedthe literature searches and analyses.
Authors Eduardo Yoshio Nakano and Diana Moitinho Bezerraundertook the statistical analysis, and authors Diana Moitinho
Bezerra and Cássio Machado de Campos Bottino wrote the firstdraft of the manuscript.
All authors contributed to and have approved the finalmanuscript.
Conflict of interest
Authors declare no conflict of interests affecting this manuscript.
Acknowledgments
We would like to thank Professor Edson Amaro Junior by hisadvices during this research.
Table 3Summary of the literature on DTI parameters and depressed elderly compared to non-depressed elderly.
```
Study n P/C Age mean (SD) Study design Methods Significant results in depressed elderlyTaylor et al., 2004b 17
```
```
1667.5 (6.1)69.8 (6.4)Depressed ! non-depressed ROI Y FA in the right superior frontal gyrusNobuhara et al., 2004 8
```
```
1262.9 (5.8)60.9 (4.6)Depressed ! non-depressed ROI Y FA in widespread frontal and temporal regionsNobuhara et al., 2006 13
```
```
1362.8 (6.6)61.5 (4.8)Depressed ! non-depressed ROI Y FA in widespread regions of the frontal and temporal lobesAssociation between severity and FA in frontal lobeBae et al., 2006 106
```
```
8470.4 (6.4)71.7 (6.0)Depressed ! non-depressed ROI Y FA in white matter of the right anterior cingulate cortex, bilateralsuperior frontal gyri, and left middle frontal gyrusAbsence of association between severity and FA
```
```
Yang et al., 2007 311564.6 (5.2)64.3 (4.2)Depressed ! non-depressed ROI Y FA in frontal (superior and middle frontal gyrus), and temporal(right parahippocampal gyrus) regions
```
```
Shimony et al., 2009 782368.6 (7.2)70.0 (5.9)Depressed ! non-depressed ROI Y RA (similar to FA) in pre-frontal ROIs[ MD in pre-frontal ROIs and deep white matter
```
```
[ MD in combined non-prefrontal regions (temporal, parietal, occipitaland motor regions)
```
```
Dalby et al., 2010 222257.4 (4.6)59.2 (7.3)Depressed ! non-depressed VBA There is no significant difference in FA when compared both groupsAssociation between FA and severity in deep white matter lesions
```
```
Colloby et al., 2011 383074.1 (6.1)74.4 (6.4)Depressed ! non-depressed TBSS Corrected maps showed no significant differences in FA neither MDparameters when compared both groups
```
```
D.M. Bezerra et al. / Journal of Psychiatric Research 46 (2012) 1643e16491648
```
102
References
Abe O, Yamasue H, Kasai K, Yamada H, Aoki S, Inoue H, et al. Voxel-based analyses ofgray/white matter volume and diffusion tensor data in major depression.
```
Psychiatry Research 2010;181(1):64e70.Afzali M, Soltanian-Zadeh H, Elisevich KV. Tract based spatial statistical analysis and
```
```
voxel based morphometry of diffusion indices in temporal lobe epilepsy.Computers in Biology and Medicine 2011;41(12):1082e91.
```
Alexopoulos GS, Meyers BS, Young RC, Mattis S, Kakuma T. The course of geriatricdepression with “reversible dementia”: a controlled study. American Journal of
```
Psychiatry 1993;150(11):1693e9.Alexopoulos GS, Murphy CF, Gunning-Dixon FM, Latoussakis V, Kanellopoulos D,
```
```
Klimstra S, et al. Microstructural white matter abnormalities and remission ofgeriatric depression. American Journal of Psychiatry 2008;165(2):238e44.
```
American Psychiatric Association Committee on Nomenclature and Statistics.Diagnostic and statistical manual of mental disorders. 4th ed. Washington, DC:
```
American Psychiatric Association; 1994.Ashburner J, Friston KJ. Voxel-based morphometrydthe methods. NeuroImage
```
```
2000;11:805e21.Avila R, Ribeiz S, Duran FL, Arrais JP, Moscoso MA, Bezerra DM, et al. Effect of
```
```
temporal lobe structure volume on memory in elderly depressed patients.Neurobiology of Aging 2011;32(10):1857e67.
```
Bae JN, MacFall JR, Krishnan KR, Payne ME, Steffens DC, Taylor WD. Dorsolateralprefrontal cortex and anterior cingulate cortex white matter alterations in
```
late-life depression. Biological Psychiatry 2006;60(12):1356e63.Barcelos-Ferreira R, Pinto Jr JA, Nakano EY, Steffens DC, Litvoc J, Bottino CM.
```
Clinically significant depressive symptoms and associated factors in communityelderly subjects from Sao Paulo, Brazil. American Journal of Geriatric Psychiatry
```
2009;17(7):582e90.Baudic S, Tzortzis C, Barba GD, Traykov L. Executive deficits in elderly patients with
```
```
major unipolar depression. Journal of Geriatric Psychiatry and Neurology 2004;17(4):195e201.
```
Blazer D, Burchett B, Service C, George LK. The association of age and depressionamong the elderly: an epidemiologic exploration. Journal of Gerontology 1991
```
Nov;46(6):210e5.Blazer DG. Depression in late life: review and commentary. Journals of Gerontology.
```
```
Series A, Biological Sciences and Medical Sciences 2003;58(3):249e65. Review.Bottino CMC, Almeida OP, Tamai S, Forlenza OV, Scalco MZ, Carvalho IAM. Entrevista
```
```
estruturada para diagnóstico de transtornos mentais em idosos e CAMDEX(translated and adapted on behalf of the editors). São Paulo: Cambridge
```
```
University Press; 1999.Butters MA, Becker JT, Nebes RD, Zmuda MD, Mulsant BH, Pollock BG, et al. Changes
```
```
in cognitive functioning following treatment of late-life depression. AmericanJournal of Psychiatry 2000;157(12):1949e54.
```
Colloby SJ, Firbank MJ, Thomas AJ, Vasudev A, Parry SW, O’Brien JT. White matterchanges in late-life depression: a diffusion tensor imaging study. Journal of
```
Affective Disorders 2011;135(1e3):216e20.Dalby RB, Frandsen J, Chakravarty MM, Ahdidan J, Sørensen L, Rosenberg R, et al.
```
```
Depression severity is correlated to the integrity of white matter fiber tracts inlate-onset major depression. Psychiatry Research 2010;184(1):38e48.
```
de Toledo Ferraz Alves TC, Ferreira LK, Busatto GF. Vascular diseases and old agemental disorders: an update of neuroimaging findings. Current Opinion in
```
Psychiatry 2010;23(6):491e7. Review.Folquitto JC, Bustamante SEZ, Barros SB, Azevedo D, Lopes MA, Hototian SR, et al.
```
```
The Bayer-Activities of Daily Living Scale (B-ADL) in the differentiation betweenmild to moderate dementia and normal aging. Revista Brasileira de Psiquiatria
```
```
2007;29:350e3.Folstein MF, Folstein SE, Mchugh PR. Mini mental state: a practical method for
```
```
grading the cognitive state of patients for the clinician. Journal of PsychiatricResearch 1975;12:189e98.
```
```
Hamilton M. A rating scale for depression. Journal of Neurology, Neurosurgery, andPsychiatry 1960;23:56e9.
```
Janssen J, Hulshoff Pol HE, de Leeuw FE, Schnack HG, Lampe IK, Kok RM, et al.Hippocampal volume and subcortical white matter lesions in late life depres-
```
sion: comparison of early and late onset depression. Journal of Neurology,Neurosurgery, and Psychiatry 2007;78(6):638e40.
```
Kiosses DN, Alexopoulos GS, Murphy C. Symptoms of striatofrontal dysfunctioncontribute to disability in geriatric depression. International Journal of Geriatric
```
Psychiatry 2000;15(11):992e9.Kieseppä T, Eerola M, Mäntylä R, Neuvonen T, Poutanen VP, Luoma K, et al. Major
```
```
depressive disorder and white matter abnormalities: a diffusion tensor imagingstudy with tract-based spatial statistics. Journal of Affective Disorders 2010;
```
```
120(1e3):240e4.
```
```
Lehfeld H, Reisberg B, Finkel S, Kanowski S, Wied V, Pittas J, et al. Informant-ratedactivities of daily living (ADL) assessments: results of a study of 141 items in the
```
```
USA, Germany, Russia and Greece from the International ADL Scale Develop-ment Project. Alzheimer Disease and Associated Disorders 1997;11(4):39e44.
```
```
Linn BS, Linn MW, Gurell L. Cumulative illness rating scale. Journal of the AmericanGeriatrics Society 1968;16:622e5.
```
Ma N, Li L, Shu N, Liu J, Gong G, He Z, et al. White matter abnormalities in first-episode, treatment-naive young adults with major depressive disorder. Amer-
```
ican Journal of Psychiatry 2007;164:823e6.Madden DJ, Whiting WL, Huettel SA, White LE, MacFall JR, Provenzale JM. Diffusion
```
```
tensor imaging of adult age differences in cerebral white matter: relation toresponse time. NeuroImage 2004;21:1174e81.
```
Mazziotta J, Toga A, Evans A, Fox P, Lancaster J, Zilles K, et al. A probabilistic atlasand reference system for the human brain: International Consortium for Brain
```
Mapping (ICBM). Philosophical Transactions of the Royal Society of London BBiological Sciences 2001;1412:1293e322.
```
Mettenburg JM, Benzinger TL, Shimony JS, Snyder AZ, Sheline YI. Diminished perfor-mance on neuropsychological testing in late life depression is correlated with
```
microstructural white matter abnormalities. NeuroImage 2012;60(4):2182e90.Montgomery SA, Asberg M. A new depression scale designed to be sensitive to
```
```
change. British Journal of Psychiatry 1979;134:382e9.Mori S, Zhang J. Principles of diffusion tensor imaging and its applications to basic
```
```
neuroscience research. Neuron 2006;51(5):527e39. Review.Nobuhara K, Okugawa G, Minami T, Takase K, Yoshida T, Yagyu T, et al. Effects of
```
```
electroconvulsive therapy on frontal white matter in late-life depression:a diffusion tensor imaging study. Neuropsychobiology 2004;50(1):48e53.
```
Nobuhara K, Okugawa G, Sugimoto T, Minami T, Tamagaki C, Takase K, et al. Frontalwhite matter anisotropy and symptom severity of late-life depression:
```
a magnetic resonance diffusion tensor imaging study. Journal of Neurology,Neurosurgery, and Psychiatry 2006;77:120e2.
```
Roth M, Tym E, Mountjoy CQ, Huppert FA, Hendrie H, Verma S, et al. CAMDEX. Astandardised instrument for the diagnosis of mental disorder in the elderly
```
with special reference to the early detection of dementia. British Journal ofPsychiatry 1986;149:698e709.
```
Schiavone F, Charlton RA, Barrick TR, Morris RG, Markus HS. Imaging age-relatedcognitive decline: a comparison of diffusion tensor and magnetization
```
transfer MRI. Journal of Magnetic Resonance Imaging 2009;29(1):23e30.Sexton CE, Mackay CE, Ebmeier KP. A systematic review of diffusion tensor imaging
```
```
studies in affective disorders. Biological Psychiatry 2009;66:814e23.Shimony JS, Sheline YI, D’Angelo G, Epstein AA, Benzinger TL, Mintun MA, et al.
```
```
Diffuse microstructural abnormalities of normal-appearing white matter in latelife depression: a diffusion tensor imaging study. Biological Psychiatry 2009;
```
```
66(3):245e52.Smith SM, Jenkinson M, Woolrich MW, Beckmann CF, Behrens TE, Johansen-Berg H,
```
```
et al. Advances in functional and structural MR image analysis andimplementation as FSL. NeuroImage 2004;23(S1):208e19.
```
Smith SM, Jenkinson M, Johansen-Berg H, Rueckert D, Nichols TE, Mackay CE, et al.Tract-based spatial statistics: voxelwise analysis of multi-subject diffusion data.
```
NeuroImage 2006;31(4):1487e505.Smith SM, Johansen-Berg H, Jenkinson M, Rueckert D, Nichols TE, Miller KL, et al.
```
```
Acquisition and voxelwise analysis of multi-subject diffusion data withtract-based spatial statistics. Nature Protocols 2007;2:499e503.
```
```
Taylor WD, Hsu E, Krishnan KR, MacFall JR. Diffusion tensor imaging: background,potential, and utility in psychiatric research. Biological Psychiatry 2004a;55(3):
```
201e7. Review.Taylor WD, MacFall JR, Payne ME, McQuoid DR, Provenzale JM, Steffens DC, et al.
```
Late-life depression and microstructural abnormalities in dorsolateralprefrontal cortex white matter. American Journal of Psychiatry 2004b;161:
```
1293e6.Vernooij MW, Ikram MA, Vrooman HA, Wielopolski PA, Krestin GP, Hofman A, et al.
```
White matter microstructural integrity and cognitive function in a generalelderly population. Archives of General Psychiatry 2009;66(5):545e53.
```
Wu F, Tang Y, Xu K, Kong L, Sun W, Wang F, et al. Whiter matter abnormalities inmedication-naive subjects with a single short-duration episode of major
```
depressive disorder. Psychiatry Research 2011;191(1):80e3.Yang Q, Huang X, Hong N, Yu X. White matter microstructural abnormalities in late-
```
```
life depression. International Psychogeriatrics 2007;19:757e66.Yuan Y, Zhang Z, Bai F, Yu H, Shi Y, Qian Y, et al. White matter integrity of the whole
```
```
brain is disrupted in first-episode remitted geriatric depression. NeuroReport2007;18:1845e9.
```
Zhu X, Wang X, Xiao J, Zhong M, Liao J, Yao S. Altered white matter integrity infirst-episode, treatment-naive young adults with major depressive disorder:
```
a tract-based spatial statistics study. Brain Research 2011;19(1369):223e9.
```
```
D.M. Bezerra et al. / Journal of Psychiatric Research 46 (2012) 1643e1649 1649
```
103
Experimento 5 – Anormalidade em substância branca e cinzenta em pacientes com
mutação do gene SPG11.
RESEARCH PAPER
White and grey matter abnormalities in patients with
SPG11 mutations
Marcondes C Franc¸a Jr,1 Clarissa L Yasuda,1 Fabrı´cio R S Pereira,1 Anelyssa D’Abreu,1
Camila M Lopes-Ramos,2 Madalena V Rosa,2 Fernando Cendes,1 Iscia Lopes-Cendes2
ABSTRACTBackground Mutations in SPG11 are the most frequent
known cause of autosomal recessive hereditary spasticparaplegia. Corpus callosum thinning is a hallmark of the
condition but little is known about damage to otherstructures in the CNS.
Objective To evaluate in vivo cerebral damage inpatients with SPG11 mutations.
Methods 5 patients and 15 age and sex matchedhealthy controls underwent high resolution diffusion
```
tensor imaging (32 directions) and a T1 volumetric(1 mm slices) acquisition protocol in a 3 T scanner
```
```
(Philips Achieva). These sequences were then analysedthrough voxel based morphometry (VBM) and tract
```
```
based spatial statistics (TBSS).Results Mean age of the patients was 23.664.5 years
```
```
(range 14e45) and mean duration of disease was 12 years(range 5e15). All patients presented with progressive
```
spastic paraplegia and three were already wheelchairbound when first evaluated. Mutations found were:
c.529_533delATATT, c.704_705delAT, c.733_734delAT,c.118C>T and c.7256A>G. VBM identified significant grey
matter atrophy in both the thalamus and lentiform nuclei.TBSS analyses revealed reduced fractional anisotropy
involving symmetrically subcortical white matter of thetemporal and frontal lobes, the cingulated gyrus, cuneus,
striatum, corpus callosum and brainstem.Conclusions Widespread white matter damage in
patients with SPG11 mutations has been demonstrated.Grey matter atrophy was prominent in both the thalamus
and basal ganglia but not in the cerebral cortex. Thesefindings suggest that neuronal damage/dysfunction is more
widespread than previously recognised in this condition.
```
INTRODUCTIONHereditary spastic paraplegia (HSP) is a heteroge-
```
neous group of neurodegenerative disorders charac-terised by progressive lower limb weakness and
spasticity.1 In some patients, these are the sole clin-ical findings and these patients are classified as pure
```
HSP. In contrast, some additional systemic (cata-racts) or neurological (dementia, ataxia, epilepsy)
```
```
features may be found in other patients; these in turnare classified as complicated HSP. At present, there are
```
at least 48 loci associated with HSP and 17 identifiedgenes.1 2 HSP may segregate as an autosomal domi-
nant, autosomal recessive or X linked trait.Mutations in the SPG11 gene located on chro-
mosome 15q13-15 are now recognised as the mostfrequent cause of autosomal recessive HSP.3
Patients typically present with gait complaints in
the first or second decades but ultimately developcognitive impairment and peripheral manifesta-
tions. Ataxia, parkinsonism and motor neurondisease have lately been described as frequent find-
ings in individuals bearing SPG11 mutations.4e6MRI usually shows severe corpus callosum
thinning and sparse white matter hyperintense fociin this disease.4 The clinical variability that is
otherwise characteristic of HSP due to SPG11mutations suggests that neuronal damage is not
restricted to these structures but this has not yetbeen proved. Modern neuroimaging techniques,
```
including voxel based morphometry (VBM) anddiffusion tensor imaging (DTI), make it possible to
```
perform automated and unbiased whole brainanalyses and to determine in vivo the distribution
of damage to neural structures.7 8 These have beensuccessfully used to study similar neurodegenera-
tive disorders, such as NiemmanePick type C andinherited ataxias.9 10 Therefore, we designed an
MRI based study to characterise white matter andgrey matter abnormalities in a cohort of patients
with confirmed SPG11 mutations.
METHODSSubject selection
We recruited 11 consecutive adult patients withautosomal recessive HSP, thin corpus callosum and
cognitive decline that were regularly followed atthe Neurogenetics Outpatient Clinic at UNICAMP
hospital between 2007 and 2010. From this group,we found five patients with mutations in the
SPG11 gene that underwent detailed clinical andMRI analyses. Severity of disease was quantified
with the Spastic Paraplegia Rating Scale.11Imaging findings were compared with a control
```
group of 15 age and sex matched individuals withno neurological abnormalities (men/women ratio
```
```
7/8 and mean age 24.063.8 years). These weremostly relatives of patients and volunteers from the
```
local community and were recruited during thestudy period. None of the patients or controls had
significant motion artefacts on MRI scans.This study was approved by our institutional
ethics committee and written informed consentwas obtained from all participants.
Molecular studiesGenomic DNA from each subject was isolated from
lymphocytes of fresh blood by standard methodsusing phenolechloroform extraction. We used
previously designed forward and reverse primers toperform PCR analyses, as described elsewhere.3 4
1Department of Neurology and
Neuroimaging Laboratory,Faculty of Medicine, University
of CampinaseUNICAMP,Campinas, Sa˜o Paulo, Brazil
2Department of Medical
Genetics, Faculty of Medicine,University of
CampinaseUNICAMP,Campinas, Sa˜o Paulo, Brazil
Correspondence toDr I Lopes-Cendes, Department
of Medical Genetics, Universityof CampinaseUNICAMP, Rua
Tessa´lia Vieira de Camargo, 126Cidade Universitaria ‘Zeferino
```
Vaz’, Campinas, Sa˜o Paulo,Brazil; icendes@unicamp.br
```
Received 24 March 2011Revised 22 February 2012
Accepted 13 May 2012
```
Franc¸a MC Jr, Yasuda CL, Pereira FRS, et al. J Neurol Neurosurg Psychiatry (2012). doi:10.1136/jnnp-2011-300129 1 of 6
```
Neurogenetics
JNNP Online First, published on June 13, 2012 as 10.1136/jnnp-2011-300129
```
Copyright Article author (or their employer) 2012. Produced by BMJ Publishing Group Ltd under licence.
```
104
```
Purified PCR products were then sequenced on an automaticsequencer MegaBACE 1000 (Amersham Bioscience, Piscataway,
```
```
New Jersey). All 40 exons and exoneintron boundaries of theSPG11 gene were investigated for each individual.
```
MRI acquisition protocolAll patients and controls underwent MRI scans on a Phillips
Achieva-Intera 3 T scanner at UNICAMP hospital. T1 and T2weighted images were acquired in axial, coronal and sagittal
planes with thin cuts. We also obtained two specific sequencesthat were later employed for VBM and DTI analyses,
```
respectively.1. Volumetric (three-dimensional) T1 gradient echo imagesd
```
```
acquired in the sagittal plane with 1 mm slice thickness (flipangle¼358, TR¼7.1 ms, TE¼3.2 ms, matrix¼240 3 240, field
```
```
of view¼24 3 24 cm).2. DTIdundertaken via a 32 direction non-collinear echoplanar
```
```
sequence (flip angle¼908, voxel size¼23232 mm3,TR¼8500 ms, TE¼61 ms, matrix¼128 3 128, field of
```
```
view¼256 3 256 mm, 70 slices with 3 mm thickness,b value ¼1000).
```
VBM protocol and analysisMRI scans produce images in DICOM format. These images
```
were converted into ANALYSE format using the MRIcro soft-ware (http://www.mricro.com). We used the SPM8 package
```
```
(Wellcome Department of Imaging Neuroscience, London, UK,http://www.fil.ion.ucl.ac.uk) running on MaTLab 8.0 to
```
perform the preprocessing steps that are required before statis-tical analyses are performed. These include spatial normalisation
```
of all image data to the same stereotaxic space; segmentationand tissue extraction; spatial smoothing; and correction for
```
```
volume changes induced by spatial normalisation (modulation).The SPM8 package has improved some of the algorithms needed
```
```
to perform these initial steps. Regarding spatial normalisation, itnow includes a more sophisticated registration model (the
```
```
DARTEL algorithm) that substantially reduces the imprecisionof intersubject registration.12
```
Table 1 Demographic, genetic and clinical data for the SPG11 patients included in the study
```
Patient No Mutation Age (years) Duration (years) Gender PN Parkinsonism Dementia MMSE SPRS
```
```
1 c. 529_533delATATT (Exon 3) 19 13 F " + ++ 14 372 c.733_734delAT (Exon 4) 31 15 M ++ " ++ 19 38
```
```
3 c.704_705delAT (Exon 4) 23 14 F " " ++ 18 324 c.118C>T (Exon 1) 21 5 M " + + 23 19
```
```
5 c.A7256G/c. 733_734delAT (Exon 40/Exon 4) 24 13 F + " + 22 26
```
```
MMSE, Mini-Mental State Examination; PN, peripheral neuropathy; SPRS, Spastic Paraplegia Rating Scale.
```
Figure 1 Results of voxelwiseanalysis showing areas of grey matter
volumetric reduction in patients withSPG11 mutations after comparison with
age and sex matched controls. Resultsare shown on the MNI152 1 mm
```
template. MNI z axis coordinates areshown (in mm) above each image. The
```
colour coded bar represents the Zscore.
```
2 of 6 Franc¸a MC Jr, Yasuda CL, Pereira FRS, et al. J Neurol Neurosurg Psychiatry (2012). doi:10.1136/jnnp-2011-300129
```
Neurogenetics
105
Processed images of patients and controls were comparedusing a voxelwise statistical analysis. We looked for differences
in white and grey matter volumes between the two groups. Wedefined the contrast searching for areas of reduced and increased
volumes both in white and grey matter. The results werecorrected for multiple comparisons using a false discovery rate of
```
5% and significant differences were set at a<0.05. We usedxjView8 (http://www.alivelearn.net/xjview8/), a MatLab
```
toolbox to display our results.
```
Tract based spatial statisticsWe obtained maps of fractional anisotropy (FA), mean diffu-
```
```
sivity (MD), radial diffusivity (RD) and axial diffusivity (AD)using the FMRIB diffusion toolbox which is part of the FSL
```
```
software V.4.1.4.13 Comparison of groups was then carried outusing tract based spatial statistics (TBSS) on the FSL software
```
V.4.1.4.14 TBSS involves several preprocessing steps before finalanalyses. All FA images are first aligned to a standard space using
the non-linear registration. The next step involves the creationof a mean FA template which then enables the creation of the
```
mean FA skeleton. Thereafter, each patient’s aligned FA map isthen projected over this skeleton; this is an essential step in the
```
processing algorithm because it removes the effect of crosssubject spatial variability. These final data are then used to
```
perform the voxelwise statistics. A similar procedure wasperformed for the other DTI parameters (MD, RD and AD). We
```
performed a two sample t test to compare group of patients andcontrols, searching for areas with FA, MD, RD and AD
Table 2 Voxel based morphometry results for volumes of grey matter in patients with SPG11
```
Cluster size (voxels)
```
```
MNI coordinates (local maxima)
```
AreasX Y Z
3765 12 13.5 13.5 R caudate nucleus, lentiform nucleus, putamen48 39 15 !9 R insula, frontal inferior gyri
4280 !19.5 9 4.5 L caudate nucleus, lentiform nucleus, putamen,globus pallidus, thalamus, claustrum
573 18 !24 3 R thalamus, mammillary body33 !46.5 !12 40.5 L precentral gyrus
48 31.5 !49.5 46.5 R inferior parietal lobule406 !30 !22.5 52.5 L precentral and postcentral gyri, middle frontal gyrus
23 39 !43.5 60 R inferior parietal lobule12 4.5 !6 57 R medial frontal gyrus, supplementary motor area
Figure 2 Results of voxelwiseanalysis showing areas of white matter
volumetric reduction in patients withSPG11 mutations after comparison with
age and sex matched controls. Resultsare shown on the MNI152 1 mm
```
template. MNI z axis coordinates areshown (in mm) above each image. The
```
colour coded bar represents the Zscore.
```
Franc¸a MC Jr, Yasuda CL, Pereira FRS, et al. J Neurol Neurosurg Psychiatry (2012). doi:10.1136/jnnp-2011-300129 3 of 6
```
Neurogenetics
106
differences between the two groups. In order to control formultiple comparisons, we applied a family wise error correction,
accepting p values <0.05. We used the Johns Hopkins whitematter DTI based atlas within the FSL toolbox to identify the
abnormal white matter fibre tracts.
RESULTSWe observed that four patients were homozygous and one was
```
compound heterozygous for mutations in SPG11 (table 1).All mutations found had been previously reported in patients
```
with autosomal recessive HSP and thinning of the corpuscallosum.3 4 15 16 They were of the non-sense type, leading to
```
premature protein truncation. Mean age of the patients was23.664.5 years (range 19e31) and mean duration of disease was
```
```
12 years (range 5e15). All patients presented with progressivespastic paraplegia and three were already wheelchair bound
```
when first evaluated. Cognitive decline was evident in allpatients according to the Mini-Mental State Examination scores
```
(adjusted for age and educational level). Detailed information foreach patient is depicted in table 1.
```
Grey matter resultsVBM analysis identified symmetrical and significant grey matter
```
volumetric reduction in both the thalamus, caudate and lentiformnuclei of patients with SPG11 compared with controls (figure 1).
```
```
We found small areas of cortical volumetric reduction, essentiallyrestricted to the precentral and postcentral gyri (table 2). There
```
were no regions with grey matter volumetric increases.
White matter resultsCerebral white matter was assessed both with VBM and TBSS.
These are essentially complementary tools as VBM providesa macroscopic map of atrophy whereas DTI based analyses
enable the identification of microstructural damage.
```
VBM identified severe white matter volumetric reductionaround the corpus callosum (figure 2). TBSS, however, revealed
```
reduced FA involving symmetrically subcortical white matter ofthe temporal and frontal lobes, the cingulated gyrus, cuneus,
```
striatum, corpus callosum, cerebellum and brainstem (figure 3).There was no region of significantly increased FA. MD maps also
```
```
revealed diffuse white matter abnormalities (figure 4). Therewere also widespread areas of increased RD, especially involving
```
```
subcortical white matter of the posterior temporal and occipitallobes (figure 4). We found areas of significantly increased AD
```
```
around the thalamus and frontal deep white matter, but not inthe posterior regions (figure 4).
```
DISCUSSIONIn this study, we investigated SPG11 mutations in all patients
```
with typical HSP with the thin corpus callosum phenotype17from our centre, and found that 45% (5/11) of the families
```
tested positive. This confirms that SPG11 is a rather commoncause of HSP but that there is also locus heterogeneity within
the limits of this phenotype. All mutations identified in thisstudy had been previously reported in a large survey of patients
from different ethnic origins.3 4 15 16 This indicates that thegenotypes of Brazilian patients with SPG11 related HSP are not
different from other populations.18Damage to grey and white matter structures other than the
corpus callosum in a cohort of genetically proven SPG11patients has not been systematically investigated. We thus used
two validated and unbiased methodsdVBM and TBSSdtoperform whole brain analysis in patients with SPG11 without
```
a priori hypotheses. We were also able to scan these patients ona high field MRI scanner (3 T), which is more sensitive in
```
detecting subtle abnormalities.19 In addition, processing ofimages to run VBM was accomplished by SPM8 running on
MaLab 8.0. This version of the software improved several of the
Figure 3 Results of tract basedspatial statistics voxelwise analysis
```
showing areas of reduced fractionalanisotropy (FA) in patients with SPG11
```
mutations after comparison with ageand sex matched controls. Areas with
reduced FA are shown in yelloweredand represent cluster based values
```
(p<0.05, corrected). Results are shownon the MNI152 1 mm template.
```
```
4 of 6 Franc¸a MC Jr, Yasuda CL, Pereira FRS, et al. J Neurol Neurosurg Psychiatry (2012). doi:10.1136/jnnp-2011-300129
```
Neurogenetics
107
required preprocessing steps but especially the spatial normal-isation algorithm.20 There is a single previous DTI based study
in SPG11 but the authors included only two patients.21 Theyperformed a voxelwise analysis but without an algorithm to
adjust for the alignment of images from multiple subjects. Theseare major limitations of the study and preclude the extrapola-
tion of the findings. Our study, in turn, enrolled a larger sampleof patients and used TBSS analysis, which improves the
sensitivity, objectivity and interpretability of DTI data.14We have found restricted areas of grey matter atrophy in
patients with mutations in SPG11. These were symmetrical andincluded the thalamus and basal ganglia. It is noteworthy that
significant volumetric reduction was only found over smallregions of the cortical mantle. These findings suggest that
neurons in different regions of the CNS may present distinctvulnerability to SPG11 related damage. This possibility is further
supported by gene expression data which show much higherspatacsin mRNA levels in subcortical structures than in the
cortex.3 This suggests that neuronal populations of deep nucleirequire higher spatacsin expression for proper functioning and
integrity. Although not widespread, grey matter damageinvolves key subcortical structures that take part in motor and
cognitive networks. Thalamic damage in combination withcorpus callosum atrophy might result in dementia and behav-
ioural disturbances in these patients. In addition, we foundsignificant volumetric reduction of the lentiform nuclei but not
of the substantia nigra. This suggests that parkinsonism, whichhas been increasingly recognised in SPG11,5 may be due to
dysfunction in the dopaminergic receptors located in theputamen and not in the dopamine producing neurons of the
midbrain. This helps to explain why levodopa and dopaminergicagonists do not improve parkinsonian features in many patients
with SPG11.In striking contrast to the grey matter results, we found
remarkable and diffuse white matter abnormalities. Aspredicted, gross structural data provided by VBM confirmed
severe corpus callosum atrophy in these individuals. However,we should emphasise the microstructural damage identified by
DTI on the cerebellum, corpus callosum, cingulated gyrus andsubcortical white matter of the temporal and occipital lobes.
These results are similar to those reported by Chen et al in twopatients with SPG11 mutations.21 In addition, we found
abnormal FA in areas not described previously, such as thebrainstem, and internal and external capsulae. Reduced FA
```
Figure 4 Results of tract based spatial statistics voxelwise analysis showing areas of increased mean diffusivity (MD), radial diffusivity(RD) and axial diffusivity (AD) in patients with SPG11 mutations after comparison with age and sex matched controls. Areas with increased
```
```
MD, RD and AD are shown in redeyellow and represent cluster based values (p<0.05, corrected). Results are shown on the MNI152 1 mmtemplate.
```
```
Franc¸a MC Jr, Yasuda CL, Pereira FRS, et al. J Neurol Neurosurg Psychiatry (2012). doi:10.1136/jnnp-2011-300129 5 of 6
```
Neurogenetics
108
indicates disruption of nerve fibre bundles, either due to axonalor myelin compromise. Experimental evidence indicates that
axonal damage takes part in this process. In a zebrafish model,Southgate et al used morfolino antisense nucleotides to knock-
down SPG11 in embryos, and found severe abnormalities ofneuronal differentiation, especially in motor pathways.22
Cranial and spinal motor nerves appeared thinner and withreduced numbers of axons. Oligodendrocyte and myelin abnor-
malities probably also contribute to white matter microstruc-tural alterations. Proton magnetic resonance spectroscopy of
```
frontal white matter showed mild reduction of N-acetylas-partate (NAA) levels but a prominent increase in choline (Cho)
```
levels in a patient bearing the c.1951C>T mutation at SPG11.4Analysis of AD and RD maps also provides some insight into
the substrate of white matter damage in SPG11 related HSP. ADmeasures diffusivity along the main direction of diffusion and is
considered a marker of axonal damage.23 By contrast, RD eval-uates diffusion that is orthogonal to the principal diffusion
direction. Experimental data indicate that RD abnormalities areassociated with myelin and/or oligodendrocyte damage.24 In our
patients, we found increased AD and RD, which indicates thatboth axonal damage and demyelination indeed take place in
SPG11. RD abnormalities were, however, much more wide-spread than those related to AD, suggesting that CNS myelin is
severely affected in the condition and this is especiallyprominent in posterior white matter.
An unsettled issue about SPG11 is the nature of corpuscallosum thinning as it is not clear whether it is due to true
atrophy or hypoplasia. Although we are not able to definitivelyanswer this question with the present data, we had the oppor-
tunity of studying two patients who had been part of a previousprospective study.25 Indeed, we could document that both
```
patients presented with progressive volumetric reduction of thecorpus callosum over a 1 year period (data not shown). This
```
suggests that progressive corpus callosum atrophy occurs at leastin some patients with SPG11 mutations.
HSP due to SPG11 mutations is a relatively new and rarecondition, thus enabling us to enrol only a small number of
patients for MRI scans. Regarding group comparisons, we triedto mitigate this with a large number of age and sex matched
controls and a conservative statistical approach. Despite theselimitations, our results provide insight into the neurobiology of
the disease and help to understand many of the symptomspresented by these patients. Further studies are needed to eval-
uate the usefulness of MRI as a progression biomarker in SPG11related HSP.
```
Contributors 1¼Research project: (A) conception, (B) organisation, (C) execution.2¼Statistical analysis: (A) design, (B) execution, (C) review and critique.
```
```
3¼Manuscript: (A) writing of the first draft, (B) review and critique. MCF: 1, 2A, 2Band 3A. CLY: 1C, 2B, 2C and 3B. FRSP: 1C, 2B, 2C and 3B. AD: 1A, 2C and 3B.
```
CML-R: 1B, 1C, 2B and 3B. MVR: 1B, 1C and 2B. FC: 1A, 1B, 2C and 3B. IL-C: 1A, 1B,2C and 3B.
```
Funding MCF received a post-doctoral fellowship from Fundac¸a˜o de Amparo a`Pesquisa do Estado de Sa˜o PauloeFAPESP, Sa˜o Paulo, Brazil (2008/58605-7). IL-C and
```
```
FC are supported by FAPESP and Conselho Nacional de Pesquisa (CNPq, Brazil). Thefunding agencies did not interfere with the design of the study, collection of the data
```
or drafting of the manuscript.
Competing interests None.
```
Ethics approval Ethics approval was provided by Comiteˆ de E´tica da Faculdade deCieˆncias Me´dicas (UNICAMP).
```
```
Provenance and peer review Not commissioned; externally peer reviewed.
```
Data sharing statement There are no additional unpublished data from thisresearch. All information is included in the manuscript, tables and figures.
REFERENCES1. Salinas S, Proukakis C, Crosby A, et al. Hereditary spastic paraplegia: clinical
```
features and pathogenetic mechanisms. Lancet Neurol 2008;7:1127e38.2. Słabicki M, Theis M, Krastev DB, et al. A genome-scale DNA repair RNAi screen
```
```
identifies SPG48 as a novel gene associated with hereditary spastic paraplegia. PLoSBiol 2010;8:e1000408.
```
3. Stevanin G, Santorelli FM, Azzedine H, et al. Mutations in SPG11, encodingspatacsin, are a major cause of spastic paraplegia with thin corpus callosum. Nat
```
Genet 2007;39:366e72.4. Hehr U, Bauer P, Winner B, et al. Long-term course and mutational spectrum of
```
```
spatacsin-linked spastic paraplegia. Ann Neurol 2007;62:656e65.5. Anheim M, Lagier-Tourenne C, Stevanin G, et al. SPG11 spastic paraplegia. A new
```
```
cause of juvenile parkinsonism. J Neurol 2009;256:104e8.6. Orlacchio A, Babalini C, Borreca A, et al. SPATACSIN mutations cause autosomal
```
```
recessive juvenile amyotrophic lateral sclerosis. Brain 2010;133:591e8.7. Ashburner J, Friston KJ. Voxel-based morphometrydthe methods. Neuroimage
```
```
2000;11:805e21.8. Le Bihan D, Mangin JF, Poupon C, et al. Diffusion tensor imaging: concepts and
```
```
applications. J Magn Reson Imaging 2001;13:534e46.9. Walterfang M, Fahey M, Desmond P, et al. White and grey matter alterations in
```
```
adults with NiemannePick disease type C: a cross-sectional study. Neurology2010;75:49e56.
```
10. Alcauter S, Barrios FA, Dı´az R, et al. Gray and white matter alterations inspinocerebellar ataxia type 7: an in vivo DTI and VBM study. Neuroimage
```
2011;55:1e7.11. Schu¨le R, Holland-Letz T, Klimpe S, et al. The Spastic Paraplegia Rating Scale
```
```
(SPRS): a reliable and valid measure of disease severity. Neurology 2006;67:430e4.12. Yasuda CL, Betting LE, Cendes F. Voxel-based morphometry and epilepsy. Expert
```
```
Rev Neurother 2010;10:975e84.13. Smith SM, Jenkinson M, Woolrich MW, et al. Advances in functional and structural
```
```
MR image analysis and implementation as FSL. Neuroimage 2004;23(Suppl 1):S208e19.
```
14. Smith SM, Jenkinson M, Johansen-Berg H, et al. Tract-based spatial statistics:voxelwise analysis of multi-subject diffusion data. Neuroimage 2006;31:1487e505.
15. Stevanin G, Azzedine H, Denora P, et al; SPATAX consortium. Mutations in SPG11are frequent in autosomal recessive spastic paraplegia with thin corpus callosum,
```
cognitive decline and lower motor neuron degeneration. Brain 2008;131:772e84.16. Paisan-Ruiz C, Dogu O, Yilmaz A, et al. SPG11 mutations are common in familial
```
```
cases of complicated hereditary spastic paraplegia. Neurology 2008;70:1384e9.17. Nakamura A, Izumi K, Umehara F, et al. Familial spastic paraplegia with mental
```
```
impairment and thin corpus callosum. J Neurol Sci 1995;131:35e42.18. Denora PS, Schlesinger D, Casali C, et al. Screening of ARHSP-TCC patients
```
```
expands the spectrum of SPG11 mutations and includes a large scale gene deletion.Hum Mutat 2009;30:E500e19.
```
19. Alvarez-Linera J. 3T MRI: advances in brain imaging. Eur J Radiol2008;67:415e26.
20. Ashburner J. A fast diffeomorphic image registration algorithm. Neuroimage2007;38:95e113.
21. Chen Q, Lui S, Wang JG, et al. Diffusion tensor imaging of two unrelated Chinesemen with hereditary spastic paraplegia associated with thin corpus callosum.
```
Neurosci Lett 2008;441:21e4.22. Southgate L, Dafou D, Hoyle J, et al. Novel SPG11 mutations in Asian kindreds and
```
```
disruption of spatacsin function in the zebrafish. Neurogenetics 2010;11:379e89.23. Song SK, Sun SW, Ju WK, et al. Diffusion tensor imaging detects and differentiates
```
```
axon and myelin degeneration in mouse optic nerve after retinal ischemia.Neuroimage 2003;20:1714e22.
```
24. Song SK, Yoshino J, Le TQ, et al. Demyelination increases radial diffusivity in corpuscallosum of mouse brain. Neuroimage 2005;26:132e40.
25. Franc¸a MC Jr, D’Abreu A, Maurer-Morelli CV, et al. Prospective neuroimaging studyin hereditary spastic paraplegia with thin corpus callosum. Mov Disord
```
2007;22:1556e62.
```
PAGE fraction trail=6
```
6 of 6 Franc¸a MC Jr, Yasuda CL, Pereira FRS, et al. J Neurol Neurosurg Psychiatry (2012). doi:10.1136/jnnp-2011-300129
```
Neurogenetics
110
```
Expert Rev. Neurother. 13(5), (2013)484
```
Review
elderly population: although variable, the prevalence-estimates
of these lesions are very high, reaching 95% [7,8]. WM hyper-
intensities can be measured by visual rating scales [9,10] or quan-
titative methods [11], which take into account the location and
volume of WM lesions. In this section, the authors review the
relationship of WM hyperintensities with AD, cognitive decline,
neuropathology and diagnosis of dementia.
The neuropathological correlates of WM hyperintensities are
still not completely understood and may reflect local demyeli-
nation, loss of axons and oligodendroglial cells, astrogliosis,
fibrohyanolitic arterioles, and dilatation of perivascular spaces,
corresponding to incomplete infarctions [8]. In the general popu-
lation, the presence of WM hyperintensities is related to major
vascular-related risk factors, such as hypertension, diabetes, smok-
ing and hypercholesterolemia, as well as with signs of endothelial
dysfunction [12]. WM hyperintensities are frequently taken as due
to cerebrovascular disease, given such association with cardio-
```
vascular risk factors; also, a number of histopathological studies
```
have found signs of microinfarcts and markers of hypoxia in the
regions where WM hyperintensities are located [13]. However, it
is important to note that some studies did not find evidence of
ischemia in association with such lesions, even in extensive deep
WM hyperintensities [13]. Apart from ischemia, there are indica-
tions that WM hyperintensities may be related to blood–brain
barrier dysfunction [14] and microglial activation [15]. Thus, there
is evidence suggesting that the etiopathological substrate of WM
hyperintensities is heterogeneous and the common assumption
that their causality is fully explained by cerebrovascular changes
may lead to an oversimplification of the phenomena.
The interaction between cerebrovascular disease and AD is
quite frequent and complex, and may occur in two ways: firstly by
the presence of vascular lesions in patients with AD and secondly,
by the sharing of major vascular-related risk factors [16]. In addi-
tion, endothelial damage and amyloid angiopathy may be present
in AD. The pattern of WM changes found in AD seems to be
```
more subtle than that associated with vascular dementia (VD),
```
but nonetheless the differentiation between AD and VD may be
difficult [17]. This is a relevant topic because cerebrovascular dis-
ease is the second main cause of cognitive decline [18]. One of the
most commonly used methods to characterize the cerebrovascular
risk and to distinguish between AD and VD is the Hachinski
```
Ischemic Score (HIS) [19] or its modified version [20,21]. The sensi-
```
tivity and specificity of the HIS to distinguish AD from VD was
```
high (89%) in a study of 312 patients with dementia but it was
```
not accurate in distinguishing AD or VD from mixed dementia
[22]. More recently, a longitudinal study showed that higher HIS
scores significantly increased the odds of incident VD relative to
AD within 5 years [23].
The relationship between the presence and intensity of WM
hyperintensities and the existence or severity of cognitive deficits
is still controversial. Cross-sectional studies of elderly individuals
have reported an association of WM abnormalities with episodic
and working memory deficits, executive dysfunction, and neu-
ropsychiatric symptoms, particularly depression [24–27]. However,
there are also studies that could not demonstrate any relationship
between WM hyperintensities and cognitive deficits [28,29]. Motor
impairments such as decreased postural and gait stability have also
been associated with WM hyperintensities [30].
Amyloid deposition in the brain, a hallmark of AD [31], is seen
initially and most prominently in the entorhinal and perirhinal
cortex [32,33] and can nowadays be evaluated in vivo with
molecular imaging methods using PET [34]. Two recent neuro-
imaging studies could not find significant correlations between
WM hyperintensities and brain amyloid burden in vivo [25,28].
Conversely, in a study that combined MRI and amyloid depo-
sition imaging with PET [35], the authors showed that, among
elderly individuals with significant brain amyloidosis, those with
clinically defined AD presented increased volumes of WM hyper-
intensities when compared with normal elders, thus suggesting
that clinical dementia may be the result of a ‘double hit’ on the
```
brain: amyloid deposition and WM degeneration [35]. This is in
```
accordance with a longitudinal study of 804 elderly individu-
als from the AD neuroimaging initiative, which reported that
higher baseline WM hyperintensity volumes were associated with
decreases in global measures of cognition [36] and also with a
community-based epidemiological study that reported that vol-
ume of parietal WM hyperintensities predicted incident AD [37].
Another relevant finding of the aforementioned study is that the
volume of WM hyperintensities did not differ between subjects
with and without significant amyloid deposition [35]. In other
words, although WM hyperintensities seem to occur indepen-
dently of AD pathology, they may increase the risk of developing
cognitive decline, especially in those who have undergone other
brain insults such as extensive amyloid deposition [35,38].
In conclusion, WM hyperintensities are very common in both
AD and in the general elderly population. These brain lesions can-
not be taken as specific to AD, but rather may indicate increased
cerebrovascular brain damage and vulnerability to cognitive
decline [35,39]. It is also important to note that there are other
brain lesions caused by vascular pathology – such as gross infarcts
detectable with MRI – that may have strong effects on cognition
[28]. In fact, a recent study has shown that in a sample of elderly
subjects – including those with normal cognition and those with
```
cognitive impairment – the relationship of cognition (executive
```
```
function, verbal and nonverbal memory) with brain infarcts was
```
stronger than its association with amyloid deposition [28].
Volumetric abnormalities of WM in AD & MCI
T1-weighted MRI scans can detect quantitative changes in WM
volume of separate regions in groups of patients with neuro-
psychiatric disorders compared with healthy control groups
matched for demographic variables. Two strategies have most
often been employed to perform such quantitative measurements
and between-group comparisons: the delineation of regions-of-
```
interest (ROI) around selected brain structures (manually or in
```
```
an automated fashion); or voxel-based morphometry (VBM), an
```
automated technique that uses T1-weighted images to perform
voxel-wise statistical tests with the purpose of uncovering sub-
tle brain volume changes in association with neuropsychiatric
disorders [40,41].
Radanovic, Pereira, Stella et al.
111
485www.expert-reviews.com
Review
Morphometric MRI studies of AD using the ROI-based
approach have focused on the detection of volume deficits of the
hippocampus and other medial temporal lobe regions, as well
as other selected cortical regions. Differently, VBM analyses are
performed separately on either gray or WM tissue compartments
across the whole brain [42,43]. Suitable for group comparisons, the
application of VBM has been widespread to identify gray matter
volume abnormalities in AD samples relative to elderly healthy
control groups [41,43–46]. The VBM approach has also been used to
investigate the risk for dementia in premorbid conditions such as
MCI [9], and recent meta-analyses of VBM studies demonstrated
atrophy of the hippocampus and parahippocampal gyrus as the
most reliable predictors of progression from amnestic MCI to
AD [47].
In the first VBM study that investigated the topography of WM
volume deficits affecting the corpus callosum in AD subjects,
Chaim et al. showed that callosal atrophy was most significant
in the anterior splenium and isthmus, which are crucial callosal
fiber tracts that interconnect the two cortical hemispheres [43].
Although less significantly, there were also volume reductions in
the rostral genu as well as the anterior and posterior regions of
the callosal body in AD patients relative to controls [43]. There
was also a positive correlation between the degree of cognitive
decline as assessed by the Mini-Mental State Examination and the
volume of the anterior body of the corpus callosum. VBM-based
findings of corpus callosum volume deficits in association with
AD [48] complement findings of callosal shape abnormalities as
assessed in sophisticated MRI studies that used high-dimensional
warping methods [49], as well as the results of earlier ROI-based
morphometric MRI investigations comparing AD patients to
elderly healthy controls [50–52].
Several other morphometric MRI studies of AD, using either
the ROI-based approach or VBM, have reported WM atrophy of
subcortical regions in AD patients compared with healthy elderly
individuals affecting temporal lobe structures in addition to the
corpus callosum [53–55], as well as other WM tracts including
the inferior longitudinal fasciculus [56]. A recent meta-analysis
including eight VBM studies reported significant WM volume
reduction in temporal lobe regions including the parahippocam-
pal gyrus bilaterally, as well as the posterior corpus callosum in
AD patients relative to elderly controls [48].
Structural abnormalities of the splenial portion of the corpus
callosum in AD may be related to findings of neuronal loss in the
temporoparietal cortical regions that are interconnected by this
callosal subregion, with an unfavorable impact on episodic mem-
ory performance among other cognitive aspects. Additionally,
volume reduction of the anterior corpus callosum may explain
the decline of executive functions that may be seen even at early
stages of AD, as this brain region connects interhemispheric fron-
tal cortical regions [43]. WM volume increase in samples of AD
patients relative to healthy controls has not been detected in VBM
investigations to date [48].
A few VBM studies have also investigated groups of MCI
individuals in regard to WM volumes, but to date, these studies
have reported conflicting findings. For instance, one VBM study
reported WM atrophy in periventricular areas in a group of AD
```
patients relative to controls (mainly in the anterior corpus cal-
```
```
losum and the WM of associative cortical regions), but no WM
```
volume deficits in a sample of amnestic MCI subjects compared
with the same healthy control group [44]. Conversely, there have
been reports of WM volume decrements in the medial temporal
lobe in a group of amnestic MCI subjects compared with age-
matched controls, which predicted significantly episodic memory
decline as much as gray matter volumes in the hippocampal region
[56]. In individuals at risk for AD, dysfunction of episodic memory
might be influenced by changes in WM pathways connecting the
hippocampus and neocortical regions.
Finally, another point of interest refers to the relationship
between volumetric deficits in gray and WM compartments in
the same samples of AD patients or MCI subjects [55,57]. One
such VBM investigation showed that the degree of gray matter
hippocampal atrophy in AD patients was specifically correlated
to decreased WM volume in the cingulum bundle. As the same
AD sample was also investigated with PET after injection of18
F-fluorodeoxyglucose, the authors were able to demonstrate that
the WM cingulum disruption was significantly correlated with
the degree of glucose hypometabolism in the posterior cingulate
```
cortex (a very early functional imaging feature associated with
```
```
the diagnosis of AD), as well as with hypometabolism in other
```
subcortical and cortical regions. These findings provide support to
the notion that gray matter abnormalities and deficits in long WM
tracts are related to each other in AD, leading to disconnection of
multifocal neural networks relevant to cognitive processing [58].
Despite the interest raised by the above data, limitations of
the VBM approach to assess WM volumes need to be acknowl-
edged. In regard to the corpus callosum, for instance, inter-subject
variations in callosal location may emerge secondary to ventri-
cle dilatation or between-group differences in callosal shape [59],
interfering with the process of spatial normalization and poten-
tially confounding VBM-based group comparisons. The spatial
normalization step in the VBM methodology, whereby images
are warped to conform to a standardized anatomical space, may
be prone to inaccuracies that are more likely to occur when the
```
degree of brain structural inter-subject variations is wider (as in
```
```
the case of neurodegenerative disorders) [59].
```
One additional approach of demonstrated validity to investi-
gate morphometric brain abnormalities associated with AD and
MCI consists of analyzing the nonlinear deformation fields that
result from registering the MRI datasets of individual subjects to
a standardized reference brain space, using such information to
infer local differences in brain volume or shape [60,61]. Two tech-
niques based on this principle, referred to as deformation-based
morphometry and tensor-based morphometry, have been infre-
quently applied to demonstrate WM morphological abnormalities
in AD and MCI patients relative to healthy controls [62].
Finally, computational methods for measuring regional brain
thickness changes have also been applied to investigate WM
abnormalities associated with AD using structural MRI data-
sets. These include: mesh-based geometrical modeling meth-
ods, recently used to demonstrate reduced callosal thickness
MRI studies & white matter abnormalities
112
```
Expert Rev. Neurother. 13(5), (2013)486
```
Review
```
in patients with severe AD relative to unaffected controls [49];
```
and the FreeSurfer suite, a surface-based approach that allows
thickness and volume measurements of separate regions across
the entire brain to be obtained on an automated fashion, after
segmentation of separate gray matter, WM and cerebrospinal
fluid compartments [63]. Several studies using FreeSurfer soft-
ware have confirmed and extended VBM findings of gray mat-
ter changes associated with AD and MCI, revealing reductions
in both volume and thickness of key brain regions [64,65]. The
FreeSurfer approach has also been applied in a study that identi-
fied differences of WM volume between AD patients and elderly
```
controls: AD-related decreases in WM volume were found in
```
para hippocampal, entorhinal, precuneus, inferior parietal and
middle frontal WM [66]. The FreeSurfer methodology provides
volumetric measures in native space and information can be
extracted for individual subjects, rather than solely for statistical
group comparisons. Moreover, there is evidence that FreeSurfer
may be more suitable for longitudinal investigations of regional
brain volume changes over time as compared with voxel-based
methods [67].
Microstructural WM abnormalities as assessed by DTI
Despite the usefulness of the above MRI methods employed to
assess WM, either by quantifying hyperintense lesions or meas-
uring WM volumes and thickness, DTI methods have a greater
potential to provide detailed information about the structural
characteristics of WM tracts in the brain. DTI is a technique
based on the concept of random movement of water molecules
in brain tissue, which is altered when there are microstructural
lesions in WM fiber bundles. Indices of WM integrity are afforded
```
by measuring mean diffusivity (MD) and fractional anisotropy
```
```
(FA) [68]. There is recent empirical demonstration that volumetric
```
and DTI analyses of WM yield different and complementary
results in regard to the pathophysiology of AD [69].
Since the development of DTI methods, there have been a large
number of cross-sectional DTI studies comparing samples of AD
patients and MCI subjects relative to elderly control groups [70–76].
The DTI literature has been evaluated in recent meta-analyses,
which have indicated that both in AD and MCI samples relative
to healthy controls, there are significant changes in WM micro-
structure in the corpus callosum as well as in other brain regions
including the cingulum and parahippocampal region [77,78], as well
as the longitudinal and uncinate fascicule [74–76]. As expected, DTI
investigations have indicated greater loss of WM integrity in AD
patients relative to MCI individuals, affecting key brain regions
```
such as the corpus callosum and fornix (which contains efferent
```
```
fibers from the hippocampal region) [71,74,79]. WM microstructural
```
changes as assessed by DTI are significantly associated with the
degree of cognitive decline, and might be considered as predictors
of AD pathology [71]. There is also indication that DTI indices
```
(particularly MD) provide high levels of diagnostic accuracy to
```
differentiate MCI subjects from healthy controls, possibly with
larger effect sizes in comparison to measures of hippocampal vol-
ume [77]. On the other hand, a recent study showed that FA indices
in the fornix predicted conversion to AD in a sample of 23 MCI
```
subjects (from which six developed AD over 2.5 years) with an
```
impressive accuracy of 95% [80]. However, more studies with
greater samples are needed to replicate and confirm these findings.
High-resolution DTI scanning enables the investigation of spe-
cific WM tracts such as the perforant path, which connects the
entorhinal cortex to the hippocampus [73,81,82]. The entorhinal
cortex is seen as critically relevant to memory processing as it
provides the main input from the cortex to the hippocampal for-
mation [83,84]. Postmortem studies have documented neuropatho-
```
logical findings characteristic of AD (i.e., neurofibrillary tangles)
```
and decreased neuronal density in the entorhinal cortex of patients
```
in the earliest stages of AD [32,33]; such degenerative changes are
```
thought to affect the perforant path and lead to an isolation of
the hippocampus from cortical input [85,86]. In vivo DTI studies
identified decreased FA and increased MD – suggestive of WM
damage and/or loss of fibers – in normally appearing WM of the
perforant path in AD and MCI [73,82]. Moreover, DTI indices of
the perforant path integrity have been shown to correlate with
declarative memory performance [82].
One important DTI question arises with regards to the assess-
ment of the relationship between changes in WM microstructure
and gray matter atrophy. A common multimodal integration that
deals with such issue regards to the combination of DTI indi-
ces with gray matter volume indices as assessed using VBM. A
pioneering study that used this approach detected widespread
```
WM changes in AD patients as assessed with DTI; however,
```
these degenerative changes were largely unrelated with gray mat-
ter volume measurements, suggesting that both features would
be independent pathological aspects in the progression of AD
[87]. A relative independence between altered diffusivity in the
parahippocampal WM as assessed with DTI and volumetric
measurements of the hippocampal region were also reported in a
subsequent investigation [73]. Conversely, in one other study, FA
indices both in anterior and posterior regions of the corpus callo-
```
sum in AD patients (but not in healthy controls) were significantly
```
correlated with gray matter volumes in several cortical regions [70].
The latter findings support a view that axonal impairments in the
corpus callosum are closely linked to gray matter degeneration in
the cortical areas interconnected by these callosal fibers in AD
[43,70]. Moreover, a study that investigated whole brain WM also
found correlations between regional gray matter volume and DTI
indices of WM degeneration, this time in the left frontal and
temporal cortices [82].
One other important, but as yet relatively unexplored, issue
in regard to the possibility that WM abnormalities, as detected
by reduced FA, may also be significantly related to gray matter
volume deficits as assessed by VBM in patients with MCI due to
AD. Further MRI studies with complementary information from
such gray and WM measurements may improve the accuracy to
distinguish AD patients from MCI subjects and healthy controls.
Finally, one of the methods used most often recently to quan-
```
tify diffusion images is Tract-Based Spatial Statistics (TBSS),
```
which allows comparisons of the integrity of WM tracts across
different groups by means of projecting the FA onto an alignment
tract representation, with improved sensitivity [88]. The TBSS
Radanovic, Pereira, Stella et al.
113
487www.expert-reviews.com
Review
methodology is a promising approach to examine the integrity
of WM tracts and it may also be used to classify distinct groups
of subjects. This procedure has been applied to infer WM micro-
structural changes in MCI that may predict conversion to AD
[89–91]. Significant FA differences in the fornix, cingulum and cor-
pus callosum have been observed between MCI subjects that con-
verted to AD and those that did not [89]. The TBSS approach has
also shown that amnesic MCI patients display FA abnormalities
relative to healthy controls consistent with pathological findings
```
of AD (involving the temporal lobe, corpus callosum and fornix,
```
```
among other regions), while non-amnesic MCI patients display
```
more widespread and variable patterns of WM abnormalities, but
relatively sparing the temporal lobe [90].
Limitations & caveats in the interpretation of DTI
findings
When interpreting WM results from neuroimaging studies, it
is important to remember that these findings represent indirect
estimates of the brain anatomy. Therefore, one type of neuro-
imaging finding may result from different changes in the brain
microstructure [92,93]. For instance, as addressed above, WM
hyperintensities may be associated with different pathological
findings, such as cerebrovascular disease, microglial activation
and/or blood–brain barrier dysfunction.
In DTI studies, findings of regional lower FA have been inter-
```
preted as indicating decreased WM integrity (an unspecific term
```
that generally encompasses loss of myelination, axonal degen-
```
eration or atrophy and/or increased membrane permeability).
```
However, one other plausible explanation is that FA changes would
be due to variations in axonal diameter or atypical packing density
of axons [92–94]. Moreover, decreased anisotropy may simply result
from different axonal alignment: regional anisotropy differences
may indicate, in one group of subjects, that the axons are all
aligned in the same direction, while in another group this same
brain region contains branching or crossing fibers [92]. As noted
elsewhere, in its current state, ‘DTI is useful for localizing and
quantifying the anatomical abnormalities, but it is apparently not
adequate to investigate the histopathological background of the
diseases’ [93]. For a recent and thorough review of the limitations
of DTI methods, the reader is referred to Jones et al. [92].
Relationship between WM changes & neuropsychiatric
syndromes in AD
Although MRI studies of AD have predominantly concentrated
on investigating the relationship between brain abnormalities and
measures of cognitive decline, it is also critical to drive attention to
```
neuropsychiatric symptoms (such as psychosis, agitation, depres-
```
```
sion and apathy). These are highly frequent in AD patients, being
```
associated with greater disease severity and increased mortality [95].
Morphometric MRI studies, by means of VBM, have demon-
strated that distinct patterns of gray matter abnormalities are cor-
related with the presence of neuropsychiatric syndromes in mild
AD, including associations between: delusions and gray matter
```
reduction in fronto-parietal regions; agitation and gray matter
```
```
reduction in the insula and anterior cingulate cortex; and apathy
```
and decreased gray matter volume in frontal, anterior cingulate
and striatal regions [96]. Similar regional-specific associations have
been reported in more recent morphometric MRI investigations
using large AD and MCI samples [97]. However, these studies did
not investigate if degenerative WM volume deficits could also be
associated with neuropsychiatric syndromes.
Such investigations of WM abnormalities would be highly
relevant, since the neural substrate underlying neuropsychiatric
syndromes in neurodegenerative diseases has not yet been
clearly defined. Using a sample of AD patients who displayed
delusions over a period of 2 years, an interesting VBM study
recently examined neuroanatomical changes both in gray matter
and WM compartments before delusions onset [98]. The authors
found significantly smaller gray matter volume bilaterally in the
parahippocampal gyrus, inferior frontal gyrus, right orbitofrontal
cortex, and left insula in AD patients who developed delusions
compared with those without delusions. Conversely, the authors
did not observe significant WM changes in any brain regions
among patients who developed delusions compared with those
without psychotic symptoms. Thus, the role of WM degenerative
changes to predict the emergence of neuropsychiatric syndromes
in AD patients remains to be clarified.
More recently, neuropsychiatric symptoms have also been
addressed in DTI studies investigating relatively modest MCI
and AD samples. In one of these studies, the relationship between
neuropsychiatric symptoms and WM integrity was examined
in the fornix, cingulum bundle and splenium of the corpus cal-
losum [99]. Expecting similar associations across AD and MCI
subjects, the authors combined both groups in their analyses.
Patients in the lowest tertile regarding anterior cingulum FA were
more likely to exhibit irritability, agitation, dysphoria, apathy,
and night-time behavioral disturbances. After accounting for the
influence of the degree of cognitive decline using Mini-Mental
State Examination scores, only irritability remained significantly
associated with reduced FA in the cingulum [99]. Another DTI
study explored the association between apathy and WM integrity
in AD patients. The authors found negative statistical correlations
between scores on an apathy scale and FA in the right anterior
cingulum as well as in the right thalamus and bilateral parietal
regions, after taking into account the influence of demographic
and cognitive decline variables [100].
Possible mechanisms underlying volume deficits &
integrity changes of WM tracts in AD & MCI
It has not yet been possible to fully clarify the mechanisms that
specifically underlie the AD-related pathological changes in
WM tracts detected in the MRI studies reviewed herein, nor the
relationship between the degeneration of such subcortical WM
interconnections and the gray matter changes that characterize AD.
One proposed mechanism is that gray matter degeneration
would lead to WM deficits through demyelination in efferent
pathways connecting the hippocampus and amygdala to the para-
hippocampal gyrus and the temporal lobe neocortex, extending
towards the corpus callosum. Amyloid plaques and neurofibrillary
tangles affecting gray matter could drive anterograde Wallerian
MRI studies & white matter abnormalities
114
```
Expert Rev. Neurother. 13(5), (2013)488
```
Review
degenerative changes in WM tracts [101], particularly in close
proximity to cortical regions. Wallerian degeneration affecting
the posterior portion of the corpus callosum would disorganize
axonal interconnections among temporo-parietal regions, which
are known to be affected early over the course of AD [45].
One alternative explanation is that primary, AD-related patho-
logical WM changes would lead to decreased WM volume and
contribute to cortical gray matter degeneration. Within this frame-
work, damage to WM is seen as an early phenomenon in AD,
caused either by microvascular ischemic events or other myelin-
related defects, with amyloid and tau pathologies representing sec-
ondary effects [102]. Such primary WM abnormalities would lead
to interconnection deficits and axonal injuries reducing synaptic
activity, even in prodromal MCI stages. This myelin model of AD,
proposed by Bartzokis, is based on the observation that the myeli-
nation of the human brain is dynamic and presents an inverted
U-shaped trajectory throughout the lifespan [102]. According to this
model, it is necessary to understand the pathophysiology of AD
in light of age-related myelin toxicity, which has been suggested
to be an earlier event that may not only be induced by, but also
promote β-amyloid aggregation and tau deposits [102]. According
to this model, brain amyloidosis can be considered a late patho-
logical event and therefore treatments aiming at amyloidosis may
not be successful.
Recently, a retrogenesis model has been proposed to explain the
decreased WM integrity in AD [103], according to which there is
firstly degeneration of the late-myelinating WM tracts, such as the
inferior and superior longitudinal fascicule and the uncinate fas-
ciculus, a proposition supported by findings of reduced FA in these
regions in AD patients [74,76,87]. Early-myelinating tracts would only
be affected later in the course of AD. According to the retrogen-
esis model, dropping off WM integrity reflects myelin breakdown
occurring as a reverse pattern of the myelogenic process [102].
It is actually possible that both primary and secondary WM
degeneration processes are present in AD and MCI [72,73].
Moreover, the fact that oligodentrocytes – the cells that produce
myelin – are vulnerable to a diversity of insults, such as hypop-
erfusion, iron toxicity, oxidative damage, glucocorticoids, alco-
hol, cocaine, brain trauma and β-amyloid oligomers makes WM
degeneration a pivotal element of the neuropathology of cogni-
```
tive decline and AD (for a thorough review, see Bartzokis [104]).
```
Regardless of the underlying nature and sequencing of white and
gray matter changes over the disease course, WM abnormali-
ties undoubtedly reduce cortico-cortical and cortico-subcortical
connectivity in AD subjects. Future neuroimaging studies with
improved methods are likely to better delineate how critically such
WM changes contribute, not only to cognitive decline but also,
to the emergence of neuropsychiatric syndromes. These studies
are also expected to contribute further to improve the accuracy of
diagnosis of AD and MCI.
Five-year view
This review shows that current neuroimaging technology allows
the quantification of regional indices of human WM struc-
ture reliably in vivo. The MRI studies addressed herein have
demonstrated unequivocally that WM abnormalities in the brain
are detectable in early stages of AD and in MCI. Between-group
differences have been clearly identified when comparing AD
and/or MCI patients to elderly controls, and significant asso-
ciations between WM structure and cognitive performance and
prognosis have been documented. These changes affect key com-
ponents of a complex brain network relevant to episodic memory
and other cognitive processes, including fiber connections that
directly link medial temporal structures and different regions of
the corpus callosum. Abnormalities in these network nodes may
influence one another, and the profile of cognitive deficits and
emergence of neuropsychiatric syndromes may be best explained
in terms of disturbances of such brain networks rather than by
damage to a specific subcortical structure. Degeneration of WM
fiber pathways causes disconnection among neural cells, with loss
of myelinated axons resulting in reduced signaling and synaptic
activity [105]. Overall, these findings encourage the exploration of
a number of important novel research avenues in the field of WM
investigations in AD and MCI.
The literature on WM changes associated with AD has led
some authors to suggest that such abnormalities could be an
important target for aiding in the diagnosis and disease moni-
toring in AD [93]. DTI studies have provided interesting results
```
regarding: identification of WM differences between AD and
```
```
VD [106]; discrimination between individual AD or MCI patients
```
```
and controls [62,107–110]; distinction of individual patients with
```
AD from those with frontotemporal lobar degeneration [111] and
characterization of treatment effects of galantamine – a cholinest-
erase inhibitor approved for the treatment of AD – in the WM of
AD patients [112]. However, despite such encouraging findings,
DTI methods are still not developed as robust clinical tools in the
field of brain aging and dementia [113]. Though much progress has
been made in the past years, there is still much to be improved
in terms of in vivo WM imaging methods before MRI indices
of WM integrity can be established as accurate and reliable bio-
markers in the AD field [114]. A number of these limitations have
been evoked in the reasoning why DTI was not included in the
MRI core of the AD neuroimaging initiative [114]. These issues
were ‘uncertainty about long-term test-retest precision’, ‘absence
of widely available phantoms to calibrate measurements of dif-
fusion’ and ‘minimal evidence of diagnostic efficacy in AD’ [113].
In other words, advances in multiple fronts are required before
DTI can be implemented in clinical practice for AD diagno-
sis and monitoring. One important research field that must be
explored further in the near future regards to the assessment of
advanced acquisition methods to increase spatial resolution of
DTI data and more accurately extract information from specific
small WM tracts of critical relevance to AD and MCI, such as
the perforant path [115].
One other important issue for future research refers to multi-
modal neuroimaging approaches. By applying different acquisi-
tion protocols in the same imaging session, MRI techniques may
provide complimentary information about brain structure and
```
function in one single cohort of individuals. Sophisticated com-
```
putational and statistical methods also allow the combination
Radanovic, Pereira, Stella et al.
115
489www.expert-reviews.com
Review
of information from MRI data with other imaging modalities,
including the use of PET for measuring regional glucose metabo-
lism and molecular imaging. For instance, structural connectivity
– measured with DTI – can provide useful information to assist
the interpretation of neurofunctional results as assessed with
functional MRI or PET imaging, as it is known that structural
and functional connectivity are intimately related [116]. In accord-
ance with this idea, glucose hypometabolism in the posterior
cingulate cortex – a common feature of AD – was associated with
decreased FA in the descending cingulum in a study that acquired
DTI and PET data from MCI and AD patients [107]. These fib-
```
ers connect the hippocampus to neocortical regions; thus, these
```
results provide further support to the notion that disconnectivity
between the medial temporal lobe and medial parietal cortex con-
tributes to the hypometabolism in the posterior cingulate cortex
found in AD [117]. Another example of a multimodal study is one
recent report showing that regional decreased FA in the cingulum
of amnestic MCI patients was associated with failure to deactivate
the inferior parietal lobe and precuneus, during an object recogni-
tion task as assessed with functional MRI [118]. These two regions
comprise the default mode network, which is thought to present
normal deactivations during externally oriented tasks in healthy
controls [119,120]. Multimodal imaging studies may afford greater
accuracy for the distinction of AD from other forms of dementia
[111,121], as well as for the prediction of the transition from pre-
dementia stages to AD [122,123]. Given the wealth of recent data
indicating the relevance of WM abnormalities in MCI and AD,
we foresee a greater emphasis on the inclusion of MRI protocols
dedicated to the assessment of WM among the methods selected
for use in future multimodal studies evaluating these disorders.
We also expect to see an exponential growth of studies integrat-
ing neuroimaging data on WM changes with findings obtained
with other research methods. Though the cognitive decline of
AD and MCI emerges from brain changes that can be assessed
using neuroimaging techniques, there are several determinants of
brain abnormalities that are better evaluated with methods from
other research fields. Perhaps the best example of this is provided
by the emerging field of imaging genetics, which investigates how
single or combined molecular genetic characteristics may influ-
ence the variability of structural and/or functional neuroimaging
phenotypes. For instance, it is known that the APOE ε2 allele is
```
associated with a lower risk for AD [124]; in a recent DTI study of
```
healthy elderly individuals, APOE ε2 carriers presented increased
FA in the posterior cingulate cortex and in the corpus callosum
compared with homozygous for the APOE ε3 allele, suggesting
that the protective effect of APOE ε2 against the incidence of AD
may be exerted through a greater degree of WM integrity [125].
Finally, a number of CSF and plasma biomarkers have been
identified as potentially useful to aid in the early diagnosis and
prediction of AD [126,127], and they have been investigated in con-
junction with imaging biomarkers in recent studies [111,128–130].
Given the salience of WM abnormalities in AD and MCI as
shown in the present report, we expect that future studies inves-
tigating multiple peripheral, CSF and neuroimaging markers
in large samples will place greater emphasis on the role of WM
changes in association with those clinical conditions.
Financial & competing interests disclosure
```
The authors were partially funded by the University of São Paulo (Grant
```
#2011.1.9333.1.3, Center for Interdisciplinary Research on Applied
```
Neurosciences - NAPNA). GF Busatto and OV Forlenza are supported by
```
```
the National Council of Technological and Scientific Development (CNPq),
```
Brazil. LK Ferreira is supported by Fundação de Amparo à Pesquisa do
```
Estado de São Paulo (FAPESP). The authors have no other relevant affili-
```
ations or financial involvement with any organization or entity with a
financial interest in or financial conflict with the subject matter or materials
discussed in the manuscript apart from those disclosed.
No writing assistance was utilized in the production of this manuscript.
ReferencesPapers of special note have been highlighted as:
s฀OF฀INTERESTss฀OF฀CONSIDERABLE฀INTEREST
1 Dubois B, Feldman HH, Jacova C et al.Revising the definition of Alzheimer’s
```
disease: a new lexicon. Lancet Neurol.9(11), 1118–1127 (2010).
```
2 Sperling RA, Aisen PS, Beckett LA et al.Toward defining the preclinical stages of
Alzheimer’s disease: recommendationsfrom the National Institute on Aging
– Alzheimer’s Association workgroups on
```
diagnostic guidelines for Alzheimer’sdisease. Alzheimers Dement. 7(3), 280–292
```
```
(2011).
```
3 Dickerson BC, Sperling RA. Neuro-imaging biomarkers for clinical trials of
```
disease-modifying therapies in Alzheimer’sdisease. NeuroRx 2(2), 348–360 (2005).
```
Key issues
```
s฀ Recent MRI investigations using volumetric measurements and diffusion tensor imaging clearly indicate the presence of white matter(WM) abnormalities in Alzheimer’s disease (AD), even at early stages such as minor cognitive impairment.
```
s฀ WM changes in AD have been found to affect tracts that interconnect relevant networks for cognition such as the perforant pathway,THE฀CORPUS฀CALLOSUM ฀FORNIX ฀THE฀CINGULUM฀BUNDLE฀AND฀OTHER฀CORTICO CORTICAL฀TRACTS
s฀ $EGENERATION฀OF฀7-฀CAUSES฀DISCONNECTION฀AMONG฀NEURAL฀CELLS ฀DAMAGE฀TO฀CORTICO CORTICAL฀AND฀CORTICO SUBCORTICAL฀PATHWAYS ฀AS฀WELL฀AS฀loss of myelinated axons resulting in reduced signaling and synaptic activity, even at early AD stages.
```
s฀ The degree of WM abnormalities in AD (hyperintense lesions on T2/FLAIR and diffusion tensor imaging indices of WM disruption) arerelated to the severity of cognitive impairment, and these WM changes may predict the progression from minor cognitive impairment
```
to AD.
s฀ The possible relationship between WM abnormalities and the emergence of neuropsychiatric symptoms in AD remains to be clarified.
MRI studies & white matter abnormalities
116
```
Expert Rev. Neurother. 13(5), (2013)490
```
Review
4 Hommet C, Mondon K, Constans T et al.Review of cerebral microangiopathy and
Alzheimer’s disease: relation between whitematter hyperintensities and microbleeds.
```
Dement. Geriatr. Cogn. Disord. 32(6),367–378 (2011).
```
5 Admiraal-Behloul F, van den Heuvel DM,Olofsen H et al. Fully automatic segmenta-
```
tion of white matter hyperintensities in MRimages of the elderly. Neuroimage 28(3),
```
```
607–617 (2005).
```
6 Gold BT, Powell DK, Andersen AH, SmithCD. Alterations in multiple measures of
white matter integrity in normal women athigh risk for Alzheimer’s disease.
```
Neuroimage 52(4), 1487–1494 (2010).
```
7 Longstreth WT Jr, Manolio TA, Arnold Aet al. Clinical correlates of white matter
findings on cranial magnetic resonanceimaging of 3301 elderly people. The
```
Cardiovascular Health Study. Stroke 27(8),1274–1282 (1996).
```
8 Schmidt R, Schmidt H, Haybaeck J et al.Heterogeneity in age-related white matter
```
changes. Acta Neuropathol. 122(2),171–185 (2011).
```
ss฀ !฀REVIEW฀ABOUT฀WHITE฀MATTER฀7- ฀HYPERINTENSITIES฀IN฀THE฀AGING฀
BRAIN ฀INCLUDING฀IMAGING฀lNDINGS ฀NEUROPATHOLOGY฀AND฀GENETIC฀ASPECTS
9 Fazekas F, Chawluk JB, Alavi A, HurtigHI, Zimmerman RA. MR signal abnor-
malities at 1.5 T in Alzheimer’s dementiaand normal aging. AJR. Am. J. Roentgenol.
```
149(2), 351–356 (1987).
```
```
10 Wahlund LO, Barkhof F, Fazekas F et al.;European Task Force on Age-Related
```
White Matter Changes. A new rating scalefor age-related white matter changes
```
applicable to MRI and CT. Stroke 32(6),1318–1322 (2001).
```
11 Brickman AM, Sneed JR, Provenzano FAet al. Quantitative approaches for
assessment of white matter hyperintensitiesin elderly populations. Psychiatry Res.
```
193(2), 101–106 (2011).
```
```
12 Rostrup E, Gouw AA, Vrenken H et al.;LADIS study group. The spatial distribu-
```
tion of age-related white matter changes asa function of vascular risk factors – results
```
from the LADIS study. Neuroimage 60(3),1597–1607 (2012).
```
13 Gouw AA, Seewann A, van der Flier WMet al. Heterogeneity of small vessel disease:
a systematic review of MRI and histo-pathology correlations. J. Neurol.
```
Neurosurg. Psychiatr. 82(2), 126–135(2011).
```
```
14 Simpson JE, Fernando MS, Clark L et al.;MRC Cognitive Function and Ageing
```
Neuropathology Study Group. Whitematter lesions in an unselected cohort of
the elderly: astrocytic, microglial andoligodendrocyte precursor cell responses.
```
Neuropathol. Appl. Neurobiol. 33(4),410–419 (2007).
```
```
15 Simpson JE, Ince PG, Higham CE et al.;MRC Cognitive Function and Ageing
```
Neuropathology Study Group. Microglialactivation in white matter lesions and
```
nonlesional white matter of ageing brains.Neuropathol. Appl. Neurobiol. 33(6),
```
```
670–683 (2007).
```
16 Elias MF, Elias PK, Sullivan LM, Wolf PA,D’Agostino RB. Lower cognitive function
in the presence of obesity and hyper-tension: the Framingham heart study. Int.
J. Obes. Relat. Metab. Disord. 27(2),260–268 (2003).
17 de la Torre JC. Three postulates to helpidentify the cause of Alzheimer’s disease.
J. Alzheimers Dis. 24(4), 657–668 (2011).
18 O’Brien JT, Erkinjuntti T, Reisberg B et al.Vascular cognitive impairment. Lancet
```
Neurol. 2(2), 89–98 (2003).
```
19 Hachinski VC, Iliff LD, Zilhka E et al.Cerebral blood flow in dementia. Arch.
```
Neurol. 32(9), 632–637 (1975).
```
20 Loeb C, Gandolfo C. Diagnostic evalua-tion of degenerative and vascular dementia.
```
Stroke 14(3), 399–401 (1983).
```
21 Rosen WG, Terry RD, Fuld PA, KatzmanR, Peck A. Pathological verification of
```
ischemic score in differentiation ofdementias. Ann. Neurol. 7(5), 486–488
```
```
(1980).
```
22 Moroney JT, Bagiella E, Desmond DWet al. Meta-analysis of the Hachinski
```
Ischemic Score in pathologically verifieddementias. Neurology 49(4), 1096–1105
```
```
(1997).
```
23 Brewster PW, McDowell I, Moineddin R,Tierney MC. Differential prediction of
vascular dementia and Alzheimer’s diseasein nondemented older adults within 5 years
```
of initial testing. Alzheimers. Dement. 8(6),528–535 (2012).
```
24 Gunning-Dixon FM, Raz N. The cognitivecorrelates of white matter abnormalities in
```
normal aging: a quantitative review.Neuropsychology 14(2), 224–232 (2000).
```
25 Hedden T, Mormino EC, Amariglio REet al. Cognitive profile of amyloid burden
and white matter hyperintensities incognitively normal older adults. J. Neurosci.
```
32(46), 16233–16242 (2012).
```
26 Herrmann LL, Le Masurier M, EbmeierKP. White matter hyperintensities in late
```
life depression: a systematic review.J. Neurol. Neurosurg. Psychiatr. 79(6),
```
```
619–624 (2008).
```
27 Tamashiro JH, Zung S, Zanetti MV et al.Increased rates of white matter hyperinten-
```
sities in late-onset bipolar disorder. BipolarDisord. 10(7), 765–775 (2008).
```
28 Marchant NL, Reed BR, Sanossian N et al.The aging brain and cognition: contribu-
tion of vascular injury and Aβ to mildcognitive dysfunction. JAMA Neurol.
```
70(4), 488–495 (2013).
```
29 Wahlund LO, Almkvist O, Basun H, JulinP. MRI in successful aging, a 5-year
```
follow-up study from the eighth to ninthdecade of life. Magn. Reson. Imaging 14(6),
```
```
601–608 (1996).
```
30 Murray ME, Senjem ML, Petersen RCet al. Functional impact of white matter
```
hyperintensities in cognitively normalelderly subjects. Arch. Neurol. 67(11),
```
```
1379–1385 (2010).
```
31 Hardy J, Selkoe DJ. The amyloidhypothesis of Alzheimer’s disease: progress
```
and problems on the road to therapeutics.Science 297(5580), 353–356 (2002).
```
32 Braak H, Braak E. Frequency of stages ofAlzheimer-related lesions in different age
```
categories. Neurobiol. Aging 18(4), 351–357(1997).
```
33 Price JL, Morris JC. Tangles and plaques innondemented aging and ‘preclinical’
```
Alzheimer’s disease. Ann. Neurol. 45(3),358–368 (1999).
```
34 Ferreira LK, Busatto GF. Neuroimaging inAlzheimer’s disease: current role in clinical
```
practice and potential future applications.Clinics (Sao. Paulo). 66(Suppl. 1), 19–24
```
```
(2011).
```
```
35 Provenzano FA, Muraskin J, Tosto G et al.;for the Alzheimer’s Disease Neuroimaging
```
Initiative. White matter hyperintensitiesand cerebral amyloidosis: necessary and
```
sufficient for clinical expression ofAlzheimer disease? JAMA Neurol. 70(4),
```
```
455–461 (2013).
```
s฀ !฀RECENT฀STUDY฀ADDRESSING฀THE฀RELATIONSHIP฀BETWEEN฀AMYLOID฀DEPOSITION฀AND฀7-฀
```
HYPERINTENSITIES฀USING฀AMYLOID฀IMAGING฀AND฀-2)
```
```
36 Carmichael O, Schwarz C, Drucker Det al.; Alzheimer’s Disease Neuroimaging
```
Initiative. Longitudinal changes in whitematter disease and cognition in the first
```
year of the Alzheimer disease neuroimaginginitiative. Arch. Neurol. 67(11), 1370–1378
```
```
(2010).
```
Radanovic, Pereira, Stella et al.
117
491www.expert-reviews.com
Review
37 Brickman AM, Provenzano FA, Muraskin Jet al. Regional white matter hyperintensity
volume, not hippocampal atrophy, predictsincident Alzheimer disease in the
```
community. Arch. Neurol. 69(12),1621–1627 (2012).
```
```
38 Gorelick PB, Scuteri A, Black SE et al.;American Heart Association Stroke
```
Council, Council on Epidemiology andPrevention, Council on Cardiovascular
Nursing, Council on CardiovascularRadiology and Intervention, and Council
on Cardiovascular Surgery and Anesthesia.Vascular contributions to cognitive
impairment and dementia: a statement forhealthcare professionals from the American
```
Heart Association/American StrokeAssociation. Stroke 42(9), 2672–2713
```
```
(2011).
```
39 Debette S, Markus HS. The clinicalimportance of white matter hyperintensities
on brain magnetic resonance imaging:systematic review and meta-analysis. BMJ
```
341, c3666 (2010).
```
40 Mechelli A, Price CJ, Friston KJ,Ashburner J. Voxel-based morphometry of
```
the human brain: methods and applica-tions. Curr. Med. Imag. Rev. 1(2), 105–113
```
```
(2005).
```
41 Busatto GF, Diniz BS, Zanetti MV.Voxel-based morphometry in Alzheimer’s
```
disease. Expert Rev. Neurother. 8(11),1691–1702 (2008).
```
42 Whitwell JL. Voxel-based morphometry:an automated technique for assessing
```
structural changes in the brain. J. Neurosci.29(31), 9661–9664 (2009).
```
43 Chaim TM, Duran FL, Uchida RR, PéricoCA, de Castro CC, Busatto GF. Volumet-
ric reduction of the corpus callosum inAlzheimer’s disease in vivo as assessed with
```
voxel-based morphometry. Psychiatry Res.154(1), 59–68 (2007).
```
44 Balthazar ML, Yasuda CL, Pereira FR,Pedro T, Damasceno BP, Cendes F.
Differences in grey and white matteratrophy in amnestic mild cognitive
```
impairment and mild Alzheimer’s disease.Eur. J. Neurol. 16(4), 468–474 (2009).
```
45 Busatto GF, Garrido GE, Almeida OPet al. A voxel-based morphometry study of
temporal lobe gray matter reductions inAlzheimer’s disease. Neurobiol. Aging
```
24(2), 221–231 (2003).
```
46 Balthazar ML, Yasuda CL, Cendes F,Damasceno BP. Learning, retrieval, and
recognition are compromised in aMCI andmild AD: are distinct episodic memory
processes mediated by the same anatomical
```
structures? J. Int. Neuropsychol. Soc. 16(1),205–209 (2010).
```
47 Ferreira LK, Diniz BS, Forlenza OV,Busatto GF, Zanetti MV. Neurostructural
predictors of Alzheimer’s disease: ameta-analysis of VBM studies. Neurobiol.
```
Aging 32(10), 1733–1741 (2011).
```
48 Li J, Pan P, Huang R, Shang H. Ameta-analysis of voxel-based morphometry
studies of white matter volume alterationsin Alzheimer’s disease. Neurosci. Biobehav.
```
Rev. 36(2), 757–763 (2012).
```
s฀ !฀RECENT฀META ANALYSIS฀OF฀VOXEL BASED฀MORPHOMETRY฀STUDIES฀ADDRESSING฀7-฀
VOLUME฀DIFFERENCES฀BETWEEN฀PATIENTS฀AND฀CONTROLS
49 Di Paola M, Luders E, Di Iulio F et al.Callosal atrophy in mild cognitive
impairment and Alzheimer’s disease:different effects in different stages.
```
Neuroimage 49(1), 141–149 (2010).
```
50 Hampel H, Teipel SJ, Alexander GE,Pogarell O, Rapoport SI, Möller HJ. In vivo
imaging of region and cell type specificneocortical neurodegeneration in
Alzheimer’s disease. Perspectives of MRIderived corpus callosum measurement for
mapping disease progression and effects oftherapy. Evidence from studies with MRI,
```
EEG and PET. J. Neural Transm.109(5–6), 837–855 (2002).
```
51 Teipel SJ, Bayer W, Alexander GE et al.Regional pattern of hippocampus and
corpus callosum atrophy in Alzheimer’sdisease in relation to dementia severity:
```
evidence for early neocortical degeneration.Neurobiol. Aging 24(1), 85–94 (2003).
```
52 Teipel SJ, Bayer W, Alexander GE et al.Progression of corpus callosum atrophy in
```
Alzheimer disease. Arch. Neurol. 59(2),243–248 (2002).
```
53 Li S, Pu F, Shi F, Xie S, Wang Y, Jiang T.Regional white matter decreases in
Alzheimer’s disease using optimizedvoxel-based morphometry. Acta Radiol.
```
49(1), 84–90 (2008).
```
54 Matsuda H. Voxel-based morphometry ofbrain MRI in normal aging and Alzhei-
```
mer’s disease. Aging Dis. 4(1), 29–37(2013).
```
55 Di Paola M, Spalletta G, Caltagirone C.In vivo structural neuroanatomy of corpus
callosum in Alzheimer’s disease and mildcognitive impairment using different MRI
```
techniques: a review. J. Alzheimers Dis.20(1), 67–95 (2010).
```
56 Stoub TR, deToledo-Morrell L, StebbinsGT, Leurgans S, Bennett DA, Shah RC.
Hippocampal disconnection contributes to
memory dysfunction in individuals at riskfor Alzheimer’s disease. Proc. Natl Acad.
```
Sci. USA 103(26), 10041–10045 (2006).
```
57 Guo X, Wang Z, Li K et al. Voxel-basedassessment of gray and white matter
```
volumes in Alzheimer’s disease. Neurosci.Lett. 468(2), 146–150 (2010).
```
58 Villain N, Desgranges B, Viader F et al.Relationships between hippocampal
atrophy, white matter disruption, and graymatter hypometabolism in Alzheimer’s
```
disease. J. Neurosci. 28(24), 6174–6181(2008).
```
59 Pereira JM, Xiong L, Acosta-Cabronero J,Pengas G, Williams GB, Nestor PJ.
Registration accuracy for VBM studiesvaries according to region and degenerative
```
disease grouping. Neuroimage 49(3),2205–2215 (2010).
```
60 Davatzikos C, Vaillant M, Resnick SM,Prince JL, Letovsky S, Bryan RN.
A computerized approach for morphologi-cal analysis of the corpus callosum.
J. Comput. Assist. Tomogr. 20(1), 88–97(1996).
61 Leporé N, Brun C, Pennec X et al. Meantemplate for tensor-based morphometry
```
using deformation tensors. Med. ImageComput. Comput. Assist. Interv. 10(Pt 2),
```
```
826–833 (2007).
```
62 Friese U, Meindl T, Herpertz SC, ReiserMF, Hampel H, Teipel SJ. Diagnostic
utility of novel MRI-based biomarkers forAlzheimer’s disease: diffusion tensor
```
imaging and deformation-based morphom-etry. J. Alzheimers Dis. 20(2), 477–490
```
```
(2010).
```
```
63 Fischl B. FreeSurfer. Neuroimage 62(2),774–781 (2012).
```
64 Westman E, Muehlboeck JS, Simmons A.Combining MRI and CSF measures for
classification of Alzheimer’s disease andprediction of mild cognitive impairment
```
conversion. Neuroimage 62(1), 229–238(2012).
```
65 Ridgway GR, Lehmann M, Barnes J et al.Early-onset Alzheimer disease clinical
```
variants: multivariate analyses of corticalthickness. Neurology 79(1), 80–84 (2012).
```
66 Salat DH, Greve DN, Pacheco JL et al.Regional white matter volume differences
```
in nondemented aging and Alzheimer’sdisease. Neuroimage 44(4), 1247–1258
```
```
(2009).
```
67 Clarkson MJ, Cardoso MJ, Ridgway GRet al. A comparison of voxel and surface
```
based cortical thickness estimationmethods. Neuroimage 57(3), 856–865
```
```
(2011).
```
MRI studies & white matter abnormalities
118
```
Expert Rev. Neurother. 13(5), (2013)492
```
Review
68 Masutani Y, Aoki S, Abe O, Hayashi N,Otomo K. MR diffusion tensor imaging:
recent advance and new techniques fordiffusion tensor visualization. Eur. J.
```
Radiol. 46(1), 53–66 (2003).
```
69 Yoon B, Shim YS, Hong YJ et al. Compari-son of diffusion tensor imaging and
voxel-based morphometry to detect whitematter damage in Alzheimer’s disease.
J. Neurol. Sci. 302(1–2), 89–95 (2011).
70 Sydykova D, Stahl R, Dietrich O et al. Fiberconnections between the cerebral cortex and
the corpus callosum in Alzheimer’s disease:a diffusion tensor imaging and voxel-based
```
morphometry study. Cereb. Cortex 17(10),2276–2282 (2007).
```
71 Mielke MM, Kozauer NA, Chan KC et al.Regionally-specific diffusion tensor
```
imaging in mild cognitive impairment andAlzheimer’s disease. Neuroimage 46(1),
```
```
47–55 (2009).
```
72 Cho H, Yang DW, Shon YM et al.Abnormal integrity of corticocortical tracts
in mild cognitive impairment: a diffusiontensor imaging study. J. Korean Med. Sci.
```
23(3), 477–483 (2008).
```
73 Salat DH, Tuch DS, van der Kouwe AJet al. White matter pathology isolates the
```
hippocampal formation in Alzheimer’sdisease. Neurobiol. Aging 31(2), 244–256
```
```
(2010).
```
74 O’Dwyer L, Lamberton F, Bokde AL et al.Multiple indices of diffusion identifies
white matter damage in mild cognitiveimpairment and Alzheimer’s disease. PLoS
```
ONE 6(6), e21745 (2011).
```
75 Alves GS, O’Dwyer L, Jurcoane A et al.Different patterns of white matter
degeneration using multiple diffusionindices and volumetric data in mild
```
cognitive impairment and Alzheimerpatients. PLoS ONE 7(12), e52859 (2012).
```
76 Stricker NH, Schweinsburg BC,Delano-Wood L et al. Decreased white
matter integrity in late-myelinating fiberpathways in Alzheimer’s disease supports
```
retrogenesis. Neuroimage 45(1), 10–16(2009).
```
77 Sexton CE, Kalu UG, Filippini N, MackayCE, Ebmeier KP. A meta-analysis of
diffusion tensor imaging in mild cognitiveimpairment and Alzheimer’s disease.
```
Neurobiol. Aging 32(12), 2322.e5–2322.18(2011).
```
78 Clerx L, Visser PJ, Verhey F, Aalten P.New MRI markers for Alzheimer’s disease:
a meta-analysis of diffusion tensor imagingand a comparison with medial temporal
```
lobe measurements. J. Alzheimers Dis.29(2), 405–429 (2012).
```
79 Shu N, Wang Z, Qi Z, Li K, He Y.Multiple diffusion indices reveals white
matter degeneration in Alzheimer’s diseaseand mild cognitive impairment: a
```
tract-based spatial statistics study.J. Alzheimers Dis. 26(Suppl. 3), 275–285
```
```
(2011).
```
80 Mielke MM, Okonkwo OC, Oishi K et al.Fornix integrity and hippocampal volume
predict memory decline and progression toAlzheimer’s disease. Alzheimers. Dement.
```
8(2), 105–113 (2012).
```
81 Kalus P, Slotboom J, Gallinat J et al.Examining the gateway to the limbic
system with diffusion tensor imaging: theperforant pathway in dementia. Neuroimage
```
30(3), 713–720 (2006).
```
82 Wang J, Zuo X, Dai Z et al. Disruptedfunctional brain connectome in individuals
```
at risk for Alzheimer’s disease. Biol.Psychiatr. 73(5), 472–481.(2012).
```
83 Heinemann U, Schmitz D, Eder C, GloveliT. Properties of entorhinal cortex
projection cells to the hippocampalformation. Ann. N. Y. Acad. Sci. 911,
```
112–126 (2000).
```
84 Witter MP. The perforant path: projectionsfrom the entorhinal cortex to the dentate
```
gyrus. Prog. Brain Res. 163, 43–61 (2007).
```
85 Hyman BT, Van Hoesen GW, Kromer LJ,Damasio AR. Perforant pathway changes
```
and the memory impairment of Alzheimer’sdisease. Ann. Neurol. 20(4), 472–481
```
```
(1986).
```
86 Morys J, Sadowski M, Barcikowska M,Maciejewska B, Narkiewicz O. The second
layer neurones of the entorhinal cortex andthe perforant path in physiological ageing
```
and Alzheimer’s disease. Acta Neurobiol.Exp. (Wars) 54(1), 47–53 (1994).
```
87 Xie S, Xiao JX, Gong GL et al. Voxel-baseddetection of white matter abnormalities in
```
mild Alzheimer disease. Neurology 66(12),1845–1849 (2006).
```
88 Smith SM, Jenkinson M, Johansen-Berg Het al. Tract-based spatial statistics:
```
voxelwise analysis of multi-subjectdiffusion data. Neuroimage 31(4),
```
```
1487–1505 (2006).
```
89 van Bruggen T, Stieltjes B, Thomann PA,Parzer P, Meinzer HP, Fritzsche KH.
Do Alzheimer-specific microstructuralchanges in mild cognitive impairment
```
predict conversion? Psychiatry Res.203(2–3), 184–193 (2012).
```
90 Zhuang L, Wen W, Zhu W et al. Whitematter integrity in mild cognitive
```
impairment: a tract-based spatial statisticsstudy. Neuroimage 53(1), 16–25 (2010).
```
91 Liu Y, Spulber G, Lehtimäki KK et al.Diffusion tensor imaging and tract-based
spatial statistics in Alzheimer’s disease andmild cognitive impairment. Neurobiol.
```
Aging 32(9), 1558–1571 (2011).
```
92 Jones DK, Knösche TR, Turner R. Whitematter integrity, fiber count, and other
```
fallacies: the do’s and don’ts of diffusionMRI. Neuroimage 73, 239–254 (2013).
```
```
s฀ !฀REVIEW฀PAPER฀ON฀DIFFUSION฀TENSION฀IMAGING฀$4) ฀METHODOLOGY฀EXPLAINING฀
```
```
THE฀LIMITS฀OF฀INTERPRETING฀$4)฀lNDINGS
```
93 Oishi K, Mielke MM, Albert M, LyketsosCG, Mori S. DTI analyses and clinical
```
applications in Alzheimer’s disease.J. Alzheimers Dis. 26(Suppl. 3), 287–296
```
```
(2011).
```
```
s฀ !฀REVIEW฀OF฀$4)฀STUDIES฀IN฀!LZHEIMERS฀DISEASE฀!$ 
```
94 Takahashi M, Hackney DB, Zhang G et al.Magnetic resonance microimaging of
intraaxonal water diffusion in live excisedlamprey spinal cord. Proc. Natl Acad. Sci.
```
USA 99(25), 16192–16196 (2002).
```
95 Lyketsos CG, Carrillo MC, Ryan JM et al.Neuropsychiatric symptoms in Alzheimer’s
```
disease. Alzheimers. Dement. 7(5), 532–539(2011).
```
96 Bruen PD, McGeown WJ, Shanks MF,Venneri A. Neuroanatomical correlates of
```
neuropsychiatric symptoms in Alzheimer’sdisease. Brain 131(Pt 9), 2455–2463
```
```
(2008).
```
```
97 Trzepacz PT, Yu P, Bhamidipati PK et al.;Alzheimer’s Disease Neuroimaging
```
Initiative. Frontolimbic atrophy isassociated with agitation and aggression in
mild cognitive impairment and Alzheimer’sdisease. Alzheimers. Dement. doi:10.1016/j.
```
jalz.2012.10.005 (2012) (Epub ahead ofprint).
```
98 Nakaaki S, Sato J, Torii K et al. Neuro-anatomical abnormalities before onset of
delusions in patients with Alzheimer’sdisease: a voxel-based morphometry study.
```
Neuropsychiatr. Dis. Treat. 9, 1–8 (2013).
```
99 Tighe SK, Oishi K, Mori S et al. Diffusiontensor imaging of neuropsychiatric
symptoms in mild cognitive impairmentand Alzheimer’s dementia.
J. Neuropsychiatry Clin. Neurosci. 24(4),484–488 (2012).
100 Ota M, Sato N, Nakata Y, Arima K, UnoM. Relationship between apathy and
diffusion tensor imaging metrics of thebrain in Alzheimer’s disease. Int. J. Geriatr.
```
Psychiatry 27(7), 722–726 (2012).
```
101 Tomimoto H, Lin JX, Matsuo A et al.Different mechanisms of corpus callosum
Radanovic, Pereira, Stella et al.
119
493www.expert-reviews.com
Review
```
atrophy in Alzheimer’s disease and vasculardementia. J. Neurol. 251(4), 398–406
```
```
(2004).
```
102 Bartzokis G. Alzheimer’s disease ashomeostatic responses to age-related myelin
```
breakdown. Neurobiol. Aging 32(8),1341–1371 (2011).
```
ss฀ 4HOROUGH฀REVIEW฀ABOUT฀THE฀RELATIONSHIP฀BETWEEN฀7-฀DEGENERATION฀AND฀
NEURODEGENERATION ฀INCLUDING฀ALTERNATIVE฀RELATIONSHIPS฀BETWEEN฀THE฀AMYLOID฀
HYPOTHESIS฀OF฀!$฀AND฀7-
103 Brickman AM, Meier IB, Korgaonkar MSet al. Testing the white matter retrogenesis
```
hypothesis of cognitive aging. Neurobiol.Aging 33(8), 1699–1715 (2012).
```
104 Bartzokis G. Age-related myelin break-down: a developmental model of cognitive
```
decline and Alzheimer’s disease. Neurobiol.Aging 25(1), 5–18; author reply 49 (2004).
```
s฀ !฀PROPOSAL฀FOR฀A฀DEVELOPMENTAL฀MODEL฀OF฀COGNITIVE฀DECLINE฀AND฀!$฀CENTERED฀ON฀
7-฀PATHOLOGY
105 Kuceyeski A, Zhang Y, Raj A. Linkingwhite matter integrity loss to associated
cortical regions using structural connectiv-ity information in Alzheimer’s disease and
```
fronto-temporal dementia: the Loss inConnectivity (LoCo) score. Neuroimage
```
```
61(4), 1311–1323 (2012).
```
106 Fu JL, Zhang T, Chang C, Zhang YZ, LiWB. The value of diffusion tensor imaging
in the differential diagnosis of subcorticalischemic vascular dementia and Alzhei-
mer’s disease in patients with only mildwhite matter alterations on T2-weighted
```
images. Acta Radiol. 53(3), 312–317(2012).
```
107 Bozoki AC, Korolev IO, Davis NC,Hoisington LA, Berger KL. Disruption of
limbic white matter pathways in mildcognitive impairment and Alzheimer’s
```
disease: a DTI/FDG-PET study. Hum.Brain Mapp. 33(8), 1792–1802 (2012).
```
108 Müller MJ, Greverus D, Weibrich C et al.Diagnostic utility of hippocampal size and
```
mean diffusivity in amnestic MCI.Neurobiol. Aging 28(3), 398–403 (2007).
```
109 O’Dwyer L, Lamberton F, Bokde AL et al.Using support vector machines with
multiple indices of diffusion for automatedclassification of mild cognitive impairment.
```
PLoS ONE 7(2), e32441 (2012).
```
110 Wang L, Goldstein FC, Veledar E et al.Alterations in cortical thickness and white
matter integrity in mild cognitiveimpairment measured by whole-brain
cortical thickness mapping and diffusiontensor imaging. AJNR. Am. J. Neuroradiol.
```
30(5), 893–899 (2009).
```
111 McMillan CT, Brun C, Siddiqui S et al.White matter imaging contributes to the
```
multimodal diagnosis of frontotemporallobar degeneration. Neurology 78(22),
```
```
1761–1768 (2012).
```
112 Likitjaroen Y, Meindl T, Friese U et al.Longitudinal changes of fractional
anisotropy in Alzheimer’s disease patientstreated with galantamine: a 12-month
randomized, placebo-controlled, double-blinded study. Eur. Arch. Psychiatry Clin.
```
Neurosci. 262(4), 341–350 (2012).
```
```
113 Jack CR Jr, Bernstein MA, Borowski BJet al.; Alzheimer’s Disease Neuroimaging
```
Initiative. Update on the magneticresonance imaging core of the Alzheimer’s
```
disease neuroimaging initiative. Alzheimers.Dement. 6(3), 212–220 (2010).
```
114 Jack CR Jr. Alzheimer disease: newconcepts on its neurobiology and the
```
clinical role imaging will play. Radiology263(2), 344–361 (2012).
```
115 Yassa MA, Muftuler LT, Stark CE.Ultrahigh-resolution microstructural
diffusion tensor imaging reveals perforantpath degradation in aged humans in vivo.
```
Proc. Natl Acad. Sci. USA 107(28),12687–12691 (2010).
```
116 Greicius MD, Supekar K, Menon V,Dougherty RF. Resting-state functional
connectivity reflects structural connectivityin the default mode network. Cereb. Cortex
```
19(1), 72–78 (2009).
```
117 Chételat G, Desgranges B, Landeau B et al.Direct voxel-based comparison between
```
grey matter hypometabolism and atrophyin Alzheimer’s disease. Brain 131(Pt 1),
```
```
60–71 (2008).
```
118 Jacobs HI, Gronenschild EH, Evers EAet al. Visuospatial processing in early
Alzheimer’s disease: a multimodalneuroimaging study. Cortex. doi:10.1016/j.
```
cortex.2012.01.005 (2012) (Epub ahead ofprint).
```
119 Buckner RL, Andrews-Hanna JR, SchacterDL. The brain’s default network: anatomy,
```
function, and relevance to disease. Ann. N.Y. Acad. Sci. 1124, 1–38 (2008).
```
120 Raichle ME, MacLeod AM, Snyder AZ,Powers WJ, Gusnard DA, Shulman GL.
```
A default mode of brain function. Proc.Natl Acad. Sci. USA 98(2), 676–682
```
```
(2001).
```
121 Kantarci K, Lowe VJ, Boeve BF et al.Multimodality imaging characteristics of
```
dementia with Lewy bodies. Neurobiol.Aging 33(9), 2091–2105 (2012).
```
```
122 Shaffer JL, Petrella JR, Sheldon FC et al.;Alzheimer’s Disease Neuroimaging
```
Initiative. Predicting cognitive decline insubjects at risk for Alzheimer disease by
using combined cerebrospinal fluid, MRimaging, and PET biomarkers. Radiology
```
266(2), 583–591 (2013).
```
123 Zhang D, Shen D. Predicting futureclinical changes of MCI patients using
```
longitudinal and multimodal biomarkers.PLoS ONE 7(3), e33182 (2012).
```
124 Kim J, Basak JM, Holtzman DM. The roleof apolipoprotein E in Alzheimer’s disease.
```
Neuron 63(3), 287–303 (2009).
```
125 Chiang GC, Zhan W, Schuff N, WeinerMW. White matter alterations in
cognitively normal apoE e2 carriers: insightinto Alzheimer resistance? AJNR. Am. J.
```
Neuroradiol. 33(7), 1392–1397 (2012).
```
126 Forlenza OV, Diniz BS, Gattaz WF.Diagnosis and biomarkers of predementia
```
in Alzheimer’s disease. BMC Med. 8, 89(2010).
```
```
127 Hu WT, Holtzman DM, Fagan AM et al.;Alzheimer’s Disease Neuroimaging
```
Initiative. Plasma multianalyte profiling inmild cognitive impairment and Alzheimer
```
disease. Neurology 79(9), 897–905 (2012).
```
128 Mielke MM, Haughey NJ, RatnamBandaru VV et al. Plasma ceramides are
altered in mild cognitive impairment andpredict cognitive decline and hippocampal
```
volume loss. Alzheimers. Dement. 6(5),378–385 (2010).
```
```
129 Vemuri P, Wiste HJ, Weigand SD et al.;Alzheimer’s Disease Neuroimaging
```
Initiative. MRI and CSF biomarkers innormal, MCI, and AD subjects: predicting
```
future clinical change. Neurology 73(4),294–301 (2009).
```
130 Thambisetty M, An Y, Kinsey A et al.Plasma clusterin concentration is associated
```
with longitudinal brain atrophy in mildcognitive impairment. Neuroimage 59(1),
```
```
212–217 (2012).
```
MRI studies & white matter abnormalities
120
Experimento 7 – Alterações neuropsiquiátricas associados com danos de redes
funcionais em pacientes com doença de Alzheimer e transtorno cognitivo leve.
```
r Human Brain Mapping 000:00–00 (2013) r
```
Neuropsychiatric Symptoms in Alzheimer’s
Disease Are Related to Functional Connectivity
Alterations in the Salience Network
Marcio L. F. Balthazar,1 Fabrı´cio R. S. Pereira,1 Ta´tila M. Lopes,1
Elvis L. da Silva,1 Ana Carolina Coan,1 Brunno M. Campos,1 Niall W.
Duncan,2 Florindo Stella,3 Georg Northoff,2 Benito P. Damasceno,1
and Fernando Cendes1*
1Neuroimaging Laboratory, Department of Neurology, Medical Sciences School, University of
```
Campinas (UNICAMP), Brazil2Institute of Mental Health Research, University of Ottawa, Ottawa, Ontario, Canada
```
```
3Biosciences Institute, Sa˜o Paulo State University (UNESP), Brazil
```
r r
```
Abstract: Neuropsychiatric syndromes are highly prevalent in Alzheimer’s disease (AD), but theirneurobiology is not completely understood. New methods in functional magnetic resonance imaging,
```
```
such as intrinsic functional connectivity or ‘‘resting-state" analysis, may help to clarify this issue. Usingsuch approaches, alterations in the default-mode and salience networks (SNs) have been described in
```
Alzheimer’s, although their relationship with specific symptoms remains unclear. We therefore carriedout resting-state functional connectivity analysis with 20 patients with mild to moderate AD, and
```
correlated their scores on neuropsychiatric inventory syndromes (apathy, hyperactivity, affective syn-drome, and psychosis) with maps of connectivity in the default mode network and SN. In addition,
```
we compared network connectivity in these patients with that in 17 healthy elderly control subjects.All analyses were controlled for gray matter density and other potential confounds. Alzheimer’s
```
patients showed increased functional connectivity within the SN compared with controls (right ante-rior cingulate cortex and left medial frontal gyrus), along with reduced functional connectivity in the
```
```
default-mode network (bilateral precuneus). A correlation between increased connectivity in anteriorcingulate cortex and right insula areas of the SN and hyperactivity syndrome (agitation, irritability,
```
```
aberrant motor behavior, euphoria, and disinhibition) was found. These findings demonstrate an asso-ciation between specific network changes in AD and particular neuropsychiatric symptom types. This
```
underlines the potential clinical significance of resting state alterations in future diagnosis and therapy.Hum Brain Mapp 00:000–000, 2013. VC 2013 Wiley Periodicals Inc.
```
Key words: Alzheimer’s disease; default mode network; salience network; functional connectivity;neuropsychiatric symptoms
```
r r
```
Contract grant sponsor: Sa˜o Paulo Research Foundation(FAPESP), Brazil; Contract grant number: 2009/02179-2.
```
```
*Correspondence to: Fernando Cendes, Department of Neurology,FCM, University of Campinas (UNICAMP), Cidade Universita´ria,
```
Campinas-SP, Brazil, 13083-970. E-mail: fcendes@unicamp.br
```
Received for publication 22 February 2012; Revised 6 November2012; Accepted 3 December 2012
```
```
DOI: 10.1002/hbm.22248Published online in Wiley Online Library (wileyonlinelibrary.com).
```
VC 2013 Wiley Periodicals, Inc.
121
INTRODUCTION
```
Neuropsychiatric symptoms (NPS) are highly prevalentin patients with dementia. This is particularly the case in
```
```
those with Alzheimer’s disease (AD), where studies reporta prevalence of NPS that varies from 60 to 90% during the
```
course of the disease [Youn et al., 2011]. However, despitethis high prevalence, the neurobiology underlying these
symptoms is poorly understood. The most widespreadtheories about the genesis of cognitive deficits and NPS in
```
AD relate to anatomic-structural changes, associated withpathological features (neuritic plaques, neurofibrillary tan-
```
```
gles, and loss of synaptic density, among others), in thelimbic, paralimbic, and neocortical regions. In addition,
```
NPS may be associated with dysfunction of various neuro-transmitter systems due to neuronal death in specific
```
transmitter source nuclei (cholinergic, serotonergic, norad-renergic, etc.) [Cummings, 2000].
```
In addition to the observed anatomical deficits, recentadvances in the neuroimaging of dementia have high-
lighted concurrent dysfunctions in functional networks.Such networks have been identified across a number of
imaging modalities, most prominently fMRI, and are char-acterized by inter-regional correlations in spontaneous
```
BOLD fluctuations (known as functional connectivity) inthe absence of an experimental paradigm or any other
```
explicit stimulus [van den Heuvel and Pol, 2010]. Differentnetworks are spatially distinct but functionally related and
```
have been found to be present at rest, during tasks, andeven during sleep and anesthesia [Deshpande et al., 2010;
```
```
Fox and Raichle, 2007; van den Heuvel and Pol, 2010].Neurodegenerative diseases, such as AD, can disrupt ac-
```
tivity within the networks [Seeley et al., 2009], as well asthe complex system of interconnections between the differ-
```
ent networks, causing cognitive problems (memory, atten-tion, language, praxis, and executive functions), and NPS
```
```
(apathy, depression, agitation, disinhibition, etc.) [Bruenet al., 2008; Gauthier et al., 2010; Lyketsos et al., 2011]. In
```
```
the case of AD, one of the most relevant networks appearsto be the default mode network (DMN). The role of the
```
```
DMN, which consists of regions such as the posterior cin-gulate cortex (PCC), precuneus, ventromedial prefrontal
```
```
cortex, and the hippocampal formation, remains unclear;however, it is widely accepted that this system shows
```
```
increased activity when a person is not focused on activ-ities directed to the external environment (e.g., when an
```
```
individual recalls autobiographical facts and events, orplans the future) [Buckner et al., 2008]. Some studies in
```
AD have shown a breakdown in functional connectivity inthe DMN, even at early stages of the disease [Greicius
```
et al., 2004; Zhang et al., 2010]. In addition, Celone et al.[2006] reported associations between DMN connectivity
```
and memory performance assessed outside of the scanner,whereas Westlye et al. [2011] showed a negative correla-
tion between DMN synchronization and performance onmemory tests, suggesting a neurocognitive significance of
brain activity patterns during rest in healthy elderly
```
individuals who are carriers of the AD-related apolipopro-tein e4 gene (APOE4).
```
```
A second network that seems to be relevant in AD is thesalience network (SN), which comprises the anterior cingu-
```
```
late cortex (ACC), the frontal insula, the amygdala and thestriatum. Activity in the SN is related to emotionally rele-
```
vant stimuli, which can originate either internally or fromthe external environment [Seeley et al., 2007]. In the case
```
of AD (and the behavioral variant of frontotemporal de-mentia), Zhou et al. [2010] showed a negative correlation
```
between the connectivity of the SN and the DMN, mean-ing that decreasing activity in the DMN is related to
```
increased activity in the SN and vice versa). A dynamicinteraction between these networks may provide regula-
```
tion of shifts in attention, as well as access to personalresources for general cognitive processing and specific cog-
nitive domains. Such mechanisms would have importantimplications for psychopathological disorders involving
dysfunctional saliency processing, which can diminish theability to direct attentional resources and goal-relevant
cognition [Menon, 2011].Several unanswered questions remain, however, regard-
ing the role of these functional networks in the develop-ment of AD symptoms. To our knowledge, no studies
have investigated the correlation between neuropsychiatricsyndromes and disruptions in the DMN or SN in AD. One
study by Seeley et al. [2007] did find significant correla-tions between the level of anxiety in healthy adults before
```
MRI scanning and the degree of connectivity of the ACC(an important part of the SN). The authors proposed that
```
behavioral symptoms in AD, which often involve earlyemotional sensitizations such as irritability and anxiety,
might be associated with functional alterations in SN[Zhou et al., 2010].
```
We based our study hypothesis on the following prem-ises: (1) alterations in functional networks may be related
```
```
to NPS; and (2) disruptions in one network may interferewith other networks (e.g., the negative correlation in con-
```
```
nectivity patterns between DMN and SN). We hypothe-sized that alterations in DMN and SN connectivity may be
```
responsible at least in part for the NPS of AD patients.More specifically, we sought to determine whether an
increase in connectivity in the SN could lead to hyperac-tivity behaviors, such as agitation and irritability. With
regard to the DMN, we hypothesized that a decrease inconnectivity within this network could lead to apathy,
potentially through deficits in forming expectations for thefuture or recounting recent events [Buckner et al., 2008].
Given the anticorrelation between SN and DMN, it is plau-sible to hypothesize that decreases in DMN connectivity
might also be related to hyperactivity behaviors, whichwould fit with observations of combined apathy and agita-
tion in patients with dementia.To test our hypotheses, we correlated the scores of the
```
neuropsychiatric inventory (NPI) subsyndromes, as definedby Aalten et al. [2007], with individual maps SN and DMN
```
connectivity in patients with mild to moderate AD,
r Balthazar et al. r
r 2 r
122
considering age, atrophy, and dementia severity as covari-ates. The subsyndromes used were apathy, hyperactivity,
affective syndrome, and psychosis. The use of NPI subsyn-dromes, rather than unitary symptoms, is supported by the
fact that various individual symptoms usually manifest to-gether and have a similar course over time, suggesting a
common biological basis. In addition, pharmacologicalstudies have shown that drug treatments have an effect on
behavioral features in dementia when neuropsychiatricsubsyndromes are considered but not when individual
```
symptoms are considered [Gauthier et al., 2005; Herrmannet al., 2005]. We also compared the patterns of connectivity
```
between patients and a group of healthy elderly people.
MATERIALS AND METHODS
Subjects
```
We studied 37 subjects over the age of 50 years (73.85 !8.19). Of those subjects, 20 had mild to moderate AD and
```
```
were treated at the Neuropsychology and Dementia Out-patient Clinic (UNICAMP University Hospital). The
```
remaining 17 subjects were healthy control subjects,matched for age and sex. Routine laboratory studies,
including B12 levels, folate levels, syphilis serology, andthyroid hormone levels, were performed for all patients.
The local ethics committee approved these experiments.The diagnosis of probable AD was based on criteria estab-
lished by the National Institute of Neurological and Com-municative Disorders, and the Stroke/Alzheimer’s Disease
and Related Disorders Association [McKhann et al., 1984].We only included patients who were classified as clinical
```
dementia rating (CDR) 1 (13 patients) and 2 (sevenpatients). All patients had at least one psychiatric symp-
```
tom, as measured by the NPI. Exclusion criteria included ahistory of other neurological or psychiatric diseases, previ-
ous head injury with loss of consciousness, drug or alcoholaddiction, prior chronic exposure to neurotoxic substances,
and a Hachinski ischemic score >4. Patients who met theclinical criteria for probable AD but had extensive white
matter hyperintensities on T2-weighted MRI were alsoexcluded. Fifteen patients underwent MRI scanning on the
same day that their caregivers completed the NPI inter-view. In the remaining five cases, the interviews were per-
formed 2 days before the MRI scanning. The control groupconsisted of subjects who were classified as CDR 0 and
had no history of neurological diseases, psychiatric dis-eases, or memory complaints.
Neuropsychological, Neuropsychiatric, andFunctional Evaluations
```
Global cognitive status was measured using the MiniMental Status Examination [MMSE, Folstein et al., 1975;
```
Brazilian version by Brucki et al., 2003]. Episodic memorywas evaluated by the Rey auditory verbal learning test
```
[Rey, 1964]. Visual perception was assessed with subtestsof Luria’s Neuropsychological Investigation (LNI), using
```
```
items G12, G13, G14 (the patient is asked to examine andname pictures of objects that are scribbled over or super-
```
```
imposed on another picture), along with G17 (an itemfrom Raven’s test) and one item for mental rotation of fig-
```
```
ures (in both items, the patient is asked to complete astructure, a portion of which is missing, by choosing from
```
```
various options) [Christensen, 1975]. Four items from theRatcliff’s manikin test for mental rotation were also used
```
[Ratcliff, 1979]. Constructive praxis was evaluated usingthe Rey-Osterrieth’s Complex Figure test [Osterrieth, 1944].
```
Language tests included the Boston Naming Test [Kaplanet al., 1983] and verbal fluency for category words (ani-
```
```
mals) and phonology (FAS). Working memory wasassessed by the forward (FDS) and backward digit span
```
subtest of the WAIS-R [Wechsler, 1987]. Executive func-tions were evaluated using the Trail Making Test A and B,
Stroop color-word test and Clock drawing test.The neuropsychiatric assessment consisted of the Neuro-
```
psychiatric Inventory (NPI) [Cummings et al., 1994] basedon an interview with the closest caregiver. The NPI con-
```
sists of a detailed evaluation of the following 12 neuro-psychiatric domains: hallucinations, delusions, agitation/
aggression, depression, anxiety, irritability, disinhibition,euphoria, apathy, aberrant motor behavior, change in
night-time sleep behavior, and changes in appetite andeating. The questions were read to the caregiver exactly as
written. If the caregiver failed to comprehend the question,we repeated it in alternate terms. After reading the screen-
ing question, the caregiver was asked if the behaviordescribed had been observed. If the answer was ‘‘no’’ then
we proceeded to the next section and read the next screen-ing question. If the answer was ‘‘yes,’’ then the subques-
tions were read, and yes/no responses were obtained. Thecaregiver was then asked to rate the frequency and sever-
ity of the behaviors within that domain, based on the mostabnormal behavior revealed in the subquestions. The
```
scores were calculated by multiplying the frequency of thesymptoms (from 1 to 4: rarely, sometimes, often and very
```
```
often) by the intensity (from 1 to 3: mild, moderate andsevere). Each NPI domain score may thus vary from 0 to
```
12. Based on a study by Aalten et al. [2007], we consideredthe following four subsyndromes: apathy, hyperactivity
```
(the sum of agitation, disinhibition, irritability, euphoria,and aberrant motor behavior scores), psychosis (delusions,
```
```
hallucinations, and night-time behavior disturbances) andaffective syndrome (depression and anxiety). We also
```
applied the CDR using a semistructured interview andPfeffer’s daily-life activities questionnaire.
Data analysis was performed using Systat software 12.0.Student’s t-tests were performed for intergroup compari-
sons of the demographic and cognitive scores. On occa-sions where the data violated the assumptions of
parametric tests, we performed the Mann Whitney test.The results were considered to be statistically significant
when P < 0.05.
r NPS in AD and Functional Connectivity Alterations of SN r
r 3 r
123
Magnetic Resonance Image Acquisition
```
Structural and functional images were acquired on a 3TMRI scanner (Philips Achieva, Best, The Netherlands). A
```
```
set of structural images was composed with the followingsequences: (a) sagittal high-resolution T
```
1-weighted withgradient echo images that were acquired with TR/TE ¼
```
7/3.2 ms, FOV ¼ 240 " 240, and isotropic voxels of 1mm3; (b) coronal and axial FLAIR (fluid-attenuated inver-
```
```
sion recovery) T2-weighted images, anatomically alignedat the hippocampus with image parameters set to TR/TE/
```
TI ¼ 12,000/140/2,850 ms, FOV ¼ 220 " 206, voxels recon-structed to 0.45 " 0.45 " 4.00 mm3 with the gap between
```
slices set to 1 mm; (c) coronal IR (inversion recovery)T
```
1-weighted images with TR/TE/TI ¼ 3,550/15/400 ms,FOV ¼ 180 " 180 and voxels reconstructed to 0.42 " 0.42
```
" 3.00 mm3; (d) coronal multiecho (five echos)T
```
2-weighted images with TR/TE ¼ 3,300/30 ms, FOV ¼180 " 180, voxels reconstructed to 0.42 " 0.42 " 3.00 mm3.
Functional images were acquired during rest. Subjectswere instructed to keep their eyes closed and to not think
of anything in particular. Axial T2*-weighted images hadTR/TE ¼ 2,000/30 ms, FOV ¼ 240 " 240, 40 axial slices
per volume, and isotropic voxels set to 3 " 3 " 3 mm3.For each participant, we acquired 10-min of echo planar
```
images (300 volumes) and discarded the first threevolumes.
```
The participants’ sensory stimulation was limited to thenoise of the scanner during image acquisitions. To reduce
noise, all subjects wore earplugs. In addition, all subjectshad their head movements restricted by a soft Velcro
strap.
Structural Imaging Analysis
```
To exclude the influence of structural abnormalities, weevaluated gray matter (GM) density through voxel-based
```
```
morphometry (VBM) analysis. VBM is a technique thatallows the assessment of the volume or concentration of
```
gray and white matter across the whole brain through anautomated postprocessing MRI evaluation [Ashburner and
Friston, 2000]. The voxelwise approach does not requireprior information about GM [Good et al., 2001]. We carried
```
out VBM analysis on 3D, sagittal T1-weighted images,with a thickness of 1 mm (TR/TE ¼ 22/9 ms, flip angle ¼
```
```
35, matrix ¼ 256 " 220) using the FSL toolbox (http://www.fmrib.ox.ac.uk/fsl/) [Smith et al., 2004]. Images were
```
skull stripped using the BET algorithm [Smith, 2002] andGM was automatically segmented using the FAST4 algo-
rithm [Zhang et al., 2001]. GM maps were then normalizedto MNI standard space with affine registration [Jenkinson
```
et al., 2002; Jenkinson and Smith, 2001]. Registered imageswere divided by the Jacobian of the warp field in order to
```
correct local deformation. Resulting images weresmoothed with an 8-mm FWHM isotropic Gaussian kernel.
Smoothed GM images were then used in subsequentanalysis.
Functional Imaging Analysis
Functional images were converted from DICOM to theNIfTI format using Philips scanner software. Images were
preprocessed by removing linear trends before slice timingand motion correction algorithms were applied. The motion
correction step took the first volume of the time series as itsreference and output six parameters of head movement,
```
three related to head translation and three associated to thehead rotation (yaw, pitch, and roll). Subsequently, images
```
were normalized to MNI standard space and smoothedwith a 6 mm FWHM Gaussian kernel. We applied Fourier
filters on smoothed images, setting a bandpass from 0.01 to0.1 Hz, and regressed these data with the motion parame-
```
ters previously calculated. All of these steps were donewith the AFNI software package (http://afni.nimh.nih.-
```
```
gov/). Subsequently, probabilistic independent component(IC) analysis (pICA) [Beckmann and Smith, 2004; Guo,
```
```
2011] was estimated in order to extract independent spatialmaps (IC) for each subject. ICs were obtained with the FSL
```
```
toolbox, Multivariate Exploratory Linear OptimizedDecomposition into Independent Components (MELODIC
```
```
v3.0). We allowed the MELODIC algorithm to determine asmany ICs as was necessary to explain 99% of the variability
```
```
of preprocessed data (default option).The set of ICs components was masked with the atlas
```
```
of functional ROIs (fROI) available on the Stanford’sFunctional Imaging in Neuropsychiatric Disorders web-
```
```
site (http://findlab.stanford.edu/index.html) [Shirer et al.,2012]. We used the ‘‘ventral and dorsal DMN’’ (vDMN
```
```
and dDMN) and the ‘‘anterior and posterior SN’’ (aSNand pSN) to extract z-values of ICs within and outside of
```
the fROIs. To do this, we used a linear template-match-ing procedure that involves taking the average z-score of
voxels falling within the template minus the average z-score of voxels outside the template and selecting the
```
component in which this difference (the goodness-of-fit)was the greatest. The z-scores here reflect the degree to
```
which a given voxel’s time series correlates with theoverall component time series, scaled by the standard
deviation of the residual Gaussian noise [Greicius et al.,2004]. This procedure was estimated by the following
```
equation:
```
GoF ¼ ðI % OÞ " 100 " PNINI% PNONO
 
I ¼ Average z % scores from voxels inside the ROI
O ¼ Average z % scores from voxels outside the ROI
PNI ¼ Number of voxels with positive score inside the ROI
PNO ¼ Number of voxels with positive score outside the ROI
NI ¼ Number of voxels inside the ROI
NO ¼ Number of voxels outside the ROI
Among the set of ICs, we selected the one with the high-est value of GOF to use for the second level of analysis
r Balthazar et al. r
r 4 r
124
```
and to calculate correlations with NPI scores. Thus, one ICwas chosen for each fROI (vDMN, dDMN, aSN, and pSN)
```
to enter subsequent analyses.Differences between controls and patients were esti-
```
mated by nonparametric permutation tests (RANDOM-ISE - 5000 permutations) [Nichols and Holmes, 2002].
```
The P values calculated were corrected for multiplecomparisons according to the threshold-free cluster
```
enhancement algorithm implemented in FSL [Andersonand Robinson, 2001; Bullmore et al., 1999; Hayasaka and
```
Nichols, 2003]. We included each subject’s 3D map ofGM in this analysis to correct the results for atrophy on
a voxelwise basis.
Correlations Between NPI and DMN and SNConnectivity
```
We used the same nonparametric approach to evaluate thecorrelation between patients’ selected ICs (vDMN, dDMN,
```
```
aSN, and pSN) and NPI syndromes (apathy, hyperactivity,affective syndrome, and psychosis). Age, dementia severity
```
```
(as measured by CDR sum of boxes (memory, orientation,judgment, and problem solving, community affairs, home
```
```
and hobbies, and personal care), and GM maps were enterednuisance variables. Statistical maps were then corrected for
```
multiple comparisons with P < 0.01, FDR corrected.
RESULTS
Cognitive and Neuropsychiatric Evaluations
```
As shown in Table I, there was no difference betweenthe AD group and the controls with regard to age (P ¼
```
```
0.43), but there was a significant difference in the twogroups regarding education (P < 0.05). The AD patients
```
performed worse in all tests, which included episodicmemory, attention and working memory, visuospatial
```
skills, executive functions, and language (Table I). Distri-bution of NPI symptoms and subsyndromes are shown in
```
Table II and Figure 1.
Differences in the DMN and SN in AD Patientsand Healthy Elderly
```
We found areas of decreased connectivity in the dorsalDMN (atrophy corrected), and in particular in its posterior
```
```
anatomical structures, when comparing the AD group tothe control subjects (P < 0.01, corrected for multiple com-
```
```
parisons). These were the right precuneus (MNI
```
TABLE I. Demographic, functional, andneuropsychological data
AD Controls P
```
Age (years) 73.85 " 8.19 72.33 " 6.37 0.43*Education (years) 6.95 " 4.45 10.16 " 5.36 <0.05
```
CDR–SB 6.72 " 2.74 0Pfeffer Functional
ActivityQuestionnaire18.45 " 7.83 0
MMSE 16.35 " 6.22 28.55 " 1.85 <0.0001RAVLT: COD 18.83 " 7.53 45.66 " 8.46 <0.0001
```
RAVLT: A7 0.55 " 1.09 8.26 " 0.61 <0.0001BNT 29.53 " 13.80 52.46 " 4.89 <0.0001
```
```
Semantic VF 6.88 " 3.12 18.00 " 4.20 <0.0001*Phonologic VF (FAS) 13.82 " 9.76 33.46 " 13.19 <0.0001
```
VSP-LNI 13.25 " 3.76 18.13 " 1.24 <0.0001FDS 3.82 " 1.70 5.40 " 2.16 0.02*
```
BDS 2.05 " 1.81 4.33 " 1.54 0.002*TMT-A (s) 225.67 " 98.66 66.73 " 20.32 <0.0001
```
```
TMT-B (s) 278.73 " 56.60 123.07 " 83.34 <0.0001Stroop test:
```
```
Congruent (s)98.52 " 41.51 58.06 " 18.69 0.004Stroop test:
```
```
Congruent (errors)0.23 " 0.75 0.06 " 0.25 0.62Stroop test:
```
```
Incongruent (s)216.24 " 59.00 108.20 " 28.20 0.008Stroop test:
```
```
Incongruent (errors)34.52 " 23.93 2.53 " 3.75 <0.0001Clock drawing
```
```
test (0–10)5.53 " 0.79 9.46 " 0.35 0.0004Rey complex
```
```
figure (copy)14.00 " 3.37 34.60 " 1.19 <0.0001
```
Data presented as mean " SD.*Mann–Whitney test was applied due to non-normal distribu-
```
tion.MMSE, mini-mental status examination; RAVLT-COD, encod-ing of Rey auditory verbal learning test (sum of A1 þ A2 þ : : : þ
```
```
A5); RAVLT -A7, delayed recall of RAVLT; BNT, Boston namingtest; VF, verbal fluency; VSP-LNI, visuospatial perception item of
```
```
Luria’s neuropsychological investigation; FDS, forward digit span;BDS, backward digit span; TMT, Trail Making Test. Significance
```
levels of comparisons between AD and healthy groups are givenin the final column.
TABLE II. Neuropsychiatric inventory syndromes andsymptoms
NPIsubsyndromes NPI symptoms Mean " SD% ofpatientswith symptom
Apathy Apathy 4.25 " 3.22 90Appetite and
eating abnormalities1.70 " 2.93 35Hyperactivity Agitation 1.10 " 2.75 30
Disinhibition 0.30 " 1.34 5Irritability 1.2 " 2.19 40
Euphoria 0.2 " 0.89 5Aberrant
motor behavior1.45 " 2.32 35Affective Depression 1.55 " 2.28 35
Anxiety 0.95 " 2.25 25Psychosis Hallucinations 0.10 " 0.30 10
Delusions 0.15 " 0.48 10Night time
behavior disturbances1.20 " 2.17 30
r NPS in AD and Functional Connectivity Alterations of SN r
r 5 r
125
```
coordinates: 6, !66, 24; 205 voxels; z ¼ 4.12) and leftprecuneus (!2, !64, 54; 160 voxels; z ¼ 3.82) (Fig. 2A).
```
The same analysis did not show any areas of increasedconnectivity in the DMN in AD patients.
The opposite pattern was found in relation to theanterior SN. AD patients showed areas of increased con-
```
nectivity (atrophy corrected) in the right cingulate gyrus(18, 20, 38; 96 voxels; z ¼ 4.42; P < 0.01, corrected) and left
```
```
medial frontal gyrus (!8, 32, 38; 79 voxels; z ¼ 4.08; P <0.01, corrected) (Fig. 2B). We did not find any significant
```
differences between AD and controls in the connectivity ofthe ventral DMN and posterior SN.
Multiple Regressions of NPI Syndromes WithDMN and SN
We performed multiple regressions between the dorsaland ventral DMN and anterior and posterior SN maps
and the NPI syndromes of apathy, affective symptoms,hyperactivity, and psychosis. We found significant areas of
```
positive correlation with hyperactivity in the anterior SN(atrophy corrected), specifically in the right ACC (MNI: 8,
```
```
28, 18; 180 voxels; z ¼ 4.82; P < 0.01, corrected) and rightinsula (44, 10, !6; 68 voxels; z ¼ 4.36; P < 0.01, corrected)
```
```
(Fig. 3). All other regressions did not show any significantcorrelation between dorsal/ventral DMN or anterior/pos-
```
terior SN with NPI syndromes following correction formultiple comparisons and GM atrophy.
DISCUSSION
Using resting-state fMRI in a group of patients withmild to moderate AD and age and sex matched controls,
we showed that alterations in the intrinsic connectivity ofthe anterior SN predict behavioral symptoms in AD
Figure 1.Box and whiskers plot showing the distribution of NPI syn-
```
dromes scores: hyperactivity (mean # SD: 4.05 # 6.18), apathy(4.25 # 3.22), affective syndrome (2.50 # 4.28), and psychosis
```
```
(1.45 # 2.41). The box extends from the 25th percentile to the75th percentile, with a horizontal line at the median. Whiskers
```
extend down to the smallest value and up to the largest.
```
Figure 2.(A) Dorsal DMN areas of decreased functional connectivity in AD patients (atrophy corrected): right
```
```
precuneus (MNI coordinates: 6, !66, 24) and left precuneus (!2, !64, 54); P < 0.01, corrected formultiple comparisons. (B) Anterior SN areas of increased connectivity in AD patients (atrophy cor-
```
```
rected): right cingulate gyrus (18, 20, 38) and left medial frontal gyrus (!8, 32, 38); P < 0.01, corrected.
```
r Balthazar et al. r
r 6 r
126
patients. Specifically, we demonstrated that hyperactivitysyndrome is associated with aSN hyperconnectivity in the
ACC and right insula. This correlation remains even aftercorrection for GM atrophy. No correlations were found
```
between DMN connectivity and NPS, or between SN con-nectivity and other NPS (apathy, psychosis, and affective
```
```
syndromes) following correction for atrophy.To our knowledge, our study is the first to report a cor-
```
relation between alterations in SN connectivity and a spe-cific NPS in AD. The relevance of the role of functional
networks in psychopathology has been increasingly recog-nized, especially the SN, which is important in the appro-
priate assignment of saliency to external stimuli or internalmental events. The SN, with the anterior insula as its inte-
gral outflow hub, assists target brain regions in the genera-tion of appropriate behavioral responses to salient stimuli
```
[Menon, 2011]. This property of detecting salient events(from the external environment or internally) may be sus-
```
```
ceptible to dysfunction (ineffective or enhanced detection)leading to inappropriate behaviors. We found that hyper-
```
```
activity syndrome (composed of symptoms of agitation,disinhibition, irritability, euphoria, and aberrant motor
```
```
behavior symptoms) is related to enhanced connectivity inSN nodes such as the ACC and right AI. This syndrome,
```
at least in part, could be a manifestation of an anxiety dis-order, in which hyperactivity of AI has been consistently
```
implicated [Menon, 2011; Paulus and Stein, 2006].In accordance to Menon’s triple network model, we sug-
```
gest that in AD patients, enhanced saliency detectionmight cause misperception of common events as if they
were emotionally relevant. This might cause symptomssuch as agitation, euphoria, and irritability, which more
directly involve emotional sensations. Furthermore, aber-rant motor behavior also seems to involve stereotypical
```
features (e.g., rummaging through drawers, manipulationof buttons, etc.); since the SN also receives information
```
```
about representations of goals and motor plans (Palaniyap-pan and Liddle, 2012), this kind of behavior may be
```
associated with dysfunctional representations of complexmovements. We also propose that dysfunctional process-
ing of stimuli by a hypoconnected DMN, as occurs in ADpatients, might compromise the conscious awareness of
the sensation caused by the stimuli. For example, a personwho is walking incessantly may be in pain or be thirsty,
although they cannot consciously process these sensationsproperly. Therefore, AD patients seem to have an altered
response to a wide array of internal and external stimuli,as well as problems in the conscious awareness of the
sensations caused by these stimuli. Considering the entireset of findings, it is possible that an alteration in the bal-
ance of functional connectivity networks in SN and DMNwill predict the behaviors of hyperactivity observed in our
patients.In this regard, another plausible explanation could be
based on a neurobiological account of Freudian constructs.According to Carhart-Harris and Friston [2010], Freud’s
descriptions of the primary and secondary processes areconsistent with self-organized activity in hierarchical corti-
cal systems, where the secondary process entailed by egofunctions are associated with the suppressive effect of the
DMN on its subcortical nodes and anticorrelated networks,such as the SN with its limbic and paralimbic components
```
(frontoinsular cortices, amygdala). The hyperactivity syn-drome of our AD patients could thus be equated with a
```
```
Figure 3.Areas of positive correlations between anterior SN and hyperactivity syndrome (atrophy cor-
```
```
rected): right ACC (MNI: 8, 28, 18) and right insula (44, 10, !6); P < 0.01, corrected for multi-ple comparisons.
```
r NPS in AD and Functional Connectivity Alterations of SN r
r 7 r
127
primitive, at least partly unconscious, primary processthinking and behavior. Our finding of hypoconnectivity in
the dorsal DMN and hyperconnectivity in the SN suggeststhat there have been a weakening or loss of top-down
DMN-associated ego control over limbic activity in thosehierarchically lower systems involved with the primary
process. In our view, Carhart-Harris and Friston’s neuro-biological Freudian account and Menon’s triple network
model complement each other in explaining our findings.Previous authors have found associations between SN
connectivity and NP symptoms. For example, Seeley et al.[2007] found a correlation between stressor-associated
anticipatory anxiety levels before MRI scanning and ACCconnectivity in young subjects without neurologic or
psychiatric diseases. In AD patients, Zhou et al. [2010] alsofound increased SN connectivity in the ACC, and sug-
gested that this finding may be related to behavioralsymptoms involving emotional sensations such as irritabil-
ity and anxiety. In addition, a number of authors havesuggested that the SN may also be involved in other psy-
chiatric diseases, such as schizophrenia, especially thosewith the major features of psychosis [Palaniyappan and
Liddle, 2011].Regarding the neurobiology of hyperactivity syndrome,
there are few studies about the neural correlates of agita-tion, irritability, and aberrant motor behavior in AD. Tekin
et al. [2001] demonstrated that neurofibrillary tangles inthe ACC were related to agitation in AD patients, while in
a SPECT study, Rolland et al. [2005] found a correlationbetween wandering behavior and left parietotemporal
hypoperfusion. However, Bruen et al. [2008], who found acorrelation between agitation scores and low GM density
in bilateral ACC, noted that neuropathological evidencedid not coincide with the appearance of the symptom. It is
```
possible that hyperconnectivity in the ACC of AD patients(and hyperactivity syndrome) may precede the pathologi-
```
cal findings described by these authors. Moreover, theydid not find a correlation with other symptoms of hyper-
activity syndrome. More work to support this hypothesisis required, however.
Regarding the relevance of functional connectivitydisruptions in AD, some authors speculate that DMN
problems may precede beta-amyloid pathology. This hy-pothesis is supported by recent studies which have dem-
onstrated that disconnection precedes atrophy in the PCC[Gili et al., 2011] and that asymptomatic carriers of APOE4
have a reduction in PCC connectivity, along withincreased SN connectivity [Machulda et al., 2011]. Another
possibility is that typical AD pathology may disrupt func-tional networks, with atrophy in some key DMN compo-
nents, secondary to classic AD pathology, potentiallyinitiating connectivity alterations in the whole network.
```
Should this be the case, atrophy in the hippocampi mayhave led to a decrease in connectivity in the PCC; for
```
example, studies using diffusion tensor imaging inpatients with medial temporal lobe epilepsy with hippo-
campal sclerosis showed dysfunctions in the uncinate and
arcuate fasciculus, involving frontal and posterior parietalregions in addition to the corpus callosum and cingulum
[Thivard et al., 2005]. Following this model, it is possiblethat a decrease in DMN connectivity may cause an increase
in other networks, including the SN. This is supported by anumber of studies that have shown a negative correlation
```
between the SN and DMN [Greicius and Krasnow, 2003;Fox et al., 2005; Zhou et al., 2010], with our study providing
```
additional evidence. This correlation between DMN and SNactivity has led some authors to suggest that they are func-
tionally related, proposing that the SN plays a role inswitching brain states from the internally guided DMN to
```
an external task-related activity mode [Sridharan et al.,2008; Palaniyappan and Liddle, 2011].
```
Our study has some limitations. First, we studied a rela-tively small cohort, although our findings were robust to a
wide range of potential confounds and to multiple compari-son correction, suggesting a reasonable degree of power.
```
Second, it would be better to assess NPS symptoms duringMRI scanning rather than through indirect methods; how-
```
ever, in most cases, we performed the NPI interview on thesame day as the scan procedure, which could minimize this
problem. Finally, future studies could test the validity ofthe method used here for evaluating clinical responses to
pharmacological and nonpharmacological treatments of NPsyndromes in AD and other forms of dementia.
CONCLUSIONS
Our findings demonstrate a correlation between hyperac-tivity syndrome and alterations in the connectivity of the
SN in areas without anatomic atrophy. These results under-line the potential clinical significance of resting state altera-
tions in future diagnosis and therapy. However, thesefindings do not explain the whole phenomenon of NPS
symptoms in AD—several other well-established causes,including structural, genetic, biochemical, and environmen-
tal factors, are also related to these complex mental dys-functions and may influence intrinsic connectivity patterns.
REFERENCES
Aalten P, Verhey FR, Boziki M, Bullock R, Byrne EJ, Camus V,Caputo M, Collins D, De Deyn PP, Elina K, Frisoni G, Girtler
N, Holmes C, Hurt C, Marriott A, Mecocci P, Nobili F, OussetPJ, Reynish E, Salmon E, Tsolaki M, Vellas B, Robert PH
```
(2007): Neuropsychiatric syndromes in dementia. Results fromthe European Alzheimer Disease Consortium: Part I. Dement
```
```
Geriatr Cogn Disord 24:457–463.Anderson MJ, Robinson J (2001): Permutation tests for linear mod-
```
```
els. Aust NZ J Stat 43:75–78.Ashburner J, Friston KJ (2000): Voxel-based morphometry—The
```
```
methods. Neuroimage 11(6 Pt 1):805–821.Beckmann CF, Smith SM (2004): Probabilistic independent compo-
```
nent analysis for functional magnetic resonance imaging. IEEETrans Med Imaging 23:137–152.
r Balthazar et al. r
r 8 r
128
```
Brucki SM, Nitrini R, Caramelli P, Bertolucci PH, Okamoto IH(2003): [Suggestions for utilization of the mini-mental state
```
```
examination in Brazil]. Arq Neuropsiquiatr 61:777–781.Bruen PD, McGeown WJ, Shanks MF, Venneri A (2008): Neuroa-
```
```
natomical correlates of neuropsychiatric symptoms in Alzhei-mer’s disease. Brain 131(Pt 9):2455–2463.
```
```
Buckner RL, Andrews-Hanna JR, Schacter DL (2008): The brain’sdefault network: Anatomy, function, and relevance to disease.
```
Ann NY Acad Sci 1124:1–1138.Bullmore ET, Suckling J, Overmeyer S, Rabe-Hesketh S, Taylor E,
```
Brammer MJ (1999): Global, voxel, and cluster tests, by theoryand permutation, for a difference between two groups of
```
structural MR images of the brain. IEEE Trans Med Imaging18:32–42.
```
Carhart-Harris RL, Friston KJ (2010).The default-mode, ego-func-tions and free-energy: A neurobiological account of Freudian
```
ideas. Brain 133:1265–1283.Celone KA, Calhoun VD, Dickerson BC, Atri A, Chua EF, Miller
```
SL, DePeau K, Rentz DM, Selkoe DJ, Blacker D, Albert MS,Sperling RA (2006): Alterations in memory networks in mild
```
cognitive impairment and Alzheimer’s disease: An independ-ent component analysis. J Neurosci 26:10222–10231.
Christensen A-L. 1975. Luria’s Neuropsychological Investigation,Manual and Test Material, 4th ed. Copenhagen:Munksgaard.
```
Cummings JL, Mega M, Gray K, Rosenberg-Thompson S, CarusiDA, Gornbein J (1994): The Neuropsychiatric Inventory:
```
Comprehensive assessment of psychopathology in dementia.Neurology 44:2308–2314.
```
Cummings JL (2000): Cognitive and behavioral heterogeneity inAlzheimer’s disease: Seeking the neurobiological basis.
```
```
Neurobiol Aging 21:845–861.Deshpande G, Kerssens C, Sebel PS, Hu X (2010): Altered local
```
coherence in the default mode network due to sevofluraneanesthesia. Brain Res 1318:110–121.
```
Folstein MF, Folstein SE, McHugh PR (1975): ‘‘Mini-mental state’’.A practical method for grading the cognitive state of patients
```
for the clinician. J Psychiatr Res 12:189–198.Fox MD, Snyder AZ, Vincent JL, Corbetta M, Van Essen DC,
```
Raichle ME (2005): The human brain is intrinsically organizedinto dynamic, anticorrelated functional networks. Proc Natl
```
```
Acad Sci USA 102:9673–9678.Fox MD, Raichle ME (2007): Spontaneous fluctuations in brain
```
activity observed with functional magnetic resonance imaging.Nat Rev Neurosci 8:700–711.
```
Gauthier S, Wirth Y, Mobius HJ (2005): Effects of memantine onbehavioural symptoms in Alzheimer’s disease patients: An
```
```
analysis of the Neuropsychiatric Inventory (NPI) data of tworandomised, controlled studies. Int J Geriatr Psychiatry 20:459–
```
464.Gauthier S, Cummings J, Ballard C, Brodaty H, Grossberg G, Rob-
```
ert P, Lyketsos C (2010): Management of behavioral problemsin Alzheimer’s disease. Int Psychogeriatr 22:346–372.
```
```
Gili T, Cercignani M, Serra L, Perri R, Giove F, Maraviglia B, Cal-tagirone C, Bozzali M (2011): Regional brain atrophy and func-
```
tional disconnection across Alzheimer’s disease evolution.J Neurol Neurosurg Psychiatry 82:58–66.
```
Good CD, Johnsrude IS, Ashburner J, Henson RN, Friston KJ,Frackowiak RS (2001): A voxel-based morphometric study of
```
```
ageing in 465 normal adult human brains. Neuroimage 14(1 Pt1):21–36.
```
```
Greicius MD, Krasnow B, Reiss AL, Menon V (2003): Functionalconnectivity in the resting brain: A network analysis of the
```
default mode hypothesis. Proc Natl Acad Sci U S A 100:253–258.
```
Greicius MD, Srivastava G, Reiss AL, Menon V (2004): Default-mode network activity distinguishes Alzheimer’s disease from
```
healthy aging: Evidence from functional MRI. Proc Natl AcadSci U S A 101:4637–4642.
```
Guo Y (2011): A general probabilistic model for group independ-ent component analysis and its estimation methods. Biometrics
```
```
67:1532–1542.Hayasaka S, Nichols TE (2003): Validating cluster size inference:
```
Random field and permutation methods. Neuroimage 20:2343–2356.
```
Herrmann N, Rabheru K, Wang J, Binder C (2005): Galantaminetreatment of problematic behavior in Alzheimer disease:
```
Post-hoc analysis of pooled data from three large trials. Am JGeriatr Psychiatry 13:527–534.
```
Jenkinson M, Bannister P, Brady M, Smith S (2002): Improvedoptimization for the robust and accurate linear registration
```
and motion correction of brain images. Neuroimage 17:825–841.
```
Jenkinson M, Smith S (2001): A global optimisation method forrobust affine registration of brain images. Med Image Anal
```
```
5:143–156.Kaplan EF, Goodglass H, Weintraub S (1983). The Boston Naming
```
Test, 2nd ed. Philadelphia: Lea & Febiger.Lyketsos CG, Carrillo MC, Ryan JM, Khachaturian AS, Trzepacz
```
P, Amatniek J, Cedarbaum J, Brashear R, Miller DS (2011):Neuropsychiatric symptoms in Alzheimer’s disease. Alzheimer
```
Dement 7:532–539.Machulda MM, Jones DT, Vemuri P, McDade E, Avula R, Przybel-
```
ski S, Boeve BF, Knopman DS, Petersen RC, Jack CR Jr (2011):Effect of APOE epsilon4 status on intrinsic network connectiv-
```
ity in cognitively normal elderly subjects. Arch Neurol68:1131–1136.
```
McKhann G, Drachman D, Folstein M, Katzman R, Price D, Sta-dlan EM (1984): Clinical diagnosis of Alzheimer’s disease:
```
Report of the NINCDS-ADRDA Work Group under the aus-pices of Department of Health and Human Services Task Force
```
on Alzheimer’s Disease. Neurology 34:939–944.Menon V (2011): Large-scale brain networks and psychopathol-
```
```
ogy: A unifying triple network model. Trends Cogn Sci15:483–506.
```
```
Nichols TE, Holmes AP (2002): Nonparametric permutation testsfor functional neuroimaging: A primer with examples. Hum
```
```
Brain Mapp 15:1–25.Osterrieth PA (1944).[The test of copying a complex figure: A con-
```
tribution to the study of perception and memory]. Arch Psy-chol 30:286–356.
```
Palaniyappan L, Liddle PF (2012): Does the salience network playa cardinal role in psychosis? An emerging hypothesis of insu-
```
```
lar dysfunction. J Psychiatry Neurosci 37:17–27.Paulus MP, Stein MB (2006).An insular view of anxiety. Biol Psy-
```
```
chiatry 60:383–387.Ratcliff G (1979): Spatial thought, mental rotation and the right
```
cerebral hemisphere. Neuropsychologia 17:49–54.Rey A. 1964. [Clinical examination in psychology]. Paris: Press
Universitaire de France.Rolland Y, Payoux P, Lauwers-Cances V, Voisin T, Esquerre JP,
```
Vellas B (2005): A SPECT study of wandering behavior in Alz-heimer’s disease. Int J Geriatr Psychiatry 20:816–820.
```
```
Seeley WW, Menon V, Schatzberg AF, Keller J, Glover GH, KennaH, Reiss AL, Greicius MD (2007): Dissociable intrinsic
```
r NPS in AD and Functional Connectivity Alterations of SN r
r 9 r
129
connectivity networks for salience processing and executivecontrol. J Neurosci 27:2349–2356.
```
Seeley WW, Crawford RK, Zhou J, Miller BL, Greicius MD (2009):Neurodegenerative diseases target large-scale human brain
```
networks. Neuron 62:42–52.Shirer WR, Ryali S, Rykhlevskaia E, Menon V, Greicius MD
```
(2012): Decoding subject driven cognitive states with whole-brain connectivity patterns. Cereb Cortex 22:158–165.
```
```
Smith SM (2002): Fast robust automated brain extraction. HumBrain Mapp 17:143–155.
```
Smith SM, Jenkinson M, Woolrich MW, Beckmann CF, BehrensTE, Johansen-Berg H, Bannister PR, De Luca M, Drobnjak I,
```
Flitney DE, Niazy RK, Saunders J, Vickers J, Zhang Y, De Ste-fano N, Brady JM, Matthews PM (2004): Advances in func-
```
```
tional and structural MR image analysis and implementationas FSL. Neuroimage 23(Suppl 1):S208–S219.
```
```
Sridharan D, Levitin DJ, Menon V (2008): A critical role for theright fronto-insular cortex in switching between central-execu-
```
tive and default-mode networks. Proc Natl Acad Sci U S A105:12569–12574.
```
Tekin S, Mega MS, Masterman DM, Chow T, Garakian J, VintersHV, Cummings JL (2001): Orbitofrontal and anterior cingulate
```
cortex neurofibrillary tangle burden is associated with agita-tion in Alzheimer disease. Ann Neurol 49:355–361.
```
Thivard L, Lehericy S, Krainik A, Adam C, Dormont D, Chiras J,Baulac M, Dupont S (2005): Diffusion tensor imaging in medial
```
temporal lobe epilepsy with hippocampal sclerosis. Neuro-image 28:682–690.
```
van den Heuvel MP, Hulshoff Pol HE (2010): Exploringthe brain network: A review on resting-state fMRI func-
```
tional connectivity. Eur Neuropsychopharmacol 20:519–534.
```
Wechsler D (1987). Manual for the Wechsler Memory Scale-Re-vised (WMS-R). San Antonio: The Psychological
```
Corporation.Westlye ET, Lundervold A, Rootwelt H, Lundervold AJ, Westlye
```
LT (2011): Increased hippocampal default mode synchroniza-tion during rest in middle-aged and elderly APOE epsilon4
```
```
carriers: Relationships with memory performance. J Neurosci31:7775–7783.
```
```
Youn JC, Lee DY, Jhoo JH, Kim KW, Choo IH, Woo JI (2011):Prevalence of neuropsychiatric syndromes in Alzheimer’s dis-
```
```
ease (AD). Arch Gerontol Geriatr 52:258–263.Zhang HY, Wang SJ, Liu B, Ma ZL, Yang M, Zhang ZJ,
```
```
Teng GJ (2010): Resting brain connectivity: Changes dur-ing the progress of Alzheimer disease. Radiology 256:598–
```
```
606.Zhang Y, Brady M, Smith S (2001): Segmentation of brain MR
```
images through a hidden Markov random field model and theexpectation-maximization algorithm. IEEE Trans Med Imaging
20:45–57.Zhou J, Greicius MD, Gennatas ED, Growdon ME, Jang JY, Rabi-
```
novici GD, Kramer JH, Weiner M, Miller BL, Seeley WW(2010): Divergent network connectivity changes in behavioural
```
```
variant frontotemporal dementia and Alzheimer’s disease.Brain 133(Pt 5):1352–67.
```
r Balthazar et al. r
r 10 r
130
Experimento 8 – Pasticidade cerebral em codificação de memória verbal e visual de
pacientes com epilepsia medial temporal.
```
r Human Brain Mapping 00:000–000 (2011) r
```
Brain Plasticity for Verbal and Visual Memories in
Patients with Mesial Temporal Lobe Epilepsy and
Hippocampal Sclerosis: An fMRI Study
Andre´ a Alessio,1,2 Fabricio R.S. Pereira,1 Maurı´cio S. Sercheli,2
Jane M. Rondina,1,2 Helka B. Ozelo,1,2 Elisabeth Bilevicius,1
Tatiane Pedro,1 Roberto J.M. Covolan,2 Benito P. Damasceno,1
and Fernando Cendes1*
1Neuroimaging Laboratory, School of Medical Sciences, University of Campinas, Unicamp,
Campinas, Brazil2Neurophysics Group, Gleb Wataghin Physics Institute, University of Campinas, Unicamp,
Campinas, Brazil
r r
```
Abstract: We aimed to identify the brain areas involved in verbal and visual memory processing innormal controls and patients with unilateral mesial temporal lobe epilepsy (MTLE) associated with
```
```
unilateral hippocampal sclerosis (HS) by means of functional magnetic resonance imaging (fMRI). Thesample comprised nine normal controls, eight patients with right MTLE, and nine patients with left
```
MTLE. All subjects underwent fMRI with verbal and visual memory paradigms, consisting of encodingand immediate recall of 17 abstract words and 17 abstract drawings. A complex network including pa-
rietal, temporal, and frontal cortices seems to be involved in verbal memory encoding and retrieval innormal controls. Although similar areas of activation were identified in both patient groups, the exten-
sion of such activations was larger in the left-HS group. Patients with left HS also tended to exhibitmore bilateral or right lateralized encoding related activations. This finding suggests a functional reor-
ganization of verbal memory processing areas in these patients due to the failure of left MTL system.As regards visual memory encoding and retrieval, our findings support the hypothesis of a more dif-
fuse and bilateral representation of this cognitive function in the brain. Compared to normal controls,encoding in the left-HS group recruited more widespread cortical areas, which were even more wide-
spread in the right-HS group probably to compensate for their right mesial temporal dysfunction. Incontrast, the right-HS group exhibited fewer activated areas during immediate recall than the other
two groups, probably related to their greater difficulty in dealing with visual memory content. HumBrain Mapp 00:000–000, 2011. VC 2011 Wiley Periodicals, Inc.
```
Key words: cognitive functions; neuropsychological evaluation; hippocampal atrophy; functionalreorganization
```
r r
```
Contract grant sponsor: Fundac¸a˜o de Amparo a` Pesquisa do Estadode Sa˜o Paulo—FAPESP; Contract grant number: 05/54908-7.
```
*Correspondence to: Fernando Cendes, Department of Neurology,FCM-UNICAMP, Cidade Universita´ria, Campinas, SP, Brazil, CEP
13083-970. E-mail: fcendes@unicamp.br
```
Received for publication 18 January 2010; Revised 13 June 2011;Accepted 8 July 2011
```
```
DOI: 10.1002/hbm.21432Published online in Wiley Online Library (wileyonlinelibrary.
```
```
com).
```
VC 2011 Wiley Periodicals, Inc.
131
INTRODUCTION
```
Neuropsychological evaluation of patients with refrac-tory mesial temporal lobe epilepsy (MTLE) associated with
```
```
hippocampal atrophy (HA) and other MRI signs of hippo-campal sclerosis (HS) usually reveal a mild-to-moderate
```
```
memory deficit [Engel et al., 1997; French et al., 1993].According to the classic material-specific model of mem-
```
```
ory, lesions in the hippocampus of the left temporal lobe(dominant for language) may implicate in verbal memory
```
```
deficits [Meyer and Yates, 1955; Milner, 1972; Novellyet al., 1984] and those of the right temporal lobe, in visual
```
```
memory deficits [Jones-Gotman, 1987; Kimura, 1963; Mil-ner et al., 1962]. However, more recent studies in epilepsy
```
surgery have shown that the relationship between lateral-ized hippocampal pathology and memory dysfunction is
```
more evident in left MTLE than in right MTLE [Alessioet al., 2004a,b; Hermann et al., 1997; Jones-Gotman, 1996;
```
```
Lencz et al., 1992; Saling et al., 1993; Trenerry et al., 1995].Evidences have suggested that the most important predic-
```
tor factor for postoperative memory decline is the func-tional capacity of the ipsilateral mesial temporal lobe
```
(MTL; hippocampal adequacy model) rather than the func-tional reserve of the contralateral MTL (hippocampal
```
```
reserve model) to sustain memory performance [Powellet al., 2007; Rabin et al., 2004]. However, MRI findings
```
associated with neuropsychological data are not alwayssufficient to determine the risk of language and/or mem-
ory impairment following mesial temporal resection.Application of more invasive procedures, such as intracra-
```
nial monitoring with depth electrodes (SEEG) and intracar-otid sodium amytal test (IAT or Wada test), may be
```
```
considered necessary [Dinner, 1991; Golby et al., 2002;Lineweaver et al., 2006; Rausch and Langfitt, 1991].
```
Even though considered the gold standard, the IAT hasa series of limitations, including its invasiveness, poor spa-
tial resolution, insufficient time for detailed evaluation oflanguage and memory functions and limited ability to dis-
```
tinguish verbal versus visual memory deficits [Dade andJones-Gotman, 1997; Gotman et al., 1992; Loring et al.,
```
```
1990; Lukban et al., 1994; Rausch, 2002]. Because of theselimitations of IAT, some researchers have aimed to explore
```
```
alternative methods, such as fMRI [Aldenkamp et al.,2003; Golby et al., 2002; Rausch, 2002].
```
Although the role of fMRI in the lateralization of hemi-spheric dominance for language is relatively well-estab-
lished, such an application has so far not been provedreliable in the lateralization of verbal and visual memories
[Jokeit et al., 2001]. fMRI evaluation of memory is moredifficult than fMRI evaluation of other cognitive functions
```
due to some neuropsychological and technical issues[Alessio et al., 2004b; Detre et al., 1998; Jones-Gotman,
```
```
1996; Powell et al., 2004, 2005 Strange, 2002; Richardsonet al., 2003].
```
```
Keeping all the above factors in mind, the purposes ofthis study were: (1) to identify the brain areas involved in
```
verbal and visual memory processing in normal controls
```
and patients with unilateral MTLE associated with ipsilat-eral HS, by means of fMRI; and (2) to assess the sensitivity
```
and potential clinical role of memory tests applied duringfMRI experiments in lateralizing and localizing verbal and
visual memory functions, during two distinct stages ofmemory processing, namely: encoding and retrieval.
PATIENTS AND METHODS
Ascertainment of Subjects
In this study we included patients with diagnosis of re-fractory MTLE followed at our epilepsy clinic. We also
included a control group, which were submitted to thesame protocols. All individuals signed a written consent,
approved by the ethics committee of UNICAMP MedicalSchool.
The clinical criterion was a history of simple partialand/or complex partial seizures with characteristics of
MTL origin, such as: rising epigastric sensation, fear, expe-riential phenomena, and autonomic signs and symptoms.
As a complement of this clinical criterion, no suggestion ofany other partial epilepsy syndrome could be present. The
EEG criterion was the presence of interictal epileptiformdischarges over mid-inferomesial temporal regions and no
clear-cut epileptiform abnormalities elsewhere.The selected 26 individuals were divided into three
groups, as follows: control group, composed of nine nor-mal controls with no history of epilepsy or any other neu-
```
rological and/or psychiatric pathology, and at ages andeducation level similar to the patient groups; right-HS
```
group, composed of eight patients who fulfilled clinical-EEG criteria for right MTLE and who had right HA and
```
other signs of unilateral right HS on MRI; and finally, left-HS group, composed of nine patients who also had clinical
```
and EEG diagnosis of left MTLE and had left HA andother signs of unilateral left HS on MRI. All patients had
normal hippocampal volumes contralateral to the EEG lat-eralization, determined by MRI volumetric analysis
according to a previously defined protocol [Bonilha et al.,2004]. Other MRI signs of HS, including hyperintense T2
signal were evaluated clinically by one of the authors withexperience in neuroimaging investigation in epilepsies
```
(F.C.).
```
Neuropsychological Evaluation
```
Both patient groups were submitted to an extensive neu-ropsychological evaluation, which included: (1) vocabulary
```
```
and block design subtests of the Wechsler adult intelli-gence scale-revised (WAIS-R) to estimate IQ; (2) the Edin-
```
burgh handedness inventory and dichotic listening test todetermine hemispheric dominance for language and, by
```
inference, to lateralize verbal and visual memories; (3) thelogical memory and verbal paired associates of the Wechs-
```
```
ler memory scale-revised (WMS-R) to investigate verbal
```
r Alessio et al. r
r 2 r
132
```
memory; and (4) the figural memory, visual reproduction,and visual paired associates of the WMS-R to investigate
```
visual memory. To control other cognitive functions thatcould somehow influence memory tasks, they were also
```
submitted to tests for language (verbal fluency test andBoston naming test/BNT), and attention [Strub and Black
```
```
Vigilance Test; Fromm-Auch and Yeudall, 1983; Kaplanet al., 1983; Oldfield, 1971; Spreen and Strauss, 1998; Strub
```
```
and Black, 1993; Wechsler, 1981, 1987]. These tests wereadapted for our population by means of few stimuli sub-
```
stitutions. However, the procedures were kept the same asthe originals. The results of each test were compared with
results for normal controls matched by age and educa-tional level. We did not use the same fMRI control group
for neuropsychological data.
Verbal and Visual Memory Tests During fMRI
Verbal memory evaluation during fMRI consisted ofencoding and immediate recall of 17 abstract and emotion-
ally neutral words [the equivalent Portuguese translationsfor HONOR, OPINION, PROBLEM, DUTY, INTEREST,
PATIENCE, SOUL, LAW, OPTION, HAZARD, SYMPA-THY, PRIDE, DECISION, CRITERIA, SYSTEM, LIFE,
METHOD, as proposed by Jones-Gotman et al., 1997] pre-sented in four blocks alternating with a non-word string
```
(ARLTIP) presented in five blocks. Likewise, visual mem-ory evaluation consisted of encoding and immediate recall
```
```
of 17 abstract drawings presented in four blocks alternatingwith a fixation point (‘‘þ’’) presented in five blocks [Damas-
```
```
ceno et al., 2005; Jones-Gotman et al., 1997; see Fig. 1].Individuals were instructed to focus their attention on
```
the non-word/fixation point for 34 s during the baseline
condition, and to try to memorize the 17 words/drawingsin 34 s during the experimental condition. At the end of
this encoding period, they rested for 120 s and, soon after-ward, they attempted to recall silently all words/drawings
```
during 60 s (see Fig. 2). After this immediate recall period,the individuals were requested to try to recognize, by
```
pressing a push-button, the 17 memorized words/draw-ings among another 17 new abstract words/drawings.
fMRI Acquisition and Data Analysis
Before getting into the MR scanner, all subjects receivedcomplete instructions about the verbal and visual memory
tests they were supposed to perform inside the machine.Images were acquired in a bottom/up interleaved
```
mode, using a 2T Elscint Prestige (Haifa, Israel) MR scan-ner with an EPI protocol (TR ¼ 2 s, TE ¼ 45 ms, voxel size
```
```
¼ 3 # 3 # 6 mm3). Two hundred and ninety cerebral vol-umes with 20 slices each were obtained in the run.
```
```
The functional images acquired were then (1) recon-structed and temporally reorganized, (2) transformed from
```
```
DICOM-2D into ANALYSE-3D format by using the MRI-cro software, and finally (3) slice timed, realigned, normal-
```
```
ized (MNI standard template), smoothed (6 mm/FWHM)and analyzed by using the SPM2 software package
```
```
(http://www.fil.ion.ucl.ac.uk/spm/). The imaging prepro-cessing was carried out individually for each subject and
```
```
run, while the data analysis was performed putting to-gether all subjects of the same group (control group, right-
```
```
HS group and left-HS group).We attempted to maximize the signal-to-noise ratio
```
before acquiring the EPI images by following a semi-auto-matic shimming procedure to homogenize the magnetic
Figure 1.The cross and the 17 abstract drawings.
r Brain Plasticity for Verbal and Visual Memories r
r 3 r
133
field strength in the brain region to the sub-ppm level. Inorder to reduce the chance for ghost artifacts, we have
made use of an algorithm proposed by Buonocore andGao [1997] during the image reconstruction stage.
For data analysis, the following parameters wereadopted: gama function with window length of 32 and
order 1, whereas model interaction, parametric modula-tion, other regressors, removal of global effects, high-pass
filter and correction for serial correlations were left aside.Three T-test contrasts were created in order to identify cer-
```
ebral areas related to verbal memory encoding (wordblocks—minus—nonword blocks) and immediate recall
```
```
(words recall). The same procedure was adopted for visualmemory encoding and immediate recall (see Fig. 2). In
```
other words, the first two contrasts designed were wordblocks and nonword blocks and the third one, immediate
recall. In order to identify the cerebral areas activated dur-ing encoding stage, we assigned the value ‘‘1’’ to the word
```
blocks and the value ‘‘-1’’ to the nonword blocks, while novalue was assigned to the baseline condition (OFF). We
```
also assigned the value ‘‘0’’ to the immediate recall blockbecause in doing so it was left aside of this analysis. Then,
the program performed not only the subtraction of wordblocks—minus—nonword blocks but also compared this
result to the baseline condition result. Soon afterwards, toidentify the cerebral regions activated during immediate
recall stage, we assigned the value ‘‘1’’ to the immediaterecall block and no value to the baseline condition. Once
again, the value ‘‘0’’ was assigned to the word and non-word blocks, which were left aside of this second analysis.
Finally, for the results visualization a threshold of P <0.001, uncorrected for multiple comparisons, and clusters of
125/0 voxels were used for the encoding/retrieval phase.
RESULTS
```
The three groups had similar age and educational level(Table I). The two patient groups were similar in age of
```
seizure onset, duration of epilepsy, seizure frequency, andnumber of antiepileptic drugs used, as well as in the
results of the Edinburgh handedness inventory, dichoticlistening test, Boston naming test, verbal fluency test,
Strub&Black vigilance test, visual memory tests, and fMRIrecognition tests. The only difference between them was
```
that patients with left HS had lower IQ (F ¼ 9.656; P ¼0.008) and worse performance on tests of general memory
```
```
(F ¼ 15.387; P ¼ 0.002), verbal memory (F ¼ 14.510; P ¼0.002), and delayed recall (F ¼ 6.345; P ¼ 0.025) than
```
```
patients with right HS (Table II).As already mentioned, three contrasts were designed
```
during the SPM2 analysis aiming to visualize the resultsfor encoding [-1 1 0] and immediate recall [0 0 1] stages.
The differences between cerebral areas activated duringencoding and immediate recall of verbal versus visual
memories are shown in Table III.
Verbal Memory Test
```
The data analysis of the encoding stage revealed activa-tions of: (1) bilateral occipital cortices in the three groups;
```
```
(2) right parietal cortex in control group, and bilateral pari-etal cortices in right-HS and left-HS groups; (3) left supe-
```
rior temporal cortex in control group, bilateral superiortemporal cortices in right-HS group, and right superior
```
temporal cortex in left-HS group; (4) bilateral middle fron-tal cortices in control and left-HS groups, and left middle
```
```
frontal cortex in right-HS group (see Fig. 3); and (5) bilat-eral>left ventro-lateral frontal cortices in right-HS group
```
and bilateral>right ventro-lateral frontal cortices in left-HSgroup, while there was no such activation in control group
```
(see Fig. 4).The data analysis of immediate recall showed activa-
```
```
tions of: (1) left occipital cortex in control and right-HSgroups, and bilateral occipital cortices in left-HS group; (2)
```
```
left parietal cortex in the three groups; (3) right superiortemporal cortex in control and left-HS groups, whereas no
```
Figure 2.Verbal and visual memory paradigms. [Color figure can be viewed in the online issue, which is available at wileyonlinelibrary.com.]
r Alessio et al. r
r 4 r
134
```
such activation was detected in right-HS group; (4) bilater-al>right infero-medial temporal cortices in control group
```
```
and right infero-medial temporal cortex in right-HS group,and absence of such activation in left-HS group (see Fig.
```
```
5); (5) right ventro-lateral frontal cortex in right-HS andleft-HS groups, while no such activation was identified in
```
```
control group (see Fig. 6); and (6) right prefrontal cortex incontrol and right-HS groups, and bilateral prefrontal corti-
```
ces in left-HS group.
Visual Memory Test
```
The data analysis of the encoding stage revealed activa-tions of: (1) bilateral occipital and parietal cortices in the
```
```
three groups, (2) right frontal cortex in control group, andbilateral superior and inferior frontal and prefrontal corti-
```
```
ces in right-HS and left-HS groups (see Fig. 7); and (3)bilateral inferior temporal cortices in right-HS group (see
```
```
Fig. 8), while there was no such activation in control andleft-HS groups.
```
```
The data analysis of immediate recall showed activa-tions of: (1) bilateral cerebellum in the three groups; (2)
```
```
right occipital cortex in control group, and left occipitalcortex in left-HS and right-HS groups; (3) bilateral parietal
```
```
cortices in control group, and left parietal cortices in left-HS and right-HS groups; (4) right prefrontal cortex in con-
```
```
trol group and bilateral prefrontal cortex in left-HS group(see Fig. 9), whereas no such activation was detected in
```
```
right-HS; (5) bilateral inferior temporal cortices in controlgroup, and right inferior temporal cortex in left-HS and
```
```
right-HS groups; (6) right mid-temporal cortex in controland left-HS groups, while there was no such activation in
```
```
right-HS; and (7) bilateral hippocampal cortices in controlgroup (see Fig. 10).
```
DISCUSSION
As already well-established in the literature, neuropsy-chological evaluation of patients with refractory MTLE
TABLE I. Demografic and fMRI data of subjects
```
SubjectsAge(years)Education(years)
```
fMRI verbalmemory
```
(correct answers)
```
fMRI visualmemory
```
(correct answers)
```
Edinburghhandedness
inventory
Controls1 38 4 7 13 right
2 23 16 17 14 right3 19 11 12 8 right
4 29 15 10 8 right5 31 11 10 16 right
6 50 7 12 11 right7 40 15 17 17 right
8 35 5 12 8 right9 31 11 16 12 right
Right-HS group1 34 11 12 12 right
2 32 11 5 NA right3 43 11 13 11 right
4 49 11 14 14 left5 50 16 14 15 right
6 41 13 15 11 right7 38 8 12 13 right
8 35 8 17 16 rightLeft-HS group
1 48 15 15 14 right2 42 4 7 11 right
3 24 11 14 11 right4 34 11 8 13 right
5 47 8 11 13 left6 33 11 8 9 right
7 42 7 0 NA right8 20 4 15 14 Right
9 31 5 11 12 RightF and 1.5 1.574 1.402 0.508 0.536
P values 0.244 0.229 0.266 0.609 0.592
NA, not available.
r Brain Plasticity for Verbal and Visual Memories r
r 5 r
135
TABLE II. MRI, clinical, and neuropsychological data of patients
Patients

MRI
Side ofTL spikeson EEG
```
Age atseizureonset(years)
```
```
Duration ofepilepsy(years)
```
```
Seizurefrequency(P/month)
```

AEDs
Dichoticlisteningtest
WAIS-RestimatedIQ
```
Bostonnamingtest(z score)
```
```
Verbalfluencytest(z score)
```
```
Vigilancetest(errors)
```
```
WMS-Rgeneralmemory(z score)
```
```
WMS-Rverbalmemory(z score)
```
```
WMS-Rvisualmemory(z score)
```
```
WMS-Rdelayedrecall(z score)
```
Right-HS group1
# RHA

right

4
30
20
```
CBZ; CLN
```

left
100
0.12

!0.63

0
1.23

1.53

-0,05

1,95
2
# RHA

right

8
24
12
```
CBZ; CLB
```

# NA

97
!4.8

!0.63

0
0.4
0.68

-0,37

-0,24
3
# RHA

right

7
36
2
```
PNT; CLB
```

left
86
!3.39

!0.19

0
!0.55

!0.54

-0,76

-1,02
4
# RHA

right

0
49
14
```
CBZ; CLB
```

left
100
!2.13

!0.85

1
0.46

!0.02

1,68

-0,45
5
# RHA

right

19
31
2
```
LMT; CLB
```

left
115
!0.11

0.02

0
2.38

2.96

0,46

3,16
6
# RHA

right

6
34
12
```
CBZ; CLB
```

left
100
1.32

0.46

1
0.9
0.77

0,63

0,48
7
# RHA

right

4
34
30
# CBZ

left
92
!1.11

# NA

0
!0.04

0.07

-0,11

-1
8
# RHA

right

4
31
4
```
CBZ; CLB
```

left
97
!0.58

!0.85

0
1.29

1.07

1,04

1,88
Left-HS group1
# LHA

left
1
47
2
```
OXC; CLB
```

# NA

94
!1.26

!0.85

0
!0.76

!1.19

0.78

!0.77
2
# LHA

left
20
22
40
```
CBZ; CLB
```

left
80
!501

!1.02

1
!0.23

!0.22

!0.24

!1.3
3
# LHA

left
2
22
6
```
CBZ; TPM
```

left
88
!4.49

!0.85

0
!1.25

!1.12

!0.5

!0.24
4
# LHA

left
4
29
1
```
CBZ; PNT; CLB
```

left
94
!2.69

!0.19

0
!0.83

!1.55

0.59

!0.65
5
# LHA

left
3
44
5
```
CBZ; CLB
```

left
89
!1.27

0.46

0
!0.04

!0.22

0.27

!0.03
6
# LHA

left
7
26
2
```
LMT; TPM; CLB
```

left
89
!1
1.34

0
!0.04

!0.09

0.01

!0.59
7
# LHA

left
2
40
4
```
CBZ; CLB
```

left
80
!7.97

!1.64

0
!1.83

!2.3

0.01

!1.73
8
# LHA

left
2
18
11
# CBZ

left
# NA

# NA

# NA

# NA

# NA

# NA

# NA

NA
9
# LHA

left
4
27
4
# CBZ

left
86
!4.45

# NA

0
!1.51

!1.12

!1.53

!3.15
F and

0.287

0.482

0.461

0.204

9.656

3.855

0.001

0.368

15.387

14.51

1.061

6.345
P values

0.600

0.498

0.508

0.658

0.008

0.07

0.979

0.554

0.002

0.002

0.32

0.025
TL,
```
temporal lobe;
```
RHA,
```
right hippocampal atrophy;
```
LHA,
```
left hippocampal atrophy;
```
AEDs,
```
antiepileptic drugs;
```
CBZ,
```
carbamazepine;
```
CLB,
```
clobazam;
```
PNT,
```
phenytoin;
```
LMT,
```
lamotrigine;
```
TPM,
```
topiramate;
```
CLN,
```
clonazepam;
```
NA
, not available.
136
```
associated with HA usually reveals a mild-to-moderatememory deficit [Engel et al., 1997; French et al., 1993].
```
According to our previous studies [Alessio et al., 2004a,b],patients with refractory MTLE have more memory deficits
than those with drug-responsive MTLE, regardless of thepresence and degree of HA on MRI. On the other hand,
individuals with HA on MRI exhibit more memoryimpairment than individuals with normal MRI, regardless
of the presence and frequency of seizures. However, the
interaction of refractory seizures and HA is related to theworst memory performance [Alessio et al., 2004a,b].
Verbal Memory
A matter of less agreement in the literature concerns theclassic material-specific model of memory. More recent
studies in epilepsy surgery have shown that the
Figure 3.Encoding activations of bilateral middle frontal cortices in control and Left-HS groups, and left
middle frontal cortex in Right-HS group.
TABLE III. Comparison of verbal and visual memories activation areas
Activation areas
Encoding of verbal memory Immediate recall of verbal memory
ControlgroupRight-HSgroupLeft-HSgroupControlgroupRight-HSgroupLeft-HSgroup
R L B R L B R L B R L B R L B R L B
Superior temporal cortex * * * * *Infero-medial temporal cortex * *
Middle frontal cortex * * *Ventro-lateral frontal cortex * * * *
Parietal cortex * * * * * *Occipital cortex * * * * * *
Encoding of visual memory Immediate recall of visual memory
Inferior temporal cortex * * * *Mid-temporal cortex * *
Hippocampal cortex *Superior and inferior frontal cortex * * *
Prefrontal cortex * * * * *Parietal cortex * * * * * *
Occipital cortex * * * * * *Cerebellum * * *
```
R, right; L, left; B, bilateral; * presence of activation.
```
r Brain Plasticity for Verbal and Visual Memories r
r 7 r
137
relationship between lateralized hippocampal pathologyand memory dysfunction is more evident in left MTLE for
verbal memory deficits than in right MTLE for visualmemory [Alessio et al., 2004a,b]. However, it is not well
```
established what kind of verbal memory process (encod-ing, consolidation, or retrieval) is related to which cortical
```
brain regions in these patients, and this issue is particu-larly important when selecting candidates for resection of
mesial temporal lobe structures.Hence, one of the purposes of this study was to identify
and compare the cerebral areas involved in verbal memoryprocessing in normal controls and in patients with refrac-
tory MTLE by means of fMRI. More specifically, we triedto localize and lateralize verbal memory function, during
two distinct stages of memory processing: encoding andretrieval.
The first important result of this study is the fact thatthe two patient groups were similar as regards several var-
iables which can influence verbal memory performance,such as age of seizure onset, duration of epilepsy, seizure
frequency, and number of antiepileptic drugs used, aswell as vigilance, language and visual memory functions.
Nevertheless, patients with left HS had worse performanceon verbal memory, general memory and delayed recall
Figure 4.Encoding activations of bilateral > left ventro-lateral frontal cortices in Right-HS group and bilat-
eral > right ventro-lateral frontal cortices in Left-HS group.
Figure 5.Immediate recall activations of bilateral > right infero-medial temporal cortices in control group
and right infero-medial temporal cortex in Right HS group.
r Alessio et al. r
r 8 r
138
than patients with right HS. Moreover, they also hadlower IQ, which may have contributed to their inferior
memory performance.In addition, although the three groups were similar in
age, educational level, handedness, and hemispheric domi-nance for language, they exhibited different patterns of
activations not only in the encoding stage, but also in theretrieval stage of verbal memory processing.
With regard to the encoding stage, patients with left HSshowed more widespread areas of activations than
patients with right HS, and even more than normal con-trols. Although this pattern had been observed in the occi-
```
pital (Brodmann areas [BA]: 17/18), parietal (BA: 7) andtemporal regions (BA: 21/22), it seemed to be mostly re-
```
markable in the middle and ventro-lateral frontal regions
```
(BA: 6/8 and 44/45, respectively). These findings are inaccordance with previous fMRI studies that have demon-
```
strated a larger involvement of frontal cerebral areas inverbal memory processing in patients with left MTLE
```
[Dupont et al., 2000; Golby et al., 2001].Patients with left HS also tended to exhibit more bilat-
```
```
eral or right lateralized encoding related activations (Figs.3 and 4). This functional reorganization and, consequently,
```
cortical reallocation of verbal memory encoding in morewidespread bilateral fronto-parietal, and right temporal
areas in patients with left MTLE may indicate a compensa-tory strategy for the dysfunction of left MTL system
[Dupont et al., 2000]. A less evident functional reorganiza-tion of verbal memory encoding was also detected in the
bilateral parietal, bilateral>left ventro-lateral frontal, left
Figure 6.Immediate recall activations of right ventro lateral frontal cortex in Right HS and left HS groups.
Figure 7.Encoding activations of right frontal cortex in control group, and bilateral superior and inferior
frontal and prefrontal cortices in Right HS and left HS groups.
r Brain Plasticity for Verbal and Visual Memories r
r 9 r
139
middle frontal, and bilateral superior temporal cortices inpatients with right HS, as compared to normal controls.
We could also hypothesize that this functional rearrange-ment can be secondary to the failure of right MTL system.
Another interpretation of our regional activation dataduring verbal encoding is that the block designed visual
presentation of the abstracts words could also activate thesemantic working memory processing of these words,
```
whose meanings (concepts) are accessed almost automati-cally. Indeed, a ‘‘semantic working memory system’’ re-
```
sponsible for retrieving, maintaining, monitoring andmanipulating semantic representations and composed par-
ticularly by the left anterior-inferior prefrontal cortex andthe polar region of the left temporal lobe, has been pro-
posed by Gabrieli et al. [1998], Wagner [1999], and Martinand Chao [2001]. Additional evidence for the relevance of
the left lateral prefrontal cortex for semantic processing of
```
abstract words has been yielded afterward by otherauthors [Fiebach and Friederici, 2004; Goldberg et al.,
```
2007]. In an event-related fMRI study of normal readersFiebach and Friederici [2004] found that different semantic
classes of nouns are processed in distinct cortical regionswithin the left hemisphere, with concrete nouns activating
preferentially the left basal temporal cortex, and abstractnouns the left inferior frontal cortex. In patients with left
MTLE and HS, on the contrary, similar studies haveshown a shift of activations to homologous regions in the
right hemisphere during the processing of abstract wordsas compared to concrete words and non-words [Edwards
```
et al., 2005; Koylu et al., 2006]. Our group of left MTLEand HS patients showed similar shifted distribution of
```
```
activations: right temporal, right or bilateral inferolateralfrontal, bilateral middle frontal and bilateral parietal.
```
Thus, this widespread contralateral and ipsilateral corticalactivation may be interpreted as resulting not only from
the episodic encoding but also from the semantic workingmemory processing of the words presented.
With respect to the retrieval stage, patients with MTLEassociated with left HS continued to show more wide-
spread areas of activations than patients with right HSand normal controls. Once more, this pattern was more
evident in the frontal region. However, it is important toemphasize that the activation areas observed in the re-
trieval stage were smaller than those detected in theencoding stage in the three groups.
In the retrieval period, as opposed to the encodingstage, not only patients with left HS, but also patients with
```
right HS and normal controls tended to exhibit more bilat-eral and right-sided activations (Figs. 5 and 6).
```
This prevalence of right hemisphere activations duringthe retrieval stage is in agreement with the hemispheric
```
encoding/retrieval asymmetry (HERA) model, which pre-dicts prefrontal activation during encoding of new
```
Figure 8.Encoding activations of bilateral inferior temporal cortices in
Right HS group.
Figure 9.Immediate recall activations of right prefrontal cortex in control group and bilateral prefrontal cortices left HS group.
r Alessio et al. r
r 10 r
140
information mainly in the left hemisphere, whereas re-trieval of previously learned information is accompanied
```
by increased activity in right prefrontal areas [Dupontet al., 2000; Kapur et al., 1994; Kennepohl et al., 2007;
```
```
Powell et al., 2004; Tulving et al., 1994]. Although it con-cerns only to the material-independent lateralization of
```
certain memory tasks in frontal lobes, some authors haverecommended that it be extended to temporal lobe regions
[Kennepohl et al., 2007]. During retrieval, our group of leftMTLE patients showed bilateral prefrontal activation with
right frontal ventrolateral predominance, which indicates areduction of the functional hemispheric asymmetry in this
```
task, similarly to that observed with normal aging (the socalled HAROLD, Hemispheric Asymmetry Reduction in
```
```
Older adults), [Cabeza, 2002]. In patients with left MTLE,the increased (bilateral) prefrontal activation not only may
```
be compensatory, but also may represent a decrease in thelevel of functional differentiation of the task-relevant neu-
ral systems, as proposed by Chen et al. [2002] for theHAROLD model. It remains unexplained why our group
```
of patients with right MTLE presented ipsilateral activa-tion (right prefrontal, frontal ventrolateral, and temporal
```
```
inferomedial), thus preserving the prevalence of righthemisphere activations during retrieval. It is possible that
```
their long epilepsy duration with early development ofright HS has led to intrahemispheric reorganization of cog-
nitive functions.
Visual Memory
Our previous studies did not show a significant correla-tion between the degrees of right HA and visual memory
```
deficits in patients with right MTLE [Alessio et al.,2004a,b, 2006; Bonilha et al., 2007]. Two hypotheses have
```
```
been raised to explain this lack of correlation: (1) the vis-ual memory may have a more diffuse and bilateral repre-
```
```
sentation in the brain [Helmstaedter and Kurthen, 2001;
```
```
Jones-Gotman, 1996], and/or (2) the visual memory testsemployed may not be robust enough to identify nondomi-
```
nant hippocampal dysfunction [Jones-Gotman, 1996]. Webelieve in a combination of these two hypotheses, because:
```
(1) we found visual memory deficits in MTLE patientswith bilateral HA and rarely in those with right unilateral
```
```
HA, and (2) we observed that some patients made use ofverbal strategies in order to memorize a visual content
```
[Alessio et al., 2004a].Hence, another purpose of this study was to identify
and compare the cerebral areas involved in visual memoryprocessing in normal controls and patients with refractory
MTLE by means of fMRI.With regard to the encoding stage, patients with right
MTLE showed more widespread and bilateral areas ofactivations than patients with left MTLE, and even more
```
than normal controls. Moreover, while normal controlstended to exhibit asymmetrical (bilateral>right) activated
```
regions, patients with right HS tended to show more sym-metrical and bilateral activated regions probably to com-
```
pensate for the failure of their right MTL system (Figs. 7and 8).
```
These findings are in agreement with the hypothesis ofa more diffuse and bilateral representation of visual mem-
ory in the brain. Not only MTL structures, but also tem-poroparietal and prefrontal areas seem to be involved with
```
the functional neuroanatomy of visual memory, as follows:(1) posterior parietal cortex provides a bridge from percep-
```
```
tion to recognition, it is related to attention and spatialawareness, and it takes part in spatial memory; and (2)
```
dorsolateral prefrontal cortex is associated with attention,working memory and executive functions that are also
```
critical for memory processes [Burgess et al., 2001; Des-granges et al., 1998].
```
```
However, in contrast to some authors [Detre et al., 1998;Stern et al., 1996; Szaflarski et al., 2004] who have found
```
bilateral-symmetrical hippocampal activation in normalcontrols and bilateral-asymmetrical hippocampal activation
in MTLE patients, we did not find hippocampal activa-tions in the three groups during encoding stage of a visual
```
content. This discrepancy could be explained by (1) differ-ences in the fMRI task design; and/or (2) lack of MTL acti-
```
vation in our study owing to those technical limitationsmentioned before, such as geometric distortions, signal
```
loss artifacts, and partial volume effects [Figueiredo et al.,2008; Powell et al., 2004, 2005, 2007]. For different reasons
```
some other functional studies have also failed to demon-strate hippocampal activation either during encoding or
```
retrieval stages [Cabeza and Nyberg, 2000; Schacter andWagner, 1999].
```
With respect to the retrieval stage, the activation pat-terns found in the three groups were exactly the opposite
of those detected in the encoding stage. Compared topatients with right MTLE, left MTLE patients retrieval pro-
```
duced more diffuse activation, which was even more dif-fuse in normal controls (Figs. 9 and 10). It is important to
```
note that in the retrieval stage we were able to detect
Figure 10.Immediate recall activations of bilateral hippocampal cortices in
control group.
r Brain Plasticity for Verbal and Visual Memories r
r 11 r
141
bilateral symmetrical hippocampal activation in the controlgroup [Jokeit et al., 2001]. Again, not only MTL structures
but also temporal, parietal and prefrontal areas seem to beinvolved in visual memory processing [Burgess et al.,
```
2001; Engelsen et al., 2006; Fletcher, 1995; Ungerleideret al., 1998].
```
In addition, patients with right-HS tended to exhibitmore left-sided activated areas during retrieval as opposed
to patients with left-HS and normal controls, which tendedto show more bilateral and right-sided activations. This
prevalence of right hemisphere activations during the re-trieval stage in normal controls is in agreement with the
```
hemispheric encoding/retrieval asymmetry (HERA)model. Patients with right MTLE, on the contrary, tended
```
to show more left-sided activated areas probably to com-pensate for the failure of their right MTL system.
Limitations
As already mentioned, fMRI evaluation of memory ismore difficult than fMRI evaluation of other cognitive
functions, due to some neuropsychological and technicalissues [Powell et al., 2004, 2005]. As regards the neuropsy-
```
chological aspects, we polarized as much as possible theverbal versus the nonverbal (visual) memory contents, by
```
using a list of 17 abstract and emotionally neutral wordsas opposed to a series of 17 abstract drawings. In spite of
this, some of the drawings may have led the patients touse verbal strategies in order to memorize the visual con-
tent. In addition, the drawings may have led to a differentpattern of activation because they were more complex
```
than the fixation point (‘‘þ’’) of the baseline condition. Inaddition, the technical aspects could not be so well con-
```
```
trolled, because (1) the fMRI acquisitions were made usingEPI sequence, which is particularly susceptible to geomet-
```
```
ric distortions and signal loss, and (2) the BOLD responseis naturally lower in the hippocampal regions. All these
```
problems may have contributed to the relative lack ofMTL activations, and their solution requires paradigms
with even less verbalizable visual-spatial test material andmore complex stimulus than a fixation point, as well as
fMRI equipments with higher spatial resolution andgreater sensitivity.
However, we believe that the restrictive and rigorousstatistical analysis that we performed in the present study
make our findings quite reliable.
CONCLUSION
A complex network including parietal, temporal andfrontal cortices seems to be involved in verbal memory
encoding and retrieval in normal controls. The extensionof such activations was larger in patients with right and
left HS, more so in patients with left HS. Whereas normalcontrols and patients with right HS tended to exhibit more
left-sided activated areas, patients with left HS tended to
show more bilateral and right-sided activated regions inthe encoding stage. These findings can indicate either a
dysfunction or a functional reorganization of verbal mem-ory processing in other cerebral regions, particularly in
frontal lobes. In contrast, the three groups presented moreright-sided activated areas in the retrieval stage, which is
in agreement with the HERA model.As regards visual memory encoding and retrieval, our
findings support the hypothesis of a more diffuse andbilateral representation of this cognitive function in the
brain. Compared to normal controls, encoding of visualmaterial in patients with left HS recruited more wide-
spread cortical areas, which were even more widespreadin patients with right HS probably to compensate for their
right mesial temporal dysfunction. On the other hand,when compared to the right MTLE group, the drawing re-
trieval task produced more diffuse activation in the leftMTLE group and even more diffuse activation in the con-
```
trol group (including also both hippocampi). In spite oftheir effort in memorizing (encoding) the 17 drawings,
```
patients with right MTLE exhibited fewer activated areasduring immediate recall probably related to their greater
difficulty in dealing with visual memory content.
REFERENCES
Aldenkamp AP, Boon PA, Deblaere K, Achten E, Backes WH,Boon P, Hofman P, Troost J, Vandemaele P, Vermeulen J,
```
Vonck K, Wilmink J (2003): Usefulness of language and mem-ory testing during intracarotid amobarbital testing: Observa-
```
tions from an fMRI study. Acta Neurol Scand 108:147–152.Alessio A, Kobayashi E, Damasceno BP, Lopes-Cendes I, Cendes F
```
(2004a): Evidence of memory impairment in asymptomatic indi-viduals with hippocampal atrophy. Epilepsy Behav 5:981–987.
```
```
Alessio A, Damasceno BP, Camargo CHP, Kobayashi E, GuerreiroCAM, Cendes F (2004b): Differences in memory performance
```
and other clinical characteristics in patients with mesial tempo-ral lobe epilepsy with and without hippocampal atrophy. Epi-
lepsy Behav 5:22–27.Alessio A, Bonilha L, Rorden C, Kobayashi E, Li ML, Damasceno
```
BP, Cendes F (2006): Memory and language impairments andtheir relationship to hippocampal and perirhinal cortex dam-
```
age in patients with medial temporal lobe epilepsy. EpilepsyBehav 8:593–600.
```
Baxendale SA (1997): The role of the hippocampus in recognitionmemory. Neuropsychologia 35:591–598.
```
```
Baxendale SA, Thompson P, Harkness W, Duncan J (2006): Pre-dicting memory decline following epilepsy surgery: A multi-
```
```
variate approach. Epilepsia 47:1887–1894.Bonilha L, Kobayashi E, Cendes F, Li LM (2004): Protocol for vol-
```
umetric segmentation of medial temporal structures using highresolution 3D MRI. Hum Brain Mapp 22:145–154.
```
Bonilha L, Alessio A, Rorden C, Baylis G, Damasceno BP, Li ML,Cendes F (2007): Extrahippocampal gray matter atrophy and
```
memory impairment in patients with medial temporal lobeepilepsy. Hum Brain Mapp 28:1376–1390.
```
Bunge SA, Ochsner KN, Desmond JE, Glover GH, Gabrieli JD(2001): Prefrontal regions involved in keeping information in
```
and out of mind. Brain 124:2074–2086.
r Alessio et al. r
r 12 r
142
```
Buonocore MH, Gao L (1997): Ghost artifact reduction for echoplanar imaging using image phase correction. Magn Reson
```
```
Med 38:89–100.Burgess N, Maguire EA, Spiers HJ, O’Keefe J (2001): A tempopar-
```
ietal and prefrontal network for retrieving the spatial contextof lifelike events. Neuroimage 14:439–453.
```
Cabeza R (2002): Hemispheric asymmetry reduction in olderadults: The HAROLD model. Psychol Aging 17:85–100.
```
```
Cabeza R, Nyberg L (2000): Imaging cognition II: An empiricalreview of 275 PET and fMRI studies. J Cogn Neurosci 12:1–47.
```
```
Chen J, Myerson J, Hale S (2002): Age-related dedifferentiation ofvisuospatial abilities. Neuropsychologia 40:20–50.
```
```
Dade LA, Jones-Gotman M (1997): Sodium amobarbital memorytests: What do they predict?Brain Cogn 33:189–209.
```
```
Damasceno A, Alessio A, Damasceno BP, Li LM, Cendes F (2005):Spatial and emotional memory in patients with temporal lobe
```
```
epilepsy. Neurology 64 (Suppl 1):A359–A360.Desgranges B, Baron JC, Eustache F (1998): The functional neuro-
```
anatomy of episodic memory: The role of the frontal lobes, thehippocampal formation and other areas. Neuroimage 8:198–213.
```
Detre JA, Maccotta L, King D, Alsop DC, Glosser G, D’EspositoM, Zarahn E, Aguirre GK, French JA (1998): Functional MRI
```
lateralization of memory in temporal lobe epilepsy. Neurology50:926–932.
```
Dinner DS (1991): Intracarotid amobarbital test to define languagelateralization. In: Luders H, editor. Epilepsy Surgery. New
```
```
York: Raven Press. pp 503–506.Dupont S, Van de Moortele PF, Samson S, Hasboun D, Poline JB,
```
```
Adam C, Lehe´ricy S, Le Bihan D, Samson Y, Baulac M (2000):Episodic memory in left temporal lobe epilepsy: A functional
```
```
MRI study. Brain 123:1722–1732.Edwards J, Bass A, Goodyear B, Federico P (2005): An fMRI study
```
```
of semantic reorganization in temporal lobe epilepsy. J NeurolSci 238 (Suppl 1):S122.
```
```
Engel J, Willimson PD, Wieser HG (1997): Mesial temporal lobeepilepsy. In: Engel J, Pedley TA, editors. Epilepsy: A Compre-
```
hensive Textbook. Philadelphia: Lippincott-Raven Publishers.pp 2417–2426.
```
Engelsen BA, Gramstad A, Thomsen T, Beneventi H, Ersland L,Smievoll AI, Lundervold A, Hugdahl K (2006): Frontoparietal
```
activation during delayed visuospatial recall in patients with epi-lepsy due to hippocampal sclerosis. Epilepsy Behav 8:565–574.
```
Fiebach CJ, Friederici AD (2004): Processing concrete words: fMRIevidence against a specific right-hemisphere involvement.
```
Neuropsychologia 42:62–70.Figueiredo P, Santana I, Teixeira J, Cunha C, Machado E, Sales F,
```
Almeida E, Castelo-Branco M (2008): Adaptative visual mem-ory reorganization in the right medial temporal lobe epilepsy.
```
Epilepsia 49:1395–1408.Fletcher PC, Frith CD, Baker SC, Shallice T, Frackowiak RS, Dolan
```
RJ (1995): The mind’s eye—Precuneus activation in memory-related imagery. Neuroimage 2:195–200.
```
```
French JA, Willimson PD, Thadani VM, Darcey TM, Mattson RH,Spencer SS, Spencer DD (1993): Characteristics of temporal
```
lobe epilepsy: I results of history and physical examination.Ann Neurol 34:774–780.
```
Fromm-Auch D, Yeudall LT (1983): Normative data for the Hal-stead-Reitan neuropsychological tests. J Clin Neuropsychol
```
```
5:221–238.Gabrieli JDE, Poldrack RA, Desmond JE (1998): The role of left
```
prefrontal cortex in language and memory. Proc Natl Acad SciUSA 95:906–913.
```
Gleissner U, Helmstaedter C, Schramm J, Elger CE (2004): Mem-ory outcome after selective amygdalohippocampectomy in
```
patients with temporal lobe epilepsy: One-year follow up. Epi-lepsia 45:960–962.
```
Golby AJ, Poldrack RA, Brewer JB, Spencer D, Desmond JE, AronAP, Gabrieli JD (2001): Material-specific lateralization in the
```
medial temporal lobe and prefrontal cortex during memoryencoding. Brain 124:1841–1854.
```
Golby AJ, Poldrack RA, Illes J, Chen D, Desmond JE, Gabrieli JDE(2002): Memory lateralization in medial temporal lobe epilepsy
```
```
assessed by functional MRI. Epilepsia 43:855–863.Goldberg RF, Perfetti CA, Fiez JA, Schneider W (2007): Selective
```
retrieval of abstract semantic knowledge in left prefrontal cor-tex. J Neurosci 27:3790–3798.
```
Gotman J, Bouwer MS, Jones-Gotman M (1992): Intracranial EEGstudy of brain structures affected by internal carotid injection
```
```
of sodium amobarbital. Neurology 42:2136–2143.Helmstaedter C, Kurthen M (2001): Memory and epilepsy: Charac-
```
teristics, course, and influence of drugs and surgery. CurrOpin Neurol 14:211–216.
```
Hermann BP, Connell B, Barr WB, Wyler AR (1995): The utility ofthe Warrington recognition memory test for temporal lobe epi-
```
```
lepsy: Pre and postoperative results. J Epilepsy 8:139–145.Hermann BP, Seidenberg M, Schoenfeld J, Davies K (1997): Neu-
```
ropsychological characteristics of the syndrome of mesial tem-poral lobe epilepsy. Arch Neurol 54:369–376.
```
Jokeit H, Okujava M, Woermann FG (2001): Memory fMRI lateral-izes temporal lobe epilepsy. Neurology 57:1786–1793.
```
```
Jones-Gotman M (1987): Commentary: Psychological evaluation:Testing hippocampal function. In: Engel JR, editor. Surgical
```
```
Treatment of the Epilepsies. New York: Raven Press. pp 68–76.Jones-Gotman M (1996): Psychological evaluation for epilepsy
```
surgery. In: Shorvon S, Dreifuss F, Fish D, Thomas D, editors.The Treatment of Epilepsy. Oxford: Blackwell Science. pp 621–
630.Jones-Gotman M, Zatorre RJ, Olivier A, Andermann F, Cendes F,
```
Staunton H, McMackin D, Siegel A, Wieser HG (1997): Learn-ing and retention of words and designs following excision
```
from medial or lateral temporal-lobe structures. Neuropsycho-logia 35:963–973.
```
Kaplan EF, Goodglass H, Weintaub S (1983): The Boston NamingTest. Philadelphia: Lea & Febiger.
```
```
Kapur S, Craik FI, Tulving E, Wilson AA, Houle S, Brown GM(1994): Neuroanatomical correlates of encoding in episodic
```
```
memory: Levels of processing effect. Proc Natl Acad Sci USA91:2008–2011.
```
```
Kennepohl S, Sziklas V, Garver KE, Wagner DD, Jones-Gotman M(2007): Memory and the temporal lobe: Hemispheric speciali-
```
```
zation reconsidered. Neuroimage 36:969–978.Kimura D (1963): Right temporal lobe damage. Perception of unfa-
```
miliar stimuli after damage. Arch Neurol 8:264–271.Koylu B, Trinka E, Ischebeck A, Visani P, Trieb T, Kremser C, Bar-
```
tha L, Schocke M, Benke T (2006): Neural correlates of verbalsemantic memory in patients with temporal lobe epilepsy. Epi-
```
lepsy Res 72:178–191.Lencz T, McCarthy G, Bronen RA, Scott TM, Inserni JA, Sass KJ,
```
Novelly RA, Kim JH, Spencer DD (1992): Quantitative mag-netic resonance imaging in temporal lobe epilepsy: Relation-
```
ship to neuropathology and neuropsychological function. AnnNeurol 31:629–637.
```
Lineweaver TT, Morris HH, Naugle RI, Najm IM, Diehl B, Binga-man W (2006): Evaluating the contributions of state-of-the-art
```
r Brain Plasticity for Verbal and Visual Memories r
r 13 r
143
assessment techniques to predicting memory outcome afterunilateral anterior temporal lobectomy. Epilepsia 47:1895–
1903.Loring DW, Lee GP, Meador KJ, Flanigin HF, Smith JR, Figueroa
```
RE, Martin,RC (1990): The intracarotid amobarbital procedureas a predictor of memory failure following unilateral temporal
```
lobectomy. Neurology 40:605–610.Lukban A, Dean G, Lisbona R, Dubeau F, McMackin D, Evans
```
AC (1994): Anatomical localization of seizure foci using regis-tered SPECT/MRI brain volumes. Neurology 44:385.
```
```
Martin A, Chao LL (2001): Semantic memory and the brain: Struc-ture and processes. Curr Opin Neurobiol 11:194–201.
```
```
Meyer V, Yates AJ (1955): Intellectual changes following temporallobectomy for psychomotor epilepsy. J Neurol Neurosurg Psy-
```
```
chiatry 18:44–52.Milner B (1972): Disorders of learning and memory after temporal
```
```
lobe lesions in man. Clin Neurosurg 19:421–446.Milner B, Branch C, Rasmussen T (1962): Study of short-term
```
memory after intracarotid injection of sodium amytal. TransAm Neurol Assoc 87:224–226.
```
Novelly R, Augustine EA, Mattson RH, Glaser GH, Willimson PD,Spencer DD, Spencer SS (1984): Selective memory improve-
```
ment and impairment in temporal lobectomy for epilepsy. AnnNeurol 15:64–67.
```
Oldfield RC (1971): The assessment and analysis of handedness:The Edinburgh inventory. Neuropsychologia 9:97–113.
```
```
Powell HW, Koepp MJ, Richardson MP, Symms MR, ThompsonPJ, Duncan JS (2004): The application of functional MRI of
```
memory in temporal lobe epilepsy: A clinical review. Epilepsia45:855–863.
```
Powell HW, Koepp MJ, Symms MR, Boulby PA, Salek-HaddadiA, Thompson PJ, Duncan JS, Richardson MP (2005): Material-
```
specific lateralization of memory encoding in the medial tem-poral lobe: blocked versus event-related design. Neuroimage
27:231–239.Powell HW, Richardson MP, Symms MR, Boulby PA, Thompson
```
PJ, Duncan JS, Koepp MJ (2007): Reorganization of verbal andnonverbal memory in temporal lobe epilepsy due to unilateral
```
hippocampal sclerosis. Epilepsia 48:1512–1525.Rabin ML, Narayan VM, Kimberg DY, Casasanto DJ, Glosser G,
```
Tracy JI, French JA, Sperling MR, Detre JA (2004): FunctionalMRI predicts post-surgical memory following temporal lobec-
```
```
tomy. Brain 127:2286–2298.Rausch R (2002): Epilepsy surgery within the temporal lobe and
```
its short-term and long-term effects on memory. Curr OpinNeurol 15:185–189.
```
Rausch R, Langfitt JT (1991): Memory evaluation during the intra-carotid sodium amobarbital procedure. In: Luders H, editor.
```
Epilepsy Surgery. New York: Raven Press. pp 507–514.
```
Richardson MP, Strange BA, Duncan JS, Dolan RJ (2003): Pre-served verbal memory function in left medial temporal pathol-
```
```
ogy involves reorganization of function to right medialtemporal lobe. Neuroimage 20 (Suppl 1):S112–S119.
```
```
Saling MM, Berkovic SF, O’Shea MF, Kalnins RM, Darby DG, Bla-din PF (1993): Lateralization of verbal memory and unilateral
```
hippocampal sclerosis. Evidence of task specific effects. J ClinExp Neuropsychol 15:608–618.
```
Schacter DL, Wagner AD (1999): Medial temporal lobe activationsin fMRI and PET studies of episodic encoding and retrieval.
```
```
Hippocampus 9:7–24.Spreen O, Strauss E (1998): Language tests. In: Spreen O, Strauss
```
E, editors. A Compendium of Neuropsychological Tests:Administration, Norms and Commentary. New York: Oxford
University Press. pp 423–480.Stern CE, Corkin S, Gonzalez RG, Guimaraes AR, Baker JR, Jen-
```
nings PJ, Carr CA, Sugiura RM, Vedantham V, Rosen BR(1996): The hippocampal formation participates in novel pic-
```
ture encoding: Evidence from functional magnetic resonanceimaging. Proc Natl Acad Sci USA 93:8660–8665.
```
Strange BA, Otten LJ, Josephs O, Rugg MD, Dolan RJ (2002): Dis-sociable human perirhinal, hippocampal, and parahippocam-
```
```
pal roles during verbal encoding. J Neurosci 22:523–528.Strub RL, Black FW (1993): Mental Status Examination in Neurol-
```
ogy. Philadelphia: FA Davis.Szaflarski JP, Holland SK, Schmithorst VJ, Dunn RS, Privitera MD
```
(2004): High-resolution functional MRI at 3T in health and epi-lepsy subjects: Hippocampal activation with picture encoding
```
task. Epilepsy Behav 5:244–252.Trenerry MR, Jack CR Jr, Ivnik RJ, Sharbrough FW, Cascino GD,
```
Hirschorn KA, Marsh WR, Kelly PJ, Meyer FB (1993): MRI hip-pocampal volumes and memory function before and after tem-
```
```
poral lobectomy. Neurology 43:1800–1805.Trenerry MR, Westerveld M, Meador KJ (1995): MRI hippocampal
```
volume and neuropsychology in epilepsy surgery. Magn ResonImaging 13:1125–1132.
```
Tulving E, Kapur S, Craik FI, Moscovitch M, Houle S (1994):Hemispheric encoding/retrieval asymmetry in episodic mem-
```
```
ory: Positron emission tomography findings. Proc Natl AcadSci USA 91:2016–2020.
```
```
Ungerleider LG, Courtney SM, Haxby JV (1998): A neural systemfor human visual working memory. Proc Natl Acad Sci USA
```
```
95:883–890.Wagner AD (1999): Working memory contributions to human
```
```
learning and remembering. Neuron 22:19–22.Wechsler D (1981): Wechsler Adult Intelligence Scale-Revised.
```
```
New York: Pshychological Corp.Wechsler D (1987): Wechsler Memory Scale-Revised: Manual. San
```
```
Diego: Psychological Corp/Harcourt Brace Jovanovich.
```
r Alessio et al. r
r 14 r
144
Experimento 9 – Redes neurais de pacientes obesos com disfunção hipotalâmica.
Partial Reversibility of Hypothalamic Dysfunction and
Changes in Brain Activity After Body Mass Reduction in
Obese Subjects
Simone van de Sande-Lee,1 Fabrício R.S. Pereira,2 Dennys E. Cintra,1,3 Paula T. Fernandes,2
Adilson R. Cardoso,4 Célia R. Garlipp,5 Eliton A. Chaim,6 Jose C. Pareja,6 Bruno Geloneze,7 Li Min Li,2
Fernando Cendes,2 and Licio A. Velloso1
OBJECTIVE—Inflammation and dysfunction of the hypothala-mus are common features of experimental obesity. However, it is
unknown whether obesity and massive loss of body mass canmodify the immunologic status or the functional activity of the
human brain. Therefore, the aim of this study was to determinethe effect of body mass reduction on brain functionality.
RESEARCH DESIGN AND METHODS—In humans, changesin hypothalamic activity after a meal or glucose intake can be
```
detected by functional magnetic resonance imaging (fMRI).Distinct fMRI analytic methods have been developed to explore
```
changes in the brain’s activity in several physiologic and patho-logic conditions. We used two analytic methods of fMRI to ex-
plore the changes in the brain activity after body mass reduction.
RESULTS—Obese patients present distinct functional activitypatterns in selected brain regions compared with lean subjects.
```
On massive loss of body mass, after bariatric surgery, increasesin the cerebrospinal fluid (CSF) concentrations of interleukin
```
```
(IL)-10 and IL-6 are accompanied by changes in fMRI patterns,particularly in the hypothalamus.
```
CONCLUSIONS—Massive reduction of body mass promotesa partial reversal of hypothalamic dysfunction and increases anti-
inflammatory activity in the CSF. Diabetes 60:1699–1704, 2011
O
```
besity affects more than 300 million peopleworldwide (1). It is the main risk factor for type
```
2 diabetes, atherosclerosis, and hypertension,and therefore plays an important role in the
```
overall mortality of modern societies (2). Increased adi-posity results from the progressive loss of the homeostatic
```
control of caloric intake and energy expenditure. In animalmodels, dysfunctional activity of specialized neurons of
```
the hypothalamus is regarded as an important determinantfor the development of obesity (3–6). In both genetic and
```
diet-induced obese rodents, the malfunction of the hypo-thalamus is a consequence of the activation of local in-
flammation and eventually apoptosis of selected neuronal
```
populations (3,4,7,8). The inhibition of inflammation bygenetic or pharmacologic approaches leads to the re-
```
duction of the obese phenotype and correction of themetabolic breakdown, placing hypothalamic inflammation
```
as a potential target for the treatment of obesity (3,4,8–10).We show that obese patients present distinct functional
```
activity patterns in selected brain regions, compared withlean subjects. On massive loss of body mass, increases in
```
the cerebrospinal fluid (CSF) concentrations of interleukin(IL)-10 and IL-6 are accompanied by changes in functional
```
```
magnetic resonance imaging (fMRI) patterns, particularlyin the hypothalamus.
```
```
RESEARCH DESIGN AND METHODSThirteen obese patients (11 females) were recruited from the Obesity Clinic at
```
```
the University of Campinas. All patients were selected for bariatric surgeryaccording to the National Institutes of Health Consensus Statement (11). The
```
```
surgical technique used was always the Roux-in-Y gastric bypass (12).Patients were submitted to fMRI plus blood and CSF collection at the time of
```
the surgery and after reduction of body mass. Inclusion criteria for patientselection were men and women between 18 and 60 years of age who met the
above-mentioned criteria for surgery. Exclusion criteria for patient selectionwere diabetes, inflammatory or infectious disease, use of psychotropic or
anti-inflammatory drugs, and history of substance addiction. In addition,eight lean control subjects were selected among students of the university.
Control subjects were submitted to blood collection and fMRI. Control CSFwas obtained from patients referred to the university for headache. Criteria
for selection of both control groups were the same used for patients, exceptfor a BMI ,25. The fMRI studies were performed on a 1.5 GE MRI scanner
```
(GE Healthcare, Waukesha, WI) in 12-h fasting subjects. The method forimage acquisition was the same as previously described (13) except that
```
```
a total of 500 images were acquired in 30 min. D-glucose (50 g) was ingestedafter 5 min. Leptin, insulin, and adiponectin were determined in sera using
```
```
ELISA kits from Millipore (Billerica, MA). Tumor necrosis factor-a (TNF-a),IL-1b, IL-10, and IL-6 were determined in sera and CSF using ultra-sensitive
```
```
ELISA kits from BD Biosciences (Bedford, MA) and Cayman Chemical (AnnArbor, MI). Biochemical and cellular parameters in the blood and CSF were
```
```
determined using automated methods from F. Hoffmann-La Roche (Basel,Switzerland) and Beckman Coulter (Brea, CA). Temporal clustering analysis
```
```
(TCA) and spatial analysis were performed as described (13). The fcMRIanalysis was performed as previously described (14,15) except that the seed
```
```
(virtual label that defines the target area from or toward which connectivityis evaluated) was placed in the hypothalamus. Student t test was used for
```
statistical analysis.
RESULTS
Patients were evaluated at the time of the surgery and238 6 11 days later, when body mass was reduced by 29 6
```
4% (P , 0.05). Although most patients enrolled in the studywere women, both male patients presented similar out-
```
```
comes; therefore, we have no reason to suspect the datashown in this article represent female-specific phenomena.
```
The nutritional habits of the patients were assessedaccording to the International Collaborative Study of
```
From the 1Laboratory of Cell Signaling, University of Campinas, Campinas,Brazil; the 2Department of Neurology, University of Campinas, Campinas,
```
```
Brazil; the 3Faculty of Applied Sciences, University of Campinas, Campi-nas, Brazil; the 4Department of Anesthesiology, University of Campinas,
```
```
Campinas, Brazil; the 5Department of Clinical Pathology, University ofCampinas, Campinas, Brazil; the 6Department of Surgery, University
```
```
of Campinas, Campinas, Brazil; and the 7Laboratory of Investigation inMetabolism and Diabetes, University of Campinas, Campinas, Brazil.
```
Corresponding author: Licio A. Velloso, lavelloso.unicamp@gmail.com.Received 23 November 2010 and accepted 13 March 2011.
```
DOI: 10.2337/db10-1614Ó 2011 by the American Diabetes Association. Readers may use this article as
```
long as the work is properly cited, the use is educational and not for profit,and the work is not altered. See http://creativecommons.org/licenses/by
-nc-nd/3.0/ for details.
diabetes.diabetesjournals.org DIABETES, VOL. 60, JUNE 2011 1699
BRIEF REPORT
145
```
Macro- and Micronutrients and Blood Pressure 24-h di-etary recall (16). Total caloric intake decreased from
```
```
5,602 6 3,391 to 803 6 355 kCal/day (P , 0.05), and theconsumption of saturated fats decreased from 33.6 6 6.1
```
```
to 30.3 6 11.6% of total caloric intake (P , 0.05). Of specialinterest, the relative consumption of saturated fats by
```
obese patients was greater than that of lean control sub-jects on enrollment and reduced by 10.5% after surgery,
becoming statistically similar to lean subjects. As expected,all the systemic parameters reflecting the metabolic and
```
inflammatory status of the patients improved significantlyafter massive body mass loss (Table 1), reflecting the
```
known impact of reduction of adiposity and caloric intakeon subclinical inflammation and glucose/lipid homeostasis
```
(17).Body mass loss produced no effect on cellular and
```
```
biochemical parameters in the CSF (Table 2). Two distinctultra-sensitive ELISA methods were used to evaluate TNF-a
```
and IL-1b in CSF, but these rendered no detectable levelsin all samples evaluated. However, the CSF levels of IL-10
increased in all patients, and the CSF levels of IL-6 in-creased in all except one patient, leading to statistically
```
significant increases of both these cytokines after bodymass loss (Fig. 1A and B). Both IL-6 and IL-10 levels in the
```
```
CSF were inversely correlated with BMI (Fig. 1C and D),and IL-6 levels in the CSF were inversely correlated with
```
```
IL-6 in the blood (Fig. 1E). Compared with lean subjects,IL-10 levels in the CSF of obese subjects were similar be-
```
```
fore surgery (15.9 6 8.6 vs. 18.1 6 7.8 pg/mL for obese andlean subjects, respectively) and significantly higher after
```
```
body mass loss (29.8 6 10.4 pg/mL, P , 0.05). Conversely,IL-6 levels in the CSF of obese patients were significantly
```
```
lower than in lean control subjects before surgery (1.6 61.3 vs. 6.4 6 5.3 pg/mL [P , 0.05] for obese and lean
```
```
subjects, respectively), reaching similar levels after bodymass loss (5.7 6 2.8 pg/mL). In all groups, the CSF levels of
```
IL-10 were similar or higher than the blood levels of this
```
cytokine, suggesting that, at least in part, IL-10 was pro-duced in the central nervous system (Fig. 1F). No signifi-
```
cant differences in blood monocyte counts were detectedamong obese and lean subjects and in obese patients be-
fore and after surgery.Two distinct analytic methods were used to evaluate the
```
impact of obesity and body mass loss on the activity of thebrain: TCA and functional connectivity MRI (fcMRI). TCA
```
allows for the identification of maximal response to agiven stimulus in a combination of signal intensity and
```
spatial extent (13), whereas fcMRI defines temporal cor-relations between remote neurophysiologic events, which
```
```
are hemodynamic in nature when evaluated by fMRI (14,18).For TCA, a mathematic model converts a multiple-
```
dimension data space into a relationship between the num-ber of voxels, reaching maximum signal intensity, and the
```
time (13). On a given time frame, the spatial mappingallows for the anatomic localization of the activity. We
```
```
found that a first peak of activity occurred right afterglucose intake (Fig. 2A), as previously reported (13). This
```
```
peak was similar in lean and obese subjects both beforeand after surgery (Fig. 2A). After approximately 5 min of
```
the glucose stimulus, lean subjects presented a secondpeak that was comparable to previously reported data
```
(13). However, obese patients did not present such a peak,either before or after surgery (Fig. 2A). In addition, during
```
the remaining 20 min of analysis, the number of voxelsreaching maximum activity became progressively different
among the groups. The highest activity was presented bylean subjects, whereas obese subjects before surgery
```
presented the lowest activity and obese subjects aftersurgery presented intermediate activity (Fig. 2A). Spatial
```
analysis was then performed at three distinct time win-dows, labeled in yellow in Fig. 2A. In the first window
```
(W1), which included the first peak after glucose intake,maximum activity was detected in the hypothalamus and
```
```
orbitofrontal cortex in all three conditions (lean subjects,
```
TABLE 1Blood metabolic and inflammatory parameters
Lean Obese before surgery Obese after surgery
6 females, 2 males 11 females, 2 males
```
Age (years) 29.5 6 4 34.0 6 10BMI (kg/m2) 20.9 6 2.4 39.1 6 1.9* 28.1 6 2.8*§
```
```
WC (cm) 72.2 6 9.2 110.3 6 9.9* 89.7 6 8.7*§HC (cm) 91.3 6 7.3 127.0 6 5.2* 105.0 6 7.5*§
```
```
Glucose (mg/dL) 80.6 6 3.1 84.3 6 6.1 77.9 6 7.3HbA1c (%) 4.8 6 0.2 5.2 6 0.3 5.1 6 0.3
```
```
Insulin (pmol/L) 25.0 6 10.3 68.7 6 38.1* 21.5 6 10.4§HOMA-IR 0.7 6 0.3 2.1 6 1.2* 0.6 6 0.2§
```
```
Cholesterol (mg/dL) 189 6 28 153 6 24 141 6 16HDL (mg/dL) 74.5 6 25.7 36.9 6 5.8* 52.6 6 9.1*§
```
```
LDL (mg/dL) 99.5 6 22.4 97.6 6 26.4 73.6 6 16.1Triglycerides (mg/dL) 75.5 6 38.9 94.1 6 27.1 76.6 6 19.9
```
```
CRP (mg/dL) 0.13 6 0.02 0.91 6 0.70* 0.17 6 0.02§ESR (mm/1 h) 14 6 12 26 6 16* 16 6 9§
```
```
Adiponectin (mg/mL) 6.9 6 1.7 2.7 6 1.8* 7.8 6 1.6§Leptin (ng/mL) 21.4 6 6.2 36.8 6 12.0* 17.0 6 13.9§
```
```
TNF-a (pg/mL) 5.8 6 5.5 25.6 6 10.3* 12.4 6 9.8§IL-1b (pg/mL) 2.0 6 1.8 42.9 6 26.7* 13.6 6 4.3*§
```
```
IL-6 (pg/mL) 4.1 6 4.2 26.3 6 10.2* 8.5 6 6.4§IL-10 (pg/mL) 14.0 6 10.1 15.6 6 16.5 15.8 6 5.5
```
```
CRP, C-reactive protein; ESR, erythrocyte sedimentation rate; HC, hip circumference; HOMA-IR, homeostasis model assessment of insulinresistance; WC, waist circumference. *P , 0.05 vs. lean. §P , 0.05 vs. obese before surgery.
```
HYPOTHALAMIC DYSFUNCTION IN HUMAN OBESITY
1700 DIABETES, VOL. 60, JUNE 2011 diabetes.diabetesjournals.org
146
```
obese subjects before surgery, and obese subjects aftersurgery), in the occipital cortex in lean and obese subjects
```
```
after surgery, and in the somatosensory cortex in obesesubjects both before and after surgery (Fig. 2B, W1).
```
Comparisons between the groups revealed that lean andobese subjects before surgery presented different activi-
```
ties in the hypothalamus (inset graph, Fig. 2B, W1) andoccipital and somatosensory cortices; lean and obese
```
```
subjects after surgery were mostly similar with discretedifferences in the somatosensory cortex; and obese sub-
```
```
jects before and after surgery presented different activitiesin the hypothalamus (inset graph, Fig. 2B, W1). In the
```
```
second window (W2), which included the second peakafter glucose intake, lean subjects presented the highest
```
```
activity in the hypothalamus and somatosensory and oc-cipital cortices; obese subjects before surgery presented
```
```
the highest activities in the somatosensory and occipitalcortices and cerebellum; and obese subjects after surgery
```
```
presented the highest activity in the somatosensory cortex(Fig. 2B, W2). At W2, the activities in the hypothalamus
```
```
(inset graph, Fig. 2B, W2) and somatosensory cortex were
```
different between lean and obese subjects before surgery.The comparison between lean and obese subjects after
```
surgery showed a significant difference only in the so-matosensory cortex; the comparison between obese sub-
```
```
jects before and after surgery showed differences in thehypothalamus (inset graph, Fig. 2B, W2) and occipital,
```
```
somatosensory, and orbitofrontal cortices. In the thirdwindow (W3), lean subjects presented the highest activi-
```
```
ties in the hypothalamus and orbitofrontal and somato-sensory cortices; obese subjects before surgery presented
```
```
the highest activities in the somatosensory and occipitalcortices and in the cerebellum; and obese subjects after
```
```
surgery presented the highest activity only in the somato-sensory cortex (Fig. 2B, W3). Somatosensory and orbito-
```
```
frontal cortices and the hypothalamus (inset graph, Fig.2B, W3) presented different activities when lean subjects
```
were compared with obese subjects before surgery. Onlythe orbitofrontal cortex was different between lean and
obese subjects after surgery, and somatosensory andorbitofrontal cortices were different between obese sub-
```
jects before and after surgery (Fig. 2B, W3).At both resting state and after a stimulus, synchronized
```
fluctuations of blood oxygen levels dependent on functionin fMRI signals in remote brain areas reflect physiologic or
```
pathologic patterns in a neuronal network (14,15,18). Themeasurements of such events, which are the basis of
```
fcMRI, provide maps of connectivity that indicate inte-gration and segregation of brain information. Here, a seed
was placed on the hypothalamus to explore the connec-tivity of this anatomic region with other brain areas. In
lean subjects, the hypothalamus presented the highestlevel of functional connectivity with the orbitofrontal and
```
somatosensory cortices (Fig. 3A). In obese subjects beforesurgery, functional connectivity was detected between
```
```
FIG. 1. Inflammatory markers in the CSF. Levels of IL-6 (A) and IL-10 (B) were determined in the CSF of obese patients before and after bariatricsurgery. Correlation between IL-6 (C) and IL-10 (D) concentrations in the CSF and BMI, and correlation between IL-6 concentrations in the CSF
```
```
and blood (E) were obtained. The mean (6SD) levels of IL-10 in the blood and CSF were obtained for lean and obese subjects before and aftersurgery (F). N = 8 for lean subjects; N = 13 for obese subjects. F: *P < 0.05 vs. blood/after surgery. AS, after surgery; BL, blood; BS, before surgery;
```
CS, cerebrospinal fluid.
TABLE 2Cerebrospinal fluid cellular and biochemical parameters
Lean
Obesebefore
surgery
Obeseafter
surgery
```
Glucose (mg/dL) 59.5 6 9.6 52.9 6 8.5 48.5 6 4.4Protein (mg/dL) 26.3 6 6.8 26.6 6 11.1 23.7 6 6.8
```
Leukocytes/mL 1.6 6 0.8 2.0 6 1.5 2.5 6 4.3Erythrocytes/mL 18 6 38 37 6 79 44 6 57
S. VAN DE SANDE-LEE AND ASSOCIATES
diabetes.diabetesjournals.org DIABETES, VOL. 60, JUNE 2011 1701
147
```
the hypothalamus and the orbitofrontal cortex and cere-bellum (Fig. 3B). After surgery, functional connectivity of
```
obese patients was highest between the hypothalamusand the orbitofrontal, somatosensory, and occipital cor-
```
tices (Fig. 3C). Intergroup comparisons revealed thegreatest difference in functional connectivity between
```
lean and obese subjects before surgery, particularly inthe regions of the cerebellum and somatosensory cortex
```
(Fig. 3D). Functional connectivity was mostly similar be-tween lean and obese patients after surgery (not shown).
```
Finally, some differences in functional connectivity between
obese subjects before and after surgery were detected inthe cerebellum, somatosensory, and orbitofrontal cortices
```
(Fig. 3E).
```
DISCUSSION
Both TCA and fcMRI analyses showed distinct patterns offunctionality between obese and lean subjects. The dif-
ferences were mostly confined to a few anatomic regions,predominating in the hypothalamus and somatosensory
and orbitofrontal cortices. The hypothalamus harbors
```
FIG. 2. TCA of the human brain after glucose intake. A: Time course of the activation depicted as the means of all analyzed subjects in the re-spective groups (black, lean; red, obese before surgery; blue, obese after surgery); W1–W3 represent the time windows selected for spatial
```
```
analysis. B: Spatial mapping of the brain activity at each of the time windows (W1–W3); individual group analyses were performed for lean andobese subjects before and after surgery; comparisons were also performed for all pairs of groups. The inset graphs on the right represent the signal
```
```
intensity in the region of the hypothalamus for each group. N = 8 for lean subjects; N = 13 for obese subjects. A pixel clustering size of 5 anda t-threshold of |t| >2.1 were chosen to afford a P < 0.01 level of statistical significance of the detected signal changes. This is represented by the
```
```
different colors, as defined by the normalized color bars. Color bars indicate t value for one-sample t test (lean, BS, and AS) and two-sample t test(lean vs. BS, lean vs. AS, and BS vs. AS). In the insets in B, *P < 0.01 vs. lean and #P < 0.01 vs. before surgery. AS, after surgery; BS, before
```
```
surgery; Cb, cerebellum; Hy, hypothalamus; Oc, occipital cortex; Of, orbitofrontal cortex; Ss, somatosensory cortex. (A high-quality digital rep-resentation of this figure is available in the online issue.)
```
HYPOTHALAMIC DYSFUNCTION IN HUMAN OBESITY
1702 DIABETES, VOL. 60, JUNE 2011 diabetes.diabetesjournals.org
148
hormone and nutrient-sensing neurons and provides theintegration for the energy intake and expenditure respon-
```
ses (19). Defective leptin and insulin signaling in this re-gion provides the basis for experimental obesity (5,19).
```
The somatosensory and orbitofrontal cortices integratefeeding cues with gustatory activity and facial movements,
respectively. The activities of these regions have beenshown to be modulated after a meal or glucose ingestion
```
(13,20,21), and data obtained from experimental animalsreinforce their role in the control of feeding and energy
```
```
homeostasis (5,19). The massive loss of body mass obtainedafter surgery produced obvious changes in the function-
```
ality of the brain. By either analytic method, it is clear thatchanges occurred toward the patterns found in lean sub-
jects. This is particularly evident in the TCA spatial anal-ysis, which showed only minor differences when lean
```
subjects were compared with obese subjects after surgery(Fig. 2B, W1, W2, and W3 – Lean 3 AS). Another remark-
```
able finding was the increased levels of IL-10 and IL-6 in theCSF of obese subjects after surgery. In a recent study, in-
creased levels of both these cytokines were shown to playa role in the reduction of hypothalamic resistance to leptin
```
after physical activity (22). Although inflammatory cyto-kines were not detected in the current study, we believe
```
that advancement in measurement methods will allowquantification of these cytokines and a comparison with the
```
findings in animal models, which show reductions in bothTNF-a and IL-1b after body mass loss (3,4).
```
The human brain activity in response to glucose in-gestion is modified by obesity, and body mass loss rees-
tablishes some of the parameters. We cannot be sure ifa longer period of time elapsed from the surgery or
whether the complete restoration of body mass to levelssimilar to those of lean control subjects would completely
correct the dysfunction. As observed in experimentalobesity, neuronal apoptosis in the hypothalamus can affect
```
distinct cellular subpopulations, leading to a defective re-sponse to hormonal and nutritional inputs (7). Should
```
a similar phenomenon occur in humans, a complete res-toration of the functional activity may not be achieved.
Nevertheless, the increase in the anti-inflammatory activitydetected in the CSF of obese patients after the loss of body
mass is remarkable. In addition to the well-known anti-inflammatory activity of IL-10, the inhibition of neuronal
```
degeneration through the reduction of apoptosis has beenreported (23). Thus, we can hypothesize that body mass
```
loss or other conditions that increase IL-10 in the brainmay reduce neuronal damage resulting in the restoration
of functionality. Moreover, these findings place IL-10 andperhaps IL-6 as attractive therapeutic agents for obesity, as
```
recently suggested (22).In conclusion, reduction of body mass in obese humans
```
increases the anti-inflammatory activity in the CSF andpartially corrects the dysfunctional activity in response to
glucose in selected brain areas. These data suggest thatobesity and body mass loss affect the human brain in
a manner similar to the animal models for this disease.
ACKNOWLEDGMENTS
This work was supported by grants from the Fundação deAmparo a Pesquisa do Estado de Sao Paulo. The Labora-
tory of Cell Signaling belongs to the Instituto Nacionalde Ciência e Tecnologia–Obesidade e Diabetes. F.R.S.P.,
P.T.F., L.M.L., and F.C. are affiliated with the CooperaçãoInterinstitucional de Apoio a Pesquisas sobre o Cerebro.
No potential conflicts of interest relevant to this articlewere reported.
S.v.d.S.-L. performed patient care and collected clinicaland nutritional data. F.R.S.P. performed neuroimaging
studies. D.E.C. performed patient care and collectedclinical and nutritional data. P.T.F. performed neuroimag-
ing studies. A.R.C. and C.R.G. collected and evaluateddata. E.A.C., J.C.P., and B.G. performed surgery and the
metabolic studies. L.M.L. and F.C. performed neuroimag-ing studies. L.A.V. conceived, organized, and wrote the
article.The authors thank Dr. N. Conran, University of Campi-
nas, for editing the English grammar.
REFERENCES1. Kelly T, Yang W, Chen CS, Reynolds K, He J. Global burden of obesity in
```
2005 and projections to 2030. Int J Obes (Lond) 2008;32:1431–14372. Després JP, Lemieux I. Abdominal obesity and metabolic syndrome.
```
```
Nature 2006;444:881–8873. De Souza CT, Araujo EP, Bordin S, et al. Consumption of a fat-rich diet
```
```
activates a proinflammatory response and induces insulin resistance in thehypothalamus. Endocrinology 2005;146:4192–4199
```
4. Milanski M, Degasperi G, Coope A, et al. Saturated fatty acids produce aninflammatory response predominantly through the activation of TLR4
```
signaling in hypothalamus: implications for the pathogenesis of obesity.J Neurosci 2009;29:359–370
```
5. Velloso LA, Araújo EP, de Souza CT. Diet-induced inflammation of thehypothalamus in obesity. Neuroimmunomodulation 2008;15:189–193
6. Yang L, Hotamisligil GS. Stressing the brain, fattening the body. Cell 2008;135:20–22
```
FIG. 3. Functional connectivity maps. A seed was placed in the hypo-thalamus, and intragroup (A–C) and intergroup (D and E) analyses
```
were performed. A: Connectivity maps of lean subjects are depicted.B: Connectivity maps of obese patients before surgery are depicted.
```
C: Connectivity maps of obese patients after surgery are depicted. D:Intergroup analysis between lean subjects and obese patients before
```
```
surgery (lean 3 BS) is depicted. E: Intergroup analysis between obesepatients before surgery and obese patients after surgery (BS 3 AS) is
```
```
depicted. Color bars represent t values. For intragroup analysis (A–C),hot colors indicate the common level of correlation and cold colors
```
```
indicate the common level of anticorrelation with the time courseprovided by the seed within each group. For intergroup analysis (D and
```
```
E), hot colors indicate the level of differences between two groupstoward lean and obese patients before surgery, respectively, and cold
```
```
colors indicate the level of differences between two groups towardobese patients before and after surgery, respectively. AS, after surgery;
```
```
BS, before surgery; Cb, cerebellum; Hy, hypothalamus; Oc, occipital cor-tex; Of, orbitofrontal cortex; Ss, somatosensory cortex. (A high-quality
```
```
digital representation of this figure is available in the online issue.)
```
S. VAN DE SANDE-LEE AND ASSOCIATES
diabetes.diabetesjournals.org DIABETES, VOL. 60, JUNE 2011 1703
149
7. Moraes JC, Coope A, Morari J, et al. High-fat diet induces apoptosis ofhypothalamic neurons. PLoS ONE 2009;4:e5045
8. Thaler JP, Schwartz MW. Minireview: Inflammation and obesity patho-genesis: the hypothalamus heats up. Endocrinology 2010;151:4109–4115
9. Ozcan L, Ergin AS, Lu A, et al. Endoplasmic reticulum stress plays a cen-tral role in development of leptin resistance. Cell Metab 2009;9:35–51
10. Zhang X, Zhang G, Zhang H, Karin M, Bai H, Cai D. Hypothalamic IKKbeta/NF-kappaB and ER stress link overnutrition to energy imbalance and
```
obesity. Cell 2008;135:61–7311. Gastrointestinal surgery for severe obesity: National Institutes of Health
```
```
Consensus Development Conference Statement. Am J Clin Nutr 1992;55(Suppl.):615S–619S
```
12. de Carvalho CP, Marin DM, de Souza AL, et al. GLP-1 and adiponectin:effect of weight loss after dietary restriction and gastric bypass in morbidly
```
obese patients with normal and abnormal glucose metabolism. Obes Surg2009;19:313–320
```
13. Liu Y, Gao JH, Liu HL, Fox PT. The temporal response of the brain aftereating revealed by functional MRI. Nature 2000;405:1058–1062
14. Pereira FR, Alessio A, Sercheli MS, et al. Asymmetrical hippocampalconnectivity in mesial temporal lobe epilepsy: evidence from resting state
```
fMRI. BMC Neurosci 2010;11:6615. Biswal BB, Van Kylen J, Hyde JS. Simultaneous assessment of flow and
```
```
BOLD signals in resting-state functional connectivity maps. NMR Biomed1997;10:165–170
```
16. Robertson C, Conway R, Dennis B, Yarnell J, Stamler J, Elliott P. Attain-ment of precision in implementation of 24 h dietary recalls: INTERMAP
```
UK. Br J Nutr 2005;94:588–59417. Esposito K, Pontillo A, Di Palo C, et al. Effect of weight loss and lifestyle
```
```
changes on vascular inflammatory markers in obese women: a randomizedtrial. JAMA 2003;289:1799–1804
```
18. Colonnese MT, Phillips MA, Constantine-Paton M, Kaila K, Jasanoff A.Development of hemodynamic responses and functional connectivity in
```
rat somatosensory cortex. Nat Neurosci 2008;11:72–7919. Morton GJ, Cummings DE, Baskin DG, Barsh GS, Schwartz MW. Central
```
```
nervous system control of food intake and body weight. Nature 2006;443:289–295
```
20. Matsuda M, Liu Y, Mahankali S, et al. Altered hypothalamic function inresponse to glucose ingestion in obese humans. Diabetes 1999;48:1801–
180621. Führer D, Zysset S, Stumvoll M. Brain activity in hunger and satiety: an
```
exploratory visually stimulated FMRI study. Obesity (Silver Spring) 2008;16:945–950
```
22. Ropelle ER, Flores MB, Cintra DE, et al. IL-6 and IL-10 anti-inflammatoryactivity links exercise to hypothalamic insulin and leptin sensitivity
```
through IKKbeta and ER stress inhibition. PLoS Biol 2010;8:e100046523. Bachis A, Colangelo AM, Vicini S, et al. Interleukin-10 prevents glutamate-
```
```
mediated cerebellar granule cell death by blocking caspase-3-like activity.J Neurosci 2001;21:3104–3112
```
HYPOTHALAMIC DYSFUNCTION IN HUMAN OBESITY
1704 DIABETES, VOL. 60, JUNE 2011 diabetes.diabetesjournals.org
150151
DISCUSSÃO
152153
Neste trabalho buscou-se o desenvolvimento e o aperfeiçoamento de uma sequência
de experimentos, em ordem crescente dos níveis de dificuldade, para gerar mapas cerebrais e
conectomas diversas condições neurológicas e psiquiátricas. O conjunto de variáveis que
permearam o trabalho pode ser apresentado didaticamente em três categorias distintas, apesar
de estarem interligadas. A primeira, de ordem fisiológica, é representada pelos os processos
cerebrais. As interpretações sobre esses processos têm sido discutidas tanto em escalas
```
microscópicas, da ordem de canais iônicos (Heinzen et al., 2007), de expressões gênicas
```
```
(Kobayashi et al., 2002), ou de componentes metabólicas (Pascual et al., 2008) como também
```
em dimensões macroscópicas a exemplo, de ordem anatômica, em diferentes níveis de
```
substâncias cinzenta (Keller et al., 2002) ou branca (McMillan et al., 2004) e de conexão
```
```
(Bonilha et al., 2004). Na presente tese, os exemplos que foram estudados envolveram o
```
```
processo de envelhecimento normal (Kensinger et al., 2006, Salat et al., 2005, Corkin, 1998),
```
```
de epilepsia medial temporal (Pereira et al., 2010, Alessio et al., 2011), de doença de
```
```
Alzheimer (Balthazar et al., 2013), de transtorno cognitivo leve (Radanovic et al., 2013),
```
```
de pacientes com obesidade mórbida (van de Sande-Lee et al., 2011), de idosos com
```
```
diagnóstico de depressão (Bezerra et al., 2012) e de indivíduos com mutação gênica (Franca
```
```
et al., 2012).
```
Na segunda categoria, de ordem neuropsicológica, residem os processos de funções
cognitivas. A base deste conceito fundamenta-se na representação interna de informações,
```
sejam estas obtidas externamente ou processadas internamente (Gazzaniga et al., 2009). As
```
informações, elevadas à esfera mental, podem gerar, elaborar ou mesmo manipular grupos
de operações mentais como memória, atenção, linguagem entre outras. As interações entre
operações mentais e processos cerebrais compõem um sistema dinâmico de informações
```
denominado sistema funcional complexo (Luria, 1980). Entretanto, as manifestações mentais
```
interdependentes com a matriz cerebral podem ser modeladas apenas se os processos
```
neuronais (como metabolismo ou descargas elétricas), que foram mobilizados pelas funções
```
154
mentais, puderem se detectáveis por instrumentação. Visto que a hegemonia dos processos
```
mentais não possui relação unívoca com determinadas regiões cerebrais (Luria, 1973) (como
```
```
acreditavam os frenologista), associado ao fato de haver uma enorme limitação instrumental e
```
uma prudente orientação ética para se mensurar sinais cerebrais humanos, tem-se que a
modelagem de séries temporais, como fMRI ou EEG, é extremamente limitada. Apesar disso,
as inferências sobre interações e segregações cerebrais podem ser realizadas e comporem
uma nova abordagem da neuropsicologia. Em particular, as funções de memórias verbal e
não-verbal, além das sub-categorias de codificação, evocação e reconhecimento foram
utilizadas como exemplos para motivar a modelagem cerebral durante a realização deste
trabalho.
A terceira categoria, de ordem técnica, caracterizou-se pela modelagem dos
fenômenos cerebrais e mentais. Foram estimados esquemas mais simples que a complexidade
neural biológica utilizando-se de arcabouços estatísticos e matemáticos aplicados a séries
temporais, a exemplos daquelas séries temporais produzidas no imageamento por ressonância
magnética funcional e por aquisições de eletroencefalografia. Ambas as técnicas serviram de
molde para se verificar integração e segregação ao se calcular mapas de conectividade
```
anatômica (Sporns et al., 2005, Van Essen and Ugurbil, 2012), funcional e efetiva (Friston,
```
```
2007).
```
Nos seres humanos, a natureza dual e interpenetrante dos fenômenos mental e
cerebral dificulta uma abordagem individualizada de cada processo. A informação que flui
por estes fenômenos não é completamente mensurável devido tanto à própria natureza do
```
fenômeno biológico (mental e cerebral) como à limitação do instrumental disponível. Deste
```
modo, a estratégia para se extrair conhecimento sobre as redes neurais requer maximização e
combinação de técnicas que observem o comportamento cerebral. No estudo de
conectividade três opções podem ser utilizadas: conectividade anatômica, conectividade
funcional e conectividade efetiva. Os experimentos realizados neste trabalho são discutidos
155
abaixo de acordo com o objetivo de cada experimento. Outros seis trabalhos, publicados
previamente em revistas indexadas e apresentados na sessão de metodologia, têm a discussão
apresentada no corpo do artigo e não são reproduzidos nesta sessão.
SEM aplicado à plasticidade etária e codificação verbal
O protocolo desenvolvido neste experimento objetivou a detecção da conectividade
efetiva entre amídala e hipocampo ipsilaterais e em ambos os sentidos durante a codificação
de palavras com conteúdo emocional. Os indivíduos que participaram deste estudo foram
apenas sujeitos sadios cuja distinção foi marcada apenas pela faixa etária em que se
encontravam, formando dois grupos, o de jovens e o de adultos mais velhos. A técnica
empregada para se estimar a ecMRI foi a SEM que, como descrita anteriormente, pode
apenas estabelecer relações estáticas de um modelo anatômico. A combinação de SEM com
```
indivíduos pertencente à mesma classe (controles), cuja única variação é a diferença etária,
```
revela o comportamento plástico existente entre estes grupos durante a realização da mesma
tarefa. A interpretação dos resultados deste estudo deve ser fixada nas relações intrínsecas
entre as estruturas cerebrais presentes no modelo anatômico. Buscou-se aqui não o
entendimento de um comportamento neural dinâmico, que varia com uma determinada tarefa,
mas sim, como essa tarefa, no caso a de codificação verbal de palavras abstratas e concretas e
com conteúdo emocional, varia com a idade dos indivíduos separados em dois grupos.
Em ambos os grupos, a influência das amídalas sobre os hipocampos foi maior do que
na direção oposta, sugerindo que a tarefa efetivamente apresentava conteúdo emocional. No
grupo de adultos mais velhos, os parâmetros de conectividade efetiva estavam mais intensos
no lado direito que no lado esquerdo. Este padrão não foi encontrado no grupo de jovens. Ao
se correlacionar este achado com o desempenho dos grupos, pode-se suportar a hipótese de
que os adultos mais velhos realizem processos distintos dos jovem e que tal performance
156
pode estar associado às diferentes estratégias escolhidas por cada grupo.
Além disso, a influência da amídala sobre o hipocampo é maior do lado esquerdo nos
jovens, enquanto que para os adultos mais velhos, esta influência é maior do lado direito.
Esta diferença sugere haver mudanças na conectividade efetiva em função da idade, dado que
a tarefa verbal se encontra majoritariamente lateralizada à esquerda. Pode-se supor portanto
uma mudança de estratégia para se realizar a codificação como obtenção de estratégias não-
verbais para realizar uma atividade eminentemente verbal.
Por fim, a influência de ambos hipocampos nas amídalas ipsilaterais são equivalentes
para os jovens, enquanto que nos adultos mais velhos há uma predominância da influência
exercida à direita. Considerando os achados anteriores, este dado fortalece a hipótese de que
os hipocampos nos mais velhos exercem menor influência sobre as amídalas do que nos
jovens durante a realizada da tarefa de codificação verbal.
SEM aplicado a ELTM esquerdo com codificação verbal
Objetivou-se neste experimento estimar os parâmetros de conectividade efetiva entre
regiões frontais e mediais temporais durante a codificação de palavras abstratas e neutras.
Diferentemente do experimento anterior, os indivíduos que participaram deste estudo foram
sujeitos controles e indivíduos portadores de ELTM esquerda contudo, a técnica empregada
para se estimar a ecMRI foi a mesma, a SEM. Buscou-se aqui compreender a plasticidade
cerebral, em forma de conectividade efetiva, durante a realização de uma determinada tarefa,
não em função da idade dos sujeitos mas em detrimento de uma condição neurológica, no
caso, ELTM esquerda. A interpretação dos resultados dá-se em termos das relações
intrínsecas entre as estruturas cerebrais do modelo anatômico desse experimento.
A influência do hipocampo esquerdo sobre o parahipocampo ipsilateral mostrou-se
significativamente maior para os controles que para os pacientes. O achado sugere que,
157
durante a codificação, há uma maior sincronia dessas estruturas mediais nos controles que
nos pacientes. Essa hipótese é reforçada pelos dados de conectividade funcional.
Semelhantemente, observou-se a redução da influência entre as porções triangular e opercular
do giro frontal inferior para o giro frontal médio, quando comparados controles e pacientes.
Por fim, a influência da região medial temporal sobre a região frontal também se apresentou
reduzida nos pacientes.
A generalizada redução da intensidade dos parâmetros de conectividade efetiva, entre
as regiões frontais e mediais temporais, nos pacientes com ELTM esquerda, sugere que a
plasticidade neural, causada pela condição neurológica nestes indivíduos, deve tornar distinta
a função de codificação verbal, entretanto, com este modelo e técnica não se pode avaliar se a
extensão do dano funcional estende-se ao lobo frontal, uma vez que o fluxo da informação já
está comprometido em sua origem, ou seja, entre hipocampo e parahipocampo.
DCM aplicado a ELTM unilateral com codificação verbal
O experimento desenhado com DCM buscou estimar os parâmetros de conectividade
efetiva de regiões cerebrais envolvidas no processamento de memória verbal, durante a
codificação de palavras abstratas e neutras. Semelhantemente ao experimento anterior, foram
```
selecionadas regiões mediais temporais (hipocampo) e frontais (região dorsolateral do córtex
```
```
pré-frontal) contudo, outras áreas foram acrescidas no modelo anatômico, como visual
```
primária e a porção caudal do giro temporal superior para simular o fluxo da informação
verbal. A importante vantagem do DCM consiste no fato de que os parâmetros de
conectividade efetiva, associados ao caráter modulatório da tarefa realizada, podem ser
estimados a partir das séries temporais, para isso, utilizou-se fMRI de sujeitos controles e
```
indivíduos portadores de ELTM unilateral (esquerda e direita) durante a codificação de
```
palavras abstratas.
158
A interpretação dos resultados dá-se nos termos das relações intrínsecas entre as
estruturas cerebrais do modelo anatômico sugerido. Deve-se ressaltar, entretanto, que a tarefa
de codificação verbal foi capaz de modular a interação entre o córtex occipital primário e
hipocampo esquerdo para os controles mas não para os pacientes, sejam estes com atrofia
hipocampal à esquerda ou à direita. Semelhante modulação também foi observada na
influência que o hipocampo esquerdo exerce sobre a área de Wernick. Os indivíduos
controles apresentaram valores significativamente distintos quando comparado com os
pacientes. Além dos parâmetros modulatórios que diferenciam controles de pacientes, os
parâmetros intrínsecos também apresentam significativa diferenciação. Ressalta-se que as
influências do córtex occipital primário sobre o hipocampo esquerdo e do hipocampo
esquerdo sobre a área de Wernick e sobre a porção dorsolateral do córtex pré-frontal são bem
mais evidentes nos controles que nos pacientes.
O conjunto de achados sugere que, não obstante ao fato de que os pacientes com
```
ELTM direita não apresentarem lesão estrutural no hipocampo esquerdo (perceptível pela
```
```
MRI), deve haver comprometimento funcional ou rearranjo plástico na realização da tarefa.
```
Em contra posição, os indivíduos com ELTM esquerda, dado o comprometimento estrutural
locado no hipocampo esquerdo, devem apresentar comprometimento funcional e,
consequentemente, menores parâmetros de conectividade efetiva durante a codificação
verbal.
Enquanto o desempenho verbal de indivíduos com ELTM esquerda tem se mostrado
inferior à dos controles, desempenho de pacientes com ELTM direita apresenta índices
semelhantes aos indivíduos controles. Pode-se supor que a plasticidade ocorrida nos
pacientes com ELTM direita foi eficiente enquanto o mesmo não ocorreu com os indivíduos
com ELTM esquerda. Tal fato sugere que as estruturas mediais temporais do hemisfério
dominante para linguagem possam estar envolvidas diretamente no processo de plasticidade
para realização da tarefa de codificação verbal.
159
CONSIDERAÇÕES FINAIS
160161
O estudo do conectoma humano por imageamento de ressonância magnética nuclear
mostrou-se sensível para detectar diferenças na organização entre regiões cerebrais, tanto em
sujeitos sadios como em pacientes com condições neuropsiquiátricas diversas. No presente
trabalho, buscou-se observar plasticidade cérebro-mental em pacientes com mutações gênicas
```
(SPG11), depressão, epilepsia, obesidade mórbida, doença de Alzheimer, déficit cognitivo
```
leve, envelhecimento saudável.
Indivíduos com mutação no gene SPG11 apresentaram diferença significava nos
níveis de acMRI, em especial RD e FA. Com esse estudo, concluiu-se que pacientes com
mutação em SPG11 apresentaram dano neuronal muito mais difuso e extenso do que se
previa. Em oposição a esses achados, idosos com diagnóstico de depressivos quando
comparados a sujeitos controles não mostraram diferenças significativas em FA. Hipotetiza-
se que tal índice não seja robusto para detectar alterações neuro-estruturais mais sutis
indicando a necessidade de se evoluir no desenvolvimento de novos índices de anisotropia
que possam detectar tais alterações, como geometrias toroidais e superquadráticas.
Em idosos saudáveis observou-se significativa alteração dos níveis de ecMRI
```
(comparados a jovens saudáveis) durante a codificação de palavras com conteúdo emocional
```
indicando que a plasticidade funcional está presente no envelhecimento. Pacientes com
epilepsia também apresentaram significativas diferenças nas comparações dos grupos de
pacientes com ELTM-esquerda, ELTM-direita e sujeitos controles seja durante a codificação
de memória verbal, visual e em estado de repouso. Tais indicadores são potenciais
biomarcadores da ELTM unilateral.
Pacientes com doença de Alzheimer apresentaram a rede de modo padrão distinta dos
sujeitos controles além de terem elevada correlação da rede saliente com parâmetros
neuropsicológicos de agitação. Essa observação, obtida com fcMRI, indica a potencialidade
de uso clínicos e de diagnóstico. O mesmo se observou com pacientes portadores de
obesidade mórbida e a parcial reversibilidade de quadro inflamatório acompanhado de
162
alterações nas redes neurais desses paciente após intervenção de cirurgia bariátrica.
Diante das diversas condições neurológicas que foram exploradas pela técnicas de
conectividade, pode-se concluir que a estimativa do conectoma humano representa uma
potente ferramenta no entendimento da dinâmica cerebral normal e patológica sendo que, no
presente trabalhos, pretendeu-se demonstrar a integração dessa metodologia com estudos que
vão desde a genética até a neuropsicologia. A característica multimodal e multiescalar de
estudos do conectoma revela as potencialidades da técnica no campo das neurociências.
163
REFERÊNCIA BIBLIOGRÁFICA
164165
ABBOTT, D. F., WAITES, A. B., LILLYWHITE, L. M. & JACKSON, G. D. 2010. fMRI
assessment of language lateralization: an objective approach. Neuroimage, 50, 1446-
55.
AERTSEN, A., VAADIA, E., ABELES, M., AHISSAR, E., BERGMAN, H., KARMON, B.,
LAVNER, Y., MARGALIT, E., NELKEN, I. & ROTTER, S. 1991. Neural
interactions in the frontal cortex of a behaving monkey: signs of dependence on
stimulus context and behavioral state. J Hirnforsch, 32, 735-43.
ALESSIO, A., PEREIRA, F. R., SERCHELI, M. S., RONDINA, J. M., OZELO, H. B.,
BILEVICIUS, E., PEDRO, T., COVOLAN, R. J., DAMASCENO, B. P. &
CENDES, F. 2011. Brain plasticity for verbal and visual memories in patients
with mesial temporal lobe epilepsy and hippocampal sclerosis: An fMRI study.
Hum Brain Mapp.
ASTOLFI, L., CINCOTTI, F., MATTIA, D., SALINARI, S., BABILONI, C., BASILISCO,
A., ROSSINI, P. M., DING, L., NI, Y., HE, B., MARCIANI, M. G. & BABILONI, F.
2004. Estimation of the effective and functional human cortical connectivity with
structural equation modeling and directed transfer function applied to high-resolution
EEG. Magn Reson Imaging, 22, 1457-70.
BALTHAZAR, M. L., PEREIRA, F. R., LOPES, T. M., DA SILVA, E. L., COAN, A.
C., CAMPOS, B. M., DUNCAN, N. W., STELLA, F., NORTHOFF, G.,
DAMASCENO, B. P. & CENDES, F. 2013. Neuropsychiatric symptoms in
Alzheimer's disease are related to functional connectivity alterations in the
salience network. Hum Brain Mapp.
BASSER, P. J., MATTIELLO, J. & LEBIHAN, D. 1994. MR diffusion tensor spectroscopy
and imaging. Biophys J, 66, 259-67.
BECK, A. T. 1979. Cognitive therapy of depression, New York, Guilford Press.
166
BEZERRA, D. M., PEREIRA, F. R., CENDES, F., JACKOWSKI, M. P., NAKANO, E.
Y., MOSCOSO, M. A., RIBEIZ, S. R., AVILA, R., CASTRO, C. C. &
BOTTINO, C. M. 2012. DTI voxelwise analysis did not differentiate older
depressed patients from older subjects without depression. J Psychiatr Res, 46,
1643-9.
BONILHA, L., RORDEN, C., CASTELLANO, G., PEREIRA, F., RIO, P. A., CENDES,
F. & LI, L. M. 2004. Voxel-based morphometry reveals gray matter network
atrophy in refractory medial temporal lobe epilepsy. Arch Neurol, 61, 1379-84.
```
BRADLEY, M. M. & LANG, P. J. 1999. Affective norms for English words (ANEW):
```
Instruction manual and affective rating, Gainesville, FL, Center for Research in
Psychophysiology.
BUCHEL, C. & FRISTON, K. J. 1997. Modulation of connectivity in visual pathways by
```
attention: cortical interactions evaluated with structural equation modelling and fMRI.
```
Cereb Cortex, 7, 768-78.
BUCHEL, C. & FRISTON, K. J. 1998. Dynamic changes in effective connectivity
characterized by variable parameter regression and Kalman filtering. Hum Brain
Mapp, 6, 403-8.
CARMACK, P. S., SPENCE, J., GUNST, R. F., SCHUCANY, W. R., WOODWARD, W. A.
& HALEY, R. W. 2004. Improved agreement between Talairach and MNI coordinate
spaces in deep brain regions. Neuroimage, 22, 367-71.
CHAIGNEAU, E., TIRET, P., LECOQ, J., DUCROS, M., KNOPFEL, T. & CHARPAK, S.
2007. The relationship between blood flow and neuronal activity in the rodent
olfactory bulb. Journal of Neuroscience, 27, 6452-6460.
CHEN, B. & HSU, E. W. 2005. Noise removal in magnetic resonance diffusion tensor
imaging. Magn Reson Med, 54, 393-401.
167
CORDES, D., HAUGHTON, V. M., ARFANAKIS, K., CAREW, J. D., TURSKI, P. A.,
MORITZ, C. H., QUIGLEY, M. A. & MEYERAND, M. E. 2001. Frequencies
contributing to functional connectivity in the cerebral cortex in "resting-state" data.
AJNR Am J Neuroradiol, 22, 1326-33.
CORKIN, S. 1998. Functional MRI for studying episodic memory in aging and Alzheimer's
disease. Geriatrics, 53 Suppl 1, S13-5.
DAS, A. & GILBERT, C. D. 1995. Long-range horizontal connections and their role in
cortical reorganization revealed by optical recording of cat primary visual cortex.
Nature, 375, 780-4.
DELLA-JUSTINA, H. M., PASTORELLO, B. F., SANTOS-PONTELLI, T. E., PONTES-
NETO, O. M., SANTOS, A. C., BAFFA, O., COLAFEMINA, J. F., LEITE, J. P. &
DE ARAUJO, D. B. 2008. Human variability of fMRI brain activation in response to
oculomotor stimuli. Brain Topogr, 20, 113-21.
DESKAN, R. S., SEGONNE, F., FISCHL, B., QUINN, B. T., DICKERSON, B. C.,
BLACKER, D., BUCKNER, R. L., DALE, A. M., MAGUIRE, R. P., HYMAN, B.
T., ALBERT, M. S. & KILLIANY, R. J. 2006. An automated labeling system for
subdividing the human cerebral cortex on MRI scans into gyral based regions of
interest. Neuroimage, 31, 968-980.
DUPONT, S., VAN DE MOORTELE, P. F., SAMSON, S., HASBOUN, D., POLINE, J. B.,
ADAM, C., LEHERICY, S., LE BIHAN, D., SAMSON, Y. & BAULAC, M. 2000.
```
Episodic memory in left temporal lobe epilepsy: a functional MRI study. Brain, 123 (
```
```
Pt 8), 1722-32.
```
ENGEL, S. A., RUMELHART, D. E., WANDELL, B. A., LEE, A. T., GLOVER, G. H.,
CHICHILNISKY, E. J. & SHADLEN, M. N. 1994. fMRI of human visual cortex.
Nature, 369, 525.
168
FELDMAN, R. P. & GOODRICH, J. T. 1999. The Edwin Smith Surgical Papyrus. Childs
Nerv Syst, 15, 281-4.
FINGELKURTS, A. A. & KAHKONEN, S. 2005. Functional connectivity in the brain--is it
an elusive concept? Neurosci Biobehav Rev, 28, 827-36.
FISCHL, B., RAJENDRAN, N., BUSA, E., AUGUSTINACK, J., HINDS, O., YEO, B. T.,
MOHLBERG, H., AMUNTS, K. & ZILLES, K. 2008. Cortical folding patterns and
predicting cytoarchitecture. Cereb Cortex, 18, 1973-80.
FISCHL, B., SALAT, D. H., BUSA, E., ALBERT, M., DIETERICH, M., HASELGROVE,
C., VAN DER KOUWE, A., KILLIANY, R., KENNEDY, D., KLAVENESS, S.,
MONTILLO, A., MAKRIS, N., ROSEN, B. & DALE, A. M. 2002. Whole brain
```
segmentation: automated labeling of neuroanatomical structures in the human brain.
```
Neuron, 33, 341-55.
FISCHL, B., VAN DER KOUWE, A., DESTRIEUX, C., HALGREN, E., SEGONNE, F.,
SALAT, D. H., BUSA, E., SEIDMAN, L. J., GOLDSTEIN, J., KENNEDY, D.,
CAVINESS, V., MAKRIS, N., ROSEN, B. & DALE, A. M. 2004. Automatically
parcellating the human cerebral cortex. Cereb Cortex, 14, 11-22.
FRANCA, M. C., JR., YASUDA, C. L., PEREIRA, F. R., D'ABREU, A., LOPES-
RAMOS, C. M., ROSA, M. V., CENDES, F. & LOPES-CENDES, I. 2012. White
and grey matter abnormalities in patients with SPG11 mutations. J Neurol
Neurosurg Psychiatry.
FRISTON, K. 1994. Functional and effective connectivity in neuroimaging: A synthesis.
Human Brain Mapping, 2, 56-78.
FRISTON, K. J. 2007. Statistical parametric mapping : the analysis of funtional brain images,
```
Amsterdam ; Boston, Elsevier/Academic Press.
```
169
FRISTON, K. J. & BUCHEL, C. 2000. Attentional modulation of effective connectivity from
V2 to V5/MT in humans. Proc Natl Acad Sci U S A, 97, 7591-6.
FRISTON, K. J., FRITH, C. D. & FRACKOWIAK, R. S. J. 1993a. Time-dependent changes
in effective connectivity measured with PET. Human Brain Mapping, 1, 69-79.
FRISTON, K. J., FRITH, C. D., LIDDLE, P. F. & FRACKOWIAK, R. S. 1993b. Functional
```
connectivity: the principal-component analysis of large (PET) data sets. J Cereb
```
Blood Flow Metab, 13, 5-14.
FRISTON, K. J., HARRISON, L. & PENNY, W. 2003. Dynamic causal modelling.
Neuroimage, 19, 1273-302.
FROST, J. J. 2003. Molecular imaging of the brain: a historical perspective. Neuroimaging
Clin N Am, 13, 653-8.
GALLAGHER, M. & CHIBA, A. A. 1996. The amygdala and emotion. Curr Opin
Neurobiol, 6, 221-7.
GARBADE, K. 1977. Two Methods for Examining the Stability of Regression Coefficients.
Journal of the American Statistical Association, 72, 54-63.
GAZZANIGA, M. S., IVRY, R. B. & MANGUN, G. R. 2009. Cognitive neuroscience : the
biology of the mind, New York, Norton.
GLIELMI, C. B., SCHUCHARD, R. A. & HU, X. P. 2009. Estimating Cerebral Blood
Volume With Expanded Vascular Space Occupancy Slice Coverage. Magnetic
Resonance in Medicine, 61, 1193-1200.
GOELMAN, G. 2004. Radial correlation contrast--a functional connectivity MRI contrast to
map changes in local neuronal communication. Neuroimage, 23, 1432-9.
170
GREENE, J. D., SOMMERVILLE, R. B., NYSTROM, L. E., DARLEY, J. M. & COHEN, J.
D. 2001. An fMRI investigation of emotional engagement in moral judgment.
Science, 293, 2105-8.
HEINZEN, E. L., YOON, W., WEALE, M. E., SEN, A., WOOD, N. W., BURKE, J. R.,
WELSH-BOHMER, K. A., HULETTE, C. M., SISODIYA, S. M. & GOLDSTEIN,
D. B. 2007. Alternative ion channel splicing in mesial temporal lobe epilepsy and
Alzheimer's disease. Genome Biol, 8, R32.
HERMAN, P., SANGANAHALLI, B. G., BLUMENFELD, H. & HYDER, F. 2009.
Cerebral oxygen demand for short-lived and steady-state events. J Neurochem, 109
Suppl 1, 73-9.
HORWITZ, B. 2003. The elusive concept of brain connectivity. Neuroimage, 19, 466-70.
HYDE, P. S. & KNUDSEN, E. I. 2002. The optic tectum controls visually guided adaptive
plasticity in the owl's auditory space map. Nature, 415, 73-6.
ILAE 1989. Proposal for revised classification of epilepsies and epileptic syndromes.
Commission on Classification and Terminology of the International League Against
Epilepsy. Epilepsia, 30, 389-99.
KALMAN, R. E. 1960. A New Approach to Linear Filtering and Prediction Problems.
Transactions of the ASME ‚Äì Journal of Basic Engineering, 35-45.
KELLER, S. S., WIESHMANN, U. C., MACKAY, C. E., DENBY, C. E., WEBB, J. &
ROBERTS, N. 2002. Voxel based morphometry of grey matter abnormalities in
patients with medically intractable temporal lobe epilepsy: effects of side of seizure
onset and epilepsy duration. J Neurol Neurosurg Psychiatry, 73, 648-55.
KENDALL, M. G. & GIBBONS, J. D. 1990. Rank correlation methods, London
```
New York, NY, E. Arnold ;
```
171
Oxford University Press.
KENSINGER, E. A., KRENDL, A. C. & CORKIN, S. 2006. Memories of an emotional and
a nonemotional event: effects of aging and delay interval. Exp Aging Res, 32, 23-45.
KOBAYASHI, E., FACCHIN, D., STEINER, C. E., LEONE, A. A., CAMPOS, N. L.,
CENDES, F. & LOPES-CENDES, I. 2002. Mesial temporal lobe abnormalities in a
family with 15q26qter trisomy. Arch Neurol, 59, 1476-9.
KRUGER, G. & GLOVER, G. H. 2001. Physiological noise in oxygenation-sensitive
magnetic resonance imaging. Magn Reson Med, 46, 631-7.
LE BIHAN, D., BRETON, E., LALLEMAND, D., GRENIER, P., CABANIS, E. & LAVAL-
JEANTET, M. 1986. MR imaging of intravoxel incoherent motions: application to
diffusion and perfusion in neurologic disorders. Radiology, 161, 401-7.
LOGOTHETIS, N. K., PAULS, J., AUGATH, M., TRINATH, T. & OELTERMANN, A.
2001. Neurophysiological investigation of the basis of the fMRI signal. Nature, 412,
150-7.
```
LURIA, A. R. 1973. The working brain; an introduction to neuropsychology. Translated by
```
Basil Haigh, London,, Allen Lane.
LURIA, A. R. 1980. Higher cortical functions in man, New York, Basic Books.
MCCOLL, R. M., CLARKE, G. D. & PESHOCK, R. M. 1992. Echo-Planar Imaging -
Image-Reconstruction from K-Space Trajectories. Radiology, 185, 253-253.
MCINTOSH, A. R. & GONZALEZ-LIMA, F. 1994. Structural equation modeling and its
application to network analysis in functional brain imaging. Human Brain Mapping,
2, 2-22.
MCMILLAN, A. B., HERMANN, B. P., JOHNSON, S. C., HANSEN, R. R.,
SEIDENBERG, M. & MEYERAND, M. E. 2004. Voxel-based morphometry of
172
unilateral temporal lobe epilepsy reveals abnormalities in cerebral white matter.
Neuroimage, 23, 167-74.
MINAGAR, A., RAGHEB, J. & KELLEY, R. E. 2003. The Edwin Smith surgical papyrus:
description and analysis of the earliest case of aphasia. J Med Biogr, 11, 114-7.
OGAWA, S., LEE, T. M., KAY, A. R. & TANK, D. W. 1990. Brain magnetic resonance
imaging with contrast dependent on blood oxygenation. Proc Natl Acad Sci U S A,
87, 9868-72.
OLDFIELD, R. C. 1971. The assessment and analysis of handedness: the Edinburgh
inventory. Neuropsychologia, 9, 97-113.
PASCUAL, J. M., CAMPISTOL, J. & GIL-NAGEL, A. 2008. Epilepsy in inherited
metabolic disorders. Neurologist, 14, S2-S14.
PAULING, L. 1977. Magnetic properties and structure of oxyhemoglobin. Proc Natl Acad
Sci U S A, 74, 2612-3.
PAULING, L. & CORYELL, C. D. 1936. The Magnetic Properties and Structure of
Hemoglobin, Oxyhemoglobin and Carbonmonoxyhemoglobin. Proc Natl Acad Sci U
S A, 22, 210-6.
PAULSON, O. B., HASSELBALCH, S. G., ROSTRUP, E., KNUDSEN, G. M. &
PELLIGRINO, D. 2010. Cerebral blood flow response to functional activation. J
Cereb Blood Flow Metab, 30, 2-14.
PEREIRA, F. R., ALESSIO, A., SERCHELI, M. S., PEDRO, T., BILEVICIUS, E.,
RONDINA, J. M., OZELO, H. F., CASTELLANO, G., COVOLAN, R. J.,
DAMASCENO, B. P. & CENDES, F. 2010. Asymmetrical hippocampal
connectivity in mesial temporal lobe epilepsy: evidence from resting state fMRI.
BMC Neurosci, 11, 66.
173
PEREIRA, F. R. S. 2011. Conectividade funcional por imageamento de ressonância
```
magnética (MRI) em pacientes com epilepsia de lobo temporal mesial. Mestre em
```
Ciências Médicas - Ciências Biomédicas, Universidade Estadual de Campinas.
RADANOVIC, M., PEREIRA, F. R., STELLA, F., APRAHAMIAN, I., FERREIRA, L.
K., FORLENZA, O. V. & BUSATTO, G. F. 2013. White matter abnormalities
associated with Alzheimer's disease and mild cognitive impairment: a critical
review of MRI studies. Expert Rev Neurother, 13, 483-93.
RAYENS, W. S. & ANDERSEN, A. H. 2006. Multivariate analysis of fMRI data by oriented
partial least squares. Magn Reson Imaging, 24, 953-8.
RIDGE, R. M. & BETZ, W. J. 1984. The effect of selective, chronic stimulation on motor
unit size in developing rat muscle. J Neurosci, 4, 2614-20.
RODER, B., STOCK, O., BIEN, S., NEVILLE, H. & ROSLER, F. 2002. Speech processing
activates visual cortex in congenitally blind humans. Eur J Neurosci, 16, 930-6.
SALAT, D. H., TUCH, D. S., GREVE, D. N., VAN DER KOUWE, A. J., HEVELONE, N.
D., ZALETA, A. K., ROSEN, B. R., FISCHL, B., CORKIN, S., ROSAS, H. D. &
DALE, A. M. 2005. Age-related alterations in white matter microstructure measured
by diffusion tensor imaging. Neurobiol Aging, 26, 1215-27.
SAVICKI, J. P., LANG, G. & IKEDA-SAITO, M. 1984. Magnetic susceptibility of oxy- and
carbonmonoxyhemoglobins. Proc Natl Acad Sci U S A, 81, 5417-9.
SHEIKH, J. I., YESAVAGE, J. A., BROOKS, J. O., 3RD, FRIEDMAN, L., GRATZINGER,
P., HILL, R. D., ZADEIK, A. & CROOK, T. 1991. Proposed factor structure of the
Geriatric Depression Scale. Int Psychogeriatr, 3, 23-8.
SINGH, M., AL-DAYEH, L., PATEL, P., KIM, T., GUCLU, C. & NALCIOGLU, O. 1998.
Correction for head movements in multi-slice EPI functional MRI. Ieee Transactions
on Nuclear Science, 45, 2162-2167.
174
SPORNS, O., TONONI, G. & KOTTER, R. 2005. The human connectome: A structural
description of the human brain. PLoS Comput Biol, 1, e42.
TZOURIO-MAZOYER, N., LANDEAU, B., PAPATHANASSIOU, D., CRIVELLO, F.,
ETARD, O., DELCROIX, N., MAZOYER, B. & JOLIOT, M. 2002. Automated
anatomical labeling of activations in SPM using a macroscopic anatomical
parcellation of the MNI MRI single-subject brain. Neuroimage, 15, 273-89.
VAN DE SANDE-LEE, S., PEREIRA, F. R., CINTRA, D. E., FERNANDES, P. T.,
CARDOSO, A. R., GARLIPP, C. R., CHAIM, E. A., PAREJA, J. C.,
GELONEZE, B., LI, L. M., CENDES, F. & VELLOSO, L. A. 2011. Partial
reversibility of hypothalamic dysfunction and changes in brain activity after
body mass reduction in obese subjects. Diabetes, 60, 1699-704.
VAN ESSEN, D. C. & UGURBIL, K. 2012. The future of the human connectome.
Neuroimage, 62, 1299-310.
VAN OOYEN, A. 2001. Competition in the development of nerve connections: a review of
models. Network, 12, R1-47.
WALDVOGEL, D., VAN GELDEREN, P., IMMISCH, I., PFEIFFER, C. & HALLETT, M.
2000. The variability of serial fMRI data: correlation between a visual and a motor
task. Neuroreport, 11, 3843-7.
WANG, Z., WANG, J., CALHOUN, V., RAO, H., DETRE, J. A. & CHILDRESS, A. R.
2006. Strategies for reducing large fMRI data sets for independent component
analysis. Magn Reson Imaging, 24, 591-6.
WEBSTER, M. J., UNGERLEIDER, L. G. & BACHEVALIER, J. 1995. Development and
plasticity of the neural circuitry underlying visual recognition memory. Can J Physiol
Pharmacol, 73, 1364-71.
175
WIESER, H. G. 2004. ILAE Commission Report. Mesial temporal lobe epilepsy with
hippocampal sclerosis. Epilepsia, 45, 695-714.
YESAVAGE, J. A., BRINK, T. L., ROSE, T. L., LUM, O., HUANG, V., ADEY, M. &
LEIRER, V. O. 1983. Development and Validation of a Geriatric Depression
Screening Scale - a Preliminary-Report. Journal of Psychiatric Research, 17, 37-49.
ZBOROWSKI, M., OSTERA, G. R., MOORE, L. R., MILLIRON, S., CHALMERS, J. J. &
SCHECHTER, A. N. 2003. Red blood cell magnetophoresis. Biophys J, 84, 2638-45.
ZHAO, X., GLAHN, D., TAN, L. H., LI, N., XIONG, J. & GAO, J. H. 2004. Comparison of
TCA and ICA techniques in fMRI data processing. J Magn Reson Imaging, 19, 397-
402.