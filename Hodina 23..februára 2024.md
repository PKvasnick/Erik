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

Už sme mali takúto maticu:
$$
\mathbf{T}= 
\begin{pmatrix}
	3 & 2 \\
	2 & 1
\end{pmatrix}
$$
Aké sú vlastné čísla a vlastné vektory tejto matice?

**Riešenie**

Rovnica pre vlastné hodnoty je
$$
\left|
\begin{array}{cc}
	3 - \lambda & 2 \\
	2 & 1 - \lambda
\end{array}
\right|= 0 \\
(3-\lambda)(1-\lambda) - 4 = 0 \implies \lambda^2  - 4\lambda - 1 = 0 \implies \lambda_{1,2}=\frac{4 \pm \sqrt{20}}{2}=
\begin{cases}
	2\Phi \\
	-\frac{2}{\Phi}
\end{cases}
$$
Vlastné vektory vypočítame z definície:
$$
\begin{pmatrix}
	3 - \lambda & 2 \\
	2 & 1 - \lambda
\end{pmatrix}
\begin{pmatrix}
	v_1 \\
	v_2
\end{pmatrix} = 0
$$
Pre jednotlivé vlastné hodnoty dostávame:
$$
\lambda = 2\Phi:\\
2u_1 - 2\Phi u_2 = 0 \implies u_1 = \Phi u_2 \\
u_1^2 + u_2^2 = 1 \implies (\Phi^2+1)u_2^2 = 1 \implies u = \begin{pmatrix}
	\frac{\Phi}{\sqrt{1+\Phi^2}} \\
	\frac{1}{\sqrt{1+\Phi^2}}
\end{pmatrix}  \\ \\
\lambda = -\frac{2}{\Phi}: \\
2v_1 + \frac{2}{\Phi} v_2 \implies v_1 = -\frac{1}{\Phi}v_2 \\
v_1^2 + v_2^2 = 1 \implies \left(\frac{1}{\Phi^2}+1\right)v_2^2 = 1 \implies v = \begin{pmatrix}
	\frac{-1}{\sqrt{1+\Phi^2}} \\
	\frac{\Phi}{\sqrt{1+\Phi^2}} \\
\end{pmatrix}
$$


---

**Príklad**

Aby sme nezabudli, čo sme kedysi robili: Dokážte, že pre žiadne celé n nie je číslo n(n+1)(n+2)(n+3) úplný štvorec. 

*Návod*: treba ukázať, že číslo sa nachádza medzi dvoma nasledujúcimi úplnými štvorcami, teda existuje m také, že $m^2 < n(n+1)(n+2)(n+3) < (m+1)^2$. Natrénovať pre jednoduchšiu úlohu: dokázať, že n(n+1) nie je nikdy úplný štvorec.

**Riešenie**

Začnime jednoduchším tvrdením, totiž, že pre prirodzené $n$ nie je $n(n+1)$ nikdy úplný štvorec.

Skutočne, pre $n>0$ platia ostré nerovnosti
$$
n^2 < n(n+1) < (n+1)^2
$$
a pretože medzi $n^2$ a $(n+1)^2$ nie je žiadny úplný štvorec, číslo $n(n+1)$ nemôže byť úplným štvorcom.

Poďme teraz na samotnú úlohu: ideme dokázať, že pre prirodzené $n$ nie je číslo $n(n+1)(n+2)(n+3)$ úplným štvorcom.

Upravme
$$
n(n+1)(n+2)(n+3) = (n^2 + n)(n^2 + 5n + 6) = n^4 + 6n^3 + 11n + 6n
$$
Tento polynóm potrebujeme uzavrieť medzi dva nasledujúce úplné štvorce $(n^2 + an + b)^2$  a $(n^2 + an + b + 1)^2$. Porovnaním dostaneme
$$
(n^2+an+b)^2 = n^4 + 2an^3 + (2b + a^2)n^2 + 2abn + b^2 \\
2a = 6 \implies a = 3 \\
2b + a^2 = 2b + 9 = 11 \implies b=1
$$
a teda najbližší úplný štvorec je
$$
M(n) = (n^2 + 3n + 1)^2 = n^4 + 6n^3 + 11n^2 + 6n + 1
$$
Tento štvorec je väčší ako $n(n+1)(n+2)(n+3)$. Najbližší menší štvorec je 
$$
m(n) = (n^2 + 3n)^2 = n^4 + 6n^3 + 9n^2
$$
a je očividne menší než $n(n+1)(n+2)(n+3)$. Zhrnieme: pre $n>0$ je 
$$
(n^2 + 3n)^2 < n(n+1)(n+2)(n+3) < (n^2 + 3n + 1)^2
$$
a pretože máme naľavo a napravo dva nasledujúce úplné štvorce, nemôže byť $n(n+1)(n+2)(n+3)$ úplným štvorcom.

