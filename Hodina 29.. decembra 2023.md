## Hodina 29. decembra 2023

Program:

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli: matice
3. Row reduction
4. Domáca úloha (nová)
5. Program na budúci týždeň

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Videohovor** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

---

### 1. Domáca úloha

**Príklad 1**

Nájdite všetky $y \in C$, spĺňajúce rovnicu
$$
\sqrt{+y} + \sqrt{-y} = 4
$$

Návod: U reálnej odmocniny berieme ako hodnotu nezáporné riešenie rovnice $w^2 = y, w, y \in R_+$. U V komplexných číslach takúto konvenciu nemáme a odmocnina je viacznačná (preto sa znak odmocniny pre komplexné čísla prakticky nepoužíva).

**Riešenie**

Píšme  $y = |y|e^{i\phi}$, $\sqrt{.} \rightarrow (.)^{1/2}$. Najprv vypočítame odmocniny:
$$
w_+^2=y=|y|e^{i\phi} \implies w_{+1} = |y|^{1/2}e^{i\phi/2},\quad  w_{+2} = |y|^{1/2}e^{i(\phi/2+\pi)}
\\
w_-^2=-y=|y|e^{i(\phi+\pi)} \implies w_{-1} = |y|^{1/2}e^{i(\phi/2+\pi/2)},\quad  w_{+2} = |y|^{1/2}e^{i(\phi/2+3\pi/2)}
$$

Polohu koreňov v komplexnej rovine zobrazuje nasledujúca schéma:

<img src="C:\Users\kvasn\Documents\GitHub\Erik\img\complex_sqrt.png" style="zoom:12%;" />

Potrebujeme skombinovať červený a modrý koreň tak, aby sme dostali reálne číslo 4.  Na to musí byť $\phi = \pi/2$ alebo $\phi = -\pi/2$
$$
 w_{+1} + w_{-2} = |y|^{1/2}e^{i\pi/4} + |y|^{1/2}e^{-i\pi/4}=2|y|^{1/2}\cos{\frac{\pi}{4}}=4 \\
 |y|^{1/2}=2\sqrt{2} \implies |y| = 8
$$
a teda máme riešenie $y = 8i$, zatiaľ čo druhá možnosť dáva riešenie $y=-8i$. Skúška správnosti:
$$
y = +8i:\quad \sqrt{+8i} + \sqrt{-8i} = 2\sqrt{2}\left(\frac{1+i}{\sqrt{2}}\right) + 2\sqrt{2}\left(\frac{1-i}{\sqrt{2}}\right) = 4 \\
y = -8i:\quad \sqrt{-8i} + \sqrt{+8i} = 2\sqrt{2}\left(\frac{1-i}{\sqrt{2}}\right) + 2\sqrt{2}\left(\frac{1+i}{\sqrt{2}}\right) = 4 
$$
To sme ale využili iba jednu dvojicu odmocnín, pomocou tej druhej vieme skonštruovať riešenie rovnice s -4 na pravej strane. 

---

**Príklad 2**

Nájdite r

![image-20231215102926989](img\image-20231215102926989.png)

**Riešenie**

Body dotyku na odvesnách delia pravouhlý trojuholník na štvorec o polomere r a dva menšie pravouhlé trojuholníky, podobné pôvodnému. Z podobnosti trojuholníkov vyplýva
$$
\frac{a-r}{r} = \frac{r}{b-r} \implies ab - ar - br = 0 \implies r = \frac{ab}{a+b}
$$
Ľahké.

---

**Príklad 3**

Nájdite $\tan{(\alpha + \beta)}$ v termínoch $\tan{\alpha}, \tan{\beta}$.

**Riešenie**

Použijeme súčtové výrazy pre sínus a kosínus, a vydelíme čitateľ i menovateľ výrazom $\cos{\alpha}\cos{\beta}$, aby sme dostali výraz v termínoch $\tan{\alpha},\,\tan{\beta}$:
$$
\tan{(\alpha + \beta)} = \frac{\sin{(\alpha + \beta)}}{\cos{(\alpha + \beta)}} = \frac{\sin{\alpha}\cos{\beta}+\cos{\alpha}\sin{\beta}}{\cos{\alpha}\cos{\beta}-\sin{\alpha}\sin{\beta}} = \frac{\tan{\alpha} + \tan{\beta}}{1-\tan{\alpha}\tan{\beta}}
$$

