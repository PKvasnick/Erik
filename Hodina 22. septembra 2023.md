## Hodina 22. septembra 2023

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

1. Vyriešte.

<img src="img\Semicircle_problem.png" alt="Semicircle_problem" style="zoom:50%;" />

**Riešenie**

![Semicircle](img\Semicircle.png)

Vidíme dva trojuholníky, podobné trojuholníku ABC: ASP a SBQ. Ktorýkoľvek z nich umožňuje vyjadriť polomer polkruhu:
$$
\frac{PS}{AP} \equiv \frac{r}{b-r} = \frac{a}{b}
$$
odkiaľ
$$
rb = a(b-r) \\
r(a+b) = ab \\
r = \frac{ab}{a+b} = \frac{6 \cdot 8}{6+8} = \frac{24}{7}
$$

---

**Príklad 2**

2. Vypočítajte obsah obdĺžnika.

![image-20230911100951891](img\Rectangle_area.png)

**Riešenie**

Pomenovali sme v obrázku niektoré body a vzdialenosti, aby sa nám ľahšie riešilo.

![image-20230917010057694](img\Rectangle_area_2.png)

Začneme trojuholníkmi AVP a CUP.  Oba tieto trojuholníky sú podobné trojuholníku ABC. Ak dlhú stranu trojuholníka označíme $b$, dostaneme
$$
\frac{2R}{7} = \frac{10}{b} \implies R = \frac{35}{b} 
$$
Odtiaľ plocha obdĺžnika $Rb = 35$.  

Navyše teraz ľahko vypočítame R, r i b pomocou podobnosti trojuholníkov a vzťahu o úplnom štvorci súčtu a rozdielu:
$$
R^2 + b^2 = 100 \quad Rb = 35 \\
(R + b)^2 = R^2 + r^2 + 2Rb = 170 \\
(R-b)^2 = R^2 + r^2 - 2Rb = 30 \\
b = \frac{\sqrt{170} + \sqrt{30}}{2} \approx 9.26 \\
R = \frac{\sqrt{170} - \sqrt{30}}{2} \approx 3.78\\
r = \frac{3}{7}R \approx 1.62
$$

---



## 2. Príklady na zahriatie

**Príklad 1: Kosínová veta**

Sínusovú vetu sme už mali: Majme trojuholník ABC s vnútornými uhlami $\alpha, \beta, \gamma$ po rade pri vrcholoch $A, B, C$, a stranami $a, b, c$ protiľahlým vrcholom $A, B, C$. Nech $r$ je polomer kružnice, opísanej trojuholníku ABC. Potom platí
$$
\frac{a}{\sin{\alpha}} = \frac{b}{\sin{\beta}} = \frac{c}{\sin{\gamma}} = 2r
$$

Patrí sa doplniť aj kosínovú vetu, ale tu dám iba dva obrázky, z ktorých sú dôkazy jasné.

![cosLaw](C:\Users\kvasn\AppData\Local\Temp\cosLaw.gif)

---

**Príklad 2: Pigeonhole principle**

Majme 100 čísel $1 \le a_1 \le a_2 \le \dots \le a_{100} \le 400$. Dokážte, že sa medzi rozdielmi $d_i = a_i - a_{i-1},\, i = 2,3, \dots 100$ vyskytuje niektorá hodnota viac ako desaťkrát.

*Riešenie*

Budeme pracovať so súčtom 99 rozdielov $d_i = a_i - a_{i-1}$:
$$
D \equiv \sum_{i = 2}^{100} d_i = (a_2 - a_1) + (a_3 - a_2) + \dots + (a_{100}-a_{99}) \\
= a_{100} - a_{1}
$$
Pretože $a_{100} \le 400, a_1 \ge 1$, musí byť $D \le 399$.

Vedieme dôkaz sporom: predpokladajme, že sa žiaden rozdiel nevyskytuje medzi 99 rozdielmi $d_i$ viac ako desaťkrát. Potom, aby sme urobili D čo najmenšie, musíme mať práve 10 nulových rozdielov, 10 rozdielov 1, atď:
$$
D_{min} = 10 \cdot 0 + 10 \cdot 1 + \dots + 10 \cdot 8 + 9 \cdot 9
$$
pričom deviatku sme započítali iba deväťkrát, aby sme mali práve 99 rozdielov. Počítajme:
$$
D_{min} = 10 (0 + 1 + \dots + 9) - 9 = 10\cdot \frac{9\cdot(9+1)}{2} - 9 = 10\cdot 45 - 9 = 441
$$
a to je vytúžený spor: naša minimálna konfigurácia dáva D väčšie ako 399. Teda nemôžeme skonštruovať 99 rozdielov z číslic 0-9 bez toho, aby sa niektorý rozdiel nevyskytoval viac ako desaťkrát.: aby sme dodržali maximálny súčet 399, musíme použiť viac menších rozdielov. 

---

#### Iterácia funkcií

