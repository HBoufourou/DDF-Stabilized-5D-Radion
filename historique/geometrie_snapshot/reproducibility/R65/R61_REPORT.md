# R61 — LMHS résolue et parité sur la vraie couture de Tyurin

> **Correction de R60.** Les résultats géométriques de R60 sur la petite
> résolution, les nombres de Hodge et les tadpoles ne changent pas. En
> revanche, les conclusions « `C_safe` pair » et « `C_Nik` pair » concernaient
> la fibre spéciale `F0={x5=0}`, et non la K3 qui coud les deux composantes de
> la dégénérescence de Tyurin. R61 les retire pour la charge tubulaire.

## Verdict exécutif

R61 obtient un résultat positif important et un no-go précis.

| Question | Verdict | Statut |
|---|---|---|
| La résolution de R60 conserve-t-elle la tranche K3 ? | Oui : 7 points, 35 monômes et `rho_tor=2` | exact |
| Les deux demi-polytopes restent-ils projecting ? | Oui, avec `m0=(0,1,0,0)` et split intégral nul | exact |
| Le nouveau diviseur exceptionnel augmente-t-il le réseau de couture ? | Non : `E|S=0` et `Im(rho)=U(2)` primitivement | exact |
| Quel est le rang de restriction ? | `r=2` | exact au niveau torique intégral |
| Le CY résolu général admet-il une dégénérescence de Tyurin projective ? | Oui, par la construction torique cohérente issue de la fonction PL | théorème torique |
| Quel est le type de sa LMHS ordinaire ? | `Type II_18`, avec gradins `(20,132,20)` | exact |
| La famille relative 5D particulière de l’orientifold R60 est-elle déjà certifiée ? | Pas encore : le fan total et son Jacobien central restent à vérifier | ouvert fini |
| Action de `sigma5` sur la vraie couture | involution de revêtement, anti-symplectique | exact |
| Existe-t-il une charge active paire isotrope pour `sigma5` ? | Non : tout le bloc actif de rang 20 est impair | no-go exact |
| Action de `sigma125` sur la vraie couture | involution d’Enriques, et non Nikulin | exact |
| Existe-t-il une charge active paire isotrope pour `sigma125` ? | Non : le secteur pair actif est `E8(-2)`, négatif défini | no-go exact |

Le noyau géométrique de la théorie est donc conservé :

\[
\boxed{
R+\text{long col de Tyurin}+U(2)+\text{bloc actif de rang }20
}
\]

dans le parent non orientifoldé. Ce qui n’est pas récupéré par les deux
involutions actuelles est la **tour chargée paire** du compactifié `N=1`.

Le résumé honnête est :

```text
RESOLVED_PROJECTING_SLICE_CERTIFIED
PRIMITIVE_RESTRICTION_LATTICE_U2_AND_RANK_R2_CERTIFIED
ORDINARY_RESOLVED_TYURIN_LMHS_IS_TYPE_II18
SIGMA5_ACTUAL_SEAM_IS_DECK: ACTIVE_EVEN_RANK_ZERO
SIGMA125_ACTUAL_SEAM_IS_ENRIQUES: ACTIVE_EVEN_E8(-2)
NO_NONZERO_EVEN_ISOTROPIC_TYURIN_CHARGE_IN_EITHER_CURRENT_BRANCH
R60_EVEN_TOWER_PARITY_RETRACTED
```

## 1. Données résolues

On repart du polytope `POLY944` et de la phase positive de R60 obtenue en
ajoutant

\[
\nu_E=(1,1,0,0)=\nu_0+\nu_6.
\]

Le nouveau convexe est réflexif. Le comptage de Batyrev redonne

\[
\ell(\Delta^\circ_{\rm res})=10,
\qquad
\ell(\Delta_{\rm res})=104,
\]

\[
(h^{1,1},h^{2,1})=(5,85),
\qquad
\chi=-160.
\]

L’éventail résolu possède 20 cônes maximaux, tous unimodulaires et tous
contenus dans une facette du nouveau polytope.

Le nouvel idéal de Stanley--Reisner minimal contient

\[
(0,6),(0,7),(1,4),(2,3),(5,6),(5,E),(7,E).
\]

En particulier,

\[
D_5E=0.
\]

