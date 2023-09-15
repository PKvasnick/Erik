## Hodina 8. septembra 2023

Program:

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli.
3. Geometria: Izometrie roviny, posunutia a rotácie
4. Domáca úloha (nová)
5. Program na budúci týždeň

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Videohovor** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

### 1. Domáca úloha

**Príklad 1**

Koľko číslic (čitateľ + menovateľ) potrebujeme v racionálnej aproximácii $\sqrt[3]{5}$, aby sme dosiahli presnosť $10^{-k}$?

**Riešenie**

Ospravedlňujem sa za pôvodne chybné uvedenie metódy, správne rekurzia funguje takto:

Definujme $x_n = a_n/b_n$, kde $a_n, b_n,\, n=1, 2,\dots$ sú celé čísla. Ďalej definujme
$$
x_n = \frac{x_{n-1}^2 + x_{n-1} + p}{x_{n-1}^2 + x_{n-1} + 1}
$$

Potom platí
$$
\lim\limits_{n \rightarrow \infty} x_n = \sqrt[3]{p}
$$

Dôkaz konvergencie: vypočítame pevný bod iterácie:
$$
x = \frac{x^2 + x + p}{x^2 + x + 1} \\
x^3 + x^2 + x = x^2 + x + p \\
x^3 = p
$$
Ak chceme racionálne aproximácie, jednoducho vyjadrujeme $x_n$ v tvare zlomku. Tu je niekoľko prvých iterácií, štartujúcich z $a_0 = 2,\,b_0=1$:

| n    | $x_n$ | počet číslic | $x_n - \sqrt[3]{5}$ |
| ---- | ----- | ------------ | ------------------- |
| 0    |   2.000000    |      1        |            0.290024          |
| 1    |   1.571429    |      3        |            -0.138547         |
| 2    |   1.793522    |      6        |            0.083546          |
|3 |1.665530| 12| -0.044446|
|4 |1.735359| 25| 0.025383|
|5 |1.696036| 50| -0.013940|
|6 |1.717801| 100| 0.007825|
|7 |1.705636| 202| -0.004340|
|8 |1.712399| 404| 0.002423|
|9 |1.708628| 808| -0.001348|

Vidíme, že zatiaľ čo presnosť aproximácie sa zlepšuje len veľmi pozvoľna, počet číslic v čitateli + menovateli zlomku rastie exponenciálne - zdvojnásobuje sa s každou iteráciou. Takáto iteračná schéma je úplne neužitočná, či už ako spôsob výpočtu tretej odmocniny alebo ako spôsob produkcie racionálnych aproximácií. 

Vzhľadom na rýchlo rastúcu dĺžku čitateľov a menovateľov racionálnych aproximácií nejde takúto tabuľku spočítať v Exceli. Ide to ale ľahko v Pythone, ktorý vie počítať s celými číslami s neobmedzenou veľkosťou. Tu je ukážka kódu:

```python
# Rational approximation of cube root
# The theorem is:
# Define
#       a_{n-1}^2 + a_{n-1} + b
# a_n = -----------------------
#       a_{n-1}^2 + a_{n-1} + 1
# then a_n converges to cube root of b.

from fractions import Fraction
from math import pow, log10, ceil


def iteration(x:Fraction, b:int) -> Fraction:
    return (x**2 + x + b)/(x**2 + x + 1)


def get_num_digits(x: Fraction) -> int:
    return ceil(log10(x.numerator)) + ceil(log10(x.denominator))


def main() -> None:
    b = 5
    sqrt_b = pow(b, 1/3)
    x = Fraction(2,1)
    print(f"0 {float(x):.6f} {get_num_digits(x)} {x-sqrt_b:.6f}")
    for i in range(1,10):
        x = iteration(x, b)
        print(f"{i} {float(x):.6f} {get_num_digits(x)} {x - sqrt_b:.6f}")


if __name__ == "__main__":
    main()

```

Kód používa typ `Fraction`, čo je racionálne číslo reprezentované ako dvojica celých čísel s neobmedzenou dĺžkou, a podporuje bežné aritmetické operácie so zlomkami. 


---

**Príklad 2**

Ako poslať biliardovú guľu do ľavého zadného vrecka odrazom od pravého mantinelu?

![image-20230908132209666](img\snooker.png)

**Riešenie**

Pretože uhol odrazu je rovný uhlu dopadu (na obrázku sú uhly označené iba v zrkadlovom obraze), je situácia symetrická okolo pravej hrany stola AD. V  zrkadlovom svete smeruje dráha gule z bodu P cez bod odrazu X priamo do bodu A´. Podobne dráha zrkadlovej gule z bodu P´ smeruje cez bod X priamo do bodu A´.

![image-20230915004107541](img\snooker2.png)

Pre praktickú konštrukciu potrebujeme zostrojiť bod X ako priesečník priamky PA´ s hranou CD. 

---

**Príklad 3**

Máme priamku $g$ a dve kružnice $k_1, k_2$. Zostrojte štvorec ABCD tak, že body A, C ležia na priamke $g$, a body B, D po jednom na kružniciach $k_1, k_2$. Koľko riešení má táto úloha v závislosti od vzájomnej polohy priamky a oboch kružníc?

