## Hodina 13. októbra 2023

Program:

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli.
3. Geometria: Izometrie roviny - rýchle opakovanie
4. Domáca úloha (nová)
5. Program na budúci týždeň

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Videohovor** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

### 1. Domáca úloha

**Príklad 1**

1. Nájdite dĺžku vyznačenej úsečky.

![three_semicircles](img\three_semicircles.png)

Návod: toto nemusí byť nevyhnutne príklad na kruhovú inverziu, ale môže to byť aj príklad na podobné trojuholníky alebo oboje spolu. 

**Riešenie**

Už neviem, prečo som to nakreslil naopak. 

Dve kružnice po bokoch polkruhu sú kruhové inverzie malých kružníc podľa polkruhu. V rovnakej inverzii sa priamka AB zobrazuje sama na seba, rovnobežka s AB cez C je obrazom polkruhu, a obrazy malých kružníc sa musia oboch dotýkať. 

![image-20231003020138478](img\cCc.png)

Vieme, že AB=8. Označme polomer polkružnice R, potom R=4. Polomery menších kružníc sú po rade $r_1 = R/2,\, r_2= R/4$.

Trojuholník OBG je pravouhlý, pričom $OB=R/2, \quad OG = R + R/2$ a teda 
$$
BG^2 = (3R/2)^2 - (R/2)^2 = 2R^2 \\
BG = \sqrt{2}\cdot R
$$
Trojuholník OIJ je podobný trojuholníku OGH, takže 
$$
\frac{IJ}{OI} = \frac{GH}{OG}\quad \implies \quad IJ = \frac{GH}{OG} OI = \frac{2\sqrt{2}R}{3R/2}R = \frac{16\sqrt{2}}{3} \approx 7.542
$$
Táto úloha ide riešiť aj bez kruhovej inverzie, ale  bez trojuholníka OGH to je zložitejšie. 

---

**Príklad 2**

2. Nájdite a, pre ktoré má funkcia 

$$
f(x) = \sqrt{ax^2 + x}
$$

rovnaký definičný obor ako rozsah hodnôt.

**Riešenie**

Pozrime sa, či vieme rýchlo nájsť nejaké riešenie metódou "pozriem a vidím". Najjednoduchšie je sústrediť sa na hodnoty a, ktoré celý výraz nejako trivializujú, a to je v našom prípade a=0. 

Pre a=0 je $f(x)=\sqrt{x}$, s definičným oborom $D(f)= \langle 0, \infty)$ a rovnakým oborom hodnôt., takže a=0 je riešenie. 

Na druhej strane, odmocnina je nezáporná, a teda obor hodnôt bude nejaká podmnožina intervalu $\langle 0, \infty)$. Ale pre kladné a máme pod odmocninou kladné hodnoty aj pre veľké záporné x, takže $a \le 0$.

Takže môžeme svoje pátranie sústrediť na záporné a . Pre tieto hodnoty vyzerá funkcia $ax^2+x$ takto (červená a=-1, modrá a=-2, zelená a=-3).

<img src="img\ax2plusx.png" alt="ax2plusx" style="zoom:53%;" />

Pretože $ax^2 + x = ax(x + 1/a)$,  bude pre $a<0$ definičný obor funkcie f $\langle 0, -1/a \rangle$. Obor hodnôt bude medzi nulou a maximom funkcie, Funkcia zjavne nadobúda maximálnu hodnotu uprostred definičného intervalu, teda pre $x = -1/(2a)$., a hodnota maxima je 
$$
f_{max}^2 = a\frac{1}{4a^2} - \frac{1}{2a} = - \frac{1}{4a} \\
f_{max} = \sqrt{- \frac{1}{4a}}
$$
Aby sa definičný obor rovnal oboru hodnôt, musí platiť
$$
- \frac{1}{a} =  \sqrt{- \frac{1}{4a}} \\
a^2 = -4a \quad a(a+4) = 0
$$
Odtiaľ máme a=4, ale nie a=0, pretože pre túto hodnotu neplatia prakticky žiadne úvahy v posledných odstavcoch. 

Záver: Funkcia $f(x) = \sqrt{ax^2 + x}$ má rovnaký definičný obor a obor hodnôt pre a=0 a a=-4. Samozrejme si ukážeme aj víťazné riešenie. 

