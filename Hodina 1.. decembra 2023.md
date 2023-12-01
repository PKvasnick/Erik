## Hodina 1. decembra 2023

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

![](img\Hw_Parabola.png)

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

![image-20231118213302193](img\triangle_area_from_circumcircle.png)

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

![](img\septagon.png)

**Tvrdenie** Nakreslime pravidelný n-uholník vpísaný do jednotkového kruhu. Pospájajme jeden jeho vrchol so všetkými ostatnými. Potom súčin dĺžok všetkých týchto úsečiek je n.

**Dôkaz**

V komplexnej rovine sú vrcholy pravidelného n-uholníka, vpísaného do jednotkovej kružnice, riešeniami rovnice $z^n - 1 = 0$. Korene rovnice sú 
$$
w_0 = 1 \quad w \equiv w_1 = \exp\left({\frac{2\pi i}{n}}\right) \quad w_k = \exp\left({\frac{2\pi ki}{n}}\right) = w^k,\,k=0, 1, \dots n-1
$$
Súčin diagonál potom bude
$$
|1-w||1-w^2|\dots|1-w^{n-1}|
$$
*_Pomocné tvrdenie 1_*: $|z| = \sqrt{z\bar{z}}$. Dôkaz: 
$$
z\bar{z} = (x+iy)(x-iy) = x^2 - (iy)^2 = x^2 + y^2 = |z|^2
$$
*_Pomocné tvrdenie 2_*: $|z_1||z_2| = |z_1z_2|$. Dôkaz: 
$$
|z_1||z_2| = \sqrt{z_1\bar{z_1}}\sqrt{z_2\bar{z_2}} = \sqrt{z_1\bar{z_1}z_2\bar{z_2}} = \sqrt{z_1z_2\bar{z_1}\bar{z_2}} = |z_1z_2|
$$
Teda súčin diagonál je 
$$
|(1-w)(1-w^2)\dots(1-w^{n-1})|
$$
Teraz napíšeme $z^n-1$ dvoma spôsobmi:

1. Poznáme korene, takže môžeme faktorizovať:

$$
z^n - 1 = (z-1)(z-w)(z-w^2)\dots(z - w^{n-1})
$$

2. Použijeme všeobecný vzťah 

$$
z^n-1 = (z-1)(z^{n-1}+z^{n-2}+\dots + 1)
$$

Teda platí:
$$
(z-w)(z-w^2)\dots(z - w^{n-1}) = z^{n-1}+z^{n-2}+\dots + 1
$$
Požadované tvrdenie odtiaľ dostaneme dosadením $z=1$ :
$$
|(1-w)(1-w^2)\dots(1 - w^{n-1})| = |1^{n-1}+1^{n-2}+\dots + 1| = n
$$

---

### Domáca úloha z textu: Transformácie v rovine

#### Osová súmernosť

Vieme ľahko napísať zrkadlenie okolo súradnicových osí: Obraz bodu $A = [x, y]$ v zrkadlení okolo osi x je $A^{\prime} = [x, -y]$ a v zrkadlení okolo osi y $A^{\prime\prime} = [-x, y]$.  

**Normálová rovnica priamky**

Už sme mali parametrickú rovnicu priamky, prechádzajúcej bodmi A, B: $\mathbf{X} = \mathbf{A} + t(\mathbf{B}-\mathbf{A})$. Iný tvar rovnice priamky získame, ak máme normálový vektor $\vec{n}$ $\equiv$ kolmý na priamku) a bod $\mathbf{A}$, ktorým priamka prechádza. Pre ľubovoľný bod $\mathbf{X}$ na priamke platí $\vec{n}\cdot(\mathbf{X}-\mathbf{A}) = 0$. Odtiaľ 
$$
n_x(x - a_x) + n_y(y - a_y) = 0 \implies n_x x + n_y y - (a_x n_x +a_y n_y) = 0
$$
a teda priamka v rovine má rovnicu $ax + by + c = 0$., kde a, b sú súradnice normálového vektora a 