---


**Príklad 3**

Je daný bod $Q=[-3,1]$. Vypočítajte polohy stredov všetkých kružníc o polomere $r=\sqrt{20}$ , ktoré prechádzajú počiatkom $O=[0,0]$ a bodom Q.

**Riešenie**

Máme samé stredy a pravé uhly, takže to je ľahučké:

![](C:\Users\kvasn\Documents\GitHub\Erik\img\Homework4.png)

Vykročme od počiatku súradníc do pol cesty smerom k bodu Q: Príslušný vektor je $\vec{u} = (-3/2, 1/2)$ a jeho dĺžka je $\sqrt{10}/2$.  Smerom ku stredu kružnice musíme teraz vykročiť v kolmom smere k $\vec{u}$, teda v smere $\vec{u}_{\perp}=(1/2, 3/2)$. Aby sme dostali polomer kružnice $\sqrt{20}$, ľahko uvidíme že potrebujeme $\sqrt{7}$-násobok vektora $\vec{u}_{\perp}$ v jednom i druhom smere. Takto dostaneme dva stredy, $S_1 = (-3/2+\sqrt{7}/2, 1/2+3\sqrt{7}/2)$ a  $S_1 = (-3/2-\sqrt{7}/2, 1/2-3\sqrt{7}/2)$. Pre skúšku správnosti stačí skontrolovať vzdialenosť $S_1, S_2$ od počiatku - bodu P.

---



## Niekoľko príkladov na zahriatie a povznesenie mysle

### Lineárna nezávislosť a ortogonálne bázy vektorov

**Negatívna definícia**

Vektory $\vec{a}, \vec{b}, \vec{c}$ nazývame *_lineárne závislými_*, ak existuje ich nulová lineárna kombinácia, teda čísla $d_1, d_2, d_3 \in R$ také, že $d_1\vec{a} + d_2\vec{b} + d_3\vec{c} = 0$.  Znamená to, že priestor, tvorený lineárnymi kombináciami vektorov má nižšiu dimenziu než 3.

Trojice vektorov, ktoré sú lineárne závislé, môžeme použiť ako súradnice vektorového priestoru: každý bod-vektor $\vec{x}$ vieme jednoznačne vyjadriť ako lineárnu kombináciu vektorov $\vec{a}, \vec{b}, \vec{c}$.

**Diagnostika**

Ako zistím, či je nejaká trojica vektorov $\vec{a}, \vec{b}, \vec{c}$ lineárne nezávislá?

1. Geometrická metóda: Vypočítam objem hranola s hranami $\vec{a}, \vec{b}, \vec{c}$. Ten je 
   $$
   V = \vec{a}\cdot(\vec{b}\times \vec{c}) = \vec{b}\cdot(\vec{c}\times \vec{a}) = \vec{c}\cdot(\vec{a}\times \vec{b})
   $$
   (vektorový súčin mi dá plochu podstavy, a skalárny priemet tretieho vektora do normály na podstavu, čiže výšku). Keď si vyjadríme vektorový súčin ako determinant a urobíme skalárny súčin, zistíme, že úloha sa redukuje na zistenie, či je determinant matice, vytvorenej vektormi $\vec{a}, \vec{b}, \vec{c}$ nulový:
   $$
   V = \vec{a}\cdot(\vec{b}\times\vec{c}) = \vec{a}\cdot 
   \begin{vmatrix}
   \vec{i} & \vec{j} & \vec{k} \\
   b_1 & b_2 & b_3 \\
   c_1 & c_2 & c_3
   \end{vmatrix} = 
   \begin{vmatrix}
   a_1 & a_2 & a_3 \\
   b_1 & b_2 & b_3 \\
   c_1 & c_2 & c_3
   \end{vmatrix}
   = 0
   $$
   Že to takto funguje sa dá najlepšie uvidieť tak, že rozložíme determinant vektorového súčinu podľa horného riadku, urobíme skalárny súčin, a poskladáme ho naspäť.

2. Algebraická metóda: Riešim sústavu $d_1\vec{a} + d_2\vec{b} + d_3\vec{c} = 0$ niektorou z dostupných metód, resp. robím diagnostiku matice sústavy, či nie je singulárna - teda či jej hodnosť = počet lineárne nezávislých riadkov/stĺpcov nie je menšia ako rozmer. Táto metóda sa dá ľahko previesť na test nulovosti determinantu ako v predchádzajúcom prípade, ale môžeme sa tiež pokúsť previesť maticku na hornú trojuholníkovú pomocou ekvivalentných úprav a zistiť, ako to dopadne.



