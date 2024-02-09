## Hodina 9. februára 2024

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

Dokážte, že pre celé n
$$
\cos{n\theta} = 2\cos{\theta}\cos{(n-1)\theta} - \cos{(n-2)\theta} \\
\sin{n\theta} = 2\cos{\theta}\sin{(n-1)\theta} - \sin{(n-2)\theta} 
$$
**Riešenie**

Pomocou štandardných súčtových vzťahov ľahko ukážeme, že
$$
\cos{n\theta} = \cos{\theta}\cos{(n-1)\theta} - \sin{\theta}\sin{(n-1)\theta} \\
\cos{(n-2)\theta} = \cos{\theta}\cos{(n-1)\theta} + \sin{\theta}\sin{(n-1)\theta}
$$
Sčítame a dostaneme prvé tvrdenie,
$$
\cos{n\theta} + cos{(n-2)\theta} = 2\cos{\theta}\cos{(n-1)\theta}
$$
Podobne pre druhé tvrdenie, 
$$
\sin{n\theta} = \cos{\theta}\sin{(n-1)\theta} + \sin{\theta}\cos{(n-1)\theta} \\
\sin{(n-2)\theta} = \cos{\theta}\sin{(n-1)\theta} - \sin{\theta}\cos{(n-1)\theta}
$$
a sčítaním dostaneme druhú časť tvrdenia:
$$
\sin{n\theta} + sin{(n-2)\theta} = 2\cos{\theta}\sin{(n-1)\theta}
$$
**Význam**

Tieto dva vzťahy predstavujú rekurencie pre kosínus a sínus násobného uhla. Vídíme, že kosínus n-násobku uhla vieme napísať ako polynóm v termínoch kosínusu uhla, 
$$
\cos{n\theta} = T_n(\cos{\theta}) \\
\therefore \\
T_n(x) = 2xT_{n-1}(x) - T_{n-2}(x), \quad -1 \le x \le 1 \\
T_0(x) = 1,\quad T_1(x) = x,\quad T_2(x) = 2x^2-1,\quad 
T_3(x) = 4x^3 - 3x
$$
![image-20240209043950668](C:\Users\kvasn\Documents\GitHub\Erik\img\chebyshev1.png)

Tieto polynómy sa nazývajú Čebyševove polynómy 1. druhu. Polynómy druhého druhu neprekvapivo dostvávame z 2. vzľahu:
$$
U_n(\cos{n\theta})\sin{\theta} = \sin{(n+1)\theta} \\
\therefore \\
U_n(x) = 2xU_{n-1}(x) - U_{n-2}(x) \\
U_0(x) = 1,\quad U_1(x) = 2x, \quad U_2(x) = 4x^2-1,\quad U_3(x)=8x^3-4x
$$
![image-20240209045231860](C:\Users\kvasn\AppData\Roaming\Typora\typora-user-images\image-20240209045231860.png)

Tieto polynómy sú dôležité z viacerých dôvodov, predovšetkým ale preto, že tvoria *ortogonálnu bázu*, ateda akýsi ortogonálny súradnicový systém v priestore polynómov. Okrem toho sú rozvoje funkcií v termínoch Čebyševových polynómov v istom zmysle optimálne - minimalizujú maximálnu absolútnu odchýlku od cieľovej funkcie. 

---

**Príklad 2**

Zistite, či sú nasledujúce 3 vektory z priestoru $Z^4$ lineárne nezávislé:
$$
a = [4, 2, 0, 2] \\
b = [2, 2, 2, 1] \\
c = [1, 4, 2, 3]
$$
**Riešenie**

Ľahké, iba si treba uvedomiť, že sme na 4-rozmernej celočíselnej mriežke, takže bežné metódy nefungujú: máme vlastne sústavu 3 diofantických (celočíselných) rovníc. 

Nech existujú 3 nie súčasne nulové celé čísla také, že $k\vec{a} + k\vec{b} + m\vec{c} = 0$. To znamená
$$
4k + 2l + m = 0 \quad (1)\\
2k + 2l + 4m = 0 \quad (2)\\
2l + 2m = 0 \quad (3)\\
2k + l + 3m = 0 \quad (4)
$$
Pomocou tretej rovnice vieme eliminovať $m$, $m = -l$, a teda
$$
4k + l = 0 \quad (1)\\
2k - 2l = 0 \quad (2)\\
2k - 2l = 0 \quad (4)
$$
 Teraz druhá a štvrtá rovnica hovoria to isté, $k = l$ a prvá rovnica nadobúda tvar $5k = 0$. Odtiaľ dostávame, že jediné riešenie je $k=0, l = k = 0, m = -l = 0$. Usudzujeme, že vektory sú lineárne nezávisslé. 

Inak na tomto príklade nie je nič zaujímavé.

---

**Príklad 3**

Do daného kruhového  výseku vpíšte štvorec ABCD tak, aby body AB ležali na kružnicovom oblúku a body CD na spojniciach so stredom výseku S

**Riešenie**

Máme zadaný modrý kruhový výsek.

![13989-17794-rovnolahlost](img\13989-17794-rovnolahlost.jpeg)

Predovšetkým si  všimneme, že celá situácia je osovo symetrická okolo osi výseku (zelená  bodkovaná čiara).  Ďalej vidíme, že požadovaný štvorec nevieme ľahko  zostrojiť, pretože nevieme, kde na oblúku ležia body A, B a nevieme ani, kde vo výseku sa nachádza spodná strana CD. 

 Keby sme ale mali spodnú stranu nejakého štvorca, vedeli by sme takýto  štvorec ľahko zostrojiť. Napríklad sme si zvolili bod U na osi výseku a  ľahko zostrojili fialový štvorec A'B'C'D' (krátko: kolmica na os cez U  dá body C'D', body A', B' na rovnobežkách s osou cez D', C' vo  vzdialenosti C'D' od D', resp. C'.

Vrcholy tohto štvorca ležia na nejakej inej kružnici než máme zadanú,  ale dôležité je, že pomocou štvorca A'B'C'D' vieme zostrojiť požadovaný  štvorec ABCD vďaka vzťahu rovnoľahlosti medzi štvorcami cez vrchol  výseku O. Bod A leží na priesečníku polpriamky OA' s kruhovým oblúkom  K1K2, a bod B na priesečníku polpriamky OB' s týmto oblúkom. A to už  máme hotovo, pretože body D, C ľahko zostrojíme ako priesečníky  rovnobežiek so zelenou osou cez body A, B s ramenami výseku.  						

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

