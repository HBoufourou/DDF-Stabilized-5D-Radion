# R63 — Inventaire du corpus R61–R62 et lacunes vers un Tyurin strict

## 0. Verdict de l'audit de corpus

Le corpus local suffit à soutenir l'énoncé suivant, sous une hypothèse de
généricité des coefficients clairement formulée :

> Il existe une famille anticanonique torique explicite, projective et propre
> localement au-dessus de $t=0$, dont l'espace total générique est lisse et
> dont la fibre centrale est une union réduite SNC de deux trois-folds lisses
> irréductibles se rencontrant transversalement le long d'une K3 lisse
> anticanonique commune.

R61–R62 ne calculaient pas explicitement les annulations nécessaires au mot
« quasi-Fano » :

\[
H^i(Y_p,\mathcal O_{Y_p})=H^i(Y_m,\mathcal O_{Y_m})=0,
\qquad i>0.
\]

L'extraction intrinsèque effectuée dans ce rapport ferme cependant ce verrou :
les deux ambiants de composantes et leur diviseur torique commun sont lisses
complets, et les classes vérifient
`[Y_±] = -K_ambient - [seam]`. Les annulations suivent alors des suites
exactes, du vanishing torique et de la dualité de Serre. Le même argument
ferme le statut K3 de la couture. De plus, `div(t)=Y_p+Y_m` fournit
l'isomorphisme des fibrés normaux et la d-semistabilité.

Après le contrôle post-audit par la suite spectrale de poids, la LMHS est
également fermée **sur les rationnels** : gradins `(20,132,20)`, rang de
monodromie 20 et type \(\mathrm{II}_{18}\). Ce qui reste ouvert est la SNF de
la monodromie géométrique intégrale : `(1^18,2,2)` est encore certifiée comme
modèle de réseau compatible, pas comme matrice de Gauss–Manin calculée de la
famille.

Ainsi, sous la définition cohomologique de quasi-Fano utilisée dans les
travaux sur les dégénérescences de Tyurin, le constat post-audit est un
**GO strict**. Le rapport quasi-Fano compagnon montre en outre que \(-K\)
est semi-ample et nef mais non gros. Les composantes ne sont donc pas weak
Fano, et une convention identifiant « quasi-Fano » à « weak Fano » ne doit
pas être utilisée ici.

Le résultat de parité O3/O7 de R62 est séparé de cette porte géométrique. Il
n'est ni nécessaire pour prouver le caractère quasi-Fano, ni un moyen de le
prouver.

---

## 1. Corpus effectivement présent et reproductibilité

Il n'existe aucun fichier de données externe propre à R61/R62. Les rayons,
polytopes, cônes, supports monomiaux, matrices et signatures attendues sont
codés en dur dans les deux scripts autonomes.

| Fichier | Rôle | SHA-256 |
|---|---|---|
| `R61_REPORT.md` | construction résolue 4D, tranche K3, restriction, LMHS proposée | `e8f33e5b8629387ccfcfaea69687bd139828e653fcc696b26997ad8728ca2d15` |
| `r61_resolved_tyurin_lmhs_audit.py` | certificat calculatoire R61 | `eb3fefc077199f28a431940dcbd9d5006f3a5820a503ca0e9a1652b71ecc4fff` |
| `R61_AUDIT_OUTPUT.txt` | sortie de référence R61 | `850b9ceec588dc8f22b709ca10cffde4cbf95f7457e94cf277d75e2a2595381d` |
| `R62_REPORT.md` | éventail relatif, SNC, caractères K3 et stop-test | `62b51d7449392a86b59e1490b7793b1597d60c1e34fc9575d43620896fbf51e3` |
| `r62_stable_fan_parity_stop_audit.py` | certificat calculatoire R62 | `9a7db858d0438022be5d3bf6566876278a083701fb3f70330ad01fb0743d1b22` |
| `R62_AUDIT_OUTPUT.txt` | sortie de référence R62 | `9b8d3c5642cac79886c243e7ea38985bd6ea58398988e72469f9e7c02240c2bc` |

Contrôle effectué le 4 septembre 2026 : les deux scripts terminent avec le
code zéro et leurs sorties sont identiques octet par octet aux fichiers
`R61_AUDIT_OUTPUT.txt` et `R62_AUDIT_OUTPUT.txt`.

