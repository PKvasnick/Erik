## Hodina 7. júla 2023

Program:

1. Domáca úloha: zostávajúci príklad z prijímačkového testu a príklady z 1. lekcie
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli.
3. Rôzne postupnosti a číselné rady
4. Domáca úloha (nová)

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Telekonferencia** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

### 1. Domáca úloha

#### Zostávajúci prijímačkový príklad

![image-20230701151743850](img\image-20230701151743850.png)

Vieme, že jedno riešenie je X=10, Y=3. Treba nájsť iné riešenie. Jedno riešenie uvádzam na konci.

#### Druhá časť domácej úlohy boli ešte stále tieto príklady:

**Príklad 1**

Postupnosť začína číslami 1, 3, 6, 10. Doplň ďalšie členy. 

Ako u väčšiny príkladov, ktoré budeme riešiť, nezaujíma nás až tak veľmi konkrétny príklad, ale stratégie a postupy, ktoré sa dajú použiť. 

**Príklad 2**

Platí
$$
\sqrt{25} = 2 + 5 - 2 \quad (\textrm{odčítame dvojku, pretože máme druhú odmocninu}) \\
= 5\\
\sqrt{64} = 6 + 4 - 2 = 8\\
\sqrt{196} = 1 + 9 + 6 - 2 = 14\\
\sqrt{289} = 2 + 8 + 9 - 2 = 17
$$
Je toto nová fantastická finta na odmocňovanie? Ako to funguje? Pre aké najväčšie číslo to môže platiť?

**Príklad 3**

Majme postupnosť $x_{n+1} = a\cdot x_n(1-x_n)$. Ako sa správa pre rôzne $a$?

### 2. Príklady

Toto sú sondovacie príklady, ktoré slúžia pre všeobecné osvietenie a chcem tiež pomocou nich zistiť, čomu ešte sa treba venovať. 

**1. Príklad na deliteľnosť**

**Tvrdenie** Všetky čísla tvaru ABABAB sú deliteľné 37.

Vysvetlivka: A, B sú prirodzené čísla také, že 0 < A ≤ 9, 0 ≤ B ≤ 9. 

Dôkaz?

- Ako to vlastne budeme dokazovať?
- Čo znamená, že tvrdenie dokážeme?

**2. Exponenciálna rovnica**

Nájdi všetky x, ktoré sú riešeniami rovnice
$$
2^{5x} = 3^{2-x}
$$
**3. Kvadratická rovnica**

Nech M, N sú korene kvadratickej rovnice
$$
x^2 + 6x + 4 =0.
$$
Vypočítajte $M^2 + N^2$.

---

### 3. Všelijaké číselné rady

#### Aritmetický rad

$$
a_n = a_0 + nd, \quad n = 0, 1, \dots
$$

Aký je súčet prvých n členov? inak povedané, čomu sa rovná
$$
S_n = a_0 + a_1 + ... a_{n-1}
$$


**Gaussova finta:**
$$
S_n =& a_0 + 0d &+ a_0 + 1d &+ \dots &+a_0 + (n-1)d \\
S_n =& a_0 + (n-1)d &+ a_0 + (n-2)d &+ \dots &+ a_0 +0d \\
2S_n =& 2a_0 + (n-1)d &+2a_0 + (n-1)d &+ \dots &+ 2a_0 + (n-1)d
$$
a posledný súčet ide sčítať ľahko, pretože v ňom máme samé rovnaké členy.:
$$
2S_n = n(2a_0+(n-1)d) \\
S_n = na_0 + \frac{n(n-1)}{2}d
$$
**Príklad**

Pre rad $S_N^{(1)} = 1+2+\dots + N$ môžeme položiť $a_0 = 0,\, d=1, \, N=n+1$, a dostaneme známy vzťah
$$
S_N^{(1)} = \frac{N(N+1)}{2}
$$

---

 #### Mocninné rady

Na rad $S_n^{(1)} = 1 + 2 + \dots + n$ sa môžeme pozerať aj ako na špeciálny prípad radu 
$$
S_n^{(k)} = 1^k + 2^k + \dots + n^k
$$
Vieme, že $S_n^{(1)}$ je $n(n+1)/2$, $S_n^{(0)}$ bude jednoducho $n$, a ukážeme si recept, ako postupne dopočítať všetky ostatné $S_n^{(k)}$.

