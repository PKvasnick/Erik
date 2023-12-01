## Hodina 24. novembra 2023

Program:

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli: Ešte bude trocha projektívnej geometrie.
3. Afínna geometria a komplexné čísla.
4. Domáca úloha (nová)
5. Program na budúci týždeň

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Videohovor** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

### 1. Domáca úloha

**Príklad 1**

Máme kvadratickú formu  $y^2 - 8y - x + 19 = 0$, ktorá popisuje parabolu v rovine. Nájdte vrchol paraboly, ohnisko, smerovú priamku (pre ohnisko a riadiacu priamku platí, že body na parabole majú rovnakú vzdialenosť od ohniska a riadiacej priamky), a os paraboly. 

**Riešenie**

Upravíme výraz na normálny tvar $(y-v_x)^2 - a(x-v_x) = 0$:
$$
(y - 4)^2 - (x - 3) = 0
$$
Teda vrchol paraboly leží v bode $V = (3, 4)$, tvarový parameter $a=1$ a os paraboly je priamka  $y = 4$.

![](C:\Users\kvasn\Documents\GitHub\Erik\img\Hw_Parabola.png)

Ohnisko a riadiaca priamka (directrix) sú viazané definíciou paraboly: Parabolu tvoria body, ktoré sú rovnako vzdialené od riadiacej priamky a od ohniska. 

Ako zistíme ohnisko? Zvolíme si vrchol paraboly a bod $X = (3+1, 4-1)$. Rovnica riadiacej priamky bude $x = 3-f$ a ohnisko bude mať súradnice $F = (3+f, 4)$.  Pretože je os paraboly rovnobežná s osou x, počítajú sa všetky vzdialenosti ľahko. Pre vrchol paraboly automaticky platí, že je rovnako vzdialený od ohniska ako od riadiacej priamky (cez definíciu). Takže potrebujeme iba vypočítať $f$ z rovnosti vzdialeností pre dodatočný bod X:
$$
d^2(X, F) = (1-f)^2 + 1 \quad d^2(X, d) = (1+f)^2 \\
1 - 2f + f^2 + 1 = 1 + 2f + f^2 \implies 4f = 1,\quad f = \frac{1}{4}
$$
Teda riadiaca priamka je $d: x = 11/4$ a ohnisko $F = (13/4, 4)$.

Polomer krivosti a stred oskulačnej kružnice vo vrchole paraboly nájdeme tak, že zvolíme dva body symetricky okolo vrcholu, a cez ne a vrchol paraboly zostrojíme kružnicu. Keď body približujeme k vrcholu, blíži sa polomer a stred kružnice hľadaným hodnotám. 

---

**Príklad 2**

Vyriešte.

<img src="img\image-20231117155739169.png" alt="image-20231117155739169" style="zoom:30%;" />

**Riešenie**

Začneme Ptolemaiom (dva protiľahlé pravé uhly znamenajú, že DB je priemer opísanej kružnice ergo že taká existuje):
$$
AB\cdot CD + BC \cdot AD = AC \cdot BD \\
AB \cdot 5 = AC \cdot BD
$$
BD je spoločná prepona, teda 
$$
BD^2 = AB^2 + AD^2 = BC^2 + CD^2 = 13 \\
AB = AD = \sqrt{\frac{13}{2}} \\
BD = \sqrt{13} \\
R = \frac{\sqrt{13}}{2}
$$
kde R je polomer opísanej kružnice. Z prvej rovnice nakoniec máme
$$
AC = \frac{5\cdot AB}{BD} = \frac{5\sqrt{2}}{2}
$$
Poznáme strany a polomer opísanej kružnice, takže použijeme vzťah:
$$
S = \frac{abc}{4R} = \frac{\sqrt{\frac{13}{2}}\cdot \frac{5\sqrt{2}}{2} \cdot 3}{2\sqrt{13}} = \frac{15}{4}
$$
Nakreslíme:

<img src="img\stvoruholnik.png" alt="image-20231118124653861" style="zoom:200%;" />

Niekde by tu mal byť dôkaz vzťahu pre výpočet plochy trojuholníka zo strán a polomeru opísanej kružnice. 

Tu je:

Majme kružnicu o polomere 2r, opísanú trojuholníku ABC. 

![image-20231118213302193](C:\Users\kvasn\Documents\GitHub\Erik\img\triangle_area_from_circumcircle.png)

Plocha trojuholníka $ABC$ je 
$$
S = \frac{1}{2}bv_b = \frac{1}{2}bc\sin{\alpha}
$$
Pre $\sin{\alpha}$ máme vyjadrenie zo sínusovej vety:
$$
\frac{ \sin{\alpha}}{a} = \frac{1}{2r}
$$
a z toho dostávame výraz pre plochu trojuholníka v termínoch strán a polomeru opísanej kružnice:
$$
S = \frac{1}{2}bc\frac{a}{2r} = \frac{abc}{4r}
$$


