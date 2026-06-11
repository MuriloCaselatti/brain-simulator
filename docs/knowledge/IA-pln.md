

Processamento de LinguagemNatural
Silviodo LagoPereira
slago@ime.usp.br
## 1  Introdu ̧c ̃ao
Processamentode LinguagemNatural(Pln) consisteno desenvolvimento de
modeloscomputacionaisparaa realiza ̧c ̃ao de tarefasque dependemde informa-
̧c ̃oes expressasem algumal ́ınguanatural(e.g.tradu ̧c ̃ao e interpreta ̧c ̃ao de textos,
buscade informa ̧c ̃oes em documentos e interfacehomem-m ́aquina)[1,4].
Conforme[2], a pesquisaemPlnest ́a voltada,essencialmente, a trˆes aspectos
da comunica ̧c ̃ao em l ́ınguanatural:
## –som:fonologia
–estrutura:morfologiae sintaxe
–significado:semˆantica e pragm ́atica
Afonologiaest ́a relacionadaao reconhecimento dos sonsque comp ̃oemas
palavrasde umal ́ıngua.Amorfologiareconheceas palavrasem termosdas
unidadesprimitivas que a comp ̃oem(e.g. ca ̧cou→ca ̧c+ou). Asintaxedefine
a estruturade umafrase,combasena formacomoas palavrasse relacionam
nessafrase(figura1). Asemˆanticaassocia significadoa umaestruturasint ́atica,
em termosdos significadosdas palavrasque a comp ̃oem(e.g.`a estruturada
figura1, podemosassociaro significado“um animalperseguiu/capturou outro
animal”). Finalmente, apragm ́aticaverificase o significadoassociado`a uma
estruturasint ́atica ́e realmente o significadomaisapropriadono contextocon-
siderado(e.g.no contextopredador-presa,“perseguiu/capturou”→“comeu”).
frase
## /\
## /\
sujeitopredicado
## /\/|\
## /\/|\
artigosubstantivoverboartigosubstantivo
## |||||
ogatoca ̧couorato
Figura1.Uma ́arvore sint ́atica
Comopodemosver,Pln ́e uma ́areade pesquisamuitovasta,que envolve
diversasdisciplinasdo conhecimento humano.Por se tratarde um assunto com-
plexo,nesseartigo,vamosabordarapenasa an ́alisesint ́aticade algumasfrases

2S. L. Pereira
em portuguˆes. Mostraremoscomoespecificarumagram ́atica
## 1
capazde gerarum
conjunto finitode senten ̧cas e de decidirse umadeterminadasenten ̧ca pertence
ou n ̃ao `a linguagemdefinidapela gram ́atica.Em seguida,estenderemosessa
gram ́aticaparatratarconcordˆanciadegˆeneroen ́umero, bem comotempo ver-
bal. Finalmente, mostraremoscomomodificara gram ́aticaparaque ela construa
a  ́arvore sint ́aticade umasenten ̧ca de formaautom ́atica.
2  Gram ́aticae an ́alisesint ́atica
Umagram ́atica ́e umaespecifica ̧c ̃ao formalda estruturadas senten ̧cas permitidas
numalinguagem.O modo maissimplesde definirumagram ́atica
## 2
́e especificando
um conjunto de s ́ımbolosterminais, denotandopalavrasda linguagem,um con-
junto de s ́ımbolosn ̃ao-terminais, denotandoos componentes das senten ̧cas,e
um conjunto deregras de produ ̧c ̃ao, que expandems ́ımbolos n ̃ao-terminaisnuma
seq ̈uˆenciade s ́ımbolosterminaise n ̃ao-terminais[3]. Al ́em disso,a gram ́atica
deve ter um s ́ımbolo n ̃ao-terminalinicial.
Por exemplo,a gram ́aticaa seguirdefineum fragmento da l ́ınguaportuguesa:
## Gram ́atica1.
f rase⇒sujeitopredicado
sujeito⇒artigo substantivo
predicado⇒verbo artigo substantivo
artigo⇒o
substantivo⇒gato|rato
verbo⇒ca ̧cou
Nessagram ́atica,os s ́ımbolosterminaiss ̃aoo,gatoerato, sendoos de-
maiss ́ımbolosn ̃ao-terminais
## 3
. A regrade produ ̧c ̃aof rase⇒sujeitopredicado
estabeleceque umafrase ́e compostade um sujeitoseguidode um predicado;
enquanto a regrasubstantivo⇒gato|ratoestabeleceque um substantivo
pode ser a palavra “gato” ou “rato”. Al ́em disso,paraessagram ́atica,o s ́ımbolo
n ̃ao-terminalinicialser ́af rase.
Nasgram ́aticaslivresde contexto(do tipo que consideramosnesseartigo),
o ladoesquerdode umaregrade produ ̧c ̃ao ser ́a sempreum  ́unicos ́ımbolo n ̃ao-
terminal,enquanto o ladodireitopode conter s ́ımbolos terminaise n ̃ao terminais.
Comoveremosa seguir,umagram ́aticapode ser usadatanto parareconhe-
cimento, ou seja,paradecidirse essafrasepertence`a linguagemdefinidapela
gram ́atica;quanto paragera ̧c ̃ao, ou seja,paraconstruirumafrasepertencente
`a linguagemdefinidapela gram ́atica.
## 1
Usaremosagram ́atica de cl ́ausulasdefinidasda linguagemProlog.
## 2
Nesseartigo,tratamosapenasde gram ́aticaslivresde contexto.
## 3
Os s ́ımbolosn ̃ao-terminaiss ̃ao escritosemit ́alico.

Processamento de LinguagemNatural3
2.1Reconhecimento de frases
H ́a duasestrat ́egiasque podemser aplicadasparao reconhecimento de frases:
Top-down:comessa estrat ́egia,sintetizamosa frasea ser reconhecidaaplicando
as regrasde produ ̧c ̃ao de formaprogressiva, em profundidade,a partirdo s ́ımbolo
inicialda gram ́atica.Por exemplo,parareconhecera frase“o gatoca ̧cou o rato”,
procedemosda seguinte maneira:
f rase
## ⇒sujeitopredicado
⇒artigo substantivo predicado
⇒osubstantivo predicado
⇒o gatopredicado
⇒o gatoverbo artigo substantivo
⇒o gatoca ̧couartigo substantivo
⇒o gatoca ̧cou osubstantivo
⇒o gatoca ̧cou o rato
Comoa frasepˆode ser sintetizada,a partirdas regrasde produ ̧c ̃ao da gram ́atica,
conclu ́ımosque ela pertence`a linguagemdefinidapela gram ́atica.
O processode reconhecimentotop-downtamb ́em pode ser representadopor
meiode uma ́arvore sint ́atica(geradade formasemelhante a uma ́arvore de
buscaem profundidade,conformea numera ̧c ̃ao indica),veja:
## 1-frase
## /\
## /\
## 2-sujeito5-predicado
## /\/|\
## /\/|\
## 3-artigo4-substantivo6-verbo7-artigo8-substantivo
## |||||
## |||||
## "o""gato""ca ̧cou""o""rato"
Numa ́arvore sint ́atica,as folhass ̃ao sempres ́ımbolos terminais(i.e.palavras
da linguagem),enquanto os demaisn ́os s ̃ao sempres ́ımbolosn ̃ao-terminais(i.e.
nomesda unidadescomponentes da frase).
Considereagoraa frase“o gatorato ca ̧cou o”:
f rase
## ⇒sujeitopredicado
⇒artigo substantivo predicado
⇒osubstantivo predicado
⇒o gatopredicado
⇒o gatoverbo artigo substantivo
Comon ̃ao h ́a na gram ́aticaumaregraque sejacapazde derivar o s ́ımbolo ter-
minalrato, a partirdo s ́ımbolo n ̃ao-terminalverbo, o reconhecimento fracassa.

4S. L. Pereira
Exerc ́ıcio 1Combase na gram ́atica definidaa seguir,fa ̧ca o reconhecimento
top-downdas frases“umgatomia”e “umrato corre desesperadamente”e de-
senheas  ́arvores sint ́aticas.
f rase⇒sujeitopredicado
sujeito⇒artigo substantivo
predicado⇒verbo
intransitivo
predicado⇒verbo
intransitivoadv ́erbiomodal
artigo⇒um
substantivo⇒gato|rato
verbo
intransitivo⇒mia|corre
adv ́erbiomodal⇒desesperadamente§
Botton-up:comessaestrat ́egiaderivamoso s ́ımbolo inicialda gram ́atica,a
partirda frasea ser reconhecida,aplicandoas regrasde produ ̧c ̃ao de forma
regressiva. Por exemplo,parareconhecera frase“o gatoca ̧cou o rato”, fazemos:
o gatoca ̧cou o rato
⇒artigogatoca ̧cou o rato
⇒artigo substantivoca ̧cou o rato
⇒sujeitoca ̧cou o rato
⇒sujeitoverboo rato
⇒sujeitoverbo artigorato
⇒sujeitoverbo artigo substantivo
## ⇒sujeitopredicado
⇒f rase
Comoconseguimosobtero s ́ımbolo n ̃ao-terminalinicialda gram ́atica,a partirda
frasesendoreconhecida,conclu ́ımosque essafrasepertence`a linguagemdefinida
pela gram ́atica.Vejamosum outroexemplo“o gatorato ca ̧cou o”:
o gatoratoca ̧cou o
⇒artigogatoratoca ̧cou o
⇒artigo substantivoratoca ̧cou o
⇒sujeitoratoca ̧cou o
⇒sujeitosubstantivoca ̧cou o
⇒sujeitosubstantivo verboo
⇒sujeitosubstantivo verbo artigo
Comon ̃ao h ́a na gram ́aticaumaregraque seja capazde reconhecera seq ̈uˆencia
substantivoverbo artigocomoumpredicado, o reconhecimento fracassa.
Exerc ́ıcio 2Refa ̧ca o exerc ́ıcio 1, usandoreconhecimentobotton-up.§

Processamento de LinguagemNatural5
2.2Gera ̧c ̃ao de frases
O processode gera ̧c ̃ao de frasesfuncionade formasemelhante ao reconheci-
mentotop-down, excetopelo fatoque,quandoum s ́ımbolo n ̃ao-terminalpode
ser expandidopor duasou maisregrasde produ ̧c ̃ao distintas,devemoscriar
umaramifica ̧c ̃ao paracadapossibilidade.Comoexemplo,vamosgeraras frases
da linguagemdefinidapela Gram ́atica1.
frase
## |
sujeitopredicado
## |
artigosubstantivopredicado
## |
"o" substantivopredicado
## /\
"o gato"predicado"o rato"predicado
## ||
"o gato"verboartigosubstantivo"o rato"verboartigosubstantivo
## ||
"o gatoca ̧cou"artigosubstantivo"o ratoca ̧cou"artigosubstantivo
## ||
"o gatoca ̧cou o" substantivo"o ratoca ̧cou o" substantivo
## /\/\
"o gatoca ̧cou o gato""o gatoca ̧cou o rato""o ratoca ̧cou o gato""o ratoca ̧cou o rato"
Exerc ́ıcio 3Gere todas as frasesda linguagemdefinidapela gram ́atica a seguir:
f rase⇒sujeitopredicado
sujeito⇒pronome
pessoal|nomepr ́oprio
predicado⇒verbointransitivo
pronomepessoal⇒voc^e
nomepr ́oprio⇒Z ́e
verbointransitivo⇒come|dorme§
3  Gram ́aticade cl ́ausulasdefinidas
Prolog ́e a linguagemidealparao processamento de linguagemnatural[2].
Usandoum recursoembutidono compilador,conhecidocomonota ̧c ̃aoDcg,
podemosescrever gram ́aticasque podemser utilizadastanto parao reconheci-
mento, quanto paraa gera ̧c ̃ao de frases,de formaautom ́atica.Nessanota ̧c ̃ao, as
regrasde produ ̧c ̃ao s ̃ao codificadasda seguinte forma:
Gram ́atica2.Usandoa nota ̧c ̃aoDcg
frase-->sujeito,predicado.
sujeito-->artigo,substantivo.
predicado-->verbo,artigo,substantivo.
artigo-->[o].
substantivo-->[gato]| [rato].
verbo-->[ca ̧cou].

6S. L. Pereira
Reconhecimento autom ́aticode frases:Compilandoessagram ́aticacomo
Swi-Prolog, podemosentrarno modo de consultae digitar:
?- frase([o,gato,ca ̧cou,o,rato],[]).
A essaconsulta,o sistemaresponder ́ayes, indicandoque a frasefoi reconhecida
comopertencente `a linguagemdefinidapela gram ́atica.
Para reconheceressafrase,oSwi-Prologprocededa seguinte maneira:
?- frase([o,gato,ca ̧cou,o,rato],[])
## |
## | (expandindofrase)
## |
?- sujeito([o,gato,ca ̧cou,o,rato],R0),predicado(R0,[])
## |
## | (expandindosujeito)
## |
?- artigo([o,gato,ca ̧cou,o,rato],R1),substantivo(R1,R0),predicado(R0,[])
## |
## | (expandindoartigo:consome"o")
## |
?- substantivo([gato,ca ̧cou,o,rato],R0),predicado(R0,[])
## |
## | (expandindosubstantivo:consome"gato")
## |
?- predicado([ca ̧cou,o,rato],[])
## |
## | (expandindopredicado)
## |
?- verbo([ca ̧cou,o,rato],R2),artigo(R2,R3),substantivo(R3,[])
## |
## | (expandindoverbo:consome"ca ̧cou")
## |
?- artigo([o,rato],R3),substantivo(R3,[])
## |
## | (expandindoartigo:consome"o")
## |
?- substantivo([rato],[])
## |
## | (expandindosubstantivo:consome"rato")
## |
sucesso
Observe que cadapredicadotemdoisparˆametros:o primeirorepresenta a
listade palavrasa seremreconhecidase o segundorepresenta a listade palavras
aindan ̃ao reconhecidas.O reconhecimento terminacomsucessose todas as
palavrasda frasepodemser reconhecidas(consumidas)durante a busca.

Processamento de LinguagemNatural7
Vejamos,agora,um exemploondea frasen ̃ao pode ser reconhecida.Digitando
?- frase([o,gato,rato,ca ̧cou,o],[]).
o sistemaresponder ́ano. Para decidirque essafrasen ̃ao est ́a de acordocoma
gram ́atica,o sistemaprocededa seguinte forma:
?- frase([o,gato,rato,ca ̧cou,o],[])
## |
## | (expandindofrase)
## |
?- sujeito([o,gato,rato,ca ̧cou,o],R0),predicado(R0,[])
## |
## | (expandindosujeito)
## |
?- artigo([o,gato,rato,ca ̧cou,o],R1),substantivo(R1,R0),predicado(R0,[])
## |
## | (expandindoartigo:consome"o")
## |
?- substantivo([gato,rato,ca ̧cou,o],R0),predicado(R0,[])
## |
## | (expandindosubstantivo:consome"gato")
## |
?- predicado([rato,ca ̧cou,o],[])
## |
## | (expandindopredicado)
## |
?- verbo([rato,ca ̧cou,o],R2),artigo(R2,R3),substantivo(R3,[])
## |
## | (imposs ́ıvelconsumir"rato"comoverbo)
## |
fracasso
Noteque o sisteman ̃ao conseguereconhecera fraseporque,paraexpandiro
s ́ımbolo n ̃ao-terminalverbo, o sistemaprecisaconsumirum verbo, que deveria
ser a primeirapalavra da lista.Entretanto, comoa listainiciacomrato, e essa
palavra n ̃ao  ́e um verbo, o sistemafracassa.
Exerc ́ıcio 4Usandoa nota ̧c ̃aoDcg, especifiqueumagram ́atica capaz de reco-
nhecer as frases“o gatoe o rato correm pela casa”,“o gatoe o rato dormem
pela rua”e “o gatoe o rato dormemsilenciosamente”.§
Gera ̧c ̃ao autom ́aticade frases:Al ́em de reconhecer,usandooSwi-Prolog,
podemosgerartodas as frasesda linguagemdefinidapela gram ́atica,conforme
exemplificadoa seguir:
?- frase(F,[]).
F = [o,gato,ca ̧cou,o, gato];
F = [o,gato,ca ̧cou,o, rato];
F = [o,rato,ca ̧cou,o, gato];
F = [o,rato,ca ̧cou,o, rato];
no
O processode gera ̧c ̃ao  ́e semelhante ao processode reconhecimento; entre-
tanto, em vez de consumirpalavrasdurante as expans ̃oes, o sistemaas produz.

8S. L. Pereira
Exerc ́ıcio 5Usandoa nota ̧c ̃aoDcg, codifiqueas gram ́aticas dos exerc ́ıcios1
e 3, e utilizeoSwi-Prologpara gerar todas as frasesdas linguagensdefinidas
por essasgram ́aticas.§
3.1Concordˆanciade gˆenero
Agora,vamosampliara gram ́aticacomartigose substantivos femininos:
Gram ́atica3.Gram ́atica ampliadacom gˆenero feminino
frase-->sujeito,predicado.
sujeito-->artigo,substantivo.
predicado-->verbo,artigo,substantivo.
artigo-->[o]| [a].
substantivo-->[gato]| [gata]| [rato]| [rata].
verbo-->[ca ̧cou].
Usandoa gram ́aticaparareconhecera frase“o gataca ̧cou a rato”, obtemos:
?- frase([o,gata,ca ̧cou,a,rato],[]).
yes
Evidentemente, dever ́ıamosesperarque a respostafosseno. Entretanto, da
formacomofoi definida,a gram ́atican ̃ao tem comogarantir que artigose subs-
tantivos concordemem gˆenero.Para tanto, precisamosmodificara gram ́atica,
impondorestri ̧c ̃oes de gˆenero:
Gram ́atica4.Gram ́atica ampliadacom concordˆanciade gˆeneros
frase-->sujeito,predicado.
sujeito-->artigo(G),substantivo(G).
predicado-->verbo,artigo(G),substantivo(G).
artigo(m)-->[o].
artigo(f)-->[a].
substantivo(m)-->[gato]| [rato].
substantivo(f)-->[gata]| [rata].
verbo-->[ca ̧cou].
A modifica ̧c ̃ao que fizemosconsisteem definiros gˆenerosdos artigose subs-
tantivos (m- masculinoef- feminino)e exigirque eles tenhamo mesmogˆenero
G, quandoaparecemjuntos no sujeitoou no predicadode umafrase.
Para ver comoa restri ̧c ̃ao de gˆenerofunciona,analiseo processode reco-
nhecimento do sujeito“o gato”:

Processamento de LinguagemNatural9
?- sujeito([o,gato],[])
## |
## | (expandindosujeito)
## |
?- artigo(G,[o,gato],R0),substantivo(G,R0,[])
## |
| (expandindoartigo:consome"o" e deduzG="m")
## |
?- substantivo(m,[gato],[])
## |
| (expandindosubstantivo:consome"gato"do g^enero"m")
## |
sucesso
Agoracomparecomo processode reconhecimento do sujeito“o gata”:
?- sujeito([o,gata],[])
## |
## | (expandindosujeito)
## |
?- artigo(G,[o,gata],R0),substantivo(G,R0,[])
## |
| (expandindoartigo:consome"o" e deduzG="m")
## |
?- substantivo(m,[gata],[])
## |
| (imposs ́ıvelconsumir"gata"do g^enero"m")
## |
fracasso
Na verdade,na linguagemdefinidapela Gram ́atica4, haver ́a apenasfrases
comartigoconcordandocomsubstantivo em gˆerero:
?- frase(F,[]).
F = [o,gato,ca ̧cou,o, gato];
F = [o,gato,ca ̧cou,o, rato];
F = [o,gato,ca ̧cou,a, gata];
F = [o,gato,ca ̧cou,a, rata];
F = [o,rato,ca ̧cou,o, gato];
F = [o,rato,ca ̧cou,o, rato];
F = [o,rato,ca ̧cou,a, gata];
F = [o,rato,ca ̧cou,a, rata];
F = [a,gata,ca ̧cou,o, gato];
F = [a,gata,ca ̧cou,o, rato];
F = [a,gata,ca ̧cou,a, gata];
F = [a,gata,ca ̧cou,a, rata];
F = [a,rata,ca ̧cou,o, gato];
F = [a,rata,ca ̧cou,o, rato];
F = [a,rata,ca ̧cou,a, gata];
F = [a,rata,ca ̧cou,a, rata];
no
Exerc ́ıcio 6Modifiquea Gram ́atica 4, acrescentandotamb ́em os artigosin-
definidosumeuma. Em seguida,utilizeoSwi-Prologpara gerar todas frases
dessanovalinguagem.§

10S. L. Pereira
3.2Concordˆanciade n ́umero
Agora,vamosampliarmaisum poucoa nossagram ́atica,incluindoplural:
Gram ́atica5.Gram ́atica ampliadacom n ́umero
frase-->sujeito,predicado.
sujeito-->artigo(G),substantivo(G).
predicado-->verbo,artigo(G),substantivo(G).
artigo(m)-->[o]| [os].
artigo(f)-->[a]| [as].
substantivo(m)-->[gato]| [gatos]| [rato]| [ratos].
substantivo(f)-->[gata]| [gatas]| [rata]| [ratas].
verbo-->[ca ̧cou]| [ca ̧caram].
Comopodemosesperar,essagram ́atican ̃ao far ́a concordˆanciade n ́umero:
?- frase([os,gato,ca ̧cou,a,rata],[]).
yes
Para corrigi-la,tamb ́em vamosprecisarimpor restri ̧c ̃oes quanto ao n ́umero:
Gram ́atica6.Gram ́atica ampliadacom concordˆanciade n ́umero
frase-->suj(N),pred(N).
sujeito(N)-->artigo(N,G),substantivo(N,G).
predicado(N)-->verbo(N),artigo(M,G),substantivo(M,G).
artigo(s,m)-->[o].
artigo(p,m)-->[os].
artigo(s,f)-->[a].
artigo(p,f)-->[as].
substantivo(s,m)-->[gato]| [rato].
substantivo(p,m)-->[gatos]| [ratos].
substantivo(s,f)-->[gata]| [rata].
substantivo(p,f)-->[gatas]| [ratas].
verbo(s)-->[ca ̧cou].
verbo(p)-->[ca ̧caram].
Observe que,na regrade produ ̧c ̃ao paraf rase, o n ́umerodo sujeitoNdeve
concordarcomo n ́umerodo verbo no predicado.De formaan ́aloga,na regrapara
sujeito, artigoe substantivo devem ter o mesmon ́umeroN. Entretanto, na regra
parapredicado, o n ́umerodo verboNn ̃ao precisa,necessariamente, concordar
como n ́umeroM, do artigoe substantivo que seguemo verbo.

Processamento de LinguagemNatural11
Veja algunsexemplosde reconhecimento comconcordˆanciade n ́umero:
?- frase([os,gato,ca ̧cou,a,rata],[]).
no
?- frase([os,gatos,ca ̧cou,a,rata],[]).
no
?- frase([os,gatos,ca ̧caram,a,rata],[]).
yes
Exerc ́ıcio 7Modifiquea Gram ́atica 6, de modo a reconhecer sujeitocomposto
comosendoplural. Por exemplo,para o sujeitocomposto“o gatoe a gata”o
verbo “ca ̧car”deveestarno plural.§
3.3Tempo verbal
## ́
E poss ́ıvel ampliaraindamaisa gram ́aticaparaconsiderartempos verbais.Por
simplicidade,vamosconsiderarapenaspassado,presente e futurosimples.
Gram ́atica7.Gram ́atica ampliadacom tempo verbal
frase(T)-->sujeito(N),predicado(T,N).
sujeito(N)-->artigo(N,G),substantivo(N,G).
predicado(T,N)-->verbo(T,N),artigo(M,G),substantivo(M,G).
artigo(s,m)-->[o].
artigo(p,m)-->[os].
artigo(s,f)-->[a].
artigo(p,f)-->[as].
substantivo(s,m)-->[gato]| [rato].
substantivo(p,m)-->[gatos]| [ratos].
substantivo(s,f)-->[gata]| [rata].
substantivo(p,f)-->[gatas]| [ratas].
verbo(pas,s)-->[ca ̧cou].
verbo(pas,p)-->[ca ̧caram].
verbo(pre,s)-->[ca ̧ca].
verbo(pre,p)-->[ca ̧cam].
verbo(fut,s)-->[ca ̧car ́a].
verbo(fut,p)-->[ca ̧car~ao].
Nessanova vers ̃ao da gram ́atica,a cadaformado verbo “ca ̧car”  ́e associado
um tempo verbal.Assim,quandogerarmosumafrase,podemosindicaro tempo
verbalda frasea ser gerada.Analogamente, quandoo sistemareconheceruma
frase,ele indicar ́a o tempo verbaldessafrase.

12S. L. Pereira
Veja algunsexemplosde reconhecimento e gera ̧c ̃ao de frases,considerandoo
tempo verbal:
?- frase(T,[o,gato,ca ̧cou,o,rato],[]).
T = pas
yes
?- frase(pre,F,[]).
## F = [o,gato,ca ̧ca,o,gato]<enter>
yes
?- frase(fut,F,[]).
## F = [o,gato,ca ̧car ́a,o,gato]<enter>
yes
Exerc ́ıcio 8Especifiqueumagram ́atica para considerar pessoa e tempo verbal.
Considere que o sujeitopode ser apenasum dos pronomespessoais (eu,tu,ele,
n ́os,v ́os,eles) e que o verbo  ́efalar. Em seguida,utilizeoSwi-Prologpara
gerar a conjuga ̧c ̃ao desseverbo no tempo presente.§
3.4Constru ̧c ̃ao da  ́arvore sint ́atica
Vamosfazeruma ́ultimamodifica ̧c ̃ao na nossagram ́aticaparaque ela, ao reco-
nhecerou gerarumafrase,construatamb ́em a sua  ́arvore sint ́atica.
Gram ́atica8.Construindoa  ́arvore sint ́atica
## 4
frase(T,fra(S,P))-->sujeito(N,S),pred(T,N,P).
sujeito(N,suj(A,S))-->artigo(N,G,A),subst(N,G,S).
pred(T,N,prd(V,A,S))-->verbo(T,N,V),artigo(M,G,A),subst(M,G,S).
artigo(s,m,art(o))-->[o].
artigo(p,m,art(os))-->[os].
artigo(s,f,art(a))-->[a].
artigo(p,f,art(as))-->[as].
subst(s,m,sub(X))-->[X],{member(X,[gato,rato])}.
subst(p,m,sub(X))-->[X],{member(X,[gatos,ratos])}.
subst(s,f,sub(X))-->[X],{member(X,[gata,rata])}.
subst(p,f,sub(X))-->[X],{member(X,[gatas,ratas])}.
verbo(pas,s,ver(ca ̧cou))-->[ca ̧cou].
verbo(pas,p,ver(ca ̧caram))-->[ca ̧caram].
verbo(pre,s,ver(ca ̧ca))-->[ca ̧ca].
verbo(pre,p,ver(ca ̧cam))-->[ca ̧cam].
verbo(fut,s,ver(ca ̧car ́a))-->[ca ̧car ́a].
verbo(fut,p,ver(ca ̧car~ao))-->[ca ̧car~ao].
## 4
As condi ̧c ̃oes entre chaves s ̃ao executadascomoc ́odigonormaldoProlog.

Processamento de LinguagemNatural13
Veja um exemplode  ́arvore sint ́aticaconstru ́ıda a partirda Gram ́atica8:
?- frase(pre,A,[o,gato,ca ̧ca,o,rato],[]).
A = fra(suj(art(o),sub(gato)),prd(ver(ca ̧ca),art(o),sub(rato)))
## Yes
O valor na vari ́avelAdeve ser interpretadocomoa seguinte  ́arvore sint ́atica:
fra
## /\
## /\
sujprd
## / \/ | \
## /\/  |  \
artsubverartsub
## |||||
## |||||
o  gatoca ̧caorato
Exerc ́ıcio 9Modifiquea gram ́atica a seguir,de modo que ela possaser usada
para construiras  ́arvores sint ́aticas das frasesreconhecidaspor ela.
s -->sn,sv.
sn -->art,subst.
sv -->vi | vt,sn.
art-->[o].
subst-->[gato]| [rato].
vi -->[correu].
vt -->[comeu].
## §
## Referˆencias
1.Covington,M.NLPfor Prolog Programmers, Prentice-Hall,1994.
2.Covington,M.,Nute,D.andVellino,A.Prolog Programmingin Depth,
Prentice-Hall,1997.
3.Rich,E. andKnight,K.InteligˆenciaArtificial, 2
a
ed., MakronBooks,1995.
4.Russell,S. andNorvig,P.ArtificialIntelligence - a modernapproach, Prentice-
## Hall,1995.