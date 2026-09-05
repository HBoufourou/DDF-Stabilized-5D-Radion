# R64 — Audit d’antériorité intrinsèque et de nouveauté

**Date de l’audit :** 4 septembre 2026  
**Objet :** distinguer ce qui est déjà théorique, ce qui possède une collision
d’invariants, et ce qui pourrait rester propre au modèle reconstruit en R63.  
**Règle de méthode :** les noms locaux `POLY944`, `sigma5`, `R63` et `DDF`
ne sont jamais utilisés comme critères d’identité bibliographique.

## 1. Verdict exécutif

```text
BROAD_TYURIN_NOVELTY             = FAIL
TORIC_QUASI_FANO_NOVELTY         = FAIL
K3_(4,4)_U(2)_NOVELTY            = FAIL
TYPE_II_TOWER_ARCHITECTURE       = STRONG_PRIOR_ART
EXACT_RELATIVE_MODEL_NOVELTY     = OPEN
RESOLVED_POLYTOPE_NOVELTY        = FAIL_KREUZER_SKARKE_NF1
16_ODP_DATABASE_CORRECTION       = OPEN_AND_POTENTIALLY_ORIGINAL
GLOBAL_ORIENTIFOLD_NO_GO         = OPEN_AND_NOT_YET_PROVED
ARTICLE_READY_ON_NOVELTY         = NO
RECOVERY_ROUTE                   = NARROW_COMPUTATIONAL_GEOMETRY_PAPER
```

La théorie n’est pas « perdue », mais elle doit être décomposée. L’idée
générale

\[
\text{top/partition nef}\longrightarrow
Y_+\cup_S Y_-\longrightarrow
\text{limite de Tyurin}\longrightarrow
\text{direction longue/tour}
\]

possède une antériorité directe et substantielle. La couture K3 double de
\(\mathbf P^1\times\mathbf P^1\) ramifiée en \((4,4)\), sa polarisation
générique \(U(2)\), le critère de \(d\)-semistabilité et l’arithmétique
élémentaire de \(U(2)\) ne peuvent pas porter une revendication de nouveauté.

Le polytope résolu lui-même est désormais identifié exactement dans la base
Kreuzer–Skarke : il est équivalent à la première des deux formes normales de
l’empreinte \(M:104\ 14,\ N:10\ 8,\ H:5,85\). Il n’est donc pas nouveau.
En revanche, aucune source identifiée dans cet audit ne reproduit encore le
**paquet intrinsèque complet** de R63 : phase, éventail
relatif à deux composantes, paire de quasi-Fano, morphisme de restriction,
et correction des seize nœuds de l’entrée de base de données. Cette absence
de collision n’est pas une preuve de nouveauté : elle définit un test exact à
terminer.

L’antériorité la plus proche est Braun–Cicoli–Milioli–Valandro (2026). Leur
famille possède elle aussi une équation de base de forme
\(z=\zeta_a\zeta_b\), une fibre centrale à deux composantes et une couture
qui est une K3 double de \(\mathbf P^1\times\mathbf P^1\) ramifiée en
\((4,4)\). Leur trois-fold lisse a toutefois
\((h^{1,1},h^{2,1})=(4,98)\), et non \((5,85)\). C’est donc une collision
d’architecture très forte, pas encore une identification du modèle.

## 2. Empreinte intrinsèque employée pour la recherche

La recherche a été menée sur les invariants suivants, et non sur les noms
internes du projet.

### 2.1 Fibre lisse résolue

- hypersurface anticanonique torique de dimension trois ;
- \((h^{1,1},h^{2,1})=(5,85)\), \(\chi=-160\) ;
- polytope ambiant réflexif de dimension quatre avec neuf rayons de fan ;
- dix points réticulaires dans le polytope, dont huit sommets ;
- polytope polaire à quatorze sommets et 104 points réticulaires ;
- sommets de l’enveloppe convexe :

\[
\begin{split}
&(-2,0,-1,0),\ (-2,0,0,-1),\ (-1,-1,0,0),\ (0,0,0,1),\\
&(0,0,1,0),\ (0,1,0,0),\ (1,0,0,0),\ (1,1,0,0).
\end{split}
\]

Le rayon additionnel \(E=(1,1,0,0)\) est introduit par une subdivision étoilée
crépante destinée à résoudre seize nœuds ordinaires forcés par l’action de
base. L’objet de départ correspond localement à l’enregistrement CQSV
`polyid=944`, triangulation `0`, étiquette `1509`, et à `KSID=947`, avec
\((h^{1,1},h^{2,1})=(4,100)\). Ces identifiants servent à remonter la
provenance.

La recherche exacte dans la base officielle Kreuzer–Skarke avec les filtres
\(h^{1,1}=5\), \(h^{2,1}=85\), \(V=14\), \(M=104\) et \(N=10\)
retourne deux formes normales avec en-tête
`M:104 14 N:10 8 H:5,85 [-160]`. Le polytope R63 est équivalent à la
**première**, et non à la seconde. Dans la convention où les sommets R63 sont
des vecteurs-colonnes, les quatorze sommets de \(M\) sont

\[
\begin{split}
\{&(-1,0,-1,-1),(-1,0,-1,3),(-1,0,3,-1),(-1,0,3,3),\\
&(-1,2,-1,-1),(-1,2,-1,3),(-1,2,3,-1),(-1,2,3,3),\\
&(0,-1,-1,-1),(0,-1,-1,1),(0,-1,1,-1),(0,-1,1,1),\\
&(1,-1,-1,-1),(1,0,-1,-1)\}.
\end{split}
\]

