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

**Kružnica a dva body** (Apolóniova úloha)

Toto je ľahšie, ako sa zdá, a je to výborné cvičenie na Pascalovo rozšírenie Pappusovej šesťuholníkovej vety, ktorú sme spomínali vyššie (bežne sa dá nájsť iné riešeniel). Toto riešenie má čaro projektívnej goemetrie - že začneme hlava-nehlava kresliť kružnice a spájať rôzne body. 

**Riešenie**

Začneme tým, že nakreslíme tri rôzne kružnice, prechádzajúce dvoma zadanými bodmi tak, aby každá pretínala zadanú kružnicu v dvoch bodoch. Dostaneme sériu 6 bodov na kružnici a použijeme Pappusovu vetu pre kužeľosečku: priesečníky spojníc musia ležať na priamke. Potom priesečníky Pappusovej priamky so zadanou kružnicou sú body dotyku na kružnici. 

![](img\Apolonius_bbk.png)

---

#### Regulérna domáca úloha

**Príklad 1.**

Máme dve priamky f, g, ktorých priesečník X sa nachádza mimo výkresu, a bod P. Veďte bodom P priamku, prechádzajúcu priesečníkom X.  (Návod: Desarguesova veta)


![image-20231027113232179](C:/Users/kvasn/Documents/GitHub/Erik/img/Hw_Desargues.png)

**Riešenie**

Na riešenie možno použiť buď duálnu Pappusovu vetu alebo Desarguesovu vetu.

![](img\Hw_dual_Pappus.png)

Duálna Pappusova veta: Nakreslíme zelený zväzok: priamky, vychádzajúce z bodu Y. Máme tri priesečníky s každou z priamok f, g (ktoré sme si premenovali na $x_1, x_2$) a jedna zelená priamka prechádza bodom X. Vieme skonštruovať červený bod Z ako priesečník priamok $Z_{12}Z_{21}$ a $XZ_{32}$. Potom ale vieme skonštruovať aj bod $Z_{13}$ na modrej čiare. Niekde som sa v rysovaní dopustil nepresnosti, takže priesečník nevyšiel úplne presne. 

![](img\Hw_Desargues_soln.png)

Ľahko vytvoríme prvý trojuholník XFE tak, že zvolíme ľubovoľné body na priamkach. Jediná strana čiarkovaného trojuholníka E'F' stačí na konštrukciu jediného bodu priamky, kde ležia priesečníky zodpovedajúcich strán trojuholníkov. Nevadí, zvolíme si ľubovoľnú priamku, prechádzajúcu týmto bodom. Potom už ľahko zostrojíme zvyšné strany trojuholníka, a keď máme vrchol X', jeho spojnica s X musí prechádzať priesečníkom priamok f a g. 

2. Máme dve dvojice priamok f, g a h, i, ktorých priesečníky X, resp. Y sa nachádzajú mimo výkresu. Máme bod P a za úlohu viesť bodom P rovnobežku s priamkou XY.

![image-20231027122419371](C:/Users/kvasn/Documents/GitHub/Erik/img/Hw_parallel.png)

**Riešenie**

Toto nie je typická projektívna úloha, pretože v nej figurujú rovnobežky. Takže bez hanby vytvoríme zmenšenú kópiu štvoruholníka $XZ_1W_1Z_2$. Riešenie neukazuje rovnobežku priamo cez X, ale ukazuje konštrukciu požadovanej rovnobežky v blízkosti X, čo stačí.

![](img\Hw_parallel_soln.png)

**Príklad 3**

Dokážte:, že pomocou paraboly môžeme násobiť čísla. 

![image-20231030124951037](C:/Users/kvasn/Documents/GitHub/Erik/img/nasobenie_na_parabole.png)

**Riešenie**

Priamka, spájajúca ěavý a pravý bod na parabole prechádza bodmi $A=(-a, a^2)$ a $B = (b, b^2)$. Potrebujeme zistiť, kde táto priamka pretína y-ovú os.

Rovnica priamky v parametrickom tvare je $X = A + t(B-A)$. Po súradniciach: $x = -a + t(b+a),\,y = a^2 + t(b^2 - a^2)$.  Priesečník s y-ovou osou máme pre $x=0$, teda $t_0 = a/(a+b)$, a y je vtedy $y_0 = a^2 + a(b^2-a^2)/(a+b) = a^2 + a(b-a) = ab$.

**Príklad 4**

Nájdite všetky komplexné čísla z také, že $z^3 = 1 + i$. (Príprava na budúce: čo vieme o komplexných číslach?)

**Riešenie**

Pretože to asi musíme vysvetliť z gruntu, odložíme do ďalšej časti. 



---



## 2. Príklady na zahriatie

#### Ešte trocha projektívnej geometrie

**Kužeľosečky**

Projektívna geometria je o bodoch a priamkach, a predsa v nej prirodzene vznikajú kužeľosečky ako množiny bodov či priamok. 

![](img\Projective_ellipse.png)

Zelená a fialová priamka vytvárajú väzbu medzi zväzkami priamok, vychádzajúcich z $O_1$ a $O_3$ prostredníctvom bodu $O_2$ (čierne priamky). Sledujme priesečník X priamok zo zväzkov $O_1$ a $O_3$. Skúmajme, ako sa bude pohybuje bod X v závislosti od polohy A_1. 

Opisuje *elipsu*. Pre zobrazenie elipsy som použil funkciu Lokus z Geogebry. Lokus zobrazí všetky polohy X pre všetky možné polohy bodu $A_1$ na zelenej priamke. 

**Ako dokázať Pappusovu vetu?**

Nie, nebude dôkaz, ale podobne ako pri Desarguesovej vete prevedieme Pappusovu vetu na zrejmé tvrdenie. 

Duálna Pappusova veta hovorí o priesečníkoch dvoch zväzkov priamok:

![](img\Pappus_dual.png)

V afínnom priestore (teda v rovine, z ktorej robíme projekciu) bude originálne zobrazenie nejaké takéto:

![](C:\Users\kvasn\Documents\GitHub\Erik\img\Pappus_affine.png)

V 3D vidíme vzťah medzi týmito konštruktmi:

![](img\Pappus_projective_affine.png)

máme tri body hľadanej kružnice, ľahko ju zostrojíme. 

---



## 3. Vektory a komplexné čísla

### Van Aubelova veta

Spojnice štvorcov sú na seba kolmé a majú rovnakú dĺžku.

![](img\Stelling van Van Aubel.png)

### Komplexné čísla

![](img\complex_0.png)

---



## 4. Domáca úloha (nová)

1. Majme šesťuholníkový biliardový stôl.

![](img\Hexagon_billiard.png)

Guľa sa nachádza na spojnici $P_2P_6$. Máte guľu postrčiť tak, aby sa prvýkrát odrazila od strany $P_1P_2$ alebo $P_4P_5$ a druhý odraz ju poslal do vrecka $P_4$.  Kde všade na červenej spojnici sa môže guľa nachádzať, aby bol takýto strk možný?

2. Nájdite polomer kruhu.

<img src="img\Hw_semicircle.png" style="zoom:50%;" />



---



## 5. Program na budúci týždeň

Grupy symetrií a dlaždice.

Ale dosť hrozí, že už ideme na goniometriu a komplexné čísla. 