Les dépendances d'exécution sont Python, SymPy et, pour R61, NumPy. R62 fait
ses calculs de fan et de réseau en arithmétique entière/rationnelle ; R61
utilise toutefois `numpy.linalg.eigvalsh` pour reconnaître certaines
signatures. La forme par blocs permet de remplacer facilement ce dernier
contrôle flottant par une preuve exacte.

---

## 2. Inventaire exact des objets géométriques

### 2.1 Modèle torique résolu en dimension quatre

Le réseau est $N\simeq\mathbb Z^4$. Les rayons de départ, dans l'ordre
`x0,...,x7`, sont

\[
\begin{aligned}
\nu_0&=(1,0,0,0),&\nu_1&=(-2,0,-1,0),\\
\nu_2&=(-2,0,0,-1),&\nu_3&=(0,0,0,1),\\
\nu_4&=(0,0,1,0),&\nu_5&=(-1,-1,0,0),\\
\nu_6&=(0,1,0,0),&\nu_7&=(-1,0,0,0).
\end{aligned}
\]

La petite résolution ajoute

\[
\nu_E=(1,1,0,0)=\nu_0+\nu_6.
\]

Le fan résolu possède 20 cônes maximaux unimodulaires. Son idéal SR minimal
en dimension quatre contient

\[
x_0x_6,;x_0x_7,;x_1x_4,;x_2x_3,;x_5x_6,;x_5E,;x_7E.
\]

Le polytope dual résolu contient 104 points de réseau ; son polaire en
contient 10. Le comptage de Batyrev codé dans R61 donne

\[
(h^{1,1},h^{2,1})=(5,85),\qquad \chi=-160.
\]

### 2.2 Découpage projecting et K3 de couture

Le normal primitif est

\[
m_0=(0,1,0,0).
\]

Le fan résolu se partage en 12 cônes du top supérieur, 8 du top inférieur et
aucun cône mixte. La tranche a :

- 7 points de réseau ;
- 5 sommets ;
- 35 points dans le dual ;
- 8 cônes maximaux ;
- rang de Picard torique \(\rho_{\rm tor}=2\).

Les cônes de la tranche sont

```text
012, 013, 024, 034, 127, 137, 247, 347.
```

L'image de restriction annoncée est le réseau primitif

\[
L=U(2),\qquad
G_L=\begin{pmatrix}0&2\\2&0\end{pmatrix},
\qquad r=2.
\]

Dans la base `B=(D1,D2,D5,D7,E)`, la matrice utilisée est

\[
\rho_B=
\begin{pmatrix}
1&0&0&0&0\\
0&1&0&0&0
\end{pmatrix},
\]

de SNF `(1,1)` et de noyau annoncé
`<D5,D7,E>`. Attention : le script **déclare** cette matrice de restriction,
puis en vérifie le rang, la SNF et la compatibilité avec les classes de
diviseurs. Il ne la reconstruit pas à partir d'un calcul indépendant dans
l'anneau de Chow de la K3. C'est une donnée géométrique raisonnablement
justifiée dans le rapport, mais à redémontrer humainement dans R63.

### 2.3 Éventail relatif de dimension cinq

Le réseau relatif est

\[
N'=N\oplus\mathbb Z\simeq\mathbb Z^5.
\]

Aux neuf rayons résolus \((\nu_i,0)\), R62 ajoute

\[
\nu_p=(0,-1,0,0,1),\qquad
\nu_m=(0,0,0,0,1).
\]

La matrice de charges de Cox a rang six et une SNF
`(1,1,1,1,1,1)`. Il n'y a donc pas de torsion cachée dans le quotient de Cox
utilisé. Le fan relatif possède exactement 28 cônes maximaux :

- 8 cônes du top inférieur avec `p` ;
- 12 cônes du top supérieur avec `m` ;
- 8 cônes de couture avec `p,m`.

Tous leurs déterminants valent \(\pm1\).

Le vecteur de hauteurs

\[
h=(0,0,0,5,5,0,5,2,4,0,3)
\]

donne exactement 28 sommets entiers dont les cônes normaux sont les 28 cônes
ci-dessus. Le certificat trouve 60 murs internes, 20 murs de bord et des
écarts stricts appartenant à \(\{1,2,3,4,5\}\). C'est le certificat exact de
cohérence/polytopalité.

Le cône de récession est la demi-droite engendrée par
\(-e_5^*\). L'ajout du rayon \(-e_5\) produit une complétion à 48 cônes
maximaux unimodulaires et 120 murs appariés. Le morphisme torique est

\[
\pi:X_{\Sigma_5}\longrightarrow\mathbb A^1,
\]

