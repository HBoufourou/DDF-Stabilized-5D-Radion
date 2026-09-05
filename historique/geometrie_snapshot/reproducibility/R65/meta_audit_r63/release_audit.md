# R63 — Audit indépendant de livraison

**Date :** 4 septembre 2026  
**Périmètre :** résultats R61–R63 relatifs à la famille résolue de
`POLY944`, phase et sous-famille `sigma5` fixées.  
**Fonction de ce document :** décider ce qui peut entrer dans un article,
isoler les réserves et définir le contenu minimal d'un dossier de dépôt
complet. Ce document ne réaudite pas la phénoménologie DDF antérieure.

## 1. Décision de livraison

```text
PORTE_MATHEMATIQUE_R63 = PASS
TYURIN_AU_SENS_DHT = OUI, SOUS GENERICITE EXPLICITE
LMHS_RATIONNELLE_II_18 = OUI, POUR UNE COUTURE TRES GENERALE
MONODROMIE_INTEGRALE_COMPLETE = NON CERTIFIEE
ORIGINALITE_D_UN_ARTICLE_AUTONOME = PLAUSIBLE, NON ETABLIE
DOSSIER_ACTUEL_PRET_POUR_DEPOT_EN_REVUE = NON
R_MICROMETRIQUE_OU_TOUR_PHYSIQUE = NON DERIVEES
```

Le résultat central de R63 résiste au contre-audit. Sous les entrées
géométriques de R62 — projectivité relative, lissité générique de l'espace
total et des strates, fibre centrale réduite SNC — les deux composantes
satisfont

\[
h^\bullet(Y_p,\mathcal O_{Y_p})
=h^\bullet(Y_m,\mathcal O_{Y_m})=(1,0,0,0),
\]

la couture est une K3 anticanonique, et

\[
N_{S/Y_p}\simeq N_{S/Y_m}\simeq\mathcal O_S.
\]

La famille est donc une dégénérescence de Tyurin **au sens de la définition
de Doran–Harder–Thompson**. Le mot interne « stricte » peut servir dans le
registre DDF pour l'opposer à « Tyurin-type », mais le manuscrit doit annoncer
la définition plutôt que suggérer une nouvelle notion.

Cette réussite ferme une porte mathématique ; elle ne suffit pas encore à
faire un dépôt. Il manque un manuscrit intégré, une hiérarchie documentaire
sans verdicts contradictoires, un paquet reproductible durci et une étude
d'antériorité par les données intrinsèques du polytope. R63 doit donc être
gelé comme **résultat validé en préparation d'article**, pas annoncé comme
article déjà prêt.

## 2. Contrôle effectivement réalisé

Les cinq chemins de calcul suivants ont été exécutés avec succès pendant cet
audit :

1. reconstruction exacte indépendante du fan, des degrés et des supports :
   `meta_audit_r63/r63_toric_independent_audit.py` ;
2. seconde reconstruction du réseau/fan et recoupement Qhull :
   `r63_independent_lattice_fan.py` ;
3. contrôle des supports, lieux de base, décompositions locales,
   transversalité et irréductibilité générique :
   `r63_independent_jacobian_snc.py` ;
4. certificat des étoiles, classes, morphismes toriques et normales :
   `meta_audit_r63/r63_quasifano_certificate.py` ;
5. contre-calcul exhaustif EMS/Čech de la cohomologie de
   \(\mathcal O(-Y_\pm)\) :
   `meta_audit_r63/r63_ems_cohomology_audit.py`.

Le calcul cohomologique a deux justifications indépendantes : une preuve
courte par suites exactes et dualité de Serre, puis un contrôle combinatoire
exhaustif des cellules de poids. Le rapport adversarial n'a trouvé ni erreur
de signe dans \(K_V+Y\sim-T\), ni mauvais décalage EMS, ni confusion entre
les quatre-folds ambiants et les trois-folds quasi-Fano.

Il faut néanmoins employer une formulation exacte : il existe deux
**implémentations indépendantes**, plus des contrôles Gröbner avec SymPy et un
recoupement Qhull. Il n'y a pas eu de réplication par SageMath,
Macaulay2 ou Singular autonome dans l'environnement courant.

