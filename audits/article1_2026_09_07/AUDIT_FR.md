# Article 1 : relecture approfondie et corrections du 7 septembre 2026

**Résultat : manuscrit renforcé pour évaluation scientifique, avec T1 intégré. La nouveauté et l'intérêt éditorial ne sont pas certifiés.** Cette relecture a examiné les deux avis reçus, le texte intégral de l'article, ses équations, les sorties de calcul et les travaux proches. Les avis ont été traités comme des propositions à vérifier, jamais comme une autorité.

Le premier avis était globalement favorable, mais « aucune erreur » ne couvre pas les lacunes bibliographiques et de domaine identifiées ici. Le second signalait une omission réelle dans le PDF tout en contenant deux erreurs mathématiques. Les calculs et contrelectures internes assistés par IA ne remplacent pas une expertise externe.

## Corrections effectivement intégrées

| Point | Conclusion de la relecture | Modification du manuscrit |
|---|---|---|
| Secteur nul absent du PDF | La positivité massive seule ne prouvait pas sa complétude. | Section 4 et annexe B : base nulle complète, jonctions, deux courants avec coins, embeddings et quotient. |
| Ancien X₁ de norme négative | La forme −3BI est reproduite ; X₁ viole Israel. L'ancien RED avait été rétracté. | Exclusion par le domaine explicitée sans modifier l'action ni le signe calculé. |
| Poids de bord | Le second avis écrit un signe supplémentaire incorrect. Le poids est ηᵢWᵢ+2λ. | Signe conservé ; preuve analytique de W₀<0<WL ajoutée. |
| Borne cα>1/3 | Cette affirmation vient de l'avis, pas de l'article ; elle est fausse. Par exemple cα(3,20)≈0,282346. | Bornes positives point par point conservées, confusion cα/αr explicitement levée. |
| Annulation du volume de Planck | Correcte, mais trop condensée. | Équations A0a/A0b pour I/L et Nf/(3BL), avec distinction bord/milieu. |
| L<Lflat | Comparaison correcte à même pente centrale. | Égalité des pentes √(2Λ₅) démontrée ; tension compatible séparée. |
| Domaine de courbure | La seule borne h<Λ₅/(6B) ne garantit pas l'événement. | Voisinage régulier/transversal autour de zéro et deux conditions centrales nécessaires explicites. |
| Réponse à la tension | Dérivée exacte au point plat, approximation au detuning fini. | Nature du reste quadratique explicitée ; aucune résolution du problème cosmologique revendiquée. |
| Modes vectoriels | Le comptage pouvait rester implicite. | Élimination de la tour vectorielle indépendante pour p²≠0 et cinq polarisations du tenseur massif décrites. |
| Conventions d'unités | « L=B=1 » était ambigu physiquement. | Coordonnées xμ/L,y/L et scalaire σ/√B définis ; BL³ n'est pas fixé physiquement. |
| Boos et al. | Égalité du warp aux bouts ne signifie pas symétrie de réflexion. | Attribution séparée de Medina–Pontón. |
| Antériorité manquante | Girmohanta et al. 2024 traite précisément rigidité finie, masses, profils et produit spectral. | Référence 23 ajoutée et comparaison des équations et modèles. |
| Monotonie avec rigidité | Olechowski avait déjà démontré le résultat et décrit la reconstruction à fond fixé. | Attribution directe ; retrait de toute présentation comme nouveau principe. |
| Références récentes | [9], [15] et [20] authentifiées. | Métadonnées/initiales harmonisées ; comparaison de [9] avec sa version publiée. |
| Portées en micromètres | L'ancien tableau choisissait arbitrairement R=3 μm. | Colonne remplacée par 1/(mrL), directement calculée ; conversion dimensionnelle définie séparément. |

## Ce qui peut porter la contribution

Le candidat principal est l'évaluation explicite du résidu canonique cα(x,λ̂), avec dépendance complète en rigidité au premier ordre de rétroaction, dans ce potentiel convexe à Λ₅>0 et cette branche symétrique. Ses bornes et le théorème d'événement scalaire spécifique sont les autres résultats à apprécier.

La relation masse/couplage résulte de l'élimination d'ε ; elle ne fournit pas une information indépendante supplémentaire. La révision donne aussi les bornes exactes du coefficient C=π²cα/κ entre π²(coth x−1/x)/(2x) et π²(coth x+1/x)/(2x). Le reste O(ε⁴) demeure dans la relation physique. Cette bande n'est pas annoncée comme une contrainte exacte à amplitude finie.

La [matrice bibliographique](BIBLIOGRAPHIE.md) distingue les précédents, les différences de modèles et ce que la lecture n'a pas identifié. Une formule particulière différente de celles trouvées ne garantit ni priorité ni importance suffisante pour publication.

## Vérifications exécutées

Les quatre calculs du premier article ont été rejoués dans un dossier neuf : 11 602 valeurs numériques comparées aux références, quatre statuts PASS. Les cinq programmes T1 ont également été relancés et passent. Les contrôles indépendants ajoutent 30 intégrales de profils, cinq longueurs avec raffinement, trois réponses de courbure par différences centrales et 30 vérifications des bornes du coefficient. Les précisions numériques sont des diagnostics de calcul et non des erreurs physiques ou expérimentales.

Les rapports sont [le rejeu de l'article](../../verification/ARTICLE1_REPRODUCTION_2026_09_07.json), [T1](../../verification/T1_REPLAY_EXECUTED.json), [les contrôles indépendants](../../verification/article1_review/independent_math_checks.json) et [la contrelecture](CONTRELECTURE.md). Les contrôles d'intégrité ne remplacent pas les solveurs.

## Portée de cette version

L'[article actuel](../../publications/article_1/manuscript.pdf) traite un problème distinct de [l'ancien Article III](DISTINCTION_ARTICLE_III.md), consacré au milieu sombre et à la RAR. Cela ne réhabilite pas les anciennes affirmations galactiques et ne préjuge pas d'une décision éditoriale ou administrative.

Une évaluation externe doit encore apprécier la substantialité de la contribution et la robustesse de ses hypothèses. La stabilité non linéaire ou quantique, les tranches courbes, l'échelle absolue R, la cosmologie et la RAR ne sont pas fermées. Aucun manuscrit n'a été soumis automatiquement à une revue ou à arXiv pendant cette correction.
