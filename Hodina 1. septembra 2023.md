## Hodina 1. septembra 2023

Program:

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli.
3. Geometria, (hlavne) Ptolemaiova veta.
4. Domáca úloha (nová)
5. Program na budúci týždeň

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Videohovor** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

### 1. Domáca úloha

 **Príklad 1**

Pomocou princípu dobrého usporiadania dokážte, že pre všetky nezáporné celé čísla $n$ platí
$$
0^3 + 1^3 + 2^3 + \dots + n^3 = \left( \frac{n(n+1)}{2}\right)^2
$$

**Riešenie**

Vykonáme dôkaz sporom, teda budeme predpokladať, že existuje nejaké n >0, pre ktoré tvrdenie neplatí. Ukážeme, že tento predpoklad vedie k logickým rozporom. 

Označme C množinu všetkých n, pre ktoré neplatí tvrdenie P(n):
$$
0^3 + 1^3 + 2^3 + \dots + n^3 = \left( \frac{n(n+1)}{2}\right)^2
$$
Množina C musí mať minimálny prvok, pretože množina jej potenciálnych prvkov je ohraničená zdola nulou, a vieme ľahko ukázať, že pre malé n tvrdenie platí. Označme minimálny prvok množiny C ako N. Pretože N je minimálny prvok, tvrdenie P(n) platí pre N-1:
$$
0^3 + 1^3 + 2^3 + \dots + (N-1)^3 = \left( \frac{N(N-1)}{2}\right)^2
$$
Odtiaľ ale máme 
$$
0^3 + 1^3 + 2^3 + \dots + (N-1)^3 + N^3 = \left( \frac{N(N-1)}{2}\right)^2 + N^3 \\
= N^2\frac{(N-1)^2 + 4N}{4} = N^2\frac{(N+1)^2}{4} = \left( \frac{N(N+1)}{2}\right)^2
$$
P(N) teda tiež platí, a teda musí byť chybný predpoklad o platnosti P(N-1), čo by zase znamenalo, že N nie je najmenším prvkom C a to je rozpor s predpokladom. Vidíme, že množina C nemôže mať najmenší prvok, a to je možné iba ak je prázdna. 

---

**Príklad 2**

Iná verzia mini-tetrisu: Máme stále hraciu dosku o rozmeroch $2\times n$, a tentoraz máme  5 dielikov::

​		![image-20230808173304124](img\mini-tetris3.png)

​		Teda napríklad pre hraciu plochu $2\times 1$ máme dve riešenia:

​		<img src="img\mini-tetris4.png" alt="image-20230808173603186" style="zoom:75%;" />

​		a pre hraciu plochu $2\times 2$ sú platnými riešeniami napríklad tieto:

​		![image-20230808173900907](img\mini-tetris5.png)

​		Vypočítajte počet riešení $T_n$ pre hraciu plochu $2\times n,\,n=1, 2, \dots$. 

**Riešenie**

Použijeme identický postup ako v predchádzajúcej verzii mini-tetrisu:

Riešenie pre $n$ môžeme zostrojiť z "elementárnych" riešení pre $n-1$ a $n-2$, teda riešení, ktoré nemožno rozložiť na riešenia menšej výšky:
$$
T_n = E_1 \cdot T_{n-1} + E_2 \cdot T_{n-2}
$$
Nemáme elementárne stavebné dieliky s výškou väčšou ako 2, takže ďalšie členy nepotrebujeme. Všetko čo potrebujeme pre zostavenie rekurzie sú počty elementárnych riešení  $E_1, E_2$ a tie môžeme ľahko vyčísliť priamo:

- n=1: Riešenie vidíme v zadaní, $E_1 = T_1 = 2$, pretože riešenia výšky 1 z princípu nie sú redukovateľné.
- n=2: Ak sa obmedzíme na riešenia, používajúce dieliky výšky 2 (pretože tie a iba tie nie sú redukovateľné), dostaneme $E_2=3$:

![minitetriDUs.drawio](img\minitetriDUs.drawio.png)

