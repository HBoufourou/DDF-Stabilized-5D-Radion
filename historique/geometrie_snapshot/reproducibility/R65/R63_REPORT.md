# R63 — Porte de Tyurin stricte pour la famille résolue POLY944/sigma5

**Date :** 4 septembre 2026  
**Projet :** DDF I–VIII  
**Objet :** fermer les lacunes quasi-Fano, logarithmiques et LMHS laissées par R61–R62, sans introduire le plan de Fano ni une valeur micrométrique non dérivée.

## 1. Verdict exécutif

R63 obtient un résultat positif et plus fort que R62 :

> Pour des coefficients très généraux sur \(\mathbb C\), la famille torique
> résolue POLY944/sigma5, restreinte à un petit disque autour de \(t=0\),
> est une dégénérescence de Tyurin stricte, projective, saturée et
> log-lisse. Sa fibre centrale est
> \(\mathcal Y_0=Y_p\cup_S Y_m\), où \(Y_p,Y_m\) sont des trois-folds
> quasi-Fano et \(S\) est une K3 anticanonique commune. De plus,
> \(N_{S/Y_p}\simeq N_{S/Y_m}\simeq\mathcal O_S\).

Les annulations qui manquaient en R62 sont désormais démontrées par deux voies indépendantes :

1. deux suites exactes de diviseurs, l'annulation torique et la dualité de Serre ;
2. un calcul gradué de cohomologie torique de type Eisenbud–Mustaţă–Stillman, avec élimination exacte de tous les motifs de poids susceptibles de contribuer.

Le résultat est

\[
h^\bullet(Y_p,\mathcal O_{Y_p})
=h^\bullet(Y_m,\mathcal O_{Y_m})=(1,0,0,0).
\]

Pour une couture très générale, le réseau de restriction est \(L=U(2)\), de rang deux. La LMHS **rationnelle/complexe** est donc de type \(\mathrm{II}_{18}\), avec

\[
\dim\bigl(\operatorname{Gr}^W_2,\operatorname{Gr}^W_3,\operatorname{Gr}^W_4\bigr)
=(20,132,20),\qquad N^2=0,\qquad\operatorname{rang}N=20.
\]

Une correction importante est cependant imposée à R61 : la forme de Smith
\((1^{18},2,2)\) est certifiée pour le morphisme canonique du réseau gradué
K3, mais le code disponible ne calcule pas directement la matrice de
Gauss–Manin intégrale complète sur \(H^3(\mathcal Y_t,\mathbb Z)\).

Enfin, R63 ne dérive toujours ni \(R=R(t)\), ni une longueur en microns, ni
une tour KK/BPS stable. La géométrie nécessaire à une telle étude est mieux
fondée, mais la physique métrique reste une étape distincte.

## 2. Ce que R63 change par rapport à R62

| Énoncé | Fin de R62 | Fin de R63 |
|---|---:|---:|
| éventail relatif 5D lisse, cohérent, propre | démontré | confirmé indépendamment |
| famille anticanonique génériquement lisse | Bertini + jet | confirmé + témoins de Gröbner |
| fibre centrale réduite SNC à deux composantes | démontré génériquement | confirmé indépendamment |
| couture lisse | démontré | K3 connexe avec \(h^\bullet=(1,0,1)\) |
| \(S\in|-K_{Y_p}|\cap|-K_{Y_m}|\) | démontré par adjonction | redérivé intrinsèquement |
| \(H^{>0}(Y_p,\mathcal O)=H^{>0}(Y_m,\mathcal O)=0\) | ouvert | **démontré deux fois** |
| composantes quasi-Fano DHT | seulement « forme Tyurin » | **démontré** |
| fibrés normaux | produit attendu | chacun est trivial |
| log-lissité/d-semistabilité | implicite | **démontré** |
| LMHS \(\mathrm{II}_{18}\) sur \(\mathbb Q/\mathbb C\) | modèle compatible | **dérivée de la famille** |
| SNF de la monodromie intégrale complète | suraffirmée | **rétrogradée à ouverte** |
| \(R(t)\), échelle micrométrique, spectre | non démontré | non démontré |

## 3. Données géométriques fixées

On note

\[
\pi:\mathcal X\longrightarrow\Delta
\]

