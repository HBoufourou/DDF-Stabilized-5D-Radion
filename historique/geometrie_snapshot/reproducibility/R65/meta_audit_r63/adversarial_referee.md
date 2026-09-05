# R63 — Rapport adversarial sur le certificat quasi-Fano

## Mandat et verdict

Fichiers examinés :

- `meta_audit_r63/quasifano_normal_bundles.md` ;
- `meta_audit_r63/r63_quasifano_certificate.py` ;
- `meta_audit_r63/r63_ems_cohomology_audit.py`.

Les deux scripts ont été exécutés sans erreur. Le premier retourne le
certificat torique annoncé ; le second trouve zéro cellule de poids réalisable
portant une cohomologie non nulle, pour les deux composantes.

**Verdict de rapporteur : PASS conditionnel, sans erreur mathématique fatale.**
Le cœur nouveau de R63 est correct : sous les hypothèses de R62 déjà invoquées
(ambiant relatif projectif, espace total et membres restreints génériques
lisses, fibre centrale SNC), les deux composantes ont

\[
H^i(Y_p,\mathcal O_{Y_p})=H^i(Y_m,\mathcal O_{Y_m})=0\qquad(i>0),
\]

la couture est une K3 anticanonique, et ses deux fibrés normaux sont même
individuellement triviaux. Le passage de « Tyurin-type » à une dégénérescence
de Tyurin au sens quasi-Fano de Doran--Harder--Thompson est donc justifié.

Il reste toutefois plusieurs corrections de présentation et de robustesse du
certificat avant d'utiliser le mot **prouvé** dans un article. Elles sont
énumérées à la section 7. Elles ne renversent pas le verdict.

## 1. Contrôle des objets : aucune confusion dimensionnelle détectée

La séparation suivante est maintenue correctement dans le rapport :

| Objet | Définition | Dimension |
|---|---|---:|
| \(D_p,D_m\) | diviseurs toriques de l'ambiant relatif \(X\) | 4 |
| \(Y_p,Y_m\) | \(\mathcal Y\cap D_p\), \(\mathcal Y\cap D_m\) | 3 |
| \(T\) | \(D_p\cap D_m\) | 3 |
| \(S\) | \(\mathcal Y\cap T=Y_p\cap Y_m\) | 2 |

En particulier, la suite avec \(\mathcal O_V(-T)\) est une suite dans le
quatre-fold torique \(V=D_j\), tandis que la normale finale
\(N_{S/Y_j}\) vit sur la surface \(S\). Je n'ai trouvé aucun passage où
\(D_j\) serait remplacé illicitement par \(Y_j\), ou \(T\) par \(S\).

## 2. Audit du signe \(K_V+Y=-T\)

Prenons \(V_p=D_p\) et \(Y_p=\mathcal Y|_{D_p}\). L'adjonction donne

\[
K_{V_p}=(K_X+D_p)|_{D_p}.
\]

Comme \(\mathcal Y\sim-K_X\),

\[
K_{V_p}+Y_p
=(K_X+D_p+\mathcal Y)|_{D_p}
\sim D_p|_{D_p}.
\]

Or \(D_p+D_m=\operatorname{div}(z)\sim0\), donc

\[
D_p|_{D_p}\sim-D_m|_{D_p}=-T.
\]

Ainsi

\[
\boxed{K_{V_p}+Y_p\sim-T.}
\]

Le même calcul échangeant \(p\) et \(m\) donne
\(K_{V_m}+Y_m\sim-T\). Le signe négatif du rapport est donc correct. Un
signe positif à cet endroit détruirait le calcul de Serre ; ce n'est pas ce
qui est écrit.

Correction typographique recommandée : employer \(\sim\) ou un isomorphisme
de fibrés plutôt que le signe \(=\), sauf lorsqu'on a explicitement fixé des
représentants de Cartier.

Le calcul tridimensionnel est également correct. Dans l'espace total
\(\mathcal Y\),

\[
K_{Y_p}=(K_{\mathcal Y}+Y_p)|_{Y_p}
\sim Y_p|_{Y_p}
\sim-Y_m|_{Y_p}=-S,
\]

et de même pour \(Y_m\). Il s'ensuit bien que \(S\in|-K_{Y_j}|\).

## 3. Audit des suites exactes et de la dualité de Serre