## 3. Registre concis des affirmations

Légende : **A** = admissible comme résultat d'article ; **A\*** = admissible
avec hypothèse ou citation explicite ; **S** = supplément calculatoire ;
**O** = ouvert ; **X** = à exclure de l'article géométrique.

| ID | Affirmation | Statut | Formulation autorisée et limite |
|---|---|:---:|---|
| R63-C01 | Le fan relatif possède 28 cônes unimodulaires, un support cohérent et une complétion projective lisse à 48 cônes. | A/S | Résultat exact pour les rayons, la phase et les hauteurs publiés ; joindre toutes les données. |
| R63-C02 | La famille anticanonique est projective et semi-stable près de \(t=0\), avec espace total générique lisse et fibre centrale réduite \(Y_p\cup_S Y_m\). | A\* | Dire « pour les coefficients dans un ouvert de Zariski non vide, \(c\ne0\), après restriction à un petit disque ». La preuve est Bertini + jet unité + cartes SNC, pas une saturation jacobienne globale. |
| R63-C03 | \(S\) est une K3 lisse connexe et \(S\in|-K_{Y_p}|\cap|-K_{Y_m}|\). | A\* | Lissité sous généricité ; connexité, \(K_S\simeq\mathcal O_S\) et \(h^1=0\) suivent de la suite anticanonique sur le trois-fold torique. |
| R63-C04 | \(h^\bullet(Y_p,\mathcal O)=h^\bullet(Y_m,\mathcal O)=(1,0,0,0)\). | A | Preuve par \(K_V+Y\sim-T\), acyclicité de \(\mathcal O_V(-T)\), Serre et suite de l'hypersurface ; EMS en contre-vérification. |
| R63-C05 | \(Y_p,Y_m\) sont quasi-Fano et la famille est Tyurin. | A\* | Employer explicitement la convention DHT. Ne pas employer « weak Fano » : \(-K\) est semi-ample/nef mais non gros, avec \((-K)^3=0\). |
| R63-C06 | Le produit des normales est trivial et la fibre est d-semi-stable. | A | \(Y_p+Y_m=\operatorname{div}(t)\) donne un isomorphisme de fibrés, pas seulement \(c_1=0\). |
| R63-C07 | Les deux normales sont individuellement triviales. | A\* | Ajouter les diviseurs principaux \(\operatorname{div}(\chi^{q+s})=D_m-D_5\) et \(\operatorname{div}(\chi^q)=D_6+D_E-D_p\), puis utiliser la transversalité. |
| R63-C08 | Le morphisme est log-lisse saturé et son canonique relatif/log est trivial. | A\* | Écrire les cartes \(t=u,v,uv\), les monoïdes et l'adjonction relative ; ne pas déduire abusivement tout théorème de lissage de la seule d-semistabilité. |
| R63-C09 | Pour une couture très générale, le rang de restriction est \(r=2\) et la polarisation est \(U(2)\). | A\* | Citer ou prouver que la double couverture \((4,4)\) très générale a \(NS(S)=U(2)\), et expliquer la primitivité des classes de fibres. Les loci de Noether–Lefschetz sont exclus. |
| R63-C10 | La LMHS polarisée sur \(\mathbb Q/\mathbb C\) est \(II_{18}\), avec gradins \((20,132,20)\), \(N^2=0\) et \(\operatorname{rang}N=20\). | A\* | Valable pour le membre très général précédent et pour le lissage de Hodge \((5,85)\) ; présenter le complexe de poids/Clemens–Schmid, pas seulement une matrice modèle. |
| R63-C11 | Le morphisme canonique de réseaux gradués K3 a diviseurs élémentaires \((1^{18},2,2)\). | A\* | Admissible comme lemme de réseau associé à \(U(2)\), sous la preuve de l'inclusion intégrale. |
| R63-C12 | La vraie monodromie de Gauss–Manin sur tout \(H^3(Y_t,\mathbb Z)\) a SNF \((1^{18},2,2,0^{152})\). | O | Non démontré. R61 construit une matrice intégrale compatible ; il ne transporte pas une base de cycles de la famille. |
| R63-C13 | Le stop-test O3/O7 exclut le tube fermé dans le modèle. | O hors R63 | R63 n'a pas réaudité toute la branche de parité. Si elle entre plus tard dans l'article, l'énoncé doit rester borné aux caractères diagonaux de Cox et aux six hypothèses de R62. |
| R63-C14 | La construction est nouvelle. | O | Aucun antécédent exact trouvé, mais la méthode des tops, la K3 \((4,4)/U(2)\) et l'étiquette \(II_{18}\) sont standards. Écrire seulement « to our knowledge » après comparaison intrinsèque des sommets, charges et SR. |
| R63-P01 | La géométrie fixe \(R=8{,}2\,\mu\mathrm m\), ou une autre valeur micrométrique. | X | Faux au stade R63 : aucun \(R(t)\), aucune métrique Ricci-plate et aucun mécanisme de stabilisation ne sont calculés. |
| R63-P02 | La fenêtre externe \(1\!-\!30\,\mu\mathrm m\) prédit le rayon DDF. | X | C'est une motivation/contrainte issue d'autres scénarios, pas une sortie du modèle. \(8{,}2\,\mu\mathrm m\) reste un benchmark historique. |
| R63-P03 | \(II_{18}\), une orbite de monodromie ou un tube impliquent une tour KK/BPS stable. | X | Aucun opérateur KK, indice BPS, théorème de non-annulation infinie ni chambre de stabilité n'est fourni. |
| R63-P04 | Le plan de Fano organise déjà sept charges physiques. | X | Aucun réseau physique de sept classes et aucune incidence démontrée ; Fano reste un programme ultérieur. |

