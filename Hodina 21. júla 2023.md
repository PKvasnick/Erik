## Hodina 21. júla 2023

Program:

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli.
3. Dôkazy. Matematická indukcia
4. Domáca úloha (nová)

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Telekonferencia** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

### 1. Domáca úloha

**Príklad 1**

Označme gcd(m, n) najväčší spoločný deliteľ celých čísel m,n (*_greatest common divisor_*), teda najväčšie číslo, ktoré je deliteľom m i n. Nech m>n. Dokážte, že 

​	a. gcd(m-n, n) = gcd(m,n)

​	b. gcd(m % n) = gcd(m, n) 

kde znak % označuje zvyšok po celočíselnom delení m a n. 

**Riešenie**

$gcd(m,n)$ je najväčšie prirodzené číslo d také, že pre nejaké prirodzené čísla p, q platí $m = pd, n = qd$.

Vyjadrime $m-n$:
$$
m - n = pd - qd = (p-q)\cdot d
$$
 a teda d je deliteľom aj $m-n$​. Ešte musíme ukázať, že d je *_najväčší_* spoločný deliteľ m-n a n. 

Dôkaz vykonáme sporom: Budeme predpokladať opak, teda že $gcd(m-n, n) = D > d$, a ukážeme, že takýto predpoklad vedie k logickým rozporom.  Skutočne,  ak $gcd(m-n, n) = D > d$, existujú prirodzené čísla P a Q také, že $m-n = PD, n = QD$. Ďalej ale tiež platí
$$
m = (m - n) + n = PD + QD = (P+Q)D
$$
D je teda deliteľom m aj n, a pretože sme predpokladali, že d je najväčším spoločným deliteľom m a n, nemôže byť $D>d$. Negácia pôvodného tvrdenia teda vedie k logickému sporu, a preto musí platiť pôvodné tvrdenie: d je najväčší spoločný deliteľ m-n a n, a teda aj m-n a n. 

Podobne dokážeme druhé tvrdenie: 

Označme r = m % n, teda existuje nejaké celé číslo k také, že $m = k\cdot n + r$.  Nech $d = gcd(m, n)$, potom píšeme $m = pd, n = qd, r = m - k\cdot n = p\cdot d - k\cdot q \cdot d = (p - kq)\cdot d$ a teda aj r je deliteľné d. Podobne ako v predchádzajúcom prípade treba ešte dokázať, že d je *_najväčší_* spoločný deliteľ. 

---

**Príklad 2**

Dokážte, že $\sqrt{2}$ nie je racionálne číslo.

**Riešenie**

Dôkaz uskutočníme sporom: Dokážeme, že opačné tvrdenie vedie k logickým rozporom:

Predpokladajme, že platí opačné tvrdenie: $\sqrt{2}$ je racionálne číslo. Potom existujú nesúdeliteľné prirodzené čísla p a q také, že 
$$
\sqrt{2} = \frac{p}{q}
$$
(Nesúdeliteľnosť p a q znamená, že gcd(p, q) = 1).  Ak predchádzajúcu rovnosť umocníme na druhú, dostaneme 
$$
2 = \frac{p^2}{q^2}
$$
teda $2q^2 = p^2$ a teda p musí byť párne, $p = 2k$. Potom ale $2q^2 = 4k^2$, resp. $q^2 = 2p^2$ a aj q musí byť párne. To je ale v spore s predpokladom, že p a q sú nesúdeliteľné - znamená to, že nech zlomok p/q krátime, koľko chceme, stále sa dá skrátiť ďalšia dvojka. Opačné tvrdenie nás teda priviedlo k logickým rozporom, a preto musí platiť pôvodné tvrdenie:  $\sqrt{2}$ nie je racionálne číslo.

---

**Príklad 3.**                             

Riešte:
$$
x^2 - y^2 = 24 \\
xy=35 \\
x + y = ?
$$
**Riešenie**

Symetria: ak je $\{x,y\}$ riešením rovníc, potom je ním aj $\{-x,-y\}$. 

Skúsme najprv nájsť ľahké riešenie v celých číslach:

x a y musí byť dvojica i združených deliteľov 35, pričom kvôli prvej rovnici bude x väčší z deliteľov, a teda - ak odhliadneme od záporných riešení - máme dve možnosti, $\{35,1\}$ a $\{7,5\}$. Z nich iba druhá dáva použiteľné riešenie, a teda $x+y=\pm12$. Existuje ešte iné riešenie? Ak z druhej rovnice vyjadríme y a dosadíme do prvej rovnice, dostaneme kvadratickú rovnicu pre $x^2$:
$$
y = \frac{35}{x} \\
x^2 - \frac{35^2}{x^2} = 24 \\
x^4 - 24x^2 - 35^2 = 0 \\
x^2 = 12 \pm 37
$$
Prvý koreň dáva riešenie, ktoré sme už našli,  $\{\pm 7, \pm 5\}$. Druhý koreň nám dáva zábavné komplexné riešenie  $\{\pm 5i, \pm 7i\}$, v ktorom si x a y vymenia roly, ale $x+y=\pm 12$ ako u predchádzajúceho riešenia.

---

**Príklad 4**

Nájdite reálne riešenia rovnice
$$
x^6 = (x-1)^6
$$
**Riešenie**

