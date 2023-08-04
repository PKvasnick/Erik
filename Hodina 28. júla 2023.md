## Hodina 28. júla 2023

Program:

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli.
3. Dôkazy. Matematická indukcia
4. Domáca úloha (nová)

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Videohovor** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

### 1. Domáca úloha

**Príklad 1**

Dokážte, že pre všetky prirodzené n je číslo $n(n+1)(n+5)$ deliteľné 3.

**Riešenie**

*_Priamy dôkaz_*

Nech $r$ je zvyšok po delení n troma, teda $n=3k+r$, kde $k$ je prirodzené číslo alebo 0 a $r\in \{0, 1, 2\}$. Môžu nastať tri prípady: 

​	a. $r=0$, v tomto prípade tvrdenie očividne platí; 

​	b. $r=1$: v tomto prípde $n+5 = 3k +1+5$ a tvrdenie platí, pretože $n+5$ je deliteľné 3, a konečne v prípade 

​	c. $r=2$ je $n+1 = 3k+2+1$, a tvrdenie platí, pretože $n+1$ je deliteľné 3.

Tieto tri prípady vyčerpávajú všetky možné situácie a preto tvrdenie platí.

*_Dôkaz indukciou_*

Pre $n\in N$ označme $P(n)$ tvrdenie, že výraz $n(n+1)(n+5)$ je deliteľný 3.

1.  Základný prípad: P(0) platí, pretože 0 je deliteľná 3, a platí aj P(1), pretože $1\cdot 2 \cdot 6 = 12$ je deliteľné troma. 
2. Nech platí P(n) pre $n \in \{1, 2, \dots\}$. Dokážeme, že platí P(n+1). Skutočne, 

$$
(n+1)(n+1+1)(n+1+5) = n(n+2)(n+6) + (n+2)(n+6) \\
= n(n+1)(n+6) + n(n+6) + (n+2)(n+6) \\
= n(n+1)(n+5) + n^2 + n + n^2 + 6n + n^2 + 8n + 12 \\
= n(n+1)(n+5) + 3n^2 + 15 n + 12 \\
= n(n+1)(n+5) + 3(n^2 + 5n + 4)
$$

a oba výrazy na poslednom riadku sú deliteľné troma (prvý podľa indukčného predpokladu, druhý je násobkom 3), čím je tvrdenie dokázané. 

**Príklad 2**

Riešte rovnicu 

​		a.  $x^3 + x = 350$

​		b.  $x^3 - 9x^2 + 27x - 27 = 0$

**Riešenie a.** 

*_Metóda pozriem a vidím_*: $343 = 7^3$ a teda $x=7$ je jeden koreň rovnice. Známou metódou syntetického delenia dostaneme 

| 7 ⌟  | 1    | 0    | 1    | -350 |
| ---- | ---- | ---- | ---- | ---- |
|      |      | 7    | 49   | 350  |
|      | 1    | 7    | 50   | 0    |

$$
x^3 + x - 350 = (x-7)(x^2 + 7x + 50) 
$$

Z toho vidíme, že sme našli jediný reálny koreň rovnice, pretože polynóm druhého stupňa vpravo nemá reálne korene. 

Koreň $x=7$ dostaneme tiež pomocou vety o racionálnom koreni. Pretože $q=1$,  $p = 350 = 2\cdot 5^2 \cdot 7$, možné racionálne korene sú $\{\pm1, \pm2, \pm5, \pm7, \pm10, \pm14, \pm25, \pm35, \pm50, \pm70, \pm175, \pm350\}$. Vzhľadom na tvar rovnice môžeme ľahko vylúčiť malé $(1, 2, 5)$, ako aj veľké $(10, 14, \dots)$ korene. 

**Riešenie b.**

$x^3 - 9x^2 + 27x - 27 = 0$

