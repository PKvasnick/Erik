## Hodina 9. februára 2024

**Program**

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli: matice
3. Ortogonálne bázy a QR rozklad matice
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

### 1. Cramérovo pravidlo

**Všeobecné vlastnosti determinantu**

Majme štvorcovú maticu A a jej determinant $\det{A}$. Naučili sme sa, že

- $det{A}$ je antisymetrická funkcia stĺpcov matice A: ak vzájomne vymeníme dva stĺpce, determinant zmení znamienko
- jednoduchý dôsledok predchádzajúceho: ak sú dva stĺpce A rovnaké, determinant bude 0.
- Determinant je lineárnou funkciou prvkov svojho ľubovoľného stĺpca, pretože ho môžeme rozvinúť podľa prvkov stĺpca.

$$
\det{A} = \sum_j a_{jk}C_{jk}
$$

$a_{jk}$ je prvok matice v j-tom riadku a k-tom stĺpci, $C_{jk}$ je príslušný komplement, teda determinant matice vzniknutej vynechaním j-teho riadku a k-teho stĺpca z natice A, krát $(-1)^{j+k}$. Komplementy $C_{jk}$ sú funkciami prvkov matice okrem tých, ktoré sú v k-tom stĺpci, a teda $\det{A}$ je lineárna funkcia prvkov k-teho stĺpca. 

Všetky predchádzajúce tvrdenia pre stĺpce matice A platia rovnako pre riadky matice. 

**Cramérovo pravidlo**

Uvažujme determinant matice A ako lineárnu funkciu prvkov zvoleného $k-$teho stĺpca matice:
$$
D(a_{1k}, a_{2k},\dots, a_{nk}) \equiv D(\vec{a_k}) = \sum_j a_{jk}C_{jk}
$$
Ak namiesto prvkov k-teho stĺpca dosadíme prvky iného stĺpca, dostaneme výraz pre determinant matice s dvoma rovnakými stĺpcami, teda 0.

Teraz si vezmieme sústavu rovníc
$$
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2 \\
\dots \\
a_{n1}x_1 + a_{n2}x_2 + \dots + a_{nn}x_n = b_n \\
$$
Vynásobme prvý riadok $C_{1k}$, druhý $C_{2k}$, atď.  a rovnice sčítame:
$$
D(\vec{a_1})x_1 + D(\vec{a_2})x_2 + \dots + D(\vec{a_n})x_n = D(\vec{b})
$$
Vyššie sme dokázali, že 
$$
D(\vec{a_i}) = \begin{cases}
	\det{A} & i=k \\
	0, & i \ne k
\end{cases}
$$
a teda rovnica bude mať tvar
$$
D(\vec{a_k})x_k = D(\vec{b})\quad \therefore \quad x_k = \frac{D(\vec{b})}{D(\vec{a_k})} = \frac{D(\vec{b})}{\det{A}}
$$
$D(\vec{b})$ je determinant matice, ktorú získame z matice A tak, že jej  k-ty stĺpec nahradíme pravou stranou sústavy. A toto je Cramérovo pravidlo: pomocou takýchto determinantov vieme ľahko vypočítať riešenie sústavy rovníc. 

Ešte by sme mali dokázať, že takto vypočítané $x_k, \, k=1, 2, \dots n$ sú skutočne riešením sústavy. Dosadením za $x_k$ podľa Cramérovho pravidla dostaneme
$$
\sum_i a_{ik}\frac{D_i(\vec{b})}{\det{A}} = \frac{1}{\det{A}}\sum_{i}a_{ik} b_k C_{ik} = \frac{1}{\det{A}}D_k{\vec{a_k}}b_k = b_k
$$
Až teraz je dôkaz úplný.

**Príklad**
$$
x + y + z = 2 \\
2x + y + 3z = 9 \\
x - 3y + z = 10
$$
Potrebné determinanty sú
$$
D = \left|
\begin{array}{ccc}
1 & 1 & 1 \\
2 & 1 & 3 \\
1 & -3 & 1
\end{array}
\right| = 10 + 1 - 7 = 4 \\
D_x = \left|
\begin{array}{ccc}
2 & 1 & 1 \\
9 & 1 & 3 \\
10 & -3 & 1
\end{array}
\right| = 20 + 21 - 37 = 4 \\
D_y = \left|
\begin{array}{ccc}
1 & 2 & 1 \\
2 & 9 & 3 \\
1 & 10 & 1
\end{array}
\right| = -21+2+11 = -8 \\
D_z = \left|
\begin{array}{ccc}
1 & 1 & 2 \\
2 & 1 & 9 \\
1 & -3 & 10
\end{array}
\right| = 37 - 11 - 14 = 12 \\
$$
a odtiaľ $x = \frac{4}{4} = 1,\quad y = \frac{-8}{4} = -2,\quad z = \frac{12}{4} = 3$

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
takže stopa matice A je 2, a ľahko vidno, že to je súčet diagonálnych prvkov. Napriek tomu, že vyzerá triviálne, stopa je veľmi dôležitá veličina: je to *divergencia* vektorového poľa matice A, teda sila "zdroja" vektorového poľa. 