Teraz už ľahko dostaneme rekurzívny vzťah pre $T_n$:
$$
T_n = 2T_{n-1} + 3T_{n-2}
$$
Zase máme lineárnu rekurzívnu rovnicu s konštantnými koeficientmi a riešime ju štandardným postupom:
$$
T_n = q^n \\
q^n = 2q^{n-1} + 3q^{n-2} \implies q^2 - 2q - 3 = 0 \implies (q+1)(q-3) = 0 \\
q_1 = -1, q_2 = 3 \\
T_n = C_1(-1)^n + C_23^n
$$
Konštanty $C_1, C_2$ určíme z počiatočných podmienok:

- $T_1$ = 2
- $T_2$ = 7, z čoho vyplýva 
- $T_0$ = 1

S použitím n=0, 1 dostaneme sústavu
$$
C_1 + C_2 = 1\\
-C_1 + 3C_2 = 2 \\
4C_2 = 3 \implies C_2 = \frac{3}{4}, C_1 = \frac{1}{4}
$$
a teda nakoniec dostaneme
$$
T_n = \frac{1}{4}(-1)^n + \frac{3}{4}3^n = \frac{3^{n+1} + (-1)^n}{4}
$$

---

**Príklad 3**

Napíšte kus kódu v Pythone, ktorý vygeneruje všetky riešenia mini-tetrisu (vo verzii, ktorú si vyberiete) pre zadané $n$. 

**Riešenie**

Začneme s prázdnym stĺpcom a máme niekoľko možností, ako ho zväčšiť. Pre každý zväčšený stĺpec máme opäť niekoľko možností predĺženia atď. Predchádzame teda stromom riešení a keď dosiahneme stĺpec požadovanej dĺžky, uložíme ho alebo vypíšeme a pokračujeme na ďalšej vetvi stromu. 

Efektívna implementácia takéhoto algoritmu používa zásobník - začneme so zásobníkokm, obsahujúcim prízdny stĺpec a potom pracujeme v cykle, až kým sa zásobník nevyprázdni:

- vyberieme stĺpec zo zásobníka
- použijeme všetky možné dieliky či ich kombinácie, aby sme stĺpec predĺžili. 
- Ak má predĺžený stĺpec dĺžku n, uložíme ho alebo vytlačíme. Ak má väčšiu dĺžku, zahodíme ho. Ak má menšiu dĺžku, uložíme ho do zásobníka.
- Po vyčerpaní všetkých možností predĺženia pokračujeme ďalším cyklom. 

Tuto je jednoduchá implementácia (znaky Unicode sú iba ozdoba, nie sú pre riešenie vôbec podstatné; nájdete v repozitári ako `mini_tetris.py`):

```python

# Dlzky a kody dielikov

parts = [
    ("\U00002589", 2),              # ▉ štvorec 2x2
    ("\U00002599\U0000259D",2),     # ▙▝ diel L, plus chýbajúci štvorec
    ("\U0000259B\U00002597",2),     # ▛▗ diel obrátené L plus chýbajúci štvorec
    ("\U0000258B", 1),              # ▋ obdĺžnik 2x1
    ("\U0000259A", 1)               # ▚ dva štvorce 1x1
]


def print_column(column: list[str]) -> None:
    *** Vypisujeme kombinácie znakov s medzerou ***
    print(" ".join(column))


def generate(n:int) -> None:
    *** Prehľadáva strom do hĺbky pomocou zásobníka ***
    stack = []
    stack.append(([], 0))
    n_solutions = 0
    while stack:
        column, length = stack.pop()
        for part in parts:
            column.append(part[0])
            new_length = length + part[1]
            if new_length < n:
                stack.append((column[:], new_length))
            elif new_length == n:
                print_column(column)
                n_solutions += 1
            column.pop()

    print(f"{n_solutions} rieseni.")


def main():
    print(parts)
    generate(3)


if __name__ == "__main__":
    main()

```

Výstup:

```python
[('▉', 2), ('▙▝', 2), ('▛▗', 2), ('▋', 1), ('▚', 1)]
▚ ▉
▚ ▙▝
▚ ▛▗
▚ ▚ ▋
▚ ▚ ▚
▚ ▋ ▋
▚ ▋ ▚
▋ ▉
▋ ▙▝
▋ ▛▗
▋ ▚ ▋
▋ ▚ ▚
▋ ▋ ▋
▋ ▋ ▚
▛▗ ▋
▛▗ ▚
▙▝ ▋
▙▝ ▚
▉ ▋
▉ ▚
20 rieseni.
```



