## Hodina 14. júla 2023

Program:

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli.
3. Dôkazy. Matematická indukcia
4. Domáca úloha (nová)

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Telekonferencia** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

### 1. Domáca úloha

1. > Jozef si z banky požičal 500 000 eur na hypotéku s úrokom 2.4% na tridsať rokov. Vypočítaj mesačnú splátku. 

**Riešenie**

Označme q mesačný úrok, teda  2.4% p.a./12 = 0,2% mesačne.  Označme $A_n$ nesplatenú istinu v n-tom mesiaci, $a_n$ istinu splatenú v n-tej mesačnej splátke,  $u_n$ úroky splatné v n-tej mesačnej splátke, Označme mesačnú splátku $m$, splátka je fixná a platí $m = a_n + u_n$, teda $a_n = m - u_n$. Úroky sa počítajú z nesplatenej istiny, $u_n = qA_n$. V nasledujúcom mesiaci bude istina $A_{n+1} = A_n - a_n = A_n - m + u_n = A_n(1+q) - m$, a pre úroky a istinu, zaplatenú v n+1-vej splátke platia rovnaké vzťahy. Vzťah 
$$
A_0 = A,\quad A_{n+1}=A_n(1+q) - m,\, n = 1, 2, \dots N
$$
kde A je 500 000 euro,  N = 24 x 30 = 720 je počet mesačných splátok,  je hlavný vzťah pre výpočet mesačnej splátky m. Potrebujeme vypočítať m tak, aby $A_{270}$ bolo 0. 

Čo vieme povedať o m?  Aby riešenie existovalo, musí platiť $m \gt qA \approx 1000$ eur, teda mesačná splátka musí byť väčšia ako úroky za prvý mesiac - inak by nesplatená čiastka rástla a nie klesala. 