la restriction à un petit disque du cinq-fold torique relatif de R62, et

\[
\mathcal Y=\{P=0\}\subset\mathcal X
\]

l'hypersurface relative sigma5. Les onze coordonnées de Cox sont
\((x_0,\ldots,x_7,E,p,m)\), la coordonnée de base est

\[
t=pm,\qquad \operatorname{div}_{\mathcal X}(t)=D_p+D_m.
\]

On distingue systématiquement quatre objets :

\[
\begin{aligned}
V_p&:=D_p,&V_m&:=D_m &&\text{(quatre-folds toriques)},\\
Y_p&:=\mathcal Y\cap V_p,&Y_m&:=\mathcal Y\cap V_m
&&\text{(trois-folds)},\\
T&:=V_p\cap V_m&&&\text{(trois-fold torique)},\\
S&:=\mathcal Y\cap T=Y_p\cap Y_m&&&\text{(surface)}.
\end{aligned}
\]

Les étoiles du fan donnent :

| Ambiant | Rayons | Cônes maximaux | Rang de Picard |
|---|---:|---:|---:|
| \(V_p\) | 8 | 16 | 4 |
| \(V_m\) | 9 | 20 | 5 |
| \(T\) | 6 | 8 | 3 |

Tous ces fans quotients sont complets et lisses. Les classes intrinsèques extraites du réseau de Cox sont :

| Composante | \([Y_j]\) | \(-K_{V_j}\) | \([T]\) |
|---|---|---|---|
| \(Y_p\subset V_p\) | \((4,4,2,2)\) | \((4,4,2,3)\) | \((0,0,0,1)\) |
| \(Y_m\subset V_m\) | \((4,4,2,-1,1)\) | \((4,4,2,-1,2)\) | \((0,0,0,0,1)\) |

Dans les deux cas,

\[
\boxed{K_{V_j}+Y_j\sim -T,}
\]

Dans \(T\), avec une base \((H_1,H_2,F)\) de \(\operatorname{Pic}(T)\),

\[
-K_T=(4,4,2)=2[D_0].
\]

La restriction de l'équation est

\[
S:\quad x_7^2 A^0_{44}+c\,x_0^2=0,\qquad c\ne0,
\]

et possède précisément la classe \(-K_T\).

## 4. Contre-audit du noyau R62

Deux implémentations exactes indépendantes, plus une vérification Qhull et des
tests de Gröbner locaux, reproduisent les données critiques :

- 28 cônes relatifs de déterminant \(\pm1\) ;
- 28 sommets exacts du polyèdre de cohérence et écarts \(\{1,2,3,4,5\}\) ;
- complétion projective avec 48 cônes unimodulaires et 120 murs appariés ;
- réseau de Gale de rang six et saturé, le PGCD de ses 462 mineurs maximaux étant un ;
- support relatif de 69 monômes, tous de degré anticanonique \((4,4,3,2,-1,0)\) ;
- supports restreints de tailles \(60,35,26\) ;
- unique lieu de base pertinent \(x_6=x_7=0\), traité par le jet \(\partial_{x_6}P=cx_0^2E^2\ne0\) ;
- décompositions locales \((a,b)\cap(p,b)=(ap,b)\) et \((p)\cap(m)=(pm)\) ;
- existence de témoins exacts : branche \((4,4)\) lisse et paire \((2,2)/(4,4)\) transverse en 16 points.

Ainsi l'ouvert de coefficients nécessaire à Bertini, à la lissité de la
couture et à la transversalité est non vide. Aucun résultat n'est attribué à
Sage, Singular, Macaulay2, polymake ou Normaliz : ils ne sont pas installés
dans l'environnement du présent audit.

## 5. Première preuve des annulations quasi-Fano

Fixons \(j=p\) ou \(m\), et écrivons \(V=V_j\), \(Y=Y_j\). Les variétés
\(V\) et \(T\) sont toriques, lisses, projectives et connexes. Par annulation
torique,

\[
H^q(V,\mathcal O_V)=H^q(T,\mathcal O_T)=0\quad(q>0),
\qquad H^0(\mathcal O_V)=H^0(\mathcal O_T)=\mathbb C.
\]

La suite de la couture ambiante est

