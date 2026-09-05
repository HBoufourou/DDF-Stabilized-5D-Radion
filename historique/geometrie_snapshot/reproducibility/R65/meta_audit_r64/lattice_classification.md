# R64 — Classification exacte de $U(2)$, involutions et orthogonal actif

**Date :** 4 septembre 2026  
**Objet :** contre-calcul indépendant du réseau de couture de R61–R63, des
symétries toriques et du scan de caractères de Cox.  
**Programme reproductible :** `meta_audit_r64/r64_lattice_classification.py`

## 1. Verdict

Le réseau de restriction de la couture très générale est bien

\[
L=U(2),\qquad G_L=\begin{pmatrix}0&2\\2&0\end{pmatrix},
\qquad \operatorname{sign}(L)=(1,1).
\]

Le contre-calcul ferme exactement les points suivants.

1. Le groupe entier complet est

   \[
   O(U(2),\mathbb Z)=\{I,-I,S,-S\},\qquad
   S=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
   \]

2. Le sous-groupe qui préserve la composante ample choisie est seulement
   \(\{I,S\}\).
3. Les seules classes isotropes primitives de $L$ sont
   \(\pm h_1,\pm h_2\).
4. Le fan de couture possède huit automorphismes de réseau : quatre agissent
   par $I$ sur $L$, quatre par $S$. Le fan résolu 4D possède également
   huit automorphismes, mais **tous préservent la hauteur du top** : aucun
   n'échange les deux tops.
5. Les $2^9=512$ signes diagonaux de Cox redonnent exactement huit motifs
   effectifs sur les 35 monômes de couture, avec 64 relèvements chacun.
6. L'orthogonal actif est reconstruit intégralement comme

   \[
   K=L^\perp\simeq U\oplus U(2)\oplus E_8(-1)^{\oplus2},
   \qquad \operatorname{sign}(K)=(2,18),\quad |\det K|=4.
   \]

7. Des matrices intégrales $22\times22$ indépendantes reproduisent les
   secteurs actifs des modèles de revêtement, d'Enriques et de Nikulin.

Le résultat conceptuel le plus important est plus général que le scan Cox :

> **Dans le cadre d'une involution holomorphe d'ordre deux préservant
> $L$ et du tube propre isotrope utilisé en R61–R62, ni la branche qui
> préserve les deux composantes, ni celle qui les échange ne peut fournir le
> tube isotrope pair fermé demandé par la projection O3/O7 standard.**

Ce résultat ne détruit ni la dégénérescence de Tyurin de R63, ni le mécanisme
parent \(\mathcal N=2\). Il ferme une voie orientifold fermée précise.

---

## 2. Données extraites et contrôle croisé

Dans la base intégrale

\[
B=(D_1,D_2,D_5,D_7,E),
\]

la restriction est

\[
\rho_B=
\begin{pmatrix}
1&0&0&0&0\\
0&1&0&0&0
\end{pmatrix},
\qquad \operatorname{SNF}(\rho_B)=(1,1).
\]

Le programme ne charge aucun module Python antérieur. Il contient une copie
indépendante des rayons et de la matrice de Gale, vérifie leur orthogonalité,
puis les compare au manifeste JSON de R63. Les restrictions obtenues sont :

| Diviseur | Classe sur $S$ | Carré |
|---|---:|---:|
| $D_0$ | $2h_1+2h_2$ | $16$ |
| $D_1,D_4$ | $h_1$ | $0$ |
| $D_2,D_3$ | $h_2$ | $0$ |
| $D_5,D_6,D_7,E$ | $0$ | $0$ |

Ainsi

\[
\ker\rho_B=\langle D_5,D_7,E\rangle,
\]

et la nouvelle classe exceptionnelle est bien verticale. Le calcul de Smith
montre que l'image est primitive.

