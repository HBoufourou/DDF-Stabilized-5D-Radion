# R64 — Pré-rapport adversarial sur le seuil de substance de l’Article 1

**Date :** 4 septembre 2026  
**Rôle :** rapporteur volontairement hostile  
**Corpus examiné :** `R62_REPORT.md`, `R63_REPORT.md`,
`R63_CLAIM_LEDGER.csv`, les audits contradictoires de `meta_audit_r63/`,
`DDF_R1_R62_AUDIT_MAITRE.md` et `DDF_APRES_R62_FEUILLE_DE_ROUTE.md`.

## 1. Verdict exécutif

```text
CORRECTION_MATHEMATIQUE_DU_NOYAU_R63 = PLAUSIBLEMENT_PASS
SUBSTANCE_NOUVELLE_DE_L_ARTICLE_1_ACTUEL = FAIL
ORIGINALITE_INTRINSEQUE_DU_MODELE = OPEN
ARTICLE_1_PRET_A_SOUMETTRE = NO_GO
R64_COMME_PROGRAMME_DE_RECUPERATION = GO
```

Le résultat R63 est nettement meilleur que les anciens articles DDF : il
décrit une famille torique précise, donne des hypothèses de généricité, ferme
les annulations quasi-Fano et corrige la suraffirmation sur la monodromie
intégrale. Je ne vois pas, dans le corpus inspecté, de contradiction fatale
dans la preuve courte des cohomologies ni dans la déduction Tyurin au sens de
Doran–Harder–Thompson.

Cela ne suffit cependant pas à franchir le motif exact de la décision arXiv :
**originalité ou substance insuffisante**. Sous sa forme actuelle, le résultat
principal est un exemple explicite très contrôlé d’un schéma de construction
déjà connu. Les deux calculs des cohomologies augmentent la fiabilité ; ils ne
créent pas deux résultats scientifiques. La couture `(4,4)`, la polarisation
`U(2)`, l’étiquette rationnelle `II_18`, les dégénérescences semistables par
tops et l’idée générale d’une tour aux limites de Tyurin sont déjà dans une
littérature dense.

Le seuil publiable peut néanmoins être atteint sans abandonner le modèle. Il
faut que R64 produise **au moins un résultat invariant et non formel** parmi :

1. un théorème intégral de monodromie/nearby cycles réellement appliqué à la
   famille, avec la vraie matrice de Gauss–Manin ou une identification
   canonique équivalente ;
2. une classification complète d’une classe non triviale de dégénérescences,
   quotientée par isomorphisme de réseau, dont POLY944 n’est qu’un cas ;
3. un théorème équivariant global concernant toutes les involutions compatibles
   d’une classe définie, et non les seuls signes diagonaux de Cox.

Sans l’un de ces trois blocs, le dossier R63 doit être conservé comme exemple,
dataset ou annexe reproductible d’un futur article physique, mais je
recommanderais le rejet d’un Article 1 autonome.

## 2. Le test brutal de substance

Un rapporteur peut appliquer le contre-test suivant :

> Si l’on supprime les noms locaux `POLY944`, `sigma5`, les listes de cônes et
> les sorties `PASS`, quel énoncé conceptuel nouveau reste-t-il ?

À la fin de R63, les énoncés généraux restants sont essentiellement :

- une hypersurface anticanonique dans une famille torique semistable donne une
  fibre centrale SNC sous les hypothèses de lissité usuelles ;
- si `K_V+Y ~ -T` et si `V,T` sont toriques complets connexes, deux suites
  exactes et la dualité de Serre donnent `H^{>0}(Y,O_Y)=0` ;
- une K3 double de `P1 x P1` branchée en `(4,4)` est très généralement
  `U(2)`-polarisée ;
- le rang de la polarisation de couture détermine le sous-type rationnel de la
  LMHS de type II ;
- l’orthogonal invariant d’un réseau hyperbolique contenant la direction
  positive est négatif défini ;
- l’anti-invariant d’une involution symplectique de Nikulin est `E8(-2)`.