---

**Príklad**

Na lúke stojí Adam a Barbora. Inde na lúke je kruhové jazero. Adam chce doniesť Barbore vodu z jazera. Aká je najkratšia trasa Adam - jazero - Barbora? (stačí geometrická úvaha, počítať budeme nabudúce).

**Riešenie**

Pre jednoduchosť budeme analyzovať najjednoduchší prípad, kedy spojnica A, B je celá na súši. 

V matematičtine hľadáme bod T na kružnici (brehu jazera), pre ktorý je súčet vzdialeností $|AT|+|BT|$ minimálny. 

Táto úloha má jednoduché riešenie: Bod T je bod dotyku najmenšej elipsy s ohniskami A, B, dotýkajúcej sa kruhu - jazera. 

<img src="img\beh_pre_vodu_setup.png" style="zoom:19%;" />

---

Intuitívne je jasné, prečo to je tak. 

Všimnime si, že takýto pohľad na vec mení minimalizačný problém na problém hľadania konkrétnej elipsy. To môžeme urobiť analyticky, ale môžeme si tiež zvoliť rôzne spôsoby, ako sformulovať rovnicu, ktorú chceme riešiť. 

Už starovekí Gréci vedeli, že v eliptickej miestnosti zvuk vychádzajúci z jedného ohniska sa sústreďuje v druhom. 

<img src="img\echo_chamber.png" alt="Elli-norm-tang-n.svg" style="zoom:25%;" />

Preto bod dotyku T môžeme nájsť ako bod na kružnici, v ktorom dotyčnica ku kruhu zviera s priamkami AT a BT rovnaký uhol. 

<img src="C:\Users\kvasn\Documents\GitHub\Erik\img\beh_pre_vodu_riesenie.png" style="zoom:19%;" />

To je dobrý spôsob, ako formulovať úlohu analyticky. Priamočiare riiešenie je hľadať bod T tak, že leží na elipse s ohniskami A, B, ktorá sa dotýka kruhu. Teda ak označíme E(x,y|a) body ležiace na elipse a K(x, y) body, ležiace na kružnici, hľadáme bod T a parameter $a$ tak, že $E(x,y|a) = K(x,y)$ a okrem toho musia mať elipsa i kružnica v bode T rovnakú dotyčnicu. V termínoch uhlov dostaneme omnoho jednoduchší vzťah.

## Niekoľko príkladov na zahriatie a povznesenie mysle

### 1. Všelijaké dotyčnice

Čo dotyčnice kružnice a elipsy? Podrobnejšie: Čo keď mám funkciu $f(x,y)=0$. Ako vypočítam dotyčnicu ku krivke?

<img src="img\Ellipse-def0.svg.png" alt="Ellipse-def0.svg" style="zoom:19%;" />

### 2. Derivácie

Posledne sme prišli na to, že smernica dotyčnice ku krivke y = f(x) je 
$$
y^{\prime} = \lim_{h \rightarrow 0} \frac{f(x+h) - f(x)}{h}
$$
Limity sme už mali, takže je jasné, čo tento zápis znamená?
$$
\forall \epsilon > 0\quad \exist \delta(\epsilon) > 0 : 0 < h < \epsilon \implies \left| \frac{f(x+h) - f(x)}{h} - y^{\prime} \right| < \epsilon
$$
A čo derivácie iných funkcií?



---

##  Domáca úloha (nová) 

1. Ktorý obdĺžnik má pri konštantnom obsahu najmenší obvod? 
2. Aký najväčší obdĺžnik (v zmysle plochy) vieme vpísať do polkruhu?
3. Aký najväčší kužeľ môžeme vpísať do gule? (v zmysle podielu obsahu kužeľa a gule)
4. Adam a Barbora 2: Adam s Barborou sa prechádzajú po cestičke pri pláži.  Cestička vedie rovnobežne s brehom mora vo vzdialenosti 50 m. Zrazu vietor zhodí Barbore klobúk a odnesie ho presne do bodu K 200 m nižšie na rozhraní pláže a mora. Adam ho chce zachrániť, kým ho spláchne vlna . Po cestičke beží rýchlosťou 8 km/h, ale v piesku len rýchlosťou 3 km/h. Ako dlho má Adam bežať po cestičke, kým vbehne do piesku, aby sa ku klobúku dostal čo najrýchlejšie?

---

## 5. Program na budúci týždeň

- Ešte trocha derivácií a trocha integrálov. 


$$
\bar{a}
$$

