## Hodina 10. novembra 2023

Program:

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli: Projektívna geometria a Apolóniove úlohy
3. Geometria: už nebude
4. Domáca úloha (nová)
5. Program na budúci týždeň

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Videohovor** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

### 1. Domáca úloha

#### Domáce úlohy v texte

**Kružnica a dva body**

Toto je ľahšie, ako sa zdá, a je to výborné cvičenie na Pascalovo rozšírenie Pappusovej šesťuholníkovej vety, ktorú sme spomínali vyššie (bežne sa dá nájsť iné riešeniel). Toto riešenie má čaro projektívnej goemetrie - že začneme hlava-nehlava kresliť kružnice a spájať rôzne body. 

**Riešenie**

Začneme tým, že nakreslíme tri rôzne kružnice, prechádzajúce dvoma zadanými bodmi tak, aby každá pretínala zadanú kružnicu v dvoch bodoch. Dostaneme sériu 6 bodov na kružnici a použijeme Pappusovu vetu pre kužeľosečku: priesečníky spojníc musia ležať na priamke. Potom priesečníky Pappusovej priamky so zadanou kružnicou sú body dotyku na kružnici. 

![](img\Apolonius_bbk.png)

#### Regulérna domáca úloha

**Príklad 1**

Dve rotácie okolo bodov $P_1, P_2$ sú ekvivalentné jedinej rotácii. Zostrojte túto rotáciu. 

**Riešenie**

Nech sú rotácie definované zrkadleniami okolo priamok f, g, resp. h, i.  Otočíme dvojicu f, g okolo $R_1$ tak, aby g prechádzala bodom $P_2$. Otočíme h, i tak, aby h prechádzala bodom $P_1$. Zrkadlenia okolo g´ a h´ sa potom vyrušia a ostane výsledné otočenie okolo f´ a i´.

![image-20231021105721877](img\TwoRotations2.png)

**Príklad 2**

Sú dané dve kružnice $k_1, k_2$ a bod P. Zostrojte dva body $A \in k_1,\,B \in k_2$ tak, aby bol bod P stredom úsečky AB.

**Riešenie**

Situácia je stredovo symetrická vzhľadom na bod P.



![image-20231025155144971](img\TowCircles_and_a_Point.png)

Podrobnejšie: Pre stredovú symetriu $S_P$ so stredom P platí 
$$
A \in c_1 \implies S_P(A) \equiv B \in c_1^{\prime} \equiv S_P(c_1) \implies B \in c_2 \and B \in c_1^{\prime} = B \in (c_2 \cap c_1^{\prime})
$$
a tým je daná konštrukcia. Zaujímavé rozšírenie je zostrojiť pre dané kružnice množinu bodov P, pre ktoré má úloha riešenie.

**Príklad 3**

Priamka g prechádza bodmi $A[1,2]$ a $P[3,0]$ a priamka h cez $Q[2,4]$ a $R[6,3]$.  Zostrojte rovnostranný trojuholník ABC tak, aby bod B ležal na g a bod C na h.

**Riešenie**

Potrebujeme zrotovať priamku g okolo bodu A o 60° a (360 - 60)°:

![Two_lines_and_a_triangle](img\Two_lines_and_a_triangle.png)


---



## 2. Príklady na zahriatie

#### Perspektíva a projektívna geometria

**Dlaždice v perspektíve**

V zásade robíme to, že všetky zväzky rovnobežných priamok chytíme ako špagety a necháme ich stretnúť sa v jedinom bode na horizonte. 

![](img\Perspective_tiles.png)

Projekcie možno robiť aj zo zábavnejších vecí ako sú dlaždice. Napríklad kužeľosečky sa premiietajú na kužeľosečky, ibaže občas iné. 

![](img\Perspective_parabola.png)

Setup pre projekciu vyzerá asi takto:



![Perspective](img\Perspective2.png)

Máme spodnú šedú rovinu, kde sa rozprestiera reálny svet. Ten zobrazujeme na šikmú modrošedú rovinu tak, že sa dívame z bodu P a šikmá (obrazová) rovina je naše maliarske plátno. Hormá vodorovná rovina je projektívna rovina, sú tam veci, ktoré v reálnom svete ležia v nekonečne. Plocha nášho zobrazenia je prirodzene ohraničená horizontom - priesečníkom zobrazovacej a projektívnej roviny, a faktom, že sa dívame pred seba - veci, ktoré sú za nami a zobrazovali by sa nad horizont, ignorujeme. 

