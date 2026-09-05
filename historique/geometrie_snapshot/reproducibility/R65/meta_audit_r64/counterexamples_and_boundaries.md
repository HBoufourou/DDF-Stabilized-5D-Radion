# R64 — Contre-exemples, hypothèses minimales et frontière du no-go

**Périmètre.** Ce rapport ne modifie aucune donnée de POLY944/sigma5 et ne
réexécute pas la porte R63. Il soumet les inférences utilisées ou envisagées
après R63 à des modèles adversariaux explicites. Le but est de distinguer :

1. les hypothèses nécessaires à une dégénérescence de Tyurin ;
2. les hypothèses seulement suffisantes et propres au modèle R63 ;
3. les données nécessaires pour passer de la LMHS à \(R(t)\), puis à une tour ;
4. les hypothèses exactes sous lesquelles le no-go de parité survit.

Les calculs finis sont recoupés par
**meta_audit_r64/r64_boundary_certificate.py**.

## 1. Verdict synthétique

| Hypothèse ou raccourci testé | Modèle adversarial | Ce qui échoue | Conclusion R64 |
|---|---|---|---|
| Le diviseur ambiant \(T\) doit être une fibre | \(V=\mathbb P^1\times\mathbb P^3\), \(T\sim A+B\), \(Y\sim A+3B\) | \(S=Y\cap T\) est K3 anticanonique, mais \(N_{S/Y}\) est non trivial | « \(T\) fibre » est **suffisant**, pas nécessaire à Tyurin ; il est nécessaire à la preuve R63 des normales individuellement triviales |
| Les normales peuvent être ignorées | Deux \(\mathbb P^3\) collés le long d'une même quartique K3 | \(N_1\otimes N_2\simeq\mathcal O_S(8)\neq\mathcal O_S\) | Le **produit** trivial est nécessaire à une famille semistable à espace total lisse |
| Chaque normale doit être triviale | Modèle local \(uv=t\) dans \(\operatorname{Tot}(L\oplus L^{-1})\) | Les normales sont \(L\) et \(L^{-1}\), parfois non triviales | La trivialité individuelle n'est **pas** nécessaire ; seule leur dualité est intrinsèque |
| Anticanonicité \(\Rightarrow H^{>0}(\mathcal O_Y)=0\) | Suite exacte anticanonique ; jouets \(K3\times\mathbb P^1\) et \(E\times\mathbb P^2\) | La suite exacte ne force que \(h^1=h^2\) dans le cas K3 connexe | L'annulation R63 est une vraie entrée ; elle ne découle pas de l'adjonction seule |
| Une couture \((4,4)\) a toujours \(\mathrm{NS}=U(2)\) | Branche tangente à une fibre : \(w^2=x_1^4g_2(y)^2+x_0h_{3,4}\) | Une classe \(\delta^2=-8\) apparaît | « Très générale » est indispensable pour \(\mathrm{NS}=U(2)\) |
| Saut de \(\mathrm{NS}\Rightarrow\) saut automatique de II_18 | Même exemple Noether–Lefschetz | La classe nouvelle peut ne pas se prolonger aux composantes | Faux : la LMHS dépend de l'image réelle \(L\), pas de tout \(\mathrm{NS}(S)\) |
| L'action sur les deux rulings détermine l'involution | Branche symétrique et deux relèvements \(w\mapsto\pm w\) | Même action sur \(U(2)\), parité opposée sur \(H^{2,0}\) | Il faut calculer le relèvement et l'action sur le réseau K3 complet |
| Vecteur isotrope intégral \(\Rightarrow\) cycle algébrique/BPS | \(e\) primitif isotrope dans \(U\subset T(S)\) | Pour une couture très générale, \(e\notin H^{1,1}\) | L'isotropie topologique ne prouve ni courbe, ni cycle calibré, ni état BPS |

## 2. \(T\) non fibre : K3 anticanonique à normale non triviale

Posons

\[
V=\mathbb P^1\times\mathbb P^3,\qquad
A=c_1\mathcal O(1,0),\quad B=c_1\mathcal O(0,1).
\]

Dans

\[
A^*(V)=\mathbb Z[A,B]/(A^2,B^4),\qquad \int_V AB^3=1,
\]

prenons des membres généraux et transverses