<img src="img\ax2plusx_soln.png" alt="image-20231003033701984" style="zoom:67%;" />

---

**Príklad 3**

3. Vyriešte 

![image-20230929214615231](img\two-circles-and-a-square.png)

**Riešenie**

Najprv odvoďme výraz pre polomer kružnice vpísanej do pravouhlého trojuholníka. 

Uvažujme trojuholník CBF na obrázku. Bisektory uhlov, v ktorých priesečníku leží stred vpísanej kružnice, ho rozdeľujú na tri trojuholníky BGC, CGF, FGB.  



![image-20231006002333031](img\circles_in_triangle.png)

Pozorovanie za euro: Tieto tri trojuholníky majú rovnakú výšku, a teda vieme zrátať ich obsah. Teraz to už je ľahké:
$$
S_{BFC} = S_{BGF} + S_{FGC} + S_{CGB} \\
\frac{ab}{2} = \frac{ar}{2} + \frac{br}{2} + \frac{cr}{2} \\
r = \frac{ab}{a+b+c} = \frac{S}{s}\quad S \equiv \frac{ab}{2},\quad  s \equiv \frac{a+b+c}{2}
$$
Mimochodom, toto je špeciálny prípad vzťahu pre polomer vpísanej kružnice r a opísanej kružnice R pre všeobecný trojuholník :
$$
rR = \frac{abc}{2(a+b+c)}
$$
Ešte jeden vzťah pre polomer vpísanej kružnice je 
$$
\frac{1}{r} = \frac{1}{v_a} + \frac{1}{v_b} + \frac{1}{v_c}
$$
a pre pravouhlý trojuholník sa redukuje na predošlý vzťah.

Hoci vzťah pre r vyzerá jednoducho, dá sa prekvapivo ešte viac zjednodušiť:
$$
r = \frac{ab}{a+b+c} = \frac{ab(a+b-c)}{(a+b+c)(a+b-c)}=\frac{ab(a+b-c)}{(a+b)^2 - c^2}=\frac{ab(a+b-c)}{(a^2+b^2-c^2) + 2ab}=\frac{a+b-c}{2}
$$
Pozrime sa na obvod pravouhlého trojuholníka a jeho vzťah k polomeru vpísanej kružnice:

1. Zjavne $a+b-c$ = a + b - (a - r) - (b - r)  = 2r$ v súlade s predošlým vzťahom.
2. $a+b+c = a + b + a - r + b - r = 2a + 2b - 2r$.

![image-20231012173159639](img\two-circles-and-a-square2.png)

Vráťme sa teraz k nášmu zadaniu so štvorcom a dvoma vpísanými kružnicami.  Toto je ťažký príklad, pretože sa ľahko môžeme utopiť v mori podobných trojuholníkov. 

Nech je pre jasnosť v trojuholníku zo zadania $a$ zvislá odvesna, $b$ vodorovná, $c$ prepona. Stranu štvora označíme $x$, ale polomery vpísaných kružníc označíme veľkými písmenami $A, B$, aby sa nám neplietli označenia. 

Začneme tým, že dvoma spôsobmi vyjadríme plochu horného trojuholníka. Jeho strany sú $a-x$, $x$, a $a-x-A + x-A = a - 2A$. Pripomínam, že to sú iné označenia ako na predošlom obrázku a vzťahujú sa k trojuholníku zo zadania. Plocha trojuholníka je 
$$
S = \frac{1}{2}(a-x)x
$$
ale môžeme ju vyjadriť aj ako 
$$
S = sA
$$
kde $s$ je polovičný obvod horného trojuholníka
$$
s = \frac{1}{2}(a-x + x + a - 2A) = a - A
$$
a teda 
$$
S = \frac{1}{2}(a-x)x = (a-A)A
$$
Potrebujeme x v termínoch A a B, takže potrebujeme eliminovať $a$. Z podobnosti trojuholníkov s vpísanými kružnicami máme:
$$
\frac{a-x}{x} = \frac{A}{B}
$$
odkiaľ 
$$
a - x = \frac{A}{B}x \quad a = \frac{A+B}{B}x 
$$
Z rovnosti dvoch výrazov pre S máme
$$
(a-x)x = 2(a-A)A \\
\frac{A}{B}x^2 = 2\frac{A + B}{B}Ax - 2A^2 \\
x^2 = 2(A + B)x -2AB \\
x^2 - 2(A + B)x + 2AB = 0 \\
x_{1,2} = \frac{2(A+B) \pm \sqrt{4(A+B)^2 - 8AB}}{2} \\
x_{1,2} = A + B \pm \sqrt{A^2+B^2}
$$
 Máme dve reiešenia, ale z obrázku k zadaniu vidno, že $2A < x, \,2B<x$ a teda $A+B<x$. Z toho vyplýva, že prípustné je iba riešenie s plusom, a teda 