et la fonction de base est le caractère

\[
t=z=pm,qquad \operatorname{div}(t)=D_p+D_m.
\]

### 2.4 Idéal SR relatif et composantes ambiantes

L'idéal SR relatif minimal est

\[
\begin{gathered}
x_0x_6,\;x_0x_7,\;x_1x_4,\;x_2x_3,\;x_5x_6,\\
x_5E,\;x_5m,\;x_6p,\;x_7E,\;Ep.
\end{gathered}
\]

La fibre torique centrale a donc exactement les deux composantes
`D_p={p=0}` et `D_m={m=0}`, chacune avec multiplicité un.

L'extraction directe des étoiles du fan donne les données suivantes. Les
indices sont ceux du fan relatif global.

| Objet torique | Rayons présents | Cônes maximaux | SR minimal induit |
|---|---|---:|---|
| $D_p$ | `0,1,2,3,4,5,7,10(m)` | 16 | `(0,7),(1,4),(2,3),(5,10)` |
| $D_m$ | `0,1,2,3,4,6,7,8(E),9(p)` | 20 | `(0,6),(0,7),(1,4),(2,3),(6,9),(7,8),(8,9)` |
| $D_p\cap D_m$ | `0,1,2,3,4,7` | 8 | `(0,7),(1,4),(2,3)` |

Ces trois fans sont complets dans leurs réseaux quotients respectifs, puisque
ce sont des étoiles de la fibre d'un morphisme propre. Le calcul
cohomologique R63 demande aussi leurs rayons quotients et leurs matrices de
classes ; l'extraction suivante les fournit, mais elle n'est pas encore
intégrée au certificat R62.

Une réduction directe des rayons fournit déjà un manifeste intrinsèque
minimal. Pour `D_p`, on prend l'ordre
`(x0,x1,x2,x3,x4,x5,x7,m)` et le quotient
`(a,b,c,d,s) -> (a,b+s,c,d)`. Une base de charges est :

```text
2 0 1 1 0 0 0 0
2 1 0 0 1 0 0 0
1 0 0 0 0 0 1 0
1 0 0 0 0 1 0 1
```

Pour `D_m`, on prend l'ordre
`(x0,x1,x2,x3,x4,x6,x7,E,p)` et on oublie la dernière coordonnée du
réseau relatif. Une base de charges est :

```text
 2 0 1 1 0  0 0 0 0
 2 1 0 0 1  0 0 0 0
 1 0 0 0 0  0 1 0 0
-1 0 0 0 0 -1 0 1 0
 0 0 0 0 0  1 0 0 1
```

Dans ces bases, les classes sont :

| Composante | Degré de l'équation | Classe anticanonique de l'ambiant | Classe de la couture |
|---|---|---|---|
| `Y_p in D_p` | `(4,4,2,2)` | `(4,4,2,3)` | `deg(m)=(0,0,0,1)` |
| `Y_m in D_m` | `(4,4,2,-1,1)` | `(4,4,2,-1,2)` | `deg(p)=(0,0,0,0,1)` |

Ainsi, dans les deux cas, `degree(equation) = -K_ambient -
degree(seam)`. L'adjonction donne bien `-K_Y = seam`. Cette vérification
rend l'anticanonicité commune plus explicite que la seule phrase de R62.

Enfin, l'ambiant torique de la couture, dans l'ordre
`(x0,x1,x2,x3,x4,x7)`, a les charges

```text
2 0 1 1 0 0
2 1 0 0 1 0
1 0 0 0 0 1
```

et la K3 a le degré anticanonique `(4,4,2)`.

### 2.5 Hypersurface relative

La famille considérée dans R62 est la sous-famille à 69 monômes invariante
sous `sigma5` :

\[
\begin{aligned}
P={}&p\,x_0x_5^2x_7A^-_{22}
 +x_5^2x_6x_7^2A^0_{44}
 +c\,x_0^2E^2x_6\\
&+m\,x_0E^2x_6^2x_7A^+_{22}
 +m^2E^2x_6^3x_7^2A^{++}_{44}.
\end{aligned}
\]

Le support se répartit ainsi :

```text
q=-1 :  9
q= 0 : 26
q=+1 :  9
q=+2 : 25
```

Tous les monômes ont le degré Cox

\[
(4,4,3,2,-1,0),
\]

qui est la somme des onze colonnes de la matrice de charges. La famille est
donc anticanonique dans l'ambiant relatif lisse.