### 3.1 Acyclicité de \(\mathcal O_V(-T)\)

Pour \(V=V_p\) ou \(V_m\), la suite de Cartier

\[
0\longrightarrow\mathcal O_V(-T)
\longrightarrow\mathcal O_V
\longrightarrow\mathcal O_T\longrightarrow0
\]

est la bonne suite. Puisque \(V\) et \(T\) sont toriques complets et
connexes,

\[
H^{>0}(V,\mathcal O_V)=H^{>0}(T,\mathcal O_T)=0,
\qquad
H^0(V,\mathcal O_V)=H^0(T,\mathcal O_T)=\mathbf C.
\]

La restriction des constantes est l'identité, donc la suite longue donne

\[
H^q(V,\mathcal O_V(-T))=0\quad(0\le q\le4).
\]

Le groupe en degré zéro n'a pas été oublié : son annulation utilise
précisément l'injectivité de la restriction des constantes.

### 3.2 Passage de \(-T\) à \(-Y\)

En dimension quatre, la dualité de Serre appliquée à
\(L=\mathcal O_V(-Y)\) donne

\[
H^k(V,L)^\vee
\simeq H^{4-k}(V,K_V\otimes L^{-1})
=H^{4-k}(V,\mathcal O_V(K_V+Y)).
\]

Avec \(K_V+Y\sim-T\), le membre de droite est nul dans tous les degrés.
Donc \(\mathcal O_V(-Y)\) est acyclique. La suite

\[
0\longrightarrow\mathcal O_V(-Y)
\longrightarrow\mathcal O_V
\longrightarrow\mathcal O_Y\longrightarrow0
\]

donne alors

\[
h^\bullet(Y,\mathcal O_Y)=(1,0,0,0).
\]

Il n'y a ici ni mauvais degré de Serre, ni hypothèse de Kodaira cachée, ni
confusion entre l'annulation torique sur \(V\) et une annulation qu'il aurait
fallu supposer sur \(Y\).

### 3.3 Couture K3

La suite

\[
0\longrightarrow\mathcal O_T(K_T)
\longrightarrow\mathcal O_T
\longrightarrow\mathcal O_S\longrightarrow0
\]

et Serre en dimension trois donnent bien

\[
h^\bullet(S,\mathcal O_S)=(1,0,1).
\]

L'adjonction fournit \(K_S\simeq\mathcal O_S\). Sous la lissité générique
déjà certifiée en R62, cela prouve que \(S\) est une K3 connexe ; la connexité
n'est pas simplement supposée.

## 4. Audit des fibrés normaux individuels

Le produit trivial

\[
N_{S/Y_p}\otimes N_{S/Y_m}\simeq\mathcal O_S
\]

découle déjà de \(Y_p+Y_m=\operatorname{div}(z)\). R63 affirme plus : chaque
facteur est trivial. Cette affirmation résiste à l'audit.

Sur \(V_p\), le caractère quotient \(\ell_p=q+s\) vérifie

\[
\operatorname{div}(\chi^{\ell_p})=-D_5+D_m.
\]

Il définit un morphisme torique \(f_p:V_p\to\mathbf P^1\), les deux fibres
toriques opposées étant \(D_5\) et \(D_m=T\). Comme
\(D_5\cap D_m=\varnothing\),

\[
\mathcal O_{V_p}(D_m)|_T
\simeq\mathcal O_{V_p}(D_5)|_T
\simeq\mathcal O_T.
\]

Sur \(V_m\), le caractère \(\ell_m=q\) vérifie

\[
\operatorname{div}(\chi^{\ell_m})=-D_p+D_6+D_E.
\]

Ainsi \(D_p=T\) est la fibre opposée à la fibre réductible
\(D_6\cup D_E\). Les non-faces \(D_6D_p\) et \(D_ED_p\) donnent la
disjonction nécessaire, d'où

\[
\mathcal O_{V_m}(D_p)|_T\simeq\mathcal O_T.
\]

Enfin, pour les intersections transverses de R62,

\[
N_{S/Y_j}
\simeq N_{T/V_j}|_S
\simeq\mathcal O_S.
\]

Ce passage est un isomorphisme de fibrés, pas seulement une annulation de
première classe de Chern. L'argument serait faux si les intersections
n'étaient pas schématiquement transverses ; c'est pourquoi la dépendance au
certificat SNC de R62 doit rester explicite.

