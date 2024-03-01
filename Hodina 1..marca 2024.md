## Hodina 1. marca 2024

**Program**

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli: všelijaké derivácie
3. Minimá a maximá
4. Domáca úloha (nová)
5. Program na budúci týždeň

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Videohovor** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

---

### 1. Domáca úloha

**Príklad 1**

Ktorý obdĺžnik má pri konštantnom obsahu najmenší obvod? 

**Riešenie**

Hľadáme maximum $x+y$ za podmienky $xy=S= const$. 

![](C:\Users\kvasn\Documents\GitHub\Erik\img\minimum_perimeter2.png)

Jednoduché riešenie:
$$
xy = S \implies y = \frac{S}{x}
$$
a teda minimalizujeme funkciu 
$$
o(x) = x + \frac{S}{x}
$$
V okolí minima alebo maxima sa funkcia pri malej zmene x prakticky nemení, teda jej dotyčnica v tom mieste má nulovú smernicu, čiže minimum budeme hľadať tam, kde $o^{\prime}(x)=0$. Môžeme tak dostať minimum aj maximum, takže sa v riešeniach musíme rozobrať, ktoré je čo. 
$$
o^{\prime}(x) = (x + \frac{S}{x})^{\prime} = 1 + S(x^{-1})^{\prime} = 1 +S(-1)x^{-2}=1-\frac{S}{x^2} = 0 \\
x = \pm \sqrt{S}
$$
Záporné riešenie zahadzujeme (v skutočnosti zodpovedá maximu, ale nespadá do prípustných hodnôt), kladné znamená, že $y = S/x = \sqrt{S} = x$​ a teda obdĺžnik s namenším obvodom je štvorec. Kladné riešenie zodpovedá minimu, ako vidieť z grafu. Pretože derivácia $o^{\prime}(x) = 1-S/x^2$ je pre $x<\sqrt{S}$ záporná a na opačnej strane kladná, znamená to, že máme minimum. 

Systematickejšie riešenie: 

![](C:\Users\kvasn\Documents\GitHub\Erik\img\minimum_perimeter.png)

Minimum bude tam, kde sa modrá čiara $x+y=const$ dotkne červenej $xy=S$. Inak povedané, v optime musí byť normálový vektor na obmedzenie kolineárny s prírastkom cieľovej funkcie. Ešte inak, dotyčnice k obmedzeniu a k cieľovej funkcii v optime musia mať rovnaký smer. Preto namiesto $o(x,y) = x + y$ optimalizujeme funkciu $L(x,y) = o(x,y) - \lambda(xy - S)$.  Derivácie tejto funkcie podľa $x, y, \lambda$ musia byť nulové:
$$
L = x + y - \lambda(xy - S) \\
\frac{\partial L}{\partial x} = 0 \implies 1 - \lambda y = 0 \\
\frac{\partial L}{\partial y} = 0 \implies 1 - \lambda x = 0 \\
\frac{\partial L}{\partial \lambda} = 0 \implies xy = S
$$
takže máme $x = y = 1/\lambda$ a z tretej rovnice máme $\lambda^2 = 1/S\implies \lambda = 1/\sqrt{S}$.  Odtiaľ $x = y = \sqrt{S}$​ a máme predchádzajúce riešenie. 

**Príklad 2**

Aký najväčší obdĺžnik (v zmysle plochy) vieme vpísať do polkruhu?

**Príklad 3**

Aký najväčší kužeľ môžeme vpísať do gule? (v zmysle podielu obsahu kužeľa a gule)

**Príklad 4**

Adam a Barbora 2: Adam s Barborou sa prechádzajú po cestičke pri pláži.  Cestička vedie rovnobežne s brehom mora vo vzdialenosti 50 m. Zrazu vietor zhodí Barbore klobúk a odnesie ho presne do bodu K 200 m nižšie na rozhraní pláže a mora. Adam ho chce zachrániť, kým ho spláchne vlna . Po cestičke beží rýchlosťou 8 km/h, ale v piesku len rýchlosťou 3 km/h. Ako dlho má Adam bežať po cestičke, kým vbehne do piesku, aby sa ku klobúku dostal čo najrýchlejšie?



## Niekoľko príkladov na zahriatie a povznesenie mysle

### 1. Všelijaké derivácie: súčin

