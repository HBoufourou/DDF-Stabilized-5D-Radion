# Lire le premier article en français

**L'article présente un modèle 5D calculable et des résultats sur sa stabilité et ses interactions.** Il ne demande pas au lecteur d'accepter tout le programme DDF. Son contenu peut être examiné à partir de l'action, des hypothèses et des démonstrations qu'il fournit.

## Le problème étudié

Imaginons une dimension spatiale supplémentaire de longueur finie, délimitée par deux surfaces appelées branes. La matière test est placée sur l'une de ces surfaces. La longueur et la géométrie de cet intervalle peuvent fluctuer; le plus léger mode scalaire associé est appelé radion.

Pour que le modèle ait un sens, il faut vérifier que ses petites perturbations ne croissent pas spontanément. Il faut aussi calculer comment chaque mode agit sur la matière. Une masse seule ne suffit pas à connaître l'effet observable : le couplage du mode compte également.

Le modèle choisi contient un champ scalaire dans la dimension supplémentaire, un potentiel de bulk quadratique et des potentiels linéaires aux bords. Son fond possède une symétrie de réflexion : les deux moitiés de l'intervalle se correspondent, avec inversion du signe du scalaire.

## Ce que le travail apporte

1. **Un modèle défini sans mélange de conventions.** L'action, les bords, les sources et les unités sont explicités.
2. **Des preuves de stabilité linéaire dans ce modèle.** Le secteur scalaire a un quotient spectral positif sous les hypothèses précisées. Le secteur tensoriel possède une démonstration séparée. Cela dépasse la recherche numérique de quelques masses positives.
3. **Une formule générale pour le couplage à faible rétroaction.** Le paramètre x compare la masse du stabilisateur à la longueur de l'intervalle. Pour x>0, la première correction calculée est positive. À x=2, son coefficient vaut environ 0,98342024.
4. **Des profils, masses et couplages numériques.** Les résultats à amplitude finie testent les limites de l'approximation analytique; d'autres modes que le radion sont également calculés.
5. **Des données et programmes accessibles.** Le lecteur peut examiner les hypothèses et reproduire les chiffres.

Ces résultats utilisent des méthodes de gravité–scalaire déjà établies. L'apport revendiqué est leur application détaillée à une famille précise, avec ses formules et contrôles. L'originalité et l'intérêt de cette étude doivent être évalués par rapport à la littérature, puis par une relecture scientifique indépendante.

## Ce que signifie le nombre 8,2 µm

Les calculs déterminent des rapports sans dimension, par exemple une masse multipliée par la longueur L. Pour les exprimer en micromètres, il faut choisir une échelle physique. Le dossier utilise parfois R0=L/pi=8,2 µm comme exemple de conversion.

À x=2 et epsilon=0,53, cette convention donne une portée du radion d'environ 30,30 µm. **La portée est calculée conditionnellement au rayon choisi; le rayon n'est pas prédit par ce calcul.** Dans une géométrie déformée, R0=L/pi et la longueur déduite du premier graviton massif ne sont pas automatiquement identiques.

Prédire R exigera une détermination indépendante des paramètres du stabilisateur. Pour que cette prédiction soit proprement une prédiction DDF, il faudra aussi démontrer leur origine dans la géométrie DDF.

## Comment lire les limites de l'article

« Stable » désigne ici la stabilité des petites perturbations des secteurs explicitement présents dans l'action. Cela ne prouve pas la stabilité de tous les modèles à cinq dimensions, ni la robustesse contre toute correction quantique ou contre l'ajout d'autres champs.

Les résultats à plusieurs amplitudes sont des membres d'une famille reconstruite : certaines constantes du modèle changent d'un membre à l'autre. Ils ne décrivent donc pas automatiquement l'évolution du rayon d'un seul univers avec toutes ses constantes fixées.

Une expérience réelle mesure une force, un couple ou une autre observable avec une géométrie particulière. Il faut calculer sa réponse à la somme des modes avant de conclure que le modèle est compatible ou exclu. Le présent manuscrit ne revendique pas un tel verdict.

## Parcours de lecture

- Pour comprendre l'apport : lire ce guide, puis le résumé et la discussion du [PDF anglais](article/manuscript.pdf).
- Pour examiner les équations : lire [le modèle et ses conventions](noyau/EFT_MODELE_ET_RESULTATS.md), puis [les démonstrations](noyau/ANALYTIQUE_ET_STABILITE.md).
- Pour vérifier les calculs : consulter [les résultats à x=2](resultats/spectre_5d.json), [l'extension à x=1,3](resultats/extension_x.json) et le dossier `calculs/`.
- Pour juger le positionnement scientifique : lire [l'antériorité](audits/ANTERIORITE_ARTICLE1.md), [la relecture interne](audits/AVIS_ARTICLE1.md) et [l'état des revendications](ETAT_SCIENTIFIQUE.md).
- Pour poursuivre vers une prédiction du rayon : lire [DEVELOPPEMENT.md](DEVELOPPEMENT.md).

Le manuscrit est une première version de recherche à discuter et à améliorer. L'achèvement de tout DDF n'est pas un préalable à son examen; une prédiction indépendante de R reste un objectif supplémentaire.