\[
T\in|A+B|,\qquad Y\in|A+3B|.
\]

Ils sont lisses par Bertini. Comme

\[
-K_V=2A+4B=T+Y,
\]

la surface \(S=T\cap Y\) vérifie

\[
K_S=(K_V+T+Y)|_S\simeq\mathcal O_S.
\]

Les deux coupes sont amples ; Lefschetz donne \(H^1(S,\mathbb Z)=0\). Donc
\(S\) est une K3. De plus,

\[
K_Y=(K_V+Y)|_Y=-T|_Y,\qquad S\in|-K_Y|.
\]

Cependant

\[
N_{S/Y}\simeq\mathcal O_S(T)
\]

n'est pas trivial, car

\[
\int_S c_1(N_{S/Y})^2
=\int_V T^3Y
=\int_V(A+B)^3(A+3B)
=10.
\]

Un diviseur réduit qui est une fibre d'un morphisme vers une courbe possède
une normale triviale, donc ce \(T\) ne peut pas être une telle fibre.

**Frontière exacte.** L'hypothèse « \(T\) est une fibre » n'est pas requise par
la définition de Tyurin. Elle fournit, dans R63, une conclusion plus forte et
spéciale : \(N_{S/Y_j}\simeq\mathcal O_S\) séparément. Sans elle, il faut
calculer les deux normales et leur produit.

## 3. Normales : le produit trivial est nécessaire, les facteurs triviaux ne le sont pas

### 3.1 Contre-exemple global au produit trivial

Soit \(S\subset\mathbb P^3\) une quartique lisse. C'est une K3 et

\[
S\in|-K_{\mathbb P^3}|,\qquad
N_{S/\mathbb P^3}\simeq\mathcal O_S(4).
\]

Collons deux copies \(Y_1=Y_2=\mathbb P^3\) le long de \(S\) par l'identité :

\[
X_0=Y_1\cup_S Y_2.
\]

Les composantes sont Fano, la couture est anticanonique des deux côtés, et le
dualiseur de \(X_0\) est trivial sur chaque composante. Pourtant

\[
T^1_{X_0}|_S
\simeq N_{S/Y_1}\otimes N_{S/Y_2}
\simeq\mathcal O_S(8)\neq\mathcal O_S.
\]

Si \(H=\mathcal O_S(1)\), alors \(H^2=4\) et

\[
\int_S c_1\!\left(\mathcal O_S(8)\right)^2=8^2H^2=256.
\]

Ce \(X_0\) ne peut donc pas être la fibre centrale d'une dégénérescence
**semistable à espace total lisse** : dans une telle famille,
\(Y_1+Y_2=\operatorname{div}(t)\), et sa restriction à \(S\) impose
\(N_{S/Y_1}\otimes N_{S/Y_2}\simeq\mathcal O_S\). Cela n'exclut pas, sans
analyse supplémentaire, toute déformation ayant un espace total singulier.

### 3.2 Modèle local avec normales non triviales mais opposées

Soit \(L\in\operatorname{Pic}(S)\) un fibré non trivial. Dans

\[
\operatorname{Tot}(L\oplus L^{-1})\times\mathbb A^1_t,
\]

considérons l'équation globale donnée par l'appariement naturel

\[
\mathfrak X_L=\{uv=t\}.
\]

L'espace total est lisse puisque la dérivée par rapport à \(t\) vaut \(-1\).
Sa fibre centrale possède deux composantes,

\[
\{u=0\}=\operatorname{Tot}(L^{-1}),\qquad
\{v=0\}=\operatorname{Tot}(L),
\]

qui se coupent le long de la section nulle \(S\). Leurs normales sont

\[
N_1\simeq L^{-1},\qquad N_2\simeq L,\qquad
N_1\otimes N_2\simeq\mathcal O_S.
\]

C'est un modèle local semistable parfaitement lisse malgré la non-trivialité
individuelle des normales. Dans un futur calcul métrique, ce cas conduit à un
plombage tordu par \(L\), et non à une coordonnée normale globale unique.

## 4. Cohomologie : ce que l'adjonction prouve et ne prouve pas

Soit \(Y\) un trois-fold projectif lisse connexe et
\(S\in|-K_Y|\) une K3 lisse connexe. La suite exacte est

\[
0\longrightarrow K_Y\longrightarrow\mathcal O_Y
\longrightarrow\mathcal O_S\longrightarrow0.
\]