---

**Príklad 4**

Ptolemaiova veta je silnejšie tvrdenie ako Pytagorova veta: Pre štvoruholník ABCD vpísaný v kružnici platí


​		![Ptolemy_equality.svg](img\Ptolemy_equality.svg.png)
$$
|AB||CD| + |AD||BC| = |AD||BC|
$$
Dokážte, že z tohto tvrdenia vyplýva Pytagorova veta. 

**Riešenie**

Stačí vziať štvoruholník ABCD, ktorý je obdĺžnik so stranami $a, b$ a uhlopriečkami $c$, teda $AB = a, BC = b, CD = a, DA = b, AC = c, BD = c$. Potom z Ptolemaiovej vety priamo dostávame Pytagorovu vetu $a^2 + b^2 = c^2$.

Treba vyjasniť, že trojuholníky ABC a CDA sú pravouhlé. Pretože priesečník uhlopriečok je stred symetrie obdĺžnika, musí byť totožný so stredom opísanej kružnice. Potom napríklad uhol ABC je obvodový uhol zodpovedajúci stredovému uhlu ASC, ktorý je zjavne 180°, a má teda 90°. 

---

## 2. Príklady na zahriatie

**$\sqrt{2}$ je iracionálne číslo - geometrický dôkaz**

Dôkaz iracionality $\sqrt{2}$ sme už robili, ale poďme si to ešte raz urobiť trocha inak, a možno sa naučíme čo-to nové. 

Budeme robiť dôkaz sporom, teda predpokladáme, že existujú dve celé čísla $a, b$ také, že$a/b = \sqrt{2}$. Predpokladajme ďalej, že $\gcd(a, b) = 1$, inak povedané, naše $a, b$ sú najmenšie čísla  s touto vlastnosťou. 

Zostrojme rovnoramenný pravouhlý trojuholník s ramenami o dĺžke $b$. Odvesna trojuholníka má potom podľa Pytagorovej vety dĺžku $a$. Podrobnejšie:, z Pytagorovej vety máme $a^2 = 2b^2$, a teda $a/b=\sqrt{2}$.  

![TwoIrrationalProof](img\TwoIrrationalProof.png)

Zostrojme teraz nový rovnoramenný pravouhlý trojuholník takto:

- Na odvesne AB zostrojíme bod D tak, že $|BD| = |BC| = b$.  
- Dotyčnica ku kružnici so stredom B o polomere $b$ v bode D pretína stranu AC v bode E. 
- Trojuholník ADE je podobný trojuholníku ACB,  pretože má pravý uhol vo vrchole D a zdieľa uhol DAE s trojuholníkom ACB. 
- To znamená, že $|AD| = |DE| = a - b$ ; okrem toho $|EC| = |ED| = a-b$, pretože body D a C ležia na rovnakej kružnici so stredom B a polomerom $b$ a bod E leží na osi uhla DBC. 
- Pretože $|AC| = b,\, |EC|=a-b$, je $|AE| = b - (a-b) = 2b-a$.
- Pretože ACB a ADE sú podobné trojuholníky, platí 

$$
\sqrt{2} = \frac{a}{b} = \frac{2b-a}{a-b}
$$

Keďže a, b sú kladné celé čísla a $b<a<2b$, je $a-b<b,\, 2b-a<a$. Máme teda dve nové čísla $A=2b-a,\, B = a-b$, ktoré sú menšie než $a, b$, ale obe majú požadovanú vlastnosť. To je v spore s predpokladom, a teda chybný je pôvodný predpoklad o existencii čísel $a, b$.

Tu by sme mohli dobre skončiť, ale skúsme sa na to celé pozrieť naopak. Vedeli by sme proces obrátiť? Teda vychádzajúc z racionálnej aproximácie $\sqrt{2} \approx a/b$ získať nejakú novú aproximáciu? 

Vyjdime z rovnoramenného pravouhlého trojuholníka $A_1B_1C_1$ s odvesnami o (celočíselnej) dĺžke $b_1=|A_1C_1|=|B_1C_1|$ a preponou $a_1 = |A_1B_1|$. Zostrojme nový rovnoramenný pravouhlý trojuholník takto:

- Bod $C_2$ leží na predĺžení úsečky $A_1B_1$ tak, že $|B_1C_2|=b_1$.
- Bod $B_2$ leží na kolmici k priamke $A_1B_1$ cez bod $C_2$ tak, že $|A_1C_2|=|C_2B_2|=a_1+b_1$.
- Bod $A_2$ je totožný s bodom $A_1$.
- Z konštrukcie vyplýva, že $|A_1C_2| = b_1 + a_1 + b_1 = a_1 + 2b_1$.

![RationalApproximation](img\Two_Approximation.png)

Skúsme, ako sa takéto aproximácie budú správať:  

- Definujme $a_0 = 3, b_0=2$.
- Definujme $a_k = a_{k-1} + 2b_{k-1},\, b_k = a_{k-1} + b_{k-1}$.

Prvých desať hodnôt je

| $k$  | $a$   | $b$   | $a/b$      | $a/b - \sqrt{2}$ |
| ---- | ----- | ----- | ---------- | ---------------- |
| 0    | 3     | 2     | 1.5        | 0.085786438      |
| 1    | 7     | 5     | 1.4        | -0.01421356      |
| 2    | 17    | 12    | 1.41666667 | 0.002453104      |
| 3    | 41    | 29    | 1.4137931  | -0.00042046      |
| 4    | 99    | 70    | 1.41428571 | 7.21519E-05      |
| 5    | 239   | 169   | 1.41420118 | -1.2379E-05      |
| 6    | 577   | 408   | 1.41421569 | 2.1239E-06       |
| 7    | 1393  | 985   | 1.4142132  | -3.644E-07       |
| 8    | 3363  | 2378  | 1.41421362 | 6.25218E-08      |
| 9    | 8119  | 5741  | 1.41421355 | -1.0727E-08      |
| 10   | 19601 | 13860 | 1.41421356 | 1.84047E-09      |

Toto nie je dobrá metóda na počítanie odmocniny z dvoch. Na to sa omnoho viac hodí metóda používajúca Newtonovu metódu:
$$
x_n = \frac{1}{2}\left(x_{n-1} + \frac{2}{x_{n-1}} \right)
$$
Táto metóda spresňuje výsledok v každom kroku približne o 2 desatinné miesta. 

Z pedagogických dôvodov poďme skúmať, či naša metóda konverguje k odmocnine z 2 a za akých podmienok. 

Naša metóda používa nejaké takéto priblíženie:
$$
\frac{a_n}{b_n} \equiv x_n = \frac{a_{n-1} + 2b_{n-1}}{a_{n-1} + b_{n-1}} = \frac{x_{n-1}+2}{x_{n-1} + 1}
$$
a rekurziu môžme vyjadriť pomocou reťazového zlomku:
$$
x = 1 + \frac{1}{1+\frac{1}{1+\frac{1}{1+ \dots}}}
$$
Rekurzia i reťazový zlomok budú konvergovať k hodnote 
$$
x = \frac{x+2}{x+1}
$$
teda $x^2-2 = 0$ a teda limita je skutočne $\sqrt{2}$. To nie je úplne prekvapivé a skôr nás bude zaujímať takáto otázka: Ako dobrý odhad x musíme mať na začiatku, aby došlo ku konvergencii? A začnime rovno ťažšou úlohou - skúsme vyriešiť pôvodnú celočíselnú rekurenciu
$$
a_n = a_{n-1} + 2b_{n-1} \\
b_n = a_{n-1} + b_{n-1}
$$
a chceme výrazy pre $a_n, b_n$ v termínoch $n$ a počiatočných podmienok $a_0, b_0$. Toto je dosť častá úloha a riešenie sa dá nájsť jednoducho:

