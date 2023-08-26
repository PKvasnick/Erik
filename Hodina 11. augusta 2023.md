## Hodina 11. augusta 2023

Program:

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli.
3. Geometria. Pytagorova veta.
4. Domáca úloha (nová)

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Videohovor** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

### 1. Domáca úloha

**Príklad 1** 

Nájdite všetky reálne riešenia rovnice
$$
(x^2 - 10x - 12)^{x^2 + 5x + 2}=1
$$

​	Návod: Metodicky preskúmať, pre aké $a, b$ je $a^b=1$.

**Riešenie**

Začneme skúmaním, pre aké  $a, b$ je $a^b=1$. Platí to v troch prípadoch:

- $a$ = 1, b je ľubovoľné
- $b=0$, $a$ je ľubovoľné
- $a=-1$, $b$ je celé párne.

*__1. prípad: $a=1$, ľubovoľné $b$__*

Riešenia v tomto prípade budú korene rovnice 
$$
x^2 - 10x - 12 = 1
$$
teda  
$$
x_{1,2} = \frac{10 \pm \sqrt{148}}{2} = 5 \pm \sqrt{37}
$$
Pre tieto hodnoty je exponent $x^2+5x+2$ rovný
$$
x^2 + 5x + 2 = \underbrace{x^2 - 10x - 13}_0 + 15x + 15 = 90 \pm 15\sqrt{37}
$$
a výraz na ľavej strane rovnice je dobre definovaný.

*__2. prípad: $b=0$, $a$ ľubovoľné__* 

Korene exponenta sú 
$$
x^2 + 5x + 2 = 0 \\
x_{3,4} = \frac{-5 \pm \sqrt{17}}{2}
$$
V týchto hodnotách má základ hodnoty
$$
x^2 - 10x - 12 = \underbrace{x^2 + 5x + 2}_{0} - 15x -14 = -15\frac{-5 \pm \sqrt{17}}{2} - 14 \\
= \frac{61 \mp 15\sqrt{17}}{2}
$$
Tieto hodnoty základu sú v poriadku a máme ďalšie dve platné riešenia. 

*__3. prípad: $a=-1$, $b=2k$__*

Základ je $-1$ pre hodnoty
$$
x^2 - 10x - 12 = -1
$$
teda $x_5=-1, x_6=11$,  a pre tieto hodnoty je exponent rovný
$$
x^2 +5x +2 = \underbrace{x^2 - 10x - 11}_0 + 15x + 13 = 15(5\pm 6) + 13 = 88\pm 6
$$
a obe tieto hodnoty sú párne, takže $x_5, x_6$ sú riešeniami rovnice. 

*__Záver:__* Našli sme 6 riešení rovnice. 

---

**Príklad 2**

Dokážte, že pre prirodzené $n$ platí
$$
n + \frac{1}{n + \frac{1}{n+ \frac{1}{n + \dots}}} = \frac{n + \sqrt{n^2 + 4}}{2}
$$

Poznámka. Pre n=1 dostávame zlatý rez, pre ostatné n sa tieto čísla nazývajú "metalické čísla".

**Riešenie**

Aby sme dali nekonečnému reťazovému zlomku presný zmysel, vyjadríme ho  ako limitu postupnosti:
$$
A_{k+1}^{(n)} = n + \frac{1}{A_k^{(n)}}
$$
a stanovíme počiatočné podmienky:
$$
A_0^{(n)} = n \implies A_1^{(n)} = n + \frac{1}{n},\,A_2^{(n)} = n + \frac{1}{n + \frac{1}{n}}, \,\dots
$$
Mohli by sme položiť tiež $A_0=1$ a dostali by sme mierne odlišnú postupnosť 
$$
A_0^{(n)} = 1 \implies A_1^{(n)} = n + 1,\,A_2^{(n)} = n + \frac{1}{n + 1}, \,\dots
$$
Limita postupnosti spĺňa rovnicu 
$$
A^{(n)} = n + \frac{1}{A^{(n)}} \\
\left(A^{(n)}\right)^2 - nA^{(n)} - 1 = 0 \\
A_{1,2}^{(n)} = \frac{n \pm \sqrt{n^2 + 4}}{2}
$$
Z definície postupnosti jednoznačne vyplýva $A^{(n)} \ge 1 > 0$, takže prípustné je iba kladné riešenie
$$
A^{(n)} = \frac{n + \sqrt{n^2 + 4}}{2}
$$
a tento výraz je dobre definovaný pre každé prirodzené n. Tým je tvrdenie dokázané. 

