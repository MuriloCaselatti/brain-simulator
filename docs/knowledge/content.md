


Departamento de Física


## PROCESSAMENTO DE DADOS EM
## AQUISIÇÃO SIMULTÂNEA DE EEG / IFRM





## Miguel Vasco Rodrigues Gonçalves


Dissertação  apresentada  na  Faculdade  de  Ciências  e
Tecnologia da   Universidade   Nova   de   Lisboa   para
obtenção do Grau de Mestre em Engenharia Biomédica

## Orientador: Prof. Doutor Mário Forjaz Secca



## LISBOA
## 2009











“A mente que se abre a uma nova ideia
jamais voltará ao seu tamanho original”
## Albert Einstein


iii

## A GR A DE C I M E N T O S

Gostaria de agradecer, em primeiro lugar, ao meu orientador, o Prof. Doutor Mário Secca,
pela disponibilidade e relevância de objectivos propostos, e ao Dr. Alberto Leal pelo trabalho
realizado enquanto neurofisiologista, e a ambos pela oportunidade de realizar este interessante
projecto.
Gostaria  também  de  expressar  o  meu  agradecimento  à  clínica  de  Ressonância  Magnética
de  Caselas  pela  disponibilização  dos  exames  clínicos  efectuados  aos  pacientes  em  estudo
neste projecto.
Um  muito  obrigado  ao  apoio  técnico  do  BrainVoyager
## TM
,  cujos  esclarecimentos  foram
absolutamente determinantes na conclusão dos objectivos pretendidos.
Aos meus amigos e aos  meus colegas de laboratório pelo companheirismo e discussão de
ideias, os meus sinceros agradecimentos.
À  minha  família  e àqueles que, sem o serem, os considero, porque família “é quem está
junto de nós”, pelo entusiasmo partilhado na conclusão deste projecto e do mestrado.
A  ti,  pelo  teu  apoio,  especialmente  nas  alturas  mais  críticas,  e  por  me  acompanhares  ao
longo  deste  processo,  muitas  vezes  sacrificando  a  tua  própria  vontade  para  que  eu  pudesse
alcançar um melhor resultado. Obrigado!


iv

## R E S UM O

No contexto da epilepsia, torna-se necessária a localização precisa do foco epiléptico com
o  objectivo  da  sua  remoção  cirúrgica  em  pacientes  cuja  medicação  não  é  uma  opção  eficaz.
Neste sentido,   a   aquisição   simultânea   de electroencefalograma/imagem   funcional   por
ressonância  magnética  (EEG/IfRM)  durante  a  actividade  epileptiforme  interictal  promete  ser
uma  opção  eficaz,  na  medida  em  que  associa  a  elevada  resolução  temporal  do  EEG  à  boa
resolução  espacial  da  IfRM.  Este  projecto  de  investigação  tem os  objectivos  de  avaliar  a
ocorrência  e  significância  de  alterações  positivas  (activações)  e  negativas  (desactivações)  no
sinal  de  contraste  dependente  do  nível  de  oxigenação  sanguínea  (BOLD) relacionadas  com
descargas epilépticas, bem como de observar a relação entre diferentes sequências funcionais
do  mesmo  paciente segundo  duas  abordagens:  a  primeira com respeito  ao  tipo e localização
das respostas e a segunda com respeito à determinação das mesmas segundo uma perspectiva
de   integração   global.   Foram   estudados seis pacientes   com   diagnóstico   de   epilepsia.
Recorrendo  ao programa BrainVoyager
## TM
, foram criados, para cada sequência, quatro mapas
estatísticos diferentes, em que o atraso entre a função de resposta hemodinâmica e a activação
é de 3, 5, 7 ou 9 segundos, tendo sido obtidas respostas BOLD significantes (푝<0.05, com
clusters de  5 voxeis contíguos). A análise dos resultados tem por base a utilização de uma
técnica relativamente recente, em que toda a informação tridimensional anatómica e funcional
do  cérebro é  projectada  numa  representação  plana  do mesmo. O  grau  de  correlação  obtido
entre  o  modelo  adoptado e  o  sinal  dos  exames  funcionais não foi elevado,  verificando-se
também que  as  regiões  cerebrais  que  evidenciam  activação/desactivação  sofrem  grande
variabilidade entre sequências do mesmo paciente. Foi ainda observado que zonas de resposta
BOLD  condizentes entre  sequências  não  implicam  necessariamente  elevada  significância.
Estes resultados permitem concluir que, embora  esta seja uma técnica com grande potencial,
os   mecanismos   que    estão   subjacentes    aos   fenómenos   observados   ainda   não   são
completamente compreendidos, pelo que actualmente é utilizada apenas no sentido de indicar
zonas prováveis para posterior investigação.


Palavras-chave: descargas epilépticas; EEG/IfRM; resposta BOLD; activação; desactivação.





v

## A B S TR A C T

In the context of epilepsy, it becomes necessary the precise location of the epileptic focus,
as  the  surgical  intervention  for  its  removal  is  the  only  option  for  those  patients  whose
medication     is     not     an     effective     option. With     this     in     mind,     simultaneous
electroencephalogram/functional  magnetic resonance  imaging (EEG/fMRI) during  interictal
epileptiform  discharges  promises  to  be  an  efficient  choice,  as  it  associates  high  temporal
resolution of EEG with good IfRM spatial resolution. This investigation project was intended
to evaluate the occurrence and significance of positive (activation) and negative (deactivation)
changes   in   the   blood  oxygenation   level-dependent   (BOLD)   signal   related   to   epileptic
discharges,  as  well  as  to  observe  the  relationship  between  different  functional runs of  the
same patient following two approaches: the first concerning the type and location of responses
and the second respecting the determination of those responses according a global integration
view. Six patients who  had  a  diagnosis  of  epilepsy  were  studied. Four different  statistical
maps  were  created  for  each run, using  the BrainVoyager
## TM
software, in  which  the delay
between the hemodynamic  response  function and  the  activation  is 3, 5,  7 or 9  seconds,
resulting  in  significant  (푝<0.05,  with clusters  of  5  contiguous  voxels)  BOLD  responses.
The analysis of results is based on the utilization of a relatively recent technique in which all
three-dimensional  anatomical  and  functional  information  of  the  brain  is  projected  in  a  flat
representation  of  itself. The  degree  of  correlation  between  the  adopted  model  and  the
functional  exams  was not  high,  being verified  as  well that  the  cerebral  areas  showing
activation/deactivation  suffer  from  great  variability  between  runs  of  the  same  patient.  It  was
yet  observed  that  matching  BOLD  response  areas  amongst  runs  do  not  necessarily  imply
elevated significance. The results obtained allow concluding that, although this is a technique
with  great  potential,  the  mechanisms  that  underlie  the  observed  phenomena  are  not  yet
completely understood,  in  view  of  which  nowadays  it  is  used  exclusively in  order to  point
probable areas for further investigation.


Key words: epileptic discharges; EEG/fMRI; BOLD response; activation; deactivation.


vi

## L I S TA   DE   A C R Ó N I M OS E   S I GL A S

ATP – adenosina trifosfato
BOLD – Blood Oxygen Level Dependent contrast
DICOM – Digital Imaging Communications in Medicine
DP – densidade protónica
EEG – electroencefalograma
EPI – echo planar imaging
FID – free induction decay
FRH – função de resposta hemodinâmica
IfRM – imagem funcional por ressonância magnética
ILAE – International League Against Epilepsy
IRM – imagem por ressonância magnética
MLG – Modelo Linear Geral
PET – Positron Emission Tomography
rCBF – regional cerebral blood flow
rCBV – regional cerebral blood volume
RF – radiofrequência(s)
RM – ressonância magnética
ROI – Region of Interest
SPECT – Single Photon Emission Computed Tomography
SPGR – Spoiled Gradient Recovery
TE – tempo de eco
TR – tempo de repetição

## L I S TA   DE  S Í M B O L O S

M – magnetização total
## T
## 1
– relaxação longitudinal
## T
## 2
– relaxação transversal
## T
## 2
## *
– decaimento livre de indução


vii

## Í NDI C E   DE   M A TÉ R I A S

AGRADECIMENTOS .......................................................................................................................................... iii
RESUMO .............................................................................................................................................................. iv
ABSTRACT ............................................................................................................................................................ v
LISTA DE ACRÓNIMOS E SIGLAS .................................................................................................................. vi
LISTA DE SÍMBOLOS ........................................................................................................................................ vi
CAPÍTULO 1 – INTRODUÇÃO .......................................................................................................................... 1
CAPÍTULO 2 – ANATOMIA E FISIOLOGIA CEREBRAIS ............................................................................. 3
2.1 – O CÉREBRO ............................................................................................................................................................................ 3
2.2 – CÉLULAS DO SISTEMA NERVOSO ............................................................................................................................... 4
2.3 – O POTENCIAL DE ACÇÃO ................................................................................................................................................ 5
2.4 – A SINAPSE .............................................................................................................................................................................. 6
CAPÍTULO 3 – EPILEPSIA ................................................................................................................................ 8
3.1 – SINTOMATOLOGIA E CLASSIFICAÇÃO ..................................................................................................................... 8
3.2 – TRATAMENTO DA EPILEPSIA ................................................................................................................................... 10
CAPÍTULO 4 – ELECTROENCEFALOGRAFIA ............................................................................................. 11
4.1 – CARACTERÍSTICAS DO EEG ........................................................................................................................................ 11
4.2 – TÉCNICAS DE REGISTO ................................................................................................................................................. 11
4.3 – LOCALIZAÇÃO DE FONTES.......................................................................................................................................... 13
CAPÍTULO 5 – IMAGEM POR RESSONÂNCIA MAGNÉTICA.................................................................... 14
5.1 – PRINCÍPIOS FUNDAMENTAIS DA IMAGEM POR RESSONÂNCIA MAGNÉTICA................................... 14
5.2 – PROCESSAMENTO DA IMAGEM TRIDIMENSIONAL ........................................................................................ 17
5.3 – IMAGEM FUNCIONAL POR RESSONÂNCIA MAGNÉTICA ............................................................................... 22
CAPÍTULO 6 – METODOLOGIA EXPERIMENTAL ..................................................................................... 32
6.1 – CASOS CLÍNICOS .............................................................................................................................................................. 32
6.2 – AQUISIÇÃO SIMULTÂNEA DE EEG/IFRM ............................................................................................................. 32
6.3 – PROCESSAMENTO DE DADOS ................................................................................................................................... 34
6.4 – PARÂMETROS DA FUNÇÃO DE RESPOSTA HEMODINÂMICA .................................................................... 36
CAPÍTULO 7 – RESULTADOS ........................................................................................................................ 37
7.1 – FASE 1 – TIPO, INTENSIDADE E LOCALIZAÇÃO DAS RESPOSTAS ........................................................... 37
7.2 – FASE 2 – CONCORDÂNCIA ENTRE REGIÕES COM ALTERAÇÕES BOLD ................................................. 44
7.3 – FASE 3 – ANÁLISE MÚLTIPLA DAS RESPOSTAS BOLD .................................................................................. 50


viii

CAPÍTULO 8 – DISCUSSÃO DE RESULTADOS ........................................................................................... 58
CAPÍTULO 9 – CONCLUSÃO E PERSPECTIVAS FUTURAS ...................................................................... 61
BIBLIOGRAFIA ................................................................................................................................................. 63
ANEXOS .............................................................................................................................................................. 67



ix

## ÍNDI C E   DE   F I G UR A S

Figura  2.1 - Estruturas  do  cérebro.  Corte  coronal  do cérebro evidenciando  as  substâncias  cinzenta  e
branca  ..................................................................................................................................................................................... 3
Figura 2.2 – Estrutura de um neurónio típico de um mamífero .......................................................................... 4
Figura 2.3 – Potencial de acção num neurónio  ........................................................................................................ 6
Figura 2.4 – Transmissão sináptica  ............................................................................................................................. 7
Figura 4.1 – EEG ictal evidenciando o início de uma crise epiléptica  .......................................................... 12
Figura 4.2 – Sistema Internacional 10/20 para registo do EEG clínico  ........................................................ 12
Figura 5.1 – Técnica de eco de spin  ......................................................................................................................... 16
Figura 5.2 – Evolução temporal da forma do molde ao longo do processo de deformação  ................... 19
Figura 5.3 – Planos de corte numa estrutura composta apenas por voxeis de matéria branca ............... 20
Figura 5.4 – Representação de um hemisfério direito insuflado (a), após a introdução dos cortes (b) e
planificado (c)  ................................................................................................................................................................... 20
Figura  5.5 – Diagrama  esquemático  do  sinal  BOLD,  bem  como  do  CBF  e  CBV  em  resposta  a  um
breve período de estimulação neuronal  .................................................................................................................... 24
Figura  5.6 – Aquisição  de um  EEG, simultâneo  com  IfRM,  em  que  se  registou  a  ocorrência  de
actividade epiléptica interictal  ..................................................................................................................................... 26
Figura 5.7 – Protocolo de estimulação com base num EEG simultâneo com um exame de IfRM  ...... 26
Figura 5.8 – Apresentação gráfica de um MLG, em que o modelo consiste em três preditores  ........... 29
Figura 5.9 – Mapa estatístico evidenciando activações positivas e negativas numa representação   3D
(a) e na correspondente planificação (b)  .................................................................................................................. 30
Figura 7.1 – Representações plana e tridimensional do hemisfério esquerdo  ............................................ 38
Figura 7.2 – Representações plana e tridimensional do hemisfério direito, com a respectiva região de
interesse  .............................................................................................................................................................................. 38
Figura  7.3 – Representações plana e tridimensional do hemisfério esquerdo, com a respectiva região
de interesse  ........................................................................................................................................................................ 39
Figura 7.4 – Representações plana e tridimensional do hemisfério direito, com a respectiva região de
interesse  .............................................................................................................................................................................. 39
Figura  7.5 – Representações plana e tridimensional do hemisfério esquerdo, com a respectiva região
de interesse  ........................................................................................................................................................................ 40
Figura 7.6 – Representações plana e tridimensional do hemisfério direito, com a respectiva região de
interesse  .............................................................................................................................................................................. 40


x

Figura  7.7 – Representações plana e tridimensional do hemisfério esquerdo, com a respectiva região
de interesse  ........................................................................................................................................................................ 41
Figura  7.8 – Representações  plana  e  tridimensional  do  hemisfério  direito,  com a  respectiva  zona  de
interesse  .............................................................................................................................................................................. 41
Figura  7.9 – Representações plana e tridimensional do hemisfério esquerdo, com a respectiva região
de interesse  ........................................................................................................................................................................ 42
Figura 7.10 – Representações plana e tridimensional do hemisfério direito, com a respectiva região de
interesse  .............................................................................................................................................................................. 42
Figura 7.11 – Representações plana e tridimensional do hemisfério esquerdo, com a respectiva região
de interesse  ........................................................................................................................................................................ 43
Figura 7.12 – Representações plana e tridimensional do hemisfério direito, com a respectiva região de
interesse  .............................................................................................................................................................................. 43
Figura  7.13 – Hemisfério  esquerdo  evidenciando  as  respostas  para  duas  sequências  diferentes,  bem
como as regiões em comum  ......................................................................................................................................... 45
Figura 7.14 – Hemisfério direito evidenciando as respostas para duas sequências diferentes  .............. 45
Figura  7.15 – Hemisfério  esquerdo  evidenciando  as  respostas  para  seis  sequências  diferentes,  bem
como as regiões em comum  ......................................................................................................................................... 46
Figura 7.16 – Hemisfério direito evidenciando as respostas para seis sequências diferentes, bem como
as regiões em comum  ..................................................................................................................................................... 46
Figura 7.17 – Hemisfério esquerdo. Das três sequências diferentes que foram sobrepostas, apenas uma
possui respostas que ultrapassam o limiar imposto, pelo que não se verificam regiões em comum  .... 47
Figura  7.18 – Hemisfério direito. Das três  sequências  diferentes que foram sobrepostas, apenas uma
possui respostas que ultrapassam o limiar imposto, pelo que não se verificam regiões em comum  .... 47
Figura 7.19 – Hemisfério esquerdo evidenciando as respostas para quatro sequências diferentes, bem
como as regiões em comum  ......................................................................................................................................... 48
Figura 7.20 – Hemisfério direito evidenciando as respostas para quatro sequências diferentes. Não se
verificam regiões em comum  ....................................................................................................................................... 48
Figura 7.21 – Hemisfério esquerdo evidenciando as respostas para quatro sequências diferentes, bem
como a região em comum  ............................................................................................................................................. 49
Figura  7.22 – Hemisfério  direito  evidenciando  as  respostas  para  quatro  sequências  diferentes,  bem
como a região em comum  ............................................................................................................................................. 49
Figura 7.23 – Zonas de resposta no hemisfério esquerdo .................................................................................. 51
Figura 7.24 – Zonas de resposta no hemisfério direito  ...................................................................................... 51
Figura 7.25 – Zonas de resposta no hemisfério esquerdo .................................................................................. 52
Figura 7.26 – Zonas de resposta no hemisfério direito  ...................................................................................... 52
Figura 7.27 – Zonas de resposta no hemisfério esquerdo .................................................................................. 53


xi

Figura 7.28 – Zonas de resposta no hemisfério direito  ...................................................................................... 53
Figura 7.29 – Zonas de resposta no hemisfério esquerdo .................................................................................. 54
Figura 7.30 – Zonas de resposta no hemisfério direito  ...................................................................................... 54
Figura 7.31 – Zonas de resposta no hemisfério esquerdo .................................................................................. 55
Figura 7.32 – Zonas de resposta no hemisfério direito  ...................................................................................... 55
Figura 7.33 – Respostas hemodinâmicas mais significativas: tipo e grau de correlação com o modelo
adoptado  ............................................................................................................................................................................. 56
Figura 7.34 – Número de regiões condizentes e não condizentes ou não visíveis relativamente àquelas
obtidas na fase 2  ............................................................................................................................................................... 57
Figura a.1 – Ajuste do modelo escolhido para uma ROI do paciente GM, hemisfério esquerdo  ........ 70
Figura a.2 – Forma das funções de resposta hemodinâmica com picos a 3, 5, 7 e 9 segundos ............. 71