Le centre de R60 est donc disjoint du pôle `F0=D5`, et la classe
exceptionnelle se restreint trivialement à cette fibre.

## 2. Les tops et la tranche K3

Le normal primitif reste

\[
m_0=(0,1,0,0).
\]

Dans la base adaptée

\[
(a,b,c,d)\longmapsto(-a,c,d\,;b),
\]

les rayons hors tranche sont

| Rayon | Projection ; hauteur |
|---|---|
| `x5` | `(1,0,0;-1)` |
| `x6` | `(0,0,0;+1)` |
| `E` | `(-1,0,0;+1)` |

Leurs projections sont déjà des points de la tranche : celle de `x5` est le
point `x7`, celle de `x6` est l’origine et celle de `E` est le point `x0`.
Ainsi le split intégral est

\[
s=(0,0,0),
\]

et les deux côtés sont projecting.

La tranche possède sept points de réseau, cinq sommets et un seul point
intérieur à une facette. Son polaire possède cinq sommets et 35 points. Le
calcul torique donne

\[
\rho_{\rm tor}(S)=7-4-1+0=2.
\]

Les 20 cônes résolus se répartissent en

\[
12\text{ supérieurs},\qquad
8\text{ inférieurs},\qquad
0\text{ mixte}.
\]

Les huit cônes maximaux induits sur la tranche coïncident des deux côtés :

```text
012, 013, 024, 034, 127, 137, 247, 347.
```

Il existe une nuance importante. Le sommet du top positif contient deux
points de hauteur un, `x6` et `E`. Son morphisme interne vérifie donc

\[
w_+=x_6e,
\qquad
w_+^{-1}(0)=D_6\cup E.
\]

Il s’agit d’une fibre K3 réductible à l’intérieur du bâtiment `Z+`. Ce fait ne
crée pas automatiquement une troisième composante tridimensionnelle dans une
dégénérescence de Tyurin construite avec deux paramètres `zeta+`,`zeta-` ; il
impose toutefois de vérifier le fan relatif 5D au lieu de l’inférer des seules
données 4D.

## 3. Rang de restriction exact

Prenons la base intégrale

\[
B=(D_1,D_2,D_5,D_7,E).
\]

Les relations linéaires de diviseurs sont

\[
\begin{aligned}
D_0-2D_1-2D_2-D_5-D_7+E&=0,\\
-D_5+D_6+E&=0,\\
-D_1+D_4&=0,\\
-D_2+D_3&=0.
\end{aligned}
\]

La restriction à la K3 torique commune est

\[
\rho_B=
\begin{pmatrix}
1&0&0&0&0\\
0&1&0&0&0
\end{pmatrix}.
\]

Sur les neuf diviseurs coordonnées :

\[
\rho_{D_0,\ldots,D_8}=
\begin{pmatrix}
2&1&0&0&1&0&0&0&0\\
2&0&1&1&0&0&0&0&0
\end{pmatrix}.
\]

Si `h1,h2` sont les deux rulings de la double couverture de
`P1 x P1`, leur matrice d’intersection est

\[
\begin{pmatrix}0&2\\2&0\end{pmatrix}=U(2).
\]

La forme restreinte dans la base `B` est donc

\[
G_S=
\begin{pmatrix}
0&2&0&0&0\\
2&0&0&0&0\\
0&0&0&0&0\\
0&0&0&0&0\\
0&0&0&0&0
\end{pmatrix}.
\]

Enfin,

\[
\operatorname{SNF}(\rho_B)=\operatorname{diag}(1,1).
\]

La conclusion ne dépend donc pas d’un comptage de Picard seulement :

\[
\boxed{
\operatorname{Im}\rho=U(2)\text{ primitivement},
\qquad r=2,
\qquad\ker\rho=\langle D_5,D_7,E\rangle.
}
\]

Le nouveau module kählérien exceptionnel est vertical et ne modifie pas le
réseau de couture.

## 4. Candidat relatif explicite et verrou restant

Écrivons un point du polytope dual résolu sous la forme

\[
m=(a,q,c,d).
\]

Les 104 monômes se répartissent selon

```text
q=-1 : 10
q= 0 : 35
q=+1 : 34
q=+2 : 25.
```

Le pgcd des hauteurs non nulles vaut un : le paramètre est primitif.