Ukážeme si postup pre  $S_n^{(2)} = 1^2 + 2^2 + \dots + n^2$.  Gaussova finta tu nefunguje, tak skúsime niečo iné. Napíšeme
$$
k^3 - (k-1)^3 = k^3 - k^3 + 3k^2 - 3k + 1 = 3k^2 - 3k + 1
$$
a vypíšeme rovnice pre $k$ od 1 do $n$:
$$
1^2 &-& 0^2 &=& 3\cdot 1^2 &-& 3\cdot 1 + 1 \\
2^2 &-& 1^2 &=& 3\cdot 2^2 &-& 3\cdot 2 + 1 \\
3^2 &-& 2^2 &=& 3\cdot 3^2 &-& 3\cdot 3 + 1 \\
\dots \\
n^2 &-& (n-1)^2 &=& 3\cdot n^2 &-& 3\cdot n + 1 \\
$$
Teraz tieto rovnice sčítame. Naľavo nám ostane iba $n^3$, zatiaľ čo napravo dostaneme lineárnu kombináciu súčtov $S_n^{(2)}$,  $S_n^{(1)}$ a $S_n^{(0)}$.  Z nich súčet $S_n^{(2)}$ je to, čo chceme vypočítať, takže ho zo vzťahu vyjadríme:
$$
n^3 = 3S_n^{(2)} - 3S_n^{(1)} + S_n^{(0)} \\
S_n^{(2)} = \frac{1}{3}\left(n^3 + 3\frac{n(n+1)}{2} - n \right) \\
= \frac{n}{6}\left(2n^2 + 3n + 1 \right) = \frac{n(n+1)(2n+1)}{6}
$$
Podobne, ak vypíšeme rovnice pre $k^4 - (k-1)^4$ od 1 do n, môžeme odvodiť vzťah pre $S_n^{(4)}$:
$$
S_n^{(4)} = \left( \frac{n(n+1}{2}\right)^2
$$

---

#### Harmonický rad

Harmonický rad je prípad mocninného radu pre k = -1:
$$
H_n = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} +\frac{1}{6} +\frac{1}{7} +\frac{1}{8} +\dots + \frac{1}{n}
$$
Tento rad nevieme presne sčítať, ale vieme, že pre veľké $n$ súčet $H_n$ neohraničene rastie. Dôkaz: uvažujme rrad
$$
G_n = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} +\frac{1}{8} +\frac{1}{8} +\frac{1}{8} +\dots + \frac{1}{2^{\lceil \log_2 n \rceil}}
$$
ktorý vznikne tak, že každé k v menovateli harmonického radu nahradíme najbližšou väčšou mocninou 2, teda n v menovateli nahradíme $2^{\lceil \log_2 n \rceil}$, kde $\lceil x \rceil$ označuje najmenšie celé číslo väčšie ako $x$ .

Každý člen radu G je menší alebo rovný príslušnému členu harmonického radu, a teda $G_n \le H_n$. Rad G ale vieme ľahko sčítať a ukázať, že je je divergentný, teda jeho súčet pre rastúce n neohraničene rastie:
$$
G_n = 1 + \frac{1}{2} + \left(\frac{1}{4} + \frac{1}{4}\right) + \left(\frac{1}{8} +\frac{1}{8} +\frac{1}{8} +\frac{1}{8}\right) +\dots  \\
= 1 + \frac{1}{2} + \frac{1}{2} + \dots = 1 + \frac{\lceil \log_2 n \rceil}{2}
$$
kde neriešime niekoľko prípadne chýbajúcich členov na konci radu. Zjavne vidíme, že rad G je divergentný a divergentný musí byť aj harmonický rad. 

Je známe, že pre veľké n dobre platí priblížný vzťah
$$
H_n = \ln n + \gamma + O/1/n)
$$
kde $\gamma = 0.577\dots$ je Eulerova-Mascheroniho konštanta a O(1/n) znamená, že ďalšie opravné členy budú rádu 1/n a vyššieho, teda pre veľké n zanedbateľné. 

Čo tento výraz znamená? Znamená, že $H_n$ s rastúcim n neohraničene rastie do nekonečna, ale rastie nesmierne pomaly.  

**Alternujúci harmonický rad**

Rad 
$$
A_n = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} -\frac{1}{6} +\frac{1}{7} -\frac{1}{8} +\dots + (-1)^{n+1}\frac{1}{n}
$$
sa od harmonického radu líši striedajúcimi sa znamienkami. Tento rad konverguje a pre rastúce n sa hodnota súčtu blíži k $\ln 2$.

#### Ďalšie mocninné rady so záporným k

Nekonečný rad
$$
S_{\infty}^{-2} \equiv 1 + \frac{1}{2^2} + \frac{1}{3^2} + \frac{1}{4^2} + \dots = \sum_{n=1}^{\infty} \frac{1}{n^2}
$$
má súčet $\pi^2/6$. Tento výsledok pochádza od Leonarda Eulera, a je prekvapujúci tým, že v ňom figuruje $\pi$. Okrem toho nie je úplne ľahké ho získať. 

Čo môžeme ukázať ľahko je, že súčet radu existuje a nachádza sa medzi 1 a 2. 