xii

## ÍNDI C E   DE  TA B E L A S

Tabela 3.1 – Classificação internacional de crises epilépticas  ............................................................................ 9
Tabela 6.1 – Lesões e tipos de crises epilépticas dos pacientes ....................................................................... 32
Tabela 6.2 – Parâmetros de aquisição das imagens funcionais e anatómicas  ............................................. 34
Tabela 7.1 – Regiões cerebrais com activação/desactivação comum em diferentes sequências ........... 56

## Capítulo 1 – Introdução Miguel Gonçalves
## 1

## C A P Í TUL O   1  – I N TR O D UÇ Ã O

Associada  desde  a  Antiguidade  a  entidades  maléficas  e  religiosas, a  epilepsia  foi  durante
séculos  rodeada  pelo  medo  e pela discriminação.  Embora  ainda  se  verifique algum  estigma
social  em determinadas regiões, hoje  em  dia a  epilepsia é  encarada  naturalmente  como  um
distúrbio neurológico, no qual demasiadas células nervosas ficam simultaneamente excitadas,
com respeito à actividade neuronal normal.
No contexto da epilepsia, os estudos de aquisição simultânea de
electroencefalograma/imagem  funcional  por  ressonância  magnética (EEG/IfRM) realizados
até  hoje  mostram  que as  respostas pelo  Método de Contraste  Dependente  do  Nível  de
Oxigenação  Sanguínea (BOLD) observadas  nos  exames  de  IfRM  estão  relacionadas com  os
picos  epileptiformes  detectados  no  EEG,  contudo  esta  ligação  está  longe  de  ser  totalmente
compreendida. Para  além  das respostas  positivas,  que  provavelmente  reflectem  aumentos  na
actividade   neuronal   e   consequente   necessidade   energética, foram   também   descobertas
respostas negativas, cujas origens são mais difíceis de explicar. Há assim ainda muito a fazer
e a descobrir neste campo.
A  partir  do  processamento  dos  dados  funcionais  de  seis  casos  clínicos  com  epilepsia, é
avaliada, numa primeira  fase, a ocorrência e significância das respostas BOLD consequentes
de descargas  epilépticas.  Numa  fase  posterior,  estuda-se  a variação  do  tipo  e  local  das
respostas  entre diferentes  sequências  funcionais  do  mesmo  paciente. Numa  última  fase,
integram-se  todas  as  sequências  funcionais  respeitantes  ao  mesmo  paciente,  segundo  uma
abordagem de análise global, visando a determinação das respostas BOLD mais robustas.
Para o processamento da informação anatómica e funcional, recorreu-se a uma técnica que
permite   modificar   a   forma   como   esses   dados são   apresentados.   Assim,   a   partir da
representação  tridimensional  de  um  hemisfério  cerebral, em  que  são  visíveis  os  respectivos
sulcos  e  circunvoluções,  é  obtida  uma  representação  insuflada  do  mesmo  e,  a  partir  desta,  é
obtido um mapa planificado. Neste último, está presente, contudo, toda a informação original.
Deste modo, é possível observar a localização de todos os focos de activação neuronal numa
mesma imagem e  de  uma  forma  mais  precisa,  uma  vez  que  se  tem  uma  melhor  noção  da
fronteira entre circunvoluções e sulcos e entre margens do mesmo sulco.


## Capítulo 1 – Introdução Miguel Gonçalves
## 2

Esta  dissertação  está  estruturada  de  modo  a que  os  resultados  possam  ser  correctamente
interpretados tendo por base a informação precedente. Assim, os quatro capítulos posteriores
à introdução constituem os fundamentos teóricos nos quais se alicerçou este trabalho.
No capítulo 2 são introduzidos aspectos gerais de anatomia e fisiologia relativos ao cérebro
e    células    nervosas, devido    à    sua    importância    na    compreensão    dos    fenómenos
electrofisiológicos que constituem a base do EEG e daqueles associados às crises epilépticas.
O terceiro capítulo faz uma introdução à epilepsia: sintomatologia, classificação e métodos
de tratamento.
O capítulo 4 trata das características e princípios básicos da electroencefalografia enquanto
técnica fundamental para a detecção dos geradores de actividade epiléptica.
No quinto capítulo são descritos  os  princípios  fundamentais  da  imagem  por  ressonância
magnética  (IRM),  revelando  com  maior  pormenor  os  aspectos  da  imagem  funcional por
ressonância magnética, uma vez que é esta a técnica com maior ênfase neste trabalho. É ainda
explicado detalhadamente o modo como os dados foram processados.
A  parte  experimental  da  dissertação  começa  com  o  capítulo 6,  que  apresenta os  casos
clínicos  e a  descrição  da  metodologia  experimental  implementada,  com  incidências  no
procedimento de aquisição dos exames de EEG e IfRM.
No capítulo seguinte são apresentados os resultados na forma de mapas estatísticos para as
várias fases do processamento de dados.
O oitavo capítulo apresenta  a  discussão  dos  resultados  obtidos, de  acordo  com  os
objectivos  propostos,  incluindo  uma  análise  justificativa  das  diferenças  encontradas  entre  o
modelo proposto e o sinal real e entre diferentes sequências do mesmo paciente. No final, são
ainda referidos os principais problemas que surgiram e a forma como foram superados.
O capítulo 9 contém a conclusão final, em que é feita uma apreciação global do trabalho e
onde se indicam algumas propostas de interesse relevante para o futuro.






Capítulo 2 – Anatomia e Fisiologia Cerebrais  Miguel Gonçalves
## 3

## C A P Í TUL O  2 – A N A TO M I A   E   F I S I O L O GIA C E R E B R A I S

Alguns  cientistas  referem-se ao cérebro como “a última fronteira” na ciência e medicina.
Indubitavelmente, o cérebro é o órgão mais misterioso e pobremente compreendido no corpo
humano.  Embora  se  saiba  muito  acerca  deste  órgão e  do  sistema  nervoso,  há  ainda  muito  a
descobrir [1].

## 2.1 – O CÉREBRO

O  cérebro  é  a  maior e  mais  evidente  estrutura  do  encéfalo,  constituindo  cerca  de  80%  da
massa total deste [1].
O  cérebro  está dividido  em  duas  metades,  os  hemisférios  cerebrais esquerdo  e  direito,
interligados  entre  si  pelo  corpo  caloso,  situado  na  parte  inferior  da  fissura  inter-hemisférica.
Cada  hemisfério  possui  uma  fina  camada  externa  de  substância  cinzenta – o córtex cerebral
(figura 2.1),  que  contém  os  corpos  celulares  dos  neurónios  [1].  Situada  debaixo  do  córtex
cerebral  está  uma  abundante  camada  de substância  branca,  contendo  feixes  de  axónios
neuronais mielinizados, que lhe conferem a aparência branca [1].
Os hemisférios cerebrais estão divididos em quatro lobos cerebrais: lobo frontal, temporal,
parietal e occipital, cada um com funções específicas a desempenhar [1].










Figura 2.1 - Estruturas do  cérebro. Corte coronal do cérebro evidenciando as substâncias cinzenta e
branca [adapt. 1].


Capítulo 2 – Anatomia e Fisiologia Cerebrais  Miguel Gonçalves
## 4

## 2.2 – CÉLULAS DO SISTEMA NERVOSO

No  sistema  nervoso  diferenciam-se  dois  tipos  de  células:  os neurónios,  ou  células
nervosas, e as células da glia ou células gliais [2].
As células gliais cumprem a função de sustentar, proteger, isolar e nutrir os neurónios [2].
No  que  diz  respeito  aos  neurónios,  estes  são  as  unidades  estruturais  fundamentais  do
sistema  nervoso.  Estas  células  altamente  especializadas  geram  impulsos  bioeléctricos  e
transmitem-nos  de  uma  parte  do  corpo  para  outra.  Estes  sinais  alertam-nos  para  uma
variedade de estímulos internos e externos e permitem ao nosso organismo responder-lhes [1].
Os  neurónios  podem  assumir  mais  do  que  uma  forma  e  vários  tamanhos,  contudo,  todos
têm a mesma estrutura básica (figura 2.2). O neurónio é constituído por um volumoso corpo
celular, contendo o núcleo que, por sua vez, se encontra rodeado pelo citoplasma e organelos
nele existentes. Dois tipos de prolongamentos estendem-se a partir do corpo celular: axónios
e dendrites [1,3].
As  dendrites são  prolongamentos  altamente  ramificados  que  se  vão  afilando  e  que
terminam  em  receptores  sensoriais  especializados  (como  os  neurónios  sensoriais  primários)
ou  formam  sinapses  com  neurónios  vizinhos,  dos  quais  recebem  estímulos.  Em  geral,  as
dendrites  são o  principal  meio  de  entrada  de  informação  para  dentro  do  neurónio,  isto  é,  em
direcção ao corpo celular [1,3].
Cada neurónio tem um único axónio que transmite, de uma forma geral, os impulsos para
fora do corpo celular. Os axónios apresentam uma estrutura cilíndrica que pode medir até um
metro  de  comprimento,  terminando  sobre  outros  neurónios  ou  órgãos  efectores  por  meio  de
pequenos ramos que finalizam em pequenas dilatações chamadas botões terminais [3].
Figura 2.2 – Estrutura  de  um  neurónio  típico  de  um  mamífero.  a) Neurónio  sensorial  em  que  o
axónio  se  ramifica.  b) Neurónio  motor  enervando  uma  célula  muscular.  As  setas  indicam  a  direcção
de condução dos potenciais de acção no neurónio [adapt. 4].

Capítulo 2 – Anatomia e Fisiologia Cerebrais  Miguel Gonçalves
## 5

## 2.3 – O POTENCIAL DE ACÇÃO

As funções do sistema nervoso dependem de uma propriedade fundamental dos neurónios
intitulada excitabilidade,  a  qual  está  intimamente  relacionada  com  as  propriedades  do  seu
estado  de  repouso. Como ocorre  em  todas  as  células,  o  neurónio  em  repouso  mantém um
gradiente  iónico através  da  sua  membrana  plasmática,  criando  desse  modo  um  potencial
eléctrico [3]. A diferença de potencial entre os meios intracelular e extracelular num neurónio
típico é cerca de -70  milivolts. Este é conhecido como o potencial de repouso da membrana,
uma vez  que  é  o  potencial  da  célula  nervosa  em  repouso. Nos  neurónios,  os  iões  que  são  os
principais  responsáveis  por  este   gradiente  são  o  sódio  (Na
## +
)  e  o  potássio  (K
## +
),  que  se
encontram em maior concentração nos meios extra e intracelular, respectivamente [1,5].
Este gradiente é possível devido ao facto da membrana plasmática do neurónio transportar
activamente  estes  iões através  de  bombas  sódio-potássio.  Esta  bomba  consiste  em  várias
membranas proteicas que transportam os iões Na
## +
para o exterior da célula e os iões K
## +
para o
interior  da  mesma,  utilizando  energia  na  forma  de adenosina  trifosfato  (ATP) [1]. A
proporção  entre  iões transportados  pela  bomba  é  3  Na
## +
## :  2K
## +
.  Somando  a  este  facto, a
membrana  da  célula  nervosa  é,  em  repouso, praticamente  impermeável  ao  sódio,  impedindo
que este se desloque a favor do seu gradiente electroquímico [5]. Como a saída de sódio não é
acompanhada  pela  entrada  de potássio  na  mesma  proporção,  resulta  que  o  potencial  de
repouso da membrana é negativo. Diz-se então que a membrana está polarizada.
Quando um neurónio é estimulado, a sua membrana torna-se subitamente mais permeável
aos   iões   Na
## +
e,   como tal,   estes   entram   para   dentro   da   célula   a   favor   do   gradiente
electroquímico. Em consequência, ocorre uma alteração do potencial de membrana de -70 mV
para  +30  mV,  fenómeno  que  tem  o  nome  de despolarização da  membrana,  ficando  o
neurónio  num  estado  excitado. Uma  onda  de  despolarização,  conhecida  como potencial  de
acção, transmite-se então ao longo da membrana plasmática (figura 2.3 a) [3,5].
Imediatamente  após a  despolarização  dá-se  o  fenómeno  de repolarização,  em  que  a
membrana  retorna  ao  seu estado  anterior.  A  repolarização  da  membrana é  resultado  de  dois
factores: (1)  um  súbito decréscimo  na  permeabilidade da  membrana  aos  iões  de  sódio,  que
interrompe o  seu  influxo,  e  (2) um  rápido  efluxo  de  iões  potássio  [1].  Observa-se  que  o
potencial  de  membrana decresce  momentaneamente  abaixo  dos -70  mV  neste processo –
hiperpolarização da membrana – o que se deve  a um atraso no encerramento dos canais de
potássio  presentes  na  membrana  (figura 2.3  b)  [5].  Quando um neurónio deixa  de  ser

Capítulo 2 – Anatomia e Fisiologia Cerebrais  Miguel Gonçalves
## 6

estimulado,   a   bomba sódio-potássio   rapidamente   restabelece as   concentrações   intra   e
extracelulares de ambos os iões, preparando-o para um novo potencial de acção [1].

## 2.4 – A SINAPSE

A  informação  chega  e  abandona  o  cérebro  por  meio  de  impulsos  nervosos  que  são
propagados  através  dos  neurónios. Estes impulsos transmitem-se de  um  neurónio  para  outro
mediante um  pequeno  espaço  que  os  separa.  Esta  junção  tem  o  nome  de sinapse. Existem
dois tipos de sinapses: químicas e eléctricas. As sinapses químicas consistem em (1) um botão
terminal  (ou  outro  tipo  de terminação  axonal) do  neurónio  pré-sináptico  (o  que  transmite  o
impulso),  (2)  um  espaço  entre  os  neurónios  adjacentes – fenda  sináptica,  e  (3) a  membrana
da dendrite  do  neurónio  pós-sináptico  (aquele  que  recebe  o  impulso)  [1]. As  sinapses
eléctricas  são,  por  sua  vez,  relativamente  mais  simples  estrutural  e  funcionalmente,  tendo
lugar em locais especializados denominados gap junctions [2].
Como se dá então a transmissão sináptica entre neurónios adjacentes?
Nas sinapses de origem química, quando um potencial de acção alcança um botão terminal,
a despolarização  da  membrana plasmática  do  botão  estimula  um  rápido  influxo  de  iões  de
cálcio. Estes iões, por sua vez, estimulam a libertação, por exocitose, de substâncias químicas
armazenadas em pequenas vesículas no botão terminal. Estes químicos são conhecidos como
neurotransmissores.   Os   neurotransmissores   são   libertados   para   a   fenda   sináptica e
Figura 2.3 – Potencial  de  acção  num  neurónio: (a)  onda  de despolarização  [adapt.  5].  (b)  Potencial
de membrana e permeabilidade aos iões Na
## +
e K
## +
## [adapt. 1].

Capítulo 2 – Anatomia e Fisiologia Cerebrais  Miguel Gonçalves
## 7

posteriormente  ligam-se aos  receptores  localizados  na  membrana  do  neurónio  pós-sináptico.
Na  maioria  dos  casos,  isto  estimula  um  rápido  aumento  na  permeabilidade  da  membrana  do
neurónio pós-sináptico  aos  iões  de  sódio,  o  que  irá  desencadear  um  novo  potencial  de  acção
na  célula  pós-sináptica – sinapse  excitatória.  Contudo,  existem  também  sinapses  inibitórias
que,  como  o  próprio  nome  indica,  inibem  a transmissão  do  impulso  nervoso por  meio  de
neurotransmissores  que  tornam  a  membrana  da  célula  pós-sináptica  menos  excitável. Uma
única  célula  nervosa  pode  ter  até  50000  sinapses,  e  é  a  soma  de  impulsos  excitatórios  e
inibitórios que vai definir se o neurónio pós-sináptico gera um potencial de acção ou não [1].
Nas  sinapses  eléctricas,  a  corrente  iónica  é  transferida  directamente  de  uma  célula  para
outra,  uma  vez  que  os  canais  existentes  nas gap  junctions permitem  a  passagem  directa  dos
iões do citoplasma de uma célula para o citoplasma da outra, criando, quase instantaneamente,
um  potencial  de  acção  no  neurónio  pós-sináptico. Deste  modo,  a  transmissão  da  informação
por  meio  de  sinapses  eléctricas  é  manifestamente  mais  rápida  relativamente  às  sinapses
químicas. Porém,  as  sinapses  de  origem  eléctrica são  utilizadas  apenas  no  sentido  de  enviar
sinais  de  despolarização;  elas não  possuem  a  capacidade  de produzir  impulsos  inibitórios  ou
de alterar as propriedades eléctricas das células pós-sinápticas [2].
A um aumento da activação neuronal corresponde um consumo de glicose mais elevado, a
qual é degradada preferencialmente em condições aeróbias. Como forma de responder a esta
necessidade, as quantidades de oxigénio sanguíneo e, consequentemente, de oxihemoglobina,
aumentam na região em causa. É este aumento de hemoglobina oxigenada que é utilizado pela
ressonância magnética funcional para medir esse aumento de actividade.






Figura 2.4 – Transmissão  sináptica
## [adapt. 1].

## Capítulo 3 - Epilepsia  Miguel Gonçalves
## 8

## C A P Í TUL O  3 – E P I L E P S I A

A epilepsia é um distúrbio neurológico que afecta pessoas de todas as idades e em todos os
países do mundo.

## 3.1 – SINTOMATOLOGIA E CLASSIFICAÇÃO

