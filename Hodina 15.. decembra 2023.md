## Hodina 15. decembra 2023

Program:

1. Domáca úloha (z minula)
2. Niekoľko príkladov na zahriatie a pozdvihnutie mysli: Komplexné čísla a goniometria
3. Afínny priestor
4. Domáca úloha (nová)
5. Program na budúci týždeň

### 0. Úvod

**Tento text** a texty k nasledujúcim cvičeniam budú vyložené - ako pdf - v Github repozitári https://github.com/PKvasnick/Erik. Odporúčam Github Desktop (na Windows) pre uloženie a synchronizáciu repozitára. 

**Videohovor** Používame SpeakApp, link postnem vždy pred hodinou, *_je možné, že sa bude týždeň od týždňa líšiť_*.

---

### 1. Domáca úloha



**Príklad 1**

Vypočítajte limitu 
$$
\lim_{n\rightarrow\infty} \sqrt{\frac{1}{n}+\sqrt{\frac{1}{n}+ \dots }}
$$
**Riešenie**

Táto limita sú v skutočnosti dve limity:
$$
\lim_{n\rightarrow\infty} \lim_{m\rightarrow \infty} 
\underbrace{\sqrt{\frac{1}{n}+\sqrt{\frac{1}{n}+ \dots }}}_{m\,krát}
$$
Intuitívne je toto poradie limít to správne, pretože najskôr adresujeme otázku hodnoty nekonečného radikálového výrazu pre fixné n ako limitu pre $m \rightarrow \infty$, a potom skúmame, čo sa stane s touto limitou, keď $n \rightarrow \infty$. Naopak, pri opačnom poradí vchádzame s limitou v n do potenciálne zle definovaného výrazu a nemôžeme si byť istí, čo vlastne robíme. 

Vyšetríme najskôr toto poradie limít a ukážeme, ako veci fungujú, a potom vyšetríme opačné poradie, a ukážeme, že vôbec nefunguje. 

Začnime výrazom 
$$
S_{m,n} = \underbrace{\sqrt{\frac{1}{n}+\sqrt{\frac{1}{n}+ \dots }}}_{m\,krát}
$$
Rekurencia je 
$$
S_{m,n} = \sqrt{\frac{1}{n} + S_{m-1,n}},\quad S_{1,n} = \frac{1}{n}
$$
Limitu rekurencie nájdeme ľahko, stačí nájsť stacionárny bod rekurzie:
$$
S_n = \sqrt{\frac{1}{n} + S_n} \\
S_n^2 - S_n - 1/n = 0\\
S_{n|1,2} = \frac{1 + \sqrt{1 + 4/n}}{2}
$$
a záporný koreň zahadzujeme z očividných dôvodov. 

Táto limita je stacionárny bod funkčnej iterácie, ale nevieme, či to je stabilný stacionárny bod - teda či sa k nemu iterácie približujú alebo sa od neho vzďaľujú. Pre úplný dôkaz konvergencie potrebujeme typicky dve veci:

- hornú hranicu $S_{m,n} \le D\quad\forall m\in N$
- monotónnosť, teda že platí $S_{m,n} > S_{m-1,n}\quad \forall m,n \in N$.

*_Monotónnosť_* 
$$
S_{m+1,n} = \sqrt{\frac{1}{n}+\sqrt{\frac{1}{n}+ \dots + \sqrt{\frac{1}{n}+\sqrt{\frac{1}{n}}}}} \gt \sqrt{\frac{1}{n}+\sqrt{\frac{1}{n}+ \dots + \sqrt{\frac{1}{n}+0}}} = S_{m,n}
$$
Postupnosť $\{S_{m,n}\},\,m=1,2,\dots$ (pre fixné n) je teda rastúca. 

*_Horná hranica_*

Pre fixné $m$ je zjavne $S_{m,1} > S_{m,2} > \dots$. Ukážeme, že pre ľubovoľné m, n je $S_{m,n} \le \phi$, kde $\phi$ je pomer zlatého rezu, 
$$
\phi = \frac{1 + \sqrt{5}}{2}
$$
Prečo potrebujeme zlatý rez? Pre rovnicu, ktorou je definovaný a vlastnosť, ktorá z nej vyplýva: $\phi^2 = \phi + 1$. Teraz nám stačí dôkaz indukciou:

