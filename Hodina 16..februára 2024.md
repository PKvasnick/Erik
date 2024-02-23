## Hodina 23. februára 2024

**Program**

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli: všelijaké dotyčnice)
3. Domáca úloha (nová)
5. Program na budúci týždeň

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Videohovor** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

---

### 1. Domáca úloha

**Príklad 1**

Vypočtaj x:

![image-20240209162634979](C:\Users\kvasn\Documents\GitHub\Erik\img\circle_in_a_rect.png)

To je ľahká úloha, oveľa ťažšie je vypočítať všetko ostatné.

**Riešenie**

![image-20240216122155403](img\image-20240216122155403.png)

Ostatné veci sa počítajú oveľa ťažšie.

---

**Príklad**

Fibonacciho čísla môžeme vyjadriť v tvare
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

**Riešenie**

Toto sme už robili kedysi v lete. 

Označme 
$$
\mathbf{A} = 
\begin{pmatrix}
	1 & 1 \\
	1 & 0
\end{pmatrix}
$$


Rovnica pre vlastné hodnoty matice $\mathbf{A}$:
$$
\left|
\begin{array}{cc}
	1 - \lambda & 1 \\
	1 & - \lambda
\end{array}
\right|= 0 \\
-(1-\lambda)\lambda - 1 = 0 \implies \lambda^2 - \lambda - 1 = 0 \implies \lambda_{1,2}=\frac{1 \pm \sqrt{5}}{2}=
\begin{cases}
	\Phi \\
	-\frac{1}{\Phi}
\end{cases}
$$
Vlastné vektory vypočítame z definície:
$$
\begin{pmatrix}
	1 - \lambda & 1 \\
	1 & - \lambda
\end{pmatrix}
\begin{pmatrix}
	v_1 \\
	v_2
\end{pmatrix} = 0
$$
Pre jednotlivé vlastné hodnoty dostávame:
$$
\lambda = \Phi:\\
u_1 - \Phi u_2 = 0 \implies u_1 = \Phi u_2 \\
u_1^2 + u_2^2 = 1 \implies (\Phi^2+1)u_2^2 = 1 \implies u = \begin{pmatrix}
	\frac{\Phi}{\sqrt{1+\Phi^2}} \\
	\frac{1}{\sqrt{1+\Phi^2}}
\end{pmatrix}  \\ \\
\lambda = -\frac{1}{\Phi}: \\
v_1 + \frac{1}{\Phi} v_2 \implies v_1 = -\frac{1}{\Phi}v_2 \\
v_1^2 + v_2^2 = 1 \implies \left(\frac{1}{\Phi^2}+1\right)v_2^2 = 1 \implies v = \begin{pmatrix}
	\frac{-1}{\sqrt{1+\Phi^2}} \\
	\frac{\Phi}{\sqrt{1+\Phi^2}} \\
\end{pmatrix}
$$
Definujme 
$$
\mathbf{V} = (\vec{u}\quad \vec{v}) = \frac{1}{\sqrt{1+\Phi^2}}
\begin{pmatrix}
	\Phi & -1 \\
	1 & \Phi
\end{pmatrix}
$$
Matica $\mathbf{V}$ je ortogonálna, teda jej inverzná matica je $\mathbf{V}^T$.

Ďalej nech
$$
\mathbf{\Lambda} = 
\begin{pmatrix}
	\lambda_1 & 0 \\
	0 & \lambda_2
\end{pmatrix} \equiv 
\begin{pmatrix}
	\Phi & 0 \\
	0 & -\frac{1}{\Phi}
\end{pmatrix} 
$$
Platí
$$
\mathbf{AV = \Lambda V} \implies \mathbf{A = \Lambda VV^T}= \lambda_1 \mathbf{uu^T}+\lambda_2\mathbf{vv^T} \\
$$
Teraz nie je problém vyjadriť akúkoľvek mocninu matice $\mathbf{A}$, pretože vektory $\mathbf{u,v}$ sú normalizované a ortogonálne, teda $|\mathbf{u}|=|\mathbf{v}|=1, \mathbf{u^T v} = \mathbf{v^T u} = 0 $
$$
\mathbf{A^2} = (\lambda_1 \mathbf{uu^T}+\lambda_2\mathbf{vv^T})(\lambda_1 \mathbf{uu^T}+\lambda_2\mathbf{vv^T}) \\
= \lambda_1^2 \mathbf{uu^T}+\lambda_2^2\mathbf{vv^T}
$$
Platí $\lambda_1 \equiv \Phi > 1, |\lambda_2| = 1/\Phi < 1 $ a teda s rastúcim $n$ bude vo výraze pre n-tú mocninu $\mathbf{A}$ dominovať člen s $\lambda_1 \equiv \Phi$:
$$
n \rightarrow \infty:\quad \mathbf{A^n} \rightarrow \Phi^n \mathbf{uu^T}
$$
a teda veľké Fibonacciho čísla sa budú chovať ako $\Phi^n$. Tento výraz je pozoruhodne presný. 

​			

---



## Niekoľko príkladov na zahriatie a povznesenie mysle

### 1. Všelijaké dotyčnice

Aká je rovnica dotyčnice k funkcii $f: y=x^2$ v bode $[2,4]$

### 2. Stopa

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



Riešenie si vyžaduje zložitejšie maticové derivovanie, ale vyzerá takto:
$$
\mathbf{(F^T F)\beta} = \mathbf{F^T Y} \quad \therefore \quad \mathbf{\beta} = \mathbf{(F^T F)^{-1}F^T Y}
$$
teda vidíme, že koeficienty lineárneho regresného modelu nájdeme pomocou pseudoinverznej matice (aj keď v praxi to spravidla robíme pomocou QR rozkladu a nie explicitným vytvorením pseudoinverznej matice.)

---

##  Domáca úloha (nová) 

1. Už sme mali takúto maticcu:

$$
\mathbf{T}= 
\begin{pmatrix}
	3 & 2 \\
	2 & 1
\end{pmatrix}
$$

​	Aké sú vlastné čísla a vlastné vektory tejto matice?

2. Aby sme nazabudli, čo sme kedysi robili: Dokážte, že pre žiadne celé n nie je číslo n(n+1)(n+2)(n+3) úplný štvorec. 

   *Návod*: treba ukázať, že číslo sa nachádza medzi dvoma nasledujúcimi úplnými štvorcami, teda existuje m také, že $m^2 < n(n+1)(n+2)(n+3) < (m+1)^2$. Natrénovať pre jednoduchšiu úlohu: dokázať, že n(n+1) nie je nikdy úplný štvorec.

3. Na lúke stojí Adam a Barbora. Inde na lúke je kruhové jazero. Adam chce doniesť Barbore vodu z jazera. Aká je najkratšia trasa Adam - jazero - Barbora? (stačí geometrická úvaha, počítať budeme nabudúce).

---

## 5. Program na budúci týždeň

- Ešte trocha derivácií a trocha integrálov. 


$$
\bar{a}
$$