Esta perturbação é caracterizada por ataques (ou crises) recorrentes e espontâneas, que são
reacções   físicas   a   súbitas   e   excessivas   descargas   eléctricas   num   grupo   de   neurónios
anormalmente hiperactivos e hipersíncronos [6,7].
Os ataques podem variar desde os mais breves lapsos de atenção ou espasmos musculares a
severas  e  prolongadas  convulsões  (i.e.  contracções musculares violentas  e  involuntárias  ou
séries   de   contracções   musculares).   As   crises   epilépticas   podem   variar   igualmente   em
frequência, desde menos de uma por ano a várias por dia [6].
O tipo mais comum de epilepsia, para 6 em cada 10 pessoas com este distúrbio, é chamada
epilepsia  idiopática  e  não  tem  causa conhecida  [6].  Epilepsia com  causa  conhecida  é
denominada epilepsia secundária ou sintomática. As causas deste tipo de epilepsia podem ser:
traumatismos  cranianos  que  provocam  cicatrizes  cerebrais,  traumatismos  de parto,  algumas
drogas  ou  tóxicos,  interrupção  do  fluxo  sanguíneo  cerebral  causado  por  acidente  vascular
cerebral  ou  problemas  cardiovasculares,  doenças  infecciosas  ou  tumores  [6,8]. Existe  ainda
um  terceiro  tipo,  chamado epilepsia  criptogénica.  Este  termo emprega-se  quando  se  suspeita
da existência de uma causa mas não se consegue detectar a mesma [8].
No   que   diz   respeito   à   classificação   das   crises   epilépticas,   a   tabela 3.1   mostra   a
Classificação  Internacional  de  crises  epilépticas proposta  pela  Comissão de  Classificação  e
Terminologia  da Liga  Internacional  Contra  a  Epilepsia  (ILAE)  e  aprovada  em 2001.  Esta
classificação    é    baseada    na    expressão    clínica    do    ataque,    bem    como    no    registo
electroencefalográfico  durante  e entre  crises.  A  principal  divisão  é  realizada  entre crises
autolimitadas e crises contínuas,  sendo  que  ambas  se  subdividem em  crises  focais  (ou
parciais) e crises generalizadas [9].
Nas  crises focais,  as  descargas  eléctricas  anormais  têm  origem  numa  parte  localizada  do
cérebro, sendo que os sintomas/sinais são dependentes do local afectado, não existindo nunca
perda  completa  dos  sentidos. Estas  descargas  podem  permanecer  localizadas  ou  podem

## Capítulo 3 - Epilepsia  Miguel Gonçalves
## 9

disseminar-se para   outras   partes   do   cérebro, tornando-se, assim, generalizadas   (crises
generalizadas secundárias) [10].
Por  outro  lado, as  crises  generalizadas têm  a  sua  origem  em  ambos  os  hemisférios
cerebrais  simultaneamente  (crises  generalizadas  primárias), sendo caracterizadas  por uma
perda completa  dos  sentidos/percepção e  por  ausência  de  uma  aura
## 1
,  uma  vez  que  surgem
subitamente e sem aviso prévio [10].
Existe ainda uma terceira categoria principal: factores precipitantes de crises reflexas, que
podem dar origem a crises generalizadas ou focais [9].
Embora o registo electroencefalográfico da  actividade ictal, isto é, aquando da ocorrência
da  crise,  permaneça  a  pedra  fundamental  no  que  respeita  ao  diagnóstico  da  epilepsia, as
descargas  epilépticas  interictais  (entre  crises)  são  consideradas  como  sendo  importantes,  na
medida  em  que  representam  indicadores  independentes e  complementares da  zona  activada
epilepticamente [11,12]. É com base nesta informação que se irão procurar as localizações dos
focos  epilépticos  a  partir  da  informação  contida  na  actividade  interictal. Porém,  e  também
devido à reduzida regularidade com que se consegue obter um electroencefalograma aquando
da  ocorrência  de  uma  crise,  os  profissionais  desta  área continuam dependentes da  expressão
clínica do doente: o historial médico e a capacidade do observador de descrever o ataque, uma
vez que o próprio paciente não tem recordação do ataque, excepto em crises parciais simples.
Se não for muito jovem, o paciente pode dar informação acerca da presença e natureza da aura
## [10].

Tabela 3.1 – Classificação internacional de crises epilépticas [adapt 9]
## CRISES AUTOLIMITADAS
Crises generalizadas
Crises focais

## CRISES CONTÍNUAS
Status epilepticus
## 2
generalizado
Status epilepticus focal

## FACTORES PRECIPITANTES DE CRISES REFLEXAS



## 1
Conjunto de sensações que precede um ataque epiléptico.
## 2
Um status epilepticus acontece sempre que uma crise persiste pelo menos por 30 minutos ou a sua frequência
de repetição é tão elevada que não existe recuperação entre ataques.

## Capítulo 3 - Epilepsia  Miguel Gonçalves
## 10

## 3.2 – TRATAMENTO DA EPILEPSIA

Há  a  ideia errónea  de  que  a  epilepsia  é  uma  doença  para  toda  a  vida;  inclusive,  muitos
médicos  advertem  os  seus  pacientes de que  devem  fazer  medicação  antiepiléptica  a  vida
inteira.  Na  realidade, há  uma  série  de medicamentos  para  a  epilepsia  e cada  vez  mais vão
surgindo novos produtos. O sucesso do tratamento depende de vários factores: tipo de crises,
diagnóstico  precoce  da  doença,  eficácia  do(s)  medicamento(s)  utilizado(s),  cumprimento  da
medicação,  existência  de  outras  lesões  associadas  e  de  problemas socioprofissionais [8].
Algumas  epilepsias  das  crianças  curam-se  sempre,  outros  tipos  quase  sempre,  só  algumas
necessitam permanentemente de medicação antiepiléptica. De uma forma geral, 70 por cento
dos doentes estão livres de crises 15 anos após o início da medicação [8].
Quando  o  tratamento  médico  não  surte  efeito, é  possível,  nalguns casos,  recorrer  à
“cirurgia da epilepsia”. Para isso, o tecido cerebral lesado, que provoca as crises, tem de estar
circunscrito  a  uma  área  do  cérebro,  sendo  ainda  necessário  que  esta possa  ser  removida  sem
alterar  a  personalidade  ou  as  funções  do  doente [8]. É  devido  a  esta  necessidade  que  o  tema
em  questão  nesta  tese:  a  aquisição  simultânea  de  EEG/IfRM,  é  de  extrema  importância,  na
medida em que visa detectar mais rigorosamente os focos epilépticos no cérebro, com vista à
sua remoção cirúrgica.
A  cirurgia  pode  ser  praticada  em  crianças  e  adultos,  mas  não  serve  para  todas  as  pessoas
com epilepsia ou para todas que têm mau controlo das crises [8]. Para decidirem se a pessoa
beneficia com a cirurgia, os médicos pretendem saber:
 Os ataques são realmente crises epilépticas?
 Foi tentado um controlo medicamentoso exaustivo?
 O tipo de crises pode melhorar com a cirurgia?
 Os benefícios ultrapassam os riscos da cirurgia?

Verificando-se estas condições pode realizar-se a intervenção.
Com  excepção  do implante  vagal, todos  os  tipos  de  cirurgia  envolvem  o  cérebro. De  um
modo  geral, podem  ser  feitos  dois  tipos  de  cirurgia: (1)  remoção  da  área  responsável  pela
produção de crises ou (2) interrupção das vias nervosas ao longo das quais se disseminam os
impulsos que transmitem as crises [8].

## Capítulo 4 - Electroencefalografia  Miguel Gonçalves
## 11

## CA P Í TUL O  4 – E L E C TR O E NC E F A L O GR A F IA

A  electroencefalografia  consiste no  registo  da  actividade  eléctrica  do  cérebro  através  da
colocação  de  vários  eléctrodos  ao  longo  do  escalpe. A  actividade  conjunta  de  milhões  de
neurónios  corticais,  gerando potenciais neuronais pós-sinápticos  inibitórios  e  excitatórios,
produz um campo eléctrico suficientemente forte para ser medido à superfície do escalpe, na
forma  de electroencefalograma. Para  além  destes  potenciais,  correntes  celulares  intrínsecas
produzidas pela activação de canais iónicos provavelmente também contribuem para o EEG,
embora o seu papel ainda não tenha sido demonstrado claramente [13,14].

## 4.1 – CARACTERÍSTICAS DO EEG

O  EEG  começou  a  ser  utilizado  no  contexto  dos  distúrbios  epilépticos  pouco  após  a  sua
descoberta. Este teste permanece hoje como o exame padrão para o diagnóstico da epilepsia,
assim como para a classificação dos tipos de crise epiléptica e de epilepsia e localização dos
geradores  da  actividade  epiléptica [7,13]. Para  tal,  muito  contribuiu a  sua insuperável
resolução  temporal  da  ordem  do  milissegundo,  em  comparação  com  outras  técnicas  de
imagem  como a PET
## 3
## ,  SPECT
## 4
ou  IRM,  fornecendo  informação  detalhada  sobre  a  evolução
temporal  do  funcionamento  cerebral (figura 4.1) [13,15]. Contudo,  a resolução  espacial  do
EEG é pobre, na gama do centímetro, o que se deve a vários factores: 1) limitado número de
eléctrodos utilizados;  2) distorções  resultantes  das  diferentes condutividades dos  tecidos
intervenientes;  3) ao  facto  de existirem processos  mentais,  tal  como  o  pensamento,  que
apresentam  respostas  difusas e,  como  tal, constituem  fontes  de  ruído  relativamente  ao  sinal
que  se  pretende  analisar;  4) o  problema  inverso,  desenvolvido  no  subcapítulo  4.3.  Deste
modo,  a  correlação  dos  sinais com  uma  determinada  fonte  é  problemática, dificultando  a
determinação precisa da região responsável pela descarga epiléptica [15].

## 4.2 – TÉCNICAS DE REGISTO

O EEG clínico é comummente gravado utilizando o Sistema Internacional 10/20, que é um
sistema padrão  para  a  colocação uniforme de  eléctrodos  na  superfície  do escalpe, sendo,  em
geral,  o  contacto  assegurado  por  um  gel  condutor  de  forma  a  diminuir  a  impedância.  Este

## 3
Do inglês: Positron Emission Tomography
## 4
Do inglês: Single Photon Emission Computed Tomography

## Capítulo 4 - Electroencefalografia  Miguel Gonçalves
## 12

sistema de montagem emprega 21 eléctrodos em pontos definidos por referências anatómicas
no escalpe. Os números 10 e 20 representam percentagens que significam distâncias relativas
entre as diferentes localizações dos eléctrodos no perímetro do crânio (figura 4.2) [13].











Figura 4.2 – Sistema  Internacional  10/20  para  registo  do  EEG  clínico.  Inion  representa  a  saliência
mais   proeminente   do   osso   occipital   na   parte   póstero-inferior   do   crânio,   enquanto   nasion   é   a
intersecção dos ossos frontal e nasais [adapt. 13].

Como é sabido, o potencial eléctrico é uma grandeza relativa, pelo que o seu valor terá que
ser obtido através de uma diferença, o que significa que é necessária a utilização de potenciais
Figura 4.1 – EEG ictal evidenciando o início de uma crise epiléptica (a partir do primeiro segundo)
## [adapt. 13].

## Capítulo 4 - Electroencefalografia  Miguel Gonçalves
## 13

de  referência.  Nesse  sentido,  existem  duas  montagens  principais  que  são  utilizadas  na  rotina
clínica:  as  montagens  monopolares  e  as  bipolares.  As  primeiras requerem  um  eléctrodo  de
referência  que  está  posicionado  a  uma  distância  considerável  ou  que  é  tido  como  o  valor
médio de todos os eléctrodos [13]. Por sua vez, as montagens bipolares consideram a medida
de cada canal como a diferença entre um par de eléctrodos, normalmente adjacentes [14].
Como  alternativa  à  colocação  de  eléctrodos  directamente  no  escalpe, podem  ser  usadas
toucas onde os eléctrodos estão fixos.
As  exigências  técnicas  no  que  respeita  ao  equipamento  para  o  registo  de  EEGs  são
relativamente  modestas:  um  conjunto  de  eléctrodos,  um  amplificador  de  sinal,  um  conversor
analógico/digital   e   um   computador   para   armazenamento   de   dados,   análise   do   sinal   e
representação gráfica [13].
Convém  ainda  referir,  já  no  campo  do  processamento  de  sinal,  que  o  sinal  obtido  está
contaminado com artefactos e ruído, pelo que o seu cancelamento através do uso de filtros é
um procedimento importante para a subsequente análise do sinal ser fiável [13].

## 4.3 – LOCALIZAÇÃO DE FONTES

O sonho último da   electroencefalografia é   o   de   ser   possível   encontrar   as   fontes
intracerebrais dos  potenciais  registados  no  escalpe  e  relacioná-las  com  a  actividade  dos
geradores neurais dentro do cérebro. Este forma o problema inverso da electroencefalografia.
A  questão  reside  no  facto  do  problema  inverso  não  possuir  uma  solução  única  e,  como  tal,
diferentes  combinações  de  fontes  intracerebrais  podem  resultar  na  mesma  distribuição  de
potencial  no  escalpe. A  única forma de resolver  este  problema  é  através  da  realização  de
suposições  apriorísticas  específicas  acerca  das  fontes  intracerebrais  que  se  assume  serem a
causa  de  uma  dada  distribuição  de  potencial  no  EEG ao  nível  do  escalpe, bem  como pela
introdução de um modelo do meio condutor que separa a fonte dos eléctrodos e que leva em
conta propriedades essenciais do corpo humano, como a geometria e a resistividade [13,16].
Acerca das   fontes   intracerebrais,   vários   métodos   matemáticos   têm   vindo   a   ser
desenvolvidos, sendo que normalmente estão divididos em dois grupos principais: os modelos
dipolares, que assumem que as fontes estão localizadas; e os modelos lineares ou distribuídos,
que assumem fontes extensas com características específicas [7,13].

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 14

## C A P Í TUL O  5 – I M A GE M   P O R   R E S S O NÂ NC I A   M A G NÉ TI C A

A  descoberta  e  o  desenvolvimento  da  imagem  por  ressonância  magnética representa  um
marco histórico no aperfeiçoamento da imagem médica, complementando-se com as restantes
técnicas de imagem previamente existentes. É uma técnica de diagnóstico que, sem recurso à
radiação  ionizante, obtém  informação  anatómica  detalhada  devido  à  sua  elevada  resolução
espacial (0.3 – 1 mm) e  contraste. Adicionalmente,  a  IRM é  dotada  de uma  grande
flexibilidade,  permitindo  obter  igualmente imagens  funcionais,  espectroscópicas  e  de  tensor
de difusão, pelo que é considerada por muitos como a „jóia da coroa‟ da tecnologia médica.

## 5.1 – PRINCÍPIOS FUNDAMENTAIS DA IMAGEM POR RESSONÂNCIA MAGNÉTICA

Neste  capítulo, adoptou-se  uma  abordagem  clássica  na  forma  de  descrever  os  princípios
fundamentais da imagem por ressonância magnética.

5.1.1 – Resposta do núcleo de hidrogénio a um campo magnético estático

A  ressonância  magnética  (RM)  baseia-se  na  interacção  entre  um  campo  magnético
aplicado e um núcleo que possui spin. Spin nuclear, ou mais precisamente, momento angular
de  spin  nuclear,  é  uma  das  várias  propriedades  intrínsecas  dum  átomo e  consiste  num
movimento rotacional constante sobre um eixo. O núcleo do isótopo
## 1
H de hidrogénio, sendo
composto  por  apenas  um  protão,  é  uma  escolha  natural para  sondar  o  corpo  utilizando
técnicas de RM, por várias razões: 1) tem um spin de ±½ e é o isótopo mais abundante para o
hidrogénio; 2) a sua resposta a um campo magnético aplicado é uma das maiores encontradas
na  natureza;  3)  o  corpo humano  é  composto  por  tecidos  que  contêm  principalmente  água  e
gordura, ambos contendo hidrogénio [17].
Num volume arbitrário de tecido, existe um grande número de átomos de hidrogénio, cujos
momentos   magnéticos
## 5
estão   orientados   aleatoriamente,   de   forma   que   se   anulam
mutuamente, resultando numa magnetização total (M) nula. Uma vez sujeitos à acção de um
campo  magnético B
## 0
, os  protões  passam  a  precessar paralela  (estado  de  energia  mais  baixa)
ou antiparalelamente (estado de energia mais elevada) em torno de um eixo com a direcção do

## 5
Cada protão em rotação tem a si associado um vector de momento magnético, orientado paralelamente ao eixo
de rotação.

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 15

campo aplicado – interacção de Zeeman. Devido à diferença de energias dos dois estados, o
estado  de  energia  mais  baixa  é  mais  povoado  que  o  estado  de  energia  mais  alta.  Por  este
motivo, a magnetização total deixa de ser nula e passa a ter a direcção do campo [17].
A frequência de precessão é determinada através da equação de Larmor:
## 휔
## 0
## =훾퐵
## 0
## (5.1)
onde 휔
## 0
é  a  frequência  de  Larmor, 퐵
## 0
é  a intensidade do  campo  magnético e 훾 representa  a
razão giromagnética, que é uma constante que depende do núcleo [17,18].

5.1.2 – Resposta a um pulso de radiofrequências: ressonância e relaxação

De modo a obter um sinal que possa ser medido, ter-se-á que excitar o sistema em primeiro
lugar.  Isto  é  realizado  através  da  introdução  de  pulsos  de radiofrequências (RF) com  uma
frequência  exactamente  igual  à  frequência  de  Larmor.  Deste  modo,  as  ondas  de  RF  vão
transmitir energia aos protões por ressonância, o que vai provocar um aumento no número de
núcleos antiparalelos, sendo que a magnetização total roda em direcção ao plano transversal
## 6

(plano xy). De acordo com a lei de Faraday da indução, uma corrente eléctrica de frequência
## 휔
## 0
é induzida numa bobine devido à variação do fluxo magnético, o que constitui o sinal de
RM. Quando o pulso de RF é desligado, os núcleos perdem a energia em excesso e retornam
ao  seu  alinhamento  original,  provocando  um aumento  gradual  na  magnetização  longitudinal
(em z) – relaxação.  Ao  mesmo  tempo,  mas  independentemente,  a  magnetização  no  plano
transversal   decresce   gradualmente   devido   à   desfasagem   progressiva   dos   momentos
magnéticos
## 7
,  o  que  implica  uma  diminuição  no  sinal  medido – decaimento  livre  de  indução
## (FID
## 8
## ) [19-21].

5.1.3 – Tempos de relaxação e ponderação de imagem

