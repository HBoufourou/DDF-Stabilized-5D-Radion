# R63 — Audit canonique relatif, logarithmique et LMHS de la famille R62

**Périmètre.** Ce rapport concerne exclusivement la famille relative résolue
`sigma5` de `POLY944` construite en R62. Aucun résultat, réseau, flux, modèle de
stabilisation ou argument métrique de `POLY925` n'est transporté ici.

## 1. Verdict

| Question | Verdict R63 | Portée exacte |
|---|---:|---|
| La famille est-elle semi-stable après restriction à un petit disque ? | **Oui** | espace total lisse, fibre centrale réduite SNC à deux composantes |
| Le morphisme logarithmique est-il log-lisse et saturé ? | **Oui** | cartes locales `t=u` et `t=uv`; monoïdes `N -> N` et `N -> N²`, `1 -> (1,1)` |
| La fibre centrale est-elle d-semi-stable ? | **Oui** | \(T^1\simeq N_{S/Y_p}\otimes N_{S/Y_m}\simeq\mathcal O_S\) ; le rapport quasi-Fano R63 montre même que les deux normales sont individuellement triviales |
| Le canonique relatif/logarithmique est-il trivial ? | **Oui** | `Y` est anticanonique dans le cinq-fold torique relatif lisse et `K_A1` est trivial |
| La monodromie est-elle unipotente sans changement de base caché ? | **Oui** | semi-stabilité réduite et paramètre primitif `t=pm` |
| Le rang de restriction est-il exactement et primitivement `r=2` ? | **Oui, pour un membre très général** | image intégrale `L=NS(S)=U(2)`, primitive dans le réseau K3 |
| La LMHS est-elle de type `II_18` ? | **Oui sur `Q`/`C`** | `N²=0`, `rank N=20`, gradués `(20,132,20)` |
| La LMHS est-elle polarisée ? | **Oui** | conséquence de la variation de Hodge polarisée d'une famille projective lisse sur le disque ponctué |
| La SNF intégrale complète de la vraie monodromie est-elle calculée par le script R61 ? | **Pas encore** | `(1^18,2,2)` est exact pour le morphisme canonique de réseaux `T(S) -> Lambda_K3/L`; son identification avec la SNF du `N` de Gauss–Manin sur tout \(H^3(Y_t,\mathbb Z)\) exige encore l'argument intégral de cycles proches/torsion |

La porte géométrique R63 est donc **GO** : avec le certificat quasi-Fano
compagnon, la famille est une dégénérescence de Tyurin stricte au sens de
Doran–Harder–Thompson. La formulation `II_18` est publiable sur les rationnels
et les complexes. La seule réserve de cette partie concerne l'élévation de la
forme de Smith du modèle de réseau au statut de forme de Smith de la monodromie
intégrale complète.

## 2. Entrées recalculées

Les deux certificats antérieurs ont été réexécutés sans modification :

```text
r62_stable_fan_parity_stop_audit.py
SHA256 = 9a7db858d0438022be5d3bf6566876278a083701fb3f70330ad01fb0743d1b22

R62_AUDIT_OUTPUT.txt
SHA256 = 9b8d3c5642cac79886c243e7ea38985bd6ea58398988e72469f9e7c02240c2bc

r61_resolved_tyurin_lmhs_audit.py
SHA256 = eb3fefc077199f28a431940dcbd9d5006f3a5820a503ca0e9a1652b71ecc4fff
```

Les entrées utilisées dans le présent audit sont :

- un éventail relatif 5D lisse, cohérent et propre sur `A1`, avec 28 cônes
  maximaux unimodulaires ;
- la fonction torique globale `t=pm` et
  `div(t)=D_p+D_m`, avec multiplicité un ;
- une hypersurface relative anticanonique générique `mathcal Y` lisse ;
- une fibre centrale
  `Y_0=Y_p union_S Y_m`, où `Y_p`, `Y_m` et `S` sont lisses, les deux
  composantes sont irréductibles et `S` a la codimension attendue ;
- le type topologique du lissage
  `(h11,h21)=(5,85)`, donc `b3=172` ;
- une couture très générale qui est la double couverture de
  `P1 x P1` ramifiée sur une courbe `(4,4)` et dont
  `NS(S)=U(2)`.

