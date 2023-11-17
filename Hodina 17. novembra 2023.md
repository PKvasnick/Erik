## Hodina 17. novembra 2023

Program:

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli: Ešte bude trocha projektívnej geometrie.
3. Afínna geometria a komplexné čísla.
4. Domáca úloha (nová)
5. Program na budúci týždeň

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Videohovor** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

### 1. Domáca úloha

**Príklad 1**

Majme šesťuholníkový biliardový stôl.

![](img\Hexagon_billiard.png)

Guľa sa nachádza na spojnici $P_2P_6$. Máte guľu postrčiť tak, aby sa prvýkrát odrazila od strany $P_1P_2$ alebo $P_4P_5$ a druhý odraz ju poslal do vrecka $P_4$.  Kde všade na červenej spojnici sa môže guľa nachádzať, aby bol takýto strk možný?

**Riešenie**

Toto nie je presné riešenie, ale takto sa na to treba pozerať:

![](img\heaxagon_billiard.png)



---

**Príklad 2**

Nájdite polomer kruhu.

<img src="img\Hw_semicircle.png" style="zoom:50%;" />



**Riešenie**

Veta o skrížených tetivách a neutopiť sa v číslach.

Označme x dĺžku úsečky od bodu C po X, priesečník s kružnicou pod DE. Potom 
$$
(r+10)\cdot (2r - r - 10) = 21\cdot x \\
r^2 = 100 + 21x
$$
Potom z pravouhlého trojuholníka ABX máme
$$
16^2 + (21+x)^2 = (2r)^2
$$
Dosadenie za x vedie ku škaredým číslam, ľahšie je dosadiť za r:
$$
256 + 441 + 42x + x^2 = 400 + 84x \\
x^2 - 42x + 297 = 0 \\
(x-9)(x-33)=0
$$
Druhý koreň je nereálny, takže x = 9 a 
$$
r^2 = \frac{16^2 + 30^2}{4} = 289
$$
a teda r = 17.

---



## 2. Príklady na zahriatie

#### Ešte trocha projektívnej geometrie

**Pappusova veta**

Sľúbil som dôkaz, a síce nebude s vektormi, ale bude pekne projektívny a nebudeme prechádzať do afínnej roviny.

![](img\Pappus.png)

Ppappusovu veta tvrdí, že body $C_1, C_2, C_3$ sú kolineárne. Prekreslíme si obrázok a pozrieme sa bližšie, ako tu veci fungujú. 

![](img\Pappus_proof_1.png)

Máme tu zobrazenie bodov $B_1, B_2, B_3$ na body $A_1, A_2, A_3$ pomocou dvoch perspektívnych projekcií: Prvá projekcia s ohniskom $A_3$ "stiahne" body $B_1, B_2, B_3$ na červenú priamku (zelené šípky). Druhá projekcia s ohniskom $B_3$ pošle body z červenej čiary do bodov $A_1, A_2, A_3$. Máme tu tri takéto dvojice, ale skúmame iba túto jednu. Nemáme žiadnu záruku, že bod $C_3$ leží na červenej čiare - to práve potrebujeme dokázať. 

Pre náš dôkaz bude podstatné, čo sa udeje s bodmi P a Q, Prvá projekcia stiahne bod P do bodu Q, a druhá ho ponechá na mieste, pretože už leží na priamke $A_1 A_2$. O bode Q pozitívne vieme, že leží na červenej čiare. 

Pozrime sa teraz na inverzné zobrazenie: 

![](img\Pappus_proof_2.png)

Na tomto obrázku máme dvojicu projekcií, ktoré zobrazjú body $A_1, A_2, A_3$ na $B_1, B_2, B_3$. Červená čiara na tomto obrázku nemusí byť nutne totožná s červenou čiarou na predošlom obrázku, konkrétne nevieme povedať, či na nej leží bod $C_1$. 

Čo ale vieme je, že toto zobrazenie je inverzné k projekciám na predošlom obrázku.  Pretože kombinácia projekcií na dvoch obrázkoch zobrazuje body $B_1, B_2, B_3$ na seba, musí toto platiť pre všetky body na priamke $B_1B_2$, a teda aj pre priessečník P. To ale znamená, že bod Q musí ležať na oboch červených priamkach, a pretože na oboch červených priamkach musí ležať aj bod $C_2$, musia byť priamky totožné. 



---



## 3. Vektory a komplexné čísla

### Van Aubelova veta

Spojnice štvorcov sú na seba kolmé a majú rovnakú dĺžku.

![](img\Stelling van Van Aubel.png)

To som minule pokašľal, ale snáď teraz to už je jasné. 

**Rovnica priamky**

Parametrickú rovnicu sme už mali: 

Body, ležiace na priamke, prechádzajúcej bodmi $A, B$ sú $X = A + t(B-A)$.

- Toto nejde ľahko zovšeobecniť na zložitejšie krivky (teda ide, ale užitočné to je iba občas. 

Afinny priestor: máme body, vektory, a vzdialenosti medzi nimi.

- Vzdialenosť bodov: $|B-A|=\sqrt{(b_x - a_x)^2+(b_y-b_x)^2}$

- Vzdialenosť vektorov meria odchýlku ich smerov:  $\vec{a}\cdot\vec{b} = |\vec{a}||\vec{b}|\cos{\angle(\vec{a},\vec{b})} = a_x\cdot b_x + a_y \cdot b_y$.

Body nemôžeme sčítať, ale vektory áno. Body ale môžeme odčítať, pričom dostávame vektor. 

*Normálová rovnica priamky*

Priamku, kolmú na vektor $\vec{n}$ a prechádzajúcu bodom $A$, tvoria body, pre ktoré platí $(X-A)\cdot \vec{n} = 0$, čo vedie k rovnici tvaru $ax + by + c = 0$.

### Komplexné čísla

![](img\complex_0.png)

Komplexné čísla sú čisla tvaru $z = x + iy$, kde x, y sú reálne súradnice v rovine a $i^2 = -1$.

### Transformácie

**Vektor je posunutie**, takže posunutia sú ľahké. 

**Rotácie** sú ťažšie, ale sú ľahké v komplexných číslach. 

**Zamyslenie na domácu úlohu: Čo ostatné izometrie roviny?**

Zrkadlenie? Stredová symetria? Posunuté zrkadlenie?

(Porozmýšlať: aké ingrediencie na toto potrebujeme a v akom vyjadrení to je najprirodzenejšie.)

---



## 4. Domáca úloha (nová)

1. Máme kvadratickú formu  $y^2 - 8y - x + 19 = 0$, ktorá popisuje parabolu v rovine. Nájdte vrchol paraboly, ohnisko, smerovú priamku (pre ohnisko a riadiacu priamku platí, že body na parabole majú rovnakú vzdialenosť od ohniska a riadiacej priamky), a os paraboly. 



2. Vyriešte.

<img src="img\image-20231117155739169.png" alt="image-20231117155739169" style="zoom:30%;" />



---



## 5. Program na budúci týždeň

Grupy symetrií a dlaždice možno dáme nabudúce.

Ale robíme analytickú geometriu a komplexné čísla. 

