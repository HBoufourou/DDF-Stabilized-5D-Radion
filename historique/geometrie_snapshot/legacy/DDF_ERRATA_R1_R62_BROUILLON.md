# DDF I–VIII — note de statut et corrections provisoires

> **Brouillon à relire avant publication sur GitHub ou Zenodo.**

La série DDF I–VIII est conservée comme archive de recherche datée. Un audit cumulatif R1–R62 a identifié des résultats réutilisables, des affirmations conditionnelles et plusieurs corrections qui changent l’interprétation physique initiale. Les versions archivées ne doivent donc pas être citées comme une théorie phénoménologique démontrée.

## Corrections principales

1. **Rayon.** La valeur \(R=8{,}2\,\mu{\rm m}\) est un benchmark historique. Elle n’est pas une sortie unique de l’EFT minimale. R20 établit une sous-détermination dans la paramétrisation où les coefficients bulk/brane sont redimensionnés avec \(L\) ; il ne démontre pas qu’une microphysique ne peut jamais fixer \(L\).
2. **Tour d’Article II.** Le quadruplet d’Airy entrelace les spectres de deux problèmes aux limites distincts, Neumann et Dirichlet. Il ne constitue pas la tour d’un seul scalaire avec un domaine auto-adjoint unique.
3. **Échelles liées.** La relation \(\hbar c/R\simeq24\,{\rm meV}\) pour \(R\simeq8{,}2\,\mu{\rm m}\) n’est pas une confirmation indépendante de \(R\).
4. **Stabilité numérique.** Le script auxiliaire local **r14_scan.py** tronque les valeurs propres négatives et ne peut donc pas les détecter. Cela ne réfute pas l’identité d’énergie de la branche sans tachyon dans l’action minimale ; l’existence pour produit positif dépend encore d’un signe WKB à publier comme lemme, et la surface marginale reste ouverte.
5. **Ajustement micrométrique.** Le témoin R18 ajuste deux paramètres à deux cibles. R17 contrôle surtout une convention \(L\simeq\pi R\). R19 établit seulement que la tour TT ajustée passe la limite considérée ; le verdict complet exige le propagateur matière–matière invariant de jauge, incluant les scalaires et mélanges de bord.
6. **Branche hétérotique.** R22–R38-HM fournit une architecture 11D→5D à deux frontières et des no-go bornés, mais pas le plongement exact de l’action DDF. La longueur \(4{,}10\times10^{-32}\,{\rm m}\) de R24 est propre au benchmark Type-5 ; aucun même vide n’y dérive le micron, T1/T2, la tour, la matière noire et l’énergie sombre.
7. **Variables géométriques.** Le paramètre complexe de lissage, le rapport de forme, le module kählérien et le rayon métrique sont distincts.
8. **Changements de géométrie.** Les flux, périodes et charges calculés pour POLY925 ne sont pas automatiquement valables pour POLY944 ou pour la résolution de Hodge \((5,85)\).
9. **Tour BPS.** Une orbite de monodromie, un tube topologique ou une masse centrale linéaire ne prouvent pas l’existence d’une tour d’états stables. Le \(T^3\) global n’est pas établi pour la couture finale R62.
10. **No-go R62.** L’obstruction concerne une tour fermée D3/\(C_4\) paire dans les orientifolds O3/O7 testés. Elle ne constitue pas un no-go de toute tour KK gravitationnelle.
11. **Deux historiques R1.** « R1 eigenmode » et les fichiers **R1_\*** de stabilité sont distincts ; la correction du ghost ne valide pas la tour d’Airy.

## État des articles

| Article | Statut provisoire |
|---|---|
| I | motivation et sous-résultats explicitement redérivés seulement ; sélection de \(L\) et force totale non validées ; durée de vie sans bounce ; \(w\) sans EFT cosmologique/solution FRW |
| II | interprétation monoscalaire retirée ; chaque branche reste seulement un spectre mathématique conditionnel |
| III | article mis en quarantaine : transition, cascade, condensat, RAR, taux et screening doivent être redérivés dans une même EFT |
| IV | coïncidences reclassées comme motivation, non comme preuves indépendantes |
| V | plongement historique supersédé ; méthodes de contrôle conservées |
| VI | affirmation que la géométrie fixe \(R\) retirée ; programme LVS/Tyurin-type maintenu comme hypothèse à tester |
| VII | plan de Fano différé jusqu’à construction d’un réseau physique de sept classes |
| VIII | baryogenèse maintenue seulement comme proposition conditionnelle séparée |

## Programme révisé

Le programme actif se divise en trois projets indépendants :

- **DDF-G :** résultat Tyurin-type sur une dégénérescence semistable à couture K3, \(U(2)\), LMHS \(II_{18}\) et obstruction du tube fermé \(C_4\) dans l’ansatz O3/O7 testé ;
- **DDF-KK :** recherche d’une longue direction par diagnostic spectral, puis calcul spin-2 gauchi du vrai vide ;
- **DDF-BPS :** recherche d’une infinité d’états stables dans le parent \(\mathcal N=2\).

La prochaine étape est de vérifier les conditions strictes de Tyurin et de valider un pipeline spectral falsifiable. Le pilote ne prouvera pas à lui seul une tour physique. Aucune nouvelle revendication sur la matière noire, l’énergie sombre ou Fano ne sera ajoutée avant le test de la vraie géométrie.

## Politique de version

- Les articles I–VIII restent accessibles pour assurer la traçabilité historique.
- Toute version future citera cette note et distinguera clairement résultat démontré, calcul borné, candidat et conjecture.
- Les scripts seront accompagnés de leurs entrées indépendantes, de tests de signe et d’un registre des résultats supersédés.
- Une nouvelle soumission ne reprendra pas l’ancien Article III sous un autre titre ; elle sera fondée sur un résultat central nouveau et soumise d’abord à une évaluation scientifique appropriée.