On note

\[
\mathcal Y=\{P=0\}\subset X_{\Sigma_5},
\quad
Y_p=\mathcal Y\cap D_p,
\quad
Y_m=\mathcal Y\cap D_m,
\quad
S=Y_p\cap Y_m.
\]

Les nombres de monômes des restrictions sont respectivement

\[
60\quad (Y_p),\qquad 35\quad (Y_m),\qquad 26\quad (S).
\]

Les lieux de base minimaux codés sont : aucun pour `Y_p`,
`{x6=x7=0}` pour `Y_m`, et aucun pour `S`. Le système total a également le
lieu de base `{x6=x7=0}`. Sur ce lieu, le terme
`c*x0^2*E^2*x6` fournit un jet unité transverse si \(c\ne0\).

Sur la couture, après les jauges appropriées,

\[
S:\quad x_7^2A^0_{44}+c\,x_0^2=0,
\]

soit une double couverture de \(\mathbb P^1\times\mathbb P^1\) ramifiée sur
une courbe de bidegré \((4,4)\).

### 2.6 Fibre centrale et données LMHS annoncées

Sous les hypothèses de généricité,

\[
\mathcal Y_0=Y_p\cup_S Y_m
\]

est annoncée réduite, SNC, à exactement deux composantes lisses
irréductibles. Par adjonction et parce que `div(t)=Y_p+Y_m` dans
\(\mathcal Y\), R62 obtient

\[
K_{Y_p}+S=0,\qquad K_{Y_m}+S=0.
\]

Avec le rang de restriction \(r=2\), R61 attribue à la LMHS

\[
\bigl(\dim\operatorname{Gr}^W_2,
\dim\operatorname{Gr}^W_3,
\dim\operatorname{Gr}^W_4)=(20,132,20),
\]

\[
N^2=0,\qquad \operatorname{rang}N=20,
\qquad \text{type }\mathrm{II}_{18}.
\]

Le réseau actif choisi est

\[
K=U\oplus U(2)\oplus E_8(-1)^{\oplus2},
\]

de signature \((2,18)\), déterminant 4 et SNF non nulle
`(1^18,2,2)`.

---

## 3. Hiérarchie exacte des preuves et certificats

Légende :

- **M** : calcul exact réellement exécuté par une assertion bloquante ;
- **H** : calcul machine plus théorème/argument humain standard ;
- **T** : entrée théorique ou valeur déclarée, non dérivée par le script ;
- **O** : ouvert.

| Énoncé | Niveau | Ce que le corpus vérifie réellement | Limite à écrire dans l'article |
|---|:---:|---|---|
| Réflexivité/comptages du polytope résolu | M | points de réseau, facettes, Hodge de Batyrev | dépend du polytope et de la phase codés |
| Fan résolu 4D lisse | M | 20 cônes, déterminants \(\pm1\), compatibilité aux facettes | aucune triangulation concurrente n'est étudiée |
| Découpage projecting | M | hauteurs, projections, absence de cônes mixtes, 8 cônes communs | porte sur ce normal \(m_0\) |
| \(\rho_{\rm tor}(S)=2\) | M/H | formule combinatoire et comptage | « Picard exactement 2 » demande membre très général |
| Image de restriction \(L=U(2)\), primitive | T/M | la matrice `rho_B` est une entrée ; sa SNF et son Gram sont vérifiés | dériver `rho_B` géométriquement dans R63 |
| Fan relatif régulier | M | 28 cônes et tous les déterminants | exact |
| Cohérence/projectivité | M/H | polyèdre rationnel exact et complétion bornée | invoque le dictionnaire polytope–fan–projectivité |
| Propreté sur \(\mathbb A^1\) | H | bord, récession, complétion et projection sont contrôlés | formaliser le critère torique de propreté |
| `div(t)=D_p+D_m` | M/H | dernières coordonnées des rayons et SR | expliciter le caractère de réseau dual |
| Degré anticanonique de \(P\) | M | les 69 monômes ont le degré somme des colonnes | seulement la sous-famille `sigma5` |
| Lieux de base | M | énumération des supports sur les faces des fans | le calcul porte sur la combinatoire monomiale |
| Lissité de \(\mathcal Y,Y_p,Y_m,S\) | H | jet unité sur les lieux de base ; Bertini ailleurs | aucun idéal jacobien à coefficients explicites n'est saturé globalement |
| Irréductibilité de \(Y_p,Y_m\) | H | argument de discriminant non carré dans le rapport | non testée par le script ; détailler corps des fonctions et bord |
| Fibre réduite à deux composantes | M/H | SR, multiplicité un, non-divisibilité, irréductibilité générique | dépend de la généricité et de l'argument précédent |
| SNC | H | modèle torique et transversalité générique | rédiger des cartes locales sur \(\mathcal Y\), pas seulement l'ambiant |
| Couture K3 | H | équation de double couverture et, post-audit, suite anticanonique sur l'ambiant torique | fermé analytiquement ; non codé dans R62 |
| \(S\in\lvert-K_{Y_\pm}\rvert\) | H | adjonction et diviseur principal de la fibre | écrire le calcul de fibrés, pas seulement l'égalité de classes |
| Platitude | H | non-diviseur de zéro + Cohen–Macaulay, après rétrécissement | résultat local autour de 0, pas assertion globale sur toute \(\mathbb A^1\) |
| Produit des fibrés normaux trivial | H | `div(t)=Y_p+Y_m` donne l'isomorphisme après restriction à la couture | fermé post-audit ; à rédiger comme lemme |
| Annulations quasi-Fano | H | fermées post-audit par deux suites exactes, vanishing torique et Serre | non calculées par le script R62 |
| Dimensions LMHS rationnelles | H | suite spectrale de poids/Clemens–Schmid, \(b_3=172\) et \(r=2\) | gradins `(20,132,20)` et type II18 fermés |
| Matrice de monodromie intégrale/SNF | T/M | une matrice abstraite compatible est construite et auditée | SNF non obtenue d'une base intégrale de Gauss–Manin de \(\mathcal Y\) |
| Parités équivariantes | T/M/H | supports de caractères exacts ; signatures issues de Nikulin/Enriques | séparé du Tyurin strict |