La flèche \(H^0(\mathcal O_Y)\to H^0(\mathcal O_S)\) est un isomorphisme.
En combinant la suite longue avec la dualité de Serre, on obtient

\[
h^3(Y,\mathcal O_Y)=h^0(Y,K_Y)=0,\qquad
h^1(Y,\mathcal O_Y)=h^2(Y,\mathcal O_Y),
\]

mais **pas** leur annulation. L'adjonction et le mot « K3 » ne remplacent donc
pas le certificat cohomologique de R63.

Deux modèles jouets montrent immédiatement où les versions affaiblies
échouent :

1. Pour \(Y=S_0\times\mathbb P^1\), où \(S_0\) est une K3,
   \(F_0\sqcup F_\infty\in|-K_Y|\) est un diviseur lisse mais déconnecté,
   réunion de deux K3, tandis que
   \(H^2(Y,\mathcal O_Y)\simeq\mathbb C\).
2. Pour \(Y=E\times\mathbb P^2\), où \(E\) est elliptique, un membre
   anticanonique est \(S=E\times C\), avec \(C\subset\mathbb P^2\) cubique
   lisse. Il est connexe, lisse et \(K_S\simeq\mathcal O_S\), mais ce n'est pas
   une K3 : \(h^1(S,\mathcal O_S)=2\), et
   \(h^1(Y,\mathcal O_Y)=1\).

Ces exemples ne contredisent pas l'énoncé complet de R63 ; ils montrent que ni
la connexité ni la condition cohomologique ne peuvent être effacées en
remplaçant « K3 » par « \(K\)-triviale » ou « union lisse de K3 ». Le calcul
torique/EMS de R63 reste donc une preuve substantielle.

## 5. Couture spéciale de Noether–Lefschetz : classe supplémentaire explicite

Écrivons \(Q=\mathbb P^1_x\times\mathbb P^1_y\) et prenons une forme
\(g_2(y)\) de degré deux à racines simples. Pour un \(h_{3,4}\) général, la
courbe

\[
B:\quad x_1^4g_2(y)^2+x_0h_{3,4}(x,y)=0
\]

est de bidegré \((4,4)\). Aux deux points de base situés sur
\(x_0=g_2=0\), choisir \(h_{3,4}\neq0\) rend la dérivée normale non nulle ;
Bertini traite le complément. Il existe donc des choix pour lesquels \(B\)
est lisse.

La double couverture

\[
\pi:S\longrightarrow Q,\qquad
w^2=x_1^4g_2(y)^2+x_0h_{3,4}(x,y)
\]

est alors une K3 lisse. Posons

\[
A=\pi^*\mathcal O_Q(1,0),\qquad
B_0=\pi^*\mathcal O_Q(0,1).
\]

On a

\[
A^2=B_0^2=0,\qquad A\cdot B_0=2,
\]

donc \(\langle A,B_0\rangle\simeq U(2)\). Mais au-dessus de la fibre
\(x_0=0\), l'équation se factorise :

\[
\pi^{-1}(x_0=0)=C_+\cup C_-,\qquad
C_\pm:\ w=\pm x_1^2g_2(y).
\]

Les \(C_\pm\) sont rationnelles. Elles se coupent aux deux zéros de \(g_2\),
et l'adjonction sur une K3 donne

\[
C_+^2=C_-^2=-2,\qquad C_+\cdot C_-=2.
\]

La classe \(\delta=C_+-C_-\) vérifie

\[
\delta\cdot A=\delta\cdot B_0=0,\qquad \delta^2=-8.
\]

Ainsi

\[
U(2)\oplus\langle-8\rangle\subseteq\operatorname{NS}(S),
\]

et le rang de Picard est au moins trois. Le qualificatif « très générale » de
R63 est donc réellement nécessaire pour conclure
\(\operatorname{NS}(S)=U(2)\).

### 5.1 Nuance décisive pour la LMHS

Un saut de \(\operatorname{NS}(S)\) ne change pas automatiquement la LMHS.
Celle-ci dépend de

\[
L=\operatorname{im}\left(
H^2(Y_1,\mathbb Z)\oplus H^2(Y_2,\mathbb Z)
\longrightarrow H^2(S,\mathbb Z)\right),
\]

