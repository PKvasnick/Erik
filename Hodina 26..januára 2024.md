## Hodina 2. februára 2024

Program:

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli: matice
3. Poznámky k maticiam: row reduction, násobenie maticou, lineárna regresia
4. Domáca úloha (nová)
5. Program na budúci týždeň

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Videohovor** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

---

### 1. Domáca úloha

**Príklad 1**

Dokážte, že v ľubovoľnom trojuholníku platí $\tan{\alpha} + \tan{\beta} + \tan{\gamma} = \tan{\alpha} \cdot \tan{\beta} \cdot \tan{\gamma}$.

**Riešenie**

Máme trojuholník, takže $\alpha + \beta + \gamma = \pi$. Prepíšeme:
$$
\tan \alpha + \tan \beta + \tan(\gamma = \tan(\alpha + \beta)(1-\tan\alpha \tan\beta) + \tan\gamma \\
= \tan(\alpha+\beta) + \tan\gamma - \tan(\alpha + \beta)\tan\alpha \tan\beta \\
= \tan(\alpha + \beta + \gamma)(1 - \tan(\alpha + \beta)\tan\gamma) -\tan(\pi - \gamma)\tan\alpha\tan\beta 
$$
$\tan\pi=0$,  takže prvý člen je 0. Ďalej $\tan(\pi - \gamma) = -\tan\gamma$, takže druhý člen je $\tan{\alpha} \cdot \tan{\beta} \cdot \tan{\gamma}$, a tvrdenie je dokázané.

**Príklad 2**

Máme v rovine bod S, kružnicu k a priamku p. Zostrojte štvorec ABCD tak, že S je priesečník jeho uhlopriečok, A leží na k a B leží na p. 

**Riešenie**

Modré objekty sú to, čo je zadané: kružnica k, bod S, priamka p. Bod B je obrazom bodu A v rotácii okolo S o $\pm$90°. Takže zrotujeme kružnicu k (hnedé kružnice) a dostaneme možné body B.  Štvorce potom zostrojíme ľahko. 

![](C:\Users\kvasn\Dropbox\doučko\Priklady z doucma\Stvorec_na_kruznici_a_priamke.png)

---



## Niekoľko príkladov na zahriatie a povznesenie mysle

### 1. Ešte náš vzorček na plochu trojuholníka

Máme v rovine 3 body $A=[x_1, y_1], B=[x_2, y_2], C=[x_3, y_3]$. Obsah trojuholníka $ABC$ je 
$$
\pm \frac{1}{2}\begin{array}{|ccc|}
	x_1 & x_2 & x_3 \\ 
	y_1 & y_2 & y_3 \\
	1 & 1 & 1
\end{array}
$$
kde $\pm$ vyjadruje neistotu ohľadne znamienka, ktoré závisí od toho, ako si označíme body trojuholníka. 

To vyzerá ako nejaká projektívna geometria, máme tam afínne súradnice bodov. Z 3D predstavy ľahko pochopíme aj to, ako tento vzťah funguje. 

Tento vzťah je aj dobrý test kolinearity bodov $A, B, C$ a tak ho môžeme použiť aj na iné nekalé účely. 

#### Rovnica priamky, prechádzajúcej dvoma bodmi

Majme priamku, danú dvoma bodmi  $A=[x_1, y_1], B=[x_2, y_2]$. Túto priamku budú tvoriť všetky body, $X = [x, y]$, ktoré sú kolineárne s bodmi $A, B$. Teda pre ne bude platiť (transponovali sme determinant, aby sa nám ľahšie počítalo):
$$
\begin{array}{|ccc|}
	x & y & 1 \\ 
	x_1 & y_1 & 1 \\
	x_2 & y_2 & 1
\end{array}
= 0
$$
Rozvojom podľa prvého riadku dostaneme
$$
x \cdot \begin{array}{|cc|}
	y_1 & 1 \\
	y_2 & 1
\end{array}
- y \cdot \begin{array}{|cc|}
	x_1 & 1 \\
	x_2 & 1
\end{array}
+ \begin{array}{|cc|}
	x_1 & y_1 \\
	x_2 & y_2
\end{array} = 0
$$
resp. 
$$
x(y_1 - y_2) + y(x_1 - x_2) + (x_1y_2 - x_2y_1) = 0
$$
čo je normálová rovnica priamky tvaru $ax + by + c = 0$.

**Príklad** 

Majme   $A=[3, 1], B=[2, 7]$.  Rovnica priamky, prechádzajúcej týmito dvoma bodmi bude
$$
\begin{array}{|ccc|}
	x & y & 1 \\ 
	3 & 1 & 1 \\
	2 & 7 & 1
\end{array}
= 0
$$
odkiaľ máme rovnicu $-6x + y + 19 = 0$.

#### A čo rovnica paraboly?

Analogicky by sme mohli skúsiť
$$
\begin{array}{|cccc|}
	x^2 & x & y & 1 \\
	x_1^2 & x_1 & y_1 & 1 \\
	x_2^2 & x_2 & y_2 & 1 \\
	x_2^2 & x_3 & y_3 & 1 \\
\end{array} = 0
$$
**Príklad**

Uvažujme tri body $A=[-1,3], B=[0,0], C=[2,0]$. Rovnica paraboly bude
$$
\begin{array}{|cccc|}
	x^2 & x & y & 1 \\
	1 & -1 & 3 & 1 \\
	0 & 0 & 0 & 1 \\
	4 & 2 & 0 & 1 \\
\end{array} = 0
$$
Rozvoj podľa tretieho riadku má jediný člen:
$$
\begin{array}{|cccc|}
	x^2 & x & y & 1 \\
	1 & -1 & 3 & 1 \\
	0 & 0 & 0 & 1 \\
	4 & 2 & 0 & 1 
\end{array} = 
(-1) \cdot \begin{array}{|ccc|}
	x^2 & x & y \\
	1 & -1 & 3 \\
	4 & 2 & 0 
\end{array} = (-1)\cdot(-6x^2 + 12x - 6y) = 0
$$
teda rovnica paraboly je $x^2 - 2x - y = 0$, alebo, ako sme viac zvyknutí, $y = (x-1)^2 - 1$. Pravdaže, toto je vzťah pre parabolu s osou rovnobežnou s y. Pre všeobecnejšie formy by sme museli zahrnúť ešte členy $y^2, xy$. To ale znamená, že by sme potrebovali viac bodov, 5, a náš vzťah by sa stal vzťahom pre všeobecnú kužeľosečku. Taký vzťah je ale menej použiteľný, pretože vo všeobecnom prípade je počítanie determinantu 6x6 dosť prácne. 

### 2. O všeobecnej prospešnosti trojuholníkových matíc

Už sme zistili, že ak máme hornú alebo dolnú trojuholníkovú maticu, vieme ľahko riešiť sústavu rovníc alebo vypočítať determinant. Pretože nájdenie inverznej matice nie je nič iné ako riešenie troch sústav lineárnych rovníc, zjavne aj to pôjde ľahšie s trojuholníkovou maticou:
$$
\begin{pmatrix}
	1 & 0 & 0 \\
	2 & 1 & 0 \\
	3 & 4 & 1
\end{pmatrix}
\cdot
\begin{pmatrix}
	1 & 0 & 0 \\
	a & 1 & 0 \\
	b & c & 1
\end{pmatrix}
=
\begin{pmatrix}
	1 & 0 & 0 \\
	0 & 1 & 0 \\
	0 & 0 & 1
\end{pmatrix}
$$
a roznásobením dostaneme:
$$
I_{11}=1 & I_{12} = 0, & I_{13} = 0 \\
I_{2,1} = 2 + a = 0 \therefore a = -2 & I_{22} = 1, & I_{23} = 0 \\
I_{31} = 3 + 4a + b = 0 \therefore b = 5 & I_{32} = 4 + c = 0 \therefore c = -4 & I_{33} = 1
$$
teda 
$$
\begin{pmatrix}
	1 & 0 & 0 \\
	2 & 1 & 0 \\
	3 & 4 & 1
\end{pmatrix}^{-1} =
\begin{pmatrix}
	1 & 0 & 0 \\
	-2 & 1 & 0 \\
	5 & -4 & 1
\end{pmatrix}
$$
Všimneme si, že v jednotlivých krokoch postupne dopočítavame jednotlivé členy inverznej matice a už neriešime sústavu. 

Zovšeobecníme:
$$
A = \{a_{ij}\}, \quad a_{ij}=0 \text{ pre } j > i, \quad a_{ii} \ne 0;\quad i,j = 1,2,3 \\
\begin{pmatrix}
	a_{11} & 0 & 0 \\
	a_{21} & a_{22} & 0 \\
	a_{31} & a_{32} & a_{33}
\end{pmatrix} \cdot \mathbf{A}^{-1} 
=
\begin{pmatrix}
	1 & 0 & 0 \\
	0 & 1 & 0 \\
	0 & 0 & 1
\end{pmatrix}
\\
\begin{pmatrix}
	1 & 0 & 0 \\
	a_{21}/a_{22} & 1 & 0 \\
	a_{31}/a_{33} & a_{32}/a_{33} & 1
\end{pmatrix} \cdot \mathbf{A}^{-1}
=
\begin{pmatrix}
	1/a_{11} & 0 & 0 \\
	0 & 1/a_{22} & 0 \\
	0 & 0 & 1/a_{33}
\end{pmatrix} \\
\begin{pmatrix}
	1 & 0 & 0 \\
	0 & 1 & 0 \\
	0 & a_{32}/a_{33} & 1
\end{pmatrix} \cdot \mathbf{A}^{-1}
=
\begin{pmatrix}
	1 & 0 & 0 \\
	-a_{21}/a_{22} & 1 & 0 \\
	-a_{31}/a_{33} & 0 & 1
\end{pmatrix} 
\cdot
\begin{pmatrix}
	1/a_{11} & 0 & 0 \\
	0 & 1/a_{22} & 0 \\
	0 & 0 & 1/a_{33}
\end{pmatrix} 
 \\
 \mathbf{A}^{-1} =
 \begin{pmatrix}
	1 & 0 & 0 \\
	0 & 1 & 0 \\
	0 & -a_{32}/a_{33} & 1
\end{pmatrix} 
\cdot
\begin{pmatrix}
	1 & 0 & 0 \\
	-a_{21}/a_{22} & 1 & 0 \\
	-a_{31}/a_{33} & 0 & 1
\end{pmatrix} 
\cdot
\begin{pmatrix}
	1/a_{11} & 0 & 0 \\
	0 & 1/a_{22} & 0 \\
	0 & 0 & 1/a_{33}
\end{pmatrix} \\
\mathbf{A}^{-1} =
\begin{pmatrix}
	1 & 0 & 0 \\
	-a_{21}/a_{22} & 1 & 0 \\
	-a_{31}/a_{33}+a_{21}/a_{22}\cdot a_{32}/a_{33} & -a_{32}/a_{33} & 1
\end{pmatrix} 
\cdot
\begin{pmatrix}
	1/a_{11} & 0 & 0 \\
	0 & 1/a_{22} & 0 \\
	0 & 0 & 1/a_{33}
\end{pmatrix} \\
\mathbf{A}^{-1} =
\begin{pmatrix}
	1/a_{11} & 0 & 0 \\
	-a_{21}/(a_{11}a_{22}) & 1/a_{22} & 0 \\
	-a_{31}/(a_{11}a_{33})+a_{21}a_{32}/(a_{11}a_{22}a_{33}) & -a_{32}/(a_{22}a_{33}) & 1/a_{33}
\end{pmatrix} 
$$
Pretože vidíme, že trojuholníkové matice sú fajn, je na mieste pýtať sa, či a ako možno všeobecnú maticu previesť na trojuholníkovú. Tomu sa hneď ideme venovať, ale trocha okľukou.



---



## Matice et al.

### 1. **Čo robí násobenie maticou?**

Môžeme vziať nejakú plochu v rovine, vziať niekoľko vektorov, ktoré v nej končia, transformovať ich pomocou matice a pozrieť sa, v akej oblasti sa nachádzajú. Napríklad si môžeme vziať maticu 
$$
\mathbf{A}= \begin{pmatrix}
1 & -1 \\
1/2 & 1
\end{pmatrix}
$$
a pozrieť sa, čo sa stane s jednotkovým štvorcom:

![](img\Matrix.png)

Zväčšenie plochy je dané *determinantom* matice, teda červený rovnobežník má plochu 1.5-krát väčšiu ako modrý, ako ľahko vidieť z obrázku. Táto vlastnosť je veľmi všeobecná, nezávisí od polohy v priestore ani od tvaru východiskovej oblasti.

Dokážeme pre náš prípad:

Strany štvorca sa transformujú na strany rovnobežníka takto:
$$
\vec{a^{\prime}} \equiv \vec{AB^{\prime}}  = 
\begin{pmatrix}
	1 & -1 \\
	1/2 & 1
\end{pmatrix} 
\cdot
\begin{pmatrix}
	1 \\ 0
\end{pmatrix} 
=
\begin{pmatrix}
	1 \\ 1/2
\end{pmatrix} ,
\\
\vec{b^{\prime}} \equiv \vec{AD^{\prime}}  = 
\begin{pmatrix}
	1 & -1 \\
	1/2 & 1
\end{pmatrix} 
\cdot
\begin{pmatrix}
	0 \\ 1
\end{pmatrix} 
=
\begin{pmatrix}
	-1 \\ 1
\end{pmatrix}
$$
Plochu červeného rovnobežníka ľahko vypočítame ako vektorový súčin, teda
$$
\vec{a^{\prime}} \times \vec{b^{\prime}} \equiv
\begin{array}{|ccc|}
	\vec{i} & \vec{j} & \vec{k} \\
	1 & 1/2 & 0 \\
	-1 & 1 & 0
\end{array} = 
\vec{k}\det \mathbf{A}
$$
Determinant je zvláštna funkcia:

- je to lineárna funkcia N vektorových argumentov
- je antisymetrická vo všetkých dvojiciach argumentov - teda vzájomná výmena dvoch argumentov zmení znamienko determinantu.

Dá sa ukázať, že taká funkcie je (až na konštantný faktor) jediná. 

**Stopa**

Stopa matice (alebo iného operátora) $\mathbf{A}$ je lineárny člen rozvoja determinantu $|1+\epsilon \mathbf{A}|$ podľa $\epsilon$. 

Príklad:
$$
|1 + \epsilon\mathbf{A}| \equiv 
\begin{array}{|cc|}
1 + \epsilon & -\epsilon \\
1/2 \cdot \epsilon & 1 + \epsilon
\end{array} =
1 + 2\epsilon + O(\epsilon^2)
$$
takže stopa matice A je 2, a ľahko vidno, že to je súčet diagonálnych prvkov. Napriek tomu, že vyzerá triviálne, stopa je veľmi dôležitá veličina.

### 2. Lineárna regresia

V prípade lineárnej regresie máme preurčenú sústavu lineárnych rovníc:
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
V skutočnosti ale neformulejeme problém ako minimalizáciu skalárneho súčinu, ale ako minimalizáciu stopy:
$$
\mathrm{\hat{\beta}} = \textrm{argmin Tr}\left[(\mathbf{Y}-\mathbf{F}\mathbf{\beta})(\mathbf{Y}-\mathbf{F}\mathbf{\beta})^T\right]
$$
Stopa matice $Tr$ je súčet jej diagonálnych prvkov. Toto je všeobecnejší výraz, ktorý funguje v širšej škále prípadov, a jeho minimalizácia podľa $\mathbf{\beta}$ je určitým spôsobom ľahšia. 



---

##  Domáca úloha (nová) 







---

## 5. Program na budúci týždeň

- Ešte lineárna algebra: eigen...


$$
\bar{a}
$$