Opäť začneme metódou pozriem a vidím, v tomto prípade vidíme koreň $x=3$, a to hneď trojnásobný: $x^3 - 9x^2 + 27x - 27 = x^3 - 3\cdot 3\cdot x^2 + 3\cdot 3^2\cdot x - 3^3 = (x-3)^3$. 

V prípade, že máme oko zahmlené, veta o racionálnom koreni nás nabáda preskúmať korene $\{\pm 1, \pm3, \pm9, \pm27\}$.

---

**Príklad 3.**                             

Riešte rovnicu $8^x 27^x = 6 \sqrt[5]{6}$

**Riešenie**

Túto rovnicu vyriešime prevedením mocnín na spoločný základ:
$$
8^x 27^x = 2^{3x}3^{3x}=6^{3x} \\
6 \sqrt[5]{6} = 6^{1+\frac{1}{5}} = 6^{6/5}
$$
odtiaľ $3x = 6/5 \implies x = 2/5$.

---

**Príklad 4**

Ak je $\sin{x°} = 12/13$, čomu sa rovná $\cos{(90°-x°)}$?

**Riešenie**
$$
cos(90\degree - x\degree) = cos(90\degree)cos(x\degree) + sin(90\degree)sin(x\degree) \\
= 0\cdot cos(x\degree) + 1\cdot sin(x\degree) = sin(x\degree) = 12/13
$$
Geometrická interpretácia:

<img src="img\sin_cos.png" alt="sin_cos" style="zoom:25%;" />

## 2. Príklady na zahriatie

Dnes iba jeden,  ukazuje sa, že viac nestíhame.

Nájdite všetky reálne x, spĺňajúce rovnicu 
$$
x^4 - 12x - 5 = 0
$$
**Riešenie**

Hoci máme vzorce pre korene rovníc 3. a 4. stupňa, tie sú prakticky nepoužiteľné. Preto sa snažíme nájsť riešenie takýchto rovníc rôznymi fintami. Niekoľko sme už prebrali:  

- Skúsiť faktorizovať, 
- veta o racionálnom koreni

Dnes sa naučíme ďalší spôsob, ako faktorizovať polynóm 4. stupňa. Veta o racionálnom koreni nám nič nedá - hoci máme polynóm s celočíselnými koeficientmi, $\pm 1, \pm5$ nie sú korene. 

Skúsme, či by nešlo náš polynóm 4. stupňa rozbiť na súčin kvadratických polynómov, nejako takto:
$$
x^4 - 12x - 5 = (x^2 + ax + b)(x^2 + Ax + B)
$$
Máme 4 koeficienty a 4 parametre, to by mohlo ísť. Roznásobíme a skúsime vyriešiť sústavu rovníc pre koeficienty:
$$
\begin{array}{llr}
x^3: \quad a + A &=& 0 \\
x^2: \quad b + B + aA &=& 0 \\
x^1: \quad aB + Ab &=& -12 \\
x^0: \quad bB &=& -5
\end{array}
$$
Teraz nejako treba rozmotať toto klbko. Napríklad
$$
A = -a \\
\implies b-B = \frac{12}{a} \\
\implies b + B = a^2 \\
2b = \frac{12}{a} + a ^2 \implies b = \frac{6}{a} + \frac{1}{2}a^2,\quad B = -\frac{6}{a} + \frac{1}{2}a^2
$$
a teraz musíme dosadiť do poslednej rovnice a vypočítať $a$:
$$
\left(\frac{6}{a} + \frac{1}{2}a^2 \right) \left(-\frac{6}{a} + \frac{1}{2}a^2\right) = -5 \\
(a^3 + 12)(a^3-12) = 20a^2 \\
(a^2)^3 + 20a^2 - 144 = 0
$$
Toto našťastie vieme faktorizovať, pretože $a^2 = 4$ je koreň, takže
$$
(a^2)^3 + 20a^2 - 144 = (a^2)^3 - 64 + 20(a^2 - 4) = (a^2-4)\left((a^2)^2 + 4a^2 + 36\right)
$$
a vidíme, že člen kvadratický v $a^2$ nemá reálne (tobôž nie kladné) korene, takže jediné riešenie našej sústavy je $a=2,\,A=-2,\,b=5,\,B=-1$ (druhý koreň $a=-2$ dáva riešenie, kde si a, b vymenia úlohy s A, B). Tak sa naša rovnica 4. stupňa rozpadáva na dve kvadratické rovnice:
$$
x^4 - 12x - 5 = (x^2 + 2x + 5)(x^2 - 2x - 1) = 0 \\ \iff \\ x^2 + 2x + 5 = 0 \quad \textrm{alebo} \quad x^2 - 2x - 1 = 0
$$
Prvá z rovníc nemá reálne riešenia, z druhej **$x = 1 \pm \sqrt{2}$**, a to sú všetky reálne riešenia našej rovnice. Táto metóda nie je univerzálne úspešná - rovnice pre koeficienty a, A, b, B môžu byť komplikovanejšie ako pôvodná rovnica. 