$$
\mathbf{x = A + B + \sqrt{A^2+B^2}}
$$
**Iné riešenie**

Zatiaľčo prvé riešenie nám umožnilo začať niekoľkými poznatkami o vpísaných kružniciach, toto riešenie dobre demonštruje stratégiu irešenia takýchto úloh: Nájdi niečo, čo sa dá vyjadriť viacerými spôsobmi.

![image-20231012220732695](img\two-circles-and-a-square3.png)

V tomto prípade je tým "niečím" vzdialenosť medzi stredmi vpísaných kružníc, ktorá je preponou dvoch rôznych pravouhlých trojuholníkov, a to takých, ktorých strany vieme vyjadriť pomocou a, b, x (v tomto riešení vôbec nepoužívame označenie strán pravouhlého trojuholníka, takže môžeme použiť označenie podľa zadania). 

Predovšetkým, vzdialenosť bodov dotyku kružníc na prepone veľkého trojuholníka je
$$
|T_1T_2| = |DT_1| + |DT_2| = x - a + x - b = 2x - a - b
$$
Modrý trojuholník $O_1KO_2$ má odvesny $O_1K = 2x - a - b$ a $O_2K = b-a$. Zelený trojuholník $O_1LO_2$ má odvesny $O_1L = x + a - b$ a $LO_2 = x+b-a$.  Pomocou Pythagorovej vety vyjadríme preponu $O_1O_2$ z oboch trojuholníkov a dáme do rovnosti:
$$
O_1O_2^2 = (2x - a - b)^2 + (b-a)^2 = (x+a-b)^2 + (x+b-a)^2
$$
To je výraz, obsahujúci iba $a, b, x$. Upravíme a vyjadríme x:
$$
4x^2 + a^2 + b^2 - 4xa - 4xb + 2ab + b^2 + a^2 - 2ab = 2x^2 + 2a^2 + 2b^2 - 4ab
$$





---





## 2. Príklady na zahriatie

**Príklad 1: cos(1°) je iracionálne číslo**

alebo matematická indukcia naopak: pomocou matematickej indukcie ukazujeme, že platnosť base case vedie k logickým rozporom.

![F7H4EUxXcAAL4QI](img\F7H4EUxXcAAL4QI.jpg)

---

#### "Sila" bodu - Power of a point

Poďme zovšeobecniť tvrdenie, ktorého špeciálny prípad sme už mali:

![Pop](img\Pop.PNG)

- Pre pretínajúce sa tetivy platí $AE . CE = DE . BE$
- Pre dotyčnicu a tetivu platí $AB^2 = BC . BD$
- Pre tetivy pretínajúce sa mimo kruhu platí $CB.CA = CD.CE$.

Prvé tvrdenie sme dokazovali pomocou podobnosti trojuholníkov AED a BEC.

Tretie tvrdenie: trojuholníky CDA a CBE sú si podobné, pretože zdieľajú uhol BCD a uhly CBE a ADE sú rovnaké (rovnaké sú uhly ABE a ADE, pretože sú to obvodové uhly zodpovedajúce tetive AB).

Druhé tvrdenie je limitným prípadom tretieho pre B → A.

#### Kruhová inverzia

Doteraz sme sa zaoberali izometriami - teda zobrazeniami, ktoré zachovávajú vzdialenosti bodov. Dnes sa krátko pozrieme na zobrazenie, ktoré nie je izometriou: kruhovú inverziu. 

Majme kruh so stredom O, ohraničený kružnicou k o polomere $r$. Kruhová inverzia zobrazí body vnútri kružnice k na doplnok kruhu v rovine a body mimo kruhu dovnútra kruhu. 