---

**Príklad 3**

Pomocou princípu dobrého usporiadania dokážte, že rovnica 
$$
4a^3 + 2b^3 = c^3
$$

nemá riešenie v množine prirodzených čísel. 

**Riešenie**

Vyriešme niekoľko okrajových prípadov, aby sme mali poriadok pre malé čísla $a, b, c$. 

| $4a^3 + 2b^3$ | b    | 0    | 1    | 2    |
| ------------- | ---- | ---- | ---- | ---- |
| **a**         |      |      |      |      |
| 0             |      | 0    | 2    | 16   |
| 1             |      | 4    | 6    | 20   |
| 2             |      | 32   | 34   | 48   |

Ani jedno číslo v tabuľke nie je treťou mocninou, takže bezpečne vieme, že tvrdenie neplatí pre $a, b \le 2, \, c \le \sqrt{48} < 4$. Pre ostatné $a, b,c$ dokážeme tvrdenie sporom s použitím princípu dobrého usporiadania. Označme C množinu hodnôt $c$, pre ktoré existuje nejaká dvojica prirodzených čísel $a, b$ tak, že $a, b, c$ je riešením rovnice. Pre dôkaz sporom predpokladáme, že množina C je neprázdna a teda podľa princípu dobrého usporiadania má minimálny prvok $c_0$. Podľa predpokladu existujú čísla $a_0, b_0$ tak, že $4a_0^3+2b_0^3 = c_0^3$. Pretože ľavá strana rovnice je párna, musí byť párne $c_0^3$ a teda aj samotné $c_0$, $c_0 = 2c_1$, pričom $c_1$ je nejaké prirodzené číslo. Z prípravy vieme, že $c_0>3$, a teda $c_1 \ge 2$. Dosadíme:
$$
4a_0^3 + 2b_0^3 = (2c_1)^3 = 8c_1^3 \implies 2a_0^3 + b_0^3 = 4c_1^3
$$
a teda musí aj $b_0$ musí byť párne, $b_0=2b_1$. Aj tu vieme, že $b_0>2$ a teda $b_1 \ge 2$. Opäť dosadíme:
$$
2a_0^3 + (2b_1)^3 = 4c_1^3 \implies a_0^3 + 4b_1^3 = 2c_1^3
$$
a teda aj $a_0$ musí byť párne, $a_0 = 2a_1$. Opäť vieme, že $a_0>2$ a teda $a_1\ge2$. Dosadíme
$$
(2a_1)^3 + 4b_1^3 = 2c_1^3 \implies 4a_1^3 + 2b_1^3 = c_1^3
$$
a teda trojica $(a_1, b_1, c_1)$ je riešením rovnice a $c_1$ podľa práva patrí do C. Lenže spoľahlivo vieme, že $c_0 >c_1>0$, pretože obe čísla sú zaručene väčšie ako 0, a teda minimálnym prvkom C nie je $c_0$, ale $c_1$. To je rozpor s predpokladom, že množina C má minimálny prvok: pre každý minimálny prvok vieme zostrojiť menší prvok, ktorý takisto patrí do C. Lenže minimálny prvok množiny C musí byť $>\sqrt[3]{48}$, a teda dostávame rozpor: množina C nemôže mať minimálny prvok. Jediný prípad, kedy tento rozpor nenastane je, keď je množina C prázdna a teda keď platí dokazované tvrdenie: rovnica nemá riešenie v množine prirodzených čísel. 

---