### 2. Pseudoinverzná matica a lineárna regresia

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
Používame štandardné označenie $\mathbf{F}$ pre maticu faktorov, ktorej členy závisia od hodnôt $x_i$, a maticu parametrov $\beta$.  Rovnica dáva zmysel, iba ak nadbytočné dáta sú zbytočné a hovoria to isté.  Ak hovoria niečo iné, úloha nemá riešenie. 

Sústavu možno ale ľahko "napraviť" tak, že obe strany vynásobíme zľava transponovanou maticou $\mathbf{F^T}$:
$$
\mathbf{(F^T F)\beta} = \mathbf{F^T Y}
$$
Toto je sústava 3 rovníc s 3 neznámymi, a riešenie je 
$$
\mathbf{\beta} = \mathbf{(F^T F)^{-1}F^T Y}
$$
Zatiaľ čo $\mathbf{F}$ je matica $n \times 3$ a vo všeobecnosti nebude mať inverznú maticu (pripomeňme si, že máme preurčenú sústavu - viac rovníc ako neznámych), matica $\mathbf{F^{T}F}$ je štvorcová $3 \times 3$ a okrem toho je pozitívne semidefinitná, teda pre ľubovoľný 3-vektor $\mathbf{x}$ platí $\mathbf{x^T F^T Fx} \ge 0$. Niekedy sa táto matica nazýva *Gramovou* maticou. Pozitívne definitnú maticu vieme ľahko invertovať, nulová definitnosť znamená, že matica má neúplný rank, teda faktory sú lineárne závislé a niektorý by sme mali vynechať.

Vidíme, že matica $\mathbf{(F^T F)^{-1}F^T}$ funguje ako inverzná matica $\mathbf{F}$. Nie je to inverzná matica v pravom zmysle slova, preto sa nazýva (Moorova) *pseoudoinverzná* matica. 

Pseudoinverzné matice sú veľmi významné, pretože prirodzene vznikajú v rade aplikácií, predovšetkým v lineárnej regresii. Tam chceme nájsť takú lineárnu kombináciu faktorov (resp. krivku, definovanú parametrami $a_i$), pre ktorú je súčet štvorcov odchýlok hodnôt y najmenší, teda 
$$
\mathrm{\hat{\beta}} = \textrm{argmin}\left[(\mathbf{Y}-\mathbf{F}\mathbf{\beta})^T(\mathbf{Y}-\mathbf{F}\mathbf{\beta})\right]
$$
V skutočnosti ale neformulejeme problém ako minimalizáciu skalárneho súčinu, ale ako minimalizáciu stopy:
$$
\mathrm{\hat{\beta}} = \textrm{argmin Tr}\left[(\mathbf{Y}-\mathbf{F}\mathbf{\beta})(\mathbf{Y}-\mathbf{F}\mathbf{\beta})^T\right]
$$
Stopa matice $Tr$ je súčet jej diagonálnych prvkov. Toto je všeobecnejší výraz, ktorý funguje v širšej škále prípadov (napríklad ak chceme vážiť jednotlivé dátové body), a jeho minimalizácia podľa $\mathbf{\beta}$ je určitým spôsobom ľahšia. 

Riešenie si vyžaduje zložitejšie maticové derivovanie, ale vyzerá takto:
$$
\mathbf{(F^T F)\beta} = \mathbf{F^T Y} \quad \therefore \quad \mathbf{\beta} = \mathbf{(F^T F)^{-1}F^T Y}
$$
teda vidíme, že koeficienty lineárneho regresného modelu nájdeme pomocou pseudoinverznej matice (aj keď v praxi to spravidla robíme pomocou QR rozkladu a nie explicitným vytvorením pseudoinverznej matice.)

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

