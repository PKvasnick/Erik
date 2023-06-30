## Hodina 30. júna 2023

Program:

1. Domáca úloha: zvyšné príklady z prijímačkového testu
2. Rôzne postupnosti
3. Príklady

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Telekonferencia** Používame rovnaký link na moju videomiestnosť na Doucma.sk: https://www.doucma.sk/call/408896-peter

### 1. Domáca úloha

#### Toto bola prvá časť DÚ

Používam tieto príklady na prijímaciu skúšku z matematiky: https://fmph.uniba.sk/studium/prijimacie-konanie/prihlasky/prijimacie-skusky-zadania-a-riesenia/. 

Naposledy sme skončili niekde tuto:

![image-20230630163527396](img\image-20230630163527396.png)

Ako to je s ďalšími príkladmi?

#### Druhá časť domácej úlohy boli tieto príklady:

**Príklad 1**

Postupnosť začína číslami 1, 3, 6, 10. Doplň ďalšie členy. 

Ako u väčšiny príkladov, ktoré budeme riešiť, nezaujíma nás až tak veľmi konkrétny príklad, ale stratégie a postupy, ktoré sa dajú použiť. 

**Príklad 2**

Platí
$$
\sqrt{25} = 2 + 5 - 2 \quad (\textrm{odčítame dvojku od druhej odmocniny}) \\
= 5\\
\sqrt{64} = 6 + 4 - 2 = 8\\
\sqrt{196} = 1 + 6 + 9 - 2 = 14\\
\sqrt{289} = 2 + 8 + 9 - 2 = 17
$$
Je toto nová fantastická finta na odmocňovanie? Ako to funguje? Pre aké najväčšie číslo to môže platiť?

**Príklad 3**

Majme postupnosť $x_{n+1} = a\cdot x_n(1-x_n)$. Ako sa správa pre rôzne $a$?

### 2. Všelijaké číselné rady

#### Aritmetický rad

$$
a_n = a_0 + nd, \quad n = 0, 1, \dots
$$

Aký je súčet prvých n členov?

**Gaussova finta:**
$$
S_n =& a_0 + 0d &+ a_0 + 1d &+ a_0 + 2d &+ \dots &+a_0 + nd \\
S_n =& a_0 + nd &+ a_0 + (n-1)d &+ a_0 + (n-2)d &+ \dots &+ a_0 +0d \\
2S_n =& 2a_0 + nd &+2a_0 + nd &+ 2a_0 + nd &+ \dots &+ 2a_0 + nd 
$$
a posledný súčet ide sčítať ľahko, pretože v ňom máme samé rovnaké členy. 

#### Geometrický rad:

$$
a_n = a_0 q^n
$$

Súčet: rekurentný vzťah:
$$
S_n = a_0 + a_0q + a_0q^2 + \dots = a_0 + qS_{n-1}
$$


### 