**Príklad 4**

Pomocou princípu dobrého usporiadania ukážte, že každé celé číslo rovné alebo väčšie ako 8 možno vyjadriť ako súčet celočíselných násobkov 3 a 5. 

**Riešenie**

Skúmajme, ako toto môže fungovať:

Vezmime prirodzené číslo $m$, a nech $m = 5p + r$. $p$ je prirodzené číslo alebo 0, $r = 0, 1, 2, 3, 4$.  Rozdeľme dôkaz podľa hodnôt $r$ a zo začiatku nebudeme príliš riešiť okrajové prípady:

Pre $r = 0$ tvrdenie platí. 

Pre $r = 1$ je $m = 5(p-1)  + 5 + 1 = 5(p-1) + 2\cdot 3$ a teda tvrdenie opäť platí.

Pre $r = 2$ je $m = 5(p-2) + 10 + 2 = 5(p-2) + 4\cdot 3$ a opäť vidíme, že tvrdenie platí.

Pre $r = 3$ tvrdenie platí triviálne.

Pre $r = 4$  je $m = 5(p-1)  + 5 + 4 = 5(p-1) + 3\cdot 3$ a aj v tomto prípade tvrdenie platí.

Teraz tiež vidíme, prečo tvrdenie platí až pre $m\ge 8$:  V niektorých prípadoch si potrebujeme "vypožičať " jednu alebo dve päťky, ale ak je $n$ malé, nie je z čoho. 7=5+2, takže by sme potrebovali požičať dve päťky, ale máme iba jednu. 8=5+3, takže tvrdenie platí triviálne, pre 9 máme zvyšok 4, takže si vypožičiavame jedinú päťku, a pre 10 opäť tvrdenie platí triviálne. Pre vyššie čísla si už potom môžeme podľa potreby bezpečne vypožičať jednu i dve päťky. 

S rovnakým výsledkom sme mohli namiesto zvyškov po delení 5 analyzovať zvyšky po delení 3.  Aby takéto "požičiavanie" fungovalo, je treba, aby obe čísla $p, q$ (v našom prípade 3 a 5) boli vzájomne nesúdeliteľné ("coprime"), teda ich najväčší spoločný deliteľ sa musí rovnať 1. To,  čo robíme je, že pre daný zvyšok $r$ hľadáme celé čísla $a, b$ tak, aby $ap + bq = r$, kde $gcd(p,q) = 1$. Takúto úlohu vieme výrazne zjednodušiť tak, že nájdeme riešenie rovnice $a_1p + b_1q = 1$, a riešenia rovnice s pravou stranou $r$ sú potom jednoducho $a = ra_1, b=rb_1$. Pre čísla 3, 5 riešime rovnicu $3a_1 + 5b_1 = 1$, a riešenie vidíme ľahko $a_1 = 2, b_1 = -1$. Keď máme jedno riešenie, vieme skonštruovať celú rodinu riešení $(a_1+5k, b_1 - 3k)$ kde k je celé číslo. Skutočne, 
$$
3(a_1 + 5k) + 5(b_1 - 3k) = 3a_1 + 15k + 5b_1 - 15k = 3a_1 + 5b_1
$$
a riešenia pre jednotlivé zvyšky napríklad po delení 5 budú:

- $r=0$: triviálne

- $r = 1$: $a=a_1=2, b=b_1=-1$
- $r = 2$: $a=2a_1=4, b=2b_1=-2$
- $r=3$ triviálne
- $r=4$: $a=4a_1-5=3, b=4b_1+3=-1 $

Teraz tvrdenie dokážeme sporom a využijeme princíp dobrého usporiadania. Ešte predtým ukážeme, že tvrdenie platí pre niekoľko hodnôt $m \ge 8$: 

| 8     | 9    | 10   | 11      | 12   | 13      | 14      | 15   | 16        |
| ----- | ---- | ---- | ------- | ---- | ------- | ------- | ---- | --------- |
| 5 + 3 | 3⨯3  | 2⨯5  | 5 + 2⨯3 | 4⨯3  | 2⨯5 + 3 | 5 + 3⨯3 | 3⨯5  | 2⨯5 + 2⨯3 |

