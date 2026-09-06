# Contrelecture du nouveau rejeu T1

Date : 6 septembre 2026. Fichiers examinés : `t1_background_replay.py`, `symplectic/covariant_adm_current.py`, `symplectic/PRESYMPLECTIQUE_ADM_ET_BORDS.md`, `boundary/DERIVATION_NOYAU_NUL_ET_BORDS.md`, les intégrales numériques et `VERDICT_T1.md` dans le répertoire de travail T1. Contrelecture de la complétude tensorielle nulle et consolidation finale achevées.

## Calcul de bord et fonds

La linéarisation directe d'Israel dans `israel_X1` conserve la variation de la trace de K, celle de la métrique inverse et la tension totale U/B=3 eta A'. Les contributions isotropes s'annulent et il reste eta b p_mu p_nu. Les contractions scalaires s'annulent à p²=0 tandis que ce tenseur reste non nul au bord droit. Les signes et les facteurs de deux sont cohérents avec un intervalle physique unique.

La matrice de bord agit sur (c1,C,theta0,thetaL), theta_i=zeta_i+X_i^y. Les deux lignes scalaires fixent theta_i lorsque sigma'_i D_i est non nul ; les deux lignes métriques fixent ensuite C et c1 parce que I>0. Les contrôles de rang en D_i=0 sont correctement présentés comme changements de domaine, sans verdict de ghost. Les neuf fonds numériques constituent des exemples ; leur accord ne démontre pas à lui seul la complétude de la famille analytique.

## Contraction ADM indépendante

Le contrôleur `adm_component_referee.py` a été écrit séparément pendant la contrelecture. Il reconstruit les matrices 4x4 de la géométrie des tranches temporelles, calcule les extrinsèques linéarisées depuis dot h-DN-DN, forme les momenta métriques et scalaire, puis contracte la forme canonique. Il ne reprend pas l'expression condensée z_ADM pour produire sa valeur.

Les 128 entrées déterministes indépendantes, incluant la polarisation tensorielle +, donnent un écart absolu maximal de 2,842170943040401e-14 avec l'expression condensée du programme examiné. Ce sont des tests de contraction algébrique, pas 128 fonds solutions ni 128 tests expérimentaux. La sortie est `adm_component_referee.json`.

## Courant covariant et coin

La variation des deux métriques inverses dans theta, la connexion linéarisée et la densité du volume sont présentes. Les termes delta Gamma conservés correspondent à la variation de nabla_d h_ce-nabla_c h_de. Le terme scalaire conserve la variation de g^{0y} sigma', nécessaire au couplage croisé entre s et b.

Le coin C comporte correctement les variations de la densité induite, de gamma^{00}, de n^y et de n^0. Avec l'orientation spatiale dx1 dx2 dx3 dy, la correction Omega=-integral_boundary delta C ajoute bien la différence de ses composantes temporelles entre L et 0. Cela explique le signe apparemment opposé à une lecture sans orientation.

Les deux routes conduisent ainsi à la même forme complète. Pour X1, le volume covariant vaut -2BI et le coin -4BI ; le volume canonique ADM vaut zéro et le tilt -6BI. Le total est Z=-6BI. La convention du manuscrit est N=Z/2, d'où N=-3BI. Pour la polarisation graviton e_ij e_ij=2, Z=BI/2 ; pour une polarisation de norme tensorielle unité, Z=BI/4. Aucun facteur de deux contradictoire n'a été trouvé.

La table des coefficients analytiques attendus doit être distinguée des integrations réellement exécutées. Son nouvel intitulé `X1_analytic_expected_coefficients_in_units_BI` accomplit cette distinction ; le rejeu numérique des intégrales est produit séparément par l'agent principal.

## Quotient et portée de la complétion

La polarisation indépendante de z_ADM avec une transformation normale, puis la contrainte C1 et A''=-sigma'^2/(3B), confirment le terme de bord -3B[a²F zeta]. Il s'annule pour toute variation admissible appariée lorsque zeta s'annule aux bouts. Cela prouve une dégénérescence de la forme et non la seule annulation d'une auto-contraction.

Le tiré-en-arrière linéaire par hbar=h+L_X g et sbar=s+X^y sigma' rend une transformation combinée (L_xi g,xi^y sigma',-xi) nulle dans les variables habillées. Ce raisonnement est admissible comme complétion de variables d'implantation de la même action. Il doit conserver GHY et potentiels, et l'indépendance de l'extension intérieure de X doit être comprise modulo les transformations de jauge intérieures. Il ne démontre pas une nouvelle dynamique physique de bords ni une algèbre non linéaire de charges.

## Complétude nulle : contrelecture achevée