Une rangée de charges Cox adaptée est

```text
wt(x5)=-1,  wt(x7)=+1,  wt(zeta+)=+1,  wt(zeta-)=-1,
```

toutes les autres coordonnées ayant poids nul. Pour le monôme `M_m`,

\[
\operatorname{wt}(M_m)=-e_5(m)+e_7(m)=q.
\]

La rangée `wt(x0)=-1, wt(E)=+1` est équivalente modulo les anciennes
relations GLSM, puisque `-e0+eE=q` également.

Le polynôme relatif candidat est donc

\[
\mathcal P=
\sum_{m\in\Delta_{\rm res}\cap M}
c_mM_m\,
\zeta_+^{\max(-q(m),0)}
\zeta_-^{\max(q(m),0)},
\qquad
z=\zeta_+\zeta_-.
\]

Chaque terme a poids nul. Aux valeurs non nulles de `z`, l’action torique
ramène la fibre au CY résolu. À `z=0`, les deux cartes gardent respectivement
les monômes `q>=0` et `q<=0`; leur intersection conserve exactement les 35
monômes `q=0` de la K3 commune.

Pour la sous-famille de 69 monômes invariante sous `sigma5`, la transformée
propre relative s’écrit plus explicitement

\[
\begin{aligned}
\mathcal P_{\sigma_5}={}&
\zeta_+x_0x_5^2x_7A^-_{2,2}
+x_5^2x_6x_7^2A^0_{4,4}
+c\,x_0^2E^2x_6\\
&+\zeta_-x_0E^2x_6^2x_7A^+_{2,2}
+\zeta_-^2E^2x_6^3x_7^2A^{++}_{4,4}.
\end{aligned}
\]

Les nombres de termes aux hauteurs `(-1,0,+1,+2)` sont

```text
(9,26,9,25).
```

La relation

\[
e_E=e_0+e_6-1
\]

certifie que `E` réalise bien la transformée propre de l’éclatement. À
`zeta+=zeta-=0`, les coordonnées `x5,x6,E` sont inversibles sur la couture et
on retrouve l’équation de la section 6.

La fonction linéaire par morceaux

\[
\psi(\nu)=\max(0,\langle m_0,\nu\rangle)
\]

est intégrale ; ses deux domaines sont les deux tops. Comme `h(E)=+1`, la
subdivision étoilée est entièrement contenue dans le domaine positif. Cela
montre que la résolution et la dégénérescence torique sont compatibles au
niveau combinatoire.

Pour une section anticanonique générale, la construction torique cohérente
donne ainsi une dégénérescence projective semistable

\[
X_0=Z_+\cup_S Z_-,
\qquad -K_{Z_+}=S=-K_{Z_-},
\]

avec

\[
N_{S/Z_+}\otimes N_{S/Z_-}\simeq\mathcal O_S.
\]

Le modèle résolu général possède donc bien une dégénérescence de Tyurin et la
LMHS ordinaire de la section 5 est un résultat, non une simple extrapolation.

Cette équation est la bonne entrée du calcul relatif **orientifoldé**. Ce qui
reste à faire avant d’identifier sans réserve cette sous-famille particulière
au modèle semistable général est fini et concret :

1. construire les cônes du fan 5D avec `zeta+`,`zeta-` ;
2. vérifier leurs déterminants ou produire un raffinement régulier lisse ;
3. vérifier le Jacobien du polynôme restreint sur les strates de `z=0` ;
4. confirmer dans la sous-famille que la fibre centrale est réduite SNC avec exactement deux
   composantes tridimensionnelles `Z+` et `Z-` ;

Les données actuelles prouvent toutes les conditions combinatoires, donnent
l’équation Cox relative et fixent le rang de restriction. Le contrôle manquant
est uniquement la régularité globale de son espace total sur toutes les
strates de la section restreinte. La LMHS ordinaire est donc acquise ; seule sa
décomposition équivariante complète reste conditionnée par ce contrôle.

## 5. LMHS ordinaire recalculée

Pour la fibre centrale de Tyurin du modèle résolu général

\[
X_0=Z_+\cup_S Z_-,
\]

la suite de Clemens--Schmid donne

\[
\operatorname{Gr}_2^W H^3_{\lim}
\simeq
\frac{H^2(S)}
{\operatorname{im}H^2(Z_+)+\operatorname{im}H^2(Z_-)}.
\]