Vo všeobecnosti násobenie maticou transformuje plochu v rovine tak, že ju otočí a rôzne ponaťahuje. Môžeme sa pýtať, či sa dá pôsobenie matice vyjadirť čisto ako natiahnutie v nejakých smeroch. Teda, ak mám štvorcovú maticu $\mathbf{A}$, viem nájsť bázu vektorov $\mathbf{v_i}$ takú, že v smere $\mathbf{v_i}$ pôsobí matica tak, že natiahne rovinu faktorom $\lambda_i$? Skúsme:
$$
\mathbf{Av} = \lambda\mathbf{v} \implies (\mathbf{A} - \lambda\mathbf{I})\mathbf{v = 0}
$$
Posledná rovnica znamená, že $\mathbf{v}$ leží v nulovom priestore (nullspace, resp. jadro = kernel) matice $\mathbf{A} - \lambda{I}$. To znamená, že matica $\mathbf{A} - \lambda{I}$ nemá plnú hodnosť, teda jej determinant je nulový: $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$. To je algebraická rovnica pre $\lambda$ (charakteristická rovnica):
$$
\left|
\begin{array}{cccc}
	a_{11} - \lambda & a_{12} & \dots & a_{1n} \\
	a_{21} & a_{22} - \lambda & \dots & a_{2n} \\
	\vdots & \vdots & \ddots & \vdots \\
	a_{n1} & a_{n2} & \dots & a_{nn} - \lambda
\end{array}
\right| = 0
$$
To je algebraická rovnica stupňa n v $\lambda$, a teda bude mať vo všeobecnosti n riešení. Pre každé riešenie $\lambda_{i}$ dostaneme príslušný vektor $\mathbf{v_i}$ dosadením do rovnice; príslušný chýbajúci koeficient nahradíme podmienkou, že vlastné vektory musia mať normu 1.

Čísla $\lambda_i$ nazývame vlastnými číslami matice a vektory $\mathbf{v_i}$ vlastnými vektormi. Vlastné vektory tvoria ortonormálnu bázu priestoru, v ktorom býva matica $\mathbf{A}$.

**Príklad**

Vezmime si maticu
$$
\mathbf{A}= \begin{pmatrix}
1 & 1/4 \\
1/2 & 1
\end{pmatrix}
$$
Rovnica pre vlastné hodnoty  (charakteristická rovnica) je
$$
\left|
\begin{array}{cc}
1 - \lambda & 1/4 \\
1/2 & 1 - \lambda
\end{array}
\right| = 0 \implies (1-\lambda)^2 - \frac{1}{8} = 0 \implies \lambda_{12} = 
\begin{cases}
	1 + \frac{\sqrt{2}}{4} \\
	1 - \frac{\sqrt{2}}{4} 
\end{cases}
$$
Vlastné vektory vypočítame dosadením. Pretože obe rovnice hovoria pre každý vlastný vektor to isté, používame jednu rovnicu a podmienku normalizácie:
$$
\lambda_1 = 1 + \frac{\sqrt{2}}{4}:\\
(1-\lambda_1)v_{11} + 1/4 v_{12} = 0 \\
-\sqrt{2}v_{11} + v_{12} = 0 \implies v_{12} = \sqrt{2}v_{11} \\
v_{11}^2 + v_{12}^2 = 1 \implies v_{11} = \frac{\sqrt{3}}{3},\,v_{12} = \frac{\sqrt{6}}{3} \\ \\
\lambda_2 = 1 - \frac{\sqrt{2}}{4}:\\
1/2v_{21} + (1-\lambda_2)v_{22} = 0 \\
v_{21} + \sqrt{2}v_{22} = 0 \implies v_{21} = -\sqrt{2}v_{22} \\
v_{21}^2 + v_{22}^2 = 1 \implies v_{22} = \frac{\sqrt{3}}{3},\,v_{21} = -\frac{\sqrt{6}}{3} 
$$
Zhrnieme:
$$
\lambda_1 = 1 + \frac{\sqrt{2}}{2},\quad \mathbf{v_1} = \begin{pmatrix}\frac{\sqrt{3}}{3}\\\frac{\sqrt{6}}{3}\end{pmatrix} \\
\lambda_1 = 1 - \frac{\sqrt{2}}{2},\quad \mathbf{v_2} = \begin{pmatrix}\frac{-\sqrt{6}}{3}\\\frac{\sqrt{3}}{3}\end{pmatrix}
$$
Vektory $\mathbf{v_1,v_2}$ tvoria ortonormálnu bázu, teda $\mathbf{v_1\cdot v_2}$ = 0, $|\mathbf{v_1}| = |\mathbf{v_2}| = 1$. Matica 
$$
\mathbf{V} = \begin{pmatrix}
	v_{11} & v_{21} \\
	v_{12} & v_{22}
