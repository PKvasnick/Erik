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

---

## 3. Geometria

Mali sme posledne, dnes na ňu neostane čas.

### Zrkadlenie

**Definícia**

Majme priamku $g$ a uvažujme takéto zobrazenie $\sigma_g$ Euklidovskej roviny $E_2$ na seba:

- $X \in g:\quad \sigma_g(X) = X$ 
- $X \notin g: \quad \sigma_g(X) = Y, d(X, g) = d(Y, g) \and XY \perp g$

<img src="C:\Users\kvasn\Documents\GitHub\Erik\img\spiegelung.png" alt="spiegelung" style="zoom:20%;" />

Takéto zobrazenie sa nazýva zrkadlenie okolo osi $g$.

**Tvrdenie 1**

Zrkadlenie je *_involúcia_*, teda si je samo sebe inverzným zobrazením: $\sigma_g \circ \sigma_g = I$ (identické zobrazenie), resp. $\sigma_g^{-1} = \sigma_g$

**Tvrdenie 2**

Zrkadlenie je *_izometria_*, teda zachováva vzdialenosti: $X^\prime = \sigma_g(X), Y^\prime = \sigma_g(Y) \implies d(X, Y) = d(X^\prime, Y^\prime)$.

Izometrií roviny je 5 (zrkadlenie, posunutie, bodová súmernosť, rotácia, posunutá rotácia) a všetky možno zostrojiť kombináciou niekoľkých zrkadlení. 

**Tvrdenie 3**

3a. Všetky body na osi zrkadlenia sú pevnými bodmi zrkadlenia a zrkadlenie nemá žiadne iné pevné body.

3b. Pevné priamky zrkadlenia sú os zrkadlenia a všetky priamky na ňu kolmé. 

### Posunutie

Zložené zobrazenie pozostávajúce z dvoch zrkadlení okolo rovnobežných priamok f a g je posunutie. 

Ak zrkadlenia označíme $\sigma_f, \sigma_g$, potom môžeme formálne písať $T = \sigma_g \circ \sigma_f$.  Ľahko zistíme, že inverzné zobrazenie je $T^{-1} = \sigma_f \circ \sigma_g$. Skutočne, 
$$
TT^{-1} = (\sigma_g \circ \sigma_f) \circ (\sigma_f \circ \sigma_g) = \sigma_g \circ (\sigma_f \circ \sigma_f) \circ \sigma_g = \sigma_g \circ \sigma_g = I \\
T^{-1}T = (\sigma_f \circ \sigma_g) \circ (\sigma_g \circ \sigma_f) = \sigma_f \circ (\sigma_g \circ \sigma_g) \circ \sigma_f = \sigma_f \circ \sigma_f = I
$$
pretože zrkadlenie je involúcia. 

Veľkosť posunutia je dvojnásobok vzdialenosti  medzi priamkami a smer je kolmý na obe rovnobežky. 

![posunutie](img\posunutie.png)

- Posunutie nemá pevný bod
- Pretože je kompozíciou dvoch izometrií, je posunutie tiež izometria.
- Dve priamky rovnobežné s f a g a s rovnakou vzdialenosťou ako medzi f a g realizujú rovnaké posunutie. 
- Priamky rovnobežné s posunutím sa zobrazujú na seba. 

Posunutie v rovine je vo všetkých bodoch rovnaké, a teda na jeho rekonštrukciu stačí jeden bod a jeho obraz, čo stačí na rekonštrukciu vektora posunutia. 

Medzi vektormi a posunutiami je priradenie 1:1, a preto sa niekedy vektor priamo definuje ako posunutie. 

### Rotácia

Zložené zobrazenie pozostávajúce z dvoch zrkadlení okolo rôznobežných priamok f a g je rotácia. 