\[
0\longrightarrow\mathcal O_V(-T)\longrightarrow\mathcal O_V
\longrightarrow\mathcal O_T\longrightarrow0.
\]

La restriction des constantes \(\mathbb C\to\mathbb C\) est un isomorphisme.
La suite longue donne donc

\[
\boxed{H^q(V,\mathcal O_V(-T))=0\quad\text{pour tout }q.}
\]

Puisque \(K_V+Y\sim-T\), ou de façon équivalente
\(\mathcal O_V(K_V+Y)\simeq\mathcal O_V(-T)\), la dualité de Serre en
dimension quatre donne

\[
H^k(V,\mathcal O_V(-Y))^\vee
\simeq H^{4-k}(V,\mathcal O_V(K_V+Y))
=H^{4-k}(V,\mathcal O_V(-T))=0.
\]

La suite de l'hypersurface

\[
0\longrightarrow\mathcal O_V(-Y)\longrightarrow\mathcal O_V
\longrightarrow\mathcal O_Y\longrightarrow0
\]

implique enfin

\[
\boxed{h^\bullet(Y,\mathcal O_Y)=(1,0,0,0).}
\]

Cette preuve vaut séparément pour \(Y_p\) et \(Y_m\). Elle prouve aussi leur
connexité. Comme ils sont lisses, ils sont alors irréductibles ; cela fournit
une seconde fermeture de l'irréductibilité, indépendante des discriminants
quadratiques non carrés utilisés en R62.

## 6. Deuxième preuve : certificat EMS poids par poids

Le script meta_audit_r63/r63_ems_cohomology_audit.py applique la description
graduée de la cohomologie torique. Pour
\(D=\sum_\rho a_\rho D_\rho\) et \(u\in M\), il forme

\[
I(u)=\{\rho:\langle u,\nu_\rho\rangle+a_\rho<0\}.
\]

La pièce de poids \(u\) de \(H^i(V,\mathcal O(D))\) est calculée par la
cohomologie réduite du sous-complexe du fan induit par \(I(u)\). Pour
\(D=-Y_j\), le programme :

1. énumère les \(2^8\), respectivement \(2^9\), sous-ensembles de rayons ;
2. calcule exactement leurs nombres de Betti réduits ;
3. isole 15 motifs topologiquement dangereux sur \(V_p\) et 47 sur \(V_m\) ;
4. traduit chaque motif en inégalités intégrales de poids ;
5. prouve, par élimination de Fourier–Motzkin sur \(\mathbb Q\), que chacun de ces polyèdres est vide.

Il ne s'agit pas d'une recherche dans une boîte finie et aucun solveur
flottant n'intervient. Le résultat indépendant est

\[
H^k(V_p,\mathcal O(-Y_p))
=H^k(V_m,\mathcal O(-Y_m))=0,\qquad 0\le k\le4.
\]

La suite de l'hypersurface redonne donc exactement les mêmes annulations.
Cette seconde méthode est fondée sur la description topologique de la
cohomologie torique d'Eisenbud, Mustaţă et Stillman.

## 7. La couture est une K3, sans hypothèse cachée de connexité

Le diviseur \(S\) appartient à \(|-K_T|\). Sa suite exacte est

\[
0\longrightarrow\mathcal O_T(K_T)\longrightarrow\mathcal O_T
\longrightarrow\mathcal O_S\longrightarrow0.
\]

L'annulation torique et la dualité de Serre sur le trois-fold \(T\) donnent

\[
h^\bullet(S,\mathcal O_S)=(1,0,1).
\]

En particulier, \(S\) est connexe et \(h^1(S,\mathcal O_S)=0\). L'adjonction donne

\[
K_S=(K_T+S)|_S\simeq\mathcal O_S.
\]

Un membre lisse possède donc bien la structure d'une K3. La présentation comme
double couverture de \(\mathbb P^1\times\mathbb P^1\), ramifiée sur une courbe
\((4,4)\), fournit une vérification géométrique indépendante.

## 8. Anticanonicité et normales individuellement triviales

Dans l'espace total lisse \(\mathcal Y\),

\[
Y_p+Y_m=\operatorname{div}_{\mathcal Y}(t).
\]