*_Alternatívna faktorizácia_*

Iný spôsob, ako faktorizovať polynóm štvrtého stupňa:

Upravíme rovnicu na tvar $x^4 = 5x + 12$ a skúsime k obom stranám pridať člen tvaru $ax^2 + b$ tak, aby sme na oboch stranách dostali úplný štvorec. Na pravej strane máme $x^4 + ax^2 + b$, a aby sme získali úplný štvorec $(x^2 + a/2)^2 = x^4 + 2\cdot a/2 \cdot x^2 + (a/2)^2$,  potrebujeme, aby platilo
$$
b = \frac{a^2}{4}
$$
Podobne na druhej strane budeme mať $ax^2 + 12x + 5 + b = a(x^2 + 2\cdot 12/(2a) x + (5+b)/a)$, a teda pre úplný štvorec $(x + 6/a)^2$ potrebujeme
$$
\frac{5 + b}{a} = \frac{36}{a^2} \implies b = 36/a - 5
$$
Máme dve rovnice pre parametre $a, b$, a podobne ako v predchádzajúcom prípade nemáme žiadnu záruku, že riešenie tejto sústavy bude ľahšie ako riešenie pôvodnej rovnice. Dosadíme za b z prvej rovnice do druhej
$$
\frac{a^2}{4} = \frac{36}{a} - 5 \\
a^3 + 20a - 144 = 0 
$$
a túto rovnicu sme už videli a vieme, že má jediný reálny koreň a = 4.  Potom b = 4 a máme
$$
(x^2 + 2)^2 - 4(x+3/2)^2 = 0 \\
(x^2 + 2 + 2x + 3)(x^2 + 2 - 2x - 3) = 0 \\
(x^2 + 2x + 5)(x^2 - 2x - 1) = 0
$$
teda rovnaků faktorizáciu ako predtým a oba postupy sa cestou zišli a teda sú prakticky ekvivalentné. 

---

## 3. Dôkazy. Matematická indukcia

#### Čo je dôkaz

Dôkaz je metóda určenia pravdy.  V rôznych oblastiach sa toto dosahuje rôznymi spôsobmi:

- Súdny výrok
- Božie slovo
- Experimentálna veda
- Štatistické zisťovanie
- Vnútorné presvedčenie
- "Neviem, prečo by to nemala byť pravda..."
- Zastrašovanie

**V matematike** znamená dôkaz výroku reťazec logických dedukcií, ktoré dokazujú pravdivosť výroku vychádzajúc z množiny axióm. 

**Logický výrok** je tvrdenie, ktoré je pravdivé alebo nepravdivé. Ne-výroky: "Umy si nohy!", "A teda čo je to dôkaz?"

* Výrok: 2+3 = 5. Tento výrok je pravdivý, aj keď nie je úplne jednoduché ukázať to, pretože toto tvrdenie spočíva na úplných základoch aritmetiky. 
* Výrok. Pre prirodzené číslo $n$ je $n^2 + n + 41$ prvočíslo. 