Majme funkciu $f(x)\times g(x)$, napríklad $y = x\ln{x}$. Ako spočítam deriváciu?
$$
\frac{d}{dx}\left(f(x)g(x)\right) = \lim_{h\rightarrow 0}\frac{f(x+h)g(x+h) - f(x)g(x)}{h} \\
= \lim_{h\rightarrow 0}\frac{f(x+h)g(x+h) - f(x)g(x+h) + f(x)g(x+h) - f(x)g(x)}{h} \\
= \lim_{h\rightarrow 0}\frac{(f(x+h)-f(x))g(x+h) + f(x)(g(x+h) - f(x))}{h} \\
= \lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h} \lim_{h\rightarrow 0}g(x+h) + f(x)\lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h} = f^{\prime}(x(g(x) + f(x)g^{\prime}(x)
$$
Ešte raz::
$$
\left(f(x)g(x)\right)^{\prime} = f^{\prime}(x(g(x) + f(x)g^{\prime}(x)
$$
**Príklad**
$$
\left(x\ln{x}\right)^{\prime} = (x)^{\prime}\ln{x} + x\left(\ln{x}\right)^{\prime} = \ln{x} + x\cdot \frac{1}{x} = \ln{x} + 1
$$
**Vložka**: derivácia $\ln{x}$
$$
(\ln{x})^{\prime} = \lim_{h\rightarrow 0} \frac{\ln(x+h) - ln(x)}{{h}} = \lim_{h\rightarrow 0} \ln \left(1+\frac{h}{x}\right)^{1/h} \\
= \lim_{h\rightarrow 0}\ln\left(1 + \frac{h}{x}\right)^{x/h\cdot 1/x} = \ln\left(e^{1/x}\right) = \frac{1}{x}
$$

---

### 2. Všelijaké derivácie: zložené funkcie

Majme funkciu $g \circ f(x) \equiv g(f(x))$. Aká je jej derivácia?
$$
\left(g(f(x)))\right)^{\prime} = \lim_{h \rightarrow 0} \frac{g(f(x+h))-g(f(x))}{h} = \lim_{h\rightarrow 0}\frac{g(f(x+h))-g(f(x))}{f(x+h)-f(x)} \frac{f(x+h)-f(x)}{h} \\
= \frac{dg}{df}\cdot \frac{df}{dx}
$$
**Príklad**
$$
\left( \sqrt{1+x^2}\right)^{\prime} = \frac{1}{2}(1+x^2)^{-\frac{1}{2}}\cdot 2x = \frac{x}{\sqrt{1+x^2}}
$$

---

### 3. Všelijaké derivácie: derivácia inverznej funkcie

Majme funkciu  $y = f(x)$ a nech je $x = f^{-1}(y)$ je inverzná funkcia. Formálne:
$$
dy = f^{\prime}(x)dx \quad \therefore \quad dx = \frac{1}{f^{\prime}(x)}dy
$$
takže
$$
\left(f^{-1}(x)\right)^{\prime} = \frac{1}{f^{\prime}(y)}|_{y=f^{-1}(x)}
$$
Najprv píšeme deriváciu v termínoch y, aby bolo jasné, čo sa má derivovať a čo iba dosadiť. Je to trocha jemná argumentácia, treba si osvojiť. 

**Príklady**
$$
(e^x)^{\prime} = e^x \quad \therefore \quad (\ln{x})^{\prime} = \frac{1}{e^{\ln{x}}} \equiv \frac{1}{x}
$$

$$
(\sin{x})^{\prime} = \cos{x} \quad \therefore \quad (\arcsin {x})^{\prime} = \frac{1}{\cos(\arcsin{x})} = \frac{1}{\sqrt{1-x^2}}
$$



### 4. Všelijaké derivácie: viac premenných

Majme funkciu $z = f(x,y)$. Táto funkcia sa zjavne mení pri zmene x i y, preto má dva druhy derivácií:
$$
\frac{\partial f}{\partial x} = \lim_{h \rightarrow 0} \frac{f(x+h,y) - f(x,y)}{h}, \quad \frac{\partial f}{\partial y} = \lim_{h \rightarrow 0} \frac{f(x,y+h) - f(x,y)}{h}
$$
Tieto derivácie teda berieme podľa jednej premennej, pričom ostatné premenné držíme na konštantnej hodnote. 

**Príklad**
$$
S = - \sum_i p_i \ln{p_i} \\
\frac{\partial S}{\partial p_i} = -\ln{p_i} - 1
$$

---

### 5. Všelijaké derivácie: implicitné funkcie

Niekedy máme funkciu, definovanú vzťahom $F(x,y)=0$ a nie je úplne ľahké vyjadriť y v termínoch x, aby sme mohli derivovať obvyklým spôsobom. 

Vtedy postupujeme takto: $F(x,y)=0$ je konštantná funkcia, takže
$$
dF = \frac{\partial F}{\partial x}dx + \frac{\partial F}{\partial y}dy = 0 \quad \therefore \quad \frac{dy}{dx} = - \frac{\frac{\partial F}{\partial x}}{\frac{\partial F}{\partial y}}
$$
**Príklad**
$$
F(x,y) = x^2+y^2 = r^2 \quad \therefore \quad 
\frac{dy}{dx} = - \frac{2x}{2y} = -\frac{x}{y}
$$


### 6. Všelijaké derivácie: rôzne funkcie

![image-20240301161101791](img\table_derivatives.png)

**Príklad: Tangens**
$$
(\tan{x})^{\prime} = \left(\frac{\sin{x}}{\cos{x}}\right)^{\prime} = (\sin{x})^{\prime} \frac{1}{\cos{x}} + \sin{x}\left(\frac{1}{\cos{x}}\right)^{\prime} = 1 + \sin{x}\frac{-1}{\cos^2{x}}(-\sin{x}) = \frac{1}{cos^2{x}}
$$
**Príklad: Arkustangens**
$$
(\arctan{x})^{\prime} = \frac{1}{(\tan{y})^{\prime}}|_{y=\arctan{x}}= \cos^2(\arctan{x})= \frac{\cos^2(\arctan{x})}{\cos^2(\arctan{x})+\sin^2(\arctan{x})} \\
= \frac{1}{1 + \tan^2(\arctan{x})} = \frac{1}{1+x^2}
$$


---

## Minimá a maximá

##  Domáca úloha (nová) 

Nájdi prvú deriváciu funkcií (netreba všetko, ale treba prepočítať čo najviac typov a použiť rôzne metódy na kontrolu, kde sa dá.

![image-20240301130955972](img\derivatives1.png)

![image-20240301131141091](img\derivatives2.png)

![image-20240301131310532](img\derivatives3.png)

---

## 5. Program na budúci týždeň

- Budeme riešiť diferenciálne rovnice a integrovať.



