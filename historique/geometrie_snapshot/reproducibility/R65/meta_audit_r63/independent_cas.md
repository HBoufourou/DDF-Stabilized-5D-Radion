# R63 — Contrôle indépendant des certificats critiques de R62

> **Statut documentaire : audit partiel du fan et des prémisses SNC.** Ce
> fichier n'a pas pour périmètre la cohomologie quasi-Fano ni la LMHS. Les
> conclusions finales correspondantes se trouvent dans R63_REPORT.md ; les
> mentions « non calculé ici » ci-dessous ne signifient pas « ouvert après
> R63 ».

**Projet :** DDF I–VIII  
**Objet :** audit indépendant du réseau de Cox, de l’éventail relatif, du certificat de cohérence et des prémisses jacobiennes/SNC de R62  
**Date :** 4 septembre 2026  
**Verdict :** **PASS pour le noyau torique et SNC de R62, avec limites explicites**

## 1. Conclusion

Le noyau mathématique suivant de R62 résiste à une reconstruction indépendante :

1. les relations de Cox sont primitives et sans torsion cachée ;
2. les 28 cônes relatifs sont unimodulaires ;
3. le vecteur de support annoncé définit exactement ces 28 cônes comme cônes normaux ;
4. l’ajout du rayon à l’infini donne 48 cônes unimodulaires formant le fan normal complet d’un polytope borné ;
5. les dix générateurs de Stanley–Reisner sont reproduits ;
6. le support relatif comporte bien 69 monômes de classe anticanonique commune ;
7. les lieux de base et le jet transverse unité annoncés sont reproduits ;
8. les décompositions idéales locales, le nombre d’intersections horizontales (16), la lissité générique de la branche ((4,4)) et la transversalité générique ((2,2)/(4,4)) sont confirmés par bases de Gröbner.

La conclusion prudente autorisée est donc :

> L’éventail relatif 5D de R62 est lisse, cohérent et propre sur \(\mathbb A^1\). Les données monomiales et jacobiennes nécessaires à l’argument standard de Bertini/SNC sont correctes. Pour des coefficients génériques, la fibre centrale est réduite à deux composantes lisses se rencontrant transversalement le long d’une K3 lisse.

Ce contrôle **ne ferme pas** les annulations quasi-Fano, la LMHS, la classification de Nikulin, le stop-test de parité, les invariants BPS, ni la relation métrique (R(t)). Ces points nécessitent des audits distincts.

## 2. Indépendance effective du contrôle

### 2.1 Logiciels disponibles

| Logiciel | Disponibilité locale |
|---|---:|
| Python 3.12.13 | oui |
| SymPy 1.14.0 | oui |
| SciPy 1.17.0 / Qhull | oui |
| NumPy 2.3.5 | oui |
| SageMath | non |
| Singular autonome | non |
| Macaulay2 | non |
| polymake | non |
| Normaliz | non |
| cddlib / pycddlib | non |
| GAP | non |
| PARI/GP | non |

Il serait donc incorrect de prétendre que R62 a déjà été reproduit avec Sage, Singular ou Macaulay2 dans cet environnement.

### 2.2 Trois moteurs de vérification

- **Arithmétique exacte indépendante :** déterminant de Bareiss, élimination de Gauss sur `Fraction`, énumération complète des sommets et calcul des non-faces réécrits sans SymPy et sans importer R62.
- **Géométrie convexe indépendante :** `scipy.spatial.HalfspaceIntersection`, dont l’énumération passe par Qhull, recoupe numériquement les 48 sommets exacts.
- **Algèbre commutative :** bases de Gröbner SymPy pour les intersections d’idéaux, les critères jacobiens sur quatre cartes de \(\mathbb P^1\times\mathbb P^1\) et les témoins de transversalité.

Cette séparation évite de simplement réexécuter `r62_stable_fan_parity_stop_audit.py`.

## 3. Contrôle du réseau de Cox

La matrice (Q\in M_{6\times11}(\mathbb Z)) et les onze rayons (V\in M_{11\times5}(\mathbb Z)) ont été saisis à nouveau depuis l’énoncé mathématique.

Résultats exacts :

| Test | Résultat |
|---|---:|
| (QV=0) | exact |
| mineurs maximaux (6\times6) testés | 462 |
| mineurs non nuls | 108 |
| pgcd des mineurs maximaux | 1 |
| rang de (Q) | 6 |

Un mineur maximal non nul prouve le rang six. Le pgcd égal à un prouve que le réseau des relations est primitif ; comme le produit des invariants de Smith est ce pgcd, les six invariants valent tous un. La conclusion SNF de R62 est donc reproduite sans appeler la routine Smith de SymPy.

## 4. Éventail et cohérence

