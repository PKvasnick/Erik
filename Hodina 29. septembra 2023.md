## Hodina 29. septembra 2023

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

Trojuholník má strany 4 m, 11 m a 8 m. Vypočítajte jeho vnútorné uhly. 

**Riešenie**

Označme $a=4\,m,\,b=11\,m,\,c=8\,m$. 

Použijeme kosínovú vetu
$$
\cos{\gamma} = \frac{a^2 + b^2 - c^2}{2ab} \\
\cos{\gamma} = \frac{16 + 121 - 64}{2\cdot 4 \cdot 11} = \frac{73}{88} = 33,95°
$$

$$
\cos{\beta} = \frac{a^2 + c^2 - b^2}{2ac} \\
\cos{\beta} = \frac{16 + 64 - 121}{2\cdot 4 \cdot 8} = \frac{-41}{64} = 129,84°
$$

$$
\cos{\alpha} = \frac{b^2 + c^2 - a^2}{2bc} \\
\cos{\alpha} = \frac{121 + 64 - 16}{2\cdot 11 \cdot 8} = \frac{169}{176} = 16,21°
$$

Všetko dokopy 180°, takže to sedí. Mohli sme  po prvom použití kosínovej vety použiť sínusovú vetu, ale je to iba trocha jednoduchšie na počítanie. 

---

**Príklad 2**

Majme tri rovnobežné priamky f, g, h. Dokážte,že existuje priamka j taká, že pre zrkadlenia okolo priamok f, g, h , j platí $\sigma_h \circ \sigma_g \circ \sigma_f = \sigma_j$ - teda že tri zrkadlenia môžeme nahradiť jediným. Kde leží priamka j?

**Riešenie**

*A. Naivné kreslenie a počítanie*

![three_lines](img\three_lines.png)

Poďme počítať posunutia. Majme bod $X$ v polohe $x$ na súradnicovej osi, a tri priamky $f, g, h$ kolmé na os x v polohách $x_1, x_2, x_3$. Počítajme postupne transformácie pri zrkadleniach okolo priamok $f, g, h$:
$$
x^{\prime} = x_1 - (x-x_1) = 2x_1 - x \\
x^{\prime \prime} = x_2 - (x^{\prime} - x_2) = 2x_2 - x^{\prime} = 2x_2 - 2x_1 + x \\
x^{\prime \prime \prime} = x_3 - (x^{\prime \prime} - x_3) = 2x_3 - x^{\prime \prime} = 2x_3 - 2x_2 + 2x_1 - x = 2(x_3 - x_2 + x_1) - x \\
$$
a teda výsledok je ekvivalentný zrkadleniu okolo priamky, kolmej na os x a v polohe $x_1 - x_2 + x_3$.

*B. Algebra zobrazení*

Ale to nie je dosť a hlavne by nám to vôbec nepomohlo pre ďalší príklad, kde priamky zrkadlení nie sú rovnobežné. Ešte jeden prístup, ktorý môžeme použiť, spočíva v tom, že si uvedomíme, že zrkadlenie je involúcia, teda je rovnaké ako jeho inverzné zobrazenie. To tiež znamená, že platí
$$
\sigma_g \circ \sigma_g \circ \sigma_h \circ \sigma_j = id
$$
A teraz sa pozrime na kompozíciu prvých dvoch zrkadlení. Ide o zrkadlenie okolo dvoch rovnobežných priamok a teda sa jedná o posunutie. Aby sme zrušili efekt zobrazenia $\sigma_f \circ \sigma_g$, musíme zo zvyšných dvoch zobrazení skonštruovať rovnaké posunutie, ale v opačnom smere. Inak povedané, 

- priamka j sa nachádza od priamky h v rovnakej vzdialenosti ako priamka g od priamky f
- priamka j leží na opačnej strane priamky h než priamka g od priamky f. 

Takto sa nám posunutia zrušia. 

*C. Geometrická konštrukcia*

Geometricky môžeme zostrojiť priamku výsledného zrkadlenia. Môžeme ale aj dokázať, že sa jedná o jednoduché zrkadlenie okolo priamky (Geradespiegelung), a to tak, že ukážeme, že zobrazenie má dva fixné body a nie je identické. Za tým účelom stačí zostrojiť obraz dvoch priamok, rôznobežných s f, g, h. Priesečníky týchto priamok sú fixné body výsledného zobrazenia, a ak zostrojíme dva, musí byť výsledné zobrazenie zrkadlením okolo priamky. 

