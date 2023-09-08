## Hodina 8. septembra 2023

Program:

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli.
3. Geometria: Ptolemaiova veta, ale začíname so zobrazeniami.
4. Domáca úloha (nová)
5. Program na budúci týždeň

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Videohovor** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

### 1. Domáca úloha

 **Príklad 1**

Majme rovnostranný trojuholník $A_1A_2A_3$ Nech P je ľubovoľný bod na kružnici, opísanej tomuto trojuholníku. Dokážte, že spomedzi spojníc $PA_1, PA_2, PA_3$ je súčet dvoch kratších rovný najdlhšej. 

<img src="img\from_ptolemy.gif" alt="from_ptolemy" style="zoom:150%;" />

**Riešenie**

Označme $a, b, c, d$ po rade dĺžku strany rovnostranného trojuholníka a dĺžky úsečiek $A_1P, A_2P, A_3P$.  Potom z Ptolemaiovej vety máme $ac + ad = ab$, z očho vyplýva dokazované tvrdenie $b = a+c$.

---

**Príklad 2**

V kruhu máme dve tetivy AB a CD, a na nich body P, Q. Dĺžky a vzdialenosti sú vyznačené na obrázku a úloha je vypočítať dĺžku tetivy, ktorá vznikne predĺžením úsečky PQ k hraniciam kružnice. 

<img src="img\ExercisePQ.png" alt="image-20230830232443871" style="zoom:120%;" />

**Riešenie**

Označme dĺžku úsečky medzi bodom P a priesečníkom polpriamky QP a kružnice ako x, a dĺžku úsečky medzi bodom Q a priesečníkom polpriamky PQ s kružnicou ako y. Potom z vety o skrížených tetivách máme
$$
(27+x)y = 7\cdot 12 \\
(27+y)x = 5 \cdot 6
$$
To je sústava dvoch rovníc a začneme tým, že ich od seba odčítame:
$$
(1) & 27y + xy &=& 84 &\\
(2) & 27x + xy &=& 30 &\\
(1)-(2) & 27(y - x) &=& 54 &\implies y = x + 2
$$
Dosadíme a vyriešime kvadratickú rovnicu:
$$
(27 + x + 2)x = 30 \\
x^2 + 29x - 30 = 0 \\
(x-1)(x+30) = 0 \\
x_1 = 1,\quad x_2 = -30 \\
y_1 = 3, \quad y_2 = -28
$$
Záporné riešenia zahadzujeme a ako jediné riešenie máme $x=1, y=3$.

---

## 2. Príklady na zahriatie

**Racionálne aproximácie odmocnín (z minula**)

Definujme dve postupnosti celých čísel $a_n, b_n$ takto:
$$
a_n = a_{n-1} + 2b_{n-1} \\
b_n = a_{n-1} + b_{n-1}
$$


![RationalApproximation](img\Two_Approximation.png)

Potom platí
$$
\lim\limits_{n \rightarrow \infty} \frac{a_n}{b_n} = \sqrt{2}
$$
pre prakticky ľubovoľné počiatočné $a_0, b_0$. 

K tomuto vzťahu sme došli "obrátením" geometrického dôkazu iracionality $\sqrt{2}$.

Takéto tvrdenie ide zovšeobecniť, najprv pre odmocninu z ľubovoľného iného čísla:

1. Majme dve postupnosti $a_n, b_n$ definované takto:

$$
a_n = a_{n-1} + pb_{n-1} \\
b_n = a_{n-1} + b_{n-1}
$$

Potom platí
$$
\lim\limits_{n \rightarrow \infty} \frac{a_n}{b_n} = \sqrt{p}
$$

2. Druhé zovšeobecnenie: ako spočítať racionálne aproximácie tretej odmocniny? 
   Majme dve postupnosti $a_n, b_n$ definované takto:

$$
a_n = a_{n-1}^2 + a_{n-1} + pb_{n-1} \\
b_n = a_{n-1}^2 + a_{n-1} + b_{n-1}
$$

Potom platí
$$
\lim\limits_{n \rightarrow \infty} \frac{a_n}{b_n} = \sqrt[3]{p}
$$

- Ako toto dokázať?
- Ako by to bolo so štvrtou, piatou, ... odmocninou?

**Stredové a obvodové uhly**