### 4.1 Éventail relatif

- 28 cônes maximaux ont été saisis indépendamment ;
- leurs 28 déterminants ont valeur absolue (1) ;
- l’énumération exhaustive des \(\binom{11}{5}=462\) intersections potentielles de cinq hyperplans donne exactement 28 sommets faisables ;
- chaque sommet est entier et simple ;
- ses cinq facettes actives reproduisent exactement l’un des 28 cônes annoncés ;
- tous les écarts stricts sont dans ({1,2,3,4,5}).

Le comptage des murs donne 60 murs internes, chacun partagé par deux cônes, et 20 murs de bord.

### 4.2 Stanley–Reisner

Une recherche exhaustive dans le complexe simplicial donne exactement :

\[
06,\ 07,\ 14,\ 23,\ 56,\ 5E,\ 5m,\ 6p,\ 7E,\ Ep.
\]

Cela confirme notamment deux exclusions cruciales pour R62 :

\[
x_6p\in SR,\qquad Ep\in SR.
\]

La première supprime la courbe verticale du modèle pré-semi-stable ; la seconde sépare le lieu exceptionnel horizontal de la couture.

### 4.3 Complétion et proprement relatif

Après ajout de \(\nu_\infty=(0,0,0,0,-1)\) à hauteur un :

| Test | Résultat |
|---|---:|
| sommets exacts | 48 |
| cônes normaux maximaux | 48 |
| déterminants | tous (pm1) |
| murs codimension un | 120 |
| multiplicité de chaque mur | 2 |

La relation strictement positive

\[
5\nu_0+\nu_1+\cdots+\nu_m+2\nu_\infty=0
\]

— avec poids explicites ((5,1,1,1,1,1,1,1,1,1,1,2)) — et le fait que les rayons engendrent le rang cinq prouvent que le polytope complété est borné. Son fan normal est donc complet.

Qhull retrouve indépendamment 48 sommets, avec une erreur maximale de raccordement de (1.776\times10^{-15}). Cette vérification flottante n’est pas utilisée comme preuve ; elle recoupe le calcul rationnel exact.

Pour le polyèdre non borné, le cône de récession est \(\mathbb R_{\ge0}(-e_5^*)\). Le support du fan normal est donc son polaire

\[
N_{\mathbb R}^4\times\mathbb R_{\ge0},
\]

qui est exactement l’image inverse du cône de \(\mathbb A^1\). Le critère torique de propreté relative utilisé en R62 s’applique.

Enfin, le caractère de base a ordres

\[
(0,0,0,0,0,0,0,0,0,1,1),
\]

d’où \(\operatorname{div}(z)=D_p+D_m\), avec multiplicité un sur chaque composante.

## 5. Support anticanonique et lieux de base

Les inégalités du polytope résolu donnent directement la boîte exacte

\[
-1\le a\le1,\quad -1\le b\le2,\quad -1\le c,d\le3.
\]

L’énumération indépendante trouve 104 points résolus, puis 69 monômes dans le sous-espace pair de \(\sigma_5\), avec distribution

\[
q=-1:9,\quad q=0:26,\quad q=1:9,\quad q=2:25.
\]

Les 69 monômes ont tous le degré de Cox

\[
(4,4,3,2,-1,0),
\]

égal à la somme des colonnes de (Q), donc à la classe anticanonique.

Un calcul de transversaux minimaux de l’hypergraphe des supports monomiaux, restreint aux faces toriques autorisées, reproduit :

| Système | Monômes | Lieu de base minimal |
|---|---:|---|
| espace total | 69 | (x_6=x_7=0) |
| (p=0) | 60 | aucun |
| (m=0) | 35 | (x_6=x_7=0) |
| couture (p=m=0) | 26 | aucun |

Sur le seul lieu de base, le terme

\[
x_0^2E^2x_6
\]

est l’unique terme donnant le jet normal pertinent. Les relations (x_0x_6\in SR) et (x_7E\in SR) rendent (x_0) et (E) inversibles sur (x_6=x_7=0), donc

\[
\partial_{x_6}P=x_0^2E^2\ne0.
\]

Les prémisses de l’argument de Bertini employé dans R62 sont confirmées.

## 6. Contrôles par bases de Gröbner

### 6.1 Décomposition jacobienne locale

Une élimination avec une variable auxiliaire recalcule exactement

\[
(a,b)\cap(p,b)=(ap,b).
\]

Elle confirme que le modèle pré-semi-stable possède deux composantes jacobiennes locales : la branche horizontale et la branche verticale.

De même,

\[
(p)\cap(m)=(pm),
\]

ce qui confirme que la fibre centrale locale est réduite, avec exactement deux composantes de multiplicité un. Dans des coordonnées lisses, c’est le modèle SNC standard (pm=0).