Cette conclusion suppose, comme R63, une branche $(4,4)$ très générale. Sur
un lieu de Noether–Lefschetz, $NS(S)$ peut être plus grand que $U(2)$, mais
la copie de $L$ ci-dessus reste la polarisation provenant des deux
composantes.

---

## 3. Solution symbolique de $O(U(2),\mathbb Z)$

Écrivons

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]

L'équation $A^tG_LA=G_L$ équivaut exactement à

\[
ac=0,\qquad bd=0,\qquad ad+bc=1.
\]

Ce système se résout sans scan borné.

- Si $c=0$, alors $ad=1$, donc $a=d=1$ ou $a=d=-1$, et
  $bd=0$ impose $b=0$. On obtient $I,-I$.
- Si $a=0$, alors $bc=1$, donc $b=c=1$ ou $b=c=-1$, et
  $bd=0$ impose $d=0$. On obtient $S,-S$.

Les quatre solutions sont des involutions. Le scan dans la boîte
\([-4,4]^4\) fourni par le programme est seulement un test de régression ;
la preuve d'exhaustivité est le raisonnement symbolique précédent.

### 3.1 Cône ample

Pour $x=ah_1+bh_2$,

\[
x^2=4ab.
\]

Il n'existe aucune racine de carré $-2$ dans $U(2)$, car tous les carrés
sont divisibles par quatre. Pour la K3 très générale, il n'existe donc aucune
paroi de Weyl intérieure et

\[
\operatorname{Amp}(S)=\{ah_1+bh_2:a>0,\ b>0\},
\]

avec cône nef fermé $a,b\geq0$. Seuls $I$ et $S$ préservent cette
composante. L'échange $S$ fixe une polarisation $ah_1+bh_2$ si et seulement
si $a=b$. Pour une polarisation asymétrique générique, seul $I$ subsiste.

L'existence de $S$ comme isométrie de réseau ou comme symétrie du fan ne
signifie pas qu'une équation $(4,4)$ générique soit invariante : il faut
imposer aux coefficients d'être symétriques sous l'échange des deux facteurs.

### 3.2 Sous-réseaux propres de $L$

| Action sur $L$ | $L^+$ | Signature | $L^-$ | Signature | Indice de $L^+\oplus L^-$ |
|---|---|---:|---|---:|---:|
| $I$ | $L$ | $(1,1)$ | $0$ | $(0,0)$ | 1 |
| $-I$ | $0$ | $(0,0)$ | $L$ | $(1,1)$ | 1 |
| $S$ | $\langle h_1+h_2\rangle$ | $(1,0)$ | $\langle h_1-h_2\rangle$ | $(0,1)$ | 2 |
| $-S$ | $\langle h_1-h_2\rangle$ | $(0,1)$ | $\langle h_1+h_2\rangle$ | $(1,0)$ | 2 |

L'indice deux dans les deux dernières lignes est important : la décomposition
rationnelle en espaces propres n'est pas une somme directe primitive sur
\(\mathbb Z\).

### 3.3 Classes isotropes

L'équation $x^2=4ab=0$ impose $a=0$ ou $b=0$. Avec la primitivité
\(\gcd(a,b)=1\), on obtient exactement

\[
\boxed{x\in\{\pm h_1,\pm h_2\}.}
\]

Dans le cône nef, les deux rayons primitifs sont $h_1,h_2$. Ils sont échangés
par $S$ : leurs combinaisons propres $h_1\pm h_2$ ont carrés $+4$ et
$-4$, jamais zéro. Un échange des rulings ne produit donc pas une classe
isotrope propre dans $L$.

---

## 4. Automorphismes toriques : classification exhaustive

Le programme choisit, parmi les rayons, une base unimodulaire du réseau. Tout
automorphisme $GL(n,\mathbb Z)$ du fan est déterminé de façon unique par les
images de cette base, lesquelles doivent être des rayons. Toutes les suites
ordonnées possibles de rayons cibles sont énumérées, puis les cônes maximaux
sont contrôlés. Ce procédé est fini et exhaustif ; il ne repose pas sur une
borne arbitraire sur les coefficients des matrices.