Point important : les chaînes `assert` de R62 vérifient les données qu'elles
calculent, mais certaines conclusions imprimées (`SMOOTH`, `SNC`, LMHS) sont
des conclusions théoriques tirées de ces données, et non la sortie d'un CAS de
géométrie algébrique calculant directement un schéma singulier ou une
cohomologie.

---

## 4. Hypothèses indispensables déjà utilisées

1. Le corps de base est de caractéristique zéro, implicitement
   \(\mathbb C\), pour Bertini, la théorie des K3 et la LMHS.
2. La phase résolue de `POLY944` est exactement celle définie par les 20 cônes
   codés et par le rayon \(\nu_E\).
3. On travaille dans la sous-famille `sigma5` de 69 monômes, pas dans la
   famille anticanonique complète à 104 monômes.
4. Le coefficient \(c\) est non nul.
5. Les sections \(A^-_{22},A^0_{44},A^+_{22},A^{++}_{44}\) sont générales ; en
   particulier la branche \((4,4)\) est lisse, les intersections pertinentes
   sont transverses et les discriminants de composantes ne sont pas des
   carrés.
6. Les arguments de lissité et d'irréductibilité valent sur un ouvert de
   Zariski des coefficients. Aucun point rationnel explicite de cet ouvert
   n'est fourni.
7. La platitude est revendiquée après restriction à un voisinage de
   \(t=0\). C'est suffisant pour une dégénérescence de Tyurin locale, mais doit
   être dit explicitement.
8. Pour écrire `Pic(S)=U(2)` et identifier le réseau actif, la K3 est supposée
   très générale dans la famille pertinente.
9. La classification des involutions de Nikulin/Enriques et leurs réseaux
   invariants est importée de la littérature.
10. Clemens–Schmid et la suite spectrale de poids ferment le résultat
    rationnel avec le réseau de restriction annoncé. L'identification
    intégrale précise du bloc de Gauss–Manin reste une hypothèse à contrôler.

---

## 5. Checklist Tyurin strict / quasi-Fano

La définition doit être fixée avant tout calcul. Sous la convention utilisée
implicitement dans R62 — composantes lisses projectives, annulations
\(H^i(\mathcal O)=0\) pour \(i>0\), et K3 lisse anticanonique commune — le
statut est le suivant.