J'ai recomputé les non-faces de taille deux directement depuis les 28 cônes.
La liste obtenue est exactement

\[
(06),(07),(14),(23),(56),(5E),(5m),(6p),(7E),(Ep),
\]

donc les trois disjonctions utilisées ci-dessus ne proviennent pas d'une
table SR incohérente.

## 5. Audit indépendant du script EMS

### 5.1 Degré du complexe

Pour un diviseur torique \(D=\sum a_\rho D_\rho\) et un poids
\(u\in M\), le sous-complexe pertinent est le complexe induit par

\[
I(u)=\{\rho:\langle u,v_\rho\rangle+a_\rho<0\}.
\]

Sur un fan simplicial complet,

\[
H^i(V,\mathcal O_V(D))_u
\simeq
\widetilde H^{,i-1}(\Delta_{I(u)};\mathbf C).
\]

Les cônes maximaux de \(V_p,V_m\) ont quatre rayons. Le complexe abstrait a
donc des simplexes jusqu'au degré trois. Les quatre nombres calculés par
`reduced_betti` correspondent correctement à

\[
\widetilde b_0,\widetilde b_1,\widetilde b_2,\widetilde b_3,
\]

donc aux cohomologies \(H^1,H^2,H^3,H^4\). Le décalage EMS n'est pas inversé.
La fonction calcule l'homologie réduite rationnelle plutôt que la cohomologie
réduite complexe, mais les dimensions de Betti coïncident sur un corps : ce
n'est pas une erreur.

Le degré \(H^0\), qui correspond au cas de degré réduit \(-1\), est traité
séparément par le test de la cellule `empty_bad_set`. Cette séparation est
correcte et devrait être mentionnée plus explicitement dans le commentaire du
code.

### 5.2 Seuils et classe du diviseur

Le vecteur `REFERENCE_EXPONENT` n'est pas arbitraire : il représente une
section monomiale de \(\mathcal O(Y)\). J'ai vérifié indépendamment que les
coefficients de \(-Y\) utilisés par le script diffèrent de ceux de
\(K_V+T\) par un diviseur principal.

Dans les coordonnées quotient \((a,c,d,q+s)\) de \(V_p\), la différence est
le diviseur du caractère

\[
u_p=(1,1,1,0).
\]

Dans les coordonnées \((a,q,c,d)\) de \(V_m\), elle est le diviseur du
caractère

\[
u_m=(1,0,1,1).
\]

Les seuils EMS représentent donc bien \(\mathcal O(-Y_j)\), et non son dual
ou une classe ambiante mal restreinte.

### 5.3 Énumération et faisabilité

Le script énumère les \(2^8\) et \(2^9\) motifs de signes possibles. Pour
chaque motif topologiquement susceptible de porter de la cohomologie, les
inégalités strictes sur les poids entiers sont correctement remplacées par
des inégalités fermées décalées d'une unité. L'élimination de
Fourier--Motzkin travaille exactement sur \(\mathbf Q\). Montrer que le
polyèdre rationnel est vide est plus fort que montrer qu'il ne contient aucun
point du réseau.

Résultat reproduit :

| Composante | Motifs topologiquement non nuls | Motifs réalisables | \(H^0,\ldots,H^4(\mathcal O(-Y))\) |
|---|---:|---:|---:|
| \(V_p\) | 15 | 0 | \((0,0,0,0,0)\) |
| \(V_m\) | 47 | 0 | \((0,0,0,0,0)\) |

Un balayage indépendant des poids dans la boîte \([-4,4]^4\) donne également
zéro poids portant \(H^{>0}\) et zéro poids donnant une section globale. Ce
balayage n'est qu'un contrôle de fumée ; la preuve exhaustive reste
l'élimination exacte par cellules.

## 6. Ce que les scripts prouvent réellement

`r63_quasifano_certificate.py` vérifie correctement les données combinatoires
nécessaires : étoiles, unimodularité, classes sur \(T\), caractères vers
\(\mathbf P^1\) et non-faces utiles. En revanche, les dernières lignes

```text
h^i(O_Yp)=h^i(O_Ym)=(1,0,0,0)
Tyurin/DHT quasi-Fano: YES
```