Označme C množinu prirodzených čísel $m$, ktoré nemožno vyjadriť ako súčet násobkov 3 a 5.  Pre dôkaz sporom budeme predpokladať, že množina C je neprázdna. Podľa princípu dobrého usporiadania musí mať množina c najmenší prvok $c$. Zjavne $c>16$.  Uvažujme číslo $c-5$, ktoré je určite menšie ako $c$ a väčšie ako 8.  Toto číslo tiež nie je vyjadriteľné ako súčet násobkov 3 a 5 a patrí do množiny C. V opačnom prípade, ak by existovali dve celé čísla $a,b$ také, že $c-5 = 3a + 5b$, bolo by $c=3a + 5(b+1)$ a teda aj $c$ by bolo vyjadriteľné ako súčet násobkov 3 a 5. Čo sme dosiahli: pre minimálny prvok množiny C vieme zostrojiť menší prvok, ktorý tiež patrí do C, aj keď množina prirodzených čísel, ktoré potenciálne môžu patriť do C, je zdola ohraničená. Jediný prípad, kedy toto nevedie k logickému rozporu je, keď je množina C prázdna a teda platí pôvodné tvrdenie. 

---

## 2. Príklady na zahriatie

**Iný dôkaz AGM**

Minulý týždeň sme dokazovali, že pre všetky kladné čísla $a, b$ platí 
$$
\frac{a+b}{2}\ge \sqrt{ab}
$$
(nerovnosť AGM). 

Ukážem ešte jeden priamy dôkaz. Aj keď je myšlienkovo veľmi pdobný tomu, ktorý sme robili, ukazuje iný postup ako urobiť takýto dôkaz: vziať jednu stranu a dopracovať sa ku kompletnému tvrdeniu. 
$$
\sqrt{ab} = \frac{\sqrt{4ab}}{2} \le \frac{\sqrt{4ab + (a-b)^2}}{2} = \frac{\sqrt{4ab + a^2 - 2ab + b^2}}{2} = \frac{\sqrt{(a+b)^2}}{2}=\frac{a+b}{2}
$$
V odvodení máme jedinú nerovnosť - v 2. kroku - keď sme pridali pod odmocninu člen, ktorý je určite väčší alebo rovný nule, pričom rovnosť nastáva iba v prípade $a=b$.  Odmocninu sme mohli legálne odstrániť, pretože $a, b \ge 0$.

**Príklad**

Máme ešte jednu podobnú nerovnosť, a to medzi geometrickým a harmonickým priemerom:
$$
\sqrt{ab} \ge \frac{2}{\frac{1}{a}+\frac{1}{b}}, \quad a,b > 0
$$
Ako toto dokázať?

**Riešenie**

Keď upraceme všetky členy na ľavú stranu nerovnosti (dávame pozor, či náhodou nenásobíme záporným číslom alebo nebodaj nulou - nie, nenásobíme), dostaneme
$$
\frac{1}{a} - 2\frac{1}{\sqrt{a}}\frac{1}{\sqrt{b}} + \frac{1}{b} = \left(\frac{1}{\sqrt{a}}-\frac{1}{\sqrt{b}}\right)^2 \ge 0
$$
a rovnosť zjavne nastáva pre $a=b$. Táto nerovnosť sa teda dokazuje rovnako, ako AGM nerovnosť. 

---

**Príklad** 

Ukážeme si jedno využitie AGM nerovnosti: 

Nájdite minimálnu hodnotu výrazu 
$$
\frac{9x^2\sin^2{x}+4}{x \sin{x}}, \quad x \in \{0, \pi\}
$$
**Riešenie**