et non de tout \(\operatorname{NS}(S)\).

- Si \(\delta\) ne se prolonge à aucune composante, \(L=U(2)\), \(r=2\), et
  II_18 peut rester inchangé.
- Si \(\delta\in L\), alors \(r=3\). En gardant \(b_3=172\), les formules de
  R63 donnent

  \[
  \dim(\operatorname{Gr}^W_2,\operatorname{Gr}^W_3,
  \operatorname{Gr}^W_4)=(19,134,19),\qquad \mathrm{II}_{17}.
  \]

Il existe un mécanisme géométrique explicite qui fait entrer une classe de
courbe dans l'image : si \(C\subset S\subset Y\), alors pour
\(\widetilde Y=\operatorname{Bl}_C(Y)\), la transformée stricte
\(\widetilde S\simeq S\) reste anticanonique, car

\[
K_{\widetilde Y}=\rho^*K_Y+E,\qquad
\widetilde S=\rho^*S-E=-K_{\widetilde Y},
\]

et \(E|_{\widetilde S}=C\). Cette modification change aussi la normale de la
couture ; la composante opposée doit donc être ajustée pour restaurer la
d-semistabilité. Elle prouve le mécanisme de saut de \(L\), pas à elle seule
l'existence d'un nouveau lissage global ayant encore \((5,85)\).

## 6. Involution échangeant les rulings : même action algébrique, deux parités

Choisissons une branche lisse \((4,4)\) symétrique sous
\((x,y)\leftrightarrow(y,x)\). L'échange des facteurs admet deux relèvements :

\[
\sigma_+(x,y,w)=(y,x,w),\qquad
\sigma_-(x,y,w)=(y,x,-w).
\]

Ils ont la **même** action sur le réseau des rulings :