## 4. Contradictions documentaires à résoudre

Il n'y a pas de contradiction mathématique fatale entre les rapports, mais
plusieurs verdicts datent d'étapes différentes. Ils deviendraient
contradictoires s'ils étaient livrés sans étiquette chronologique.

1. `toric_recheck.md` et `independent_cas.md` déclarent encore le terme
   Tyurin suspendu parce que leur périmètre n'inclut pas les cohomologies.
   `quasifano_normal_bundles.md`, le script EMS et le rapport adversarial
   ferment ensuite cette lacune. Les deux premiers rapports doivent porter un
   bandeau « audit partiel antérieur à la fermeture quasi-Fano ».
2. La conclusion finale de `corpus_and_gaps.md` conserve par endroits une
   feuille de route écrite avant la fermeture, alors que son verdict initial
   est désormais `GO strict`. Le rapport consolidé R63 doit remplacer ces
   temps verbaux par un état final unique.
3. R61 présente la SNF complète de \(N\) comme exacte. R63 démontre seulement
   la SNF du morphisme canonique de réseau K3 gradué. Cette rétrogradation est
   une errata obligatoire, pas une note facultative.
4. `r63_quasifano_certificate.py` imprime les annulations et le verdict Tyurin
   comme conclusions, mais ne calcule pas ces groupes. La preuve est dans le
   texte et le calcul indépendant dans `r63_ems_cohomology_audit.py`. Renommer
   ces lignes `THEOREM_DEDUCTION` ou `REPORT_CONSEQUENCE`.
5. L'appariement des murs n'est pas, seul, un théorème général de complétude.
   Ici la complétude vient du support/propreté de R62 ; le manuscrit doit
   l'invoquer au bon endroit.
6. Les données `SR_PAIRS` et `REFERENCE_EXPONENT` sont actuellement codées en
   dur dans les nouveaux scripts. Avant livraison, elles doivent être
   recomputées ou contrôlées par assertions contre les cônes et les classes.
7. Ne jamais mélanger `POLY944/(5,85)/sigma5` avec les périodes, flux,
   tadpoles ou triangulations de `POLY925/(4,98)`. Une isomorphie partielle ou
   un même motif Tyurin ne suffit pas à transporter ces données.

## 5. Noyau de théorème publiable

La formulation suivante reflète exactement le niveau de preuve actuel et
peut devenir le théorème principal après intégration des lemmes :