Le calcul R62 de Bertini et du jet unité ne donne pas seulement trois variétés
lisses séparées. La lissité de `mathcal Y`, de `Y_p`, de `Y_m` et de leur
intersection lisse de codimension deux implique que les deux diviseurs centraux
se rencontrent transversalement dans `mathcal Y`.

## 3. Formes locales et log-lissité saturée

La projection du réseau torique relatif sur sa cinquième coordonnée envoie les
neuf anciens rayons sur zéro, et les rayons `p,m` sur un. Le caractère dual
définissant la base a donc le diviseur

\[
\operatorname{div}(t)=D_p+D_m.
\]

Sur les cartes unimodulaires de l'ambiant, le morphisme est de la forme

\[
t=u,\qquad t=v,\qquad\text{ou}\qquad t=uv.
\]

Comme l'hypersurface totale et toutes les strates centrales sont transverses,
ces mêmes expressions fournissent, après un changement de coordonnées étale ou
analytique, les formes locales du morphisme restreint

\[
f:\mathcal Y\longrightarrow\Delta.
\]

Aux points lisses d'une composante, la carte caractéristique est

\[
\mathbb N\longrightarrow\mathbb N,\qquad 1\longmapsto1.
\]

Sur la couture, elle est

\[
\mathbb N\longrightarrow\mathbb N^2,
\qquad 1\longmapsto(1,1).
\]

Les formes normales de Smith de ces deux inclusions sont toutes deux
`diag(1)`. Le conoyau en groupes de la seconde est libre de rang un. Ces cartes
sont donc intégrales, saturées et log-lisses. En particulier, il ne se cache ni
indice `k>1` ni modèle local `uv=t^k`.

Après avoir rétréci autour de zéro pour éviter les autres valeurs critiques, on
obtient une famille projective et lisse sur `Delta*`, avec espace total lisse et
fibre centrale réduite SNC. C'est précisément une famille semi-stable.

## 4. d-semistabilité comme isomorphisme de fibrés

Pour une union SNC à deux composantes, le faisceau de déformations locales sur
la couture est

\[
T^1_{Y_0}\simeq
N_{S/Y_p}\otimes N_{S/Y_m}.
\]

Or `Y_p+Y_m=div(t)` dans `mathcal Y`. En restreignant à `S`, on obtient un
isomorphisme de fibrés, et pas seulement une égalité de premières classes de
Chern :

\[
\begin{aligned}
N_{S/Y_p}\otimes N_{S/Y_m}
&\simeq
\mathcal O_{\mathcal Y}(Y_m)|_S
\otimes\mathcal O_{\mathcal Y}(Y_p)|_S\\
&\simeq
\mathcal O_{\mathcal Y}(Y_p+Y_m)|_S\\
&\simeq\mathcal O_S.
\end{aligned}
\]

La section de lissage provenant de `t` est partout non nulle dans cette
trivialisation. La fibre centrale est donc d-semi-stable. Le certificat
`quasifano_normal_bundles.md` renforce ce résultat en identifiant `S` comme une
fibre torique dans chaque composante ambiante et conclut

\[
N_{S/Y_p}\simeq\mathcal O_S,
\qquad
N_{S/Y_m}\simeq\mathcal O_S.
\]

Cette propriété renforcée n'est pas nécessaire à la d-semistabilité : le
produit trivial est la condition intrinsèque requise.

## 5. Canonique relatif et canonique logarithmique

Notons `mathcal X` le cinq-fold torique relatif lisse. Le contrôle des degrés de
Cox en R62 donne

\[
[\mathcal Y]=\sum_{\rho}D_\rho=-K_{\mathcal X}.
\]

L'adjonction fournit donc

\[
K_{\mathcal Y}\simeq\mathcal O_{\mathcal Y}.
\]

Comme `K_Delta` est trivial,

\[
\omega_{\mathcal Y/\Delta}\simeq\mathcal O_{\mathcal Y}.
\]

Pour les structures logarithmiques divisorielles données par `Y_0` et le point
`0`,

\[
\omega^{\log}_{\mathcal Y/\Delta}
=\omega_{\mathcal Y}(Y_0)\otimes
f^*\omega_\Delta(0)^{-1}
\simeq\omega_{\mathcal Y/\Delta}
\simeq\mathcal O_{\mathcal Y},
\]

car `Y_0=f^*(0)`. Sur les composantes centrales, la même identité donne