Toutes ces phrases sont des applications assez directes de résultats connus.
Le travail de R63 est utile et peut être exact, mais sa difficulté de calcul ne
doit pas être confondue avec un apport conceptuel. Un grand tableau de cônes et
un programme de contrôle ne deviennent un article que s’ils produisent une
classification, un invariant nouveau, un contre-exemple ou une conséquence
qui n’était pas prévisible avant le calcul.

## 3. Ce qui paraît standard, connu ou trop formel

| Bloc R63 | Appréciation hostile | Pourquoi cela ne suffit pas seul |
|---|---|---|
| 28 cônes unimodulaires, complétion à 48 cônes, support de 69 monômes | Certificat utile d’un exemple | Les tops courts fournissent déjà un procédé constructif de dégénérescences semistables de CY3 et une lecture combinatoire de la fibre centrale. |
| Fibre centrale réduite SNC à deux composantes | Attendu après le choix du fan et la non-dégénérescence | Davis et al. prouvent précisément la réduction/SNC pour les hypersurfaces non dégénérées associées aux tops courts lisses. |
| Fermeture quasi-Fano | Correcte mais formelle | La preuve par `K_V+Y ~ -T`, annulation torique, Serre et deux suites exactes tient en un lemme général court. Le certificat EMS est une réplication, pas une seconde découverte. |
| Normales individuellement triviales | Propriété propre à la présentation fibrée, mais élémentaire | Une fibre réduite d’un morphisme vers `P1` a normale triviale ; la restriction transverse à `Y_j` donne le résultat sur `S`. |
| Log-lissité saturée | Nécessaire à la correction, peu distinctive | Une famille semistable à cartes `uv=t` a la carte saturée `N -> N^2`, `1 -> (1,1)`. |
| K3 double `(4,4)` et `NS=U(2)` très générale | Standard | La famille des doubles couvertures de `P1 x P1` ramifiées en `(4,4)` est un modèle classique de K3 `U(2)`-polarisées. |
| LMHS rationnelle `II_18` | Conséquence informative, mais pas encore un nouvel invariant | Une fois `r=2` et `(h11,h21)=(5,85)` admis, les dimensions annoncées suivent des formules générales de Clemens–Schmid/type `II_b`. |
| SNF `(1^18,2,2)` du morphisme gradué K3 | Lemme de réseau, pas encore monodromie | R63 reconnaît correctement qu’il ne s’agit pas de la vraie matrice intégrale de Gauss–Manin sur `H^3`. |
| Scan de 512 signes | Exhaustif seulement dans un petit ansatz | Après quotient de jauge, il ne reste que huit actions effectives sur la couture. Cela ne classifie pas les permutations de rayons, automorphismes non toriques ni toutes les involutions globales du CY. |
| No-go de signature | Potentiellement utile, mais presque une corollaire | La branche préservée repose sur l’indice de Hodge ; la branche échangée sur le réseau anti-invariant de Nikulin. Il faut une portée globale réellement nouvelle pour dépasser une observation d’une page. |
| Discussion de `R` et de la tour | Motivation seulement | Aucun opérateur métrique, vide stabilisé, indice BPS ni spectre n’est calculé pour POLY944. |

### Sources primaires qui élèvent la barre