O  tempo  de  relaxação  T
## 1
,  ou  spin-rede,  é  o  intervalo  de  tempo  requerido  para  a
componente longitudinal de M recuperar 63% do seu valor original após um pulso de RF de
90º. Por   sua   vez,   o   tempo   de   relaxação   T
## 2
,   ou spin-spin,   reflecte   o   decaimento   da
magnetização  transversal  e representa  o  tempo  necessário  para  que  essa  componente  decaia
37% do seu valor inicial i.e., imediatamente após um pulso de RF de 90º [17,19].

## 6
Um pulso de 90º, por exemplo, faz rodar a magnetização total do plano longitudinal para o plano transversal.
## 7
Esta desfasagem deve-se à inomogeneidade do campo magnético e a diferenças de susceptibilidade magnética.
## 8
Do inglês: Free Induction Decay.

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 16

Existe ainda o tempo de relaxação T
## 2
## *
, que é o tempo de decaimento do envelope do FID:
## 1
## 푇
## 2
## ∗
## =
## 1
## 푇
## 2
## +
## 1
## 푇
## 2 푖푛표푚표푔
## (5.2)
onde 푇
## 2 푖푛표푚표푔
é  o  tempo  de  relaxação  devido  às inomogeneidades  do  campo externo  [18].
Como referido anteriormente, o sinal que é medido é o FID, contudo, o que interessa medir é
o  T
## 2
intrínseco  dos  tecidos.  Para  separar  as  duas  constantes  de  decaimento  utiliza-se  uma
técnica conhecida como Eco de Spin. Esta sequência utiliza um ou mais pulsos de RF de 180º
após  a  obtenção  do FID (figura 5.1). Os  pulsos  de  180º  têm  a  finalidade  de  reverter  a
desfasagem dos protões, de modo que os momentos magnéticos se voltam a alinhar no plano
xy,  actuando  assim  como  um  eco. Assim,  apenas  a  relaxação  spin-spin  não  é  afectada  pelo
pulso  de  180º,  pelo  que  a  perda  de  sinal  no  plano  transversal  se  deve  apenas  à  relaxação  T
## 2

verdadeira [17,18].
Neste  contexto,  existe  uma  alternativa  ao  Eco  de  Spin.  A  técnica  de Eco  de  Gradiente
utiliza,  ao  invés  do  pulso  de  180º,  a  inversão  de  gradientes. Deste modo,  a  aplicação  de  um
pulso de gradiente de polaridade oposta ao desfasamento original inverte este desfasamento e
produz um sinal de eco [17,19].
O facto dos tempos de  relaxação T
## 1
e T
## 2
diferirem entre os vários tecidos é a base para a
obtenção  do  contraste  em  IRM. Podem  ainda  ser  obtidas  imagens  ponderadas  em  densidade
protónica (DP), que consiste no número de protões por unidade de volume de tecido [19,20].
A  ponderação  em  T
## 1
e  T
## 2
e  DP pressupõe  o  ajuste dos  seguintes parâmetros:  tempo  de
repetição (TR) e tempo de eco (TE). O primeiro é o tempo entre pulsos de excitação de RF de
90º sucessivos e o segundo mede o tempo decorrido entre o pulso de excitação e o máximo do
eco [17,19]. Cada ponderação será obtida com uma sequência de aquisição diferente.
Figura 5.1 – Técnica  de  eco  de  spin. a) Sequência  de  pulsos  de RF. b) Obtenção  de T
## 2
a  partir  da
recuperação do sinal de T
## 2
## *
## [adapt. 18].

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 17

5.1.4 – Formação de imagem: gradientes de campo magnético

Para  se  obter  uma  imagem,  ter-se-á  que identificar  a  contribuição  de cada  elemento  de
volume,  ou voxel. O mecanismo  através  do  qual  se  associa  um  sinal  a  uma  determinada
posição espacial é realizado através do uso de gradientes de campo magnético, que constituem
pequenas perturbações (~1%) sobrepostas ao campo magnético estático principal. Assim, em
primeiro  lugar,  um gradiente  de  campo  é  imposto segundo  uma  direcção  (x,  y ou z). Como
resultado, cada  corte (ou “fatia”) vai  ter  uma  frequência  de  ressonância  única. Deste  modo,
quando  se  aplica  um  pulso  de  RF  com  uma  frequência  específica,  apenas  a  “fatia”  cujos
protões precessam a essa frequência vai ser excitada. Em seguida, realiza-se a codificação de
frequência, que consiste na aplicação de um gradiente de campo num plano perpendicular ao
anterior, resultando que, em cada linha da “fatia” previamente seleccionada, as frequências
serão  diferentes.  Para  isolar  um  ponto  dessa  linha  realiza-se  uma  codificação  de  fase,
recorrendo   ao   uso   de   um   gradiente   num   plano   perpendicular   aos   dois   anteriores.
Analogamente,  cada  ponto  dessa  linha  adquire  uma  frequência  diferente.  Contudo,  se  o
gradiente estiver activo apenas por breves instantes, resulta que os spins, ao recuperarem a sua
frequência  original,  possuem  fases  diferentes. Deste  modo,  cada  voxel está  individualizado,
podendo assim ser obtida a sua informação de uma forma independente dos voxeis contíguos.
A informação obtida é processada com recurso a análise de Fourier [17,22].
Uma  vez  obtida  a  primeira  “fatia”,  isto  é,  a  primeira  imagem  bidimensional  (2D)  da
estrutura que estamos a analisar, é obtida a “fatia” seguinte, e assim sucessivamente. Uma vez
terminado   o   exame,   temos   várias imagens   2D   que,   no   seu   conjunto,   formam   uma
representação tridimensional da estrutura.

## 5.2 – PROCESSAMENTO DA IMAGEM TRIDIMENSIONAL

No  contexto  deste  trabalho,  este  subcapítulo assume grande  importância, na  medida  em
que  visa  explicar  os  fundamentos  das  transformações  efectuadas  na  anatomia  cerebral  dos
pacientes. Assim, uma vez obtida a imagem tridimensional do cérebro, é realizada uma série
de  operações  que  conduzem  à  obtenção  de uma  representação  planificada de  cada  um  dos
hemisférios  cerebrais como  forma  de visualizar de  um  modo  mais  correcto os focos  de
activação neuronal:


Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 18

5.2.1 – Correcção de inomogeneidades

As  imagens  de  RM  de  alta  resolução  ponderadas  em  T
## 1
estão  normalmente  corrompidas
por  artefactos  de  susceptibilidade  magnética  e  por  inomogeneidades  do  campo  magnético
externo,  o  que  resulta  em  variações  na  intensidade  e  contraste  ao  longo  da  imagem. Estas
variações  são  indesejáveis quando  se  pretende classificar os  voxeis  em  diferentes  tipos  de
tecidos [23].
Neste  procedimento, pretende-se  normalizar  a  intensidade  dos  voxeis  de  matéria  branca,
apenas. Deste modo, o primeiro passo consiste em seleccionar a gama de intensidades na qual
se  encontram  todos  os voxeis  de  matéria  branca  e, em  seguida, é  utilizada  uma  interpolação
cubic spline [23]. Para verificar se a intensidade dos voxeis está suficientemente homogénea é
calculado um histograma de intensidades.

5.2.2 – Transformação para o espaço Talairach

De  modo  a  ser  possível  realizar  comparações  significativas  entre  imagens  de  diferentes
cérebros,  diferenças  extrínsecas  (posição  e  orientação)  devem  ser  removidas  e  diferenças
intrínsecas  (tamanho  e  forma)  minimizadas.  Um  processo  de  transformação  denominado
normalização  espacial   é  utilizado  para  calcular   e  reverter   essas  diferenças   através  da
comparação de um conjunto de  características cerebrais derivadas de um cérebro padrão.  As
características globais do cérebro documentado no Atlas de Talairach de 1988 [24] são ideais
para este processo de transformação. Assim, a abordagem mais comum consiste na utilização
de  uma  transformação affine com  nove  parâmetros, compreendendo rotações,  translações e
redimensionamentos [25].

5.2.3 – Remoção do crânio

Para remover o crânio utiliza-se um molde elipsoidal, cuja constituição se assemelha a uma
rede.  Este  molde  é  deformado  para  coincidir  com  a  superfície  interior  do  crânio,  sendo  o
processo de deformação conduzido por dois tipos de “forças”: (1) uma força de  IRM (푭
## 푀
## )
orientada no sentido de conduzir o molde em direcção ao exterior do cérebro, e (2) uma força
de  redução  de  curvatura (푭
## 푆
),  forçando  a  suavização  do  molde  deformado.  O  procedimento
consiste  em  centrar  o  molde,  baseado  num  icosaedro  super-rendilhado  com  2562  vértices  e

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 19

5120  triângulos,  nas  coordenadas  de  Talairach (푥=0,푦=−10,푧=10) e  gradualmente
deformá-lo  através  de  um  conjunto  de  passos  iterativos  (ver  anexos)  (figura  5.2). Uma  vez
deformado,  o  molde  é  utilizado  para  eliminar  o  crânio  da  imagem  tridimensional  através  da
remoção de todos os voxeis exteriores à superfície rendilhada [23].

5.2.4 – Segmentação e Reconstrução do córtex

A  classificação  dos  diferentes  tipos  de  tecidos  cerebrais  torna-se  necessária  quando  se
pretende  realizar  um  procedimento  de segmentação,  isto  é,  dividir  o  cérebro  nos  seus
hemisférios  constituintes. Este  procedimento  é  tanto  mais  necessário  e  importante  quando  a
segmentação é realizada segundo a fronteira matéria cinzenta/branca, como neste projecto. A
razão de se utilizar esta interface em vez da superfície exterior do córtex deve-se ao facto de,
aquando  da  reconstrução  das  superfícies  após  a  segmentação,  a  topologia  das  mesmas  ser
mais  correcta  quando  se  utiliza  a  matéria  branca.  Assim, um  dos  primeiros  passos  neste
procedimento consiste na criação e análise de histogramas de intensidade com o objectivo de
detectar  os  picos  de  matéria  cinzenta  e  branca,  a  partir  dos  quais  se  decide  o  valor  da
intensidade que  as  separa. Em  seguida,  e  com  base  nos  valores  de  intensidade  dos  picos  de
matéria  cinzenta  e  branca,  todos  os  voxeis  correspondentes  a  matéria  branca  são  marcados
através  de  um  processo  iterativo,  sendo  aos  restantes  atribuída  intensidade zero  (figura  5.3).
Por último, os hemisférios são desconectados através da criação automática de dois planos de
corte que previnem a conectividade entre hemisférios. O primeiro é um corte sagital ao longo
do  corpo  caloso,  que  separa  os  dois  hemisférios,  enquanto  o  segundo  é  um  corte  horizontal
através  da  ponte  de  Varólio  (estrutura  integrante  do  tronco  encefálico),  removendo  as
estruturas   subcorticais   e   permitindo   a   geração   de   duas   superfícies tridimensionais
topologicamente fechadas (figura 5.3) [26,23].
O  processo  de reconstrução das  superfícies  é  realizado  através  da  deformação  de  um
molde, utilizando transformações elásticas baseadas na informação da intensidade, de modo a
forçá-lo a moldar a forma da estrutura obtida anteriormente [23].
Figura 5.2 – Evolução temporal da forma do molde ao longo do processo de deformação [23].

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 20

Em  último  lugar,  as  superfícies  resultantes são  cobertas  com  um  molde  de  rendilhados
triangulares,  sendo  este  deformado  para  produzir  uma  representação  exacta  e  suavizada  da
interface matéria cinzenta/branca [23].





5.2.5 – Insuflação e planificação dos hemisférios cerebrais

A natureza  altamente  pregueada  da camada cortical  dificulta  a  visualização  da  actividade
funcional  de  um  modo  significativo.  Esta  realidade  toma  especial importância  em  focos  de
activação  diferentes  que  estão  próximos  em  volume, mas  relativamente  distantes  em  termos
de  distância  ao  longo  da  camada  cortical,  como, por  exemplo, activações  em  margens
diferentes do mesmo sulco. Assim, as superfícies hemisféricas obtidas anteriormente são alvo
de um processo de “insuflação” (figura 5.4 a) para que a actividade ocorrente no interior dos
sulcos  possa  ser  facilmente  visualizada. Posteriormente, essas  estruturas  insufladas são
planificadas   de   modo   a   que   todos   os   focos   de   actividade   no   hemisfério   possam   ser
contemplados numa  única visualização (figura  5.4 c), permitindo  a  observação  de  toda  a
informação de um modo mais imediatamente abrangente [27].

A  curvatura  intrínseca  da  camada  cortical  não  possibilita  que este  tipo  de  transformações
seja  realizável  sem  algum  tipo  de  distorção  métrica/topológica.  De  modo  a minimizar a
distorção na superfície, esta é coberta com um molde rendilhado de alta precisão que capta as
Figura 5.4 – Representação de um hemisfério direito insuflado (a), após a introdução dos cortes (b) e
planificado  (c). Zonas  claras  representam  circunvoluções  enquanto  zonas  escuras  indicam  sulcos. (a
– vista lateral, b – vista medial).
Figura 5.3 – Planos de corte numa estrutura composta apenas por voxeis de matéria branca [adapt.
## 23].

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 21

suas  propriedades  métricas  e  topológicas. A  função  de  energia  que  é  responsável  por  esta
minimização das distorções é dada por:
## 푱
## 푑
## =
## 1
## 4푉
## (푑
## 푖푛
## 푡
## −푑
## 푖푛
## 0
## )
## 2
## 푛∈푁(푖)
## ,푑
## 푖푛
## 푡
## 푉
## 푖=1
## =

x
## 푖
## 푡
## −x
## 푛
## 푡

## (5.3)
onde 푉 é o número total de vértices, 푡 é o número de iterações, x
## 푖
## 푡
é a posição do vértice 푖 na
iteração 푡, 푑
## 푖푛
## 0
é  a  distância  entre  os  vértices 푖 e 푛 na  superfície  cortical  original  antes  da
transformação e 푁(푖) é o conjunto de vértices na vizinhança do vértice 푖 [27].
Para  além  da  minimização  das  distorções,  o  processo  de insuflação tem  por  base  uma
força que  suaviza  a  superfície,  sendo  a forma  desejada dada  pela minimização  da seguinte
função de energia:
## 푱
## 푆
## =
## 1
## 2푉


x
## 푖
## −x
## 푛

## 2
## 푛∈푁
## 1
## (푖)
## 푉
## 푖=1
## +휆
## 푑
## 푱
## 푑
## (5.4)
onde 푁
## 1
indica  o  conjunto  de  vértices  na  vizinhança  de  cada  vértice, 푱
## 푑
é como  definido  na
equação 5.3 e 휆
## 푑
define a importância relativa do termo de minimização das distorções [27].
De modo a planificar um hemisfério cortical com o mínimo de distorção, é realizado um
conjunto de cortes na região medial da superfície insuflada: um em redor do corpo caloso para
remover todas as estruturas inferiores, um na parte inferior da fissura calcarina, um conjunto
de  cortes  radiais  igualmente  espaçados e  ainda um  corte  orientado em  torno  da  extremidade
anterior  do  lobo  temporal (figura 5.4 b), eliminando  assim  a  maior  parte  da  curvatura
intrínseca da superfície e preservando a topologia da região lateral [27].
Uma  vez  realizados  os  cortes,  a  superfície  resultante  é  projectada  num  plano,  sendo  este
um  processo  iterativo  realizado  com  recurso  a  vectores  de  desdobramento  orientados  em
cinco direcções diferentes (figura 5.4 b). Esta transformação segue uma função de energia que
penaliza a diminuição da área ocupada por cada triângulo do molde rendilhado:
## 푱
## 푎
## =
## 1
## 2푇
## 푃

## 퐴
## 푖
## 푡

## 퐴
## 푖
## 푡
## −퐴
## 푖
## 0

## 2
## ,푃

## 퐴
## 푖
## 푡

## =
## 1,퐴
## 푖
## 푡
## ≤0
## 0,             푐.푐.

## 푇
## 푖=1
## (5.5)
em  que 푇 é o  número  de  triângulos  do  molde  e 퐴
## 푖
## 0
e 퐴
## 푖
## 푡
representam  a  área  do  triângulo 푖 na
superfície cortical original e após 푡 iterações, respectivamente [26,27].

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 22

Apesar de terem sido realizados os cortes, o resultado obtido é uma superfície severamente
distorcida,  especialmente  nas  regiões  fronteiras  do  local  onde  os  cortes  foram  realizados.
Porém, este processo de planificação, bem como o de insuflação, foi realizado com a condição
de manter a área de superfície constante relativamente à superfície inicial (antes do processo
de insuflação), fazendo ainda referência aos vértices e arestas do molde rendilhado que cobre
as superfícies. Assim, com base nesta informação e através da utilização da função de energia
## 푱
## 푑
, a fase final do processo de planificação consiste na correcção da distorção [26].

## 5.3 – IMAGEM FUNCIONAL POR RESSONÂNCIA MAGNÉTICA

A imagem funcional por ressonância magnética é a área da IRM cujo objectivo consiste na
detecção das regiões onde existe aumento de actividade neuronal decorrente da realização de
tarefas específicas ou de distúrbios neurológicos, como a epilepsia [28].
Existem  várias técnicas para detectar  o  aumento  metabólico associado à actividade
neuronal  através  da  IRM,  entre  eles: o  Método  de  Contraste  Dependente  do  Nível  de
Oxigenação Sanguínea (BOLD), medição do fluxo sanguíneo ou perfusão (por marcação dos
spins arteriais), medição do volume ou oxigenação sanguíneos e consumo de oxigénio [28].
No  âmbito  deste  projecto,  a  actividade  neuronal  foi  detectada  com  recurso  à  técnica
BOLD, pelo que será esta a técnica enfatizada neste contexto.

5.3.1 – Resposta hemodinâmica e metabólica à actividade neuronal

Estudos  anteriores  concluíram  que  o  consumo  local  de  glucose  aumenta  de  uma forma
acentuada  quando  ocorre  activação  neuronal.  Por  sua  vez,  a  glucose  é  preferencialmente
degradada  na  presença  de  oxigénio,  o  qual  é  fornecido  pelas  moléculas  de  oxihemoglobina
presentes  nos  glóbulos  vermelhos  que  percorrem  os  capilares  sanguíneos.  Deste  modo,  este
fenómeno  é acompanhado por um aumento do fluxo sanguíneo nas regiões onde  a activação
teve  lugar  (rCBF
## 9
),  bem  como  um  aumento do  volume  sanguíneo  nessas  regiões  (rCBV
## 10
## )
## [28,29].
A partir da equação do princípio de Fick aplicada ao cérebro podemos obter uma expressão
para o aumento da taxa metabólica de consumo de oxigénio:

## 9
Do inglês: regional cerebral blood flow
## 10
Do inglês: regional cerebral blood volume

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 23

## ∆퐶푀푅푂
## 2
## 퐶푀푅푂
## 2
## =
## ∆퐶퐵퐹
## 퐶퐵퐹
## −
## ∆푌
## 푉
## (1−푌
## 푉
## )
## =
## ∆퐶퐵퐹
## 퐶퐵퐹
## +
## ∆푂퐸퐹
## 푂퐸퐹
## (5.6)
onde 퐶푀푅푂
## 2
é a taxa metabólica de consumo de oxigénio, 퐶퐵퐹 é o fluxo sanguíneo cerebral,
## 푌
## 푉
é  o  valor  de  saturação  de  oxigénio  para  o  sangue  venoso  e 푂퐸퐹 representa  a  fracção  de
extracção de oxigénio [28].
Analisando  a  equação 5.6, constata-se  que,  aquando  da  activação  cerebral,  e  de  algum
modo contra-intuitivamente, a fracção de extracção de oxigénio diminui (i.e. 푌
## 푉
aumenta). Isto
ocorre  porque  o  fluxo  de  sangue  afluente  aumenta  mais  do  que  o  necessário,  isto  é,  mais  do
que é requerido pela actividade das células nervosas. De facto, durante a actividade neuronal,
e no local de activação, o nível de oxigenação do sangue venoso aumenta [28-30].

5.3.2 – A técnica BOLD IfRM

A  origem  do  sinal  BOLD  IfRM  reside  no  facto  da  hemoglobina  possuir  diferentes
propriedades  magnéticas  consoante  se encontra  no  estado  oxigenado  (oxihemoglobina)  ou
desoxigenado    (desoxihemoglobina).    Pauling    e    Coryell    (1936)    descobriram    que    a
desoxihemoglobina   é   ligeiramente   paramagnética   relativamente   ao   tecido   circundante,
enquanto  a  oxihemoglobina  é  isomagnética em  relação  ao  tecido  circundante.  Assim,  o
aumento  da  concentração  de  oxihemoglobina  aquando  do  aumento  da  actividade  neuronal
contribui  para  a  homogeneidade do  campo magnético  no  tecido  circundante, uma  vez  que,
sendo isomagnética, provoca uma distorção do campo magnético mínima ou nula. Como tal, e
de acordo com a equação 5.2, o tempo de relaxação T
## 2
## *
aumenta e, consequentemente, o sinal
medido  também. Em  contrapartida, no  caso  em  que  a  desoxihemoglobina  aumenta,  dá-se  o
processo inverso, visto que, por ser paramagnética, concentra as linhas de campo, provocando
um  aumento  da  intensidade  do  campo  magnético.  Este  fenómeno  faz  com  que  o  campo  se
torne mais inomogéneo e, como tal, T
## 2
## *
diminui mais rapidamente, o que implica que o sinal
medido  é  menor.  O  sinal  BOLD  IfRM  tem,  por  sua  vez,  uma  contribuição  das  moléculas  de
água que estão no próprio sangue (intravasculares) e uma contribuição das moléculas de água
que se situam no espaço tecidular que rodeia os vasos (extravasculares) [28,29].
A  resposta  hemodinâmica  que  as  técnicas  de IfRM  medem  ocorre  a  uma  escala  temporal
muito  mais  lenta  que  a  actividade  eléctrica  que  lhe  subjaz  (segundos  contra  milissegundos).
Não  obstante,  é  possível  extrair  informação  da  dinâmica  temporal  relativa  à  resposta
hemodinâmica  causada  pelas  alterações  na  actividade  neuronal.  A  figura 5.5 mostra  uma

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 24

representação  esquemática  da  resposta  hemodinâmica  a um  período  de  estimulação  neuronal
curto. Nesta  figura  observa-se  que,  em  primeiro  lugar,  imediatamente  após  a actividade
eléctrica  ter  começado,  existe  uma breve depressão  inicial na  intensidade  do  sinal  BOLD
(apenas  observável  com  B  3T). Este  efeito  é  o  resultado  de  um  aumento  na  extracção  de
oxigénio,  resultante  de  um  aumento  do metabolismo,  anterior  ao  incremento do  fluxo
sanguíneo,    provocando    um    grau de    desoxigenação    sanguínea mais    acentuado.
Subsequentemente,  o  rCBF  aumenta  e  o  sangue  torna-se  hiperoxigenado,  levando  a  uma
resposta positiva do sinal BOLD (alteração de 3-5 %
## 11
do sinal a 1.5T), cujo pico sucede 5 a
8 segundos após o início do estímulo. Finalmente, após o estímulo cessar, dá-se o retorno da
resposta  BOLD  à  linha  de  base,  frequentemente  acompanhada  por  uma  depressão  pós-
estímulo.  Esta  depressão  está documentada ser  causada  por uma  extracção  de  oxigénio
elevada após o fluxo sanguíneo ter retornado ao seu nível de base, solicitada para reabastecer
as reservas de oxigénio dos tecidos agora vazias [28,30].
Enquanto  as  respostas  positivas  reflectem  provavelmente  um  aumento  na  actividade
neuronal  e  demanda de  energia,  existem  também  respostas  negativas  (desactivações), cujas
bases   neurofisiológicas   são   mais   difíceis   de   explicar.   Quatro   mecanismos   podem   ser
considerados  na  explicação  deste  fenómeno:  1)  uma  redução  relativa  no  CBF  nas  zonas
desactivadas  é  causada  por  um  fenómeno  de  “roubo”  de  fluxo,  secundário  ao  aumento  do
CBF nas regiões activadas positivamente e causado por este. Contudo, isto apenas explica um

## 11
Para sequências de Eco de Gradiente, a sensibilidade do sinal BOLD é superior relativamente às sequências de
Eco de Spin, cuja sensibilidade é 0.5 %, embora o seu sinal seja mais contaminado por efeitos externos, como a
sensibilidade às inomogeneidades do campo magnético.
Figura 5.5 – Diagrama  esquemático  do  sinal
BOLD, bem como do CBF e CBV em resposta a
um   breve   período   de   estimulação   neuronal
(como numa crise epiléptica) [adapt. 28].

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 25

decréscimo em zonas que são adjacentes a regiões em que há aumento do sinal BOLD. 2) O
aumento da actividade neuronal pode não ser acompanhado por um aumento do rCBF devido
a,  por  exemplo,  condições  patológicas  envolvendo  a  circulação  cerebral,  implicando  assim
uma  diminuição  no  sinal  BOLD.  3)  Regiões  de  desactivação  podem  corresponder  a  um
decréscimo na actividade sináptica causada por supressão ou limitação de estímulos aferentes
ou  devido  a  fibras  nervosas  lesadas.  4)  Inibição  GABAérgica
## 12
resulta  num  profundo
decréscimo da actividade neuronal e a um custo de energia bastante reduzido, o que resulta na
diminuição das exigências energéticas [7,31].
Deste  modo,  a  técnica  BOLD  consiste  num  método  indirecto  de  detecção  da  actividade
neuronal  através  dos  seus  efeitos  secundários,  como  a  variação  do  fluxo  e  do  volume
sanguíneos regionais, utilizando as propriedades magnéticas da hemoglobina como agente de
contraste molecular intravascular.

