# Reproduction : intégrité, recalcul et manuscrit

Le dossier conserve des références numériques et un lanceur qui écrit les nouveaux résultats ailleurs. Les neuf calculs configurés ont été rejoués dans cette édition ; le [rapport exécuté](verification/REPRODUCTION_EXECUTEE.json) conserve les versions, empreintes, tolérances et écarts. Tous ont passé la comparaison. Il s’agit d’une reproduction des modèles déclarés, pas d’une validation expérimentale.

## Installation locale

Dans un environnement Python 3.12 dédié, installer les dépendances indiquées dans `requirements.txt`. NumPy 2.3.5 et SciPy 1.18.1 sont les versions de référence. Les calculs d’événements, de réponse locale et plusieurs contrôles utilisent seulement la bibliothèque standard. Le rendu des articles demande en plus `requirements-article.txt`. Le dépôt n’installe rien automatiquement.

## Vérifier les fichiers

Depuis la racine :

```text
python verification/verify_package.py
```

Ce contrôle vérifie empreintes, couverture des fichiers, JSON, syntaxe, liens, registre unique, correspondance des 50 anciens IDs, tableaux du manuscrit et données. Il ne remplace pas les solveurs. Les fichiers produits dans `work/` et les caches Python sont exclus du gel documentaire.

## Refaire les calculs

```text
python verification/run_reproduction.py --profile article1
python verification/run_reproduction.py --profile extensions
```

Pour tout refaire en une seule commande :

```text
python verification/run_reproduction.py --profile all
```

Un emplacement neuf est créé sous `work/`, avec les scripts et entrées nécessaires. Les sorties copiées sont retirées avant exécution afin qu’un échec ne puisse être masqué par une référence préexistante. Chaque résultat est comparé à son JSON de référence avec les tolérances fixes de `verification/reproduction_config.json`. Le processus retourne un échec si un calcul, une lecture de sortie ou une comparaison échoue. Les références restent inchangées. `--destination` permet de choisir un autre emplacement neuf ; `--workers 1` limite la concurrence.

| Profil | Calculs réellement rejoués |
|---|---|
| article1 | Coefficient fermé à raideur finie ; longueur à action fixée ; spectre Galerkin ; courbure à tension fixée |
| extensions | Projection/profils Φ ; halos hydrostatiques ; intérieurs χ ; réponse à source et branches NR ; contraintes UV algébriques |

Les comparaisons reprennent tous les nombres et la structure des JSON des neuf calculs. Les résidus, ordres et autres diagnostics obéissent aux contrôles internes de chaque solveur ; leur accord entre exécutions n’est pas une erreur physique. Un petit écart de raffinement ne certifie pas une tour infinie ou une dynamique cosmologique. Les cas indépendants et limites analytiques sont détaillés dans les notes scientifiques.

Les anciens éléments finis et les anciens calculs RAR à source prescrite restent disponibles avec leurs résultats antérieurs. Ils ne sont pas silencieusement assimilés aux neuf calculs du profil courant. Les balayages exploratoires qui contiennent des branches rejetées ne font pas partie d’un verdict de stabilité globale.

## Régénérer le premier manuscrit

```text
python publications/article_1/build_manuscript.py --output-dir work/article_1_rebuild
```

Le [document de construction](publications/article_1/BUILD.md) décrit les formats. Le contenu du JSON unique produit Markdown, TeX et PDF. Le TeX est éditable ; le PDF livré est composé avec ReportLab et Matplotlib, sans compilation TeX séparée revendiquée. Pour régénérer la synthèse française à partir de sa source : `python publications/build_theorie.py` ; cette commande remplace son PDF, donc l’utiliser sur une copie si l’on veut préserver les empreintes de livraison.

## Archive reçue

Les six anciens scripts ont aussi été rejoués pour l’audit de provenance, avec SymPy 1.14.0 pour les deux calculs symboliques. SymPy n’est pas requis pour les neuf contrôles actifs. Le [rapport de rejeu](audits/REJEU_SCRIPTS_RECUS.json) distingue reproduction d’un affichage et interprétation correcte ; les sorties sont conservées sous `audits/rejeu_scripts_recus/`. Les scripts reçus originaux et les anciennes éditions complètes restent sauvegardés localement, hors de l'arbre publié. Les neuf calculs du profil courant disposent de leurs scripts et données dans le dépôt et ne dépendent pas de ces archives. Aucun code Git ni instruction contenue dans l’archive n’a servi d’autorité.

## Rejouer T1 / Z-light

Le test nul est distinct des neuf calculs ci-dessus. Il utilise uniquement la bibliothèque standard Python ; aucun paquet symbolique externe n’est requis.

```text
python noyau/T1_Z_LIGHT/run_t1.py
```

Le lanceur exécute cinq programmes dans un dossier neuf, dans l’ordre des dépendances : algèbre exacte et jonctions, courant covariant/ADM, contre-calcul ADM par composantes, neuf fonds quadratiques, puis intégration des deux normes sur trois fonds. Seuls les programmes sont copiés avant exécution. Les références ne sont jamais écrasées ; leur comparaison emploie rtol=10⁻⁹ et atol=10⁻¹⁰, en plus des contrôles internes documentés.

[Le rapport exécuté](verification/T1_REPLAY_EXECUTED.json) conserve les empreintes et statuts des cinq exécutions. GREEN signifie que le rejeu et les contrôles documentés réussissent dans le domaine de [la preuve](noyau/T1_Z_LIGHT/VERDICT_T1.md). Une erreur d’exécution retourne INCONCLUSIVE ; elle ne suffit pas à conclure à un ghost physique. Le vérificateur d’intégrité contrôle également les empreintes de ces cinq programmes, de leurs références et des entrées de l’intégrateur.

Le profil `all` du lanceur antérieur désigne ses neuf calculs configurés ; il ne lance pas T1. Utiliser la commande séparée ci-dessus pour ce complément. Le supplément T1 est un document Markdown autonome, non incorporé aux PDF livrés précédemment.
