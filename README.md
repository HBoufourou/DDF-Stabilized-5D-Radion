# DDF-Stabilized-5D-Radion

**Version corrigée, article 1 relu et T1 / Z-light intégré — 7 septembre 2026.**

Ce dossier poursuit le [même dépôt GitHub](https://github.com/HBoufourou/DDF-Stabilized-5D-Radion). Une action active définit la gravité 5D sur intervalle, le stabilisateur et ses bords quadratiques, puis un champ complexe minimal. Les paramètres libres, les théorèmes conditionnels et les questions ouvertes sont identifiés. La motivation « dark dimension » de Montero–Vafa–Valenzuela est un contexte ; elle ne détermine pas les constantes de cette action.

Lire d'abord [la théorie en français](THEORIE_DDF.pdf), ou [sa version texte](THEORIE_DDF.md). Pour la publication, ouvrir le [premier manuscrit anglais](publications/article_1/manuscript.pdf) avec [son supplément T1](publications/article_1/T1_SUPPLEMENT.md), puis [la base des articles suivants](publications/BASE_PUBLICATIONS_FR.md). La section 4 et l’annexe B intègrent désormais T1 au PDF principal. La synthèse PDF française reste un aperçu antérieur.

| Entrée | Contenu |
|---|---|
| [T1 / Z-light : verdict et preuves](noyau/T1_Z_LIGHT/VERDICT_T1.md) | GREEN dans le domaine linéaire plat déclaré ; X₁ hors domaine, deux polarisations gravitationnelles positives ; cinq programmes de rejeu |
| [Premier manuscrit](publications/article_1/manuscript.md) | Bords quadratiques, longueur, spectre, couplages et courbure ; sources TeX/JSON/PDF |
| [Audit de correction et de complétude](AUDIT_CORRECTIONS_ET_COMPLETUDE.md) | Les 15 nouveaux fichiers reçus, les erreurs corrigées et les points restant ouverts |
| [Réponse à l'avis scientifique](audits/REPONSE_AVIS_ARTICLE1.md) | Objection → section et preuve effectivement intégrées |
| [Action](MODELE.json) et [état scientifique](ETAT_SCIENTIFIQUE.md) | Domaine et limites des affirmations |
| [Registre actif unique](registre_revendications.json) | 31 affirmations, avec une preuve et un domaine pour chacune |
| [Correspondance des anciens registres](audits/CORRESPONDANCE_ANCIENS_REGISTRES.csv) | 50 anciens identifiants traités sans reprendre automatiquement leurs statuts |
| [Couplage à raideur finie](noyau/stabilisation/COUPLAGE_QUADRATIQUE_FERME.md) | Formule fermée, bornes et relation spectrale sans R absolu |
| [Secteur Φ](matiere/Phi/FERMETURE_PHI.md) | Projection, contrôle de la tour et profils chargés sonde |
| [RAR](extensions/RAR/README.md) | Calculs conditionnels de halos et corrections des interprétations |
| [Reproduction](REPRODUCTION.md) | Intégrité et recalcul scientifique séparés ; résultats écrits hors références |
| [Continuer le développement](DEVELOPPEMENT.md) | Questions précises et critères pour accepter une nouvelle contribution |

Le premier article est un manuscrit de recherche à relire, sans garantie de publication. Il n'annonce ni R micrométrique prédit, ni cinquième dimension observée, ni RAR dérivée du noyau. La seconde étude concerne Φ sur métrique fixe ; les extensions galactiques et UV restent dans ce même projet.

La branche principale présente uniquement cette dernière version corrigée. Les anciennes éditions complètes, les anciens manuscrits et les archives reçues sont sauvegardés localement, hors de l'arbre publié. Les registres sources sous `audits/sources_registres/` et les sorties de rejeu sous `audits/rejeu_scripts_recus/` restent des pièces d'audit ; le registre à la racine est le seul actif. L'historique normal des commits Git conserve la trace des mises à jour du même dépôt.

Le [rapport de relecture du 7 septembre](audits/article1_2026_09_07/AUDIT_FR.md) détaille les corrections du premier article, les antériorités et les questions encore ouvertes. Le manuscrit révisé contient directement la preuve T1 et conserve les portées en unités sans dimension.