Majme teda v rovince priamku $f: ax + by + c = 0$ a zostrojme obraz ľubovoľného bodu $\mathbf{X}$ v zrkadlení $\sigma_f$ okolo priamky f.  Budeme postupovať  ako pri geometrickej konštrukcii, teda spustíme kolmicu, nájdeme priesečník $\mathbf{F}$ a zostrojíme obraz v rovnakej vzdialenosti na opačnej strane priamky.

Pre nájdenie priesečníka môžeme použiť parametrickú rovnicu priamky:
$$
\mathbf{F} \in f \implies \vec{n}\cdot (\mathbf{F} - \mathbf{A}) = 0, \quad 
\mathbf{F} = \mathbf{X} - t\vec{n} \\
\vec{n}\cdot(\mathbf{X} - t\vec{n} - \mathbf{A}) = 0 \implies t = \frac{\vec{n}}{|\vec{n}|^2}\cdot (\mathbf{X} - \mathbf{A}) = \frac{ax + by + c}{a^2+b^2}
$$
Teraz už ľahko vpočítame súradnice bodu $\mathbf{F}$ a $\mathbf{X^{\prime}}$:
$$
\mathbf{F} = \mathbf{X} - \frac{\vec{n}\vec{n}\cdot}{|\vec{n}|^2}(\mathbf{X}-\mathbf{A}) = \mathbf{X} - \mathbf{P_n}(\mathbf{X}-\mathbf{A})
\\
\mathbf{X^{\prime}} = \mathbf{X} - 2\frac{\vec{n}\vec{n}\cdot}{|\vec{n}|^2}(\mathbf{X}-\mathbf{A}) = \mathbf{X} - 2\mathbf{P_n}(\mathbf{X}-\mathbf{A})
$$
kde $\mathbf{P_n}$ je projektor do smeru $\vec{n}$ - je to teda matica, projektujúca vektor do smeru vektora $\vec{n}$. Notácia je tu trocha nešikovná, pretože potrebujeme rozlišovať  riadkové a stĺpcové vektory, čím navyše získame možnosť používať maticové násobenie namiesto skalárneho súčinu:
$$
\vec{a}\cdot\vec{b} \equiv 
(\begin{matrix}
a_x & a_y
\end{matrix})
\left( \begin{matrix}
b_x \\
b_y 
\end{matrix}\right)
= \mathbf{a}^T\mathbf{b}
$$
V tejto notácii je jasnejší aj výraz pre projektor $\mathbf{P_n}$:
$$
\mathbf{P_n} = \frac{\mathbf{n}\mathbf{n}^T}{|\mathbf{n}|^2}
$$
teda v čitateli nemáme skalárny súčin, ale prvý vektor násobí číslo, ktorým je skalárny súčin druhého vektora s tým, čo nasleduje. V maticovom tvare 
$$
\mathbf{P_n} = \frac{1}{|\mathbf{n}|^2}
\left(
\begin{matrix}
n_x \\
m_y 
\end{matrix}
\right)
(\begin{matrix}
n_x & n_y
\end{matrix}) = \frac{1}{|\mathbf{n}|^2}
\left(
\begin{matrix}
n_x^2 & n_xn_y \\
m_yn_x & n_y^2
\end{matrix}
\right)
$$
Z definície projektora je zrejmé, že projekcia je skutočne vektor v smere $\vec{n}$.  Skutočne,
$$
\mathbf{P_{\vec{n}}}\mathbf{n} = \frac{\mathbf{n}\mathbf{n}^T\mathbf{n}}{|\mathbf{n}|^2} = \mathbf{n}
$$
Môžeme zostrojiť aj projektor do kolmého smeru:
$$
\mathbf{P_{\vec{n}\perp}} = \mathbf{1} - \mathbf{P_{\vec{n}}} = \mathbf{1} - \frac{\mathbf{n}\mathbf{n}^T}{|\mathbf{n}|^2}
$$
Skutočne, 
$$
(\mathbf{1} - \mathbf{P_{\vec{n}}})\mathbf{n} = \mathbf{n} - \frac{\mathbf{n}\mathbf{n}^T\mathbf{n}}{|\mathbf{n}|^2} = \mathbf{n} - \mathbf{n} = 0
$$
Riešenie pre priamkové zrkadlenie máme, a ostáva nám iba urobiť skúšku správnosti:

$\mathbf{X} - \mathbf{F} = \mathbf{F} - \mathbf{X^{\prime}} = \mathbf{P_{n}}(\mathbf{X}-\mathbf{A})$ a oba vektory sú kolmé na priamku (vyplýva z definície projektora).

Takéto riešenie ale nie je úplne uspokojivé: radi by sme mali niečo ako operátor zrkadlenia, niečo ako $\mathbf{X^{\prime}} = \mathbf{\Sigma X}$. To ale v tejto reprezentácii nejde, pretože nevieme reprezentovať vektorový súčet, resp. posunutie, ako maticovú operáciu. 

Uvidíme ako na to, keď zavedieme projektívne súradnice.

---

### Pellova rovnica radikálové rozšírenia

Uvažujme takúto rovnicu:
$$
x^2 - 2y^2 = 1\quad x, y \in Z
$$
Niekoľko riešení ľahko uvidíme hneď: $[1,0]$ a $3,2$. Ostatné sa nachádzajú tam, kde hyperbola prechádza celočíselnými uzlami karteziánskej mriežky:

![](img\Pell.png)

Túto rovnicu využijeme na zavedenie radikálového rozšírenia celých čísel: Označme $\mathbf{Z[\sqrt{2}]}$ množinu čísel tvaru $x + y\sqrt{2}, x, y \in Z$. Túto množinu nazývame pridruženým (adjoint) rozšírením celých čísel. Sú to poväčšine iracionálne čísla, ale dedia dôležité vlastnosti celých čísel: uzavretosť pre sčítanie, odčítanie a násobenie. 

*_Definícia_* Normou (veľkosťou) čísla $z = x + y\sqrt{2}$ nazývame číslo $|z|=(z\bar{z})^{1/2} = ((x + \sqrt{2}y)(x-\sqrt{2}y))^{1/2} = (x^2 - 2y^2)^{1/2}$. 

Teda riešením Pellovej rovnice sú čísla zo $\mathbf{Z[\sqrt{2}]}$ s normou 1.  Ľahko ukážeme, že norma je multiplikatívna, teda že $|z_1z_2|=|z_1||z_2|$. Z toho ale vyplýva, že môžeme z jedného riešenia Pellovej rovnice vygenerovať nekonečne veľa ďalších riešení: skutočne, ak $|z|=1$,  potom aj $|z|^n = 1,\,n = 1, 2, \dots$. Teda ďalšie riešenia sú
$$
(3 + 2\sqrt{2})^2 = 17 + 12\sqrt{2} \rightarrow (17, 12) \\
(3 + 2\sqrt{2})^3 = 99 + 70\sqrt{2} \rightarrow (99, 70)
$$
atd. Toto nie je veľmi praktické, ale ľahko si vytvoríme rekurentný vzťah. 



---



## 4. Domáca úloha (nová)

1. Vypočítajte limitu 

$$
\lim_{n\rightarrow\infty} \sqrt{\frac{1}{n}+\sqrt{\frac{1}{n}+ \dots }}
$$

2. Dokážte, že riešenia Pellovej rovnice typu $(3 + 2\sqrt{2})^n, n\rightarrow \infty$ dávajú racionálne aproximácie $\sqrt{2}$.



---



## 5. Program na budúci týždeň

Afínne a projektívne súradnice.

Viac komplexných čísel.