5.3.3 – Características da IfRM

A   imagem   funcional   por   ressonância   magnética   tem   vindo   a   ser   utilizada   para   a
visualização  da  função  cerebral  humana  com  uma  resolução  espacial  relativamente  elevada.
Na maioria dos estudos de IfRM em humanos, a resolução espacial varia entre 3 e 5 mm, com
espessuras de corte entre 3 e 10mm. Apesar de a IfRM não possuir uma resolução espacial tão
boa  quanto  a  IRM,  devido  ao  uso  de  técnicas  de  aquisição  rápida  de  imagens,  ela  é  contudo
melhor que outras técnicas de imagem funcional, como a PET e a SPECT, que têm resoluções
espaçais de 4-8 mm e <1-2 cm para sistemas clínicos, respectivamente [32,33].
Como  acontece  com  todas  as  técnicas,  também  a  IfRM  tem  as  suas  limitações.  Uma  das
mais  importantes  consiste  na  sua  pobre resolução  temporal, uma  vez  que  é limitada  pela
natureza da resposta hemodinâmica. Em adição, o efeito BOLD é reduzido e, como tal, a sua
sensibilidade é limitada, pelo que exames deste género necessitam de uma grande quantidade
de imagens com respostas neuronais. Existem ainda outros factores que constituem fontes de
erro  quando  se  pretende fazer  comparações  quantitativas:  perda  e  distorção  de  sinal  em
interfaces  de  diferente  susceptibilidade  magnética,  movimentos  da  cabeça,  volume  parcial  e
fontes de ruído instáveis devidas à fisiologia basal [28,29].


## 12
GABA  (ácido  gama-aminobutírico)  é  o  principal  neurotransmissor  inibitório  do  sistema  nervoso  central  dos
mamíferos.

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 26

5.3.4 – Paradigma de activação

O  planeamento  experimental  envolve  a  formulação  de  hipóteses  acerca  de  quais  são  os
processos  desempenhados  pelo  cérebro  na  execução  da  tarefa  administrada. Deste  modo,  é
criado  um protocolo  de  estimulação de  tal  forma  que  as  funções  cerebrais  de  interesse  são
normalmente evidenciadas de  uma  forma  ordenada  e  temporalmente  definida.  Na  sua  forma
mais simples, os paradigmas são organizados em dois blocos alternados, em que um é relativo
às funções de interesse e o outro serve de controlo [28]. Todavia, no caso da epilepsia, em que
os estímulos se caracterizam por serem irregulares e de curta duração, o modelo de blocos não
é o protocolo indicado. É, contudo, possível obter a informação temporal relativa à ocorrência
de actividade neuronal através da aquisição de um EEG, aquando da realização do exame de
IfRM (figura  5.6).  A  partir  desta  informação,  é  possível  a  definição  do  paradigma  de
activação associado à ocorrência de actividade epiléptica, como se pode ver na figura 5.7.



















Figura 5.7 – Protocolo de estimulação com base num EEG simultâneo com um exame de IfRM.
## Volumes
Figura 5.6 – Aquisição  de um  EEG,  simultâneo  com  IfRM,  em  que  se  registou  a  ocorrência
de actividade epiléptica interictal (assinalada pela oval vermelha).

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 27

5.3.5 – Aquisição de imagens funcionais: imagens eco-planares

Neste  estudo,  as  imagens  funcionais  BOLD  foram  adquiridas  recorrendo  ao  uso  de
imagens  eco-planares  (EPI
## 13
). Este  é  um  método  de  aquisição  frequentemente  utilizado
devido à sua elevada rapidez e boa relação sinal-ruído [28]. Na sua variante mais rápida, toda
a  informação  necessária  para  preencher  todas  as  linhas  do  espaço k
## 14
é  obtida  num  único
período TR. De forma a alcançar este objectivo, são gerados múltiplos ecos (p. ex. 64), cada
um codificado com uma fase diferente, de forma a preencher o espaço k com esse número de
linhas.  É  ainda  necessário  que  os  gradientes  de  codificação  de  fase  e  frequência  liguem  e
desliguem  rapidamente,  e  que  o  gradiente  de  codificação  de  frequência  mude  de  direcção  o
mais rápido possível [17,20]. Uma imagem completa pode assim ser obtida em cerca de 30-50
ms, sendo possível a aquisição de um volume em 2-4 segundos [34].

5.3.6 – Pré-processamento da informação funcional

O pré-processamento do exame funcional é um passo importante para aumentar o poder da
análise   estatística.   Neste   projecto,   todas   as   sequências de   aquisição funcionais foram
corrigidas   para   os   mesmos   parâmetros: correcção   temporal   dos   cortes, correcção   do
movimento 3D e filtragem temporal.
5.3.6.1 – Correcção temporal dos cortes
Um  volume  é  considerado  como a  informação  recolhida  num  dado  instante  temporal.
Contudo,  os cortes  de  um  volume  funcional  são  obtidos  sequencialmente  em  imagens  EPI.
Para  que  a  análise  estatística  não  seja  comprometida,  é  então  desejável  pré-processar  a
informação de tal modo que todos os cortes do mesmo volume pareçam  ter sido medidos no
mesmo instante temporal. Para tal, os cortes são deslocados no tempo de modo a condizerem
com um instante de referência, por exemplo o primeiro corte ou o corte do meio [35].
5.3.6.2 – Correcção do movimento 3D
A  correcção  do  movimento  consiste  em  detectar  e inverter  os  movimentos  da  cabeça
durante a aquisição. Para tal, um volume da sequência é escolhido, ao qual todos os restantes
se vão alinhar por movimentos de rotação e translação ao longo dos eixos x, y e z [35].

## 13
Do inglês: echo planar imaging
## 14
O espaço k é uma matriz bidimensional (k
x
, k
y
) onde cada valor de k
x
corresponde a uma frequência diferente e
cada valor de k
y
corresponde a uma amplitude diferente no gradiente de codificação de fase.

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 28

5.3.6.3 – Filtragem temporal
Devido ao ruído físico e fisiológico, os percursos temporais dos voxeis são frequentemente
não-estacionários  e  exibem  tendências  ou  desvios  de  sinal. Uma  vez  que  esses  desvios
descrevem  mudanças  lentas  de  sinal,  eles  são  removidos  através  de  análise  de  Fourier,
utilizando um filtro passa-alto [35].

5.3.7 – Co-registo da informação funcional e anatómica

Após  o  pré-processamento  da  informação  funcional,  é  necessário  alinhar os  cortes  do
exame   funcional   com   a   informação   anatómica   tridimensional.   Este   co-registo   permite
relacionar   a   actividade neuronal mais   facilmente   com   as   regiões   anatómicas   que   lhe
correspondem [26].
O  procedimento  consiste,  numa  abordagem  inicial,  em  alinhar  os  dois  tipos  de  imagens
com base na informação posicional presente nos headers, ficando estas orientadas no mesmo
sentido.  Em  seguida,  realiza-se  o  alinhamento  fino,  que  consiste  em  encontrar  a  melhor
posição de alinhamento com base nos valores de intensidade dos dois tipos de imagens [26].

5.3.8 – Análise estatística: Modelo Linear Geral

De modo a detectar fidedignamente os efeitos provocados pelos estímulos, é realizada uma
apropriada  análise  estatística  dos  resultados.  A  ferramenta nuclear  de  análise estatística  em
IfRM é  o  Modelo  Linear  Geral  (MLG). O  MLG  tem  o  objectivo  de  explicar  ou  prever  a
variação de uma variável dependente em termos de uma combinação linear (soma ponderada)
de várias funções de referência. A variável dependente corresponde  ao percurso temporal de
um  voxel observado  no  exame  de  IfRM, enquanto  as  funções  de  referência,  ou preditores,
correspondem  aos  percursos  temporais  das  respostas  funcionais  esperadas  (idealizadas)  para
diferentes condições do paradigma experimental. Um conjunto de preditores específico forma
a matriz de  plano  experimental,  também  chamada modelo (figura 5.8). O  percurso  temporal
de  um preditor é  normalmente  obtido  pela  convolução  de um  percurso  temporal  em  blocos,
que  tem  por  base  um  protocolo  de  estimulação, com  uma  função  de  resposta  hemodinâmica
(FRH). O MLG ajusta o modelo à informação do exame, independentemente para cada voxel,
associando a cada preditor X um coeficiente beta b, quantificando, deste modo, a contribuição
de  cada preditor na  predição do  percurso  temporal  da variável  dependente y. O  percurso

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 29