\[
K_{Y_p}+S=0,
\qquad
K_{Y_m}+S=0.
\]

Le rapport compagnon ferme en outre
`H^i(Y_p,O)=H^i(Y_m,O)=0` pour `i>0`. Ainsi les deux composantes sont bien
quasi-Fano selon la définition de Doran–Harder–Thompson : variété lisse, système
anticanonique contenant un Calabi–Yau lisse et annulation de toute cohomologie
supérieure de `O`.

## 6. Unipotence et polarisation

Une famille semi-stable complexe projective possède une monodromie locale
unipotente. Ici ce résultat ne nécessite aucun changement de base supplémentaire :
`t=pm` est déjà réduit et les cartes de monoïdes sont saturées. En posant

\[
T_{\rm mon}=\exp(N),
\qquad
N=\log T_{\rm mon},
\]

le nombre de composantes pouvant se rencontrer est deux. Le complexe de poids
n'a donc, pour `H^3`, que les poids 2, 3 et 4 ; par conséquent

\[
N^2=0.
\]

La restriction de la famille à `Delta*` est une famille projective de
Calabi–Yau lisses. Une classe relativement ample polarise la variation de
structure de Hodge sur `H^3`. Les théorèmes de Schmid–Steenbrink donnent alors
une LMHS polarisée. C'est cet argument géométrique qui établit la polarisation.

Le test matriciel de R61,

```text
(I+N)^T eta (I+N)=eta
signature(eta N)=(2,18),
```

est un excellent contrôle de cohérence d'un modèle de réseau, mais il ne peut
pas remplacer le théorème de polarisation appliqué à la famille effective.

## 7. Rang de restriction : pourquoi `r=2` est maintenant fermé

Le script R61 trouve, pour les classes toriques, la matrice

\[
\rho_B=
\begin{pmatrix}
1&0&0&0&0\\
0&1&0&0&0
\end{pmatrix},
\qquad
\operatorname{SNF}(\rho_B)=\operatorname{diag}(1,1).
\]

Cette matrice seule prouve que les deux rulings engendrent primitivement une
copie de `U(2)` dans l'image ; elle ne suffisait pas, à elle seule, à exclure
des restrictions non toriques supplémentaires.

R63 ferme précisément cette lacune :

1. `H^2(Y_p,O)=H^2(Y_m,O)=0`, donc, par la suite exponentielle, toutes les
   classes intégrales de degré deux des deux quasi-Fano sont algébriques ;
2. leur restriction à la K3 appartient donc à `NS(S)` ;
3. pour une couture très générale de la famille `(4,4)`,
   `NS(S)=U(2)` ;
4. les deux générateurs de ce `U(2)` sont déjà dans l'image et la SNF vaut
   `(1,1)`.

Ainsi

\[
L:=\operatorname{im}\bigl(
H^2(Y_p,\mathbb Z)\oplus H^2(Y_m,\mathbb Z)
\longrightarrow H^2(S,\mathbb Z)
\bigr)=U(2),
\]

et cette image est primitive dans le réseau K3. En particulier,

\[
r=\operatorname{rank}L=2,
\qquad
H^2(S,\mathbb Z)/L\ \text{est libre de rang }20.
\]

La mention « très général » est essentielle : sur un diviseur de
Noether–Lefschetz, `NS(S)` peut sauter et le type `II_b` doit alors être
recalculé.

## 8. Clemens–Schmid et type exact `II_18`

Pour la fibre à deux composantes, Mayer–Vietoris puis Clemens–Schmid donnent,
sur `Q` ou `C`,

\[
\operatorname{Gr}^W_2 H^3_{\lim}
\simeq
\frac{H^2(S)}{
\operatorname{im}H^2(Y_p)+\operatorname{im}H^2(Y_m)}.
\]

La source primaire directement adaptée est la section 5 de
Doran–Harder–Thompson : leur calcul donne précisément
`GrW2=H²(S,Q)/(im r_p+im r_m)`, puis utilise la suite exacte de
Clemens–Schmid pour obtenir le diamant limite. La même dérivation est détaillée
dans Hassfeld–Monnee–Weigand–Wiesner, équations (C.10)–(C.16). Il ne s'agit donc
pas d'une extrapolation depuis le seul comptage de Hodge du lissage.