> Fixons la phase résolue et l'éventail relatif explicitement donnés pour le
> modèle `POLY944`, ainsi que la sous-famille anticanonique `sigma5`. Sur
> \(\mathbb C\), pour des coefficients appartenant à un ouvert de Zariski non
> vide avec \(c\ne0\), et après restriction à un voisinage analytique de
> \(t=0\), la famille obtenue est une dégénérescence de Tyurin projective au
> sens de Doran–Harder–Thompson. Sa fibre centrale est
> \(Y_p\cup_S Y_m\), où \(Y_p,Y_m\) sont des trois-folds quasi-Fano lisses,
> \(S\) est une K3 anticanonique lisse, et
> \(N_{S/Y_p}\simeq N_{S/Y_m}\simeq\mathcal O_S\). Pour une couture très
> générale, l'image de restriction a rang deux et la LMHS rationnelle du
> lissage est de type \(II_{18}\), avec dimensions graduées
> \((20,132,20)\).

Ce théorème doit être séparé de trois énoncés éventuels : le lemme intégral de
réseau K3, le no-go équivariant borné de R62 et toute conjecture physique.
Les réunir dans une seule phrase créerait précisément la suraffirmation qui a
fragilisé les articles antérieurs.

## 6. Originalité : verdict de libération

R63 établit la **validité** du noyau géométrique, pas encore son
**originalité substantielle**. Les éléments suivants sont déjà connus dans la
littérature : construction semistable par tops, K3 double de
\(\mathbb P^1\times\mathbb P^1\) ramifiée en \((4,4)\), polarisation
\(U(2)\), limites \(II_b\), mécanisme général de tubes/D3 et taxonomie
orientifold de type A/B.

La nouveauté possible réside dans la combinaison suivante : phase résolue
précise de `POLY944`, éventail relatif complet, image intégrale primitive,
données discriminantes, classification exhaustive **dans l'ansatz diagonal
de Cox déclaré**, puis obstruction de signature sous hypothèses. Aucun
article identique n'a été trouvé par mots-clés, mais les noms `POLY944` et
`sigma5` sont locaux et mal indexés.

Avant d'écrire « first » ou « new », il faut donc comparer le modèle par :

- les sommets du polytope modulo \(GL(4,\mathbb Z)\) et permutation ;
- la matrice de charges, la phase/triangulation et l'idéal SR ;
- les invariants Kreuzer–Skarke et les bases publiques de tops ;
- l'involution comme action intrinsèque, pas seulement son nom `sigma5` ;
- une lecture externe par au moins un spécialiste des dégénérescences
  toriques/K3.

Sans ce contrôle, R63 est un excellent appendice reproductible ou un exemple
explicite ; il n'est pas encore assuré d'être un article autonome répondant
au critère de substance/originalité signalé par la modération arXiv.

## 7. Contenu minimal du dossier complet de dépôt

Le dossier ci-dessous est un **minimum de livraison**, pas un squelette de
manuscrit. Chaque élément doit exister et passer son critère de sortie.