Comme \(\mathcal Y\) est anticanonique dans \(\mathcal X\), l'adjonction donne
\(K_{\mathcal Y}\simeq\mathcal O_{\mathcal Y}\). Une nouvelle adjonction donne

\[
K_{Y_p}\sim-S,\qquad K_{Y_m}\sim-S.
\]

Le calcul torique donne davantage. Deux caractères primitifs définissent des morphismes

\[
f_p:V_p\to\mathbb P^1,\qquad f_m:V_m\to\mathbb P^1.
\]

Leurs hauteurs non nulles sur les rayons sont :

| Morphisme | Rayons de hauteur \(-1\) | Rayons de hauteur \(+1\) |
|---|---|---|
| \(f_p\) | \(x_5\) | \(m\) |
| \(f_m\) | \(p\) | \(x_6,E\) |

Dans \(V_p\), \(T=\{m=0\}\) est une fibre réduite ; dans \(V_m\),
\(T=\{p=0\}\) est la fibre réduite opposée à la fibre réductible
\(D_6\cup D_E\). Par conséquent,

\[
\mathcal O_{V_j}(T)|_T\simeq\mathcal O_T.
\]

Le carré d'intersection avec l'hypersurface étant transverse,

\[
N_{S/Y_j}\simeq N_{T/V_j}|_S.
\]

Ainsi

\[
\boxed{N_{S/Y_p}\simeq N_{S/Y_m}\simeq\mathcal O_S.}
\]

En particulier,

\[
N_{S/Y_p}\otimes N_{S/Y_m}\simeq\mathcal O_S,
\]

ce qui ferme la d-semistabilité. Ce produit trivial découle aussi directement
du diviseur principal \(Y_p+Y_m=\operatorname{div}(t)\).

Enfin,

\[
\mathcal O_{Y_j}(-K_{Y_j})\simeq
\mathcal O_{Y_j}(S)\simeq(f_j|_{Y_j})^*\mathcal O_{\mathbb P^1}(1).
\]

La classe anticanonique est donc semi-ample et nef, mais
\((-K_{Y_j})^3=S^3=0\). Les composantes sont quasi-Fano au sens de Tyurin/DHT,
mais ne sont pas weak Fano.

## 9. Semi-stabilité, log-lissité et canonique relatif

Les cartes locales de la famille sont

\[
t=u,\qquad t=v,\qquad t=uv.
\]

Sur la couture, la carte de monoïdes est

\[
\mathbb N\longrightarrow\mathbb N^2,\qquad1\longmapsto(1,1).
\]

Son conoyau en groupes est libre et sa forme de Smith vaut \(1\). La carte est
saturée : aucun modèle \(uv=t^k\), \(k>1\), n'est caché. Après restriction à
un disque assez petit, la famille est projective, plate, lisse sur
\(\Delta^*\), et sa fibre centrale est réduite SNC.

Le degré de l'hypersurface est

\[
[\mathcal Y]=\sum_\rho D_\rho=-K_{\mathcal X}.
\]

Comme \(K_\Delta\) est trivial,

\[
\omega_{\mathcal Y/\Delta}\simeq\mathcal O_{\mathcal Y},
\qquad
\omega^{\log}_{\mathcal Y/\Delta}\simeq\mathcal O_{\mathcal Y}.
\]

Les fibres générales lisses sont des Calabi–Yau : la même suite
anticanonique dans le quatre-fold torique général donne
\(h^1(\mathcal O)=h^2(\mathcal O)=0\), tandis que l'adjonction donne le
canonique trivial.

## 10. Porte de définition : Tyurin stricte

Doran–Harder–Thompson définissent une quasi-Fano comme une variété lisse dont
le système anticanonique contient un Calabi–Yau lisse et telle que
\(H^i(\mathcal O)=0\) pour tout \(i>0\). Une dégénérescence de Tyurin a deux
composantes quasi-Fano se rencontrant normalement le long d'un membre
anticanonique commun.

Toutes ces conditions sont maintenant fermées :