![2x2x4_lines](img\2x2x4_lines.png)

---

**Príklad 3**

Majme tri priamky f, g, h, pretínajúce sa v jedinom bode. Dokážte,že existuje priamka j taká, že pre zrkadlenia okolo priamok f, g, h , j platí $\sigma_h \circ \sigma_g \circ \sigma_f = \sigma_j$ - teda že tri zrkadlenia môžeme nahradiť jediným. Kde leží priamka j?

**Riešenie**

Tu naivné obrázky nepomôžu, a algebra funguje rovnako ako v predchádzajúcom prípade:

*A. Algebra zobrazení*

Zrkadlenie je involúcia, teda je rovnaké ako jeho inverzné zobrazenie. To tiež znamená, že platí
$$
\sigma_g \circ \sigma_g \circ \sigma_h \circ \sigma_j = id
$$
A teraz sa pozrime na kompozíciu prvých dvoch zrkadlení. Ide o zrkadlenie okolo dvoch rôznobežných priamok a teda sa jedná o rotáciu. Aby sme zrušili efekt zobrazenia $\sigma_f \circ \sigma_g$, musíme zo zvyšných dvoch zobrazení skonštruovať rovnakú rotáciu, ale v opačnom smere. Inak povedané, 

- priamka j prechádza spoločným priesečníkom priamok f, g, h.
- priamka j zviera s priamkou h opačný uhol ako priamka g s priamkou f (veľkosti uhlov meriame proti smeru hodinových ručičiek)

Takto sa nám otočenia zrušia. 

*B. Geometrická konštrukcia*

Pretože poznáme jeden bod priamky j, stačí zostrojiť ľubovoľný iný bod. 

![1x1x3_lines](img\1x1x3_lines.png)

---

**Príklad 4**

Strana trojuholníka má dĺžku 1. Nájdite obsah zelenej plochy. 

![equilateral_triangle3](img\equilateral_triangle3.gif)

**Riešenie**

Uvažujem trojuholník AMO. Je pravouhlý, a súčet jeho prepony AO a odvesny MO je rovný výške trojuholníka ABC. Z Pytagorovej vety máme 
$$
(v-r)^2 = r^2 + \left(\frac{a}{2}\right)^2 \\
v^2 - 2vr + r^2 =  r^2 + \left(\frac{a}{2}\right)^2 \\
\frac{3a^2}{4} - \sqrt{3}ar = \frac{a^2}{4} \\
r = \frac{\sqrt{3}}{6} = \frac{v}{3}
$$
Teraz už stačí odčítať plochu kruhu od plochy trojuholníka a výsledok vydeliť troma. 
$$
S = \frac{S(\Delta) - S(\circ)}{3} \\
= \frac{1}{3}\left(\frac{\sqrt{3}}{2} - \pi \frac{3}{36} \right) a^2 \\
\approx 0.2014
$$

---

**Príklad 5**

Polomer kružníc je 1. Vypočítajte obsah červenej plochy.

![equilateral_triangle6](img\three_circles.png)

**Riešenie**

Stredy troch kruhov okolo červenej plochy tvoria rovnostranný trojuholník so stranou a = 2r. Tri časti kruhov majú stredový uhol 60°, teda spolu 180°.  Plocha červenej oblasti teda je
$$
S = S(\Delta) - S(◗) = \frac{\sqrt{3}}{2}(2r)^2 - \frac{\pi}{2}r^2 = \frac{4\sqrt{3} - \pi }{2}r^2 \\
\approx 1.893
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



---



## 4. Domáca úloha (nová)

1. Nájdite dĺžku vyznačenej úsečky.

![three_semicircles](img\three_semicircles.png)

Návod: toto nemusí byť nevyhnutne príklad na kruhovú inverziu, ale môže to byť aj príklad na podobné trojuholníky alebo oboje spolu. 

2. Nájdite a, pre ktoré má funkcia 

$$
f(x) = \sqrt{ax^2 + x}
$$

rovnaký definičný obor ako rozsah hodnôt.

3. Vyriešte 

![image-20230929214615231](img\two-circles-and-a-square.png)

---



## 5. Program na budúci týždeň

- Dôkaz Ptolemaiovej vety pomocou kruhovej inverzie

- izometrie v rovine: zložitejšie tvrdenia a príklady

  