### 4.1 Fan de couture

Pour les six rayons et huit cônes de la couture :

\[
|\operatorname{Aut}_{\rm fan}(T)|=8.
\]

Le groupe possède les ordres d'éléments

\[
1^1,\qquad 2^5,\qquad 4^2,
\]

donc la structure attendue du groupe diédral d'ordre huit. Sur $L$, quatre
éléments induisent $I$, quatre induisent $S$. Aucun n'induit $-I$ ou
$-S$, conformément au critère du cône ample.

### 4.2 Fan résolu 4D et échange des tops

Pour les neuf rayons et vingt cônes maximaux résolus :

\[
|\operatorname{Aut}_{\rm fan}(V)|=8.
\]

Les huit automorphismes préservent exactement le caractère de hauteur $q$.
Il n'existe aucun automorphisme de ce fan qui envoie $q$ sur $-q$. Par
conséquent, l'échange des deux tops n'est pas réalisé toriquement dans la phase
résolue actuelle. Ceci renforce le simple test de multiplicité des rayons de
hauteur positive et négative de R62.

Cette exhaustivité concerne les automorphismes **de réseau du fan donné**. Elle
ne classifie pas des transformations birationnelles après flop ni des
automorphismes non toriques du Calabi–Yau.

---

## 5. Reproduction indépendante du scan Cox

Les sommets rationnels du polytope défini par

\[
\langle m,\nu_i\rangle\geq-1
\]

sont recalculés par intersections de quatre facettes. Ils donnent des bornes
entières prouvées pour l'énumération, et non une boîte choisie empiriquement.
Le programme retrouve :

- 14 sommets du polytope dual résolu ;
- 104 points de réseau ;
- histogramme de hauteur $(-1:10,0:35,1:34,2:25)$ ;
- 69 monômes dans la sous-famille `sigma5` ;
- 35 monômes avant projection sur la couture, dont 26 pour `sigma5`.

Pour chacun des $512$ signes des neuf coordonnées de Cox, on calcule le
motif de signes sur les 35 monômes, modulo le signe global du polynôme. Il y a
exactement huit motifs, chacun avec 64 relèvements. Ils coïncident avec les
huit caractères $(A,C,D)\in(\mathbb Z/2)^3$.

Sur le tore dense, une translation de signe laisse
$d\log z_1\wedge d\log z_2\wedge d\log z_3$ invariant. La formule de résidu
de Poincaré donne donc à $\Omega_S$ le même signe que l'espace propre choisi
pour le polynôme : l'inverse a le même signe pour une action d'ordre deux.

| Caractère | Monômes conservés | Répartition $a=(-1,0,1)$ | Signe de $\Omega_S$ | Identification de R62 |
|---:|---:|---:|---:|---|
| 000 | 35 | $(25,9,1)$ | $+$ | identité |
| 001 | 22 | $(15,6,1)$ | $-$ | non sympl., deux elliptiques |
| 010 | 22 | $(15,6,1)$ | $-$ | non sympl., deux elliptiques |
| 011 | 19 | $(13,5,1)$ | $+$ | Nikulin symplectique |
| 100 | 26 | $(25,0,1)$ | $-$ | revêtement `sigma5` |
| 101 | 19 | $(15,3,1)$ | $+$ | Nikulin symplectique |
| 110 | 19 | $(15,3,1)$ | $+$ | Nikulin symplectique |
| 111 | 18 | $(13,4,1)$ | $-$ | Enriques `sigma125` |

Les nombres de monômes, les motifs et le signe de la forme holomorphe sont des
sorties combinatoires indépendantes. Les mots « Nikulin », « Enriques » et
« deux elliptiques » utilisent la classification géométrique des involutions
K3 ; ils ne sont pas redémontrés par un comptage de monômes.