Le document `boundary/DERIVATION_NOYAU_NUL_ET_BORDS.md` a ensuite été examiné intégralement. Les composantes du Ricci 4D dans la base (+,-,1,2) sont correctes. L'équation radiale gaussienne normale se retrouve en linéarisant R_mu nu=(2/3B)V g_mu nu et en soustrayant le fond. Les composantes de quantité de mouvement rendent h-- et h-a constants en y. L'intégration des combinaisons d'Einstein indiquées, avec leurs deux jonctions d'Israel et I>0, impose leur annulation. Les combinaisons restantes h+-+t et h+a sont bien éliminées par des difféomorphismes tangentiels constants en y avec k non nul. Aucun inverse de p² ni de A' n'est nécessaire.

Le bloc scalaire restant se reconstruit à partir de C1 et 55 : leur différence impose G=(s/q)', puis F=A's/q-c1. La jonction anisotrope fournit l'équation pour chi et les deux contraintes sur c1,C. Les deux vraies polarisations gravitationnelles sont distinctes de la structure p_mu p_nu et ne réintroduisent pas un paramètre capable de réparer X1. Aucun défaut bloquant de complétude n'a été identifié dans ce domaine.

## Intégrales effectivement exécutées

`t1_integrated_norms.py` et sa sortie ont été examinés. Le programme réintègre trois fonds à partir du bord gauche, à 64, 128 et 256 cellules. Il contracte réellement les deux courants aux points d'intégration, ajoute leurs termes de coin, et vérifie séparément X1, la jauge zeta=sin(pi y/L) et une polarisation + du graviton. La lecture des valeurs ne révèle aucune substitution des constantes cibles aux courants calculés. Les coins de la jauge à endpoints nuls sont nuls analytiquement.

L'écart maximal au maillage le plus fin est 3,584524270011783e-10 en unités BI ; il provient de l'intégrale covariante de jauge, et décroit approximativement d'un facteur 16 lorsque le nombre de cellules double. Le total de X1 retrouve N=-3BI par les deux routes. Il demeure hors du domaine de bord.

## Conclusion de la contrelecture

Le verdict **T1 GREEN dans le domaine linéaire propagatif déclaré** est compatible avec les preuves et contrôles examinés, sous q non nul, D0 DL non nul, fond plat lisse sur intervalle fini, action minimale EH+scalaire canonique+GHY+potentiels isotropes et vide matériel. Pour l'extension au secteur massif couvert par F02, les poids de bord doivent rester strictement positifs comme indiqué dans sa démonstration existante. La branche principale symétrique à rigidités positives satisfait ces conditions.

Cela signifie : X1 est exclu par Israel ; le quotient scalaire/longitudinal nul est trivial ; deux polarisations du graviton subsistent avec Z>0. Ce résultat ne signifie ni fermeture de toute DDF, ni preuve de stabilité non linéaire ou quantique, ni compatibilité expérimentale. Les lieux q=0 ou D_i=0, les nouvelles cinétiques de brane, les fonds courbes et le secteur p_mu=0 restent hors de ce verdict.

Les deux clarifications éditoriales demandées sont présentes dans les notes finales : la complétion linéaire provient de la même action tirée en arrière, et la reproduction actuelle de -3BI ne certifie pas un ancien log absent.

Le contrôleur `boundary/null_boundary_checks.py` a désormais été exécuté par l'agent principal. Son résultat communiqué a été confronté ici au fichier `boundary/null_boundary_checks.json` : **29 contrôles PASS**, comprenant 28 identités exactes — dont trois autocontrôles de l'arithmétique rationnelle — et le rang générique quatre. L'attente de cette pièce est donc levée. Le relecteur n'a pas réexécuté ce contrôleur exact ni l'intégrateur : il en a lu les programmes et sorties, en plus de la contrelecture analytique indépendante. Le calcul effectivement écrit et exécuté directement pendant cette contrelecture est `adm_component_referee.py`, avec ses 128 comparaisons décrites plus haut. Ces niveaux de contrôle restent distincts.

La dernière lecture de `VERDICT_T1.md` ne révèle pas de nouvelle objection physique bloquante ni d'extension injustifiée du domaine : le texte distingue la norme prolongée négative de X1, son exclusion par les jonctions, le quotient scalaire nul et les deux polarisations gravitationnelles positives. Il conserve explicitement les restrictions linéaires, plates et génériques, ainsi que la séparation entre contrôle interne, expérience et DDF complète. Le terme GREEN doit continuer à être lu avec ce domaine exact, jamais comme une validation globale de la théorie.

Cette contrelecture est une vérification interne effectuée avec des agents IA distincts ; elle ne constitue pas une évaluation externe par les pairs. Les chemins de travail `boundary/` et `symplectic/` cités ci-dessus correspondent, dans la livraison, à `noyau/T1_Z_LIGHT/`.