Už sme mali viac rekurentných vzťahov typu $x_n = f(x_{n-1})$. Členy takejto postupnosti môžeme symbolicky vyjadriť ako 
$$
x_1 = f(x_0)\quad x_2 = f(f(x_0)) \quad x_3 = f(f(f(x_0)))\quad \dots
$$
čo nás nabáda skúsiť naštudovať, ako sa správajú takéto iterácie funkcií a za akých okolností k niečomu konvergujú. Toto je užitočné vedieť napríklad keď potrebujeme riešiť transcendentné rovnice typu $x = a\sin{x}$ a podobne, kde možnosť nájsť riešenie opakovaným dosadzovaním x do výrazu na pravej strane je to najjednoduchšie, čo môžeme skúsiť urobiť. 

**Príklad** 

Vezmime si známy vzťah pre numerický výpočet druhej odmocniny:
$$
x_n = \frac{1}{2}\left(x_{n-1} + \frac{a}{x_{n-1}}\right)
$$
Vieme, že postupnosť $\{x_n\}$ konverguje k $\sqrt{a}$, a to rýchlo. Označme 
$$
f(x) = \frac{1}{2}\left(x + \frac{a}{x}\right)
$$
a poďme študovať iterácie tejto funkcie:

![image-20230922112422359](img\iteration_ssqrt.png)

Originálny GeoGebra notebook nájdeš tu: https://www.geogebra.org/m/rRewsAds. Vidno, že iterácie konvergujú pre ľubovoľnú počiatočnú hodnotu $x_0$ a konvergujú vždy veľmi rýchlo.

![image-20230922112915755](img\iteration_sqrt2.png)

Poďme sa pozrieť na niečo, čo konverguje pomaly - na náš generátor racionálnych aproximácií druhej odmocniny. V tomto prípade 
$$
f(x) = \frac{x+a}{x+1}
$$
a pozrime sa, ako vyzerajú iterácie v tomto prípade:

![image-20230922113702121](img\iteration_sqrt3.png)

Vidíme, že toto konverguje pomalšie. 

**(koniec príkladu)**

Kedy ale iterácie konvergujú a kedy nie? Poďme sa pozrieť na prípad, kedy  nefungujú:
$$
x_n = e^{x_{n-1}}
$$
![image-20230922114315369](img\iteration_exp1.png)

Ako vidno, toto veľmi rýchlo diverguje bez ohľadu na počiatočnú hodnotu:

![image-20230922114711709](img\iteration_exp2.png)

Ak sa pozrieme na predchádzajúce obrázky, vidíme rozdiel: teraz sa nám graf funkcie nepretína s krivkou $y = x$. Skúsme funkciu 
$$
f(x) = e^x - 5
$$
Táto funkcia má dva priesečníky s priamkou $y = x$, tak sa pozrime, čo sa bude diať.

![image-20230922115158753](img\iteration_exp3.png)

Vidíme, že z oblasti vľavo od ľavého priesečníka a medzi priesečníkmi konvergujú iterácie rýchlo k ľavému priesečníku.

![image-20230922115607667](img\iteration_exp4.png)

Naopak, iterácie vpravo od pravého priesečníka divergujú. 

![image-20230922115907534](img\iteration_exp5.png)

Takže už trocha tušíme, ako to funguje:

Označme ako stacionárny bod iterácie $x_n=f(x_{n-1})$ bod, pre ktorý platí $x = f(x)$. Iterácie vychádzajúce z okolia stacionárneho bodu konvergujú, keď je smernica funkcie v stacionárnom bode menšia ako 1 (teda ako smernica priamky $y=x$), inak divergujú. Ako okolie stacionárneho bodu označujeme otvorený interval, v ktorom sa nenachádza iný stacionárny bod. 

**Rôzne typy správania**

Klasický príklad funkcionálnej iterácie je funkcia $f(x) = cx(1-x)$. Poďme preskúmať chovanie pre jednotlivé hodnoty c:

![image-20230922134618291](img\iteration_parabola1.png)

![image-20230922134956953](img\iteration_parabola2.png)

![image-20230922135236965](C:\Users\kvasn\Documents\GitHub\Erik\img\iteration_parabola3.png)

![image-20230922135529163](img\iteration_parabola4.png)

![image-20230922135837183](img\iteration_parabola5.png)

![image-20230922140059201](img\iteration_parabola6.png)

S rastom c vidíme prechod od monotónnej konvergencie cez tlmené kmity k oscilujúcemu nekonvergentnému chovaniu a potom cez stále komplikovanejšie oscilácie k chaotickému správaniu. 

Dolný stacionárny bod je nestabilný.

Horný stacionárny bod je stabilný, ale ako je smernica krvky v tomto bode stále zápornejšia, riešenia stále viac oscilujú.

Dôležitú úlohu hrá aj okolie maxima paraboly - slúži ako mixér, pretože posiela do prakticky rovnakého x rôzne trajektórie. Všimnime si, akú prominentnú úlohu hrá v zložitých trajektóriách. 


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

  