Comme `r=2`, sa dimension vaut

\[
22-r=20.
\]

Avec `(h11,h21)=(5,85)`, on trouve

\[
\widehat u=20-r=18,
\qquad
\widehat v=85-18-1=66,
\qquad
\widehat w=5.
\]

La LMHS sur `H3`, de rang 172, est alors

| Gradin | `GrF3` | `GrF2` | `GrF1` | `GrF0` | dimension |
|---|---:|---:|---:|---:|---:|
| `GrW4` | 1 | 18 | 1 | 0 | 20 |
| `GrW3` | 0 | 66 | 66 | 0 | 132 |
| `GrW2` | 0 | 1 | 18 | 1 | 20 |

Donc

\[
\dim(W_2,W_3,W_4)=(20,152,172),
\]

\[
N^2=0,
\qquad
\operatorname{rank}N=20,
\]

\[
\operatorname{Jordan}(T)
=J_2(1)^{20}\oplus J_1(1)^{132},
\]

et

\[
\boxed{\text{Type }II_{18}.}
\]

### 5.1 Structure entière

Le réseau actif reste

\[
K=U\oplus U(2)\oplus E_8(-1)^{\oplus2},
\]

de rang 20, signature `(2,18)` et déterminant 4. La forme normale de
Smith est

\[
\operatorname{SNF}_{\ne0}(N)=(1^{18},2,2).
\]

Sur les 172 dimensions :

\[
\operatorname{SNF}(N)=(1^{18},2,2,0^{152}),
\]

et

\[
W_{2,\mathbb Z}/\operatorname{im}N\simeq(\mathbb Z/2)^2.
\]

La résolution ne conserve donc pas toute la LMHS. Le parent lisse de
`POLY944` avait

\[
(20,162,20),
\]

tandis que la phase résolue a

\[
(20,132,20).
\]

Les 15 modules complexes perdus retirent 30 dimensions du seul `GrW3`. Les
gradins actifs, le rang de `N`, le Smith et le type restent inchangés.

Ce comparatif doit être fait avec `POLY944`, de `h21=100`, et non avec le
`POLY925` de R43--R44, qui avait `h21=98`.

## 6. La vraie couture de `sigma5`

La K3 de couture n’est pas le pôle `F0={x5=0}`. Elle est la section `q=0`
du polytope dual.

Sur ses 35 monômes, si `m=(a,0,c,d)`, on a exactement

\[
e_5=e_7=1-a.
\]

La distribution est

```text
a=-1 : 25 monômes
a= 0 :  9 monômes
a=+1 :  1 monôme.
```

La condition d’invariance sous `sigma5:x5->-x5` supprime précisément les neuf
termes `a=0`. Après jauge des coordonnées hors tranche, l’équation devient

\[
S_5:\quad x_7^2 A_{4,4}+c\,x_0^2=0.
\]

Avec `y=x0/x7`, c’est la double couverture

\[
y^2=-A_{4,4}/c
\]

de `P1 x P1`, ramifiée sur une courbe générale de bidegré `(4,4)`.

Pour comparer `sigma5` sur la même fibre après la demi-rotation de la base, il
faut appliquer la jauge torique qui ramène les coordonnées hors tranche. Elle
induit

\[
y\longmapsto-y.
\]

L’action sur la couture est donc l’involution de revêtement, anti-symplectique.
Pour la K3 très générale,

\[
NS(S_5)=U(2),
\]

\[
H^2(S_5)^+=U(2),
\qquad
H^2(S_5)^-=T(S_5),
\qquad
\operatorname{rank}T=20.
\]

Mais `L=U(2)` est précisément le réseau quotienté dans `GrW2`. Par
conséquent,

\[
\boxed{
\dim(\operatorname{Gr}_2^W)^+=0,
\qquad
\dim(\operatorname{Gr}_2^W)^-=20.
}
\]

Le cercle de plomberie est envoyé par une demi-rotation et conserve son
orientation. Ainsi `C_safe` est impair sur la vraie couture et

\[
\Gamma_{C_{\rm safe}}=C_{\rm safe}\times S^1
\]