### Matice: Redukcia po riadkoch (row reduction)

Ekvivalentné úpravy: ľubovoľný riadok alebo stĺpec matice môžeme nahradiť lineárnou kombináciou všetkých riadkov či stĺpcov.

**Problém 1** : Nachádza sa vektor 
$$
\vec{v} = \begin{pmatrix}2 \\ 1 \\ -1\end{pmatrix}
$$
v priestore pokrytom vektormi 
$$
a_1 = \begin{pmatrix}1 \\ -2 \\ 3\end{pmatrix}\quad 
a_2 = \begin{pmatrix}0 \\ 3 \\ -3\end{pmatrix}\quad 
a_3 = \begin{pmatrix}-1 \\ -1 \\ 0\end{pmatrix}\quad ?
$$
**Riešenie** Priestorom pokrytým vektormi $\vec{a_1}, \vec{a_2}, \vec{a_3}$ myslíme vektorový priestor, tvorený všetkými lineárnymi kombináciami týchto vektorov; tento priestor sa označuje ako *_span_*, čiže rozpätie:
$$
\textrm{Span}(\vec{a_1}, \vec{a_2}, \vec{a_3}) = \{\vec{x} : \exist c_1, c_2, c_3 \in R \textrm{ také že } \vec{x} = c_1\vec{a_1}+ c_2\vec{a_2}+c_3\vec{a_3} \}
$$
Otázku teda môžeme preformulovať takto: Existujú tri reálne čísla $c_1, c_2, c_3$ také, že platí 
$$
\begin{pmatrix}2 \\ 1 \\ -1\end{pmatrix} = 
c_1\begin{pmatrix}1 \\ -2 \\ 3\end{pmatrix} + 
c_2\begin{pmatrix}0 \\ 3 \\ -3\end{pmatrix}+
c_3\begin{pmatrix}-1 \\ -1 \\ 0\end{pmatrix}\quad ?
$$
 Rozpísaním po zložkách dostaneme sústavu troch lineárnych rovníc
$$
\begin{array}{cccc}
c_1 && &-&c_3 &=& 2 \\
-2c_1 &+& 3c_2 &-& c_3 &=& 1 \\
3c_1 &-& 3c_2 && &=& -1
\end{array}
$$
Aj keď nás tu riešenie zvlášť nezaujíma a potrebujeme iba vedieť, či existuje. Štandardným spôsobom zostavíme rozšírenú (augmentovanú) maticu a Gaussovou metódou vyriešime sústavu:
$$
\left(
    \begin{array}{ccc|c}
        1 & 0 & -1 & 2 \\
        -2 & 3 & -1 & 1 \\
        3 & -3 & 0 & -1 \\
    \end{array}
\right) \rightarrow
\left(
    \begin{array}{ccc|c}
        1 & 0 & -1 & 2 \\
        0 & 3 & -3 & 5 \\
        0 & -3 & 3 & -7 \\
    \end{array}
\right) \rightarrow
\left(
    \begin{array}{ccc|c}
        1 & 0 & -1 & 2 \\
        0 & 3 & 1 & 5 \\
        0 & 0 & 0 & -2 \\
    \end{array}
\right)
$$
a dostali sme na treťom riadku výraz $0=-2$, čo znamená, že sústava nemá riešenie a vektor teda neleží v priestore, tvorenom danými troma vektormi. 