\end{pmatrix}
$$
je teda ortogonálna - má ortogonálne normované stĺpce - a preto jej transponovaná matica je aj inverznou maticou: $\mathbf{V^T V=I}$. To znamená, že tiež platí 
$$
\mathbf{V^T A V = \Lambda} \equiv 
\begin{pmatrix}
	\lambda_1 & 0 \\
	0 & \lambda_2
\end{pmatrix}
$$
resp. (ak vynásobíme $\mathbf{V}$ zľava a $\mathbf{V^T}$ sprava)
$$
\mathbf{A} = \mathbf{V\Lambda V^T} = \sum_i \lambda_i \mathbf{v_i v_i^T}
$$
V súčinoch $\mathbf{v_i v_i^T}$ spoznávame projektory do podpriestorov vlastných vektorov, a to je reprezentácia, ktorú sme hľadali: Pôsobenie matice vyzerá tak, že sprojektuje vektor do vlastných vektorov a vynásobí príslušné komponenty vlastnými číslami.

Existuje oprávnená otázka, prečo sme pre výpočet vlastných hodnôt nepoužili ako príklad maticu z predchádzajúcej ukážky, 
$$
\mathbf{A}= \begin{pmatrix}
1 & -1 \\
1/2 & 1
\end{pmatrix}
$$
Je to preto, že táto matica nie je pozitívne definitná a preto nemá reálne vlastné hodnoty. 

**Aplikácia: Maticové funkcie**

Rozklad matice na vlastné hodnoty a vlastné vektory umožňuje robiť niektoré malé zázraky:
$$
\mathbf{A^2} = \mathbf{V\Lambda V^T V\Lambda V^T} = \mathbf{V\Lambda^2 V^T}
$$
Tu $\Lambda$ je diagonálna matica vlastných hodnôt, 
$$
\mathbf{\Lambda} = \begin{pmatrix}
	\lambda_1 & 0 & \dots & 0 \\
	0 & \lambda_2 &  \dots & 0 \\
	\vdots & \vdots & \ddots & \vdots \\
	0 & 0 & \dots & \lambda_n
\end{pmatrix}
$$
takže ľahko vidíme, že 
$$
\mathbf{\Lambda^2} = \begin{pmatrix}
	\lambda_1^2 & 0 & \dots & 0 \\
	0 & \lambda_2^2 &  \dots & 0 \\
	\vdots & \vdots & \ddots & \vdots \\
	0 & 0 & \dots & \lambda_n^2
\end{pmatrix}
$$
Analogicky máme (pre funkciu f(x), ktorú vieme rozvinúť do mocninného radu)
$$
f(\mathbf{A^2}) = \mathbf{Vf(\Lambda) V^T}
$$
kde $f(\mathbf{\Lambda})$ nie je nič iné ako
$$
f(\mathbf{\Lambda}) = \begin{pmatrix}
	f(\lambda_1) & 0 & \dots & 0 \\
	0 & f(\lambda_2) &  \dots & 0 \\
	\vdots & \vdots & \ddots & \vdots \\
	0 & 0 & \dots & f(\lambda_n)
\end{pmatrix}
$$


---

##  Domáca úloha (nová) 

1. Vypočtaj x:

![image-20240209162634979](C:\Users\kvasn\Documents\GitHub\Erik\img\circle_in_a_rect.png)

To je ľahká úloha, oveľa ťažšie je vypočítať všetko ostatné.

2. Fibonacciho čísla môžeme vyjadriť v tvare

$$
\begin{pmatrix}
	F_n \\
	F_{n-1}
\end{pmatrix} = 
\begin{pmatrix}
	1 & 1 \\
	1 & 0
\end{pmatrix}^n
\begin{pmatrix}
 1 \\ 1
\end{pmatrix}
$$

Ako sa správajú veľké Fibonacciho čísla? (Toto je príklad na vlastné hodnoty)

---

## 5. Program na budúci týždeň

- Ešte nám ostal QR rozklad, ale to už bude koniec lineárnej algebry.


$$
\bar{a}
$$