1. $S_{1,n} < S_{1,1} = 1 < \phi$
2. Ak $S_{n,n} \le \phi$, potom $S_{m+1,n} = \sqrt{1 + S_{m,n}} \le \sqrt{1 + \phi} = \phi$

čím je tvrdenie dokázané: dvojnásobná limita sa rovná 1: 
$$
\lim_{n\rightarrow\infty} \lim_{m\rightarrow \infty} 
\underbrace{\sqrt{\frac{1}{n}+\sqrt{\frac{1}{n}+ \dots }}}_{m\,krát}= 1
$$
*_Opačná limita_*: 
$$
\lim_{m\rightarrow\infty} \lim_{n\rightarrow \infty} 
\underbrace{\sqrt{\frac{1}{n}+\sqrt{\frac{1}{n}+ \dots }}}_{m\,krát}= \lim_{m\rightarrow\infty} 0 = 0
$$
a teda v tomto prípade nemôžeme vymeniť poradie, v ktorom počítame limity. Toto je varovný prípad, pretože tento postup často používame - napríklad implicitne pri zmene poradia integrovania. 

---

**Príklad 2**

Dokážte, že riešenia Pellovej rovnice typu $(3 + 2\sqrt{2})^n, n\rightarrow \infty$ dávajú racionálne aproximácie $\sqrt{2}$.

**Riešenie**

