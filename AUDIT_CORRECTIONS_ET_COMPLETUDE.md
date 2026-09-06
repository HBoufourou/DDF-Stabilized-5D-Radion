# Correction de files.v3.correction.zip et complétude de la base

6 septembre 2026. « Complet » désigne ici une base cohérente, documentée et reproductible pour les résultats annoncés. Cela ne signifie pas théorie fondamentale achevée ou articles acceptés.

## 1. Ce que contient réellement l'archive

La comparaison exhaustive par empreintes donne 236 fichiers scientifiques hors `.git` et caches : **221 sont identiques à la fusion déjà examinée, 15 sont nouveaux et aucun ancien fichier n'est modifié**. Les nouveautés sont huit scripts, cinq sorties et deux notes. Les répertoires Git reçus ne sont pas utilisés pour le travail ou la publication ; l'archive brute reste sauvegardée localement comme provenance, hors de l'arbre publié.

Deux annonces de la note reçue sont inexactes dans cette archive : la sortie de l'étape 1 n'est pas jointe ; `REGISTRE_UNIFIE.csv` est absent. Les registres présents contiennent bien 18+32=50 revendications. La nouvelle correspondance couvre les 50 IDs, avec six sans équivalent dans le noyau actif, et préserve les anciennes phrases littéralement. Le registre actif à la racine contient maintenant 31 affirmations après les quatre ajouts de cette correction.

## 2. Rejeu des scripts et sens du contrôle

Les six scripts scientifiques exécutables ont été rejoués après lecture, en écrivant leurs sorties dans un emplacement séparé. Le module commun a été utilisé par les deux solveurs ; le lanceur a été lu, mais sa gestion des erreurs est insuffisante pour servir de validation : il peut finir avec un code de succès même si un sous-script échoue. Le nouveau lanceur canonique propage les échecs et compare les observables.

Quatre des cinq sorties reçues sont identiques après normalisation des fins de lignes. L'étape Φ diffère seulement par 7,63×10⁻13 → 7,62×10⁻13 dans un recouvrement impair théoriquement nul sous la réflexion. Leurs masses et les autres chiffres affichés concordent. La sortie manquante de l'étape 1 a été reconstruite : à ε=.53 elle donne mrL=.850124 et αr=.402267 ; à ε=.30 la masse est .483691 et non la valeur de référence .483724 imprimée en commentaire. Reproduire une sortie ne valide pas automatiquement son interprétation physique.

## 3. Corrections intégrées

| Point reçu | Traitement dans la version active |
|---|---|
| « Les termes quadratiques augmentent la masse de 24 % au maximum » | Min–max à fond fixé ; λ̂=20 distingué de la limite rigide. À ε=.3 le gain rigide réel est environ 25,52 %. |
| Couplage et masse toujours croissants ensemble | Faux comme règle universelle. La raideur augmente κ et réduit cα dans le coefficient faible calculé ; l'ordre exact de toutes les amplitudes n'est pas revendiqué. |
| Potentiels affines utilisés pour l'article du noyau quadratique | Manuscrit réécrit avec les bonnes jonctions et les poids de bord. L'affine est une comparaison déclarée. |
| R sélectionné par q posé indépendamment | Sélection à μ,λ,v,Λ5,B fixés ; q devient sortie. Formule plate et solution avec rétroaction distinguées. |
| Logarithme de l'axe R | La branche `log(-sqrt(...))` reçue est complexe. La branche positive physique et sa condition de domaine figurent dans le calcul canonique. |
| Tensions négatives | Valeurs totales Ui, constantes affines Ti et constantes quadratiques τi distinguées ; Ui imprimées dans les données de spectre. |
| Deux limites de Planck confondues | Le Planck non réduit est adapté à H=1,66√g*T²/MPl ; la formule BK utilise le réduit. La cellule de tangle a été corrigée, sans no-go universel. |
| Homogène ⇒ zéro mode seul / tour vide | Projection exacte en modes : excitations paires petites mais non nulles pour masse positive et warp non constant. |
| Forte occupation ⇒ condensat formé | Dégénérescence, relaxation, condensation et superfluidité séparées ; seuil dépendant de la convention de vitesse. |
| Sextique ⇒ MOND automatiquement | La transformée de Legendre impose n≥0. Le sextique répulsif donne la branche X≥0 ; la branche MOND X<0 et son couplage ne sont pas dérivés. |
| Équation d'état relativiste appliquée au potentiel chimique NR | Retirer w=cs²=1/2 ; dans le régime sextique NR cs²=2X/m. |
| Moyenne temporelle nulle ⇒ absence de force | Contre-exemple explicite de réponse locale à une source, contrôlé par intégration temporelle et problème spatial à sources séparées. |
| Poids e⁶ᴬ d'un vertex sextique local | Le volume invariant 5D donne e⁴ᴬ pour tout potentiel local ; les recouvrements quartiques et sextiques ont des dimensions différentes. |
| DR4 ou boost universel annoncés sans calcul | Aucun verdict ajouté ; environnement, géométrie et modèle local restent à calculer. Aucun gel automatique de date n'est créé. |
| Masse 4D du tableau de diffusion nommée mPhi | Champs de données renommés m4D pour distinguer le mode physique 4D de la masse du champ 5D. |