Keď vo výraze oamostatníme jednotlivé členy, 
$$
9x\sin{x}+\frac{4}{x \sin{x}}
$$
vidíme, že súčin členov je konštanta. Podľa AGM nerovnosti platí
$$
9x\sin{x}+\frac{4}{x \sin{x}} \ge 2\sqrt{9\cdot 4} = 12
$$
Minimálna hodnota výrazu je teda 12, a túto hodnotu výraz dosiahne práve vtedy, keď sú si oba členy rovné, teda
$$
9x^2\sin^2{x} = 4 \\
x\sin{x} = \sqrt{\frac{4}{9}} = \frac{2}{3}
$$
a uvažujeme iba nezáporné riešenie, pretože funkcia $x\sin{x}$ je na intervale $(0, \pi)$ nezáporná (nezáporný je sínus aj x).

<img src="img\xsinx.png" alt="xsinx" style="zoom:67%;" />

Riešenia rovnice $x\sin{x} = c$ musíme nájsť numericky (napríklad pomocou algoritmov z minulého týždňa), ale úloha vlastne predpisuje iba nájdenie minimálnej hodnoty - o nej sme zistili, že sa rovná 12. 

Odkiaľ vieme, že toto je správne minimum? Podstatné je, že geometrický priemer je konštantný, a teda nám dáva dolnú hranicu pre hodnoty funkcie na *_celom_* intervale $\langle 0, \pi\rangle$. 

Úlohu o nájdení minima funkcie štandardne riešime hľadaním bodov, kde sa derivácia funkcie rovná 0 (stacionárnych bodov). Niektoré z nich môžu byť minimá a iné maximá. Pre funkciu v tomto prípade by to najskôr išlo spraviť, ale výraz pre deriváciu by bol dosť nepríjemný. Aj keď AGM je viac-menej náhodná finta, ako úlohu vyriešiť lacno, vyskytuje sa takýto postup prekvapivo často. 

<img src="img\x2sinx2.png" alt="x2sinx2" style="zoom:67%;" /> 

---

**Príklad** - Mini-tetris

Vyhrávajúcou konfiguráciou v mini-tetrise je úplné pokrytie hracej plochy o rozmere $2\times n$ kombináciou troch dlaždíc:

![image-20230808160936874](img\mini-tetris1.png)

Toto sú tri platné konfigurácie pre hraciu plochu $2\times 5$:

![image-20230808161251170](img\mini-tetris2.png)

Označme $T_n$ počet vyhrávajúcich konfigurácií pre hraciu dosku o rozmeroch $2\times n$. Vypočítajte $T_n$ pre prirodzené $n\ge 1$.

**Riešenie**

Toto je typická úloha na riešenie rekurzívnych schém. Budeme postupovať v troch krokoch:

1. Vypočítame $T_n$ pre malé $n=1, 2, 3$.
2. Vyjadríme $T_n$ cez $T_{n-1}$ a $T_{n-2}$.
3. Vyriešime rekurziu, teda vyjadríme $T_n$ iba v termínoch $n$.

**1. krok**: Pre malé $n$ môžeme riešenia ľahko vymenovať:

<img src="img\MiniTetris.drawio.png" alt="MiniTetris.drawio" style="zoom:80%;" />

**2. krok**: Riešenie pre $k=n$ môžme získať buď z riešenia pre $k=n-1$ pridaním ležatého obdĺžnika, alebo z riešenia pre $k=n-2$ pridaním buď veľkého štvorca alebo dvojice zvislých obdĺžnikov:

<img src="img\MiniTetris2.drawio.png" alt="MiniTetris2.drawio" style="zoom:90%;" />

Z ilustrácie vidno, prečo potrebujeme rekurziu s hĺbkou 2 (teda počet riešení pre dané $n$ vyjadrujeme pomocou riešení pre $n-1$ a $n-2$).  Teraz už ľahko odvodíme rekurentný vzťah pre $T_n$:
$$
T_m = T_{n-1} + 2T_{n-2}, \quad T_1 = 1,\quad T_2 = 3
$$
Z ilustrácie vidno, prečo potrebujeme rekurziu s hĺbkou 2 (teda počet riešení pre dané n vyjadrujeme pomocou riešení pre n-1 a n-2). Vidíme, že tento vzťah funguje pre $n=3$ a nie je ťažké (iba otravné) ho overiť pre $n=4$.