​	Toto je iný výrok ako predchádzajúci. Máme tu dve nové veci: **Predikát** - teda parametrizovaný výrok (logickú funkciu), ktorý je pravdivý alebo nepravdivý podľa toho, čo doň dosadíme. A máme dokázať, že tvrdenie platí pre nekonečnú množinu čísel 1, 2, ...  V matematickej notácii máme špeciálne symboly, označujúce, že nejaký predikát platí pre všetky prvky danej množiny ($\forall$), alebo že existuje prvok množiny, ktorý spĺňa daný predikát ($\exist$). Tieto symboly nazývame **kvantifikátory**. Teda posledný výrok môžeme napísať takto: $\forall n \in N: n^2 + n + 41\, \textrm{je prvočíslo}$. Negácia takéhoto tvrdenia je $\exist n \in N: n^2 + n + 41\, \textrm{nie je prvočíslo}$ (nemáme užitočný symbol pre označenie, že číslo je alebo nie je prvočíslo).

​		Pri takýchto tvrdeniach väčšinou postupujeme tak, že vykonáme prieskum bojom: overíme platnosť tvrdena na niekoľkých hodnotách, a snažíme sa zistiť, ako tvrdenie "funguje". Toto tvrdenie má tú zvláštnu vlastnosť, že platí pre všetky n menšie ako 40, ale pre 40 dostaneme $40^2 + 40 + 41 = 40*41 + 41$ a teda sa nejedná o prvočíslo.  

* Výrok. Neexistujú prirodzené čísla a, b, c, d spĺňajúce rovnosť $a^4 + b^4 + c^4 = d^4$.  Toto tvrdenie pochádza od Leonard Eulera z roku 1769, a až o 218 rokov neskôr Noam Elkies ukázal, že neplatí: a = 95800, b = 217519, c = 414560, d = 422481 sú riešením rovnice. 

**Axiómy** sú tvrdenia, ktoré považujeme za pravdivé. Existujú známe systémy axióm, napríklad Euklidove axiómy rovinnej geometrie, často ale ako systém axiómov používame zrejmé vlastnosti celých či reálnych čísel. 

**Dôkaz** je potom reťaz implikácií, ktorými ukážeme, že dané tvrdenie vyplýva z axióm (alebo zrejmých tvrdení).

#### Rôzne dôkazy

**Príklad**

Dokážte, že v každej skupine 6 ľudí sa nájde buď trojica ľudí, ktorí sa navzájom poznajú, alebo trojica ľudí, ktorí sa navzájom nepoznajú.

**Riešenie**

Toto je úloha na pomalé myslenie. Máme dokázať tvrdenie pre šesticu ľudí, ktorých vzťahy sú úplne náhodné - teda pre každú šesticu, kde sa ľudia i a j poznajú, existuje šestica, kde sa nepoznajú a tvrdenie musí platiť pre obe. 

![Untitled](img\Untitled.png)

Budeme postupovať prípad po prípade. Zvolíme si náhodného človeka a budeme osobitne skúmať prípad, keď nepozná troch alebo viac ľudí (Prípad 1 na obrázku, zelení ľudia), a  prípad, keď pozná troch alebo viacerých ľudí (Prípad 2, modrí ľudia)  Úloha: premyslieť, prečo to vyčerpáva všetky možné situácie.

<img src="img\Siesti.png" alt="Untitled" style="zoom: 67%;" />



#### Dôkaz matematickou indukciou

Ak máme dokázať platnosť tvrdenia pre všetky prirodzené čísla, často využívame dôkaz matematickou indukciou 

- Dokážeme tvrdenie pre nejaké počiatočné $n$, napríklad $n=1$.  (počiatočný prípad, *_base case_*)
- Dokážeme, že z platnosti tvrdenia pre $k = n$ vyplýva platnosť tvrdenia pre $k = n+1$.