Uvažujme "teleskopický" rad 
$$
S_T \equiv \frac{1}{1\cdot 2} + \frac{1}{2\cdot 3} + \frac{1}{3\cdot 4} + \dots = \sum_{n=1}^{\infty} \frac{1}{n(n+1)}
$$
Tento rad sa dá prekvapujúco ľahko sčítať. Stačí použiť jednoduchú fintu, ktorá sa normálne vyučuje až na vysokej škole v kurze matematickej analýzy - rozklad na parciálne zlomky:

Pokúsme sa výraz $\frac{1}{n(n+1)}$ vyjadriť v tvare $\frac{A}{n} + \frac{B}{n+1}$:
$$
\frac{1}{n(n+1)} = \frac{A}{n} + \frac{B}{n+1} \quad |\cdot n(n+1) \\
1 = A(n+1) + Bn
$$
Toto vyzerá ako jedna rovnica pre dve neznáme A a B. Pretože ale táto rovnosť má platiť pre všetky n=1, 2, ..,  sú to v skutočnosti dve rovnice - pre členy obsahujúce n a pre konštantné členy:
$$
1 = A(n+1) + Bn = (A+B)n + A
$$
Člen pri n musí byť nula a konštantný člen musí byť 1, teda $A = 1, B = -1$ a 
$$
\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}
$$
čo možno ľahko overiť  úpravou pravej strany.  Použitím tohto vzťahu možno nekonečný rad $S_T$ prepísať do tvaru, v ktorom sa dá triviálne sčítať:
$$
S_T = \sum_{n=1}^{\infty} \frac{1}{n(n+1)} = \sum_{n=1}^{\infty} \left( \frac{1}{n} - \frac{1}{n+1} \right) \\
= 1 - \frac{1}{2} +\frac{1}{2} - \frac{1}{3} + \frac{1}{3} - \frac{1}{4} +\frac{1}{4} \dots = 1
$$
Tento rad sa vyskytuje celkom často. Teraz pomocou neho ukážeme, že rad $S_{\infty}^{-2}$ konverguje k hodnote medzi 1 a 2:
$$
\frac{1}{2^2} \le \frac{1}{1 \cdot 2},\\
\frac{1}{3^2} \le \frac{1}{2 \cdot 3},\\
\frac{1}{4^2} \le \frac{1}{3 \cdot 4}, \\
\vdots
$$
a teda 
$$
1 + \frac{1}{2^2} + \frac{1}{3^2} + \frac{1}{4^2} \dots \le 1 + \frac{1}{1 \cdot 2} + \frac{1}{2 \cdot 3} + \frac{1}{3 \cdot 4} + \dots = 2
$$
čo sme si predsavzali ukázať. 

---

#### Geometrický rad:

$$
a_n = a_0 q^n
$$

Súčet: 
$$
S_n = a_0 + a_0q + a_0q^2 + \dots + a_0q^{n-1}
$$
ľahko nájdeme, ak si všimneme, že rad čiastočne obsahuje sám seba:
$$
S_n = a_0 + a_0q + a_0q^2 + \dots + a_0q^{n-1} \\
= a_0 + q(a_0 + a_0q + a_0q^2 + \dots + a_0q^{n-2}) = a_0 + qS_{n-1}
$$
a pretože zároveň platí $S_{n} = S_{n-1} + a_0q^{n-1}$, môžeme ľahko vyjadriť $S_n$:
$$
S_n = a_0 + q(S_n - a_0q^{n-1}) \\
S_n = a_0 + qS_n - a_0q^n \\
S_n(1-q) = a_0(1-q^n) \\
S_n = a_0\frac{1-q^n}{1-q}
$$
Pre n rastúce do nekonečna má rad súčet pre $|q|\lt 1$, a tento súčet je 
$$
S = \frac{1}{1-q}
$$
**Príklad**: Pre $a_0=1,\;q=1/2$  máme
$$
S = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \dots = \frac{1}{1 - \frac{1}{2}} = 2
$$
**Príklad**: Pre $q=-1/2$ máme
$$
S = 1 - \frac{1}{2} + \frac{1}{4} - \frac{1}{8} + \frac{1}{16} - \dots = \frac{1}{1 + \frac{1}{2}} = \frac{2}{3}
$$

---

## Domáca úloha