**Projektívna geometria** je oveľa staršia ako perspektíva renesančných maliarov. Tuto je jedno z najdôležitejších tvrdení, ktoré pochádza od Pappusa z Alexandrie, 300 n.l.:

**Pappusova veta (o šesťuholníku)**

![](img\Pappus.png)

Majme na tri body $A_1, A_2, A_3$, ležiace na spoločnej priamke, a tri body $B_1, B_2, B_3$, ležiace na inej spoločnej priamke. Označme $C_3 = A_1B_2 \cap A_2B_1,\quad C_2 = A_1B_3 \cap A_3B_1,\quad C_1 = A_2B_3 \cap A_3B_2$. Potom body $C_1, C_2, C_3$ ležia tiež na spoločnej priamke. 

Táto veta má zvláštne čaro, pretože vyzerá úplne fundamentálne (iba body a priamky, žiadne kruhy, vzdialenosti či uhly). 

**Dualita**

V projektívnej geometrii sú priamky a body rovnocenné. Tak, ako sú body priesečníkmi priamok, sú priamky "priiesečníkmi" bodov. Preto sa často používa aj úplne mätúce označenie vecí, ktoré nerozlišujem medzi priamkami a bodmi. 

Napríklad duálna Pappusova veta je úplne rovnoprávne tvrdenie, ktoré sa dokonca dokazuje častejšie ako "priama" verzia:

**Duálna Pappusova vetta** Nech majú priamky A, B, C spoločný bod, a nech aj priamky a, b, c majú spoločný bod. Potom priamky X, Y, Z predchádzajúce po rade priesečníkmi Ab a Ba, Ac a Ca, bC a Cb majú tiež spoločný bod. 

![Pappus_dual](img\Pappus_dual.png)

Samotná projektívna geometria sa rozvíjala od rokov 1600 + (C. Desargues, B. Pascal) v tieni Descartovej geometrie. 

**Zovšeobecnenie Pappusovej vety (B. Pascal, 1608):**

Nech c je ľubovoľná kužeľosečka, na ktorej leží 6 bodov $A_1, A_2, A_3, B_1, B_2, B_3$. Označme $C_3 = A_1B_2 \cap A_2B_1,\quad C_2 = A_1B_3 \cap A_3B_1,\quad C_1 = A_2B_3 \cap A_3B_2$. Potom body $C_1, C_2, C_3$ ležia tiež na spoločnej priamke. 

![](img\Pascal.png)



**Desarguesova veta**

*_Definícia_* Majme dva trojuholníky ABC, DEF a bod P. Hovoríme, že trojuholníky ABC, DEF sú v perspektíve vzhľadom k bodu P, ak sú trojice bodov PAD, PBE, PCF kolineárne.

*_Definícia_* Majme dva trojuholníky ABC, DEF a priamku p. Hovoríme, že trojuholníky ABC, DEF sú v perspektíve vzhľadom k priamke p, ak priesečníky strán AB a DE, AC a DF, a BC a EF ležia na priamke p.

**Desarguesova veta**: Ak sú dva trojuholníky v perspektíve vzhľadom k bodu, sú v perspektíve vzhľadom k priamke.

![](img\Desargues.png)

Inak povedané, ak sú dva trojuholníky v perspektíve, priesčníky ich zodpovedajúcich strán sú kolineárne.

Nedával som nikde dôkazy. Aj toto vyzerá, že by sa dokazovalo ťažko. Ale stačí si celú vec predstaviť v 3D a zrazu to je úplne intuitívne:

![](img\Desargues3D.png)

Pretože sa v projektívnej geometrii používa iba pravítko, pomocou ktorého sa spájajú body a konštruujú priesečníky (to neznamená, že pomocou pravítka nemožno skonštruovať kužeľosečky), konštrukcie obvykle vyzerajú tak, že sa k existujúcim čiaram a bodom prikreslí tisíc nových bodov a čiar. 

---

### Apolóniove úlohy

Zostroj kružnicu, ktorá sa dotýka trojice z týchto objektov: bod, priamka, kružnica.

![](img\Apolonius.drawio.png)

D1 je úloha na pozriem a vidím, D2 na večer, D3 na týždeň, D4 na mesiac a D5 na kus života. 

**Bod, bod, priamka**