Toto sme posledne zistili, že treba prejsť, tak poďme: Tvrdenie, ktoré chceme dokázať, má niekoľko častí:

1. Obvodové uhly zodpovedjúce rovnakej tetive sú rovnaké
2. Obvodové úhly majú veľkosť polovice príslušného stredového uhla.

<img src="C:\Users\kvasn\Documents\GitHub\Erik\img\Thales_1.png" alt="image-20230905215957180" style="zoom:60%;" />

Začneme jednoduchým prípadom, keď rameno vymedzujúce obvodový uhol prechádza stredom kružnice. V našom prípade máme obvodový uhol $\alpha \equiv \angle BAC$ a zodpovedajúci stredový uhol $\beta \equiv \angle BSC$. Trojuholník BSC je rovnoramenný, takže $\angle SBC = \angle SCB = 1/2(\pi - \beta)$.  Platí, že $\angle ASC = \pi - 2\alpha$, ale na druhej strane $\angle ASC + \beta = \pi$, takže dostávame 

1. $\beta = 2\alpha$
2. $\angle ACB = \alpha + \pi/2 - \beta/2 = \pi/2$.

Druhé tvrdenie je Thalésova veta: obvodové uhly nad priemerom sú pravé. Prvé tvrdenie sme dokázali iba v špeciálnom prípade, takže ho potrebujeme zovšeobecniť.

<img src="C:\Users\kvasn\Documents\GitHub\Erik\img\Thalse_2.png" alt="image-20230905223917843" style="zoom:60%;" />

Zjavne aj v tomto prípade tvrdenie platí, z obrázku ľahko vidíme, že $\beta + \gamma = 2\alpha + 2\delta$. Ešte musíme tvrdenie dokázať v prípade, že vrchol stredového uhla neleží vnútri obvodového uhla. 

Tretia situácia, ktorú si preberieme, je vrchol obvodového uhla na opačnej strane tetivy než vrchol stredového uhla. Dokážeme, že v tomto prípade tiež platí $\beta = 2\alpha$. 

<img src="C:\Users\kvasn\Documents\GitHub\Erik\img\Thales_3.png" alt="image-20230905231334059" style="zoom:60%;" />

Najprv zaznamenáme, že $|AS|=|BS|=|CS|=r$.  Trojuholníky ASB , BSC, ASC sú teda všetky rovnoramenné. Označme $\alpha_1 = \angle ABS,\,\beta_1 \equiv \angle ASB = \pi - 2\alpha_1$ a analogicky $\alpha_2 = \angle SBC,\,\beta_2 \equiv \angle BSC = \pi - 2\alpha_2$. Odtiaľ $\beta_1 + \beta_2 = 2\pi - 2\alpha_1 - 2\alpha_2$ a teda $\beta \equiv 2\pi - \beta_1 - \beta_2 = 2(\alpha_1 + \alpha_2) = 2\alpha$, čím sme dokázali platnosť tvrdenia pre opačnú stranu tetivy. 

Ostáva nám posledný prípad, kedy vrchol obvodového uhla leží na rovnakej strane tetivy ako stred kružnice, ale stred kružnice sa nachádza mimo obvodového uhla.  Používame rovnaký obrázok, iba sme veci premenovali. 

<img src="C:\Users\kvasn\Documents\GitHub\Erik\img\Thales_4.png" alt="image-20230905235129185" style="zoom:60%;" />

Označme $\beta_1 \equiv \angle ASB$ a z predchádzajúceho prípadu vieme, že $\beta + \beta_1 = 2\pi - 2\angle ABC$. Označme ďalej $\gamma \equiv \angle ACS = \angle CAS = 1/2(\pi - \beta - \beta_1) = \angle ABC - \pi/2$. Označme ďalej $\delta_1 \equiv \angle ABS = \alpha + \gamma$,  $\delta_2 \equiv \angle SBC = \pi/2 - \beta/2$. Platí $\angle ABC = \delta_1 + \delta_2 = \alpha + \gamma + \pi/2 - \beta/2$. Pre uhol ABC tak máme dve vyjadrenia, $\angle ABC = \gamma + \pi/2 = \alpha + \gamma + \pi/2 - \beta/2$. Obe tieto vyjadrenia môžu zároveň platiť iba ak $\alpha = \beta / 2$, čím sme dokázali posledný prípad a tvrdenie teda platí pre celú kružnicu. 