Pozrime sa na tento problém z inej strany: Čo musí platiť pre všeobecný vektor $\vec{x} = (x_1, x_2, x_3)$, aby ležal v spane vektorov $\vec{a_1}, \vec{a_2}, \vec{a_3}$ ? Napíšme znova našu augmentovanú maticu a riešme:
$$
\left(
    \begin{array}{ccc|c}
        1 & 0 & -1 & x_1 \\
        -2 & 3 & -1 & x_2 \\
        3 & -3 & 0 & x_3 \\
    \end{array}
\right) \rightarrow
\left(
    \begin{array}{ccc|c}
        1 & 0 & -1 & x_1 \\
        0 & 3 & -3 & 2x_1 + x_2 \\
        0 & -3 & 3 & -3x_1 + x_3 \\
    \end{array}
\right) \rightarrow
\left(
    \begin{array}{ccc|c}
        1 & 0 & -1 & x_1 \\
        0 & 3 & 1 & 2x_1 + x_2 \\
        0 & 0 & 0 & -x_1 + x_2 + x_3 \\
    \end{array}
\right)
$$
teda pre zložky vektora $\vec{x}$ musí platiť $-x_1 + x_2 + x_3 = 0$. Kde žijú také vektory? Stačí sa pozrieť na výraz, ktorý sme dostali, ako na rovnicu roviny: je to rovina prechádzajúca počiatkom a má normálový vektor $\vec{n} = (-1, 1, 1)$ - a to nám dáva dobrú predstavu o spane vektorov $\vec{a_1}, \vec{a_2}, \vec{a_3}$. Aby to celé dávalo zmysel, musia vektory $\vec{a_1}, \vec{a_2}, \vec{a_3}$ tiež ležať v tejto rovine!

---

**Problém 2** Nájdite kvadratickú funkciu $y = a_2x^2 + a_1x + a_0$, ktorá prechádza bodmi $[1,3],[2,-1],[3,5]$.

**Riešenie**: Máme tri neznáme koeficienty $a_0, a_1, a_2$, a tri body nám dajú tri rovnice pre tieto koeficienty.
$$
a_2 x_1^2 + a_1 x_1 + a_0 = y_1 \\
a_2 x_2^2 + a_1 x_2 + a_0 = y_2 \\
a_2 x_3^2 + a_1 x_3 + a_0 = y_3
$$
V maticovom tvare
$$
\begin{pmatrix}
	x_1^2 & x_1 & 1 \\
	x_2^2 & x_2 & 1 \\
	x_3^2 & x_3 & 1 
\end{pmatrix}
\cdot
\begin{pmatrix}
	a_2\\
	a_1\\
	a_0
\end{pmatrix}
=
\begin{pmatrix}
	y_1 \\
	y_2 \\
	y_3 
\end{pmatrix}
$$
*_Poznámka_* Síce hľadáme kvadratickú funkciu a v matici máme druhé mocniny koeficientov, ale nájdenie koeficientov je lineárny problém. 

Môžeme dosadiť hodnoty $x_i, y_i$ pre naše tri body, zostaviť augmentovanú maticu a vyriešiť sústavu:
$$
\left(
    \begin{array}{ccc|c}
        1 & 1 & 1 & 3 \\
        4 & 2 & 1 & -1 \\
        9 & 3 & 1 & 5 \\
    \end{array}
\right) \xrightarrow{R_2-=4R_1}
\left(
    \begin{array}{ccc|c}
        1 & 1 & 1 & 3 \\
        0 & -2 & -3 & -13 \\
        9 & 3 & 1 & 5 \\
    \end{array}
\right) \xrightarrow{R_3-=9R_1}
\left(
    \begin{array}{ccc|c}
        1 & 1 & 1 & 3 \\
        0 & -2 & -3 & -13 \\
        0 & -6 & -8 & -22 \\
    \end{array}
\right) \\ \xrightarrow{R_3-=3R_2}
\left(
    \begin{array}{ccc|c}
        1 & 1 & 1 & 3 \\
        0 & -2 & -3 & -13 \\
        0 & 0 & 1 & 17 \\
    \end{array}
\right) \xrightarrow{R_2+=3R_3}
\left(
    \begin{array}{ccc|c}
        1 & 1 & 1 & 3 \\
        0 & -2 & 0 & 38 \\
        0 & 0 & 1 & 17 \\
    \end{array}
\right) \\ \xrightarrow{R_2/=-2}
\left(
    \begin{array}{ccc|c}
        1 & 1 & 1 & 3 \\
        0 & 1 & 0 & -19 \\
        0 & 0 & 1 & 17 \\
    \end{array}
\right) \xrightarrow{R_1-=R_2+R_3}
\left(
    \begin{array}{ccc|c}
        1 & 0 & 0 & 5 \\
        0 & 1 & 0 & -19 \\
        0 & 0 & 1 & 17 \\
    \end{array}
\right)
$$
Nezastavili sme sa, keď sme maticu vľavo previedli na hornú trojuholníkovú (*row echelon form*), ale uviedli sme ju do tvaru jednotkovej matice (*reduced row echelon form*) a vidíme, že hľadaná kvadratická funkcia má tvar $y=5x^2 - 19x + 17$.