| Bloc | Contenu obligatoire | Critère de sortie |
|---|---|---|
| Article | Source LaTeX complète, PDF compilé, résumé, théorème principal, preuves intégrales, limites et bibliographie. | Aucun argument essentiel ne renvoie seulement à « le script dit PASS » ; toutes les hypothèses de généricité et le sens de Tyurin sont écrits. |
| Annexe torique | Rayons, 28 cônes, charges, SR, support de 69 monômes, complétion de 48 cônes, ambiants quotients \(V_p,V_m,T\), classes de \(Y_p,Y_m,S\). | Les tableaux du PDF sont générés ou comparés automatiquement au manifeste machine. |
| Annexe quasi-Fano/log | Suites exactes complètes, dualité de Serre, preuve K3, normales, d-semistabilité, cartes log et canonique relatif. | Les corrections du rapport adversarial sont intégrées ; les égalités de classes sont écrites comme équivalences/isomorphismes. |
| Annexe LMHS | Calcul du rang de restriction, hypothèse « très général », complexe de poids/Clemens–Schmid, polarisation et séparation rationnel/intégral. | Aucune phrase n'identifie la matrice modèle R61 à la Gauss–Manin intégrale complète. |
| Manifeste de données | Fichier JSON/YAML unique avec identifiant de modèle, sommets, rayons, cônes, phase, charges, involution, support et hashes. | Tous les scripts chargent ou vérifient cette source unique ; aucune donnée critique dupliquée silencieusement. |
| Reproductibilité | `README`, commande `run_all`, versions Python/SymPy/NumPy/SciPy, dépendances figées, sorties brutes R61–R63, SHA-256 et tests. | Exécution propre, code zéro, comparaison automatique des sorties ; assertions critiques actives même si Python est lancé avec `-O`. |
| Validation indépendante | Scripts toriques indépendants, EMS, témoins Gröbner et, idéalement, réplication Sage/Normaliz + Singular/Macaulay2. | Ne pas appeler « second CAS » ce qui est seulement une seconde implémentation dans la même pile. |
| Registre des claims | Version tabulaire du §3, avec source de preuve, portée, dépendances et statut. | Chaque phrase du résumé et de la conclusion a un identifiant admissible `A/A*`. |
| Errata et filiation | Note reliant R61, R62, R63 et l'errata R1–R62 ; bannière sur les audits partiels/supersédés. | La SNF intégrale et les anciennes interprétations physiques ne peuvent pas être citées sans la correction. |
| Antériorité | Tableau claim–source, recherche par données intrinsèques, différences exactes avec Davis et al., DHT, Laza–O'Grady, Hassfeld et al. et les travaux orientifold 2026. | Originalité formulée « to our knowledge » et validée par lecture experte avant soumission. |
| Dépôt revue | Lettre de couverture, déclaration de disponibilité des données/code, contributions, conflits, licence, `CITATION.cff` et archive versionnée. | Cible éditoriale vérifiée ; le dossier ne tente pas de contourner la décision arXiv par une simple resoumission du manuscrit refusé. |

Le dossier courant possède une grande partie des preuves et des programmes,
mais pas encore l'article intégré, le manifeste unique, les sorties R63
figées, le lanceur reproductible, l'errata final ni la comparaison
d'antériorité intrinsèque. C'est la raison précise du `NO` au dépôt immédiat.

## 8. Garde-fous pour \(R\), la tour et Fano

R63 ne demande pas d'abandonner ces trois idées. Il impose de les conserver
dans des branches falsifiables séparées :

- **\(R\)** reste une longueur métrique à dériver d'une métrique, d'un
  opérateur spectral et d'une stabilisation. Le paramètre construit ici est
  \(t\), pas \(R\).
- **Tour KK** : il faut un opérateur physique, des conditions aux limites,
  convergence spectrale et une loi de comptage. Une forme topologique de col
  ne suffit pas.
- **Tour BPS** : il faut une infinité de classes non nulles, un indice ou une
  fonction génératrice, une chambre de stabilité et une loi de masse. La
  monodromie seule ne suffit pas.
- **Plan de Fano** : il peut revenir après l'identification de sept objets
  physiques et de leurs incidences. Il ne doit pas être placé dans le premier
  article géométrique.

La formulation sûre est donc : « R63 fournit un socle géométrique où ces
questions pourront être testées ». Elle ne doit jamais devenir : « R63
prouve une épaisseur micrométrique ou une tour ».

## 9. Verdict final

R63 sauve un résultat mathématique précis et non trivial : une famille
torique explicite qui passe désormais la définition quasi-Fano de Tyurin, avec
normales triviales et LMHS rationnelle \(II_{18}\) pour le membre très
général. Aucun défaut fatal n'a été identifié dans les preuves de
cohomologie, de normales ou dans les calculs toriques indépendants.

La prochaine décision correcte est donc : **geler R63 comme base démontrée,
effectuer la passe d'originalité intrinsèque, puis produire le dossier complet
décrit au §7**. Une valeur micrométrique, une tour KK/BPS et le plan de Fano
restent des objectifs de la série ; ils ne sont pas des résultats de R63.