Le scan est exhaustif pour les **signes diagonaux des neuf coordonnées**. Il ne
l'est pas pour toutes les transformations polynomiales ou tous les
automorphismes abstraits d'une spécialisation de K3.

---

## 6. Reconstruction intégrale de l'orthogonal actif

Prenons

\[
\Lambda_{K3}=U_1\oplus U_2\oplus U_3\oplus
E_8(-1)_a\oplus E_8(-1)_b.
\]

Dans les deux premiers plans hyperboliques, l'inclusion

\[
h_1=e_1+e_2,\qquad h_2=f_1+f_2
\]

a Gram $U(2)$ et est primitive. Son orthogonal possède la base

\[
e_1-e_2,\quad f_1-f_2,\quad e_3,\quad f_3,\quad
E_8(-1)_a,\quad E_8(-1)_b,
\]

d'où

\[
K=L^\perp=U(2)\oplus U\oplus E_8(-1)^{\oplus2}.
\]

Le programme vérifie exactement :

\[
\operatorname{sign}(K)=(2,18),\qquad |\det K|=4,
\]

\[
\operatorname{SNF}(G_K)=(1^{18},2,2).
\]

Ici, la Smith est celle de la **forme de Gram de $K$**. Elle est cohérente
avec le morphisme gradué de R63, mais ne doit toujours pas être annoncée comme
la Smith de la matrice intégrale complète de Gauss–Manin.

L'inclusion $L\hookrightarrow\Lambda_{K3}$ est primitive, tandis que
$L\oplus K$ a indice quatre dans $\Lambda_{K3}$, ce qui rend explicite le
recollement discriminant.

### 6.1 Isotropes actifs

Le réseau parent $K$ contient des vecteurs isotropes primitifs. Le programme
en expose deux exactement :

- $e_3$ dans le facteur $U$, de divisibilité 1 ;
- $e_1-e_2$ dans le facteur $U(2)$, de divisibilité 2.

Ainsi le mécanisme isotrope parent n'est pas vide. R64 ne prétend pas ici
classifier toutes les orbites de vecteurs isotropes sous $O(K)$. Une telle
classification demanderait un argument de genre/discriminant supplémentaire ;
les deux divisibilités sont des témoins, pas une preuve d'exhaustivité des
orbites.

---

## 7. Modèles entiers d'involutions et secteurs actifs

Trois involutions sont construites comme matrices entières $22\times22$, et
non comme signatures inscrites à la main.

1. **Revêtement :** échange de $U_1,U_2$, signe moins sur
   $U_3\oplus E_8(-1)^2$.
2. **Enriques :** échange de $U_1,U_2$, signe moins sur $U_3$, échange des
   deux copies de $E_8(-1)$.
3. **Nikulin symplectique :** identité sur $U^3$, échange des deux copies de
   $E_8(-1)$.

Chaque matrice vérifie

\[
\iota^2=I,\qquad \iota^tG_{K3}\iota=G_{K3},\qquad \iota|_L=I.
\]

Le programme résout les noyaux propres et les intersecte avec $L^\perp$.

| Modèle | $\operatorname{sign}K^+$ | Isotrope dans $K^+$ ? | $\operatorname{sign}K^-$ | Isotrope explicite dans $K^-$ ? |
|---|---:|---:|---:|---:|
| revêtement | $(0,0)$ | non | $(2,18)$ | oui |
| Enriques | $(0,8)$ | non | $(2,10)$ | oui |
| Nikulin sympl. | $(2,10)$ | oui | $(0,8)$ | non |

Pour Enriques et Nikulin, le bloc défini négatif est explicitement
$E_8(-2)$. Ces calculs reproduisent les signatures employées en R61–R62,
mais à partir de réalisations intégrales dans le réseau K3.

---

## 8. No-go de signature élargi

### 8.1 Composantes de Tyurin préservées