Potrebujeme rekurentný vzťah pre riešenia Pellovej rovnice. Označme
$$
A_n = a_n + b_n\sqrt{2} = (3+2\sqrt{2})^n
$$
Potom 
$$
A_{n+1} = (a_n + b_n\sqrt{2})(3 + 2\sqrt{2}) = 3a_n + 4b_n + (3b_n + 2a_n)\sqrt{2}
$$
Odtiaľ 
$$
a_{n+1} = 3a_n + 4b_n \\
b_{n+1} = 2a_n + 3b_n
$$
Vyjadríme z prvej rovnice $b_n$ a dosadíme do druhej rovnice
$$
b_n = \frac{1}{4}a_{n+1} - \frac{3}{4}a_n\quad \implies \quad b_{n+1} = 2a_n + \frac{3}{4}a_{n+1} - \frac{9}{4}a_n = \frac{3}{4}a_{n+1} - \frac{1}{4}a_n
$$
Posunieme v tomto vzťahu $n+1 \rightarrow n$ a dosadíme za $b_n$ v prvom vzťahu:
$$
b_n = \frac{3}{4}a_{n} - \frac{1}{4}a_{n-1} \\
a_{n+1} = 3a_n + 4b_n = 3a_n + 3a_n - a_{n-1} = 6a_n - a_{n-1}
$$
To znamená, že máme samostatný vzťah pre $a_n$ a vzťah pre $b_n$ v termínoch $a_n$. Stačí teda vyriešiť rekurziu pre $a_n$ a máme kompletné riešenie. Riešenie je ľahké a známe: položíme $a_n = \lambda^n$ a dosadíme:
$$
\lambda^{n+1} = 6\lambda^n - \lambda^{n-1} \\
\lambda^2 - 6\lambda + 1 = 0 \\
\lambda_{1,2} = \frac{6 \pm \sqrt{32}}{2} = 3 \pm 2\sqrt{2} \\
a_n = c_1\lambda_1^n + c_2\lambda_2^n
$$
Konštanty $c_1, c_2$ určíme z počiatočných podmienok:
$$
a_0 = 1 \implies c_1 + c_2 = 1 \\
a_1 = 3 \implies c_1\lambda_1 + c_2\lambda_2 = 3
$$
a teda 
$$
c_1 = \frac{2}{\lambda_1 - \lambda_2} = \frac{2}{4\sqrt{2}} = \frac{\sqrt{2}}{2},\quad c_2 = 1 - \frac{\sqrt{2}}{2}
$$
Konečne máme výraz pre $a_n$:
$$
a_n = \frac{\sqrt{2}}{2}(3 + 2\sqrt{2})^n + \left(1 - \frac{\sqrt{2}}{2}\right)(3 - 2\sqrt{2})^n
$$
Ako som písal vyššie, ľahko získame aj výraz pre $b_n$:
$$
b_n = \frac{3}{4}a_n - \frac{1}{4}a_{n-1} = \frac{3}{4}(c_1\lambda_1^n + c_2\lambda_2^n) - \frac{1}{4}(\frac{c_1}{\lambda_1}\lambda_1^n + \frac{c_2}{\lambda_2}\lambda_2^n) \\
= \left(\frac{3}{4}-\frac{1}{4\lambda_1}\right)c_1\lambda_1^n + \left(\frac{3}{4}-\frac{1}{4\lambda_2} \right)c_2\lambda_1^n \\
= \frac{1}{2}(3 + 2\sqrt{2})^n - \frac{\sqrt{2}}{2}\left(1-\frac{\sqrt{2}}{2}\right)(3 - 2\sqrt{2})^n
$$
Uvedomme si, že $\lambda_1 = 3 + 2\sqrt{2} \approx 5.828$, zatiaľčo $\lambda_2 = 3 - 2\sqrt{2} \approx 0.172$. Inak povedané, o hodnotách $a_n$ a $b_n$ s rastúcim n dominujú členy s $\lambda_1$ a pre pomer $a_n/b_n$ bude rozhodujúci pomer koeficientov pri $\lambda_1^n$, teda 
$$
\frac{a_n}{b_n} \rightarrow \sqrt{2}
$$
čo sme mali dokázať. Podobný výsledok by sme získali jednoduchšie aj inou cestou, priamo z (nerozpletenej) rekurzie:
$$
a_{n+1} = 3a_n + 4b_n \\
b_{n+1} = 2a_n + 3b_n \\
q_{n+1} \equiv \frac{a_{n+1}}{b_{n+1}} = \frac{3a_n + 4b_n}{2a_n + 3b_n} = \frac{3q_n + 4}{2q_n + 3}
$$
a pohľadáme stacionárny bod:
$$
q = \frac{3q + 4}{2q + 3} \implies 2q^2 - 4 = 0 \implies q^2 - 2 = 0
$$
Toto skrátené riešenie má ale tú nevýhodu, že nevieme, či hodnoty $q_n$ skutočne konvergujú k $\sqrt{2}$ a ako rýchlo. Naopak naše explicitné vyjadrenie pre $a_n, b_n$ dáva presný obraz o konvergencii a jej rýchlosti:
$$
a_n = A\sqrt{2}\lambda_1^n + B\sqrt{2}\lambda_2^n \\
b_n = A\lambda_1^n - B\lambda_2^n \\
\frac{a_n}{b_n} = \frac{A\sqrt{2}\lambda_1^n + B\lambda_2^n}{A\lambda_1^n + C\lambda_2^n} = \sqrt{2}\frac{1 + \frac{B}{A}\left(\frac{\lambda_2}{\lambda_1}\right)^n}{1 - \frac{B}{A}\left(\frac{\lambda_2}{\lambda_1}\right)^n}
$$
Pretože $\lambda_2/\lambda_1 \approx 0.029$, zlomok bude veľmi rýchlo konvergovať k 1 a celý výraz k $\sqrt{2}$.

Tu je niekoľko prvých iterácií:

```python
     a[n]      b[n]        a[n]/b[n]    a[n]/b[n] - √2
------------------------------------------------------ 
       1         0               inf               inf
       3         2  1.50000000000000  0.08578643762690
      17        12  1.41666666666667  0.00245310429357
      99        70  1.41428571428571  0.00007215191262
     577       408  1.41421568627451  0.00000212390141
    3363      2378  1.41421362489487  0.00000006252177
   19601     13860  1.41421356421356  0.00000000184047
  114243     80782  1.41421356242727  0.00000000005418
  665857    470832  1.41421356237469  0.00000000000159
 3880899   2744210  1.41421356237314  0.00000000000005
```

Získavame asi 1.5 rádu presnosti na iteráciu, čo nie je zlé, ale tiež nie oslnivé. 


---

## 2. Príklady na zahriatie

### Moivrova veta

$$
(\cos{\phi} + i\sin{\phi})^n = \cos{n\phi} + i\sin{n\phi}
$$

**Dôkaz** je triviálny: $e^{i\phi} = \cos{\phi} + i\sin{\phi}$. 