est impair. L’argument « `F0` est fixé point par point et disjoint de
l’éclatement » reste vrai sur `F0`, mais il ne calcule pas la parité du tube de
Tyurin.

Si le modèle relatif équivariant passe le contrôle SNC, les parités globales

\[
\dim H^3_+=68,
\qquad
\dim H^3_-=104
\]

se distribueraient comme

\[
\operatorname{Gr}_{2,4}^W:(+,-)=(0,20),
\]

\[
\operatorname{Gr}_3^W:(+,-)=(68,64).
\]

Cette dernière ligne est conditionnelle à l’existence du relèvement
semistable équivariant ; le no-go de charge paire sur la couture ne l’est pas.

## 7. La vraie couture de `sigma125`

Pour

\[
\sigma_{125}:(x_1,x_2,x_5)\mapsto(-x_1,-x_2,-x_5),
\]

la restriction effective sur la couture est

\[
(x_1,x_2,x_7)\mapsto(-x_1,-x_2,-x_7).
\]

Le support de hauteur nulle possède 18 monômes :

```text
1 terme  y^2,
4 termes y g^-_(2,2),
13 termes f^+_(4,4).
```

Donc

\[
P=y^2+y\,g^-_{2,2}+f^+_{4,4}.
\]

Après `Y=y+g^-/2`,

\[
Y^2=\frac14(g^-_{2,2})^2-f^+_{4,4},
\]

et l’action est

\[
\eta:(Y,u,v)\mapsto(-Y,\alpha(u,v)),
\]

où `alpha` change simultanément un signe sur chaque `P1`.

C’est l’involution d’Enriques de l’exemple 3.5 de Garbagnati--Sarti, non la
lift symplectique de Nikulin utilisée en R60. Pour un membre générique,

\[
NS(S_{125})=U(2)\oplus E_8(-2),
\]

\[
T(S_{125})=U\oplus U(2)\oplus E_8(-2),
\]

et

\[
\eta^*=+1\text{ sur }NS,
\qquad
\eta^*=-1\text{ sur }T.
\]

Le réseau prolongeable contient `L=U(2)`. Le secteur pair qui reste actif est
donc

\[
L^\perp\cap H^2(S_{125})^+=E_8(-2).
\]

Il est négatif défini. Ainsi,

\[
\boxed{
C\in L^\perp,\quad \eta C=C,\quad C^2=0
\Longrightarrow C=0.
}
\]

Le `C_Nik` de R60 appartient au vrai réseau transcendant et est donc impair
sous `eta`. La fibre spéciale `F0` porte bien une lift symplectique, mais elle
n’est pas la couture.

Si le lift relatif triple est régulier SNC et garde `r=2`, il aurait encore

\[
\text{Type }II_{18},
\qquad
(\dim GrW_2,\dim GrW_3,\dim GrW_4)=(20,162,20),
\]

avec

\[
GrW_{2,4}:(+,-)=(8,12),
\qquad
GrW_3:(+,-)=(82,80).
\]

Mais même si `r` augmentait, le secteur pair restant serait un sous-réseau du
`E8(-2)` négatif. Le no-go isotrope pair demeure.

## 8. Ce qui est sauvé, et ce qui change

### Conservé

- la résolution globale, projective et crépante de R60 ;
- le nouveau CY de Hodge `(5,85)` ;
- la direction de fibration `m0` et les deux projecting tops ;
- la tranche K3 et le réseau de restriction primitif `U(2)` ;
- le Type `II_18` ordinaire, `rank N=20` et le bloc entier
  `U + U(2) + E8(-1)^2` ;
- l’existence d’une classe primitive isotrope et du tube `T3` dans le parent
  non orientifoldé `N=2` ;
- les capacités de tadpole `24` et `8` calculées en R60.

### Retiré

- `C_safe x S1` pair dans la branche résolue ;
- `C_Nik x S1` pair dans la branche triple ;
- toute affirmation qu’une tour BPS chargée paire `N=1` est déjà construite ;
- toute identification de la fibre spéciale `F0` avec la couture de Tyurin.

Cette correction ne signifie pas que la tour géométrique n’existe pas. Elle
signifie que les deux projections orientifoldes testées la placent dans le
mauvais secteur pour le vecteur fermé `C4` recherché en R56--R58.

## 9. Méthode différente pour la suite