Les hypothèses auxiliaires employées dans cette source sont également
satisfaites ici. Les annulations quasi-Fano donnent
`H^1(Y_p,Q)=H^1(Y_m,Q)=0`, donc `H_5(Y_p,Q)=H_5(Y_m,Q)=0` par dualité. Dans la
suite de Mayer–Vietoris, la classe fondamentale de la K3 est envoyée sur ses
deux classes de diviseur anticanonique, non nulles dans des trois-folds
projectifs. Le morphisme
\(H_4(S,\mathbb Q)\to H_4(Y_p,\mathbb Q)\oplus H_4(Y_m,\mathbb Q)\) est donc
injectif et `H_5(Y_0,Q)=0`, comme requis dans le lemme 5.2 de cette dérivation.

Comme `b2(S)=22` et `r=2`,

\[
\dim\operatorname{Gr}^W_2=20.
\]

La monodromie polarisée induit un isomorphisme

\[
N:\operatorname{Gr}^W_4\xrightarrow{\sim}
\operatorname{Gr}^W_2,
\]

donc

\[
\dim\operatorname{Gr}^W_4=20,
\qquad
\operatorname{rank}N=20.
\]

Le lissage possède `b3=2 h21+2=172`. Il reste alors

\[
\dim\operatorname{Gr}^W_3=172-20-20=132.
\]

Le quotient de la K3 par `L=U(2)` a les types de Hodge

\[
(2,0):1,qquad(1,1):18,qquad(0,2):1.
\]

Dans la convention standard où le sous-indice de `II_b` vaut
`b=dim I^{1,1}`, on obtient donc

\[
\boxed{\mathrm{LMHS}=\mathrm{II}_{18}}.
\]

Le diamant de Hodge–Deligne est

| Gradin | `GrF3` | `GrF2` | `GrF1` | `GrF0` | Dimension |
|---|---:|---:|---:|---:|---:|
| `GrW4` | 1 | 18 | 1 | 0 | 20 |
| `GrW3` | 0 | 66 | 66 | 0 | 132 |
| `GrW2` | 0 | 1 | 18 | 1 | 20 |

et

\[
\operatorname{Jordan}(T_{\rm mon})
=J_2(1)^{20}\oplus J_1(1)^{132}.
\]

Cette conclusion porte sur la LMHS de la famille résolue de `POLY944`, de
Hodge `(5,85)`. Elle ne porte ni sur `POLY925`, ni sur une tour BPS, ni sur une
tour KK, ni sur la longueur métrique du col, ni sur la valeur de `R`.

## 9. Audit de l'affirmation intégrale `SNF(N)=(1^18,2,2,0^152)`

Le réseau de la K3 est

\[
\Lambda_{K3}=U^{\oplus3}\oplus E_8(-1)^{\oplus2}.
\]

Avec l'inclusion primitive géométrique `L=U(2)`, son orthogonal est

\[
T(S)=L^\perp\simeq
U\oplus U(2)\oplus E_8(-1)^{\oplus2},
\]

de rang 20, signature `(2,18)` et déterminant 4. Le morphisme naturel de
réseaux

\[
\bar N:T(S)\longrightarrow\Lambda_{K3}/L
\]

a bien

\[
\operatorname{SNF}(\bar N)=(1^{18},2,2),
\qquad
\operatorname{coker}(\bar N)\simeq(\mathbb Z/2)^2.
\]

Ce calcul est exact. Il exprime le recollement d'indice quatre de `L` et de
son orthogonal dans le réseau K3 unimodulaire. Il faut toutefois distinguer
trois énoncés :

1. **Démontré :** `L` est primitif et le quotient `Lambda_K3/L` est sans
   torsion ;
2. **Démontré :** le morphisme canonique de réseaux gradués ci-dessus a la SNF
   `(1^18,2,2)` ;
3. **Pas démontré par le code actuel :** la matrice de la vraie monodromie
   Gauss–Manin sur le réseau intégral complet `H^3(Y_t,Z)/tors` possède, après
   choix de bases intégrales, exactement cette SNF avec 152 zéros.

En effet, `lmhs_and_monodromy_audit()` dans le script R61 construit une matrice
symplectique abstraite par blocs à partir de la forme de Gram de `T(S)`. Il ne
calcule ni le transport parallèle des cycles de la famille R62, ni la matrice
de Gauss–Manin, ni le complexe intégral des cycles proches. L'assertion complète
est attendue par le modèle semi-stable primitif, mais, pour devenir un théorème
de l'article, elle doit être reliée explicitement à une version intégrale du
complexe de poids et accompagnée du contrôle de torsion pertinent.