| Condition | Certificat R63 |
|---|---:|
| famille projective et plate sur un disque | oui |
| espace total lisse, canonique relatif trivial | oui, génériquement |
| fibre centrale réduite SNC, deux composantes | oui |
| \(Y_p,Y_m\) lisses, projectifs et irréductibles | oui |
| \(S\) K3 lisse et anticanonique des deux côtés | oui |
| \(H^{>0}(Y_p,\mathcal O)=H^{>0}(Y_m,\mathcal O)=0\) | oui, deux méthodes |
| d-semistabilité/log-lissité saturée | oui |

Verdict :

\[
\boxed{\mathcal Y\to\Delta\ \text{est une dégénérescence de Tyurin stricte.}}
\]

## 11. Réseau de restriction et LMHS

Pour une branche \((4,4)\) très générale, la K3 double couvre
\(\mathbb P^1\times\mathbb P^1\) et

\[
\operatorname{NS}(S)=U(2).
\]

Les deux classes de ruling s'étendent aux deux composantes et leur matrice de
restriction possède la SNF \((1,1)\). Les annulations
\(H^2(Y_j,\mathcal O)=0\) garantissent que toute classe intégrale de degré deux
sur \(Y_j\) est algébrique ; sa restriction appartient donc à
\(\operatorname{NS}(S)\). Ainsi l'image combinée est exactement et primitivement

\[
L=\operatorname{im}\bigl(H^2(Y_p,\mathbb Z)\oplus H^2(Y_m,\mathbb Z)\to
H^2(S,\mathbb Z)\bigr)=U(2),\qquad r=2.
\]

Cette égalité est formulée pour une couture très générale. Sur un diviseur de
Noether–Lefschetz, \(\operatorname{NS}(S)\) peut sauter et le sous-type doit être
recalculé.

Pour le lissage de Hodge \((h^{1,1},h^{2,1})=(5,85)\), la formule de
Clemens–Schmid adaptée aux dégénérescences de Tyurin donne

\[
\widehat u=20-r=18,\qquad
\widehat v=85-\widehat u-1=66,\qquad
b_3=172.
\]

D'où

\[
\begin{array}{c|cccc|c}
&\operatorname{Gr}^3_F&\operatorname{Gr}^2_F&\operatorname{Gr}^1_F&\operatorname{Gr}^0_F&\dim\\
\hline
\operatorname{Gr}^W_4&1&18&1&0&20\\
\operatorname{Gr}^W_3&0&66&66&0&132\\
\operatorname{Gr}^W_2&0&1&18&1&20
\end{array}
\]

La monodromie est unipotente, non triviale, et

\[
N^2=0,\qquad\operatorname{rang}N=20,\qquad
\operatorname{Jordan}(T_{\rm mon})=J_2(1)^{20}\oplus J_1(1)^{132}.
\]

Dans la convention où l'indice de \(\mathrm{II}_b\) est la dimension de la
partie \((1,1)\) active,

\[
\boxed{\mathrm{LMHS}_{\mathbb Q/\mathbb C}=\mathrm{II}_{18}.}
\]

La polarisation vient de la variation de Hodge polarisée de la famille
projective sur \(\Delta^*\), et non de la seule matrice abstraite construite en
R61.

### Réserve intégrale obligatoire

Le complément orthogonal de \(L=U(2)\) dans le réseau K3 est

\[
T(S)\simeq U\oplus U(2)\oplus E_8(-1)^{\oplus2}.
\]

Le morphisme canonique de réseaux gradués
\(T(S)\to\Lambda_{K3}/L\) a bien

\[
\operatorname{SNF}=(1^{18},2,2),\qquad\operatorname{coker}\simeq(\mathbb Z/2)^2.
\]

Mais r61_resolved_tyurin_lmhs_audit.py construit une matrice symplectique
compatible ; il ne calcule pas le transport parallèle des cycles ni la
matrice de Gauss–Manin de la famille. La phrase publiable est donc :

> The canonical K3 graded lattice map has elementary divisors
> \((1^{18},2,2)\).

Il ne faut pas encore écrire :

> We directly computed the full integral Gauss–Manin monodromy matrix.

## 12. Conséquences pour l'idée \(R\) et la tour

R63 sauve un support géométrique précis pour la suite du programme :

- le paramètre complexe de lissage \(t=pm\) est primitif ;
- le voisinage de la couture possède le modèle \(uv=t\) ;
- les deux normales de la K3 sont triviales ;
- la limite possède une LMHS rationnelle de type \(\mathrm{II}_{18}\) et un secteur actif de rang 20.

