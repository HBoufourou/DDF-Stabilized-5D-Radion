# DDF-Stabilized-5D-Radion

**Premier manuscrit de recherche — version du 5 septembre 2026.**

Ce dépôt développe un modèle précis de gravité à cinq dimensions : un intervalle délimité par deux branes, un champ scalaire à potentiel quadratique et des potentiels de bord linéaires. Il rassemble un premier article, ses démonstrations, les résultats numériques et les programmes permettant de les reproduire.

Le travail établit, sous les hypothèses annoncées, la stabilité linéaire des secteurs scalaire et tensoriel. Il donne une expression analytique générale de la première correction au couplage du radion, puis compare cette expression aux profils calculés avec rétroaction. **Le rayon physique reste un paramètre : ce manuscrit ne prédit pas indépendamment 8,2 µm et ne revendique aucune détection d'une cinquième dimension.**

## Commencer la lecture

- [Manuscrit anglais — PDF](article/manuscript.pdf) : le premier article à lire et à discuter.
- [Guide de lecture en français](GUIDE_LECTURE_FR.md) : ce que l'article apporte et comment comprendre ses limites.
- [État scientifique](ETAT_SCIENTIFIQUE.md) : résultats démontrés, calculés et questions ouvertes.
- [Démonstrations analytiques et stabilité](noyau/ANALYTIQUE_ET_STABILITE.md), puis [modèle et conventions](noyau/EFT_MODELE_ET_RESULTATS.md).
- [Antériorité scientifique](audits/ANTERIORITE_ARTICLE1.md) et [avis de relecture interne](audits/AVIS_ARTICLE1.md).

Le manuscrit est aussi disponible en [LaTeX](article/manuscript.tex) et dans sa [source structurée](article/manuscript.json). Il s'agit d'un manuscrit de recherche, sans validation de soumission ni garantie d'acceptation. La contribution est une étude quantitative de cette famille de modèles; son intérêt et son originalité doivent encore être évalués indépendamment.

## Résultats et reproduction

Les points de référence à x=2 figurent dans [le tableau lisible](resultats/RESUME.md) et [les données originales du recalcul](resultats/spectre_5d.json). L'[extension à x=1 et x=3](resultats/extension_x.json) complète ces résultats. Le [contrôle de convergence par éléments finis](resultats/fem_verification.json) fournit une comparaison numérique supplémentaire. Le [rapport détaillé](verification/FEM_REPORT.md) précise les vitesses de convergence et les plateaux de précision observés à faible amplitude.

Depuis la racine du dépôt, avec Python et les dépendances indiquées dans [requirements.txt](calculs/requirements.txt) :

```text
python verification/verify_package.py
python calculs/couplage_faible_retroaction.py
python calculs/weak_backreaction_general.py
python calculs/spectre_5d.py
python calculs/extension_x.py
python calculs/fem_verify.py --extended
```

Les calculs spectraux peuvent prendre plusieurs minutes. Les sorties portant le suffixe `_recalcule.json` permettent de comparer les calculs aux résultats de référence. [model.py](calculs/model.py) contient le moteur utilisé pour l'extension. Aucun verdict d'exclusion expérimentale automatisé n'est fourni : il faut encore construire la réponse de l'expérience au signal complet.

## Organisation du dossier

| Dossier ou document | Contenu |
|---|---|
| `article/` | Premier manuscrit, sources et éléments associés |
| `noyau/` | Action, conventions, démonstrations et géométrie conditionnelle |
| `calculs/` et `resultats/` | Programmes et données de référence |
| `verification/` | Contrôles numériques et d'intégrité |
| `audits/` | Antériorité, relecture et analyses qui justifient les corrections |
| `historique/` | Documents sources conservés pour retracer le travail |
| [DEVELOPPEMENT.md](DEVELOPPEMENT.md) | Étapes suivantes pour cet article et pour prédire R |
| [CORRECTIONS_APPLIQUEES.md](CORRECTIONS_APPLIQUEES.md) | Passage des formulations historiques aux résultats actuels |
| [registre_revendications.json](registre_revendications.json) | Statut explicite de chaque revendication |

## Rapport au programme DDF et provenance

La géométrie DDF conditionnelle est conservée et documentée. Son raccord à cette action 5D reste ouvert : réunir ces deux secteurs dans un dépôt ne démontre pas leur équivalence physique. Les anciens articles I–VIII et manuscrits A/B gardés dans `historique/` ne sont pas les versions scientifiques actives du présent article.

Les sources de projet sont attribuées à Hicham Boufourou selon leurs fichiers d'origine. Les corrections, développements et rédaction ont bénéficié d'une assistance par IA; la responsabilité de vérifier et d'approuver le manuscrit incombe à son auteur. [PROVENANCE.json](PROVENANCE.json) décrit les sources et leur couverture. Les informations de licence d'origine sont préservées dans les snapshots; aucune licence globale nouvelle n'est imposée.

L'objectif à plus long terme demeure de relier la géométrie DDF à des paramètres physiques déterminés, puis à une prédiction testable de la taille de la dimension supplémentaire.