sont des **sorties déclaratives**, pas des assertions calculées par ce premier
script. Leur preuve se trouve dans le rapport par les suites exactes, et leur
contre-vérification calculatoire se trouve dans le script EMS. Cette
distinction doit être explicite dans tout dossier de dépôt.

De même, l'unimodularité et l'appariement de tous les murs ne suffisent pas,
pris isolément, à certifier la complétude d'un fan arbitraire. Ici la
complétude est bien disponible parce que R62 certifie le support relatif et la
projectivité de \(X\to\mathbb A^1\), dont les composantes de fibre sont
propres. Le rapport R63 doit citer cette entrée au moment exact où il affirme
que \(V_p,V_m,T\) sont complets, au lieu de laisser entendre que le seul
comptage des murs suffit toujours.

## 7. Corrections nécessaires avant dépôt

### Nécessaires dans le texte

1. Remplacer les égalités de classes comme \(K_V+Y=-T\) par \(\sim\), ou
   écrire les isomorphismes de fibrés correspondants.
2. À chaque emploi de « Tyurin stricte », rappeler en une phrase les entrées
   reprises de R62 : projectivité/propreté, lissité générique de
   \(\mathcal Y,Y_p,Y_m,S\), et modèle SNC.
3. Pour la complétude des étoiles, invoquer explicitement la propreté de la
   fibre provenant du certificat de support R62. L'appariement des murs reste
   un contrôle, pas l'unique preuve générale.
4. Écrire les deux diviseurs principaux
   \(\operatorname{div}(\chi^{q+s})=D_m-D_5\) et
   \(\operatorname{div}(\chi^q)=D_6+D_E-D_p\). Cela rend la trivialité
   individuelle des normales immédiatement vérifiable.
5. Qualifier le résultat de « Tyurin au sens de la définition DHT employée ».
   Le mot *strict* est utile dans le corpus DDF pour l'opposer à
   *Tyurin-type*, mais il n'est pas une nouvelle notion universelle.

### Nécessaires pour durcir les certificats

1. Dans `r63_quasifano_certificate.py`, recomputer `SR_PAIRS` depuis
   `MAXIMAL_CONES` et imposer une assertion d'égalité. L'audit indépendant
   confirme que l'égalité passe avec les données actuelles.
2. Dans `r63_ems_cohomology_audit.py`, ajouter une assertion vérifiant que le
   vecteur `REFERENCE_EXPONENT`, après restriction à chaque étoile, représente
   bien la classe \(-K_V-T\) de \(Y\), ou de manière équivalente que
   \(-Y\sim K_V+T\). Les caractères explicites \(u_p,u_m\) ci-dessus donnent
   un test simple.
3. Renommer les dernières impressions du premier script en
   `THEOREM_DEDUCTION` ou `REPORT_CONSEQUENCE`. Elles ne doivent pas être
   présentées comme si Python avait vérifié Serre, la lissité ou la définition
   de DHT.
4. Ajouter dans le script EMS un commentaire disant que `reduced_betti`
   calcule l'homologie sur \(\mathbf Q\), dont les dimensions coïncident avec
   celles de la cohomologie sur \(\mathbf C\), et que \(H^0\) est traité à
   part.

## 8. Conclusion utilisable dans R63

Sous les hypothèses géométriques déjà certifiées en R62, la preuve suivante
est valide et courte :

\[
K_{V_j}+Y_j\sim-T,
\quad
H^\bullet(V_j,\mathcal O(-T))=0,
\quad
\text{Serre}\Longrightarrow
H^\bullet(V_j,\mathcal O(-Y_j))=0,
\]

puis la suite de l'hypersurface donne

\[
h^\bullet(Y_j,\mathcal O_{Y_j})=(1,0,0,0).
\]

Avec \(S\in|-K_{Y_j}|\) K3 lisse et
\(N_{S/Y_p}\simeq N_{S/Y_m}\simeq\mathcal O_S\), les deux \(Y_j\) sont des
quasi-Fano au sens DHT et la fibre centrale satisfait bien le verrou Tyurin
visé. Le certificat EMS constitue une contre-vérification indépendante
cohérente, avec le bon décalage de degré.

**Décision recommandée : accepter le résultat quasi-Fano de R63 après les
corrections de traçabilité ci-dessus ; ne pas le rétrograder pour une erreur de
signe, de normale ou de degré EMS, car aucune de ces erreurs n'est présente.**