Všimneme si, že $a_n = b_n + b_{n-1}$ a dosadíme do druhého vzťahu: 
$$
b_n = b_{n-1} + b_{n-2} + b_{n-1} = 2b_{n-1} + b_{n-2}
$$
takže máme rekurziu vyjdrenú čísto v termínoch $b$:
$$
b_n = 2b_{n-1} + b_{n-2} \\
a_n = b_{n} + b_{n-1}
$$
Riešenie rekurzie pre $b$ nájdeme ľahko: $b_n = q^n$ a po dosadení dostaneme kvadratickú rovnicu:
$$
q^n = 2q^{n-1} + q^{n-2} \\
q^2 - 2q - 1 = 0 \\
q_{12} = 1 \pm \sqrt{2}
$$
Odtiaľ 
$$
b_n = C_1q_1^n + C_2q_2^n \\
a_n = C_1q_1^n + C_2q_2^n + C_1q_1^{n-1} + C_2q_2^{n-1} = C_1(1-q_2)q_1^n + C_2(1-q_1)q_2^n
$$
kde sme využili, že $q_1q_2=-1$ a teda
$$
\frac{1}{q_1} = -q_2 \quad \frac{1}{q_2} = -q_1 \\
$$
Teraz použijeme počiatočné podmienky a vypočítame konštanty $C_1, C_2$:
$$
a_0 = C_1\sqrt{2} - C_2\sqrt{2} \\
b_0 = C_1 + C_2
$$
Vydelíme prvú rovnicu $\sqrt{2}$ a potom rovnice sčítame a odčítame:
$$
C_1 = \frac{1}{2}\left(b_0 + \frac{a_0}{\sqrt{2}}\right) \\
C_2 = \frac{1}{2}\left(b_0 - \frac{a_0}{\sqrt{2}}\right)
$$
Riešenie rekurzie teda vyzerá takto:
$$
a_n = \frac{\sqrt{2}}{2}\left(b_0 + \frac{a_0}{\sqrt{2}}\right)(1+\sqrt{2})^n - \frac{\sqrt{2}}{2}\left(b_0 - \frac{a_0}{\sqrt{2}}\right)(1-\sqrt{2})^n \\
b_n = \frac{1}{2}\left(b_0 + \frac{a_0}{\sqrt{2}}\right)(1+\sqrt{2})^n + \frac{1}{2}\left(b_0 - \frac{a_0}{\sqrt{2}}\right)(1-\sqrt{2})^n
$$
To vyzerá odstrašujúco, a jediná vec, na ktorú tieto vzťahy využijeme, bude zistenie asymptotického chovania pomeru $a_n / b_n$. Pre tento účel upravíme vzťahy pre $a_n$ a $b_n$ takto:
$$
a_n = \frac{\sqrt{2}}{2}\left(b_0 + \frac{a_0}{\sqrt{2}}\right)q_1^n \left[1 - \frac{\sqrt{2}b_0 - a_0}{\sqrt{2}b_0 + a_0}\left(\frac{q_2}{q_1}\right)^n \right] \\
b_n = \frac{1}{2}\left(b_0 + \frac{a_0}{\sqrt{2}}\right)q_1^n \left[1 + \frac{\sqrt{2}b_0 - a_0}{\sqrt{2}b_0 + a_0}\left(\frac{q_2}{q_1}\right)^n \right] 
$$
Upravme, aby sme mali zrozumiteľný vzťah:
$$
M \equiv \frac{\sqrt{2}b_0 - a_0}{\sqrt{2}b_0 + a_0} = - \frac{\frac{a_0}{b_0}-\sqrt{2}}{\frac{a_0}{b_0}+\sqrt{2}} \\
\frac{q_2}{q_1} = \frac{1-\sqrt{2}}{1+\sqrt{2}} = \frac{(1-\sqrt{2})^2}{(1+\sqrt{2})(1-\sqrt{2})} = 2\sqrt{2}-3 \\
\frac{a_n}{b_n} = \sqrt{2} \frac{1 - M(2\sqrt{2}-3)^n}{1 + M(2\sqrt{2}-3)^n}
$$
Jediný člen, obsahujúci počiatočné podmienky, je M. Pretože $2\sqrt{2}-3 \approx -0.172$, budú členy s M v čitateli i menovateli s rastúcim $n$ veľmi rýchlo ubúdať, a to pre ľubovoľné M a celý zlomok bude rýchlo konvergovať k 1. Inak povedané, algoritmus je veľmi robustný vzhľadom k počiatočným podmienkam. Pre $a_0=3, b_0=2$ dostávame $M \approx -0.0294$ a rovnaké čísla ako v predchádzajúcej tabuľke:

| $k$  | $a/b$    | $a/b - \sqrt{2}$ |
| ---- | -------- | ---------------- |
| 0    | 1.5      | 0.085786         |
| 1    | 1.4      | -0.01421         |
| 2    | 1.416667 | 0.002453         |
| 3    | 1.413793 | -0.00042         |
| 4    | 1.414286 | 7.22E-05         |
| 5    | 1.414201 | -1.2E-05         |

čo sú rovnaké čísla ako v prvej tabuľke. 

Táto metóda nie je dobrou metódou na počítanie druhej odmocniny z 2, pretože konverguje pomerne pomaly, ale poskytuje nám *_racionálnu aproximáciu_* odmocniny z 2, čo môže byť užitočná vec pri počítaní na platformách, kde nemáme k dispozícii čísla s plávajúcou desatinnou čiarkou a racionálne čísla reprezentujeme ako dvojice celých čísel. 

**Ešte jeden dôkaz iracionality $\sqrt{2}$**

Predpokladajme, že  existujú celé čísla $a, b$ tak, že $a/b=\sqrt{2}$.  Pre $a, b$ bude teda platiť  $a^2=2b^2$ a pozrime sa na posledné číslice druhých mocnín celých čísel *_modulo_* 3, teda na zvyšok po delení poslednej číslice troma:

| i         | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    |
| --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **i % 3** | 0    | 1    | 1    | 0    | 1    | 1    | 0    | 1    | 1    | 0    |

Ako vidno, posledná číslica úplných štvorcov modulo 3 je 0 alebo 1. Vo vzťahu $a^2 = 2b^2$ je teda posledná číslica na ľavej strane 0 alebo 1, zatiaľ čo posledná číslica na pravej strane musí byť 0 alebo 2. Jediná možnosť, ako môže nastať rovnosť je, aby posledná číslica naľavo i napravo bola 0. To je ale neprípustné, pretože by to znamenalo, že čísla $a, b $ sú obe deliteľné 3, hoci sme vychádzali z predpokladu, že sú nesúdeliteľné. 

Takto môžeme dokázať, že ak by bola odmocnina z 2 racionálna, boli by obe čísla $a,b$ deliteľné okrem 3 aj ľubovoľným iným prvočíslom. Tento druh dôkazu využívajúci štúdium vzťahu modulo nejaké číslo je veľmi častý a veľmi efektívny. 

**Sínusová veta**

Sínusová veta je ľahko dokázateľný vzťah pre trojuholníky. Majme trojuholník ABC s vnútornými uhlami $\alpha, \beta, \gamma$ po rade pri vrcholoch $A, B, C$, a stranami $a, b, c$ protiľahlým vrcholom $A, B, C$. Nech $r$ je polomer kružnice, opísanej trojuholníku ABC. Potom platí
$$
\frac{a}{\sin{\alpha}} = \frac{b}{\sin{\beta}} = \frac{c}{\sin{\gamma}} = 2r
$$
*_Dôkaz_*: 

![Untitled](img\Sinusova_veta.png)

Na obrázku hore máme trojuholník ABC  Stredové a obvodové uhly (Euklides): uhol BSC je dvojnásobkom uhla BAC $=\alpha$. Nech P leží uprostred strany $BC=a$.  Trojuholník BPS je pravouhlý a zdefinície 
$$
\sin{\alpha} = \frac{a/2}{r} \implies \frac{a}{\sin{\alpha}} = 2r
$$
Dôkaz je mierne odlišný, keď je uhol $\alpha$ tupý , ako ukazuje nasledujúci obrázok. Použijeme doplnkové uhly k $\alpha$ a z príslušných pravouhlých trojuholníkov dostaneme sínusovú vetu pre ne. Pretože platí $\sin{(90°-\alpha)} = \sin{\alpha}$, máme dokazované tvrdenie. 

<img src="img\Sinusova_veta2.png" alt="Untitled" style="zoom:36%;" />

Dokázali sme "tretinu" sínusovej vety a ďalšie dve tretiny dokážeme analogicky. 

*_Alternatívny dôkaz_*

Pre jednoduchý dôkaz sínusovej vety "bez pravej strany " vystačíme s jednoduchou konštrukciou:

![Untitled](img\Sinusova_veta3.png)