---

## 2. Príklady na zahriatie

#### Súčin uhlopriečok pravidelného n-uholníka



Máme tu zobrazenie bodov $B_1, B_2, B_3$ na body $A_1, A_2, A_3$ pomocou dvoch perspektívnych projekcií: Prvá projekcia s ohniskom $A_3$ "stiahne" body $B_1, B_2, B_3$ na červenú priamku (zelené šípky). Druhá projekcia s ohniskom $B_3$ pošle body z červenej čiary do bodov $A_1, A_2, A_3$. Máme tu tri takéto dvojice, ale skúmame iba túto jednu. Nemáme žiadnu záruku, že bod $C_3$ leží na červenej čiare - to práve potrebujeme dokázať. 

Pre náš dôkaz bude podstatné, čo sa udeje s bodmi P a Q, Prvá projekcia stiahne bod P do bodu Q, a druhá ho ponechá na mieste, pretože už leží na priamke $A_1 A_2$. O bode Q pozitívne vieme, že leží na červenej čiare. 

Pozrime sa teraz na inverzné zobrazenie: 

![](img\Pappus_proof_2.png)

Na tomto obrázku máme dvojicu projekcií, ktoré zobrazjú body $A_1, A_2, A_3$ na $B_1, B_2, B_3$. Červená čiara na tomto obrázku nemusí byť nutne totožná s červenou čiarou na predošlom obrázku, konkrétne nevieme povedať, či na nej leží bod $C_1$. 

Čo ale vieme je, že toto zobrazenie je inverzné k projekciám na predošlom obrázku.  Pretože kombinácia projekcií na dvoch obrázkoch zobrazuje body $B_1, B_2, B_3$ na seba, musí toto platiť pre všetky body na priamke $B_1B_2$, a teda aj pre priessečník P. To ale znamená, že bod Q musí ležať na oboch červených priamkach, a pretože na oboch červených priamkach musí ležať aj bod $C_2$, musia byť priamky totožné. 



---



## 3. Vektory a komplexné čísla

### Van Aubelova veta

Spojnice štvorcov sú na seba kolmé a majú rovnakú dĺžku.

![](img\Stelling van Van Aubel.png)

To som minule pokašľal, ale snáď teraz to už je jasné. 

**Rovnica priamky**

Parametrickú rovnicu sme už mali: 

Body, ležiace na priamke, prechádzajúcej bodmi $A, B$ sú $X = A + t(B-A)$.

- Toto nejde ľahko zovšeobecniť na zložitejšie krivky (teda ide, ale užitočné to je iba občas. 

Afinny priestor: máme body, vektory, a vzdialenosti medzi nimi.

- Vzdialenosť bodov: $|B-A|=\sqrt{(b_x - a_x)^2+(b_y-b_x)^2}$

- Vzdialenosť vektorov meria odchýlku ich smerov:  $\vec{a}\cdot\vec{b} = |\vec{a}||\vec{b}|\cos{\angle(\vec{a},\vec{b})} = a_x\cdot b_x + a_y \cdot b_y$.

Body nemôžeme sčítať, ale vektory áno. Body ale môžeme odčítať, pričom dostávame vektor. 

*Normálová rovnica priamky*

Priamku, kolmú na vektor $\vec{n}$ a prechádzajúcu bodom $A$, tvoria body, pre ktoré platí $(X-A)\cdot \vec{n} = 0$, čo vedie k rovnici tvaru $ax + by + c = 0$.

### Komplexné čísla

![](img\complex_0.png)

Komplexné čísla sú čisla tvaru $z = x + iy$, kde x, y sú reálne súradnice v rovine a $i^2 = -1$.

### Transformácie

**Vektor je posunutie**, takže posunutia sú ľahké. 

**Rotácie** sú ťažšie, ale sú ľahké v komplexných číslach. 

**Zamyslenie na domácu úlohu: Čo ostatné izometrie roviny?**

Zrkadlenie? Stredová symetria? Posunuté zrkadlenie?

(Porozmýšlať: aké ingrediencie na toto potrebujeme a v akom vyjadrení to je najprirodzenejšie.)

---



## 4. Domáca úloha (nová)

1. Máme kvadratickú formu  $y^2 - 8y - x + 19 = 0$, ktorá popisuje parabolu v rovine. Nájdte vrchol paraboly, ohnisko, smerovú priamku (pre ohnisko a riadiacu priamku platí, že body na parabole majú rovnakú vzdialenosť od ohniska a riadiacej priamky), a os paraboly. 



2. Vyriešte.

<img src="img\image-20231117155739169.png" alt="image-20231117155739169" style="zoom:30%;" />



---



## 5. Program na budúci týždeň

Grupy symetrií a dlaždice možno dáme nabudúce.

Ale robíme analytickú geometriu a komplexné čísla. 