Konkrétne, bod P sa zobrazí do bodu P' na priamke OP tak, že $OP.OP^{\prime} = r^2$

- Body vnútri kruhu sa zobrazia do bodov mimo kruhu
- Body mimo kruhu sa zobrazia dovnútra kruhu
- Body na kružnici sa zobrazujú samy na seba .

![image-20230929094702601](img\ci_1.png)

Ako z obrázka vyplýva, že $OP.OP^{\prime}$?

**Inverzia kružnice, prechádzajúcej stredom**

![image-20230929100234778](img\ci_2.png)

Stred invertujúcej kružnice sa zobrazuje do nekonečne vzdialeného bodu. Preto kružnica prechádzajúca stredom sa zobrazuje na kružnicu s nekončným polomerom - priamku.

Pretože 
$$
OP \cdot OP^{\prime} = r^2 \\
OQ \cdot OQ^{\prime} = r^2 \\
\frac{OQ}{OP} = \frac{OQ^{\prime}}{OP^{\prime}}
$$
a uhol pri O majú trojuholníky $OPQ$ a $OQ^{\prime}P^{\prime}$ spoločný, sú si tieto trojuholníky podobné. Pretože $OPQ$ je pravouhlý trojuholník, musí byť pravouhlý aj trojuholník $OQ^{\prime}P^{\prime}$. Teda kružnica c sa zobrazuje na priamku, kolmú na OP a prechádzajúcu bodom $P^{\prime}$.

**Inverzia ľubovoľnej kružnice**

![image-20230929102541019](img\ci_3.png)

Pre dôkaz, že obrazy všetkých bodov kružnice c ležia na kružnici c' stačí dokázař, že trojuholník P'Q'R' je pravouhlý. (**domáca úloha**)

**Výraz pre polomery kružnice a jej obrazu**

Nech R je polomer kružnice k (teda tej, okolo ktorej robíme inverziu, r polomer kružnice c vnútri k a r' polo

mer obrazu kružnice c:)

![image-20230929110901420](img\ci_4.png)
$$
\frac{r}{r^{\prime}} = \frac{OP^{\prime} - OQ^{\prime}}{OQ - OP} \\
= \frac{\frac{R^2}{OP} - \frac{R^2}{OQ}}{OQ - OP} = \frac{R^2}{OQ \cdot OP}
$$
Pretože podľa vety o sile bodu $OQ \cdot OP = OR^2 = OC_2^2 - r^{\prime 2}$ , máme konečne
$$
r = \frac{R^2r^{\prime}}{OC_2^2 - r^{\prime 2}}
$$
Upozorňujem, že vlastnosť "byt stredom kružnice" sa pri kruhovej inverzii nezachováva. Teda obraz bodu C nie je stredom obrazu kružnice c, preto aj má íné označenie. 

#### Načo to  je dobré

Niekedy je výhodné transformovať kružnce na priamky a kružnice na iné kružnice. Typický príklad je toto:

Aké sú polomery kružníc v postupnosti $C_2, C_3, \dots$, ak polomer kružnice $C$ je r=1 a kružnice $C_1$ $r_1$?

![Circle_sequence_0](img\Circle_sequence_0.png)

**Riešenie**

sa opiera o kruhovú inverziu okolo červenej kružnice. Je také estetické, že sa človeku ani nechce počítať, pretože to sú samé pravouhlé trojuholníky. 



![Circle_sequence](img\Circle_sequence.png)

Poďme počítať. 

- Polomer projekčnej kružnice (červenej) je $OT \equiv R =2$. 
- Polomer veľkej kružnice (so stredom C) je podľa zadania 1 
- a polomer menšej kružnice so stredom $C_1$ je podľa zadania r. 
- Polomer kružnice so stredom $C_2$ je $UC_1 \equiv r_2 =1-r_1$.  
- Obraz kružnice so stredom C je  dotyčnica prechádzajúca bodom T. 
- Obraz kružnice so stredom $C_1$ je rovnobežka s dotyčnicou prechádzajúca bodom $U^{\prime}$. Platí $OU \cdot OU^{\prime} = R^2 = 4$ a teda 

$$
OU^{\prime} = 2 + 2r_2^{\prime} = \frac{4}{2r_1} \\
r_2^{\prime} = \frac{1-r_1}{r_1} = \frac{r_2}{r_1}
$$