Ces faits rendent naturelle l'étude d'un long col autour de \(S\). Ils ne
définissent toutefois pas encore un rayon physique. Le changement
\(t\mapsto c\,t\) montre déjà que \(-\log|t|\) ne devient une longueur qu'après
choix et normalisation d'une métrique Ricci-plate, du volume total et des
unités fondamentales.

La formulation autorisée est donc :

> La famille fournit un candidat géométrique contrôlé pour une limite de col
> de type II et pour l'étude d'une tour dans la théorie parentale.

Les formulations non autorisées restent :

- \(R=8.2\,\mu{\rm m}\), ou toute autre valeur numérique non dérivée ;
- \(m_n=n/R\) sans analyse spectrale de la métrique ;
- existence/stabilité d'une infinité d'états D3-BPS pour ce modèle précis ;
- survie automatique de la tour dans un orientifold O3/O7.

Le stop-test de R62 demeure limité au mécanisme holomorphe diagonal O3/O7
testé. Il ne réfute ni la dégénérescence de Tyurin parentale ni toute tour
possible dans un autre cadre.

## 13. Originalité et statut de dépôt

La recherche bibliographique ciblée n'a trouvé aucun article indexé décrivant
le modèle exact POLY944/sigma5 avec les 28 cônes relatifs, cette résolution,
ce support de Cox et ces certificats. Cette absence de résultat n'est pas une
preuve de nouveauté : POLY944 et sigma5 sont des noms locaux et les mêmes
données peuvent être publiées dans une autre base.

Les éléments généraux ne sont pas nouveaux isolément : construction par tops,
K3 double de \(\mathbb P^1\times\mathbb P^1\) branchée en \((4,4)\),
polarisation \(U(2)\), dégénérescence \(\mathrm{II}_{18}\), tubes de Tyurin
et difficultés orientifold. En particulier, Braun–Cicoli–Milioli–Valandro
relient déjà en 2026 une limite de Tyurin à une dimension interne longue dans
un scénario ADD/Dark Dimension avec stabilisation. L'idée générale
« Tyurin donne une dimension micrométrique » ne peut donc pas porter
l'originalité de DDF.

La contribution potentiellement défendable est la combinaison spécifique :

- modèle résolu POLY944 explicite et fan relatif complètement certifié ;
- fermeture quasi-Fano par deux preuves ;
- réseau de restriction primitif \(U(2)\) et LMHS rationnelle précise ;
- classification bornée des caractères diagonaux de Cox de l'ansatz ;
- obstruction de signature, sous les hypothèses O3/O7 déclarées.

R63 passe la porte mathématique, mais **ne constitue pas encore un dossier de
dépôt complet**. Il manque notamment le manuscrit intégré, un manifeste de
données unique chargé par tous les scripts, une comparaison d'antériorité par
invariants intrinsèques, et la correction éditoriale R61–R63. Une soumission
immédiate serait donc prématurée, même si le noyau de théorème est désormais
solide.

## 14. Prochaine porte scientifique après R63

La suite rationnelle n'est pas le plan de Fano. Elle est une porte analytique/métrique :

1. définir un invariant métrique \(R(t)\) — longueur du col, diamètre ou inverse de la première valeur propre pertinente — dans une normalisation physique explicite ;
2. obtenir l'asymptotique de la métrique Ricci-plate près de \(uv=t\) ;
3. calculer l'échelle du spectre de Laplace et la comparer au secteur de périodes/charges de rang 20 ;
4. distinguer une tour KK, une tour D3-BPS et une tour d'oscillateurs d'une éventuelle corde émergente ;
5. seulement ensuite injecter \(M_{\rm Pl}\), \(M_s\), \(g_s\), le volume et confronter une échelle micrométrique à la littérature et aux contraintes.

Le plan de Fano reste réservé à une phase ultérieure, quand cette interface
géométrie–métrique sera stabilisée.

## 15. Reproductibilité

Commande principale :

~~~bash
python3 r63_strict_tyurin_gate.py
~~~

Contrôles séparés :