Une matrice unimodulaire témoin est

\[
U=\begin{pmatrix}
-1&-1&0&-1\\
 2& 1&0& 1\\
 1& 0&0& 1\\
 2& 0&1& 1
\end{pmatrix},\qquad \det U=-1.
\]

Elle envoie exactement les quatorze sommets du polytope \(M\) de R63 sur les
quatorze colonnes de cette première forme normale. La requête reproductible
est : [base Kreuzer–Skarke, filtre exact](https://quark.itp.tuwien.ac.at/cgi-bin/cy/cydata.cgi?h11=5&V=14&M=104&N=10&h12=85&L=100).
Pour rendre le certificat indépendant de l’ordre d’affichage futur de la
base, NF1 est la matrice \(4\times14\) suivante, lue par colonnes :

\[
\begin{pmatrix}
1&0&0&0&2&2&2&-2&2&-2&0&-4&-4&0\\
0&1&0&0&-2&-2&-3&1&-3&1&-1&3&3&-1\\
0&0&1&1&-1&-1&-2&2&-2&2&-2&2&2&-2\\
0&0&0&2&-2&0&-4&0&0&4&-4&4&0&0
\end{pmatrix}.
\]

### 2.2 Dégénérescence relative

- éventail relatif de dimension cinq : onze rayons, vingt-huit cônes
  maximaux, rang de Gale six ;
- deux composantes toriques ambiantes ayant respectivement
  \((8,16,\rho=4)\) et \((9,20,\rho=5)\) pour
  (rayons, cônes maximaux, rang de Picard) ;
- ambiant de couture : \((6,8,\rho=3)\) ;
- fibre centrale \(Y_+\cup_S Y_-\), avec
  \(h^\bullet(Y_\pm,\mathcal O)=(1,0,0,0)\) ;
- \(S\in|-K_{Y_+}|\cap|-K_{Y_-}|\),
  \(N_{S/Y_+}\simeq N_{S/Y_-}\simeq\mathcal O_S\) ;
- \(S\) double de \(\mathbf P^1\times\mathbf P^1\), ramifiée en \((4,4)\),
  avec réseau de restriction générique proposé \(L=U(2)\) ;
- LMHS rationnelle proposée de type \(\mathrm{II}_{18}\).

Une antériorité exacte doit retrouver cet ensemble, à isomorphisme
\(GL(4,\mathbf Z)\), changement de phase et isomorphisme de la famille près.
Une égalité de nombres de Hodge ne suffit jamais.

## 3. Matrice « claim / source / portée »

| Claim envisagé pour DDF | Source primaire la plus proche | Ce que la source établit | Conséquence de nouveauté |
|---|---|---|---|
| Une partition nef à deux parties produit une dégénérescence de Tyurin d’une hypersurface anticanonique torique | Doran–Harder–Thompson, [arXiv:1601.08110](https://arxiv.org/abs/1601.08110), [doi:10.1090/pspum/096/01655](https://doi.org/10.1090/pspum/096/01655), notamment Cor. 3.5 | Dans leur cadre, une partition nef à deux termes d’un polytope réflexif 4D fournit une dégénérescence de Tyurin de l’hypersurface anticanonique générale et une fibration K3 miroir | **Connu.** Ne pas revendiquer le mécanisme général |
| Un top court/lisse donne une famille torique semistable et une hypersurface CY semistable | Davis et al., [arXiv:1307.6514](https://arxiv.org/abs/1307.6514), [doi:10.1080/10586458.2014.910848](https://doi.org/10.1080/10586458.2014.910848) | Construction combinatoire de dégénérescences semistables à partir de short tops sous des hypothèses précises | **Connu.** R63 peut être un exemple certifié, pas le principe |
| Une partition semistable d’un polytope torique induit une dégénérescence de la variété et de ses hypersurfaces transverses | Hu, [arXiv:math/0110091](https://arxiv.org/abs/math/0110091), [doi:10.4310/CAG.2006.v14.n1.a3](https://doi.org/10.4310/CAG.2006.v14.n1.a3) | Construction de familles toriques semistables ; restriction aux hypersurfaces transverses ; cas CY à deux composantes avec couture anticanonique | **Connu.** Antériorité du squelette torique/logarithmique |
| Des composantes toriques servent de blocs quasi-Fano et se recollent le long d’un CY anticanonique | Doran–Kostiuk–You, [arXiv:1910.11955](https://arxiv.org/abs/1910.11955), [doi:10.1016/j.aim.2023.108893](https://doi.org/10.1016/j.aim.2023.108893) | Raffinement de partitions nef, dégénérescences de Tyurin de complètes intersections toriques, blocs quasi-Fano et identités de recollement | **Connu dans un cadre large.** Le petit lemme cohomologique R63 est une vérification d’hypothèses |
| Les projecting tops sont des blocs géométriques toriques contrôlés par une K3 | Braun, [arXiv:1602.03521](https://arxiv.org/abs/1602.03521), [doi:10.1007/JHEP10(2017)083](https://doi.org/10.1007/JHEP10(2017)083) | Architecture de blocs issus de tops, surtout pour la construction de \(G_2\) | **Antériorité architecturale**, même si la cible physique diffère |
| Le critère de double croisement est \(N_{S/Y_+}\otimes N_{S/Y_-}\simeq\mathcal O_S\) | Friedman, *Ann. Math.* 118 (1983), [doi:10.2307/2006955](https://doi.org/10.2307/2006955) | Identification de \(T^1\) et condition de \(d\)-semistabilité | **Connu.** Les normales individuellement triviales peuvent être une donnée spéciale de l’exemple |
| Toute variété \(d\)-semistable ainsi obtenue est automatiquement lissable | Kawamata–Namikawa, *Invent. Math.* 118 (1994), [doi:10.1007/BF01231538](https://doi.org/10.1007/BF01231538) | Théorèmes de lissage logarithmique avec hypothèses globales, projectives/kählériennes et cohomologiques | **Claim interdit.** Dans R63, la famille explicite doit porter l’existence du lissage |
| La K3 double de \(\mathbf P^1\times\mathbf P^1\) branchée en \((4,4)\) a génériquement \(NS=U(2)\) | Bhargava–Ho–Kumar, [arXiv:1312.0898](https://arxiv.org/abs/1312.0898), [doi:10.1017/fms.2016.12](https://doi.org/10.1017/fms.2016.12), §3.2 et Table 1 ; voir aussi Laza–O’Grady, [arXiv:1801.04845](https://arxiv.org/abs/1801.04845), [doi:10.1016/j.aim.2021.107680](https://doi.org/10.1016/j.aim.2021.107680) | Identification de la famille modulaire \(U(2)\)-polarisée ; modèle géométrique des doubles \((4,4)\) | **Connu.** R63 doit encore prouver que sa sous-famille n’est pas contenue dans un diviseur de Noether–Lefschetz |
| La famille \(U(2)\)-polarisée est de dimension 18 et réalisée par ces doubles | Garbagnati–Salgado, [arXiv:2505.15159v2](https://arxiv.org/abs/2505.15159), [doi:10.1017/fms.2025.10149](https://doi.org/10.1017/fms.2025.10149), Prop. 3.6 | Identification explicite de la famille \(U(2)\)-polarisée | **Connu.** Utiliser la version corrigée v2/publiée |
| \(O(U(2))=\{\pm I,\pm J\}\) et les seuls rayons isotropes primitifs sont ceux des deux générateurs | Calcul élémentaire, avec le formalisme de discriminant de Nikulin, [doi:10.1070/IM1980v014n01ABEH001060](https://doi.org/10.1070/IM1980v014n01ABEH001060) | Pour la matrice \(\bigl(\begin{smallmatrix}0&2\\2&0\end{smallmatrix}\bigr)\), \((ae+bf)^2=4ab\), puis résolution directe des isométries entières | **Lemme dérivé**, pas découverte structurante ; fournir la preuve au lieu de l’attribuer à tort à un article |
| Une K3 très générale avec \(NS=U(2)\) a seulement l’identité et l’involution de revêtement | Nikulin (formes discriminantes et Torelli) ; Galluzzi–Lombardo–Peters, [arXiv:0804.0725](https://arxiv.org/abs/0804.0725), comme contexte de rang 2 | Le résultat demandé n’apparaît pas tel quel dans la source de rang 2 ; il se déduit du cône positif, du recollement discriminant, de Torelli et de la généricité de la structure de Hodge | **Lemme propre à démontrer.** Ne pas le présenter comme citation textuelle |
| Une involution symplectique non triviale sur une K3 très générale \(U(2)\) est impossible | van Geemen–Sarti, [arXiv:math/0602015](https://arxiv.org/abs/math/0602015), [doi:10.1007/s00209-006-0047-6](https://doi.org/10.1007/s00209-006-0047-6) | Le réseau coinvariant d’une involution de Nikulin est \(E_8(-2)\) ; le cas projectif impose donc un rang de Picard bien supérieur à 2 | **Connu.** Attention : cela ne vise pas l’identité sur la couture |
| L’involution de revêtement du double \((4,4)\) est 2-élémentaire de type \((r,a,\delta)=(2,2,0)\), avec une courbe fixe de genre 9 | Nikulin–Saito, [arXiv:math/0312396](https://arxiv.org/abs/math/0312396), [doi:10.1112/S0024611505015212](https://doi.org/10.1112/S0024611505015212), à compléter par la classification complexe de Nikulin | Classification des involutions non symplectiques 2-élémentaires ; ici le lieu fixe est la ramification \((4,4)\), de genre 9 | **Connu.** Donnée utile pour classifier la branche O-type B |
| Les parités O3/O7 satisfont \(\sigma^*J=J\), \(\sigma^*\Omega_3=-\Omega_3\), avec décomposition paire/impaire des champs | Grimm–Louis, [arXiv:hep-th/0403067](https://arxiv.org/abs/hep-th/0403067), [doi:10.1016/j.nuclphysb.2004.08.005](https://doi.org/10.1016/j.nuclphysb.2004.08.005) | Action effective des orientifolds CY O3/O7 et parités cohomologiques | **Connu.** Ne classe pas à lui seul les actions sur une dégénérescence de Tyurin |
| Les deux possibilités pertinentes sont O-type A (double surface dans l’O7, composantes échangées) et O-type B (double surface non contenue, graphe préservé) | Kaufmann–Monnee–Weigand–Wiesner I, [arXiv:2603.12315](https://arxiv.org/abs/2603.12315), [doi:10.1103/blb9-hrwd](https://doi.org/10.1103/blb9-hrwd), et II, [arXiv:2603.13470](https://arxiv.org/abs/2603.13470), [doi:10.1103/ypyx-mg6r](https://doi.org/10.1103/ypyx-mg6r) | Classification et obstructions quantiques/kählériennes modernes des limites \(\mathcal N=1\) issues de Tyurin | **Antériorité directe du message physique général.** L’application exacte au modèle R63 reste possible |
| Une classe isotrope de la couture suffit à caractériser toutes les tours parentales | Hassfeld–Monnee–Weigand–Wiesner, [arXiv:2504.01066v3](https://arxiv.org/abs/2504.01066), [doi:10.1007/JHEP01(2026)140](https://doi.org/10.1007/JHEP01(2026)140) | Les cycles considérés proviennent de classes \(C_0\) dans le réseau transverse avec \(C_0^2\ge0\) ; le cas isotrope est seulement le sous-cas de genre 1. Plusieurs énoncés de tour sont formulés comme arguments suggestifs/conjecture | **R62 doit être corrigé.** L’absence d’isotropes ne suffit pas ; un secteur négatif défini exclurait en revanche tous les \(C^2\ge0\) |
| Une direction micrométrique issue d’une grande base K3 et une limite de Tyurin constituent une idée propre à DDF | Braun–Cicoli–Milioli–Valandro, [arXiv:2606.19440](https://arxiv.org/abs/2606.19440) | Modèle explicite K3-fibré, grande direction effective, limite de Tyurin ; famille centrale \(z=\zeta_a\zeta_b\) et couture double \((4,4)\) | **Échec de nouveauté architecturale.** Leur \((4,98)\) diffère toutefois du \((5,85)\) R63 |
| Le polytope/hypersurface résolu de R63 est nouveau parce qu’il a \((5,85)\) | Kreuzer–Skarke, [arXiv:hep-th/0002240](https://arxiv.org/abs/hep-th/0002240), [doi:10.4310/ATMP.2000.v4.n6.a2](https://doi.org/10.4310/ATMP.2000.v4.n6.a2) ; base de géométries Altman et al., [arXiv:1411.1418](https://arxiv.org/abs/1411.1418), [doi:10.1007/JHEP02(2015)158](https://doi.org/10.1007/JHEP02(2015)158) | Classification complète des polytopes réflexifs 4D ; la recherche exacte donne deux NF et la matrice \(U\) ci-dessus identifie R63 à NF1 | **Réfuté exactement.** Le polytope est connu ; seule une phase, une involution, une correction ou une famille relative additionnelle peut être nouvelle |
| Aucun autre CY torique \((5,85)\) n’existe dans la littérature | Klemm–Kreuzer–Riegler–Scheidegger, [arXiv:hep-th/0410018](https://arxiv.org/abs/hep-th/0410018), [doi:10.1088/1126-6708/2005/05/023](https://doi.org/10.1088/1126-6708/2005/05/023) ; He–Lee–Lukas–Sun, [arXiv:1309.0223](https://arxiv.org/abs/1309.0223), [doi:10.1007/JHEP06(2014)077](https://doi.org/10.1007/JHEP06(2014)077) | Plusieurs modèles K3-fibrés/toriques avec \((5,85)\), \(\chi=-160\), dont \(\widetilde X_{12},\widetilde X_{13}\) | **Collision hodgienne certaine.** Les cardinalités réticulaires excluent toutefois l’équivalence de leurs polytopes avec R63 |
| L’entrée source et son involution n’ont jamais été étudiées | Cao–Gao–Gao, [arXiv:2407.02565](https://arxiv.org/abs/2407.02565), [doi:10.1007/JHEP10(2024)188](https://doi.org/10.1007/JHEP10(2024)188) ; Altman–Carifio–Gao–Nelson, [arXiv:2111.03078](https://arxiv.org/abs/2111.03078), [doi:10.1007/JHEP03(2022)087](https://doi.org/10.1007/JHEP03(2022)087) | Bases de données d’orientifolds toriques et enregistrements sources dont provient le cas de travail | **La provenance est connue.** La correction géométrique des seize ODP et la nouvelle phase peuvent rester originales |

## 4. Antériorité des constructions de Tyurin : ce qui reste réellement à R63

Les résultats de Hu, Davis et al., Doran–Harder–Thompson et
Doran–Kostiuk–You couvrent déjà le passage conceptuel d’une décomposition
torique/partition nef à une famille semistable dont la fibre centrale est
formée de quasi-Fano collés le long d’un diviseur anticanonique commun. Gross,
[arXiv:math/0406171](https://arxiv.org/abs/math/0406171),
[doi:10.1007/s00208-005-0686-7](https://doi.org/10.1007/s00208-005-0686-7),
fournit en plus le contexte général des dégénérescences toriques et de la
dualité de Batyrev–Borisov.

La preuve R63

\[
K_V+Y\sim-T,
\qquad
0\to\mathcal O_V(-T)\to\mathcal O_V\to\mathcal O_T\to0,
\]

suivie de l’annulation torique et de la dualité de Serre est correcte comme
**lemme de vérification** de la quasi-Fano-ité. Elle ne constitue pas une
nouvelle théorie des quasi-Fano. Le second calcul EMS renforce la
reproductibilité ; il ne double pas la substance scientifique.

Ce qui peut rester propre au modèle est donc :

1. la présence forcée de seize ODP dans l’objet de base de données sous
   l’action choisie ;
2. leur résolution crépante simultanée par le rayon \(E=(1,1,0,0)\) ;
3. le fan relatif exact et projectif qui prolonge cette résolution ;
4. le couple exact de trois-folds quasi-Fano et son morphisme de restriction
   intégral vers \(NS(S)\) ;
5. une éventuelle propriété intégrale inattendue de la monodromie ou de
   l’action équivariante.

Ce paquet doit être comparé à isomorphisme, pas seulement à mots-clés.

## 5. K3 \((4,4)\), automorphismes et classes isotropes

Pour

\[
U(2)=\mathbf Ze\oplus\mathbf Zf,
\qquad e^2=f^2=0,
\qquad e\cdot f=2,
\]

on a \((ae+bf)^2=4ab\). Les vecteurs primitifs isotropes non nuls sont donc
\(\pm e\) et \(\pm f\). Une résolution directe de
\(A^T\bigl(\begin{smallmatrix}0&2\\2&0\end{smallmatrix}\bigr)A=
\bigl(\begin{smallmatrix}0&2\\2&0\end{smallmatrix}\bigr)\) donne

\[
O(U(2))=\{I,-I,J,-J\},
\qquad J(e)=f,\quad J(f)=e.
\]

Ce calcul est utile, mais il concerne le **réseau algébrique de
polarisation**. Il ne faut pas identifier ces deux rayons isotropes aux
classes qui construisent les 3-cycles de la tour de Hassfeld et al. Pour une
K3 très générale de polarisation \(U(2)\), le réseau transverse est

\[
T(S)\simeq U\oplus U(2)\oplus E_8(-1)^{\oplus2},
\qquad \operatorname{sign}T(S)=(2,18),
\]

et contient de nombreuses classes de carré non négatif. Ainsi :

- l’arithmétique de \(O(U(2))\) aide à classifier l’action sur les classes
  algébriques et le cône ample ;
- elle ne prouve ni l’existence ni l’absence de la tour parentale ;
- la revendication \(NS(S)=U(2)\) exige que la famille de coutures réalisée
  par les coefficients R63 ne soit pas confinée à un lieu de
  Noether–Lefschetz ;
- l’assertion
  \(\operatorname{Aut}(S_{\rm très\ générale})=\{1,\iota_{\rm deck}\}\)
  doit être démontrée dans le texte par Torelli et recollement discriminant,
  non simplement citée.

## 6. Orientifold : collision directe et correction de la branche échangée

Les articles de Kaufmann et al. de 2026 sont une antériorité directe pour
l’idée générale qu’une projection \(\mathcal N=1\) peut obstruer la tour
parentale d’une limite de Tyurin. Les étiquettes O-type A/B et leurs effets ne
doivent donc pas être présentés comme nouveaux.

Une correction logique est indispensable. Si les deux composantes sont
échangées, l’O-type A peut fixer la couture \(S\) **point par point** : l’O7
contient alors toute la double surface. La restriction à \(S\) est l’identité,
pas une involution symplectique non triviale de Nikulin. L’argument
« coinvariant \(E_8(-2)\), donc \(\rho\ge9\) » ne s’applique qu’à une action
symplectique non triviale sur la couture. Il ne suffit pas à exclure O-type A.

Le no-go de R62 peut éventuellement être sauvé sous une forme plus précise :

> le sous-réseau réellement actif après projection, identifié par la tube map
> intégrale équivariante, est négatif défini ; il ne contient donc aucun
> vecteur non nul de carré \(\ge0\) et ne peut porter la tour fermée \(C_4\)
> chargée du mécanisme parent étudié.

Mais cette phrase n’est pas encore un théorème du modèle. Il manque :

1. une involution du **total espace relatif**, et non seulement neuf signes
   sur les coordonnées de la couture ;
2. son action sur \(p,m,t\), sur la 3-forme holomorphe et sur l’orientation du
   cercle évanescent ;
3. une rétraction de Clemens équivariante et la formule intégrale
   \(\sigma_*\operatorname{Tub}(C)=\eta\operatorname{Tub}(\sigma_*C)\) ;
4. le traitement des cosets discriminants, car \(U(2)\) n’est pas
   unimodulaire ;
5. le lieu fixe global, les charges O3/O7 et la compatibilité du lissage ;
6. l’examen de toutes les classes \(C^2\ge0\), et pas seulement \(C^2=0\).

Même après cette preuve, la formulation doit rester limitée. Enríquez
Rojo–Plauschinn,
[arXiv:2002.04050](https://arxiv.org/abs/2002.04050),
[doi:10.1007/JHEP07(2020)026](https://doi.org/10.1007/JHEP07(2020)026),
montre que les D3 enveloppées ne préservent généralement pas la même
supersymétrie que l’orientifold O3/O7. Le résultat géométrique n’exclurait ni
une tour KK neutre liée à \(R\), ni toute tour non fermée, ni les limites avec
co-scaling des modules de Kähler.

## 7. Collisions intrinsèques et quasi-collisions

### 7.1 Collision d’architecture : certaine

Braun–Cicoli–Milioli–Valandro,
[arXiv:2606.19440](https://arxiv.org/abs/2606.19440), réalisent déjà les
caractéristiques suivantes :

- trois-fold Calabi–Yau K3-fibré ;
- grande direction effective et motivation micrométrique ;
- limite de Tyurin à deux composantes ;
- coordonnée de base factorisée \(z=\zeta_a\zeta_b\) ;
- couture K3 donnée par un double revêtement de
  \(\mathbf P^1\times\mathbf P^1\) ramifié en \((4,4)\).

La différence \((4,98)\) contre \((5,85)\) empêche l’isomorphisme des fibres
lisses. R63 peut donc fournir un **autre exemple**, mais pas revendiquer
l’idée de cette architecture.

La séparation est également exacte au niveau Kreuzer–Skarke. Les rayons de
l’équation (115) de Braun et al. donnent
\(M:129\ 8,\ N:10\ 8,\ H:4,98\) et sont équivalents à la troisième des
quatre formes normales retournées par le
[filtre KS correspondant](https://quark.itp.tuwien.ac.at/cgi-bin/cy/cydata.cgi?h11=4&V=8&M=129&N=10&h12=98&L=20).
Le même modèle est identifié dans leur texte comme le polytope \(\#1206\) de
la base d’Altman et al.
R63 a \(M:104\ 14,\ N:10\ 8,\ H:5,85\). L’égalité grossière
\(N:10\ 8\) et la même géométrie de couture ne peuvent donc masquer
l’inéquivalence des polytopes.

### 7.2 Collision de nombres de Hodge, mais non de polytope : certaine

Klemm–Kreuzer–Riegler–Scheidegger et He–Lee–Lukas–Sun contiennent déjà des
trois-folds toriques/K3-fibrés de nombres de Hodge \((5,85)\) et
\(\chi=-160\). Le calcul direct depuis les rayons de la Table 7 de He et al.
donne :

| Modèle | points/sommets de \(N\) | points/sommets de \(M\) |
|---|---:|---:|
| R63 | 10 / 8 | 104 / 14 |
| \(\widetilde X_{12}\) | 9 / 6 | 105 / 8 |
| \(\widetilde X_{13}\) | 9 / 7 | 105 / 10 |

Ces cardinalités sont invariantes sous \(GL(4,\mathbf Z)\) : aucun des deux
polytopes n’est donc équivalent au polytope R63. Les quotients \(X_{12}\) et
\(X_{13}\), de nombres de Hodge \((4,44)\), sont également distincts. Cette
comparaison exclut une identité de **présentation torique**, non une éventuelle
relation birationnelle abstraite entre trois-folds.

Le supplément primaire de Klemm et al. identifie ces deux couvertures comme
\(\#12539\), `M:105 8 N:9 6 H:5,85`, et \(\#87874\),
`M:105 10 N:9 7 H:5,85`. Il s’agit des deux profils repris plus tard par He
et al., et non d’une troisième collision indépendante. Voir le
[supplément Kreuzer de hep-th/0410018](https://hep.itp.tuwien.ac.at/~kreuzer/CY/hep-th/0410018/FQEK.cd1.gz).

Le [catalogue Oxford des 7 890 CICY](https://www-thphys.physics.ox.ac.uk/projects/CalabiYau/cicylist/index.html)
dans des produits d’espaces projectifs ne contient par ailleurs aucune entrée
\((5,85)\) : parmi ses entrées de
\(h^{1,1}=5\), aucune n’a \(h^{2,1}=85\). Cette observation n’a de portée que
pour cette liste CICY et ne concerne pas les hypersurfaces toriques générales.

### 7.3 Le polytope est exactement connu ; la famille relative reste ouverte

Le test Kreuzer–Skarke est désormais fermé : le polytope R63 est NF1 parmi
les deux formes normales ayant l’empreinte voulue. La phrase « nouveau
polytope » est définitivement interdite.

Aucune source inspectée n’a en revanche été reconnue comme possédant
simultanément :

\[
\begin{gathered}
(h^{1,1},h^{2,1})=(5,85),\quad
(\#\Delta,\#\operatorname{Vert}\Delta)=(10,8),\quad
(\#\Delta^\circ,\#\operatorname{Vert}\Delta^\circ)=(104,14),\\
\text{la phase résolue par }E=(1,1,0,0),\quad
16\ \mathrm{ODP},\quad
Y_+\cup_S Y_-,\quad NS(S)=U(2),
\end{gathered}
\]

avec les mêmes fans de composantes et le même morphisme de restriction.
Cette observation vaut seulement comme **état de recherche au 4 septembre
2026**. La question encore ouverte est de savoir si la phase, l’involution,
la correction des ODP et la dégénérescence relative ont déjà été publiées
ensemble. Pour exclure une identité du CY abstrait au-delà de la présentation
torique, il faudra en outre comparer la forme cubique intégrale, \(c_2\), le
groupe fondamental et les torsions.

## 8. Matrice de risque de nouveauté

| Bloc potentiel de l’article | Risque d’antériorité | Valeur scientifique possible | Statut R64 |
|---|---:|---:|---|
| Théorème général « tops/partitions nef donnent Tyurin » | Critique | Faible car déjà théorisé | À retirer du titre et du claim principal |
| Lemme quasi-Fano par suites exactes | Critique | Bon certificat d’exemple | Annexe/section de preuve |
| K3 double \((4,4)\), \(NS=U(2)\) | Critique | Donnée de couture utile | Garder comme identification, pas comme nouveauté |
| Classification de \(O(U(2))\) | Élevé | Petit lemme propre et proprement démontrable | Garder brièvement |
| LMHS rationnelle \(\mathrm{II}_{18}\) | Élevé | Utile si le complexe de poids est calculé réellement | Garder conditionnellement |
| Direction longue/Tyurin/micron | Critique depuis arXiv:2606.19440 | Motivation, pas claim | Citer et repositionner |
| Tour parentale à partir de classes K3 | Critique | Application d’un mécanisme récent | Employer « prédite/candidate » |
| No-go orientifold général | Critique depuis arXiv:2603.12315/13470 | Faible sans raffinement | Ne pas revendiquer |
| Corollaire équivariant exact pour R63 | Moyen à élevé | Potentiellement substantiel | Ouvert : tube map globale et réseau intégral manquants |
| Résolution des 16 ODP de l’entrée source | Moyen | Potentiellement forte correction de base de données | Priorité 1 de l’article |
| Polytope résolu seul | Critique | Aucune : il est exactement KS-NF1 | Ne jamais revendiquer sa nouveauté |
| Phase + résolution ODP + fan relatif exact | Moyen | Dataset reproductible et exemple relatif nouveau possible | Priorité 1 |
| Paire de quasi-Fano et morphisme intégral de restriction | Moyen | Plus distinctif que les seuls nombres de Hodge | Priorité 2 |
| Théorème intégral de monodromie/Gauss–Manin | Faible si réellement obtenu | Très forte substance | Priorité de recherche, non encore acquis |

## 9. Tests décisifs à exécuter avant toute revendication « premier »

1. **Publier l’identification déjà obtenue.** Donner NF1, les deux matrices de
   sommets \(\Delta,\Delta^\circ\) et la matrice unimodulaire \(U\). Chercher
   l’identifiant ordinal exact de NF1 si la base en fournit un stable.
2. **Finir les candidats \((5,85)\).** L’équivalence polytope avec
   \(\widetilde X_{12},\widetilde X_{13}\) est exclue par les cardinalités.
   Comparer encore les autres modèles publiés, puis phase/SR, cône de Mori,
   forme cubique et \(c_2\cdot D\).
3. **Comparer la structure relative.** Même si la fibre lisse coïncide, tester
   si le fan 5D, les deux stars, les normales et le morphisme
   \(\operatorname{Pic}(Y_+)\oplus\operatorname{Pic}(Y_-)\to NS(S)\) sont
   isomorphes.
4. **Certifier la correction des ODP.** Produire les seize idéaux locaux, leur
   type analytique, l’action de l’involution, et une preuve que la subdivision
   est crépante et simultanée.
5. **Fermer « très général ».** Calculer le rang du morphisme des coefficients
   R63 vers l’espace des formes \((4,4)\), ou exhiber un argument de monodromie
   montrant que la sous-famille n’est pas Noether–Lefschetz.
6. **Si la physique reste dans l’Article 1.** Construire l’action globale et la
   tube map intégrale équivariante, puis traiter toutes les classes de carré
   non négatif. Sans cela, déplacer l’orientifold et \(R\) dans un article
   ultérieur.

## 10. Formulations sûres et formulations interdites

| Ne pas écrire | Écrire à ce stade |
|---|---|
| « Nous introduisons les dégénérescences de Tyurin toriques issues des tops » | « Nous construisons et certifions un exemple explicite dans les cadres de Hu, Davis et al. et Doran–Harder–Thompson » |
| « La couture \((4,4)\) avec \(U(2)\) est nouvelle » | « La couture est identifiée à une K3 \(U(2)\)-polarisée standard ; son plongement exact dans la paire de blocs est la donnée à comparer » |
| « \(d\)-semistable, donc lissable » | « La famille explicite donne le lissage ; la trivialité de \(T^1\) vérifie la \(d\)-semistabilité » |
| « Aucun autre modèle \((5,85)\) n’existe » | « Plusieurs modèles \((5,85)\) existent ; l’équivalence intrinsèque du nôtre reste en cours de test » |
| « L’absence de classe isotrope élimine la tour » | « Le mécanisme publié autorise \(C^2\ge0\) ; il faut démontrer que tout le sous-réseau survivant est négatif défini » |
| « Toutes les involutions sont classifiées par 512 signes » | « Les caractères diagonaux de Cox de l’ansatz déclaré sont exhaustivement parcourus » |
| « O-type A est impossible car \(\rho=2\) » | « Une action symplectique non triviale sur la couture est exclue à \(\rho=2\), mais O-type A peut agir trivialement sur la couture » |
| « La tour micrométrique est démontrée » | « La géométrie fournit une limite candidate ; ni \(R(t)\), ni le vide stabilisé, ni le spectre stable ne sont encore dérivés » |
| « Première construction » | « À notre connaissance après comparaison intrinsèque [liste explicite des bases et candidats] » — uniquement une fois les tests §9 terminés |

## 11. Recommandation éditoriale

La route la plus solide pour sauver DDF est de faire de l’Article 1 un article
de **géométrie computationnelle étroit**, centré sur une correction et une
construction reproductible :

> Une involution d’une entrée torique répertoriée force seize nœuds ; une
> résolution crépante explicite conduit à un CY \((5,85)\) et s’étend à une
> dégénérescence semistable à deux quasi-Fano dont on calcule le réseau de
> restriction et la LMHS.

Ce claim devient substantiel seulement si l’identification KS/PALP déjà
obtenue est documentée, si la non-collision relative avec les modèles
\((5,85)\) est fermée, et si les invariants topologiques de la phase et la
correction des ODP sont fermés. La « tour », \(R\), l’échelle
micrométrique, les orientifolds et le plan de Fano doivent rester des axes
ultérieurs, sauf si R64 produit la tube map intégrale globale ou un autre
théorème équivariant réellement nouveau.

Le verdict scientifique est donc nuancé mais exploitable :

```text
RECOVER_GEOMETRIC_CORE = YES
RETRACT_BROAD_NOVELTY  = YES
REOPEN_TOWER_PARITY    = YES
EXACT_RELATIVE_MODEL_NOVELTY = OPEN
POLYTOPE_NOVELTY            = FAIL
SUBMISSION_NOW         = NO
```

## 12. Bibliographie primaire minimale

1. S. Hu, *Semi-Stable Degeneration of Toric Varieties and Their
   Hypersurfaces*, [arXiv:math/0110091](https://arxiv.org/abs/math/0110091),
   [doi:10.4310/CAG.2006.v14.n1.a3](https://doi.org/10.4310/CAG.2006.v14.n1.a3).
2. R. Davis et al., *Short Tops and Semistable Degenerations*,
   [arXiv:1307.6514](https://arxiv.org/abs/1307.6514),
   [doi:10.1080/10586458.2014.910848](https://doi.org/10.1080/10586458.2014.910848).
3. C. F. Doran, A. Harder, A. Thompson, *Mirror symmetry, Tyurin
   degenerations and fibrations on Calabi–Yau manifolds*,
   [arXiv:1601.08110](https://arxiv.org/abs/1601.08110),
   [doi:10.1090/pspum/096/01655](https://doi.org/10.1090/pspum/096/01655).
4. C. F. Doran, J. Kostiuk, F. You, *The Doran–Harder–Thompson conjecture
   for toric complete intersections*,
   [arXiv:1910.11955](https://arxiv.org/abs/1910.11955),
   [doi:10.1016/j.aim.2023.108893](https://doi.org/10.1016/j.aim.2023.108893).
5. R. Friedman, *Global smoothings of varieties with normal crossings*,
   [doi:10.2307/2006955](https://doi.org/10.2307/2006955).
6. Y. Kawamata, Y. Namikawa, *Logarithmic deformations of normal crossing
   varieties and smoothing of degenerate Calabi–Yau varieties*,
   [doi:10.1007/BF01231538](https://doi.org/10.1007/BF01231538).
7. M. Bhargava, W. Ho, A. Kumar, *Orbit Parametrizations for K3 Surfaces*,
   [arXiv:1312.0898](https://arxiv.org/abs/1312.0898),
   [doi:10.1017/fms.2016.12](https://doi.org/10.1017/fms.2016.12).
8. R. Laza, K. O’Grady, *GIT versus Baily–Borel compactification for K3’s
   which are double covers of \(\mathbf P^1\times\mathbf P^1\)*,
   [arXiv:1801.04845](https://arxiv.org/abs/1801.04845),
   [doi:10.1016/j.aim.2021.107680](https://doi.org/10.1016/j.aim.2021.107680).
9. V. V. Nikulin, *Integral symmetric bilinear forms and some of their
   applications*,
   [doi:10.1070/IM1980v014n01ABEH001060](https://doi.org/10.1070/IM1980v014n01ABEH001060).
10. B. van Geemen, A. Sarti, *Nikulin involutions on K3 surfaces*,
    [arXiv:math/0602015](https://arxiv.org/abs/math/0602015),
    [doi:10.1007/s00209-006-0047-6](https://doi.org/10.1007/s00209-006-0047-6).
11. T. W. Grimm, J. Louis, *The effective action of N=1 Calabi–Yau
    orientifolds*, [arXiv:hep-th/0403067](https://arxiv.org/abs/hep-th/0403067),
    [doi:10.1016/j.nuclphysb.2004.08.005](https://doi.org/10.1016/j.nuclphysb.2004.08.005).
12. B. Hassfeld et al., *Emergent strings in Type IIB Calabi–Yau
    compactifications*, [arXiv:2504.01066v3](https://arxiv.org/abs/2504.01066),
    [doi:10.1007/JHEP01(2026)140](https://doi.org/10.1007/JHEP01(2026)140).
13. L. Kaufmann et al., *Quantum obstructions for N=1 infinite distance
    limits — Part I*, [arXiv:2603.12315](https://arxiv.org/abs/2603.12315),
    [doi:10.1103/blb9-hrwd](https://doi.org/10.1103/blb9-hrwd).
14. L. Kaufmann et al., *Part II: Kähler obstructions*,
    [arXiv:2603.13470](https://arxiv.org/abs/2603.13470),
    [doi:10.1103/ypyx-mg6r](https://doi.org/10.1103/ypyx-mg6r).
15. A. P. Braun, M. Cicoli, R. Milioli, R. Valandro, *Moduli Stabilisation
    for ADD and the Dark Dimension Scenario*,
    [arXiv:2606.19440](https://arxiv.org/abs/2606.19440).
16. M. Kreuzer, H. Skarke, *Complete classification of reflexive polyhedra
    in four dimensions*, [arXiv:hep-th/0002240](https://arxiv.org/abs/hep-th/0002240),
    [doi:10.4310/ATMP.2000.v4.n6.a2](https://doi.org/10.4310/ATMP.2000.v4.n6.a2).
17. A. Klemm, M. Kreuzer, E. Riegler, E. Scheidegger, *Topological String
    Amplitudes, Complete Intersection Calabi–Yau Spaces and Threshold
    Corrections*, [arXiv:hep-th/0410018](https://arxiv.org/abs/hep-th/0410018),
    [doi:10.1088/1126-6708/2005/05/023](https://doi.org/10.1088/1126-6708/2005/05/023).
18. Y.-H. He, S.-J. Lee, A. Lukas, C. Sun, *Heterotic model building:
    16 special manifolds*, [arXiv:1309.0223](https://arxiv.org/abs/1309.0223),
    [doi:10.1007/JHEP06(2014)077](https://doi.org/10.1007/JHEP06(2014)077).