temporal de um voxel y é assim modelado como a soma dos preditores, cada um multiplicado
pelo  seu  peso  beta  associado.  Uma  vez  que,  devido  às  flutuações  de  ruído,  esta  combinação
linear não explica perfeitamente o resultado obtido, um valor de erro e terá que ser adicionado
ao sistema de equações do MLG [35]:
## 풚=푿풃+풆                                                                 (5.7)
Os  valores  beta  obtidos  são  comparados  entre si através  de  uma estatística t (ver  anexo),
resultando  num  valor  estatístico em  cada  voxel. Os  valores  estatísticos  de  todos  os  voxeis
formam  um  mapa  estatístico  tridimensional,  cujas  zonas  de  activação/desactivação  são
apresentadas na forma de clusters, isto é, em agrupamentos de voxeis contíguos (figura 5.9).
Como forma de evitar que voxeis não activos sejam declarados como significantes, os mapas
estatísticos possuem um limiar apropriado, ao qual está associado um valor probabilístico de
erro aceite  pela  comunidade  científica  (푝<0.05) (ver  anexo). Ao  mesmo  tempo,  e  como
forma  de  quantificar  a  inter-relação  dos  valores  previstos  pelo  modelo  com  os  valores
observados,  é  realizada  uma  análise  de  correlação,  resultando  num  valor  de  coeficiente  de
correlação múltipla, R, com valores entre 0 (correlação nula) e 1 (toda a variação dos valores
observados  é  explicada  pelo modelo) (ver  anexo).  Aos  voxeis  que  apresentam  um  valor
estatístico  supra-limiar  é-lhes  atribuída  uma  codificação  em  cor,  de  acordo  com  a  sua
magnitude  de  resposta,  isto  é,  com  o  grau  de  correlação.  Assim,  a  uma  maior  correlação
correspondem as cores amarela (activação) e verde (desactivação), enquanto para correlações
menores têm-se colorações laranja (activação) e azul (desactivação) [26,35].
Figura 5.8 – Apresentação gráfica de um MLG, em que o modelo consiste em três preditores [adapt.
## 35].

Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 30

O   mapa   de   activações   da   representação   plana   (figura   5.9 b)   é   obtido   através   do
estabelecimento  de  um  elo  de  ligação  entre  a  representação  tridimensional  e  a  representação
planificada dos hemisférios, pelo que a cada vértice do molde rendilhado da representação 3D
existe uma localização correspondente na superfície plana [26].

5.3.9 – Aquisição simultânea de EEG/IfRM

De modo a realizar a cirurgia da epilepsia, a zona epileptogénica tem que ser previamente e
precisamente  identificada,  uma  vez  que,  na  sua  vizinhança, se  encontram  frequentemente
regiões  cerebrais  responsáveis  por  processos  de  grande  importância,  como  a  linguagem  e  a
memória.  Neste  sentido,  a  aquisição  simultânea  de  EEG/IfRM  abre  a  oportunidade  de
descobrir  as  regiões  cerebrais  que  mostram  alterações  no sinal  de  IfRM  em  resposta  às
alterações epilépticas neuronais observadas no EEG, associando a elevada resolução temporal
do EEG à boa resolução espacial da IfRM.
Uma vez que se trata de uma aquisição simultânea, é necessário registar o EEG enquanto o
paciente  está  no  aparelho  de  RM. Dada  a  intensidade  do  campo  magnético  no equipamento
(1.5 e 3 T), este processo levanta várias questões relacionadas com a qualidade de imagem e
do sinal de  EEG, uma vez que é muito sensível  à interferência  electromagnética externa. De
igual modo, a segurança do paciente também é um assunto a considerar [7,36].
Os  eléctrodos  de  EEG  são  metálicos  e,  como  tal,  a  rápida  alternância  dos  campos
magnéticos pode  induzir  uma  corrente  que  pode  levar  ao  aquecimento  dos  eléctrodos  e,
consequentemente, a queimaduras localizadas no escalpe do paciente. Este problema pode ser
superado através do uso de eléctrodos e fios condutores não-ferrosos, resistências limitadoras
de corrente e evitar laçadas de corrente. De igual modo, a selecção cuidadosa dos condutores
e o escudo de RF do equipamento ajudam a minimizar a interferência das imagens [7].
Figura  5.9 – Mapa  estatístico  evidenciando activações  positivas  e  negativas  numa  representação
3D (a) e na correspondente planificação (b).


Capítulo 5 – Imagem por Ressonância Magnética  Miguel Gonçalves
## 31

O  principal  problema  reside  na  qualidade  do  EEG  no  interior  do equipamento,  que  é
reduzida  em  relação  ao EEG  de  alta  resolução.  As  correntes  induzidas  nos  eléctrodos  e  fios
condutores  resultam  em  artefactos  que  podem  ser de  ordem  50  vezes  superior  à  do  sinal  de
EEG – artefactos de gradiente. Este efeito pode ser evitado se a aquisição do sinal de RM se
der apenas após a observação de um evento de interesse no EEG, tirando partido do atraso da
resposta  hemodinâmica (EEG-triggered). Existe  também  outro  método  para  remoção  dos
artefactos  de  gradiente  que  consiste  na  estimação  e  subtracção  do  artefacto,  seguido  de
eliminação  de  ruído. Há ainda  outro  artefacto  que  é  referido  como  o  artefacto  de  pulso
cardíaco ou balistocardiograma.  Este  consiste  em  desvios  que  se  seguem  a cada  batida
cardíaca  e  possivelmente  têm  a  sua  origem  em  pequenos  movimentos  da  cabeça  ou  dos
eléctrodos  devidos  ao  rápido  movimento  do  sangue  nas  artérias.  Este  artefacto  pode  ser
removido pelo  cálculo  da  média  e  posterior  subtracção,  filtragem  adaptativa,  filtragem
wavelet ou por análise de componentes independentes [7,36].

## Capítulo 6 – Metodologia Experimental  Miguel Gonçalves
## 32

## C A P Í TUL O  6 – M E TO DO L O G I A   E X P E R I M E NTA L

Neste capítulo, são descritas as características dos pacientes, bem como o procedimento  e
parâmetros  de  aquisição  dos  exames  de  EEG  e  IfRM. É  ainda  indicado  o  modo como  o
processamento dos dados foi efectuado no programa informático.

## 6.1 – CASOS CLÍNICOS

Neste  projecto  foram estudados  seis pacientes com  epilepsia refractária  à  medicação
(tabela 6.1), seleccionados de um grupo de pacientes da clínica de Ressonância Magnética de
Caselas. Os   pacientes   ou, no   caso   de   estes serem   menores   de   idade,   os   respectivos
responsáveis  familiares, deram  a  sua  aprovação  para  a  execução  e  apresentação  destes
estudos.

Tabela 6.1 – Lesões e tipos de crises epilépticas dos pacientes.
## Paciente
## GM AP IL JB LR JP
Tipo de
crise
## Crises
parciais
complexas
## Crises
parciais
simples
motoras
Crises parciais
complexas
## Crises
parciais
complexas
Crises com
instabilidade
postural
## Crises
parciais
complexas
e sensitivas
Tipo de
lesão
Sem lesão
na RM
## Lesão
frontal
superior
esquerda
## Lesão
occipitalinterna
esquerda
## Lesão
displásica
da
## Amígdala
esquerda
Sem lesão
na RM
## Lesão
hipocampo
direito


## 6.2 – AQUISIÇÃO SIMULTÂNEA DE EEG/IFRM

Para cada paciente foi obtido um EEG com 21 canais na superfície do escalpe, segundo o
sistema 10/20, à frequência de amostragem de 1000 Hz, durante 10 a 34 minutos, utilizando-
se uma touca para o efeito. Durante a aquisição, a cabeça foi imobilizada com fitas de fixação.
Foi  ainda aplicado um  filtro  passa-baixo  a  70  Hz. Registou-se também um concomitante

## Capítulo 6 – Metodologia Experimental  Miguel Gonçalves
## 33

electrocardiograma  com  2  canais  localizados  no  peito. O  sistema  utilizado  foi  o Maglink
System for Neuroscan, El Paso, TX, U.S.A., certificado para utilização simultânea no interior
de  um  equipamento  de  RM. Utilizaram-se eléctrodos  de  AgCl, cuja  ligação  ao  amplificador
foi efectuada por fios condutores de fibra de carbono.
Os artefactos inerentes a este tipo de aquisição foram removidos com recurso ao programa
informático Scan 4.3.3 (Neuroscan).
Da análise do EEG corrigido resulta o paradigma de activação para o exame funcional de
RM. Assim, aos instantes em que se registou um aumento na actividade neuronal (activação)
foi  associado  o  valor  1  e  aos  restantes  períodos  (inactivação)  foi-lhes  associado  o  valor  0,
sendo este processo levado a cabo pelo Dr. Alberto Leal, neurofisiologista clínico.
A sala de RM encontra-se protegida por uma gaiola de Faraday, sendo a passagem dos fios
condutores  para  o  exterior  realizada  através  de  um  filtro  de  radiofrequências  inserido  no
painel  de  interface  da  sala  de  RM  com  a  sala  onde  é  realizado  o processamento  de  dados.
Deste modo, é  garantido o  isolamento da  sala  de  RM  e  evita-se a  contaminação  da mesma
com ondas electromagnéticas.
Ao mesmo  tempo  que  se  efectuava  o  registo  do  EEG, eram  adquiridas  as  imagens
funcionais.  Para  tal,  utilizou-se  um equipamento  de  1.5T GE  CVi/NVi com  recurso  a
sequências de  aquisição EPI  de  eco  de  gradiente. Para  cada  paciente,  esta  sequência  de
aquisição  foi  repetida  várias  vezes  (tabela  6.2),  obtendo-se  vários  conjuntos  de  imagens
funcionais do cérebro, também referidas como volumes funcionais, pelo que daqui em diante
o termo “sequência” será utilizado no sentido de referir um conjunto de volumes funcionais.
Neste  trabalho,  as  sequências  foram  adquiridas  em  blocos  de  cerca  de  340  segundos,  sendo
este valor variável de paciente para paciente (tabela 6.2).
Foi ainda realizado um exame anatómico de alta resolução com ponderação em T
## 1
a cada
um  dos  pacientes, utilizando  uma  sequência  de  aquisição  rápida – SPGR
## 15
, com o  objectivo
de evidenciar com  maior  detalhe a  região  anatómica  onde o  aumento ou  diminuição da
actividade neuronal teve efeito.




## 15
Do inglês: Spoiled Gradient Recovery

## Capítulo 6 – Metodologia Experimental  Miguel Gonçalves
## 34

Tabela 6.2 – Parâmetros de aquisição das imagens funcionais e anatómicas.
## Paciente
## GM AP IL JB LR JP
## Imagens Funcionais
Tempo de aquisição
## /sequência (s)
## 300 341 341 341 346 341
N.º sequências
## 2 6 3 4 4 1
N.º volumes/sequência
## 100 150 150 150 140 150
N.º cortes/volume
## 16 24 24 24 26 24
Resolução espacial (planar)
## (mm)
## 3.75 3.75 3.75 3.75 3.75 3.75
Espessura de corte (mm)
## 7 5 5 5 5 5
Espaçamento entre cortes
## (mm)
## 0 0 0 0 0 0
Campo de visão (cmcm)
## 2424 2424 2424 2424 2424 2424
## Matriz 6464 6464 6464 6464 6464 6464
TR (ms)
## 3000 2275 2275 2275 2475 2275
TE (ms)
## 30 50 50 50 50 50
Pulso de RF
## 90 90 90 90 90 90
## Imagens Anatómicas
Resolução planar (mm)
## 0.94 0.94 0.94 0.94 0.94 1.02
Espessura de corte (mm)
## 1.2 1.2 1.2 1.2 1.2 1.6
## Matriz
## 256256 256256 256256 256256 256256 256256
TE (ms)
## 3 4 4 4 4 3
TR (ms)
## 7.2 9.2 9.2 9.2 9.2 7.0
Pulso de RF
## 20º 20º 20º 20º 20º 20º


## 6.3 – PROCESSAMENTO DE DADOS

Todo   o   processamento   de   dados   foi   realizado   no   programa   BrainVoyager
## TM
## QX
1.10.2.1198 com  imagens  em  formato de  comunicação  de  imagens  digitais  em  medicina
(DICOM) e foi dividido em três fases.
A primeira fase tem o objectivo de verificar quais as regiões cerebrais que têm activação,
bem  como  o  tipo  de  activação  e  a sua  intensidade  relativa,  para  a  sequência com  resultados

## Capítulo 6 – Metodologia Experimental  Miguel Gonçalves
## 35

clinicamente  mais  relevantes de  cada  paciente, das  várias  sequências  obtidas, previamente
determinada pelo Dr. Alberto Leal.
A  metodologia  utilizada  nesta  fase  divide-se  em  três  partes. A  primeira  parte  consiste na
análise   das   imagens   funcionais   no   espaço   original,   isto   é,   considerando   os   cortes
individualizados.  Assim,  após  a  importação  das  imagens  para  o  programa,  procedeu-se  à
criação do protocolo de estimulação a partir da informação do EEG. Seguidamente, realizou-
se  o  pré-processamento  das  imagens  para  a  correcção  temporal  dos  cortes,  com  interpolação
cubic  spline,  correcção  do  movimento  3D,  através  de  uma  interpolação trilinear/sinc,  e
filtragem  temporal,  com  um  filtro  passa-alto.  Finalmente,  após  a  correcção  das  imagens,
procedeu-se à análise estatística com o MLG.
Na  segunda  parte  foi  realizado  o  processamento da  informação  anatómica  no  espaço
tridimensional. O primeiro passo consistiu em realizar a correcção de inomogeneidade para a
substância   branca.   Posteriormente,   realizou-se   o   co-registo   da   informação   funcional   e
anatómica,  seguindo-se  a  transformação  da  informação  anatómica  e  funcional  para  o  espaço
## Talairach.
Na  terceira  e  última  parte  foi  realizada  a  segmentação  e  reconstrução  de  ambos  os
hemisférios cerebrais ao  longo da fronteira matéria cinzenta/branca, com remoção do crânio,
e,  para  cada  hemisfério  resultante,  realizou-se  a  insuflação  e  subsequente  alisamento  da
superfície representativa da camada cortical. A cada uma destas representações foram depois
sobrepostos os mapas estatísticos.
A segunda  fase consiste em  reconhecer  se  as  regiões  cerebrais  que  evidenciam  resposta
são as  mesmas  e  se  estas são do  mesmo  tipo  em  diferentes  sequências  do  mesmo  paciente
(cada uma com um paradigma de activação próprio).
A  metodologia  adoptada  foi  igual  à  da  fase  anterior,  tantas  vezes  repetida  quantas  as
sequências de cada paciente (tabela 6.2).
Por  fim,  a terceira fase consiste  numa   abordagem  de   análise  múltipla das  várias
sequências  em  simultâneo,  agrupando-as  num  só  estudo,  com  o  objectivo  de  determinar  as
regiões  que  apresentam  respostas  BOLD  mais  significantes  numa  perspectiva  de  integração
global.



## Capítulo 6 – Metodologia Experimental  Miguel Gonçalves
## 36

## 6.4 – PARÂMETROS DA FUNÇÃO DE RESPOSTA HEMODINÂMICA

A  função  de  resposta  hemodinâmica  relativa  aos  picos  epilépticos  de  actividade  neuronal
não  é  bem  conhecida  e  revela  diferenças  entre  pacientes,  entre  diferentes  regiões  cerebrais  e
entre sessões do mesmo paciente [7,31]. Por esta razão é costume utilizar-se várias FRH com
picos  em  diferentes  instantes  temporais,  isto  é,  com  diferentes  intervalos  de  tempo  até  a
resposta hemodinâmica atingir o seu máximo a partir do momento em que ocorre o aumento
da  actividade neuronal.  Bagshaw  et  al. [37]  utilizaram várias  FRHs  com  picos  desde  três  a
nove segundos de atraso, em oposição à FRH padrão de Glover [38], cujo máximo é aos 5.4 s,
e obteve um aumento na resposta BOLD de 45% para 62.5%.
Assim, após uma abordagem inicial em que foi utilizada apenas uma FRH com o máximo
aos  5  s,  foi  adoptada  uma  estratégia  semelhante  à  praticada  por  Kobayashi  et  al. [31,39]  e
Bagshaw  et  al. [40],  em  que,  para  cada  sequência,  foram  criados  quatro  mapas  estatísticos
individuais, cujas  funções  de  resposta  hemodinâmica  tinham  máximos  aos  3,  5,  7  e  9
segundos.  Os  mapas  finais  foram  obtidos  através  da  sobreposição   dos  quatro  mapas,
considerando o mesmo limiar para todos. Deste modo, para cada estudo, foi criado um mapa
estatístico  com  o  valor  máximo ou  mínimo  possível em  cada  voxel,  caso  se  trate  de  uma
activação ou de uma desactivação, respectivamente.
Para os restantes parâmetros da função de resposta hemodinâmica, utilizaram-se os valores
pré-estabelecidos  pelo  programa,  sendo  estes  iguais  para  todas  as  sequências  e  mapas:  a  sua
forma  foi  modelada  através  de  uma dupla  função  gama  e  o  pico  da  depressão  pós-estímulo
tem  lugar  15  s  após  o  início  da  resposta  hemodinâmica,  tendo  esta  a  duração  total  de  31
segundos.



## Capítulo 7 – Resultados  Miguel Gonçalves
## 37

## C A P Í TUL O  7 – R E S UL TA DO S

Neste  capítulo, serão  apresentados  os  resultados  obtidos através  da  metodologia  aplicada
no processamento de dados.
A abordagem utilizada para definição do limiar consistiu em apresentar apenas os clusters
mais  significativos,  uma  vez  que  a  sua  localização  corresponderá  às  regiões  cerebrais  mais
determinantes na resposta aos paroxismos epileptiformes.

## 7.1 – FASE 1 – TIPO, INTENSIDADE E LOCALIZAÇÃO DAS RESPOSTAS

Das várias sequências adquiridas para cada paciente, foi escolhida, pelo Dr. Alberto  Leal,
aquela  com  resultados  clinicamente  mais  relevantes.  Nessa  sequência,  dos  vários clusters
observados,  escolheu-se  aquele  cuja  activação  tinha  maior  significado  estatístico,  de  modo  a
verificar  se  a  correlação  entre  o  modelo  e  o  sinal  da  imagem  funcional  era  boa. Os critérios
para escolha do cluster de activação/desactivação foram o seu tamanho e intensidade.
Nas  imagens  seguintes  mostram-se,  para  cada  paciente,  os  resultados  do  coeficiente  de
correlação múltipla do cluster mais significativo da sequência clinicamente mais relevante de
cada paciente, para os dois hemisférios.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 38

7.1.1 – Paciente 1 - GM


## 푅=0.501





## 푅=0.496


Figura 7.1 – Representações  plana  e  tridimensional  do  hemisfério  esquerdo.  A  região  de  interesse
está delimitada pela linha branca em ambas as representações.
Figura 7.2 – Representações  plana  e  tridimensional  do  hemisfério  direito,  com  a  respectiva  região
de interesse.

## Capítulo 7 – Resultados  Miguel Gonçalves
## 39

7.1.2 – Paciente 2 - AP


## 푅=0.422







## 푅=0.428


Figura 7.3 – Representações  plana  e  tridimensional  do  hemisfério  esquerdo,  com  a  respectiva  região
de interesse.
Figura 7.4 – Representações  plana  e  tridimensional  do  hemisfério  direito,  com  a  respectiva  região
de interesse.

## Capítulo 7 – Resultados  Miguel Gonçalves
## 40

7.1.3 – Paciente 3 - IL


## 푅=0.540






## 푅=0.627


Figura 7.5 – Representações  plana  e  tridimensional  do  hemisfério  esquerdo,  com  a  respectiva  região
de interesse.

Figura 7.6 – Representações  plana  e  tridimensional do  hemisfério  direito,  com  a  respectiva  região
de interesse.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 41

7.1.4 – Paciente 4 - JB


## 푅=0.250





## 푅=0.256


Figura 7.7 – Representações  plana  e  tridimensional  do  hemisfério  esquerdo,  com  a  respectiva  região
de interesse.

Figura 7.8 – Representações  plana  e  tridimensional  do  hemisfério  direito,  com  a  respectiva  zona  de
interesse.

## Capítulo 7 – Resultados  Miguel Gonçalves
## 42

7.1.5 – Paciente 5 - LR


## 푅=0.436






## 푅=0.405



Figura 7.9 – Representações  plana  e  tridimensional  do hemisfério  esquerdo,  com  a  respectiva  região
de interesse.

Figura 7.10 – Representações  plana  e  tridimensional  do  hemisfério  direito,  com  a  respectiva  região
de interesse.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 43

7.1.6 – Paciente 6 - JP


## 푅=0.403






## 푅=0.353


Figura 7.11 – Representações plana e tridimensional  do hemisfério esquerdo, com a respectiva região
de interesse.

Figura 7.12 – Representações plana e  tridimensional  do hemisfério direito, com a respectiva região
de interesse.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 44

## 7.2 – FASE 2 – CONCORDÂNCIA ENTRE REGIÕES COM ALTERAÇÕES BOLD

Nesta  fase,  foram  sobrepostos  numa  mesma  representação  cerebral,  os  resultados  dos
mapas estatísticos de todas as sequências funcionais realizadas para cada  paciente. Com esta
análise,  pretendeu-se observar  se  existe  ou  não  variabilidade  na  localização  das  respostas
hemodinâmicas em  função  da  sequência  utilizada. Verificou-se também  se,  para  a  mesma
região cerebral, existem sobreposições de clusters com tipos de resposta diferentes, isto é, se
ocorreu a sobreposição de activações com desactivações.
As  imagens  que  se  seguem  mostram,  em  representações  planificadas  de  ambos  os
hemisférios de cada paciente, os resultados da sobreposição de todos os clusters significativos
de todas as sequências estudadas para o paciente em questão.
A cada sequência corresponde um conjunto de cores diferente, devidamente indicada, e as
regiões  em que  existe sobreposição de um ou mais clusters estão assinaladas por um  círculo
ou  por  um  conjunto  fechado  de  segmentos  de  recta,  sendo ainda indicado o  número  de
sequências comuns a essa região e o tipo de resposta que cada uma representa através de uma
notação simbólica.

## Capítulo 7 – Resultados  Miguel Gonçalves
## 45

7.2.1 – Paciente 1 - GM


Figura 7.13 – Hemisfério  esquerdo  evidenciando  as respostas para  duas  sequências  diferentes,  bem
como as regiões em comum. As regiões em comum representam zonas de desactivação para ambas as
sequências.
Figura 7.14 – Hemisfério  direito  evidenciando  as respostas para  duas  sequências  diferentes.  Não  se
verificam regiões em comum.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 46

7.2.2 – Paciente 2 - AP


Figura 7.15 – Hemisfério  esquerdo  evidenciando  as respostas para  seis  sequências  diferentes,  bem
como  as  regiões  em  comum.  Todas  as  zonas  comuns  observadas  são  apenas  comuns  a  2  sequências.
Duas  dessas  zonas  representam  desactivação  para  ambas  as  sequências  e  uma  representa  activação
para uma sequência e desactivação para outra.

Figura 7.16 – Hemisfério  direito  evidenciando  as respostas para  seis  sequências  diferentes,  bem
como  as  regiões  em  comum.  Cinco  das  seis  zonas  comuns  detectadas  são  apenas  comuns  a  2
sequências.  Dentro  dessas,  3  representam  desactivação  para  ambas  as  sequências,  1  representa
activação  para  uma  sequência e  desactivação  para  outra  e  1 representa activação  para  ambas  as
sequências. A região comum a 3 sequências representa desactivação para todas.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 47

7.2.3 – Paciente 3 - IL





Figura 7.18 – Hemisfério  direito.  Das  três  sequências  diferentes  que  foram  sobrepostas,  apenas  uma
possui respostas que ultrapassam o limiar imposto, pelo que não se verificam regiões em comum.
Figura 7.17 – Hemisfério  esquerdo.  Das  três  sequências  diferentes  que  foram  sobrepostas,  apenas
uma  possui respostas que  ultrapassam  o  limiar  imposto,  pelo  que  não  se  verificam  regiões  em
comum.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 48

7.2.4 – Paciente 4 - JB



Figura 7.19 – Hemisfério  esquerdo  evidenciando  as  respostas  para  quatro  sequências  diferentes,
bem  como  as  regiões  em  comum. Todas  as  zonas  comuns  observadas  são  apenas comuns  a  2
sequências.   Duas   dessas   zonas   representam   desactivação   para   ambas   as   sequências, duas
representam activação para  ambas  as  sequências  e  duas  representam  activação para  uma  sequência  e
desactivação para outra.
Figura 7.20 – Hemisfério  direito  evidenciando  as respostas para quatro sequências  diferentes.  Não
se verificam regiões em comum.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 49

7.2.5 – Paciente 5 - LR




Figura 7.21 – Hemisfério  esquerdo  evidenciando  as  respostas  para quatro sequências  diferentes,
bem  como  a  região em  comum. Esta  é  apenas  comum  a  duas  sequências  e  representa  uma  zona de
desactivação para ambas.

Figura 7.22 – Hemisfério direito evidenciando  as  respostas  para quatro sequências  diferentes,  bem
como  a região em  comum. Esta  é  apenas  comum  a  duas  sequências  e  representa  uma  zona de
desactivação para ambas.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 50

## 7.3 – FASE 3 – ANÁLISE MÚLTIPLA DAS RESPOSTAS BOLD

Os  mapas  obtidos  na  secção  anterior  são  um  pouco  confusos  devido  ao  excesso  de
informação. Como tal, torna-se necessário por em evidência a informação relevante e eliminar
a  que  tem  significado  menos  importante.  Deste  modo,  todas  as  sequências  funcionais
referentes  a  um  paciente  foram  seleccionadas  e agrupadas segundo  uma  perspectiva  de
integração  simultânea  e  global.  Foi  assim  obtido  um  único  mapa  estatístico,  para  cada
hemisfério de cada paciente, com a informação de todas as sequências respectivas.
Nas imagens que se seguem, são exibidas, em representações planificadas dos hemisférios,
as  regiões  de  activação/desactivação  mais  significativas  para  cada  paciente.  São  ainda
indicadas,  através  de  setas,  as  regiões  correspondentes  a  áreas  de  activação  ou  desactivação
condizentes que foram observadas na secção 7.2.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 51

7.3.1 – Paciente 1 - GM



Figura 7.23 – Zonas de resposta no hemisfério esquerdo.

Figura 7.24 – Zonas de resposta no hemisfério direito.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 52

7.3.2 – Paciente 2 - AP



Figura 7.25 – Zonas de resposta no hemisfério esquerdo.

Figura 7.26 – Zonas de resposta no hemisfério direito.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 53

7.3.3 – Paciente 3 - IL



Figura 7.27 – Zonas de resposta no hemisfério esquerdo.

Figura 7.28 – Zonas de resposta no hemisfério direito.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 54

7.3.4 – Paciente 4 - JB






Figura 7.29 – Zonas de resposta no hemisfério esquerdo.

Figura 7.30 – Zonas de resposta no hemisfério direito.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 55

7.3.5 – Paciente 5 - LR



Figura 7.31 – Zonas de resposta no hemisfério esquerdo.

Figura 7.32 – Zonas de resposta no hemisfério direito.


## Capítulo 7 – Resultados  Miguel Gonçalves
## 56

Seguidamente, é apresentado um  resumo  dos  resultados  obtidos  para  cada  fase  de
processamento de dados.
A  figura  seguinte mostra  o  coeficiente  de  correlação  múltipla,  entre  o  modelo  adoptado  e
os  valores  observados,  para  o cluster cuja  resposta  hemodinâmica  foi  mais  significativa  em
cada  hemisfério  de  todos  os  pacientes. Colunas laranja indicam  activações  enquanto colunas
azuis representam desactivações.


















A tabela 7.1 indica, para cada paciente da fase 2, o número de regiões cerebrais que têm
sobreposição de clusters pertencentes a sequências diferentes, em cada hemisfério. É ainda
indicado, para cada zona de sobreposição, o tipo de resposta (positiva ou negativa) de cada
cluster.
Tabela 7.1 – Regiões cerebrais com activação/desactivação comum em diferentes sequências. As zonas comuns
observadas  são  apenas  comuns  a  2  sequências.  (+)(+)  significa  activação  para  ambas  as  sequências,  (+)(-)
significa  activação  para  uma  sequência  e  desactivação  para  outra,  (-)(-)  significa  desactivação  para  ambas  as
sequências.
## Paciente
Hemisfério esquerdo

Hemisfério direito

Nº zonas comuns
Tipo de
resposta

Nº zonas comuns
Tipo de
resposta


## GM
## 2 2 (-)(-)   0 ‒


## 0
## 0,1
## 0,2
## 0,3
## 0,4
## 0,5
## 0,6
## 0,7
## GMAPILJBLRJP
## R
## Pacientes
Hemisfério esquerdoHemisfério direito
Figura 7.33 – Respostas  hemodinâmicas  mais  significativas:  tipo  e  grau  de  correlação  com  o
modelo adoptado.

## Capítulo 7 – Resultados  Miguel Gonçalves
## 57

## AP
## 3 2 (-)(-)
## 1 (+)(-)
6 (5+1 comum a 3
sequências)
## 3 (-)(-)
## 1 (+)(-)
## 1 (+)(+)
## 1 (-)(-)(-)
## IL
## 0 ‒   0 ‒
## JB
## 6 2 (+)(+)
## 2 (+)(-)
## 2 (-)(-)
## 0 ‒
## LR
## 1 1 (-)(-)   1 1 (-)(-)


A  figura  que  se  segue  mostra  o  número  total  de  clusters  obtidos  nos  mapas  estatísticos
obtidos na fase 3, para cada hemisfério de cada paciente. A branco encontram-se o número de
clusters observados  nos  mapas  da  fase  3  que  correspondem  a  áreas  de  sobreposição  de
clusters de  sequências  diferentes,  observadas  na  fase  2.  Por  sua  vez,  a  cinzento  é  indicada  a
quantidade   de clusters que   aparecem   nos   mapas   estatísticos   da   fase   3   mas   que   não
correspondem a sobreposições de diferentes sequências, sendo ainda considerados os clusters
que não são visíveis nos mapas da fase 2 e que estão presentes nos mapas da fase 3.




## 0
## 1
## 2
## 3
## 4
## 5
## 6
## 7
## 8
## 9
## 10
## GMAPILJBLRGMAPILJBLR
Nº regiões
## Pacientes
## HEMISFÉRIO ESQUERDOHEMISFÉRIO DIREITO
Nº regiões condizentes com a fase 2Nº regiões não condizentes ou que não são visíveis na fase 2
Figura 7.34 – Número de  regiões condizentes e não condizentes ou  não  visíveis relativamente  àquelas
obtidas na fase 2.

Capítulo 8 – Discussão de Resultados  Miguel Gonçalves
## 58

## C A P Í TUL O  8 – DI S C US S Ã O   DE   R E S UL TA DOS

Nesta  secção, são  analisados  os  resultados  e  apresentadas algumas justificações para  os
fenómenos observados. No final, são referidos os principais problemas enfrentados.
No que diz respeito aos resultados da fase 1, apesar de se terem registado respostas BOLD
positivas  e  negativas significantes  (푝<0.05,  com  5 voxeis  contíguos (representação  3D)
ou  25  mm
## 2
(representação  plana)) em  todos  os  exames, e em alguns  destes com respostas
robustas  (푝<0.002, e  |t|  3.1), estas  não  exibem,  de  uma  forma  geral,  uma boa
concordância entre os valores previstos e observados, uma vez que os valores dos coeficientes
de correlação múltipla não são elevados. Contudo, o modelo criado, apesar de não explicar na
totalidade   os   resultados   obtidos,   tem   características   que   se   assemelham   à   resposta
hemodinâmica real resultante da actividade epiléptica.
A não obtenção de resultados mais satisfatórios pode dever-se aos factores seguintes.
Neste  tipo  de  análise,  os  resultados  dependem  de  uma  forma  crítica do  facto da  forma  da
resposta BOLD assumida ser apropriada ou não. Devido à variabilidade intra e entre pacientes
desta  resposta,  um  modelo estático da sua forma  pode  conduzir  a  ajustes  subóptimos. Para
modelar a forma da resposta hemodinâmica mais flexivelmente, preditores adicionais podem
ser  definidos. Dois preditores adicionais  frequentemente  utilizados  são  derivações  da  dupla
função  gama  com  respeito  aos  parâmetros  de  atraso  e  dispersão.  Uma  vez  adicionadas  à
matriz de  plano  experimental,  estas  funções  de  referência  tornam  possível  a  detecção de
pequenas  variações  na  latência  e  extensão  da  resposta e,  por  conseguinte,  a  resposta  ao
estímulo é mais bem modelada [35].
Os  resultados  apresentam  um  coeficiente  de  correlação  múltipla  médio;  contudo,  não  se
pode  esperar  uma correspondência  de  um  para  um  entre  observações  de  EEG  e  IfRM.
Primeiro, o EEG é sensível apenas  à actividade  das camadas  corticais superficiais. Segundo,
estamos  a  medir  tipos  muito  diferentes  de  actividade,  uma  eléctrica  e  outra  baseada  na
resposta venosa  a alterações metabólicas. É provável que, em alguns casos, uma modalidade
seja sensível a determinada actividade à qual a outra é indiferente [7].
Tem ainda que  se  ter  em  conta  a  perda  e  distorção  de  sinal  em  interfaces  de  diferente
susceptibilidade,  tais  como  tecido-ar  e  tecido-osso,  às  quais  as  sequências GE-EPI são
particularmente sensíveis.

Capítulo 8 – Discussão de Resultados  Miguel Gonçalves
## 59

Relativamente  ao  tipo  de  respostas  verifica-se  que,  ao  contrário  do  que  seria  de  esperar,
grande  parte  das  respostas  são  desactivações.  Embora  a  dimensão  da  amostra  não  seja
estatisticamente  significativa,  estes  resultados  deixam  a  indicação de que  as  respostas
negativas parecem assumir grande importância na epilepsia.
As  lesões  cerebrais  presentes  em  alguns  dos  pacientes  parecem  não  ter  correspondência
directa  com  a  intensidade  das  respostas  obtidas,  uma  vez  que  existem  pacientes com  lesões
cujas  respostas  têm  maior  intensidade  e  outros  cujas  respostas  têm  menor  intensidade
relativamente às respostas daqueles que não possuem lesões cerebrais.
Verificou-se  ainda que  a  resposta  BOLD  sofreu  um  aumento  em  oito  hemisférios,
referentes a cinco dos seis pacientes, aquando da sobreposição dos quatro mapas com funções
de resposta hemodinâmica diferentes, relativamente às respostas obtidas com apenas um mapa
com o pico da FRH aos 5 s, confirmando assim os resultados obtidos por Bagshaw et al [37].
Relativamente  à fase  2,  observa-se  que  as  regiões  cerebrais  que  evidenciam  activação
comum  em  diferentes  sequências  do  mesmo  paciente  são  diminutas  ou  inexistentes.  Quando
observadas,  nem  sempre correspondem  a  respostas  do  mesmo  tipo,  sendo  sempre  comuns  a
um número limitado de sequências.
Estes resultados vêm confirmar a natureza incerta da resposta hemodinâmica relativamente
à  actividade  neuronal  epiléptica,  embora  alguma  variabilidade  possa  ser  também  devida  aos
factores acima descritos.
A fase 3 permitiu observar zonas de resposta BOLD significantes de dois tipos: 1) regiões
de activação/desactivação correspondentes a sobreposições de zonas de resposta de diferentes
sequências,  sendo  que  não  são  todas  as  sobreposições  que  conduzem  a  respostas  BOLD
significativas,  e  2) zonas  que,  sem  serem  de  activação  condizente,  representam  importância
acrescida pela sua elevada intensidade. De notar que existem zonas cuja presença nos mapas
estatísticos  de  sequências  individuais  não  é  observada  com  o  limiar  imposto, mas  que,
contudo, se revelam importantes quando se estuda o efeito conjunto das respostas obtidas em
várias sequências.

