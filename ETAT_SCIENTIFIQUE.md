# État scientifique actuel

Version du 5 septembre 2026. Le dépôt contient désormais un premier manuscrit et un développement analytique du modèle effectif; il dépasse le stade du seul audit des anciennes versions.

| Objet | Résultat actuel | Portée et limite |
|---|---|---|
| Modèle du premier article | Action gravité–scalaire, intervalle physique, potentiels de bord linéaires et source minimale explicités | Modèle effectif posé; son origine géométrique DDF n'est pas dérivée |
| Stabilité scalaire linéaire | Preuve par une formulation de Sturm–Liouville avec termes de bord positifs | Branche régulière, sigma' non nul et signes des coefficients de bord démontrés; epsilon=0 traité séparément |
| Stabilité tensorielle linéaire | Mode sans masse constant et masses² non négatives par identité intégrale | Secteur tensoriel de l'action retenue, conditions de Neumann, aucun Einstein induit de brane |
| Cinétiques et couplages | Normes dérivées de l'action et sources minimales de brane | Toute cinétique, courbure induite ou source supplémentaire demande un nouveau calcul |
| Faible rétroaction, x>0 | Expressions analytiques générales de kappa(x) et c_alpha(x)>0 | Première correction à epsilon fixé comme dans le modèle; pas une série exacte à forte amplitude |
| Valeur à x=2 | c_alpha=+0,98342023984 | Cas particulier du résultat général |
| Fonds et spectres numériques | Recalcul des références à x=2 et extension à x=1,3 | Points échantillonnés d'une famille dont certains paramètres d'action sont reconstruits |
| Couplage à rétroaction finie | Par exemple alpha_r≈0,40227 à x=2, epsilon=0,53 | Valeur obtenue à partir des profils normalisés, sans extrapolation de la série faible |
| Convergence numérique | Contrôles de résidus et comparaison par éléments finis documentés | Le nombre de modes calculés reste fini; aucune précision uniforme sur toute une région n'est déduite |
| Antériorité | Bibliographie primaire comparée aux équations et hypothèses | Les méthodes générales sont connues; originalité de l'étude de cas à évaluer indépendamment |
| Manuscrit | Premier article théorique rédigé avec preuves, calculs, références et limites | Manuscrit de recherche; aucune soumission validée ni acceptation garantie |
| Rayon 8,2 µm | Conversion illustrative choisie | Pas une prédiction indépendante |
| Minimum historique à 8,34 µm | Non reproduit par le script annoncé | Revendication historique inactive |
| Confrontation expérimentale | Signal composé défini, sans verdict d'exclusion | Géométrie expérimentale, incertitudes et réponse au signal complet à construire |
| Champs et opérateurs supplémentaires | Hors de l'action du premier article | Leur stabilité et leurs mélanges restent ouverts s'ils sont ajoutés |
| Géométrie R63, U(2), II18, R64 | Résultats conservés dans leurs domaines audités | Généricité A3 et raccord physique ouverts; R64 ne supprime pas toute tour KK neutre |
| Pilote R65 | Banc d'essai sur géométries connues | Pas le spectre d'une métrique DDF |
| Raccord géométrie → paramètres 5D → R | Ouvert | Aucune origine indépendante de l'échelle dimensionnelle calculée |
| Matière noire, énergie noire, baryogenèse | Non dérivées par ce modèle | Aucune de ces applications n'est requise pour lire le premier article |
| Existence physique d'une cinquième dimension | Hypothèse | Aucun résultat du dossier constitue une détection |

## Ce qui a changé dans l'argument de stabilité

Le statut de stabilité ne repose plus sur le seul balayage de racines positives. Pour le modèle défini et la branche régulière étudiée, un quotient spectral strictement positif contrôle tout le secteur scalaire linéaire admissible. Le secteur tensoriel possède sa propre preuve. La positivité cinétique résulte de l'action. Ces résultats sont détaillés dans [ANALYTIQUE_ET_STABILITE.md](noyau/ANALYTIQUE_ET_STABILITE.md) et raccordés à des méthodes déjà publiées.

Cela ne constitue pas une preuve de stabilité non linéaire, quantique ou cosmologique, ni une preuve pour tous les champs imaginés dans l'histoire de DDF. Les degrés de liberté ajoutés à l'action, les opérateurs supplémentaires et la robustesse de la troncature demandent une analyse distincte.

## Ce que l'article peut revendiquer

Le [manuscrit](article/manuscript.pdf) caractérise une famille précise, sa stabilité linéaire, ses masses et ses couplages. Une tendance du couplage le long de cette famille ne devient pas une loi universelle de tous les modèles 5D. Les [notes d'antériorité](audits/ANTERIORITE_ARTICLE1.md) distinguent les méthodes connues des résultats spécifiques calculés ici.

Une publication consacrée à ce modèle n'exige pas que toute la théorie DDF soit achevée. Une publication annonçant une prédiction absolue de R exigerait en plus une détermination indépendante des paramètres dimensionnels et un mécanisme de raccord contrôlé.