**3. krok**: Máme lineárnu rekurziu s konštantnými koeficientmi (teda koeficienty pri $T_k$ sú konštanty).  Štandardný spôsob riešenia pre takéto rovnice je hľadať riešenia v tvare $T_n = q^n$. Dosadením získame
$$
q^n = q^{n-1} + 2q^{n-2}
$$
Odtiaľ ľahko získame kvadratickú rovnicu pre q:
$$
q^2 - q - 2 = 0 \implies q_{1,2} = \frac{1 \pm 3}{2} = 
\begin{cases} 
	+2 \\
	-1
\end{cases}
$$
Pretože máme lineárnu rovnicu, všeobecné riešenie bude mať tvar $T_n = C_12^n + C_2(-1)^n$, pričom konštanty $C_1, C_2$ určíme z počiatočných podmienok:
$$
n=1 \quad 2C_1 + (-1)C_2 = 1 \quad 2C_1 - C_2 = 1\\
n=2 \quad 4C_1 + (-1)^2C_2 = 3 \quad 4C_1 + C_2 = 3
$$
a ak sčítame obe rovnice, dostaneme $C_1 = 2/3$, a potom napríklad z prvej rovnice $C_2 = 1/3$. Nakoniec teda máme pre $T_n$ nalsedujúce vyjadrenie:
$$
T_n = \frac{2^{n+1} + (-1)^n}{3}
$$
Ľahko overíme, že tento vzťah funguje pre $n=1, 2, 3$ a tiež spĺňa rekurentný vzťah pre $T_n$.

---

## 3. Geometria

Geometria je veľmi široká oblasť, takže budeme skákať z jednej veci na druhú. Začneme vecou, ktorá je starobylá a notoricky známa, ale nedávno vzbudila dosť široký rozruch:

#### Pravouhlé trojuholníky a Pytagorova veta

Pre pravouhlý trojuholník s odvesnami a, b a preponou c platí $a^2 + b^2 = c^2$.

<img src="img\trojuholnik.png" alt="trojuholnik" style="zoom:50%;" />

Existujú stovky dôkazov Pytagorovej vety, my si pár preberieme, aby sme sa čo-to naučili o pravouhlých trojuholníkoch a iných veciach. Veľa dôkazov sa nájde napríklad na stránke `cut-the-knot.org`. 

**Dôkaz 1**

Toto je pôvodný Euklidov dôkaz, plus mínus malé úpravy. 

<img src="img\EuclidI47a.gif" alt="EuclidI47a" style="zoom:120%;" />

1. krok: △AEC = △ABF podľa princípu "sus": AE = AB, pretože obe sú strany štvorca ABDE; AC=AF, pretože obe sú strany štvorca ACGF, ∠EAC = ∠BAF, pretože oba sú (pravý uhol) + ∠BAC.
2. Plocha △ABF = |AF|$v_{AF}$/2 = $b^2/2$. Plocha △AEC= |AE|$v_{AE}$/2 = $c|AM|/2$. Inak povedané, plocha štvorca ACGF $(=b^2)$ je rovnaká ako plocha obdĺžnika AMLE. 
3. Úplne rovnako môžeme ukázať, že plocha štvorca BKHC $=a^2$ je rovnaká ako plocha obdĺžnika BMLD. 
4. Spojením dostaneme Pytagorovu vetu:

$$
c^2 = |▢ABDE| = |▭AMLE|+|▭BMLD| = a^2 + b^2
$$

Geometrická schéma ako na obrázku môže pôsobiť odstrašujúco. To, čo si treba predstaviť je, že 