Ao  longo  do  processamento  dos  dados, surgiram  alguns  problemas  que se  deveram
essencialmente  às  limitações computacionais do  programa  utilizado,  sendo  as principais  as
que se seguem.

Capítulo 8 – Discussão de Resultados  Miguel Gonçalves
## 60

Um  dos  problemas  tem  a  ver  com  o  co-registo  das  informações  anatómica  e  funcional.
Uma  vez  realizado  o  alinhamento  inicial,  o  programa BrainVoyager
## TM
é  suposto  realizar
automaticamente  o  alinhamento  fino,  em  que  se  alcança  a  melhor  posição  de  alinhamento
entre os dois tipos de imagem. Contudo, o resultado fica aquém das expectativas, uma vez que
tem que se realizar um ou vários ajustes manuais antes de se conseguir uma boa sobreposição,
confirmando  apenas  depois  esse  alinhamento  com  o  ajuste  automático.  Esta  é  uma  operação
fundamental  na  obtenção  do  resultado  pretendido  que,  pelo  facto  de  não  possuir  a  precisão
desejada, pode ser considerada como uma importante fonte de erro.
Outra  limitação  tem  a  ver  com  o  resultado  do  processo  automático  de  segmentação  e
reconstrução  dos  hemisférios  cerebrais.  Após  realizar  esse  procedimento,  as  superfícies
obtidas  têm  ainda  algumas  imperfeições  (depressões  e  protuberâncias)  que  têm  que  ser
corrigidas  manualmente.  Este  tipo  de  processamento  de imagem  é  extremamente  moroso,
podendo  levar  1  hora  por  hemisfério,  sendo  o  resultado  final  dependente  do  que  o  operador
considera necessário corrigir e da magnitude da correcção imposta.







Capítulo 9 – Conclusão e Perspectivas Futuras  Miguel Gonçalves
## 61

## C A P Í TUL O  9 – C O NC L US Ã O E   P E R S P E C TI V A S   F UT UR A S