**Odbočka 1: Interpolácia**: Predchádzajúci problém je problém interpolácie. Ukážeme si iné, priamočiarejšie riešenie: Uvažujme polynómy 
$$
l_j^{(3)} = \prod_{i\ne j}^3 \frac{x-x_i}{x_j-x_i} \\
l_1^3 = \frac{(x - x_2)(x-x_3)}{(x_1-x_2)(x_1-x_3)} \\
l_2^3 = \frac{(x - x_1)(x-x_3)}{(x_2-x_1)(x_2-x_3)} \\
l_3^3 = \frac{(x - x_1)(x-x_2)}{(x_3-x_1)(x_3-x_2)} 
$$
Sú to kvadratické polynómy, normované tak, aby v príslušnom $x_j$ mali hodnotu 1, a v ostatných $x_i, i\ne j$ sú nulové. Nazývajú sa Lagrangeove polynómy. Lagrangeov interpoland potom skonštruujeme ako lineárnu kombináciu:
$$
y_L(x) = \sum_{j=0}^3 l_j^{(3)}y_j
$$
Takto možno zostrojiť interpoland pre ľubovoľný počet bodov. 

**Odbočka:  Lineárna regresia** Predchádzajúci problém je problém interpolácie - hľadáme funkciu, prechádzajúcu danými bodmi. Aby mala úloha riešenie, potrebujeme funkciu s toľkými parametrami, koľko máme bodov. Pri vyššom počte bodov nemusí byť riešenie to, čo si predstavujeme - môže divoko oscilovať medzi zadanými bodmi.  Preto často preferujeme funkciu s menej parametrami, než máme bodov, aj za cenu, že výsledná funkcia nebude prechádzať všetkými bodmi - dôležité je, že bude hladšia. Ak sú body výsledkom merania a teda súradnice nie sú presné, potom je to veľmi rozumný kompromis. Ale ako to spraviť, keď máme viac bodov ako parametrov? Teda, keď naše rovnice vyzerajú takto:
$$
\begin{pmatrix}
	x_1^2 & x_1 & 1 \\
	x_2^2 & x_2 & 1 \\
	x_3^2 & x_3 & 1 \\
	& \cdots & \\
	x_n^2 & x_n & 1 \\
\end{pmatrix}
\cdot
\begin{pmatrix}
	a_2\\
	a_1\\
	a_0
\end{pmatrix}
=
\begin{pmatrix}
	y_1 \\
	y_2 \\
	y_3 \\
	\cdots \\
	y_n 
\end{pmatrix}
\quad
\text{resp.}
\quad
\mathbf{F}\mathbf{\beta} = \mathbf{Y}
$$
Používame štandardné označenie $\mathbf{F}$ pre maticu faktorov, ktorej členy závisia od hodnôt $x_i$, a maticu parametrov $\beta$.  Rovnica dáva zmysel, iba ak nadbytočné dáta sú zbytočné a hovoria to isté.  Ak hovoria niečo iné, úloha nemá riešenie. Môžeme sa ale pozrieť na úlohu tak, že chceme nájsť takú krivku, definovanú parametrami $a_i$, pre ktorú je súčet štvorcov odchýlok hodnôt y najmenší, teda 
$$
\mathrm{\hat{\beta}} = \textrm{argmin}\left[(\mathbf{Y}-\mathbf{F}\mathbf{\beta})^T(\mathbf{Y}-\mathbf{F}\mathbf{\beta})\right]
$$
Riešenie si vyžaduje trošku zložitejšie derivovanie, ale vyzerá takto:
$$
\mathbf{(F^T F)\beta} = \mathbf{F^T Y} \quad \therefore \quad \mathbf{\beta} = \mathbf{(F^T F)^{-1}F^T Y}
$$
Všeobecne ale rozhodnutie, aký stupeň polynómu je vhodný pre vystihnutie priebehu dát je celkom ťažké a závisí od okolností. 

---

**Problém 3**

Továreň vyrába osobné autá, nákladné autá a autobusy. Tri hlavné suroviny, ktoré používa, sú oceľ,  sklo a plasty.  Nasledujúca tabuľka obsahuje množstvo surovín, potrebných na jednotlivé výrobky, vo vhodných jednotkách:

|       | Osobné auto | Nákladné auto | Autobus |
| :---: | :---------: | :-----------: | :-----: |
| Oceľ  |      1      |       4       |    6    |
| Sklo  |      2      |       3       |   20    |
| Plast |      3      |       5       |   15    |

