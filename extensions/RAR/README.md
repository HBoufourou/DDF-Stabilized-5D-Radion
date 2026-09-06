# RAR dans le dépôt DDF unique

Cette extension ajoute des opérateurs absents du noyau canonique. Aucune dérivation complète depuis la 5D n’est revendiquée.

- [Nouvelle densité hydrostatique et frontière de fluide](RAR_HALOS_AUTOCOHERENTS.md) : 27 équilibres, trois intérieurs avec χ fini, contrôle du quartique et de la diffusion.
- [Branches à source prescrite](RAR_SOLUTIONS_RADIALES.md) : calculs précédents, sélection radiale et comparaison d’énergie sous mêmes conditions.
- [Raccord 5D](RAR_RACCORD_5D.md) : opérateurs et coefficients nécessaires, limites du mécanisme.
- [Contrôle radial indépendant](RAR_RADIAL_REFEREE.md).

La densité centrale est une donnée d’état ; la masse intégrée source est définie au premier ordre en dérivées. Le raccord de phase, le courant NLO complet et la stabilité d’un halo global restent à déterminer. Les chiffres RAR sont des diagnostics théoriques, sans fit observationnel.

## Corrections du dossier reçu

Lire [l’audit matière et RAR](AUDIT_MATIERE_RAR.md) et [les directions corrigées](DIRECTIONS_15_CORRIGEES.md). Le calcul [local_coupling_checks.py](local_coupling_checks.py) vérifie un contre-exemple de réponse à source, le domaine n≥0 du quartique/sextique et les conventions de densité et de Planck. Il ne modifie pas implicitement le noyau U(1) minimal.