Faktorizujeme, faktorizujeme, faktorizujeme:
$$
(x^3)^2 - ((x-1)^3)^2 = (x^3 + (x-1)^3)\cdot (x^3 - (x-1)^3) \\
= (2x-1)(x^2 - x(x-1) + (x-1)^2)(1)(x^2 + x(x-1) + (x-1)^2) \\
= 2(x-\frac{1}{2})(x^2 - x + 1)(3x^2 - 3x + 1)
$$
a pretože dva kvadratické členy nemajú reálne korene, máme jediný reálny koreň $x=1/2$.

![image-20230717025624021](img\image-20230717025624021.png)

(Aj keď to tak nevyzerá, je to v poriadku, pretože rovnica je skutočnosti 5. stupňa, a máme jeden reálny koreň a dve dvojice komplexných).

## 2. Príklady na zahriatie

**Príklad 1**

Nájdite všetky reálne x, spĺňajúce rovnicu 
$$
\log_4{x} = \log_x{4}
$$


**Príklad 2**

Rekurzívne štruktúry:

a. Nájdite všetky x, pre ktoré platí
$$
2 = x^{x^{x^{x^{.^{.^{.^.}}}}}}
$$
a všetky x pre ktoré platí
$$
4 = x^{x^{x^{x^{.^{.^{.^.}}}}}}
$$
Porucha...

b. Čomu sa rovná
$$
\sqrt{2+\sqrt{2+\sqrt{2+\sqrt{2+\dots}}}}
$$
c. Čomu sa rovná
$$
1 + \frac{1}{1+\frac{1}{1+\frac{1}{1+\frac{1}{1+\dots}}}}
$$
**Príklad 3**

Minule sme delili polynómy a učili sme sa používať vetu o zvyšku na výpočet hodnoty polynómu. Dnes to použijeme na riešenie rovníc:

Nájdite racionálne korene rovnice


$$
x^3 + 3x^2 - 4x - 12 = 0
$$
Návod: Veta o racionálnych koreňoch

Jediné racionálne korene rovnice s celočíselnými koeficientmi $a_nx^n + a_{n-1}x^{n-1} + \dots + a_0 = 0$ majú tvar $\pm p_i/q_j$, kde $\{p_1, p_2, \dots\}$ sú delitelia $a_0$ a  $\{q_1, q_2, \dots\}$ sú delitelia $a_{n}$ . V našom prípade máme $q=1, p \in \{1, 2, 3, 4, 6, 12\}$ , a teda korene hľadáme medzi číslami $\{\pm1, \pm 2, \pm 3, \pm 4, \pm 6, \pm 12\}$: Toto je dobrá aplikácia pre výpočet hodnoty polynómu pomocou vety o zvyšku. Okrem toho po objavení každého koreňa je treba polynóm vydeliť, aby sme mohli nájsť prípadné dvojnásobné korene a tiež aby sme si ušetrili prácu. 

**Príklad 4**

Nech $P(x) = 2x^3 + 7x^2 + 2x + 1$. Pomocou delenia polynómov nájdite $P(5)$.

Návod:

*_Veta o zvyšku_* (Remainder theorem): Nech P(x( je polynóm stupňa $\ge 1$. Potom zvyšok po delení
$$
\frac{P(x)}{x-a}
$$

sa rovná P(a). Dôkaz:  Nech výsledok delenia P(x() lineárnym polynómom (x-a) je polynóm Q(x) a zvyšok R. Z definície platí $P(x)=(x-a)Q(x) + R$, a pre $x=a$ dostaneme $P(a) = (a-a)Q(x) + R = R$ .

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

1. (Base case) K(1) triviálne platí: Pre množinu veľkosti 1 máme jediného koňa a jedinú farbu.
2. (Indukčný krok) Predpokladajme, že platí K(n): "V každej množine koní veľkosti n majú všetky kone rovnakú farbu". Ukážeme, že z toho vyplýva platnosť K(n+1). Skutočne, označme  $\Kappa = \{k_1, k_2, \dots, k_n, k_{n+1}\}$ nejakú množinu koní veľkosti n+1. Podľa predpokladu kone v množinách veľkosti n,  $\Lambda = \{k_1, k_2, \dots, k_n\}$, a $\Mu = \{k_2, \dots, k_n, k_{n+1}\}$, majú rovnakú farbu. Potom ale všetky kone v $\Kappa$ musia mať rovnakú farbu, pretože množiny $\Lambda$ a $\Mu$ obsahujú spoločné kone $k_2, \dots, k_n$, a teda - keďže každý kôň môže mať jedinú farbu - všetky kone  v ich zjednotení $\Lambda \cup \Mu = \Kappa$ musia mať rovnakú farbu. Tým sme dokázali, že z K(n) vyplýva K(n+1) a dôkaz platnosti K(n) pre všetky prirodzené n tým je dokončený. 



## 4. Domáca úloha (nová)

1. Dokážte, že pre všetky prirodzené n je číslo $n(n+1)(n+5)$ deliteľné 3.

2. Riešte rovnicu 

​		a.  $x^3 + x = 350$

​		b.  $x^3 - 9x^2 + 27x - 27 = 0$

3. Riešte rovnicu $8^x 27^x = 6 \sqrt[5]{6}$

4. Ak je $\sin{x°} = 12/13$, čomu sa rovná $\cos{(90°-x°)}$?