~~~bash
python3 r61_resolved_tyurin_lmhs_audit.py
python3 r62_stable_fan_parity_stop_audit.py
python3 r63_independent_lattice_fan.py
python3 r63_independent_jacobian_snc.py
python3 meta_audit_r63/r63_toric_independent_audit.py
python3 meta_audit_r63/r63_quasifano_certificate.py
python3 meta_audit_r63/r63_ems_cohomology_audit.py
~~~

Les sorties de R61 et R62 sont reproduites octet par octet. Le manifeste
R63_MANIFEST.sha256 fixe les versions des pièces du dossier.

## 16. Références principales

1. C. F. Doran, A. Harder, A. Y. Thompson,
   [Mirror symmetry, Tyurin degenerations and fibrations on Calabi–Yau manifolds](https://arxiv.org/abs/1601.08110),
   en particulier §2.1 pour les définitions et §5 pour la LMHS.
2. C. F. Doran, A. Thompson,
   [The Mirror Clemens–Schmid Sequence](https://arxiv.org/abs/2109.04849),
   définitions 1.4–1.5 et §6.1.2.
3. D. Eisenbud, M. Mustaţă, M. Stillman,
   [Cohomology on Toric Varieties and Local Cohomology with Monomial Supports](https://arxiv.org/abs/math/0001159),
   J. Symbolic Comput. 29 (2000), 583–600.
4. S.-Y. Jow,
   [Cohomology of Toric Line Bundles via Simplicial Alexander Duality](https://arxiv.org/abs/1006.0780).
5. S. Hu,
   [Semi-Stable Degeneration of Toric Varieties and Their Hypersurfaces](https://arxiv.org/abs/math/0110091).
6. C. Candelas, A. Font,
   [Duality Between the Webs of Heterotic and Type II Vacua](https://arxiv.org/abs/hep-th/9603170),
   pour le contexte historique des tops toriques.
7. P. Candelas, A. Constantin, H. Skarke,
   [An Abundance of K3 Fibrations from Polyhedra with Interchangeable Parts](https://arxiv.org/abs/1207.4792).
8. B. Hassfeld, J. Monnee, T. Weigand, M. Wiesner,
   [Emergent Strings in Type IIB Calabi–Yau Compactifications](https://arxiv.org/abs/2504.01066),
   pour le contexte physique récent des limites de type II ; ce travail ne
   remplace pas un calcul de tour pour le présent modèle.
9. A. P. Braun, M. Cicoli, R. Milioli, R. Valandro,
   [Moduli Stabilisation for ADD and the Dark Dimension Scenario](https://arxiv.org/abs/2606.19440),
   pour une réalisation 2026 de géométries anisotropes et l'interprétation
   d'une limite de Tyurin comme cycle interne long.

## 17. Décision finale R63

~~~text
R62_TORIC_CORE_REPRODUCED = YES
GENERIC_TOTAL_SPACE_AND_CENTRAL_SNC = YES
K3_SEAM = YES
H_HIGHER_O_YP_YM = ZERO_BY_TWO_METHODS
DHT_QUASI_FANO_COMPONENTS = YES
STRICT_TYURIN_DEGENERATION = YES
NORMAL_BUNDLES = O_S_AND_O_S
SATURATED_LOG_SMOOTH_AND_D_SEMISTABLE = YES
RANK_RESTRICTION = 2_FOR_VERY_GENERAL_SEAM
RATIONAL_LMHS = TYPE_II_18
FULL_INTEGRAL_GAUSS_MANIN_SNF = OPEN
METRIC_R_OF_T = OPEN
MICROMETRIC_VALUE = NOT_DERIVED
PHYSICAL_INFINITE_TOWER = NOT_DERIVED
FANO_PLANE = DEFERRED
~~~

La théorie n'est donc pas « sauvée en bloc ». Le noyau géométrique précis
forme désormais un théorème candidat nettement plus fort : une dégénérescence
de Tyurin torique explicite, stricte et log-lisse, avec LMHS rationnelle
\(\mathrm{II}_{18}\). Il doit encore être transformé en manuscrit et soumis à
un contrôle d'originalité intrinsèque. La prochaine difficulté scientifique
réelle est l'interface entre ce théorème algébrique et une longueur/spectre
physique, et non une nouvelle modification combinatoire du fan.