- R. Davis et al., *Short Tops and Semistable Degenerations*,
  [arXiv:1307.6514](https://arxiv.org/abs/1307.6514), Théorème 2.2,
  Corollaire 2.4 et Proposition 5.1 : construction combinatoire de familles
  semistables de CY3 à partir de tops courts lisses.
- C. Doran, A. Harder, A. Thompson, *Mirror symmetry, Tyurin degenerations
  and fibrations on Calabi–Yau manifolds*,
  [arXiv:1601.08110](https://arxiv.org/abs/1601.08110) : convention
  quasi-Fano/Tyurin employée par R63.
- C. Doran, J. Kostiuk, F. You, *The Doran–Harder–Thompson Conjecture for
  toric complete intersections*,
  [arXiv:1910.11955](https://arxiv.org/abs/1910.11955) : dégénérescences de
  Tyurin de complètes intersections toriques issues de raffinements de
  partitions nef et recollement des invariants fonctionnels/périodes.
- C. Doran, B. Pioline, T. Schimannek, *Enumerative geometry and modularity
  in two-modulus K3-fibered Calabi–Yau threefolds*,
  [arXiv:2408.02994](https://arxiv.org/abs/2408.02994) : familles explicites,
  géométrie énumérative et modularité autour de dégénérescences de Tyurin.
- B. Hassfeld, J. Monnee, T. Weigand, M. Wiesner, *Emergent Strings in Type
  IIB Calabi–Yau Compactifications*,
  [arXiv:2504.01066](https://arxiv.org/abs/2504.01066) : traitement général
  des limites Tyurin `II_b`, corde critique émergente et tours BPS dans le
  parent `N=2`.
- M. Enríquez Rojo, E. Plauschinn, *Swampland conjectures for type IIB
  orientifolds with closed-string U(1)s*,
  [arXiv:2002.04050](https://arxiv.org/abs/2002.04050) : séparation déjà
  connue entre cycles pairs chargés/massless et cycles impairs massifs/non
  chargés, ainsi que le problème de stabilité des tours après projection
  O3/O7.
- L. Kaufmann, J. Monnee, T. Weigand, M. Wiesner, *Quantum obstructions for
  N=1 infinite distance limits*, parties I et II,
  [arXiv:2603.12315](https://arxiv.org/abs/2603.12315) et
  [arXiv:2603.13470](https://arxiv.org/abs/2603.13470) : les obstructions
  `N=1` modernes doivent être comparées au no-go de parité, sans les
  confondre.
- A. P. Braun, M. Cicoli, R. Milioli, R. Valandro, *Moduli Stabilisation for
  ADD and the Dark Dimension Scenario*,
  [arXiv:2606.19440](https://arxiv.org/abs/2606.19440) : la combinaison
  générale « limite de Tyurin + direction interne longue + échelle
  micrométrique » ne peut plus être revendiquée comme idée originale de DDF.

## 4. Faiblesses techniques qu’un vrai rapporteur attaquera

Ces points ne signifient pas nécessairement que R63 est faux. Ils indiquent
où une preuve de manuscrit doit être plus forte que le rapport interne.

### 4.1 Le modèle doit être identifié intrinsèquement

`POLY944` et `sigma5` sont des étiquettes de travail. Elles ne permettent ni
de reconnaître un antécédent ni de garantir qu’un changement de base n’a pas
déjà produit la même famille. Le manuscrit doit donner :

- sommets primitifs dans une convention fixée ;
- forme normale ou identifiant Kreuzer–Skarke/PALP vérifiable ;
- matrice de charges, triangulation/phase et idéal SR ;
- critère explicite d’isomorphisme `GL(4,Z)` plus permutation ;
- identification intrinsèque de l’action appelée `sigma5`.

Sans cela, « aucun article trouvé pour POLY944 » n’est pas une recherche
d’antériorité recevable.

### 4.2 « Très général » doit porter sur la bonne famille

Pour conclure `NS(S)=U(2)`, il ne suffit pas de citer la famille complète des
doubles couvertures `(4,4)`. Il faut montrer que la restriction des
coefficients de `sigma5` domine bien l’espace de modules pertinent, ou au
minimum qu’elle n’est pas contenue dans un diviseur de Noether–Lefschetz. Un
témoin numérique lisse ne prouve pas ce point de généricité de Picard.

### 4.3 La LMHS rationnelle doit être dérivée, pas seulement dimensionnée

Le tableau `(20,132,20)` est compatible avec `II_18`, mais un manuscrit doit
présenter le complexe de poids, les morphismes restriction/Gysin, les noyaux
et cokernels et la polarisation. Un comptage de dimensions suivi d’une
matrice symplectique compatible ne calcule pas la monodromie de la famille.

### 4.4 Le no-go O3/O7 accumule des hypothèses physiques

Le corollaire R62 suppose notamment :

- une involution holomorphe globale compatible avec le lissage ;
- la préservation de `L` sous la forme requise ;
- une classe de tube propre et un état propre de parité ;
- l’appartenance de la classe active à `L^perp` ;
- l’isotropie de la classe ;
- l’identification du vecteur fermé avec le secteur pair de `C4`.

L’article de Hassfeld et al. considère des courbes de self-intersection
**non négative**, et la stabilité/multi-enroulement sont une question
supplémentaire. Exclure les vecteurs isotropes pairs n’exclut donc pas, sans
argument additionnel, toute tour possible de leur mécanisme ni toute tour
`N=1`. Le résultat sûr est un no-go pour **le sous-mécanisme isotrope défini**.

### 4.5 Le scan de signes et le théorème de réseau ne couvrent pas le même univers

Le scan est concret mais limité aux caractères diagonaux de Cox. L’argument
de signature est plus général, mais seulement conditionnel. Les combiner pour
écrire « classification exhaustive de toutes les involutions » serait
incorrect. Il faut choisir :

- soit classifier exactement une classe finie d’automorphismes du fan et
  annoncer cette classe ;
- soit prouver un théorème abstrait pour toute involution satisfaisant des
  hypothèses intrinsèques, sans citer `512` comme preuve de généralité.

### 4.6 Le manuscrit risque de tomber entre deux disciplines

- Pour un article de géométrie algébrique, les paragraphes sur le micron, les
  D3 et la matière sombre ne remplacent pas un théorème nouveau.
- Pour un article de physique des hautes énergies, une famille CY `N=2` et un
  no-go conditionnel sur la couture ne forment pas encore une compactification
  `N=1` cohérente : il manque lieux fixes globaux, charges O7/O3, branes,
  tadpoles, flux et contrôle du régime.

L’Article 1 doit choisir une identité éditoriale. La route la plus proche de
l’état actuel est un article mathématique/algorithmique étroit.

## 5. Formulations dangereuses et remplacements autorisés

| Formulation dangereuse | Objection du rapporteur | Formulation défendable à ce stade |
|---|---|---|
| « une dégénérescence de Tyurin stricte » sans définition | `strict` n’est pas ici une nouvelle notion normalisée | « une dégénérescence de Tyurin au sens de Doran–Harder–Thompson » |
| « première construction » ou « nouveau modèle » | aucune comparaison intrinsèque complète | « pour cette présentation explicite ; l’antériorité intrinsèque reste à vérifier » |
| « nous calculons la monodromie intégrale » | seule une matrice compatible/un morphisme gradué K3 est calculé | « nous calculons la LMHS rationnelle et un morphisme de réseaux gradués associé » |
| « la monodromie a SNF `(1^18,2,2)` » | pas de transport parallèle ni d’identification de `N` sur `H^3` | ne rien affirmer sur la SNF intégrale de Gauss–Manin avant R64 |
| « scan exhaustif des involutions » | seulement signes diagonaux, pas permutations/non-toriques | « scan exhaustif des caractères diagonaux de signes dans l’ansatz Cox déclaré » |
| « obstruction O3/O7 » sans qualificatif | ressemble aux obstructions déjà publiées et peut être interprété universellement | « obstruction de parité au tube isotrope fermé `C4`, sous les hypothèses H1–H6 » |
| « aucune tour ne survit » | faux hors du sous-mécanisme ; une tour KK neutre n’est pas testée | « aucun vecteur isotrope actif pair non nul n’existe dans le secteur testé » |
| « `II_18` implique une tour BPS » | Hassfeld et al. comportent encore des arguments/conjectures sur les indices ; le modèle n’est pas calculé | « la géométrie satisfait la classe limite où un mécanisme de tour a été proposé » |
| « Tyurin explique une dimension micrométrique » | déjà discuté explicitement en 2026 ; aucune métrique de POLY944 | « cette possibilité motive une étude métrique ultérieure » |
| « `R` est relié à `t` » | aucun choix de métrique/volume/unités | « `t` est le paramètre algébrique ; `R(t)` est ouvert » |
| « deux preuves indépendantes établissent la nouveauté » | indépendance de vérification, pas d’idée | « une preuve et un certificat indépendant établissent la robustesse » |
| « validé par plusieurs IA/CAS » | aucun jugement de nouveauté ni expertise externe | donner les calculs, versions, hypothèses et tests ; ne pas utiliser l’outil comme autorité |

## 6. Seuil exact de substance : trois portes alternatives

R64 ne doit pas exiger les trois routes. Une seule peut suffire, mais elle doit
passer **toutes** ses sous-conditions.

### Porte M — monodromie intégrale géométrique (route recommandée)

Cette porte est la plus proche de la lacune reconnue par R63 et produit une
différence réelle entre information rationnelle et intégrale.

`M = PASS` seulement si :

1. une base ou un réseau intégral de `H^3(Y_t,Z)/tors` est relié à la famille
   par cycles proches, transport parallèle ou modèle topologique explicite ;
2. l’opérateur géométrique `N=log(T_mon)` est obtenu de la famille, non choisi
   a posteriori pour avoir les bons rangs ;
3. `ker N`, `im N`, leur saturation et les cokernels sont calculés ;
4. la forme d’intersection est respectée et les extensions intégrales du
   complexe de poids sont traitées ;
5. la SNF annoncée est celle de cet opérateur réel, avec un test indépendant ;
6. un énoncé général explique quand le discriminant de `L` contrôle — ou ne
   contrôle pas — la torsion de la monodromie ;
7. la différence avec les résultats intégraux déjà connus est explicitement
   identifiée.

Un simple changement de nom de la matrice R61, ou la répétition du calcul du
complément orthogonal de `U(2)`, vaut `M = FAIL`.

### Porte C — classification torique non triviale

`C = PASS` seulement si :

1. l’univers fini ou algorithmique classifié est défini avant le scan ;
2. l’équivalence par `GL(n,Z)`, permutation et changement de phase est
   quotientée exactement ;
3. la complétude de l’énumération est démontrée, pas seulement supposée parce
   qu’un fichier a été parcouru ;
4. pour chaque classe, les conditions lisse/projectif/SNC/quasi-Fano/normales
   et le rang de restriction sont décidées par un critère prouvé ;
5. la sortie contient plus qu’un exemplaire renommé : elle distingue au moins
   deux comportements intrinsèques, ou établit un théorème d’unicité/non-
   existence ;
6. les résultats ne sont pas déjà une table ou un corollaire immédiat de
   Davis et al. ou d’une base publique ;
7. POLY944 apparaît comme application d’un résultat de classe, non comme
   définition de la classe.

Une recherche par le mot `POLY944`, ou l’énumération des 28 cônes d’un seul
fan, vaut `C = FAIL`.

### Porte E — théorème équivariant global

`E = PASS` seulement si :

1. la classe des dégénérescences équivariantes et les hypothèses physiques
   sont définies intrinsèquement ;
2. l’action sur l’espace total, la base, les composantes, la couture, le
   paramètre de lissage et `H^3` est construite ou contrôlée ;
3. les cas « composantes préservées » et « composantes échangées » sont tous
   traités, y compris les automorphismes de fan par permutations ;
4. le morphisme tube est rendu équivariant et sa parité est prouvée, pas
   seulement postulée localement par `d log u` ;
5. la nécessité de l’isotropie et de l’appartenance à `L^perp` est démontrée
   pour le mécanisme visé ;
6. le théorème dépasse les résultats généraux déjà connus sur la stabilité des
   D3 en orientifold et les obstructions quantiques `N=1` ;
7. une famille ou une classification non triviale illustre le théorème.

Le seul indice de Hodge appliqué à une involution hypothétique, même correct,
vaut `E = FAIL` pour la substance d’un article autonome.

## 7. Porte binaire GO/NO-GO pour l’Article 1

Définissons :

```text
B0 = noyau R63 présenté par des preuves humaines complètes
B1 = identité intrinsèque du modèle et comparaison GL/KS achevées
B2 = recherche d'antériorité claim-par-claim achevée
B3 = au moins une des portes M, C, E vaut PASS
B4 = manuscrit rattaché à une discipline et à une contribution centrale
B5 = toutes les affirmations ouvertes retirées du résumé, du titre et de la conclusion
B6 = code/données reproduits depuis un manifeste unique et archive propre
B7 = lecture contradictoire par au moins un spécialiste humain du domaine
```

La règle recommandée est :

```text
ARTICLE_1_GO = B0 and B1 and B2 and B3 and B4 and B5 and B6 and B7
```

Il n’y a pas de score compensatoire : vingt sorties numériques ne compensent
pas `B3 = FAIL`, et une idée physiquement séduisante ne compense pas
`B0 = FAIL`.

### État au début de R64

| Porte | État | Commentaire |
|---|:---:|---|
| B0 | PASS conditionnel | Le noyau R63 paraît cohérent, mais doit être réécrit comme preuve de manuscrit et non comme journal d’audit. |
| B1 | OPEN | Noms locaux, pas encore de comparaison intrinsèque exhaustive. |
| B2 | OPEN | Recherche bibliographique ciblée utile, mais pas de matrice d’équivalence des données intrinsèques. |
| B3 | **FAIL** | Aucune monodromie intégrale réelle, classification de classe ou équivariance globale n’est encore terminée. |
| B4 | FAIL/OPEN | Le projet mélange encore article mathématique et promesse de physique micrométrique. |
| B5 | PASS si le registre R63 est respecté | `R`, tour physique et Fano sont correctement marqués ouverts/différés. |
| B6 | PASS partiel | Bon niveau de reproductibilité, mais plusieurs données critiques restent dupliquées dans des scripts. |
| B7 | FAIL | Aucun rapport de spécialiste humain externe n’est présent dans le corpus. |

Conclusion objective :

```text
ARTICLE_1_GO_AU_DEBUT_DE_R64 = FALSE
```

## 8. Stratégie R64 que je recommanderais malgré mon rôle hostile

### 8.1 Priorité 1 : tenter la porte M avec un kill-test rapide

Avant de produire davantage de scans, écrire le complexe intégral exact des
cycles proches pour `Y_p union_S Y_m` et identifier où interviennent
`L=U(2)`, son discriminant et les éventuelles extensions. Le test fatal est
simple :

- si l’on ne peut relier canoniquement ce complexe à `H^3(Y_t,Z)` et à
  `T_mon`, arrêter toute phrase sur la SNF ;
- si le résultat se réduit à la seule arithmétique abstraite de `U(2)`, sans
  information nouvelle sur la famille, il ne passe pas la porte M ;
- s’il fournit la vraie saturation de `im N`, un cokernel intégral non
  trivial et une formule généralisable, il devient le meilleur cœur de
  l’Article 1.

### 8.2 Priorité 2 : construire l’identifiant intrinsèque

Cette étape est obligatoire même si M passe. Elle doit produire un certificat
machine d’isomorphisme/non-isomorphisme, pas seulement une table de Hodge. Un
résultat mathématique sur un exemple impossible à reconnaître est
invérifiable et difficile à citer.

### 8.3 Repli : transformer le no-go en porte E, ou le rétrograder

Si la monodromie intégrale n’aboutit pas, tenter de rendre le no-go réellement
global. Si l’extension des involutions et l’équivariance du tube ne peuvent
être prouvées, garder le scan de 512 signes comme appendice calculatoire et ne
pas le vendre comme résultat principal.

### 8.4 Ne pas lancer encore le calcul métrique lourd dans cet Article 1

La dérivation de `R(t)` est scientifiquement centrale pour DDF, mais elle
constitue un autre article et une autre pile technique. Mélanger une première
approximation de métrique au dossier géométrique affaiblirait les deux. R64
doit d’abord décider si le noyau géométrique est publiable ; R65 peut valider
le pipeline spectral, puis R66–R68 traiter la géométrie et la stabilisation.

## 9. Décision qu’un rapporteur hostile rendrait aujourd’hui

> **Reject in the present form, encourage resubmission only after a major
> conceptual extension.** The manuscript appears to provide a careful and
> reproducible verification of one explicit toric Tyurin degeneration. Most
> structural ingredients — semistability from tops, the `(4,4)` K3 seam,
> `U(2)` polarization, rational type `II_18`, and the lattice-signature
> observation — are standard or direct consequences of known results. The
> integral Gauss–Manin monodromy is not computed, the involution scan is
> exhaustive only within a Cox-diagonal ansatz, and no physical radius or
> stable tower follows. A publishable revision should add either a genuine
> integral monodromy theorem, a complete classification over a nontrivial
> class, or a global equivariant no-go with demonstrably new scope.

Cette conclusion n’est pas « la théorie est fausse ». Elle fixe exactement
la différence entre **un exemple correct** et **un article substantiel**.
R63 fournit l’exemple correct. La tâche de R64 est de produire le résultat qui
le dépasse.