Si les deux branches locales $u=0$ et $v=0$ sont préservées, le signe du
normal logarithmique est $+1$. La condition O3/O7

\[
\iota^*\Omega_3=-\Omega_3,
\qquad \Omega_3\sim\Omega_S\wedge d\log u
\]

impose alors

\[
\iota^*\Omega_S=-\Omega_S.
\]

L'involution de la K3 est holomorphe non symplectique. Son réseau invariant
$H^2(S,\mathbb Z)^+$ est hyperbolique et possède exactement une direction
positive. Comme l'action préserve $L$ et son cône ample, la classification
de la section 3 montre qu'elle agit sur $L$ par $I$ ou $S$. Dans les deux
cas la classe

\[
H=h_1+h_2
\]

est ample, invariante et positive. Elle consomme l'unique direction positive
du réseau invariant. Par conséquent

\[
K^+=L^\perp\cap H^2(S,\mathbb Z)^+
\]

est négatif défini (ou nul), donc ne contient aucun vecteur isotrope non nul.

Or un tube propre pair lorsque le normal est pair demande précisément une
classe $C\in K^+$ isotrope. Cette branche échoue donc pour **toute**
involution holomorphe non symplectique préservant $L$, et pas seulement pour
les quatre caractères non symplectiques du scan diagonal.

### 8.2 Composantes de Tyurin échangées

Si $u\leftrightarrow v$, alors $d\log u\mapsto-d\log u$. La condition
O3/O7 impose cette fois

\[
\iota^*\Omega_S=+\Omega_S,
\]

donc une involution symplectique sur la K3. Pour que
$C\times S^1$ soit pair alors que le cercle change d'orientation, il faut
$C\in K^-$. Pour une involution symplectique non triviale d'ordre deux,

\[
H^2(S,\mathbb Z)^-\simeq E_8(-2),
\]

qui est négatif défini. Pour l'identité, le secteur impair est nul. Dans les
deux cas, il n'existe aucun $C\ne0$ isotrope dans le secteur requis.

Cette deuxième obstruction est indépendante de l'absence, déjà prouvée, d'un
échange torique des tops actuels.

### 8.3 Portée exacte

Le no-go élargi suppose simultanément :

- une involution **holomorphe** d'ordre deux ;
- la projection O3/O7 standard ;
- $L$ préservé comme réseau de restriction ;
- un tube fermé propre $C\times S^1$, état propre de l'involution ;
- une classe $C\in L^\perp$ non nulle et isotrope ;
- le vecteur fermé issu du secteur pair de $C_4$.

Il ne couvre pas :

- le parent \(\mathcal N=2\) sans projection ;
- une paire brane–image qui n'est pas un état propre simple ;
- les secteurs ouverts, non géométriques ou anti-holomorphes ;
- un groupe d'ordre supérieur à deux ;
- un cycle non isotrope ou un autre mécanisme de tour ;
- une modification de la dégénérescence qui ne préserve plus $L$ ;
- la stabilité quantique et les invariants BPS.

---

## 9. Ce qui est exhaustif et ce qui ne l'est pas

| Objet | Statut R64 | Justification |
|---|---|---|
| $O(U(2),\mathbb Z)$ | **exhaustif** | solution symbolique des équations entières |
| Sous-groupe du cône ample | **exhaustif** | quatre isométries seulement, test exact |
| Isotropes primitifs de $U(2)$ | **exhaustif** | équation $4ab=0$ |
| Automorphismes de réseau du fan de couture | **exhaustif** | images d'une base unimodulaire |
| Automorphismes de réseau du fan résolu | **exhaustif** | images d'une base unimodulaire |
| Signes diagonaux de Cox | **exhaustif** | les $512$ relèvements sont tous parcourus |
| Modèles revêtement/Enriques/Nikulin | **exact pour ces modèles** | matrices intégrales explicites |
| No-go de signature dans le cadre §8.3 | **exhaustif conditionnel** | signatures de Hodge + classification symplectique |
| Toutes les involutions géométriques sur tous les lieux NL | **non classifié** | périodes, ample cone élargi et Torelli manquants |
| Automorphismes non toriques/non linéaires | **non classifié** | absents des données Cox discrètes |
| Orbites complètes des isotropes dans $K$ | **non classifié** | analyse discriminante supplémentaire requise |
| Monodromie intégrale de Gauss–Manin | **non calculée** | transport parallèle absent |