1. Jozef si z banky požičal 500 000 eur na hypotéku s úrokom 2% na tridsať rokov. Vypočítaj mesačnú splátku. 
2. Zenón naháňa korytnačku. Keď sa rozbehol, bola 100 m pred ním. Tých 100 metrov prebehol Zenón za 12.5 sekundy, ale Keď dobehol, bola 20 m pred ním. Keď prebehol týchto 20 m, bola 4 m pred ním, keď prebehol tieto 4 metre, bola ešte stále 80 cm pred ním. Zenón si začal zúfať, že korytnačku nikdy nedobehne, pretože kým dobehne tam, kde bola pred chvíľou, vždy o kúsok popolezie ďalej. Dohoní Zenón korytnačku alebo nie, a kedy?
3. Pán Brown prišiel z krčmy k domovým dverám, našiel vo vrecku kľúče, a chce si odomknúť. Na zväzku má 10 kľúčov, ale v tej tme vyzerajú všetky rovnako. Skúsi jeden kľúč, a keď to nie je správny, vráti ho do zväzku a zasa náhodne vyberie kľúč, a takto postupuje ďalej, kým nenájde správny kľúč. 
   - Pri koľkom pokuse má pán Brown najväčšiu šancu nájsť správny kľúč?
   - Koľko kľúčov v priemere musí vyskúšať, kým nájde ten správny?

---

### Riešenie domácej úlohy

Toto je iný prístup, ako efektívne riešiť úlohu o plochách X a Y.

Začali sme tým, že sme si označili úseky a, b, c, d, e, a vieme pre ne získať hromadu rovníc z údajov v obrázku. Treba skúsiť vyjadriť X, Y a získať nejaký vzťah medzi nimi. 

Skúsme rýchlejšie riešenie:

Predpokladáme, že riešenie X=10, Y=3 pochádza z nejakého jednoduchého tvaru oblastí X, Y - konkrétne, že budú mať celočíselné rozmery. Potom - v označení a, b, atd, môžeme predpokladať a=2, c=5, b=3, d=1, e=2, teda náš predpoklad dáva zmysel. 

Slušné riešenie by mohlo vzniknúť, keby sme vzali X=12 a nechali a=2. Potom c=6, b=2.5, d+e=3, e=2.4, takže d=0.6 a Y=0,6 x 2.5 = 1.5. 

Teda iné riešenie je X=12, Y=1.5. 

Podobne môžeme skúsiť X=12, a=3. Potom c=4, b=3.75. Ďalej d+e=2, e=6/3.75=1.6, d=0.4, Y=0.4 x 3.75 = 1.5. Toto dáva rovnaké riešenie. 

Ešte skúsme riešenie s iným X, napr. X=9. Položme a=3, potom c=3, b=15/3=5, d+e = 6/3 = 2, e=6/5=1.2, d= 0.8, Y=0.8 x 5 = 4.

Teda ešte ďalšie riešenie je X=9, Y=4.

---

### Kuriozita: Balenie pomarančov v osemrozmernom priestore

<img src="img\F7960A68-2631-4B11-99F139DAAFD92CF4_source.webp" alt="F7960A68-2631-4B11-99F139DAAFD92CF4_source" style="zoom: 67%;" />

Tento rok [Maryna Viazovska ukázala, ako najefektívnejšie usporiadať gule v osemrozmernom priestore](https://www.scientificamerican.com/article/multidimensional-sphere-packing-solutions-stack-up-as-a-major-mathematical-breakthrough/). Môže sa zdať, že to je abstraktná záležitosť, ale v skutočnosti má veľmi praktické použitie. 

- Jednorozmernú priamku môžeme úplne pokryť jednorozmernými guľami (úsečkami jednotkovej dĺžky)
- rovinu môžeme pokryť kruhmi tak, že ostane 9% voľnej plochy
- priestor môžeme pokryť guľami tak, že otstane 26% voľného priestoru
- vo vyšších rozmeroch objem, ktorý zaberajú najefektívnejšie usporiadané gule, rýchlo klesá.

**Praktický význam: algoritmy najbližšieho suseda (nearest neighbour**

Veľa úloh strjového učenia (machine learning) spočíva v tomto: Máme nejakú množnu známych hodnôt $X$ pre niekoľko kombinácií parametrov $\{p_1, p_2, \dots, p_n\} \in P$. Úloha je nájsť hodnotu pre inú kombináciu parametrov.  Najjednoduchší spôsob je nájsť najbližší bod v n-rozmernom priestore parametrov P a použiť hodnotu X z tohto bodu. Iný spôsob je použiť n najbližších známych bodov v priestore P a vypočítať vážený priemer pre nový bod. V oboch týchto prípadoch vidíme, že s rastom dimenzie priestoru P budú takéto metódy fungovať stále horšie - budeme potrebovať nerealisticky veľké počty "známych" bodov, aby sme vedeli odhadnúť hodnotu X v ľubovoľnom inom bode - teda aby sme okolo náhodne vybraného bodu v priestore P vedeli nájsť dostatočne blízky dátový bod, pre ktorý poznáme X.

![actually received](img\actually received.webp)

Tento obrázok dobre ilustruje, čo som písal vyššie, ale v skutočnosti má ilustrovať ďalšie dôležité použitie poznatkov o najefektívnejšom pokrytí priestoru guľami.

Viac v https://blogs.scientificamerican.com/roots-of-unity/why-you-should-care-about-high-dimensional-sphere-packing/