**Použitie**: goniometrické funkcie násobkov argumentu:
$$
\cos{2\phi} + i\sin{2\phi} = (\cos{\phi} + i\sin{\phi})^2 = \cos^2{\phi} + 2i\cos{phi}\sin{\phi} - \sin^2{\phi} \\
\therefore \\
\cos{2\phi} = \cos^2{\phi} - \sin^2{\phi}\quad \sin{2\phi} = 2\sin{\phi}\cos{\phi}
$$
Podobne môžeme odvodiť celý rad ďalších goniometrických vzťahov:

$e^{i\alpha}e^{i\beta} = e^{i(\alpha+\beta)}$ a teda 
$$
\cos(\alpha + \beta) + i\sin(\alpha + \beta) = (\cos\alpha + i\sin\alpha)(\cos\beta + i\sin\beta) \\
= \cos\alpha\cos\beta - \sin\alpha\sin\beta + i(\sin\alpha\cos\beta + \cos\alpha\sin\beta) \\
\therefore \\
\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta \\
\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta 
$$
**Ďalšie goniometrické vzťahy**

Vzťahy pre polovičný uhol
$$
\cos{\frac{\alpha}{2}} = \sqrt{\frac{1+\cos{\alpha}}{2}} \\
\sin{\frac{\alpha}{2}} = \sqrt{\frac{1-\cos{\alpha}}{2}}
$$
Súčty goniometrických funkcií

Domáca úloha
$$
\sin{\alpha} + \sin{\beta} = ? \\
\cos{\alpha} + \cos{\beta} = ?
$$

## Afinne transformácie

### Rotácia

<img src="img\Rotation.png" style="zoom:10%;" />

Otáčame bod $P=[x,y]$ okolo bodu O o uhol $\phi$. Aké sú nové súradnice bodu? Uhol rotácie $\phi$ meriame podľa konvencie proti smeru hodinových ručičiek.

Začneme s tým, že vyjadríme súradnice bodu $P$ v polárnych súradniciach,  $x = r\cos{\alpha}, y = r\sin{\alpha}$.  Podobne súradnice bodu $P^{\prime}$ budú $x^{\prime} = r\cos{(\alpha + \phi)}, y^{\prime}=r\sin{(\alpha + \phi)}$ a pretože sme sa práve naučili súčtové vzorce, vieme, ako pokračovať:
$$
x^{\prime} = r\cos{(\alpha + \phi)} = r\cos{\alpha}\cos{\phi} - r\sin{\alpha}\sin{\phi} = x\cos{\phi} - y\sin{\phi} \\
y^{\prime}=r\sin{(\alpha + \phi)} = r\cos{\alpha}\sin{\phi} + r\sin{\alpha}\cos{\phi} = x\sin{\phi} + y\cos{\phi} 
$$
a krajšie:
$$
\left(
\begin{matrix}
x^{\prime} \\
y^{\prime}
\end{matrix}
\right) = \left(
\begin{matrix}
\cos{\phi} & -\sin{\phi} \\
\sin{\phi} & \cos{\phi}
\end{matrix}
\right) \left(
\begin{matrix}
x \\ y
\end{matrix}
\right)
$$

### Afínne rozšírenie