- Ako som už písal, vlastnosť "byť stredom kružnice" sa pri kruhovej inverzii nezachováva, takž obrazy stredov kružníc $C_2^{\prime}, C_3^{\prime}, \dots$ nie sú totožné so stredmi obrazov kružníc $S_2, S_3, \dots$
- Budeme ešte potrebovať vzdialenosť $OC_2^{\prime} = 1 + \frac{1}{r_1}$.
- Stredy kružníc $C_2, C_3, \dots$ ležia na kružnici o polomere $\rho = r_1 + r_2/2$.

Teraz už môžeme začať počítať:

Začneme s pravouhlým trojuholníkom $OS_2S_3$. Z Pytagorovej vety máme 
$$
OS_3 = \sqrt{ (2 + r_2^{\prime})^2 + (2r_2^{\prime})^2}
$$
Trojuholník $OC_2C_3$ je tiež pravouhlý a pretože má spoločný uhol s trojuholníkom $OS_2S_3$, sú si tieto trojuholníky podobné. Preto
$$
\frac{C_2C_3}{OC_2} \equiv \frac{r_2 + r_3}{2-r_2} = \frac{2r_2^{\prime}}{OS_3} \equiv \frac{S_2S_3}{OS_3
}
$$
Prostredná rovnosť nám dáva vzťah, z ktorého môžeme vyjadriť $r_3$ v termínoch $r_1$.

Podobne môžeme vyjadriť polomery ďalších kružníc. 

---

## 3. Geometria

Dnes sme najviac urobili na domácu úlohu. 

### 5 izometrií roviny

Každú izometriu roviny (teda zobrazenie, zachovávajúce vzdialenosti) vieme vyjadriť ako jedno z piaich základných zobrazení: zrkadlenie, posunutie, rotácia, stredová súmernosť, posunuté zrkadlenie. 

- Zrkadlenie
- Posunutie
- Rotácia
- Stredová symetria
- Posunuté zrkadlenie

### Ďalšie tvrdenia

Toto budeme dokazovať nabudúce:

- Každú izometriu môžeme vyjadriť ako kompozíciu najviac troch zrkadlení. 
- Každú izometriu môžeme vyjadriť ako kompozíciu posunutia a izometrie s najmenej jedným pevným bodom.
- Kompozícia rotácie a posunutia je rotácia (má pevný bod!)

#### 1. Rotácia + posunutie = rotácia

![image-20231013004627795](img\rot-plus-trans-is-rot.png)

Tieto tvrdenia dokazujeme kombináciou dvoch vecí:

- invariancie rotácií a translácií k rotáciám, resp. transláciám zrkadlení, ktoré ich tvoria.
- algebry zobrazení

Namiesto vysvetľovania poďme tvrdenie dokázať:

Máme priamky f, g, h, i. Priamky f, g sa pretínajú v bode A a zrkadlenia okolo nich tvoria rotáciu. Priamky h, i sú rovnobežné a zrkadlenia okolo nich tvoria posunutie. Celkové zobrazenie je kompozícia rotácie a zrkadlenia:
$$
Z = \underbrace{\sigma_i \circ \sigma_h}_{T} \circ \underbrace{\sigma_g \circ \sigma_f}_{R}
$$
Najprv využijeme, že zrkadlenia okolo priamok f, g rotovaných o ľubovoľný uhol $\alpha$ okolo bodu A definujú rovnakú rotáciu. Preto môžeme túto dvojicu priamok otočiť tak, aby sa priamka g stala rovnobežnou s priamkami h, i. Tieto priamky sú označené f', g'.  Teraz využijeme fakt, že zrkadlenia okolo priamok h, i posunutých v kolmom smere o ľubovoľnú vzdialenosť d definujú rovnaké posunutie. Preto môžeme túto dvojicu priamok posunúť tak, aby priamka h splynula s priamkou g'.

Naše zobrazenie teraz vyzerá takto:
$$
Z = \sigma_{i'} \circ \underbrace{\sigma_{h'} \circ \sigma_{g'}}_{id} \circ \sigma_{f'} = \sigma_{i'} \circ \sigma_{f'}
$$
Priamky g' a h' sú totožné, takže kompozícia zrkadlení okolo nich je identické zobrazenie. Zostáva nám kompozícia dvoch zrkadlení okolo priamok f' a i', ktorá je rotáciou okolo priesečníka týchto priamok A'. 