**Sínusová veta**

Sínusová veta je ľahko dokázateľný vzťah pre trojuholníky. Majme trojuholník ABC s vnútornými uhlami $\alpha, \beta, \gamma$ po rade pri vrcholoch $A, B, C$, a stranami $a, b, c$ protiľahlým vrcholom $A, B, C$. Nech $r$ je polomer kružnice, opísanej trojuholníku ABC. Potom platí
$$
\frac{a}{\sin{\alpha}} = \frac{b}{\sin{\beta}} = \frac{c}{\sin{\gamma}} = 2r
$$
*_Dôkaz_*: 

![Untitled](img\Sinusova_veta.png)

Na obrázku hore máme trojuholník ABC  Stredové a obvodové uhly (Euklides): uhol BSC je dvojnásobkom uhla BAC $=\alpha$. Nech P leží uprostred strany $BC=a$.  Trojuholník BPS je pravouhlý a zdefinície 
$$
\sin{\alpha} = \frac{a/2}{r} \implies \frac{a}{\sin{\alpha}} = 2r
$$
Dôkaz je mierne odlišný, keď je uhol $\alpha$ tupý , ako ukazuje nasledujúci obrázok. Použijeme doplnkové uhly k $\alpha$ a z príslušných pravouhlých trojuholníkov dostaneme sínusovú vetu pre ne. Pretože platí $\sin{(90°-\alpha)} = \sin{\alpha}$, máme dokazované tvrdenie. 

<img src="img\Sinusova_veta2.png" alt="Untitled" style="zoom:36%;" />

Dokázali sme "tretinu" sínusovej vety a ďalšie dve tretiny dokážeme analogicky. 

*_Alternatívny dôkaz_*

Pre jednoduchý dôkaz sínusovej vety "bez pravej strany " vystačíme s jednoduchou konštrukciou:

![Untitled](img\Sinusova_veta3.png)

Stačí porovnať dva vzťahy pre výšku $v_b$:
$$
v_b = c\sin{\alpha} = a\sin{\gamma} \implies \frac{c}{\sin{\gamma}} = \frac{a}{\sin{\alpha}}
$$
atd. Tento dôkaz dobre funguje pre ostré i tupé uhly. 



---

## 3. Geometria

#### Veta o skrížených tetivách

Nechal som z minula.

Začneme s pomocným tvrdením, ktoré nám umožní vhľad do zvláštnych vlastností štvoruholníkov, vpísaných do kružnice. 

<img src="img\Xchords_01.png" alt="Xchords_1" style="zoom:20%;" />

Majme kružnicu a dve tetivy AB, CD, pretínajúce sa v bode O. Potom platí
$$
AO \cdot OB = CO \cdot OD
$$
**Dôkaz**

<img src="img\Xchords_2.png" alt="Xchords_2" style="zoom:33%;" />

Dokážeme, že trojuholníky AOC a DOB sú podobné. 

- Uhly $\alpha$ sú obvodové uhly, prislúchajúce oblúku BC, a sú preto rovnaké.
- Uhly $\beta$ sú obvodové uhly, prislúchajúce oblúku AD, a sú preto rovnaké.
- Uhly $\gamma$ sú vrcholové uhly okolo priesečníka AB a CD, a sú preto rovnaké. 

Z podobnosti trojuholníkov vyplýva
$$
\frac{AO}{OC} = \frac{DO}{OB} \implies AO \cdot OB = DO \cdot OC
$$


#### Ptolemaiova veta a súčtové vzorce pre sínus a kosínus

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

Naučme sa používať Ptolemaiovu vetu na nasledujúcom príklade:

Vezmime štvoruholník ABCD vpísaný do kružnice o polomere $r = 1/2$ tak, že stred kružnice leží na uhlopriečke AC. Použijeme Tálesovu či Euklidovu vetu o stredových a obvodových uhloch a sínusovú vetu, aby sme vypočítali všetky strany a uhlopriečky, potrebné do Ptolemaiovej vety:

<img src="C:\Users\kvasn\Documents\GitHub\Erik\img\Ptolemy_Sum - Copy.png" alt="Ptolemy_Sum - Copy" style="zoom:30%;" />
$$
|AC| = 1 \\
|\angle ABC| = |\angle ADC| = 90° \\
|BC| = \sin{\alpha} \\
|DC| = \sin{\beta} \\
|AB| = \sin{(90° - \alpha)} = \cos{\alpha} \\
|AD| = \sin{(90° - \beta)} = \cos{\beta} \\
|BD| = \sin{(\alpha+\beta)}
$$
Ešte sme tu použili jednu vec, ktorú sme preberali dávnejšie:

<img src="img\sin_cos.png" alt="sin_cos" style="zoom: 25%;" />
$$
\cos{\alpha} = sin{(90° - \alpha)}, \quad \sin{\alpha} = cos{(90° - \alpha)}
$$
Z Ptolemaiovej vety dostaneme
$$
|AC||BD| = |AB||CD| + |BC||AD| \\
1\cdot \sin{(\alpha+\beta)} = \cos{\alpha} \cdot \sin{\beta} + \sin{\alpha} \cdot \cos{\beta}
$$
teda 
$$
\sin{(\alpha +\beta)} = \sin{\alpha} \cdot \cos{\beta} + \cos{\alpha} \cdot \sin{\beta}
$$
čo je univerzálne platný súčtový vzorec pre sínus. 

Rovnako môžeme dokázať rozdielový vzorec, stačí trocha pohýbať s obrázkom:

![Untitled](img\Ptolemy_diff.png)

Postupujeme rovnako ako v predchádzajúcom prípade - vypočítame všetky dĺžky a dosadíme do Ptolemaiovej vety:
$$
|AD| = 1 \\
|\angle ACD| = |\angle ABD| = 90° \\
|BD| = \sin{\alpha} \\
|CD| = \sin{\beta} \\
|AB| = \sin{(90° - \alpha)} = \cos{\alpha} \\
|AC| = \sin{(90° - \beta)} = \cos{\beta} \\
|BC| = \sin{(\alpha - \beta)}
$$
a dosadíme do Ptolemaiovej vety:
$$
|AC||BD| = |AB||CD| + |BC||AD| \\
\cos{\beta} \cdot \sin{\alpha} = \cos{\alpha} \cdot \sin{\beta} + \sin{(\alpha - \beta)} \cdot 1
$$
teda 
$$
\sin{(\alpha - \beta)} = \sin{\alpha} \cdot \cos{\beta}  - \cos{\alpha} \cdot \sin{\beta}
$$
ďalší základný vzťah pre goniometrické funkcie.  Z týchto vzťahov ľahko dostaneme príslušné vzťahy pre kosinus:
$$
\cos{(\alpha + \beta)} = \sin{(90° - \alpha - \beta)} = \sin{((90° - \alpha) - \beta)} \\ 
= \sin{(90° - \alpha)} \cdot \cos{\beta}  - \cos{(90° - \alpha)} \cdot \sin{\beta} \\
= \cos{\alpha} \cdot \cos{\beta}  - \sin{\alpha} \cdot \sin{\beta}
$$
a podobne môžeme dokázať aj rozdielový vzorec pre kosínus. 

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

---



## 4. Domáca úloha (nová)

1. Koľko číslic (čitateľ + menovateľ) potrebujeme v racionálnej aproximácii $\sqrt[3]{5}$, aby sme dosiahli presnosť $10^{-k}$?
2. Ako poslať biliardovú guľu do ľavého zadného vrecka odrazom od pravého mantinelu?

![image-20230908132209666](C:\Users\kvasn\Documents\GitHub\Erik\img\snooker.png)

3. Máme priamku $g$ a dve kružnice $k_1, k_2$. Zostrojte štvorec ABCD tak, že body A, C ležia na priamke $g$, a body B, D po jednom na kružniciach $k_1, k_2$. Koľko riešení má táto úloha v závislosti od vzájomnej polohy priamky a oboch kružníc?

<img src="C:\Users\kvasn\Documents\GitHub\Erik\img\two_circles.png" alt="two_circles" style="zoom:20%;" />



## 5. Program na budúci týždeň

- izometrie v rovine: posunutie, rotácia, bodová symetria, posunuté zrkadlenie
- začneme nejakú novú paralelnú tému, aby sme sa nenudili so samou geometriou. Nápady?