Toto zaručuje platnosť tvrdenia pre všetky $n$: vychádzajúc z počiatočnej hodnoty $n=1$, postupne pomocou indukčného kroku vieme dokázať platnosť pre $n=2, 3,  \dots$. 

**Úloha**

Dokážte, že pre všetky prirodzené čísla $n \ge 1$ platí $1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}$.

**Dôkaz**

Ako P(n) označíme predikát
$$
1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}
$$
Platnosť P(n) pre všetky prirodzené čísla dokážeme matematickou indukciou.

1. Počiatočný prípad: P(1) platí , pretože $1^2 = \frac{1\cdot(1+1)(2+1)}{6} = 1$.
2. Indukčný krok: Dokážeme, že z platnosti P(n) vyplýva platnosť P(n+1), n = 1, 2, ... .Nech teda platí P(n), , teda $1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}$. Dokážeme, že z toho vyplýva platnosť  P(n+1(). Skutočne, 

$$
1^2 + 2^2 + \dots + n^2 + (n+1)^2 = \frac{n(n+1)(2n+1)}{6} + (n+1)^2 \\
=  \frac{n(n+1)(2n+1)}{6} + \frac{6(n+1)^2}{6} = \frac{(n+1)(2n^2 + n + 6n + 6)}{6} \\
= \frac{(n+1)(2n^2 + 7n + 6)}{6} = \frac{(n+1)(n+2)(2n+3)}{6} \\
= \frac{(n+1)((n+1)+1)(2(n+1)+1)}{6}
$$

a teda z platnosti P(n) vyplýva platnosť P(n+1), čím je dôkaz dokončený.

**Úloha**

Dokážte, že všetky kone sú rovnakej farby.

**Dôkaz**

Ako K(n) označíme predikát "V každej množine koní veľkosti n majú všetky kone rovnakú farbu."

Dôkaz vykonáme matematickou indukciou. 

<img src="img\kone.png" alt="Untitled" style="zoom:50%;" />

1. (Base case) K(1) triviálne platí: Pre množinu veľkosti 1 máme jediného koňa a jedinú farbu.
2. (Indukčný krok) Predpokladajme, že platí K(n): "V každej množine koní veľkosti n majú všetky kone rovnakú farbu". Ukážeme, že z toho vyplýva platnosť K(n+1). Skutočne, označme  $\Kappa = \{k_1, k_2, \dots, k_n, k_{n+1}\}$ nejakú množinu koní veľkosti n+1. Podľa predpokladu kone v množinách veľkosti n,  $\Lambda = \{k_1, k_2, \dots, k_n\}$, a $\Mu = \{k_2, \dots, k_n, k_{n+1}\}$, majú rovnakú farbu. Potom ale všetky kone v $\Kappa$ musia mať rovnakú farbu, pretože množiny $\Lambda$ a $\Mu$ obsahujú spoločné kone $k_2, \dots, k_n$, a teda - keďže každý kôň môže mať jedinú farbu - všetky kone  v ich zjednotení $\Lambda \cup \Mu = \Kappa$ musia mať rovnakú farbu. Tým sme dokázali, že z K(n) vyplýva K(n+1) a dôkaz platnosti K(n) pre všetky prirodzené n tým je dokončený: všetky kone majú rovnakú farbu. 



## 4. Domáca úloha (nová)

1. Dokážte, že pre všetky kladné čísla $a, b$ platí 

$$
\frac{a+b}{2}\ge \sqrt{ab}
$$

2. Dokážte, že pre prirodzené $n$ je $\log_7{n}$ celé alebo iracionálne číslo.

3. Dokážte, že pre reálne $r, s$ platí

   a. $min(r, s) + max(r, s) = r + s$

   b. $|r + s| \le |r| + |s|$

4. Ak umocníme iracionálne číslo na iracionálne číslo, môže byť výsledok racionálny? Ukážte na prípade $\sqrt{2}^{\sqrt{2}}$.

