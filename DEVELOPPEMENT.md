# Continuer le même modèle et produire des articles

Commencer par [l'action](MODELE.json), [le registre actif](registre_revendications.json) et [la base des publications](publications/BASE_PUBLICATIONS_FR.md). Une idée nouvelle peut modifier la théorie ; elle doit alors annoncer quels opérateurs, paramètres ou états ont changé et recalculer les résultats concernés.

| Priorité | Problème précis | Livrable vérifiable pour l'étape suivante |
|---|---|---|
| Article 1 | Évaluer la nouveauté et la robustesse du résultat à raideur finie | Comparaison d'équations et de conventions avec les travaux proches ; relecture du manuscrit et reproduction indépendante des tableaux |
| Secteur Φ | Transformer l'étude sonde en deuxième manuscrit | Présenter action, projection, bornes, profils chargés et stabilité linéaire ; conserver distincts mélange KK, régime NR et énergie de rétroaction |
| RAR | Résoudre le raccord global du champ χ et du fluide | Continuité de la solution et des flux à l'extérieur, modèle de phase normale, charge physique NLO, comparaisons à même charge ; échec ou existence documentés |
| Galaxies | Tester une extension globale une fois définie | Données et paramètres explicités, mêmes règles de masse baryonique et d'incertitude, ajustement reproductible et comparaison aux modèles de référence |
| Relique sombre | Calculer un état cosmologique | Équations de champ/Boltzmann, réchauffement et domaine EFT, charge initiale, taux et espace de phase ; distinguer une amplitude ajustée d'une prédiction |
| Échelle R | Fermer l'entrée dimensionnelle | Fournir une mesure ou un mécanisme indépendant pour μ et les rapports ; montrer quelles autres masses et couplages deviennent alors prédits |
| Théorie UV | Raccorder l'action, pas seulement des signes | Réduction des cinétiques et potentiels, bilan des sources, coefficients de bord, corrections et contrôle des masses |
| Laboratoire / binaires | Définir un observable | Convolution avec géométrie/environnement et analyse statistique appropriée ; aucun verdict à partir d'une ressemblance de courbes |

## Règles de travail proportionnées

1. Pour chaque résultat, écrire les entrées, les équations, les conditions aux limites et le domaine d'approximation. Une condition initiale ou un paramètre ajusté reste identifiable comme tel.
2. Conserver le raisonnement analytique et au moins un contrôle indépendant adapté : autre discrétisation, limite exacte, variation de l'action ou identité de conservation. Un test qui répète la formule n'établit pas sa physique.
3. Mettre les essais dans `work/` et produire les nouvelles références dans un emplacement séparé. Le lanceur de reproduction ne remplace pas silencieusement les données validées.
4. Si une nouvelle contribution change l'action, ajouter son dictionnaire et son effet sur les jonctions, le spectre et les couplages. Les extensions restent dans ce dépôt avec leur statut explicite.
5. Mettre à jour ensemble le registre, les preuves, les tableaux et les sources du manuscrit. Les comparaisons historiques servent à repérer les régressions ; elles ne deviennent pas des prémisses supplémentaires.

Une correction documentée renforce le modèle. Il n'est pas nécessaire de promettre une théorie définitive pour écrire un article limité et exact dans ses hypothèses. Aucune procédure automatique de publication ou de gel de prédiction n'est créée par ce document.