No  estudo  da  epilepsia  é  necessário  fazer  a  localização  o  mais  precisa  possível  do foco
epiléptico com vista a uma possível intervenção cirúrgica para remover a zona lesada. Foi no
âmbito   deste   tema   que   este   trabalho   de   investigação   se   inseriu,   tendo   por   base   a
complementaridade  entre  as  técnicas  de  aquisição  de  EEG  e  IfRM,  através  da  associação  da
insuperável  resolução  temporal  do  EEG  à  boa  resolução  espacial  da  IfRM.  Neste sentido,
pretendia-se,  numa  primeira  fase, verificar  quais  as  regiões  cerebrais  que  tinham  activação,
bem como quantificar o grau de correlação entre o modelo adoptado e os dados do exame de
IfRM. Posteriormente, estudou-se o efeito da variação da localização das respostas BOLD em
diferentes  sequências  do  mesmo  paciente. Por  fim,  procedeu-se  à  integração  simultânea  das
múltiplas sequências do mesmo paciente com o objectivo de uma análise global.
Neste projecto utilizou-se uma técnica ainda pouco utilizada de processamento de imagem,
que  consiste  na  insuflação  e  posterior  alisamento  dos  hemisférios  cerebrais,  sem, contudo,
perder  as  informações  referentes  aos  sulcos  e  circunvoluções,  bem  como  a  localização
tridimensional  das  estruturas  e  activações  funcionais.  É, assim, obtida  uma  informação  mais
imediata e geral da hemodinâmica cerebral.
Os  resultados obtidos  a  partir  dos  testes  efectuados revelaram,  em  primeiro  lugar, que  a
abordagem  utilizada não  explica de  uma  forma  absoluta  a  variação  dos percursos temporais
observados  no  exame  de  IfRM,  sendo  talvez  necessária  uma  análise mais  complexa. Em
segundo  lugar,  concluiu-se  que  as  respostas  aos  surtos  de  actividade  epiléptica  variam
consideravelmente  entre  sessões  de  aquisição  do  mesmo  paciente. Por  último, chegou-se  à
conclusão de que nem todas as zonas de sobreposição de actividade BOLD são significantes,
sendo que existem outras que o são sem corresponderem a regiões coincidentes.
Deste  modo, estes  resultados permitiram  confirmar pressupostos  e  resultados de  estudos
previamente  realizados  nesta  área,  nomeadamente  acerca do  carácter  mutável  da função  de
resposta  hemodinâmica,  embora  o  número  reduzido  de  casos  clínicos  possa  ser  um  factor
limitante na obtenção de resultados estatisticamente válidos.
É  ainda  de  referir  que  os  resultados  deste  trabalho  diferem  daqueles  obtidos  pelo  Dr.
Alberto  Leal  para  os  mesmos  pacientes.  No  seu  diagnóstico  da  região  cerebral  responsável
pela  actividade  epiléptica,  o  Dr.  Leal  utilizou,  para  além  da  aquisição  simultânea  de
EEG/IfRM, exames de EEG de alta resolução e informação clínica relevante (tipo de ataques,

Capítulo 9 – Conclusão e Perspectivas Futuras  Miguel Gonçalves
## 62

etc.),  confirmando-se, após  cirurgia, que  os  seus  resultados  correspondiam  à  realidade  do
paciente.
Em  conclusão, a  combinação  das  técnicas  de  EEG  e  IfRM tem grande  potencial  no
diagnóstico das zonas de actividade epiléptica, abrindo um novo caminho para a investigação
das  causas  e  efeitos  deste  distúrbio  neurológico. Porém,  a sua  aplicação  a  pacientes  com  a
finalidade  de  localizar  regiões  epileptogénicas  ainda  não  está  garantida,  pois  mais necessita
ser descoberto acerca  dos  mecanismos  subjacentes  a  este  fenómeno  e do significado  das
várias respostas. Pode ser considerada, contudo, no contexto de indicar regiões potenciais para
investigação mais detalhada de uma forma não invasiva.

Devido  à  importância  deste  assunto,  o  trabalho  realizado  ao  longo  deste  projecto  foi
bastante gratificante. Contudo, e como acima referido, há ainda muitas incógnitas. O próximo
passo na integração de EEG e IfRM passa por considerar as ligações temporais entre as duas
modalidades.  A  observação  das  flutuações  simultâneas  dos  dois  sinais  pode  ser  alcançada
através  do  agrupamento  dos  eventos  e  da  visualização  das  variações  relativas  na  amplitude
dos exames de EEG e IfRM [7].
Seria interessante também verificar o grau de coerência da forma das respostas funcionais
entre  as  mesmas  regiões  cerebrais  de  pacientes  diferentes,  com  o  objectivo de  criar  modelos
optimizados para as diferentes regiões cerebrais que evidenciam activação ou desactivação.

## Miguel Gonçalves
## 63

## B I B L I O GR A F I A

[1]  Chiras  D, Human  biology, 6ª  edição,  Jones & Barlett  Publishers,  Estados  Unidos  da
América, 2008, pp. 103, 189-204
[2]  Bear  M,  et  al., Neuroscience – Exploring  the  Brain,  3ª  Edição,  Lippincott  Williams  &
Wilkins, Estados Unidos da América, 2007, pp. 24, 103-104
[3] Young B, Heath J, Wheater’s Histologia Funcional, 4ª edição, Guanabara Koogan, Brasil,
2001, pp. 116-126
[4] Lodish H, e tal., Molecular Cell Biology, 4ª edição, W. H. Freeman and Company, Estados
Unidos da América, 2001
[5] Caldas M, Slides das aulas de Biologia Celular B, Estrutura da membrana celular, 2006
[6] WHO. Epilepsy [Online] World Health Organization. Consultado em 04 de 07 de 2009.
http://www.who.int/mediacentre/factsheets/fs999/en/
[7] Gotman J, et al., Combining EEG and fMRI: A Multimodal Tool for Epilepsy Research,
Journal of Magnetic Resonance Imaging 2006; 23:906-920
[8] LPCE. A Epilepsia [Online] Liga Portuguesa Contra a Epilepsia. Consultado em 04 de 07
de 2009. http://www.lpce.pt/doenca.htm
[9]  Engel  J, A  Proposed  Diagnostic  Scheme for  People  with  Epileptic  Seizures  and  with
Epilepsy: Report of the ILAE Task Force on Classification and Terminology, Epilepsia 2001;
## 42(6):796-803
[10] Dekker P, Epilepsy-A manual for Medical and Clinical Officers In Africa, World Health
Organization, França, 2002, pp. 19-31
[11] Zumsteg  D,  et  al., Propagation  of  interictal  discharges  in  temporal  lobe  epilepsy:
Correlation of spatiotemporal mapping with intracranial foramen ovale electrode recordings,
## Clinical Neurophysiology 2006; 117:2615–2626
[12] Barreto A, et al., Multiresolution Characterization of Interictal Epileptic Spikes based on
a Wavelet Transformation, Florida International University, 1995

## Miguel Gonçalves
## 64

[13]  Sörnmo  L,  Laguna  P, Bioelectrical  Signal  Processing  in  Cardiac  and  Neurological
Applications, Elsevier Academic Press, Estados Unidos da América, 2005, pp. 10-55
[14] Fish B, EEG Primer – Basic Principles of Digital and Analog EEG, 3ª Edição, Elsevier
B. V., Holanda, 1999, p. 3, 73
[15] Dudai Y, Memory from A to Z: keywords, concepts and beyond, Oxford University Press,
Inglaterra, 2004, p. 103
[16]   Niedermeyer   E,   Silva   F   H, Electroencephalography:   basic   principles,   clinical
applications and related fields, 5ª Edição, Lippincott Williams & Wilkins, Estados Unidos da
América, 2004, p. 111, 1224
[17]  Brown  M,  Semelka  R, MRI  Basic  Principles  and  Applications,  3ª  Edição,  John  Wiley
and Sons, Estados Unidos da América, 2003, pp. 1-81
[18] Secca M, Slides das aulas de Imagiologia, A Imagem por Ressonância Magnética (IRM),
## 2009
[19]  Belkić  K, Molecular  Imaging  through  Magnetic  Resonance  for  Clinical  Oncology,
Cambridge Int. Science Publishing, Suécia, 2004, pp. 11-17
[20] Westbrook C, et al., MRI in practice, 3ª Edição, Wiley-Blackwell, 2005, pp. 10-22
[21]  Vlaardingerbroek  M,  et  al., Magnetic  Resonance  imaging:  theory  and  practice,  3ª
Edição, Springer, 2003, pp. 15-16
[22]  Prasad  P, Magnetic  resonance  imaging:  methods and  biologic  applications,  Humana
Press, 2005, pp. 29-33
[23]   Dale   A,   et   al., Cortical   Surface-Based   Analysis.   I.   Segmentation   and   Surface
## Reconstruction, Neuroimage 1999; 9:179-194
[24]  Talairach  J,  Tournoux  P, Co-Planar  Stereotaxic  Atlas  of  the  Human Brain,  Thieme
Medical Publishers, Estados Unidos da América, 1988, pp. 1-122
[25]  Bankman  I, Handbook  of  medical  imaging:  processing  and  analysis,  Academic  Press,
Estados Unidos da América, 2000, p. 555, 558

## Miguel Gonçalves
## 65

[26]  Goebel  R,  et  al., BrainVoyager  QX – Getting Started  Guide, Versão  2.6,  Brain
Innovation B.V., 2008
[27] Fischl B, et al., Cortical Surface-Based Analysis. II: Inflation, Flattening, and a Surface-
## Based Coordinate System, Neuroimage 1999; 9:195-207
[28]  Tofts  P, Quantitative  MRI  of the  brain: measuring  changes  caused  by  disease,  John
Wiley & Sons Ltd, Inglaterra, 2003, pp. 414-438
[29] Gore J, Principles and practice of functional MRI of the human brain, Journal of Clinical
## Investigation 2003; 112:4-9
[30]  Buxton  R,  et  al., Dynamics  of  Blood  Flow  and  Oxygenation  Changes  During  Brain
Activation: The Baloon Model, Magnetic Resonance in Medicine 1998; 39:855-864
[31]  Kobayashi  E,  et  al., Negative  BOLD  Responses  to  Epileptic  Spikes,  Human  Brain
## Mapping 2006; 27:488-497
[32] Moonen C, Bandettini P, Functional MRI, Springer, 2000, p. 195
[33] Rudin M, Imaging in Drug Discovery and Early Clinical Trials, Birkhäuser, Suíça, 2006,
p. 38, 42
[34] Lazar N, The Statistical Analysis of Functional MRI Data, Springer, Estados Unidos da
América, 2008, pp. 23-25
[35] Stippich C, et al., Clinical Functional MRI, Springer, Alemanha, 2007, pp. 10-38
[36]  Salek-Haddadi  A,  et  al., EEG  quality  during  simultaneous  functional  MRI  of  interictal
epileptiform discharges, Magnetic Resonance Imaging 2003; 21:1159-1166
[37]   Bagshaw   A,   et   al., EEG-fMRI   of   focal   epileptic   spikes:   analysis   with   multiple
haemodinamic functions and comparison with gadolinium-enhanced MR angiograms, Human
## Brain Mapping 2004; 22:179-192
[38] Glover G, Deconvolution of impulse response in event-related BOLD fMRI, Neuroimage
## 1999; 9:416-429
[39]  Kobayashi  E,  et  al., Temporal  and  Extratemporal  BOLD  Responses  to  Temporal  Lobe
## Interictal Spikes, Epilepsia 2006; 47(2):343-354

## Miguel Gonçalves
## 66

[40]  Bagshaw  A,  et  al., EEG-fMRI  Using  z-Shimming  in  Patients  With  Temporal  Lobe
Epilepsy, Journal of Magnetic Resonance Imaging 2006; 24:1025-1032
[41]  Cohen  L,  Holliday  M, Practical  statistics  for  students:  an  introductory  text,  2ª  Edição,
SAGE, Inglaterra, 1996, p. 157




## Anexos  Miguel Gonçalves
## 67

## A NE X O S

## PROCESSAMENTO DA IMAGEM TRIDIMENSIONAL – REMOÇÃO DO CRÂNIO

Em cada iteração 풕, a coordenada 푥
## 푘
de cada vértice é actualizada de acordo com as forças
de IRM (푭
## 푀
) e de redução de curvatura (푭
## 푆
## ):
x
## 푘

## 풕+1

## =x
## 푘

## 풕

## +푭
## 푆

## 풕

## +푭
## 푀

## 풕

## (푎.1)
onde 푭
## 푆
é dada por
e 푭
## 푀
é dada por
## 푭
## 푀
## =휆
## 푀
## 퐧
## 푘
max

## 0,tanh

## 푰

x
## 푘
## −푑퐧
## 푘

## −푰
thresh


## 30
## 푑=1
## (푎.3)
onde 휆
## 푇
e 휆
## 푁
especificam  a importância  relativa das  componentes  tangencial  e  normal  da
força  de  suavização, 휆
## 푀
representa  o  peso  atribuído  à força 푭
## 푀
, 퐈 é  a  matriz  identidade  33,
## 푁
## 푘
indica  o  conjunto  de  vértices vizinhos  do  vértice 푘, 푉 é  o  número  de  vértices  no  molde,
## 퐈

x

é  o  valor  da  intensidade  no  local x,  enquanto 퐧
k
e 퐧
## ′
k
indicam  a  superfície  normal  à
localização de 푘 e a sua transposta, respectivamente [23].









## Anexos  Miguel Gonçalves
## 68

## IMAGEM FUNCIONAL POR RESSONÂNCIA MAGNÉTICA

Análise estatística: Modelo Linear Geral

Sistema de equações do MLG:





## 푦
## 1
## ⋮
## ⋮
## ⋮
## 푦
## 푛





## =





## 1푋
## 11
## ...
## ⋮⋮⋮
## ⋮
## ⋮
## 1
## ⋮
## ⋮
## 푋
## 푛1
## ⋮
## ⋮
## ⋯

## ......푋
## 1푝
## ⋮⋮⋮
## ⋮
## ⋮
## ⋯
## ⋮
## ⋮
## ⋯
## ⋮
## ⋮
## 푋
## 푛푝






## 푏
## 0
## ⋮
## ⋮
## 푏
## 푝
## +





## 푒
## 1
## ⋮
## ⋮
## ⋮
## 푒
## 푛





## ⇔          풚=푿풃+풆

Análise t-estatística:
Do MLG temos que:                            풚=푿풃+풆

## 풆=풚−푿풃
## 풃=(푿
## ′
## 푿)
## −ퟏ
## 푿′풚

푐 representa  um  vector  que  contém  os  valores  dos  coeficientes  beta  correspondentes  à
hipótese  nula.  A  hipótese  nula  enuncia  que  não  existe  efeito  resultante  de  uma  condição  de
activação  relativamente  a  uma  condição  de  controlo,  isto  é,  não  há  diferenças  entre  as  duas
condições [35].
Através  da  utilização  de  uma  notação  matricial,  a  combinação  linear  que  define  o  efeito
estimado de um coeficiente beta pode ser escrita como o produto escalar dos vectores 풄 e 풃. A
hipótese nula pode então ser simplesmente descrita como 풄
## ′
풃=0. Para um dado  número de
preditores,  este  efeito  pode  ser  testado  com  a  seguinte  estatística  t,  com n−p graus  de
liberdade (푛 - número de pontos temporais/volumes do exame, 푝 - número de preditores) [35]:
## 푡=
## 풄′풃

## 푉푎푟

## 풆

## 풄
## ′

## 푿
## ′
## 푿

## −1
## 풄





## Anexos  Miguel Gonçalves
## 69

Cálculo do valor probabilístico de erro, p:
A  probabilidade  de  erro  pode  ser  calculada  a  partir  do  valor  de 푡 através  da  utilização  da
função beta incompleta 퐼
## 푥
(푎,푏) e do número de pontos medidos 푁 [35]:
## 푝=퐼
## 푁−2
## 푁−2+푡
## 2

## 푁−2
## 2
## ,
## 1
## 2

sendo que
## 퐼
## 푥

## 푎,푏

## = 푡
## 푎−1
## 푥
## 0

## 1−푡

## 푏−1
## 푑푡,0≤푥≤1

Cálculo do coeficiente de correlação múltipla, R:
O coeficiente  de  correlação  múltipla  mede  o  relacionamento  linear  entre  uma  variável  e
duas ou mais outras variáveis e a sua fórmula geral é dada por [41]:
## 푅
## 1,23
## =

## 푟
## 12
## 2
## +푟
## 13
## 2
## −2푟
## 12
## 푟
## 13
## 푟
## 23
## 1−푟
## 23
## 2

em que 푅
## 1,23
representa a correlação múltipla entre a variável 1 e a combinação das variáveis
2  e  3, 푟
## 12
é  o  coeficiente  de  correlação  entre  as  variáveis  1  e  2, 푟
## 13
é  o  coeficiente  de
correlação entre as variáveis 1 e 3, 푟
## 23
é o coeficiente de correlação entre as variáveis 2 e 3.

Aplicação do MLG a uma região de interesse (ROI):




## (a)

## Anexos  Miguel Gonçalves
## 70


Figura  a.1 – Ajuste  do  modelo  escolhido para uma ROI  do paciente  GM,  hemisfério  esquerdo:
indica  quão  bem  o  MLG  escolhido  se  ajusta  à  região  de  interesse  em  questão. (a) Análise  de
variância. (b) Curvas representativas dos percursos temporais dos dados do exame e do modelo.

A  figura  a.1  (b) mostra  3  curvas: a  curva  azul  representa  os  dados  do  exame  de  IfRM
referentes ao percurso temporal da região de interesse seleccionada; a verde é o modelo, que
mostra o ajuste do MLG baseado no paradigma de activação; e a curva vermelha é a curva de
erro, obtida subtraindo a curva verde da curva azul [26].

## FUNÇÃO DE RESPOSTA HEMODINÂMICA

A seguir apresenta-se a forma das funções de resposta hemodinâmica utilizadas, com picos
a 3, 5, 7 e 9 segundos.



## (b)

## Anexos  Miguel Gonçalves
## 71


Figura a.2 – Forma das funções de resposta hemodinâmica com picos a 3, 5, 7 e 9 segundos.