Už toto je dosť tažké. "Priamočiare" riešenie je použiť množiny bodov, ktoré sú rovnako vzdialené od bodu a priamky - teda paraboly. Tak sa ťažká úloha premení na ľahučkú. 

![](img\Apolonius_bbp.png)

Ale to nie je správny geometrický telocvik - nevedeli by sme to vyriešiť nejakými elementárnejšími metódami, teda pomocou pravítka a kružidla?

Jednoduchý spôsob riešenia je využiť vetu o sile bodu (Power of a point). Ak je T bod dotyku priamky a kružnice, a bod P priesečníki priamky XY s priamkou f, potom platí $PX \cdot PY = PT^2$ a s tým už ide niečo robiť. V podstate potrebujeme zostrojiť štovrec, ktorý má rovnakú plochu ako obdĺžnik, a to nie je ťažké, hlavne ak si spomenieme na kruhovú inverziu: Ak invertujeme okolo kružnice so stredom P a polomerom PT, potom X bude obrazom Y (a naopak.). A ako sa k sebe majú vzor a obraz pri kruhovej inverzii? Pamätáme? Kolmica, kde sa pretne s kružnicou, k tomu bodu dotyčnica a hľadáme priesečník so spojnicou stredu a vzoru. Inak povedané, potrebujeme pravouhlý trojuholník s odvesnou PY a s pätou výšky X. 

![](img\Apolonius_bbp_2.png)

Tak ľahko zostrojíme kružnicu inverzie, a jej priesečník bude bod dotyku hľadanej kružnice s f, pretože to je pevný bod inverzie. Keď už máme tri body hľadanej kružnice, ľahko ju zostrojíme. 

**Priamka, bod, priamka**

To je zase ľahké pomocou parabol. 

![](img\Apolonius_pbp.png)

ale prekvapivo ľahké to je aj s pravítkom a kružidlom, pretože nám pomôže rovnoľahlosť. Stačí zostrojiť ľubovoľnú kružnicu, dotýkajúcu sa oboch priamok, a potom pomocou podobnosti stred požadovanej kružnice (presnejšie dvoch):

![](img\Apolonius_pbp_2.png)

**Pomôcka** v Desarguesovom štýle:

![](C:\Users\kvasn\Documents\GitHub\Erik\img\Polar_line.png)

1. Polára. Kruhová inverzia vytvára priradenie bodov mimo kruhu a tetív v kruhu: bodu P mimo kruhu priradzujeme jeho polárnu priamku (poláru), čo je kolmica na spojnicu bodu a stredu kruhu, predchádzajúca obrazom bodu P v kruhovej inverzii. 
2. Majme ľubovoľné priamky, prechádzajúce bodom P a vytínajúce dve tetivy na kružnici. Tieto dve tietivy definujú cirkulárny štvoruholník. Dve opačné strany tohoto štvoruholníka sa pretínajú v bode, ležiacom na poláre. 

**Kružnica a dva body**

Toto je ľahšie, ako sa zdá, a je to výborné cvičenie na Pascalovo rozšírenie Pappusovej šesťuholníkovej vety, ktorú sme spomínali vyššie (bežne sa dá nájsť iné riešeniel). Toto riešenie má čaro projektívnej goemetrie - že začneme hlava-nehlava kresliť kružnice a spájať rôzne body. **Domáca úloha**

---



## 4. Domáca úloha (nová)

Začneme pár príkladmi z projektívnej geometrie.

1. Máme dve priamky f, g, ktorých priesečník X sa nachádza mimo výkresu, a bod P. Veďte bodom P priamku, prechádzajúcu priesečníkom X.  (Návod: Desarguesova veta)


![image-20231027113232179](img\Hw_Desargues.png)

2. Máme dve dvojice priamok f, g a h, i, ktorých priesečníky X, resp. Y sa nachádzajú mimo výkresu. Máme bod P a za úlohu viesť bodom P rovnobežku s priamkou XY.

![image-20231027122419371](img\Hw_parallel.png)

3. Dokážte:, že pomocou paraboly môžeme násobiť čísla. 

![image-20231030124951037](img\nasobenie_na_parabole.png)

4. Nájdite všetky komplexné čísla z také, že $z^3 = 1 + i$. (Príprava na budúce: čo vieme o komplexných číslach?)



---



## 5. Program na budúci týždeň

Grupy symetrií a dlaždice.

Ale dosť hrozí, že už ideme na goniometriu a komplexné čísla. 