- vrchol B trojuholníka ABF môže kĺzať po úsečke BC až k vrcholu C, pričom obsah trojuholníka ostáva rovnaký - teda polovica obsahu štvorca ACGF. 
- Podobne vrchol C trojuholníka ACE môže kĺzať po úsečke CM až k bodu M, pri zachovaní plochy trojuholníka, ktorá teda bude rovná polovici plochy obdĺžnika AMLE. Teda štvorec nad stranou $b=AC$ má rovnakú plochu ako obdĺžnik AMLE.
- Rovnako sa dá ukázať, že štvorec nad stranou $a=BC$ má rovnakú plochu ako obdĺžnik BMLD.

**Dôkaz 2**

<img src="C:\Users\kvasn\Documents\GitHub\Erik\img\trojúhelník2.png" alt="trojúhelník2" style="zoom:50%;" />

Pri tomto dôkaze potrebujeme okrem samotného pravouhlého trojuholníka ABC jediný ďalší konštrukt - výšku na stranu c, $v_c = AD$. Výška delí △ABC na dva podobné trojuholníky DBA a DAC - podobnosť je poďla pravidla "uu" - každý z trojuholníkov je pravouhlý, pretože má pravý uhol pri päte výšky D, a ďalší uhol zdieľa s △ABC. 

Z podobnosti trojuholníkov vyplýva 
$$
\frac{v_c}{a} = \frac{b}{c}, \quad \frac{v_c}{b} = \frac{a}{c} \implies v_c = \frac{ab}{c} \\
\frac{v_c}{a} = \frac{|AD|}{b} \quad \frac{v_c}{b} = \frac{|BD|}{a} \implies 
|AD| + |BD| \equiv c \\
= v_c\left(\frac{b}{a} + \frac{a}{b}\right) = \frac{ab}{c}\left(\frac{b}{a} + \frac{a}{b}\right) = \frac{a^2+b^2}{c}
$$
Z tejto schémy môžeme dostať ešte jeden známy vzťah, takzvanú *_inverznú Pytagorovu vetu_*:
$$
v_c = \frac{ab}{c} \implies \frac{1}{v_c^2} = \frac{c^2}{a^2b^2} = \frac{a^2+b^2}{a^2b^2} \implies \frac{1}{v_c^2}= \frac{1}{a^2} + \frac{1}{b^2}
$$
K Pytagorovej vete sa vrátime ešte nabudúce, aby sme si trocha šliapli do gonimetrických funkcií a vektorovej algebry. 

---

## 4. Domáca úloha (nová)

1. Pomocou princípu dobrého usporiadania dokážte, že pre všetky nezáporné celé čísla $n$ platí

$$
0^3 + 1^3 + 2^3 + \dots + n^3 = \left( \frac{n(n+1)}{2}\right)^2
$$

2. Iná verzia mini-tetrisu: Máme stále hraciu dosku o rozmeroch $2\times n$, a tentoraz máme  5 dielikov::

​		![image-20230808173304124](img\mini-tetris3.png)

​		Teda napríklad pre hraciu plochu $2\times 1$ máme dve riešenia:

​		<img src="img\mini-tetris4.png" alt="image-20230808173603186" style="zoom:75%;" />

​		a pre hraciu plochu $2\times 2$ sú platnými riešeniami napríklad tieto:

​		![image-20230808173900907](img\mini-tetris5.png)

​		Vypočítajte počet riešení $T_n$ pre hraciu plochu $2\times n,\,n=1, 2, \dots$. 

3. Napíšte kus kódu v Pythone, ktorý vygeneruje všetky riešenia mini-tetrisu (vo verzii, ktorú si vyberiete) pre zadané $n$. 

4. Ptolemaiova veta je silnejšie tvrdenie ako Pytagorova veta: Pre štvoruholník ABCD vpísaný v kružnici platí


​		![Ptolemy_equality.svg](C:\Users\kvasn\Documents\GitHub\Erik\img\Ptolemy_equality.svg.png)
$$
|AB||CD| + |AD||BC| = |AD||BC|
$$
Dôkaz je zaujímavý a niekedy ho urobíme. Zatiaľ je úloha dokázať, že z tohto tvrdenia vyplýva Pytagorova veta. 