Il ne faut plus essayer de réparer la parité en choisissant un autre vecteur à
l’intérieur du même réseau : les deux no-go sont des no-go de **signature** et
non des échecs d’un vecteur particulier.

La prochaine recherche doit imposer le bon critère avant les calculs de flux :

\[
\boxed{
\operatorname{sign}
\left((L^\perp\cap H^2(S)^+)_{\mathbb R}\right)
\text{ doit être indéfinie ou dégénérée.}
}
\]

Deux voies réellement différentes restent :

1. une involution de couture dont le réseau invariant contient un plan
   hyperbolique supplémentaire qui n’appartient pas à `L` ;
2. une involution qui échange les deux tops et renverse l’orientation du
   cercle de plomberie, de sorte qu’une classe K3 impaire donne un tube pair.

La deuxième voie demande probablement une paire de tops symétriques : les
deux tops actuels ne le sont plus après ajout de `E`.

### R62 proposé

R62 devrait être un test d’arrêt, pas une nouvelle accumulation de formules :

1. expliciter le fan relatif 5D de l’équation de la section 4 dans la
   sous-famille `sigma5` ;
2. vérifier son Jacobien, SNC et l’absence de collision des 16 sections de
   nœuds ;
3. scanner les caractères d’involutions directement sur les 35 monômes de la
   couture ;
4. calculer la signature du secteur pair actif avant toute stabilisation ;
5. si aucun secteur pair indéfini n’existe, figer l’article 1 dans le parent
   `N=2` et présenter le no-go orientifold comme résultat.

Après R62, il sera préférable de rédiger l’article 1 plutôt que de prolonger
la chaîne sans critère de sortie. Le plan de Fano reste réservé à un travail
ultérieur.

## 10. Références utilisées

1. B. Hassfeld, J. Monnee, T. Weigand, M. Wiesner,
   [*Emergent strings in Type IIB Calabi--Yau compactifications*](https://doi.org/10.1007/JHEP01(2026)140),
   JHEP 01 (2026) 140, équations (2.37)--(2.44) et appendice C.
2. C. F. Doran, A. Harder, A. Thompson,
   [*Mirror symmetry, Tyurin degenerations and fibrations on Calabi--Yau manifolds*](https://doi.org/10.1090/pspum/096/01655),
   Proc. Symp. Pure Math. 96 (2017).
3. R. Davis et al.,
   [*Short Tops and Semistable Degenerations*](https://doi.org/10.1080/10586458.2014.910848),
   Experimental Mathematics 23 (2014) 351--362.
4. A. P. Braun, M. Del Zotto,
   [*Mirror Symmetry for G2-Manifolds: Twisted Connected Sums and Dual Tops*](https://doi.org/10.1007/JHEP05(2017)080),
   JHEP 05 (2017) 080.
5. A. P. Braun et al.,
   [*Moduli Stabilisation for ADD and the Dark Dimension Scenario*](https://arxiv.org/abs/2606.19440),
   section 3.6.
6. A. Garbagnati, A. Sarti,
   [*On symplectic and non-symplectic automorphisms of K3 surfaces*](https://doi.org/10.4171/RMI/716),
   Rev. Mat. Iberoam. 29 (2013) 135--162, exemple 3.5.
7. [Stacks Project, section 31.33 — Blowing up](https://stacks.math.columbia.edu/tag/01OF).
8. Y. Kawamata, Y. Namikawa,
   [*Logarithmic deformations of normal crossing varieties and smoothing of degenerate Calabi--Yau varieties*](https://doi.org/10.1007/BF01231538),
   Invent. Math. 118 (1994) 395--409.

## 11. Reproductibilité

Le script `r61_resolved_tyurin_lmhs_audit.py` vérifie exactement :

- réflexivité, nombres de points et Hodge du nouveau polytope ;
- éventail résolu, déterminants, SR et compatibilité des tops ;
- tranche, polaire, 35 monômes et rang torique 2 ;
- matrice de restriction, Gram `U(2)` et Smith `(1,1)` ;
- dimensions de la LMHS, représentant symplectique de `N` et Smith
  `(1^18,2,2,0^152)` ;
- les comptages de couture `26` et `18` ;
- les signatures qui interdisent une charge active paire isotrope dans les
  deux branches actuelles.