Stačí porovnať dva vzťahy pre výšku $v_b$:
$$
v_b = c\sin{\alpha} = a\sin{\gamma} \implies \frac{c}{\sin{\gamma}} = \frac{a}{\sin{\alpha}}
$$
atd. Tento dôkaz dobre funguje pre ostré i tupé uhly. 





---

## 3. Geometria

#### Veta o skrížených tetivách

Začneme s pomocným tvrdením, ktoré nám umožní vhľad do zvláštnych vlastností štvoruholníkov, vpísaných do kružnice. 

<img src="img\Xchords_01.png" alt="Xchords_1" style="zoom:20%;" />

Majme kružnicu a dve tetivy AB, CD, pretínajúce sa v bode O. Potom platí
$$
AO \cdot OB = CO \cdot OD
$$
**Dôkaz**

<img src="img\Xchords_2.png" alt="Xchords_2" style="zoom:33%;" />

Dokážeme, že trojuholníky AOC a DOB sú podobné. 

- Uhly $\alpha$ sú obvodové uhly, prislúchajúce oblúku BC, a sú preto rovnaké.
- Uhly $\beta$ sú obvodové uhly, prislúchajúce oblúku AD, a sú preto rovnaké.
- Uhly $\gamma$ sú vrcholové uhly okolo priesečníka AB a CD, a sú preto rovnaké. 

Z podobnosti trojuholníkov vyplýva
$$
\frac{AO}{OC} = \frac{DO}{OB} \implies AO \cdot OB = DO \cdot OC
$$


#### Ptolemaiova veta a súčtové vzorce pre sínus a kosínus

.Ptolemaiova veta je silnejšie tvrdenie ako Pytagorova veta: Pre štvoruholník ABCD vpísaný v kružnici platí


​		![Ptolemy_equality.svg](img\Ptolemy_equality.svg.png)
$$
|AB||CD| + |AD||BC| = |AD||BC|
$$
V skutočnosti platí ešte silnejšie tvrdenie, nazývané niekedy Ptolemaiova nerovnosť: Pre ľubovoľný konvexný štvoruholník ABCD platí
$$
|AB||CD| + |AD||BC| \ge |AD||BC|
$$
pričom rovnosť nastáva iba ak je štvoruholník ABCD vpísaný v kružnici alebo keď body A, B, C, D ležia na jednej priamke. 

Naučme sa používať Ptolemaiovu vetu na nasledujúcom príklade:

Vezmime štvoruholník ABCD vpísaný do kružnice o polomere $r = 1/2$ tak, že stred kružnice leží na uhlopriečke AC. Použijeme Tálesovu či Euklidovu vetu o stredových a obvodových uhloch a sínusovú vetu, aby sme vypočítali všetky strany a uhlopriečky, potrebné do Ptolemaiovej vety:

![Untitled](img\Ptolemy_Sum.png)
$$
|AC| = 1 \\
|\angle ABC| = |\angle ADC| = 90° \\
|BC| = \sin{\alpha} \\
|DC| = \sin{\beta} \\
|AB| = \sin{(90° - \alpha)} = \cos{\alpha} \\
|AD| = \sin{(90° - \beta)} = \cos{\beta} \\
|BD| = \sin{(\alpha+\beta)}
$$
Ešte sme tu použili jednu vec, ktorú sme preberali dávnejšie:

<img src="img\sin_cos.png" alt="sin_cos" style="zoom: 25%;" />
$$
\cos{\alpha} = sin{(90° - \alpha)}, \quad \sin{\alpha} = cos{(90° - \alpha)}
$$
Z Ptolemaiovej vety dostaneme
$$
|AC||BD| = |AB||CD| + |BC||AD| \\
1\cdot \sin{(\alpha+\beta)} = \cos{\alpha} \cdot \sin{\beta} + \sin{\alpha} \cdot \cos{\beta}
$$
teda 
$$
\sin{(\alpha +\beta)} = \sin{\alpha} \cdot \cos{\beta} + \cos{\alpha} \cdot \sin{\beta}
$$
čo je univerzálne platný súčtový vzorec pre sínus. 

Rovnako môžeme dokázať rozdielový vzorec, stačí trocha pohýbať s obrázkom:

![Untitled](img\Ptolemy_diff.png)