Ak zrkadlenia označíme $\sigma_f, \sigma_g$, potom môžeme formálne písať $T = \sigma_g \circ \sigma_f$.  Ľahko zistíme, že inverzné zobrazenie je $T^{-1} = \sigma_f \circ \sigma_g$. Skutočne, 
$$
TT^{-1} = (\sigma_g \circ \sigma_f) \circ (\sigma_f \circ \sigma_g) = \sigma_g \circ (\sigma_f \circ \sigma_f) \circ \sigma_g = \sigma_g \circ \sigma_g = I \\
T^{-1}T = (\sigma_f \circ \sigma_g) \circ (\sigma_g \circ \sigma_f) = \sigma_f \circ (\sigma_g \circ \sigma_g) \circ \sigma_f = \sigma_f \circ \sigma_f = I
$$
pretože zrkadlenie je involúcia. 

Stred rotácie je priesečník priamok f a g, veľkosť rotácie je dvojnásobok uhla medzi priamkami a smer je daný poradím zrkadlení. 

![rotacia](img\rotacia.png)- Rotácia má jediný pevný bod, a to stred otáčania. 

- Pretože je kompozíciou dvoch izometrií, je rotácia tiež izometria.

- Dve priamky prechádzajúce priesečníkom  f a g  a s rovnakým uhlom ako medzi f a g realizujú rovnakú rotáciu. 

- Ak uhol rotácie je $\alpha$, potom rotácia okolo rovnakého stredu o uhol $\alpha + 2k\pi,\, k= 0, \pm 1, \pm 2, \dots $ je rovnaké zobrazenie. 

Na rekonštrukciu rotácie potrebujeme dva body a ich obrazy, pretože musíme zrekonštruovať stred otáčania a jeho uhol. 

### Stredová súmernosť

Stredová súmernosť je kompozícia dvoch zrkadlení s navzájom kolmými osami. Ide teda o rotáciu o $2 \times 90° = 180°$.

- Stredová súmernosť je involúcia, teda je rovná svojmu inverznému zobrazeniu. 
- Pretože je kompozíciou dvoch izometrií, je stredová súmernosť tiež izometria.

- Stredová súmernosť má pevný bod - stred súmernosti. 

![image-20230915143418117](img\image-20230915143418117.png)

### Posunuté zrkadlenie

Posunuté zrkadlenie je kompozícia zrkadlenia a posunutia rovnobežného s osou zrkadlenia, resp. zrkadlenia okolo priamky f a dvoch na ňu kolmých priamok g a h. Ešte v inom vyjadrení je to kompozícia stredovej symetrie a zrkadlenia. 

![image-20230915144750777](img\Posunute_zrkadlenie.png)

- Posunuté zrkadlenie nemá žiadny pevný bod. 
- Pretože je kompozíciou izometrií, je posunuté zrkadlenie tiež izometria.
- Os zrkadlenia je invariantná voči posunutému zrkadleniu (zobrazuje sa sama na seba).

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





1. Trojuholník má strany 4 m, 11 m a 8 m. Vypočítajte jeho vnútorné uhly. 
2. Majme tri rovnobežné priamky f, g, h. Dokážte,že existuje priamka j taká, že pre zrkadlenia okolo priamok f, g, h , j platí $\sigma_h \circ \sigma_g \circ \sigma_f = \sigma_j$ - teda že tri zrkadlenia môžeme nahradiť jediným. Kde leží priamka j?
3. Majme tri priamky f, g, h, pretínajúce sa v jedinom bode. Dokážte,že existuje priamka j taká, že pre zrkadlenia okolo priamok f, g, h , j platí $\sigma_h \circ \sigma_g \circ \sigma_f = \sigma_j$ - teda že tri zrkadlenia môžeme nahradiť jediným. Kde leží priamka j?
4. Strana trojuholníka má dĺžku 1. Nájdite obsah zelenej plochy. 

![equilateral_triangle3](img\equilateral_triangle3.gif)

5. Polomer kružníc je 1. Vypočítajte obsah červenej plochy.

![equilateral_triangle6](img\three_circles.png)



## 5. Program na budúci týždeň

- izometrie v rovine: zložitejšie tvrdenia a príklady

  