Les détails et preuves sont dans [l'audit du fond](noyau/stabilisation/AUDIT_FOND_STABILITE_R.md), [l'audit matière/RAR](extensions/RAR/AUDIT_MATIERE_RAR.md), [les 15 directions corrigées](extensions/RAR/DIRECTIONS_15_CORRIGEES.md) et [la formule du couplage](noyau/stabilisation/COUPLAGE_QUADRATIQUE_FERME.md).

## 4. Réponse à chaque bloc de la liste « ce qui manque »

| Demande | Résultat ou statut justifié |
|---|---|
| A. Scripts et provenance | Rejeu complet, empreintes, sorties et comparaisons conservés ; scripts actifs remplacent les prototypes fragiles. |
| A. Registre unifié | Un seul registre actif ; correspondance exhaustive des 50 anciens IDs. |
| A. Directions et signes | Table corrigée ; une preuve analytique explicite peut justifier un signe sans script obligatoire. |
| B.1–B.3 Bibliographie et discussions | Vingt références vérifiées ; motivation, précédents, bords négatifs, radiatif et vide traités dans le nouveau manuscrit. Les deux dernières discussions existaient déjà dans l'ancien anglais : un comptage de mots français ne démontrait pas leur absence. |
| B.4 Tableau à R fixé | Douze lignes avec R₀=3 μm explicitement choisi ; masses, couplages, portée et familles affichés, sans verdict expérimental. |
| B.5 Énergies de bord | Valeurs totales et constantes distinctes dans `radion_comparison.json`. |
| B.6 Réponse à l'avis | Réponse point par point reliée aux sections effectivement réécrites. |
| B.7 Endossement | Question d'accès éventuelle à arXiv selon le compte ; pas condition de validité des calculs ni obligation générale de soumission directe à une revue. Aucun endossement demandé ou obtenu. |
| C.1 Bibliographie sombre/UV | Notes existantes et audit renforcé ; la base Φ possède ses références initiales et ses comparaisons à approfondir. Aucun raccord UV promis. |
| C.2 Relique Boltzmann | Non calculée ; retirée des conclusions des manuscrits limités. Protocole de développement explicite. |
| C.3 Porte locale | No-go trop large corrigé ; contre-exemple de réponse calculé. Obstruction globale d'un terme linéaire en phase compacte délimitée. |
| C.4 Homogénéité | Remplacée par le calcul de projection et ses bornes déjà contrôlées. |
| C.5 Halo/observations | 27 configurations et trois intérieurs réguliers disponibles ; raccord global et comparaison SPARC non réalisés. Ils conditionnent un article explicatif RAR, pas l'article du radion. |
| C.6 Yukawa, opérateurs et équivalence | Couplage minimal radion au trace du tenseur dans l'article 1 ; portails Φ et tests d'équivalence restent un modèle distinct à définir. |
| D.1 Courbe expérimentale | Pas de données numérisées inventées. La convolution et la statistique restent nécessaires avant toute exclusion multimode. |
| D.2 Binaires | Prédiction non calculée ; aucun « boost universel » ajouté. |
| D.3 Nom | Lien au scénario dark dimension explicité, sans identification ni autre dépôt. |
| D.4 Registres | Résolu par un registre actif et les anciens registres conservés comme pièces d'audit sous `audits/sources_registres/`. |

## 5. Ce qui est utilisable et ce qui reste à établir

Le [premier manuscrit](publications/article_1/manuscript.pdf) est une étude théorique complète dans le domaine déclaré, préparée pour relecture. La nouveauté, l'intérêt pour une revue et l'approbation scientifique de l'auteur ne sont pas certifiés par cette préparation. La [base Φ](publications/article_2/PERIMETRE_ET_BASE.md) organise un deuxième article possible sans exiger une cosmologie ou une complétion UV hors de son sujet. La fermeture RAR, l'origine des paramètres, la relique et la protection radiative sont des questions de recherche explicites, non des résultats cachés dans une version historique.

Cette édition constitue la version courante du même dépôt GitHub. La branche principale conserve la dernière version corrigée, ses calculs et ses pièces d'audit. Les anciennes éditions complètes et les archives reçues sont sauvegardées localement, hors de l'arbre publié ; les registres sources sous `audits/sources_registres/` permettent de vérifier les corrections sans créer un autre registre actif.