Existuje stará perzská metóda pre odhad mesačnej splátky, ktorá funguje takto (toto je originálny článok: https://www.maa.org/sites/default/files/Peyman_Milanfar45123.pdf):
$$
(\textrm{Mesačná splátka}) \approx \frac{(\textrm{Istina + Úrok})}{(\textrm{počet mesiacov})} \\
(\textrm{Úrok}) = \frac{1}{2} (\textrm{Istina})\times (\textrm{počet rokov}) \times (\textrm{ročný úrok})
$$
Dosadením vypočítame $\textrm{Úrok} \approx 360 000$ eur, $\textrm{Mesačná splátka} \approx 1194,44$ eur. 

Presné riešenie sa samozrejme ľahko nájde v ktorejkoľvek finančnej príručke:
$$
m = \frac{q(1+q)^N}{(1+q)^N-1}A
$$
Toto po dosadení dáva mesačnú splátku 1311.08 eur. 

Samozrejme nás bude najviac zaujímať, ako nájsť výraz pre n-tý člen postupnosti $A_n$. Z rekurentného vzťahu vidíme, že ide o geometricko-aritmetický rad. Skúsme sa pozrieť na niekoľko prvých členov postupnosti:
$$
A_0 = A \\
A_1 = A(1+q) - m \\
A_2 = A(1+q)^2 - m(1+q) - m \\
A_3 = A(1+q)^3 - m(1+q)^2 - m(1+q) - m \\
\vdots \\
A_n = A(1+q)^n - m(1 + (1+q) + (1+q)^2 + \dots + (1+q)^{n-1})
$$
Úpravou dostaneme
$$
A_n = A(1+q)^n - m \frac{1-(1+q)^n}{1-1-q} = A(1+q)^n - m \frac{(1+q)^n - 1}{q}
$$
Nesplatená istina po n-tej splátke musí byť 0, a odtiaľ môžeme vyjadriť mesačnú splátku:
$$
0 = A(1+q)^N - m \frac{(1+q)^N - 1}{q} \\
m = \frac{q(1+q)^N A}{(1+q)^N - 1}
$$
čo je presne známy vzťah. 

2. > Zenón naháňa korytnačku. Keď sa rozbehol, bola 100 m pred ním. Tých 100 metrov prebehol Zenón za 12.5 sekundy, ale Keď dobehol, bola 20 m pred ním. Keď prebehol týchto 20 m, bola 4 m pred ním, keď prebehol tieto 4 metre, bola ešte stále 80 cm pred ním. Zenón si začal zúfať, že korytnačku nikdy nedobehne, pretože kým dobehne tam, kde bola pred chvíľou, vždy o kúsok popolezie ďalej. Dohoní Zenón korytnačku alebo nie, a kedy?

**Riešenie**

Matematicky je toto ľahké, pretože máme za sebou dvetisíc rokov západného myslenia a predstava, ktorá veľmi znepokojovala  starovekých mudrcov, nám nepríde znepokojivé, že súčet nekonečného počtu vzdialeností môže byť konečný, a že tento nekonečný počet vzdialeností možno prejsť za konečný čas. 

Je to také ľahké, že dokonca ani nemusíme mobilizovať nejaké vedomosti o nekonečných radoch, stačí vypočítať dve rýchlosti a nájsť miesto a čas, kde sa Zenón a korytnačka stretnú. 
$$
v_Z = 100\,m/12.5\,s = 8\,m/s \\
v_K = 20\,m/12.5\,s = 1.6\,m/s \\
s_Z(t) = v_Z \cdot t \\
s_K(t) = 100\,m + v_K \cdot t \\
t_x = \frac{100}{v_Z - v_K} = 15.625\,s \\
s_Z = v_Z \cdot t_x = 100 \cdot \frac{v_Z}{v_Z - v_K} = 125\,m
$$
Teda Zenón dohoní korytnačku za 15.625 s a prebehne celkom 125 m.

3. > Pán Brown prišiel z krčmy k domovým dverám, našiel vo vrecku kľúče, a chce si odomknúť. Na zväzku má 10 kľúčov, ale v tej tme vyzerajú všetky rovnako. Skúsi jeden kľúč, a keď to nie je správny, vráti ho do zväzku a zasa náhodne vyberie kľúč, a takto postupuje ďalej, kým nenájde správny kľúč. 
   >
   > - Pri koľkom pokuse má pán Brown najväčšiu šancu nájsť správny kľúč?
   >
   > - Koľko kľúčov v priemere musí vyskúšať, kým nájde ten správny?

**Riešenie**

Nech N je počet kľúčov, p = 1/N pravdepodobnosť, že náhodný kľúč bude správny.

| Pokus    | P((úspechu))   | P(neúspechu) |
| -------- | -------------- | ------------ |
| 1        | $p$            | $1-p$        |
| 2        | $(1-p)p$       | $(1-p)^2$    |
| 3        | $(1-p)^2p$     | $(1-p)^3$    |
| $\vdots$ | $\vdots$       | $\vdots$     |
| n        | $(1-p)^{n-1}p$ | $(1-p)^n$    |

Teda najväčšiu pravdepodobnosť úspechu máme prekvapujúco pri prvom pokuse. Môže nás zaujímať, aký je stredný počet kľúčov, ktoré pán Brown potrebuje vyskúšať, aby sa dostal domov. 
$$
\langle n \rangle = \sum_{n=1}^\infty n \cdot p(1-p)^{n-1}
$$
Pre výpočet strednej hodnoty sa bežne používa postup, ktorý je za rámcom toho, čo chceme na tomto doučovaní robiť. Preto použijeme fintu: Čo vieme povedať o $\langle n \rangle$ pred prvým pokusom? V prípade úspechu bude $\langle n \rangle=1$ (s pravdepodobnosťou p), a prípade neúspechu (s pravdepodobnosťou 1-p) sme tam, kde sme začali, očakávaný počet pokusov bude stále $\langle n \rangle$, ale už sme jeden pokus vyčerpali:
$$
\langle n \rangle = p \cdot 1 + (1-p) \cdot (\langle n \rangle + 1)
$$
odkiaľ plynie $\langle n \rangle=1/p$, čo je neprekvapivý výsledok. 

## 2. Príklady na zahriatie

**Príklad 1**

Nájdite všetky celé čísla n, pre ktoré platí
$$
9^n - 6^n = 4^n
$$
Poznámka. Pre riešenie takýchto rovníc máme 3 stratégie: 

- snažiť sa uviesť veci na spoločný základ, 
- snažiť sa uviesť veci na spoločný exponent
- urobiť vhodnú substitúciu. 

**Príklad 2**

Ktoré číslo je väčšie? $2^{100}$ alebo $3^{75}$?

**Príklad 3**

Minule sme tu riešili parciálne zlomky, tak dnes bude komplementárna operácia: delenie polynómov. Zjednodušte výraz
$$
\frac{x^3 + 3x^2 - 4x - 12}{x-2}
$$
Návod:

<img src="img\synthetic_division.png" alt="image-20230714011752312" style="zoom:120%;" />

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

​	Toto je iný výrok ako predchádzajúci. Máme tu dve nové veci: **Predikát** - teda parametrizovaný výrok (logickú funkciu), ktorý je pravdivý alebo nepravdivý podľa toho, čo doň dosadíme. A máme dokázať, že tvrdenie platí pre nekonečnú množinu čísel 1, 2, ... 

​		Pri takýchto tvrdeniach väčšinou postupujeme tak, že vykonáme priekum bojom: overíme platnosť tvrdena na niekoľkých hodnotách, a snažíme sa zistiť, ako tvrdenie "funguje". Toto tvrdenie má tú zvláštnu vlastnosť, že platí pre všetky n menšie ako 40, ale pre 40 dostaneme $40^2 + 40 + 41 = 40*41 + 41$ a teda sa nejedná o prvočíslo.  

* Výrok. Neexistujú prirodzené čísla a, b, c, d spĺňajúce rovnosť $a^4 + b^4 + c^4 = d^4$.  Toto tvrdenie pochádza od Leonard Eulera z roku 1769, a až o 218 rokov neskôr Noam Elkies ukázal, že neplatí: a = 95800, b = 217519, c = 414560, d = 422481 sú riešením rovnice. 

**Axiómy** sú tvrdenia, ktoré považujeme za pravdivé. 



## 4. Domáca úloha (nová)

**Príklad 1**

Označme gcd(m, n) najväčší spoločný deliteľ celých čísel m,n (*_greatest common divisor_*), teda najväčšie číslo, ktoré je deliteľom m i n. Nech m>n. Dokážte, že 

​	a. gcd(m-n, n) = gcd(m,n)

​	b. gcd(m % n) = gcd(m, n) 

kde znak % označuje zvyšok po celočíselnom delení m a n. 

**Príklad 2**

Dokážte, že $\sqrt{2}$ nie je racionálne číslo.

**Príklad 3.**n                             

Riešte:
$$
x^2 - y^2 = 24 \\
xy=35 \\
x + y = ?
$$
**Príklad 4**

Nájdite reálne riešenia rovnice
$$
x^6 = (x-1)^6
$$