| Condition | Statut actuel | Travail R63 nécessaire |
|---|---|---|
| Famille propre/projective sur une courbe pointée | presque fermé | formuler précisément la restriction à un voisinage de 0 et citer le critère torique |
| Famille plate | argument disponible | écrire le lemme non-diviseur/CM ou miracle flatness sur chaque carte |
| Espace total lisse | générique, preuve hybride | définir l'ouvert de coefficients et détailler Bertini + jet unité |
| Fibre générale CY lisse | très plausible/standard | adjonction relative et vérification que la sous-famille lisse est non vide |
| Fibre centrale réduite SNC à deux composantes | fermé génériquement | transformer le raisonnement R62 en proposition avec cartes locales |
| $Y_p,Y_m$ lisses, projectifs, irréductibles, connectés | fermé génériquement sauf rédaction | rendre l'argument des discriminants entièrement algébrique |
| $S$ lisse et connectée | **fermé post-audit** | suite anticanonique sur l'ambiant torique ou double couverture |
| $K_S\simeq\mathcal O_S$, $h^1(S,\mathcal O_S)=0$ | **fermé post-audit** | adjonction + vanishing torique/dualité de Serre |
| $S\in\lvert-K_{Y_p}\rvert\cap\lvert-K_{Y_m}\rvert$ | argument d'adjonction présent | écrire les isomorphismes de fibrés ligne |
| $H^i(Y_p,\mathcal O)=H^i(Y_m,\mathcal O)=0$, $i>0$ | **fermé post-audit** | suites exactes + vanishing torique + Serre ; contrôle CAS encore utile |
| $N_{S/Y_p}\otimes N_{S/Y_m}\simeq\mathcal O_S$ | **fermé post-audit** | restriction du diviseur principal `div(t)=Y_p+Y_m` |
| d-semistabilité/log-lissité | d-semistabilité fermée | écrire les cartes $uv=t$ comme preuve log-lisse autonome |
| Canonique relatif/log trivial | degré anticanonique disponible | adjonction relative complète et convention de dualisante |
| $-K_{Y_\pm}$ nef et/ou big | non testé | seulement si la définition choisie de « quasi-Fano » l'exige |
| LMHS rationnelle \(\mathrm{II}_{18}\) | **fermée post-audit** | suite spectrale de poids ; seule la SNF intégrale reste ouverte |

### Clarification de définition

Certaines sources emploient « quasi-Fano » pour la seule combinaison

\[
H^i(Y,\mathcal O_Y)=0\;(i>0),
\qquad |-K_Y|\text{ contient une K3 lisse},
\]

tandis que d'autres imposent des propriétés de type weak Fano, par exemple
\(-K_Y\) nef et big. R63 doit choisir une source et ne pas mélanger ces deux
conventions. Si la première convention est retenue, le lemme post-audit
ci-dessous ferme le dernier verrou structurel. Si la seconde est retenue, il
faut encore calculer le cône nef et les intersections de \(-K_{Y_\pm}\).

---

## 6. Lacunes concrètes à fermer, par ordre de priorité

### G1 — Certifier le manifeste intrinsèque des deux composantes

L'extraction directe ci-dessus fournit déjà les rayons quotients, charges,
degrés et classes nécessaires. Il faut maintenant intégrer ces données à un
script bloquant et les présenter, pour chaque ambiant torique $D_p,D_m$, avec :

- le réseau quotient et les rayons primitifs ;
- le fan complet ;
- la matrice de charges/Cox ;
- le groupe de Picard ;
- la classe de l'hypersurface $Y_p$ ou $Y_m$ ;
- la classe de la couture $S$ ;
- le canonique de l'ambiant et de la composante.

Sans ce manifeste, un calcul de cohomologie automatisé risque d'utiliser la
mauvaise classe ou le mauvais quotient.

### G2 — Cohomologie des composantes : fermée post-audit

Soit $\mathcal A_p=D_p$ ou $\mathcal A_m=D_m$, et soit
$T=D_p\cap D_m$ le diviseur
torique de couture dans l'ambiant correspondant. Les calculs de degrés donnent

\[
[Y_\pm]=-K_{\mathcal A_\pm}-[T],
\qquad K_{\mathcal A_\pm}+Y_\pm=-T.
\]

Les variétés $\mathcal A_\pm$ et $T$ sont lisses, complètes et toriques. Elles
vérifient donc

\[
H^i(\mathcal A_\pm,\mathcal O)=H^i(T,\mathcal O)=0\qquad(i>0).
\]

Comme $T$ est un diviseur effectif non vide et connexe, la flèche des
constantes est un isomorphisme dans

\[
0\longrightarrow\mathcal O_{\mathcal A_\pm}(-T)
\longrightarrow\mathcal O_{\mathcal A_\pm}
\longrightarrow\mathcal O_T\longrightarrow0.
\]