Pridajme k bodom v rovine tretiu súradnicu, ktorá bude konštantná a bude 1. 
$$
\left(
\begin{matrix}
x \\
y
\end{matrix}
\right) \rightarrow
\left(
\begin{matrix}
x \\ y \\ 1
\end{matrix}
\right)
$$
Pre väčšinu účelov to neruší, napríklad
$$
\left(
\begin{matrix}
x^{\prime} \\ y^{\prime} \\ 1
\end{matrix}
\right) = \left(
\begin{matrix}
\cos{\phi} & -\sin{\phi} & 0 \\
\sin{\phi} & \cos{\phi} & 0 \\
0 & 0 & 1
\end{matrix}
\right) \left(
\begin{matrix}
x \\ y \\ 1
\end{matrix}
\right)
$$
Vyskúšajme takúto transformáciu:
$$
\left(
\begin{matrix}
1 & 0 & a \\
0 & 1 & b \\
0 & 0 & 1
\end{matrix}
\right) \left(
\begin{matrix}
x \\ y \\ 1
\end{matrix}
\right) = \left(
\begin{matrix}
x + a \\ y + b \\ 1
\end{matrix}
\right)
$$
Inak povedané, vieme aj posunutie napísať ako maticovú operáciu.  Všimneme si tiež, že to nie je zadarmo: Body a vektory už nie sú rovnaké objekty a translácia nie je lineárna operácia. 
$$
\left(
\begin{matrix}
x + a \\ y + b \\ 1
\end{matrix}
\right) \neq 
\left(
\begin{matrix}
x \\ y \\ 1
\end{matrix}
\right) + \left(
\begin{matrix}
a \\ b \\ 1
\end{matrix}
\right)
$$
Už vieme, že  horná ľavá submatica 2x2 je rotačná matica, pravá submatica 2x1 je vektor posunutia, prvok (3, 3) musí byť 1, takže nám ostáva zistiť, akú úlohu má matica 1x2 vľavo dole:
$$
\left(
\begin{matrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
s & t & 1
\end{matrix}
\right) \left(
\begin{matrix}
x \\ y \\ 1
\end{matrix}
\right) = \left(
\begin{matrix}
x \\ y \\ 1 + sx + yt
\end{matrix}
\right)
$$
Čo sme to tu spravili? Vektor sa nezmenil, ale pôvodná 1 sa zmenila. Aby sme pochopili, čo sa deje, musíme sa pozrieť do 3D priestoru.

### Geometria afínneho priestoru

V afínnom 3D priestore žijú všetky rovinné objekty na rovine z = 1. Bod $X = [a,b]$ je teda v skutočnosti priesečníkom priamky $\vec{0} + (a, b, 1)t$ s rovinou $z = 1$. Priamka, prechádzajúca počiatkom tak predstavuje ten istý bod, len posunutý do rôznych rovín. Bod $Y = [a, b, c]$ teda zodpovedá bodu $Y_1=[a/c, b/c, 1]  $ v rovine $z = 1$ a teda bodu $[a/c, b/c]$ v kartézskej rovine.

<img src="img\Affine1.png" style="zoom:50%;" />

Body sú teda priamky, a čo sú potom priamky? Priamky žijú v rovine $z = 0$, majú súradnice $[a, b, 0]$ a v 3D priestore sú to roviny:

![](C:\Users\kvasn\Documents\GitHub\Erik\img\Affine2.png)

Preto bod $[a, b, 1]$ leží na priamke $[a, b, 0]$.  Kým priesečníkom priamky $[a, b, 0]$ s rovinami $z = w$ zodpovedajú body $[aw, bw, w]$ v týchto rovinách, pre priamku nemáme operáciu pozdvihnutia do inej roviny. 

Posunutie je v Euklidovskej rovine lineárna operácia. Čo môže byť lineárnejšie ako pripočítať k polohovému vektoru iný vektor? V afínnom priestore to ale nie je lineárna operácia: Posunutie je vlastne deformácia 3D priestoru, kedy súradnicový vektor $\vec{z}_0$ nahradzujeme jeho lineárnou kombináciou $a\vec{x}_0 + b\vec{y}_0 + \vec{z}_0$. 

![](C:\Users\kvasn\Documents\GitHub\Erik\img\Affine3.png)

Takže aj keď na povrchu vyzerá afínny priestor jednoducho, je to fundamentálne iná vec a treba sa v ňom správať opatrne. 

---

##  Domáca úloha (nová) v 

1. Nájdite všetky $y \in C$, spĺňajúce rovnicu

$$
\sqrt{+y} + \sqrt{-y} = 4
$$

Návod: U reálnej odmocniny berieme ako hodnotu nezáporné riešenie rovnice $w^2 = y, w, y \in R_+$. U V komplexných číslach takúto konvenciu nemáme a odmocnina je viacznačná (preto sa znak odmocniny pre komplexné čísla prakticky nepoužíva).

2. Nájdite r

![image-20231215102926989](img\image-20231215102926989.png)

---

3.  Nájdite $\tan{(\alpha + \beta)}$ v termínoch $\tan{\alpha}, \tan{\beta}$.
4. Je daný bod $Q=[-3,1]$. Vypočítajte polohy stredov všetkých kružníc o polomere $r=\sqrt{20}$ , ktoré prechádzajú počiatkom $O=[0,0]$ a bodom Q.

---

## 5. Program na budúci týždeň

Afínne a projektívne súradnice.

Viac komplexných čísel.