Il serait donc incorrect d'écrire « toutes les involutions imaginables sont
exclues ». La formulation correcte est : « toutes les involutions du mécanisme
holomorphe O3/O7 fermé défini au §8.3 sont exclues par signature ».

---

## 10. Conséquence pour la suite de DDF

R64 montre qu'un nouveau choix de signe de Cox, un autre vecteur isotrope dans
le même orthogonal, ou le simple échange $h_1\leftrightarrow h_2$ ne peut pas
sauver la tour fermée paire. La suggestion de R61 consistant à chercher un
« plan hyperbolique invariant supplémentaire » dans $K^+$ est incompatible
avec la signature $(1,r-1)$ du réseau invariant non symplectique tant que
$L$ contient une classe ample invariante.

Les voies réellement différentes sont donc :

1. conserver le résultat Tyurin et la tour candidate dans le parent
   \(\mathcal N=2\) ;
2. changer le mécanisme physique : brane–image, secteur ouvert, état non
   propre ou cycle non isotrope ;
3. changer le type de projection/action, et non simplement son représentant
   dans $O(U(2))$ ;
4. dériver d'abord la métrique $R(t)$ sans supposer qu'une tour BPS paire
   \(\mathcal N=1\) est déjà disponible.

Le résultat géométrique strict de R63 reste intact. Le plan de Fano et une
valeur micrométrique restent hors du périmètre de ce contre-calcul.

---

## 11. Reproductibilité

Exécution :

```bash
python3 meta_audit_r64/r64_lattice_classification.py
```

La sortie finale doit contenir :

```text
U2_ISOMETRY_AND_AMPLE_CONE_CLASSIFICATION: EXACT_COMPLETE
SEAM_AND_RESOLVED_FAN_LATTICE_AUTOMORPHISMS: EXACT_COMPLETE
DIAGONAL_COX_SIGN_SCAN: EXACT_COMPLETE
BRANCH_PRESERVING_HOLOMORPHIC_NONSYMPLECTIC_ACTIVE_EVEN_ISOTROPIC: NONE
TOP_EXCHANGING_HOLOMORPHIC_SYMPLECTIC_ACTIVE_ODD_ISOTROPIC: NONE
ALL_GEOMETRIC_K3_INVOLUTIONS_ON_SPECIAL_NOETHER_LEFSCHETZ_LOCI: NOT_CLASSIFIED
```

Toutes les incohérences arithmétiques arrêtent le programme par assertion.

## 12. Références théoriques utilisées pour interpréter les matrices

1. B. van Geemen, A. Sarti, *Nikulin involutions on K3 surfaces*,
   [arXiv:math/0602015](https://arxiv.org/abs/math/0602015).
2. A. Garbagnati, A. Sarti, *On symplectic and non-symplectic automorphisms
   of K3 surfaces*, Rev. Mat. Iberoam. 29 (2013) 135–162,
   [doi:10.4171/RMI/716](https://doi.org/10.4171/RMI/716).
3. A. Artebani, A. Sarti, S. Taki, *K3 surfaces with non-symplectic
   automorphisms of prime order*,
   [arXiv:0903.3481](https://arxiv.org/abs/0903.3481).
4. T. W. Grimm, J. Louis, *The effective action of $N=1$ Calabi–Yau
   orientifolds*, [arXiv:hep-th/0403067](https://arxiv.org/abs/hep-th/0403067).