Kompozícia rotácie a posunutia je znova rotácia. 

**Domáca úloha** Dokážte, že rovnaké tvrdenie platí aj o opačnej kompozícii posunutia a rotácie. 



#### 2. Kompozícia zrkadlení okolo troch rôznobežných priamok je posunuté zrkadlenie.

Majme tri po dvojiciach rôznobežné priamky f, g, h, pretínajúce sa v bodoch A, B, C (čierne čiary). Dokážeme, že zobrazenie, zložené zo zrkadlení okolo priamok f, g, h je ekvivalentné posunutému zrkadleniu. 

![image-20231013023815691](C:\Users\kvasn\Documents\GitHub\Erik\img\three_lines_is_SGS.png)

Postupujeme rovnako ako v predchádzajúcom prípade: sérou dvoch otočení prevedieme sústavu priamok na dve rovnobežky a kolmicu na ne. 

- Otočíme priamky g, h okolo ich priesečníka C o rovnaký uhol, aby priamka g' bola kolmá na f (modré čiary). 
- Teraz budeme otáčať dvojicou na seba kolmých priamok f a g' tak, aby sa priamka g'' stala rovnobežnou s h' (červené čiary). 

Výsledkom je kompozícia zrkadlení okolo červenej priamky f' a dvojice na ňu kolmých priamok g'' (červenej)  a h' (modrej), čo je posunuté zrkadlenie.



#### 3. Dve bodové zrkadlenia sú ekvivalentné posunutiu

**Pomocná veta**

Nech f, g sú na seba kolmé priamky. Potom zobrazenie, vzniknuté kompozíciou zrkadlení okolo priamky f a potom okolo priamky g je rovnaké ako zobranie, vzniknuté zložením týchto zrkadlení v opačnom poradí:
$$
\sigma_g \circ \sigma_f = \sigma_f \circ \sigma_g
$$
Toto tvrdenie môžeme veľmi užitočne formulovať tak, že zrkadlenia okolo navzájom kolmých priamok *komutujú*.

**Dôkaz**

Zložené zrkadlenie okolo dvoch kolmých priamok je bodové zrkadlenie či stredová súmernosť, a ako zrkadlenie je involúciou, teda sa rovná svojmu inverznému zobrazeniu. Aby sme ale boli dôkladní, uvedomíme si, že priamky f, g môžeme okolo ich priesečníka otočiť o ľubovoľný uhol a dostaneme to isté zobrazenie. Tento uhol môže byť aj 90°, čo je práve tvrdenie tejto vety. $\square$

Teraz už ľahko dokážeme tvrdenie z nadpisu tejto časti. Nech f, g, h, i sú také priamky ,že 

- f, g, sú na seba kolmé a pretínajú sa v bode P
- h, i sú na seba kolmé a pretínajú sa v bode Q.

Bez ujmy na všeobecnosti môžeme predpokladať, že f je rovnobežné s h a g je rovnobežné s i (ak nie sú, môžeme ich do tejto polohy pootočiť okolo bodov P, resp. Q). Potom celkové zobrazenie je
$$
Z = \underbrace{\sigma_i \circ \sigma_h}_{P_Q} \circ \underbrace{\sigma_g \circ \sigma_f}_{P_P} = \sigma_i \circ \sigma_g \circ \sigma_h \circ \sigma_f = \underbrace{\sigma_i \circ \sigma_g}_{T_{gi}} \circ \underbrace{\sigma_h \circ \sigma_f}_{T_{fh}}
$$
čo je kompozícia dvoch posunutí a je teda tiež posunutím. To by sme ale tiež mali dokázať!

**Domáca úloha** Dokážte, že kompozícia dvoch posunutí je tiež posunutie.



#### 4. Tri bodové zrkadlenia sú ekvivalentné jednému

**Domáca úloha**

---



## 4. Domáca úloha (nová)

Okrem úloh, zadaných v texte, dáme ešte dva príklady:

1. Dve rotácie okolo bodov $P_1, P_2$ sú ekvivalentné jedinej rotácii. Zostrojte túto rotáciu. 

2. Nájdite a, pre ktoré má funkcia 







---



## 5. Program na budúci týždeň