### 6.2 Couture K3

Le polynôme bihomogène explicite

\[
B_{44}=s_0^4t_0^4+s_0^4t_1^4+s_1^4t_0^4+2s_1^4t_1^4
\]

a été testé sur les quatre cartes affines de \(\mathbb P^1\times\mathbb P^1\). Sur chaque carte, la base de Gröbner de

\[
(B_{44},\partial_uB_{44},\partial_vB_{44})
\]

est ((1)). La branche est donc lisse. Par conséquent, le double revêtement local (w^2+B_{44}=0) est lisse. L’existence de ce témoin exact montre que le bon lieu de coefficients est non vide ; la lissité est alors une propriété générique ouverte.

### 6.3 Seize intersections horizontales

Une paire explicite complète de polynômes (A_{22},A_{44}) à coefficients entiers a été testée. Sur chacune des quatre cartes, la base de Gröbner de

\[
(A_{22},A_{44},dA_{22}\wedge dA_{44})
\]

est ((1)). La paire est donc transverse. Le produit d’intersection donne

\[
(2H_1+2H_2)(4H_1+4H_2)=16H_1H_2.
\]

Il existe ainsi exactement 16 points distincts pour ce témoin, et la même propriété vaut génériquement.

### 6.4 Irréductibilité des deux composantes

Sur chacun des deux tores denses, l’équation est quadratique en (x_0). Après retrait des facteurs carrés inversibles, chaque discriminant est de degré exactement un dans le coefficient indépendant (A^0_{44}). Sa valuation le long du facteur linéaire est impaire ; il n’est donc pas carré dans le corps de fonctions générique. Les deux quadratiques, et donc les deux composantes génériques, sont irréductibles sur leurs tores denses.

## 7. Ce qui est démontré, et ce qui ne l’est pas

| Affirmation | Statut R63 indépendant |
|---|---:|
| noyau de Cox et saturation | confirmé exactement |
| 28 cônes relatifs réguliers | confirmé exactement |
| cohérence/polytopalité | confirmée exactement |
| complétion 48 cônes | confirmée exactement + Qhull |
| propre sur \(\mathbb A^1\) | confirmé par le critère du support |
| support 69 monômes anticanonique | confirmé exactement |
| lieux de base et jet unité | confirmés exactement |
| décomposition jacobienne locale | confirmée par Gröbner |
| couture et 16 intersections génériquement lisses/transverses | témoins exacts confirmés |
| fibre centrale générique à deux composantes SNC | confirmée via les données exactes + Bertini/SNC standard |
| annulations (H^i(Y_\pm,\mathcal O)=0) | **non calculées ici** |
| d-semistabilité (N_{S/Y_+}\otimes N_{S/Y_-}\simeq\mathcal O_S) | **non calculée ici comme classe de Picard** |
| LMHS de type \(\mathrm{II}_{18}\) | **non recoupée ici** |
| signatures de Nikulin/parité O3/O7 | **non recoupées ici** |
| tour BPS ou tour KK physique | **non démontrée ici** |
| (R=R(t)), stabilisation ou valeur micrométrique | **non démontrées** |

La mention « Tyurin stricte » doit donc rester suspendue jusqu’au calcul cohomologique et à la vérification de d-semistabilité. La mention sûre reste « dégénérescence semi-stable de forme Tyurin ».

## 8. Limite de reproductibilité et prochaine fermeture

Pour un dossier de revue, il reste souhaitable de reproduire les calculs avec un vrai second environnement, idéalement :

1. **SageMath + Normaliz/polymake** pour le fan, le support et les cônes normaux ;
2. **Macaulay2 ou Singular** pour les saturations jacobiennes sur toutes les cartes toriques ;
3. conservation des sorties brutes, versions logicielles et empreintes SHA-256.

L’absence locale de ces logiciels n’invalide pas les preuves exactes présentes, mais interdit d’appeler ce contrôle une réplication « Sage/Macaulay2 ». La formulation honnête est : **deux implémentations exactes indépendantes au niveau du code, recoupées par Qhull, plus un contrôle Gröbner local avec SymPy**.

## 9. Fichiers reproductibles

- `r63_independent_lattice_fan.py`
- `r63_independent_jacobian_snc.py`

Exécution :

```bash
python3 r63_independent_lattice_fan.py
python3 r63_independent_jacobian_snc.py
```

Empreintes de cette version :

```text
ee5dc1bb394710012e2c6e79f56ac1a05d3938177737954cd2685faf48e31dbc  r63_independent_lattice_fan.py
5549689c10af0a6d625ae5d627ecdc00329847adc97e3efda1f0d558eccdbd0b  r63_independent_jacobian_snc.py
```