\[
A\longleftrightarrow B_0,\qquad
[\sigma^*]_{(A,B_0)}=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Dans la base

\[
h=A+B_0,\qquad d=A-B_0,
\]

on obtient

\[
\sigma^*h=h,\qquad \sigma^*d=-d,\qquad
h^2=4,\quad d^2=-4,\quad h\cdot d=0.
\]

Une polarisation \(H=aA+bB_0\), \(a,b>0\), est envoyée sur
\(bA+aB_0\) : elle n'est fixée que si \(a=b\), même si le réseau \(U(2)\) est
préservé comme ensemble.

Localement, une forme holomorphe est proportionnelle à

\[
\Omega=\frac{dx\wedge dy}{w}.
\]

L'échange \(x\leftrightarrow y\) change le signe du numérateur. Par conséquent

\[
\sigma_+^*\Omega=-\Omega,\qquad
\sigma_-^*\Omega=+\Omega.
\]

Le premier relèvement est non symplectique et le second symplectique, bien
qu'ils aient la même matrice sur \(U(2)\). Pour une branche générique
transverse à la diagonale, les huit points de branche sur la diagonale sont
compatibles avec les huit points fixes du relèvement symplectique.

**Conséquence pour le no-go.** Ni le nom sigma5, ni l'échange des composantes,
ni la matrice sur les seuls diviseurs toriques ne déterminent la parité du
secteur transcendant. Il faut fixer le relèvement sur \(w\), son action sur
\(H^{2,0}\), puis la matrice intégrale sur le réseau K3 marqué.

## 7. Classe transcendante isotrope : un vecteur n'est pas encore un état

Pour la K3 très générale de R63,

\[
\operatorname{NS}(S)=U(2),\qquad
T(S)=\operatorname{NS}(S)^\perp
\simeq U\oplus U(2)\oplus E_8(-1)^{\oplus2}.
\]

Dans le premier facteur \(U=\langle e,f\rangle\), prenons

\[
\gamma=e,\qquad \gamma^2=0.
\]

C'est une classe intégrale primitive isotrope du secteur transverse. Pourtant,
puisque \(\operatorname{NS}(S)=U(2)\), aucun vecteur intégral non nul de
\(T(S)\) n'est de type \((1,1)\). En particulier,

\[
\gamma\notin H^{1,1}(S),
\]

et \(\gamma\) n'est la classe d'aucun diviseur ou courbe algébrique sur la
couture très générale.

La condition de Noether–Lefschetz

\[
(\gamma,\Omega)=0
\]

est de codimension un dans l'espace des périodes. Sur ce lieu spécial,
\(\gamma\) devient algébrique ; après choix de chambre nef, une classe
primitive isotrope effective peut définir une fibration elliptique. Mais on a
alors quitté le régime \(\operatorname{NS}(S)=U(2)\).

Cette observation ne nie pas l'existence du cycle topologique représenté par
\(\gamma\). Elle interdit seulement le raccourci

\[
\text{vecteur isotrope intégral}
\Longrightarrow\text{cycle calibré stable}
\Longrightarrow\text{état D3/BPS}
\Longrightarrow\text{tour}.
\]

Les deux dernières flèches exigent calibration ou stabilité, période/masse,
parité correcte et calcul du spectre.

## 8. Formulation plus générale qui survit

### Proposition R64-G — noyau géométrique robuste

Soit \(\mathcal X\to\Delta\) une dégénérescence projective semistable à espace
total lisse, dont les fibres générales sont des Calabi–Yau, et de fibre
centrale \(X_0=Y_1\cup_S Y_2\), où \(Y_1,Y_2\) sont lisses et \(S\) est une
K3 lisse connexe anticanonique dans chaque composante. Alors

\[
N_{S/Y_1}\otimes N_{S/Y_2}\simeq\mathcal O_S.
\]

Si, en plus,

\[
H^i(Y_j,\mathcal O_{Y_j})=0\quad(i>0),
\]

les \(Y_j\) sont quasi-Fano dans la convention Doran–Harder–Thompson et la
famille est une dégénérescence de Tyurin dans cette convention. Il n'est pas
nécessaire que \(S\) soit une fibre dans chaque \(Y_j\), ni que les deux
normales soient individuellement triviales.

Cette proposition conserve le cœur de R63 tout en séparant la propriété
générale de Tyurin de la propriété plus rigide de POLY944/sigma5.

### Proposition R64-L — LMHS avec rang variable

Il faut calculer l'image réelle

\[
L=\operatorname{im}(H^2(Y_1,\mathbb Z)\oplus H^2(Y_2,\mathbb Z)
\to H^2(S,\mathbb Z)),\qquad r=\operatorname{rank}L.
\]

Sur \(\mathbb Q\), sous les hypothèses de Clemens–Schmid utilisées en R63,

\[
\operatorname{Gr}^W_2H^3_{\lim}
\simeq H^2(S,\mathbb Q)/L_\mathbb Q,\qquad
\dim\operatorname{Gr}^W_2=22-r.
\]

Si les classes de \(L\) sont algébriques, l'indice vaut

\[
b=20-r.
\]

Pour le lissage R63 avec \(b_3=172\),

\[
\dim\operatorname{Gr}^W_3=172-2(22-r)=128+2r.
\]

Ainsi II_18 est le cas \(r=2\), et non une conséquence du seul mot
« couture \((4,4)\) ». Un saut de Picard impose un nouveau calcul de \(L\), pas
automatiquement un changement de type.

### Proposition R64-E — no-go équivariant robuste

La partie du no-go qui résiste aux exemples ci-dessus peut être formulée sans
demander que chaque générateur de \(L\) soit fixé :

> Si \(\sigma\) est une involution holomorphe **non symplectique**, si elle
> préserve \(L\), et si \(L\cap H^2(S,\mathbb Z)^\sigma\) contient une classe
> ample \(h\), alors
> \[
> L^\perp\cap H^2(S,\mathbb Z)^\sigma
> \]
> est négatif défini. Il ne contient donc aucun vecteur isotrope non nul.

La preuve est l'indice de Hodge : pour une involution non symplectique, le
réseau invariant est de type \((1,1)\), et l'orthogonal d'une classe ample y
est négatif défini. L'échange \(A\leftrightarrow B_0\) est autorisé puisque
\(h=A+B_0\) reste ample et invariant.

Dans le cas symplectique, l'argument précédent ne s'applique pas ; le no-go
anti-invariant de type Nikulin demande de prouver que le relèvement est bien
symplectique et que la classe physique appartient réellement au réseau
anti-invariant \(E_8(-2)\). Les deux relèvements \(\sigma_\pm\) montrent
pourquoi cette hypothèse ne peut pas être inférée de l'action sur \(U(2)\).

## 9. Conséquence opérationnelle pour \(R(t)\) et la tour

R64 ne doit pas partir de « normale triviale \(\Rightarrow R=-\log|t|\) ». Le
cadre robuste doit accepter \(N_2\simeq N_1^{-1}\) et définir :

1. une famille de métriques Ricci-plates à volume fixé ;
2. une longueur de col intrinsèque, indépendante de \(t\mapsto ct\) ;
3. le fibré normal et sa connexion lorsque \(N_1\) est non trivial ;
4. une classe intégrale marquée \(\gamma\), sa période et sa parité ;
5. un critère de calibration/stabilité avant de parler d'état BPS ;
6. le calcul spectral qui distingue KK, D3 et oscillateurs.

Le noyau Tyurin de R63 survit donc au stress-test. Ce qui ne survit pas est le
passage automatique

\[
\text{Tyurin}+\mathrm{II}_{18}
\Longrightarrow R\text{ physique}
\Longrightarrow \text{tour micrométrique}.
\]

## 10. Reproductibilité

Commande :

    python3 meta_audit_r64/r64_boundary_certificate.py

Sortie attendue :

    R64 BOUNDARY CERTIFICATE
    non-fibre model: integral_S c1(N)^2 = 10
    P3 quartic double: integral_S c1(N1 tensor N2)^2 = 256
    det U(2) = -4
    det NL lattice U(2)+<-8> = 32
    ruling swap eigen-squares = (4, -4)
    LMHS r=2: GrW(2,3,4), II_b = (20, 132, 20, 18)
    LMHS r=3: GrW(2,3,4), II_b = (19, 134, 19, 17)
    primitive transverse e has e^2 = 0
    VERDICT: EXACT_ARITHMETIC_PASS

## 11. Sources primaires

1. C. F. Doran, A. Harder, A. Y. Thompson, *Mirror symmetry, Tyurin
   degenerations and fibrations on Calabi–Yau manifolds*, §2.1 et §5,
   [arXiv:1601.08110](https://arxiv.org/abs/1601.08110).
2. R. Friedman, *Global smoothings of varieties with normal crossings*,
   **Annals of Mathematics 118** (1983), 75–114,
   [doi:10.2307/2006955](https://doi.org/10.2307/2006955).
3. Y. Kawamata, Y. Namikawa, *Logarithmic deformations of normal crossing
   varieties and smoothing of degenerate Calabi–Yau varieties*,
   **Inventiones Mathematicae 118** (1994), 395–409,
   [doi:10.1007/BF01231538](https://doi.org/10.1007/BF01231538).
4. A. Fortuna, *The Kodaira dimension of some moduli spaces of elliptic K3
   surfaces*, §5.1 pour les doubles couvertures \((4,4)\) et \(U(2)\),
   **J. London Math. Soc.** (2021),
   [doi:10.1112/jlms.12430](https://doi.org/10.1112/jlms.12430).
5. B. van Geemen, A. Sarti, *Nikulin involutions on K3 surfaces*, pour le
   réseau anti-invariant \(E_8(-2)\),
   [arXiv:math/0602015](https://arxiv.org/abs/math/0602015).

## 12. Verdict R64-counterexamples

    R63_STRICT_TYURIN_CORE = SURVIVES
    T_AS_FIBRE = MODEL_SPECIFIC_SUFFICIENT_CONDITION
    INDIVIDUAL_NORMAL_TRIVIALITY = NOT_NECESSARY
    PRODUCT_NORMAL_TRIVIALITY = NECESSARY_FOR_SMOOTH_SEMISTABLE_TOTAL_SPACE
    COHOMOLOGY_VANISHING = NOT_IMPLIED_BY_ADJUNCTION_ALONE
    VERY_GENERAL_NS_U2 = NECESSARY_FOR_THE_NS_EQUALITY
    NL_JUMP_ALONE_CHANGES_LMHS = FALSE
    LMHS_DEPENDS_ON_ACTUAL_RESTRICTION_IMAGE_L = TRUE
    DIVISOR_ACTION_DETERMINES_INVOLUTION_PARITY = FALSE
    ISOTROPIC_INTEGRAL_CLASS_IMPLIES_BPS_STATE = FALSE
    GENERALIZED_EQUIVARIANT_NO_GO = SURVIVES_WITH_EXPLICIT_HYPOTHESES