Il s'ensuit

\[
H^i(\mathcal A_\pm,\mathcal O_{\mathcal A_\pm}(-T))=0
\qquad\text{pour tout }i.
\]

Par dualité de Serre en dimension quatre,

\[
H^j(\mathcal A_\pm,\mathcal O(-Y_\pm))^*
\simeq
H^{4-j}(\mathcal A_\pm,\mathcal O(K_{\mathcal A_\pm}+Y_\pm))
=H^{4-j}(\mathcal A_\pm,\mathcal O(-T))=0.
\]

La suite de l'hypersurface

\[
0\longrightarrow\mathcal O_{\mathcal A_\pm}(-Y_\pm)
\longrightarrow\mathcal O_{\mathcal A_\pm}
\longrightarrow\mathcal O_{Y_\pm}\longrightarrow0
\]

donne finalement

\[
h^0(Y_\pm,\mathcal O)=1,
\qquad h^i(Y_\pm,\mathcal O)=0\quad(i=1,2,3).
\]

Les annulations requises par la définition cohomologique de quasi-Fano sont
donc prouvées. Un calcul Čech/Stanley–Reisner ou un second CAS reste utile
comme certificat indépendant, mais l'issue mathématique n'est plus ouverte.

### G3 — K3 et fibrés normaux : fermés post-audit

L'ambiant torique $T=D_p\cap D_m$ est lisse complet de dimension trois et
la couture $S\subset T$ a la classe anticanonique `(4,4,2)`. La suite

\[
0\longrightarrow K_T\longrightarrow\mathcal O_T
\longrightarrow\mathcal O_S\longrightarrow0
\]

avec vanishing torique et dualité de Serre donne

\[
h^0(S,\mathcal O_S)=1,\qquad
h^1(S,\mathcal O_S)=0,\qquad
h^2(S,\mathcal O_S)=1.
\]

L'adjonction donne $K_S\simeq\mathcal O_S$. Puisque R62 établit la lissité
générique, $S$ est bien une K3 lisse et connectée. Cette preuve est
indépendante de la seconde description comme double couverture
\((4,4)\), qui fournit un contrôle supplémentaire via
`varpi_* O_S = O + O(-2,-2)`.

Enfin, dans l'espace total lisse,

\[
Y_p+Y_m=\operatorname{div}(t).
\]

En restreignant à $S$, on obtient l'isomorphisme de fibrés, et pas seulement
une égalité de classes,

\[
N_{S/Y_p}\otimes N_{S/Y_m}
\simeq
\mathcal O_{\mathcal Y}(Y_p+Y_m)|_S
\simeq\mathcal O_S.
\]

Ainsi $T^1_{Y_0}\simeq\mathcal O_S$ et la d-semistabilité sont fermées.

### G4 — Rédaction locale de la log-lissité

Donner les cartes locales de \(\mathcal Y\to\Delta\) aux points de
`Y_p\setminus S`, `Y_m\setminus S` et `S`, avec formes respectives

\[
t=u,\qquad t=v,\qquad t=uv.
\]

La d-semistabilité est déjà fermée par G3. Comme l'espace total est lisse et
la fibre réduite SNC, ces cartes donnent le caractère log-lisse standard.
Il reste à les écrire explicitement comme lemme local : le script ne construit
pas lui-même la structure logarithmique.

### G5 — Certificat indépendant de lissité

Fixer un jeu explicite de coefficients génériques, puis vérifier dans un
second système (Sage + Singular, ou Macaulay2) :

- saturation par l'idéal irrelevant ;
- absence de solutions de l'idéal jacobien total ;
- lissité de chaque composante et de $S$ ;
- radicalité et nombre de composantes de la fibre centrale.

Ce contrôle ne remplace pas Bertini, mais montre que l'ouvert générique
invoqué est non vide et rend le dossier de dépôt auditable.

### G6 — LMHS rationnelle fermée ; structure intégrale ouverte

Le contrôle par la suite spectrale de poids de la fibre SNC ferme le résultat
sur \(\mathbb Q\). La couture est une K3 et l'image totale des restrictions a
le rang \(r=2\). Ainsi

\[
\dim\operatorname{Gr}^W_2 H^3_{\lim}
=\dim\operatorname{Gr}^W_4 H^3_{\lim}=22-r=20.
\]

La fibre générale a $b_3=2h^{2,1}+2=172$, donc

\[
\dim\operatorname{Gr}^W_3 H^3_{\lim}=172-40=132.
\]