Denne sa v priemere spotrebuje 48 jednotiek ocele, 113 jednotiek skla a 111 jednotiek plastov. Koľko osobných áut, nákladných áut a autobusov sa priemerne denne vyrobí?

**Riešenie** Označme $c, t, b$ priemerný počet denne vyrobených osobných áut, nákladných áut a autobusov (*c*ars, *t*rucks, *b*usses).  Tabuľka spotreby materiálov pre jednotlivé výrobky nám dáva sústavu lineárnych rovníc pre $c, t, b$:
$$
\begin{pmatrix}
	1 & 4 & 6 \\
	2 & 3 & 20 \\
	3 & 5 & 15 
\end{pmatrix}
\cdot
\begin{pmatrix}
	c \\
	t \\
	b
\end{pmatrix}
=
\begin{pmatrix}
	48 \\
	113 \\
	111 
\end{pmatrix}
$$
a riešime zase zostrojením augmentovanej matice a jej uvedením do RREF tvaru:
$$
\left(
    \begin{array}{ccc|c}
        1 & 4 & 6 & 48 \\
        2 & 3 & 20 & 113 \\
        3 & 5 & 15 & 111 \\
    \end{array}
\right) \xrightarrow{R_2-=2R_1}
\left(
    \begin{array}{ccc|c}
        1 & 4 & 6 & 48 \\
        0 & -5 & 8 & 17 \\
        3 & 5 & 15 & 111 \\
    \end{array}
\right) \xrightarrow{R_3-=3R_1}
\left(
    \begin{array}{ccc|c}
        1 & 4 & 6 & 48 \\
        0 & -5 & 8 & 17 \\
        0 & -7 & -3 & -33 \\
    \end{array}
\right) \\ \xrightarrow{R_3=5R_3 - 7R_2}
\left(
    \begin{array}{ccc|c}
        1 & 4 & 6 & 48 \\
        0 & -5 & 8 & 17 \\
        0 & 0 & -71 & -284 \\
    \end{array}
\right) \xrightarrow{R_3/=-71}
\left(
    \begin{array}{ccc|c}
        1 & 4 & 6 & 48 \\
        0 & -5 & 8 & 17 \\
        0 & 0 & 1 & 4 \\
    \end{array}
\right) \\ \xrightarrow{R_2-=8R_3}
\left(
    \begin{array}{ccc|c}
        1 & 4 & 6 & 48 \\
        0 & -5 & 0 & -15 \\
        0 & 0 & 1 & 4 \\
    \end{array}
\right) \xrightarrow{R_2/=-5}
\left(
    \begin{array}{ccc|c}
        1 & 4 & 6 & 48 \\
        0 & 1 & 0 & 3 \\
        0 & 0 & 1 & 4 \\
    \end{array}
\right) \xrightarrow{R_1-=4R_2 + 6R_3}
\left(
    \begin{array}{ccc|c}
        1 & 0 & 0 & 12 \\
        0 & 1 & 0 & 3 \\
        0 & 0 & 1 & 4 \\
    \end{array}
\right) 
$$
V priemere sa teda vyrobí 12 osobných, 3 nákladné automobily a 4 autobusy. 

*Poznámka* V tomto prípade sme mali šťastie a vyhli sme sa zásadnému problému takýchto úloh: ako zabezpečiť, aby sme dostali $c, t, b \ge 0$? Typicky sa takáto úloha rieši tak, že hľadáme projekciu riešenia lineárneho systému do podpriestoru $c, t, b \ge 0$ - najbližší vektor k vektoru riešenia, ktorý už leží v požadovanom podpriestore. 



---

##  Domáca úloha (nová) 

1. Dokážte, že v trojuholníku ABC leží priesečník osi uhla $\beta$ (pri vrchole B) a osi strany $b$ (oproti vrcholu B) na kružnici opísanej trojuholníku. 
2. Vezmime ľubovoľný bod P vnútri rovnostrannného trojuholníka. Dokážte že súčet jeho vzdialeností od strán trojuholníka je rovný výške trojuholníka (teda je pre všetky body vnútri trojuholníka rovnaký).
3. 



---

## 5. Program na budúci týždeň

Zmes:

- Viac komplexných čísel a goniometrie


$$
\bar{}
$$