### Fermeture minimale de cette réserve

Deux voies sont acceptables :

- **voie théorique :** citer un théorème intégral précis identifiant le
  morphisme `GrW4 -> GrW2` de cette dégénérescence semi-stable à
  `T(S) -> Lambda_K3/L`, puis vérifier toutes ses hypothèses de torsion ;
- **voie calculatoire :** obtenir la monodromie intégrale d'une base de cycles
  par cycles proches/Gauss–Manin et comparer directement sa SNF.

Tant que cette ligne manque, l'article doit annoncer la SNF comme celle du
**morphisme canonique de réseau K3 associé au gradué**, et non comme une matrice
de monodromie intégrale directement calculée sur les 172 dimensions.

## 10. Formulations autorisées pour l'article

### Formulation forte, démontrée

> For a very general member, the resolved `POLY944` family defines a
> projective saturated log-smooth Tyurin degeneration with trivial relative
> log canonical bundle. Its primitive restriction lattice is `U(2)`, and its
> polarized rational limiting mixed Hodge structure is of type `II_18`, with
> graded dimensions `(20,132,20)`.

### Formulation intégrale prudente

> The canonical K3 graded lattice map has elementary divisors
> `(1^18,2,2)` and cokernel `(Z/2)^2`.

### Formulations à ne pas employer encore

- « nous avons calculé directement la matrice de Gauss–Manin intégrale » ;
- « vingt périodes logarithmiques indépendantes ont été explicitement
  développées » ;
- « la LMHS démontre une longueur physique ou `R` » ;
- « `II_18` démontre une tour KK ou une tour BPS stable » ;
- toute transposition des conclusions à `POLY925`.

## 11. Références de contrôle

1. C. F. Doran, A. Harder, A. Y. Thompson, *Mirror symmetry, Tyurin
   degenerations and fibrations on Calabi–Yau manifolds*,
   [arXiv:1601.08110](https://arxiv.org/abs/1601.08110). La définition utilisée
   d'une quasi-Fano et d'une dégénérescence de Tyurin est donnée au début de la
   section 2 ; la section 5, en particulier les formules précédant et suivant
   le lemme 5.2, donne les gradués de poids et le passage par Clemens–Schmid.
2. S. Hu, *Semi-Stable Degeneration of Toric Varieties and Their
   Hypersurfaces*, [arXiv:math/0110091](https://arxiv.org/abs/math/0110091).
3. B. Hassfeld, J. Monnee, T. Weigand, M. Wiesner, *Emergent Strings in Type
   IIB Calabi–Yau Compactifications*, JHEP 01 (2026) 140,
   [arXiv:2504.01066](https://arxiv.org/abs/2504.01066), notamment les sections
   2.1–2.2 et les appendices B–C pour la convention `II_b`, Mayer–Vietoris et
   Clemens–Schmid.
4. W. Schmid, *Variation of Hodge Structure: The Singularities of the Period
   Mapping*, Invent. Math. 22 (1973), 211–319.
5. R. Friedman, *Global smoothings of varieties with normal crossings*, Ann.
   of Math. 118 (1983), 75–114.

## 12. Décision R63-log/LMHS

```text
SATURATED_LOG_SMOOTH = YES
D_SEMISTABLE = YES
RELATIVE_AND_LOG_CANONICAL_TRIVIAL = YES
MONODROMY_UNIPOTENT_WITHOUT_BASE_CHANGE = YES
RESTRICTION_LATTICE = PRIMITIVE_U2_RANK_2_FOR_VERY_GENERAL_SEAM
POLARIZED_RATIONAL_LMHS = TYPE_II_18
GRW_2_3_4 = 20_132_20
INTEGRAL_K3_GRADED_MAP_SNF = 1^18_2_2
FULL_INTEGRAL_GAUSS_MANIN_SNF = NOT_YET_DIRECTLY_CERTIFIED
NO_POLY925_TRANSPORT = ENFORCED
```

La réserve intégrale ne renverse pas le verdict Tyurin strict ni le type
`II_18`. Elle fixe seulement la frontière entre un résultat de LMHS rationnelle
pleinement démontré et une identification intégrale plus fine qui doit encore
être documentée avant dépôt.