La semi-stabilité donne une monodromie unipotente ; le complexe de poids et
Clemens–Schmid donnent

\[
N^2=0,\qquad \operatorname{rang}_{\mathbb Q}N=20,
\]

d'où le type \(\mathrm{II}_{18}\). Le résultat rationnel annoncé par R61 est
donc bien attaché à la famille R62, sous la preuve géométrique du rang de
restriction.

La réserve restante est strictement intégrale. La fonction
`lmhs_and_monodromy_audit()` construit un nilpotent symplectique abstrait à
partir de

\[
K=U\oplus U(2)\oplus E_8(-1)^{\oplus2}
\]

et vérifie la SNF `(1^18,2,2)`. Elle montre la compatibilité de ce modèle,
mais pas que la matrice de Gauss–Manin de la famille R62 possède cette SNF
dans une base intégrale de cycles. Pour fermer ce dernier point, il faut une
comparaison intégrale du complexe de poids, ou une monodromie/Picard–Fuchs
calculée dans une base entière. L'article peut annoncer la LMHS rationnelle
\(\mathrm{II}_{18}\) sans annoncer le défaut intégral `(Z/2)^2` comme théorème
de la famille.

---

## 7. Ce qui n'est pas un verrou R63

Les questions suivantes ne doivent pas être mélangées au certificat Tyurin
strict :

- la relation métrique \(R(t)\) ;
- une valeur micrométrique de \(R\) ;
- le spectre KK ou une tour BPS ;
- la stabilité des D3 multi-enroulées ;
- la projection O3/O7 et le no-go de tube pair ;
- les flux, tadpoles et la cosmologie ;
- le plan de Fano.

Elles peuvent former d'autres branches du programme DDF, mais leur absence ne
réfute pas le théorème géométrique visé par R63.

---

## 8. Protocole de décision R63

### GO strict

Sous la définition cohomologique de quasi-Fano, le post-audit atteint le
**GO strict**, avec les éléments suivants :

1. une définition publiée est fixée ;
2. G2 prouve les annulations de \(Y_p,Y_m\) ;
3. G3 prouve la K3, l'anticanonicité, les fibrés normaux et la
   d-semistabilité ;
4. R62 donne famille propre/projective, lisse et fibre centrale réduite SNC ;
5. G6 ferme la LMHS \(\mathrm{II}_{18}\) sur \(\mathbb Q\).

Avant livraison, il reste prudent d'intégrer les nouveaux lemmes au script et
de confirmer fan/classes/Jacobien dans un second CAS. Ce sont des contrôles de
publication, pas un résultat mathématique encore indéterminé.

### GO étroit

Si la revue ou la source choisie emploie « quasi-Fano » au sens weak Fano,
la condition de grosseur échoue ; conserver alors l'énoncé plus précis :

> famille CY torique semi-stable, projective, à fibre centrale K3-seamed
> réduite SNC à deux composantes.

Le mot « Tyurin-type » reste alors acceptable s'il est défini dans le texte,
mais « composantes quasi-Fano » doit disparaître.

### STOP de la branche géométrique

Un stop complet ne serait justifié que si un contrôle indépendant réfute la
lissité/SNC, la propreté, l'anticanonicité commune, ou l'existence même de la
famille. Les annulations ne sont plus un motif de stop après G2.

---

## 9. Conclusion opérationnelle

Le travail de découverte R63 est fermé au niveau rationnel. Le meilleur ordre
de consolidation est maintenant :

1. figer le manifeste avec les hashes ci-dessus ;
2. citer et choisir explicitement la définition de quasi-Fano ;
3. intégrer les fans quotients, degrés et preuves G2–G3 au certificat ;
4. rédiger les cartes log-lisses de G4 ;
5. refaire fan/classes/Jacobien dans un second CAS ;
6. annoncer la LMHS rationnelle, mais isoler la SNF intégrale comme conjecture
   ou travail futur tant qu'elle n'est pas calculée géométriquement.

La conclusion locale la plus importante est donc : **R63 ferme les
annulations quasi-Fano, le statut K3, les fibrés normaux, la d-semistabilité et
la LMHS rationnelle de type \(\mathrm{II}_{18}\). La seule réserve théorique
majeure de ce bloc est la structure intégrale précise de Gauss–Manin/SNF.
Dans la terminologie DHT les composantes sont quasi-Fano ; elles ne sont pas
weak Fano puisque leur classe anticanonique a cube nul.**