Postupujeme rovnako ako v predchádzajúcom prípade - vypočítame všetky dĺžky a dosadíme do Ptolemaiovej vety:
$$
|AD| = 1 \\
|\angle ACD| = |\angle ABD| = 90° \\
|BD| = \sin{\alpha} \\
|CD| = \sin{\beta} \\
|AB| = \sin{(90° - \alpha)} = \cos{\alpha} \\
|AC| = \sin{(90° - \beta)} = \cos{\beta} \\
|BC| = \sin{(\alpha - \beta)}
$$
a dosadíme do Ptolemaiovej vety:
$$
|AC||BD| = |AB||CD| + |BC||AD| \\
\cos{\beta} \cdot \sin{\alpha} = \cos{\alpha} \cdot \sin{\beta} + \sin{(\alpha - \beta)} \cdot 1
$$
teda 
$$
\sin{(\alpha - \beta)} = \sin{\alpha} \cdot \cos{\beta}  - \cos{\alpha} \cdot \sin{\beta}
$$
ďalší základný vzťah pre goniometrické funkcie.  Z týchto vzťahov ľahko dostaneme príslušné vzťahy pre kosinus:
$$
\cos{(\alpha + \beta)} = \sin{(90° - \alpha - \beta)} = \sin{((90° - \alpha) - \beta)} \\ 
= \sin{(90° - \alpha)} \cdot \cos{\beta}  - \cos{(90° - \alpha)} \cdot \sin{\beta} \\
= \cos{\alpha} \cdot \cos{\beta}  - \sin{\alpha} \cdot \sin{\beta}
$$
a podobne môžeme dokázať aj rozdielový vzorec pre kosínus. 

#### Dôkaz Ptolemaiovej vety

Základný jednoduchý dôkaz: Máme štvoruholník ABCD vpísaný v kružnici. Na uhlopriečke BD nájdeme bod M tak, aby $|\angle ACB|=|\angle MCD|$ (na obrázku označené ako $\alpha$). Uhly $\angle BAC$ a $\angle BDC$ (označené ako $\delta$ sú rovnaké, pretože sú to obvodové uhly zodpovedajúce rovnakej tetive BC.  Pretože trojuholníky ABC a DMC majú rovnaké dva uhly, sú si podobné, a teda platí $CD/MD = AC/AB$, resp. 
$$
AB\cdot CD = AC \cdot MD
$$
Rovnaké sú aj uhly $\angle BCM$ a $\angle ACD$ (oba sú rovné $\alpha + \epsilon$). Ďalej uhly $\angle CAD$ a $\angle CBM$ (označené ako $\eta$ sú rovnaké, pretože sú to obvodové uhly zodpovedajúce rovnakej tetive DC Preto aj trojuholníky BCM a ACD sú si podobné a teda $BC/BM = AC/AD$ čiže 
$$
AD \cdot BC = AC \cdot BM
$$
. Pretože $BM + MD = BD$, dostávame sčítaním oboch vzťahov Ptolemaiovu vetu

![Untitled](img\PtolemyProof.png)
$$
AB \cdot CD + AD \cdot BC = AD \cdot BC
$$

---



## 4. Domáca úloha (nová)

Dnes budú iba dve úlohy, pretože geometria mi príde ťažšia. 

1. Majme rovnostranný trojuholník $A_1A_2A_3$ Nech P je ľubovoľný bod na kružnici, opísanej tomuto trojuholníku. Dokážte, že spomedzi spojníc $PA_1, PA_2, PA_3$ je súčet dvoch kratších rovný najdlhšej. 

<img src="img\from_ptolemy.gif" alt="from_ptolemy" style="zoom:150%;" />

2. V kruhu máme dve tetivy AB a CD, a na nich body P, Q. Dĺžky a vzdialenosti sú vyznačené na obrázku a úloha je vypočítať dĺžku tetivy, ktorá vznikne predĺžením úsečky PQ k hraniciam kružnice. 

<img src="img\ExercisePQ.png" alt="image-20230830232443871" style="zoom:120%;" />

## 5. Program na budúci týždeň

- to, čo sme dnes nestihli (lebo som toho prichystal dosť veľa)
- kosínusová veta
- zobrazenia: involúcia, izometria, zrkadlenie
