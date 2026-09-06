# Correspondance des anciens registres : comptes et lecture

6 septembre 2026. Photographie du registre actif avant l'ajout éventuel de nouvelles revendications S02/S03. Aucun registre source ou actif modifié.

L'extraction contient effectivement **18** revendications dans `source/ddfr/registre_revendications.json` et **32** dans `source/ddfr/EFT_v3/CLAIMS_v3.csv`, soit **50 identifiants distincts**. Le CSV reçu a sept colonnes, sans ligne mal formée détectée. Les copies historiques imbriquées ne sont pas comptées une seconde fois. Le registre actif lu contient **27** identifiants.

La recherche dans toute l'extraction `source/ddfr` ne trouve **aucun fichier nommé `REGISTRE_UNIFIE.csv`**, contrairement à ce qu'annonce `received/CE_QUI_MANQUE_2026-09-06.md`. Le nombre annoncé 18+32=50 est correct ; la présence du fichier unifié annoncé ne l'est pas dans cette extraction.

`CORRESPONDANCE_ANCIENS_REGISTRES.csv` contient exactement **50 lignes de correspondance**, une par ancien ID, avec revendication, statut, portée et preuve anciens préservés littéralement. Le traitement est une décision manuelle, distincte du statut ancien ou actif :

| Traitement | Nombre |
|---|---:|
| conservé, dans sa portée explicitée | 12 |
| corrigé | 24 |
| déclassé | 4 |
| historique | 8 |
| hors noyau | 2 |

« Conservé » peut conserver un constat négatif ou une question ouverte : ce mot ne signifie pas automatiquement « démontré ». « Corrigé » conserve une partie utilisable en corrigeant portée, convention ou interprétation. Les liens vers des IDs actifs peuvent désigner une limite, une reprise partielle ou un remplacement ; **ils ne constituent pas une équivalence logique de revendications**. La colonne `nature_correspondance` l'explicite. Les statuts actifs sont recopiés pour information seulement, jamais fusionnés.

Six anciens IDs n'ont aucun équivalent actif, et portent explicitement `AUCUN` : DDFU-001 à DDFU-004 (géométrie historique), V3-017 (radion matière noire non retenu, programme distinct) et V3-021 (autre branche monotone). D'autres énoncés composés n'ont qu'une reprise partielle : DDFU-014 ne donne notamment aucun statut actif à la baryogenèse ou au Fano physique. Une prédiction DR4 n'est pas créée par un lien à E01/G05, qui constatent précisément les limites du calcul.

Les références de la colonne `preuves_actives_relatives_au_depot` se résolvent depuis la racine du dépôt canonique. Les preuves anciennes sont préservées comme références de provenance, sans prétendre qu'elles constituent des preuves actives valides. Le complément `AUDIT_MATIERE_RAR.md` donne les contrôles précis sur Φ, la condensation, les couplages et RAR ; les autres entrées renvoient au document central et aux preuves actives indiquées.

Le contrôle de livraison vérifie la couverture exacte des 50 anciens IDs, l'unicité des correspondances, l'existence des IDs cibles et la lisibilité du CSV produit. `COMPTES_CORRESPONDANCE.json` conserve les comptes, les IDs actifs lus et les empreintes SHA-256 des trois registres. Les IDs futurs ne sont ni devinés ni ajoutés. Une mise à jour future devra réexaminer les correspondances, pas remplacer mécaniquement leurs statuts.

La photographie du registre actif à 27 IDs est préservée dans `audits/sources_registres/registre_canonique_avant_correction.json`, depuis la racine du dépôt. Les deux registres reçus sont conservés dans ce même répertoire comme pièces d'audit. La présente édition ajoute S02, S03, G07 et G08, soit 31 IDs actifs, sans effacer cette traçabilité. Seul `registre_revendications.json` à la racine définit le registre courant.