<img src="C:\Users\kvasn\Documents\GitHub\Erik\img\two_circles.png" alt="two_circles" style="zoom:20%;" />

**Riešenie**

Základný riešenia spočíva v zrkadlovej symetrii výsledného štvorca podľa priamky g. Ak zrkadlenie okolo priamky g označíme ako $\sigma_g$, potom platí $D \in k_1, B \in k_2, D = \sigma_g(B) \in \sigma_g(k_2)$. Inak povedané, bod D leží na kružnici $k_1$ i na kružnici $k_2^{\prime}$. Vieme teda ľahko zostrojiť uhlopriečku štvorca kolmú na priamku g, a zvyšok štvorca skonštruujeme už ľahko.



![image-20230915011747528](img\two_circles2.png)

V konštrukcii na obrázku sme pre konštrukciu štvorca použili kružnicu so stredom v bode T, čo je priesečník BD a priamky g , a priemerom BD. Priesečníky tejto kružnice s priamkou g sú body A, C.

Pretože riešenie hľadáme ako priesečník dvoch kružníc, budeme mať spravidla dve, jedno alebo žiadne riešenie podľa vzájomnej polohy východzích kružníc a priamky g.

---



## 2. Príklady na zahriatie

**Sínusová veta**

Sínusová veta je ľahko dokázateľný vzťah pre trojuholníky. Majme trojuholník ABC s vnútornými uhlami $\alpha, \beta, \gamma$ po rade pri vrcholoch $A, B, C$, a stranami $a, b, c$ protiľahlým vrcholom $A, B, C$. Nech $r$ je polomer kružnice, opísanej trojuholníku ABC. Potom platí
$$
\frac{a}{\sin{\alpha}} = \frac{b}{\sin{\beta}} = \frac{c}{\sin{\gamma}} = 2r
$$






---

## 3. Geometria

**Sínusová veta**

Sínusová veta je ľahko dokázateľný vzťah pre trojuholníky. Majme trojuholník ABC s vnútornými uhlami $\alpha, \beta, \gamma$ po rade pri vrcholoch $A, B, C$, a stranami $a, b, c$ protiľahlým vrcholom $A, B, C$. Nech $r$ je polomer kružnice, opísanej trojuholníku ABC. Potom platí
$$
\frac{a}{\sin{\alpha}} = \frac{b}{\sin{\beta}} = \frac{c}{\sin{\gamma}} = 2r
$$



#### Ptolemaiova veta

.Ptolemaiova veta je silnejšie tvrdenie ako Pytagorova veta: Pre štvoruholník ABCD vpísaný v kružnici platí


​		![Ptolemy_equality.svg](img\Ptolemy_equality.svg.png)
$$
|AB||CD| + |AD||BC| = |AD||BC|
$$
V skutočnosti platí ešte silnejšie tvrdenie, nazývané niekedy Ptolemaiova nerovnosť: Pre ľubovoľný konvexný štvoruholník ABCD platí
$$
|AB||CD| + |AD||BC| \ge |AD||BC|
$$
pričom rovnosť nastáva iba ak je štvoruholník ABCD vpísaný v kružnici alebo keď body A, B, C, D ležia na jednej priamke. 

#### Dôkaz Ptolemaiovej vety

Základný jednoduchý dôkaz: Máme štvoruholník ABCD vpísaný v kružnici. Na uhlopriečke BD nájdeme bod M tak, aby $|\angle ACB|=|\angle MCD|$ (na obrázku označené ako $\alpha$). Uhly $\angle BAC$ a $\angle BDC$ (označené ako $\delta$ sú rovnaké, pretože sú to obvodové uhly zodpovedajúce rovnakej tetive BC.  Pretože trojuholníky ABC a DMC majú rovnaké dva uhly, sú si podobné, a teda platí $CD/MD = AC/AB$, resp. 
$$
AB\cdot CD = AC \cdot MD
$$
Rovnaké sú aj uhly $\angle BCM$ a $\angle ACD$ (oba sú rovné $\alpha + \epsilon$). Ďalej uhly $\angle CAD$ a $\angle CBM$ (označené ako $\eta$ sú rovnaké, pretože sú to obvodové uhly zodpovedajúce rovnakej tetive DC Preto aj trojuholníky BCM a ACD sú si podobné a teda $BC/BM = AC/AD$ čiže 
$$
AD \cdot BC = AC \cdot BM
$$
. Pretože $BM + MD = BD$, dostávame sčítaním oboch vzťahov Ptolemaiovu vetu

![Untitled](img\PtolemyProof.png)
$$
AB \cdot CD + AD \cdot BC = AD \cdot BC
$$

---

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

1. Vyriešte.

<img src="img\Semicircle_problem.png" alt="Semicircle_problem" style="zoom:50%;" />

2. Vypočítajte obsah obdĺžnika.

![image-20230911100951891](img\Rectangle_area.png)

Návod: 

- Hľadáme podobné trojuholníky
- Hľadáme, čo vśetko sa rovná priemeru
- Používame Pytagorovu vetu. 



## 5. Program na budúci týždeň

- izometrie v rovine: zložitejšie tvrdenia a príklady

  
