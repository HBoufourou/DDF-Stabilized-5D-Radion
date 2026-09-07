# Contrelecture adversariale avant préparation arXiv

> **Statut au 7 septembre 2026 :** compte rendu conservé de la relecture avant intégration. Les corrections retenues ont été appliquées au manuscrit livré, y compris les quatre précisions finales de notation. Le [bilan final](AUDIT_FR.md) distingue les corrections intégrées des limites scientifiques restantes.

Date : 7 septembre 2026. Auteur scientifique du projet : Hicham Boufourou. Relecture technique interne assistée par IA ; aucun endossement par un rapporteur externe n'est revendiqué.

## Périmètre et conclusion

Ont été examinés : le manuscrit complet Markdown et sa structure JSON, le supplément T1, les notes du noyau nul et de la forme présymplectique déjà contrevérifiées au tour précédent, le verdict livré, et les deux évaluations fournies le 7 septembre. La contrelecture antérieure incluait une reconstruction ADM indépendante exécutée sur 128 jeux de composantes. Ce tour ne prétend pas avoir rejoué tous les solveurs spectraux : il ajoute des contre-exemples élémentaires exécutés dans `review_counterchecks.py/.json` et une vérification analytique de la couverture vectorielle massive.

**Aucun contre-exemple physique nouveau au T1 générique n'a été identifié. Le manuscrit doit cependant devenir autonome sur ce test et préciser deux formulations de domaine.** Les résultats de longueur, masses et résidus restent des résultats conditionnels d'un modèle classique. La présente lecture ne certifie ni la nouveauté, ni une acceptation éditoriale, ni DDF complète.

## P1 — Intégrer le cône nul dans le manuscrit soumis

La section 4 saute du choix de jauge scalaire à une phrase sur les contraintes tensorielles, puis au problème spectral. La phrase « avoids introducing a spurious exception for null four-momentum » est insuffisante et mal choisie : la dégénérescence de la décomposition à p²=0 est réelle. La nouvelle preuve la résout ; elle ne la rend pas fictive.

Le supplément contient les éléments qui manquaient : vraie base nulle, jonctions sans trace, famille générale de solutions, normage covariant/ADM avec coins, embeddings et quotient. Pour un article autonome, ajouter une sous-section 4.2 résumant les hypothèses et le résultat, puis un appendice B contenant la preuve. L'appendice de reproduction actuel devient C. Retirer du supplément la mention d'un manuscrit non régénéré lorsque l'intégration a été effectuée, ou le remplacer par un renvoi explicite vers la version consolidée pour éviter deux textes normatifs concurrents.

Dans le texte scientifique, employer « no additional propagating scalar null mode » ou « absence of propagating ghosts in the stated linear domain » plutôt qu'un code couleur GREEN. Le code T1 peut rester dans le registre et le lanceur.

## P1 — Limiter correctement l'absence de contribution de bord à la norme massive

La phrase « The stated boundary terms contribute no four-dimensional derivatives » doit être limitée au représentant de bords fixes et de décalage nul utilisé pour les modes massifs. Le nouveau contrôle montre précisément qu'un coin GHY/angle ADM non nul est nécessaire lorsque delta g_ty n'est pas nul. Généraliser la phrase à toute perturbation reproduirait le défaut que le T1 vient de corriger.

Écrire que les potentiels U_i ne possèdent pas de dérivée temporelle intrinsèque, et que le coin GHY s'annule dans le représentant massif b=0 ; il est conservé dans le traitement nul avant toute décision de jauge. La formule N_f reste inchangée.

## P1/P2 — La borne supérieure sur h ne définit pas à elle seule le domaine de l'événement

La section 7 dit : « For a trial h in the local regular domain h<Lambda5/(6B), the scalar event F=0 selects the endpoint ». La qualification « local » limite déjà l'intention, mais l'inégalité affichée ne garantit que la réalité et la non-annulation de la pente centrale. Elle ne garantit pas un événement scalaire positif.

Sur la continuation monotone issue de la branche principale, F(0)<0 exige aussi

\[
\frac{\Lambda_5-2\lambda^2v^2}{6B}<h<\frac{\Lambda_5}{6B}.
\]

Ce sont les deux conditions centrales nécessaires. Le texte peut se limiter à un voisinage régulier de h=0 où l'événement est positif et transversal, sans revendiquer de théorème global d'existence à partir de ces bornes.

Contre-exemple à la lecture trop large : pour les paramètres de Table 4, h=-1 satisfait la borne supérieure 0,001875, mais sigma'_c=3,4673477 dépasse 2 lambda v=0,3. F(0)>0. La borne inférieure centrale vaut -0,005625. Les calculs locaux publiés à très petites détunes restent à l'intérieur et ne sont pas invalidés.

La dérivée de (26) est exacte à l'ordre linéaire dans la troncature classique ; la formule pour h_b à détune finie comporte explicitement O(delta tau²). Ne pas la rétrograder en simple ajustement numérique ni l'étendre à un résultat non linéaire.

## P2 — Expliquer le comptage vectoriel et tensoriel massif

Le nouveau T1 traite correctement les composantes supplémentaires du cône nul. Pour p² non nul, une phrase supplémentaire doit expliquer pourquoi la discussion scalaire et tensorielle couvre la gravité propagative sans tour vectorielle indépendante.

Vérification directe : en jauge gaussienne normale de bulk, en conservant les embeddings, la perturbation vectorielle est h_mu nu=partial_mu V_nu+partial_nu V_mu avec partial^mu V_mu=0. La contrainte mu5 donne Box_4 V'_mu=0. Pour p² non nul, V'_mu=0 ; V_mu s'enlève alors par un difféomorphisme tangentiel résiduel indépendant de y. Les jonctions naturelles ne lui ajoutent pas de cinétique de bord. Les polarisations vectorielles sous rotations spatiales d'un spin deux massif sont déjà contenues dans le tenseur TT quadridimensionnel ; elles ne sont pas une tour vectorielle supplémentaire.

Pour une masse positive, choisir le référentiel de repos : la transversalité impose h_0mu=0 et le tenseur spatial 3x3 symétrique sans trace possède cinq polarisations de norme positive. Les tenseurs sans masse n'en ont que deux, comme établi séparément par T1. Cette distinction évite de présenter un simple contrôle de deux polarisations de graviton comme une preuve pour les cinq polarisations massives.

## P2 — Clarifier les variables rescalées et la portée perturbative

« In units L=B=1 » peut faire croire que le paramètre physique sans dimension B L³ est fixé à un. Une seule unité de masse ne permet pas de fixer indépendamment deux quantités dimensionnées. Les équations classiques utilisées sont en réalité rescalées avec y/L et sigma/sqrt(B). Écrire ces définitions et conserver B L³ comme facteur global de l'action ; il n'entre pas dans les profils classiques réduits, mais ne peut être effacé d'une discussion des corrections quantiques.

Les formules de masse et de résidu rétablissent déjà B et L correctement. Le rayon conventionnel R0=L/pi et les portées de Table 3 sont cohérents avec A=0 aux deux bords symétriques. Le R0=3 micromètres de la dernière colonne est un choix, et non une sortie indépendante. Cette colonne n'est pas une mesure de la première longueur de Compton tensorielle lorsque le warp est non nul.

Préciser que les asymptotiques sont ponctuelles à x et lambda_hat fixés, epsilon vers zéro. Leur utilisation à epsilon fini exige que les corrections affichées et les profils demeurent petits au regard du terme dominant ; les résultats à epsilon=0,53 sont obtenus par le solveur complet de la troncature et ne sont pas remplacés par le développement faible epsilon. Les contrôles de dérivées par rapport à une coupure et les opérateurs de potentiel supplémentaires restent une question EFT distincte. Le texte actuel distingue déjà largement ces points : les conserver sans inventer un seuil universel epsilon<0,1.

## P2 — Rendre explicite la comparaison des longueurs et la limite affine

La suggestion de l'avis favorable concernant la pente centrale est fondée. À l'extremum plat, H=cosh u+a sinh u=zeta ; la pente centrale du profil plat vaut 2 lambda v/H=sqrt(2 Lambda5). Elle est donc identique à la pente centrale exacte. Insérer cette égalité avant L<L_flat rend la comparaison autonome.

Les valeurs lambda_hat=0 des tables sont l'action affine U_i=T_i+J_i sigma, avec U_i''=0 et sources non nulles. Elles ne sont pas le modèle quadratique avec lambda=0 et v,tau finis : celui-ci supprimerait la source de stabilisation et ne satisferait pas la branche q non nul. Le paragraphe de section 4 le dit déjà correctement. Pour éviter toute lecture rapide erronée, étiqueter les lignes « affine (0) » et la limite « rigid ». Les formules (19),(22) s'étendent continûment à la Hessienne nulle à fond fixé, et non à un prolongement de la condition de longueur (5) vers lambda=0 à v fixé.

## Les avis reçus : corrections nécessaires

1. **Ancien RED : prémisse dépassée.** Les archives rétractaient déjà ce verdict. Le nouveau T1 ne dépend pas de cette rétraction documentaire et reproduit la norme négative tout en montrant le défaut d'admissibilité. L'avis collé doit être actualisé, et non adopté comme preuve qu'un ghost survit.
2. **Borne c_alpha>1/3 : ni présente dans le manuscrit, ni vraie.** Le manuscrit affirme 0<c_infinity<=c_alpha<=c0. À x=4 : c0=0,1703647825 et c_infinity=0,1100290844 ; toutes les rigidités intermédiaires donnent donc c_alpha<1/3. Le coefficient de correction c_alpha est distinct du résidu alpha_r. La positivité de c_alpha implique alpha_r>1/3 pour epsilon suffisamment petit à paramètres de forme fixés ; aucune borne non perturbative universelle n'en découle.
3. **Signe du poids de bord erroné dans l'avis collé.** La condition correcte est eta_i W_i+2 lambda_i>0, pas eta_i W_i+2 eta_i lambda_i>0. Avec x=2, eta0=-1 et lambda_hat=20, les expressions valent respectivement +41,5231883 et -38,4768117. Le manuscrit utilise le bon signe.
4. **W0<0<WL est analytique.** À droite du centre, sigma'>0, sigma>0 et A'<0 donnent sigma''=mu²sigma-4A'sigma'>0 ; la réflexion donne le signe gauche. L'avis ne doit pas le qualifier de contrôle seulement numérique.
5. **Non-applicabilité bibliographique absolue : prescription excessive.** Des fonds/potentiels différents n'annulent pas les méthodes générales ni les précédents sur la réponse au vide. Ne pas remplacer les comparaisons prudentes actuelles par « leur résultat ne s'applique pas à notre cas » sans identifier un énoncé précis et ses hypothèses. L'article reconnaît déjà correctement plusieurs résultats établis.
6. **Avis favorable et nouveauté : pas un certificat.** L'avis revendique des recalculs exhaustifs mais ne joint pas ici leurs programmes ; cette revendication ne remplace pas les preuves et sorties du dépôt. Son indication « aucune erreur » n'interdit pas les clarifications ci-dessus. La nouveauté reste une comparaison bibliographique ciblée puis une évaluation scientifique externe.

## Dernier contrôle adversarial de T1

La preuve livrée n'emploie ni 1/p² ni 1/A'. La branche symétrique garantit q non nul et les poids positifs pour lambda>0 ; le domaine nul n'exige que D_i non nul. X1 échoue à la jonction tensorielle complète, et le déplacement de brane qui annulerait cette composante échoue à la jonction scalaire lorsque qD ne s'annule pas. Le bloc nul est reconstruit, pas seulement testé sur X1. Le tiré-en-arrière des embeddings concerne la même action et ne supprime pas une déformation habillée physique. Les deux voies présymplectiques gardent leurs coins et ont été recollées avec N=Z/2.

La complétion est linéaire, autour du vide matériel et sous conditions sans charges supplémentaires à l'infini spatial. Une théorie de bords dynamiques différente, de nouvelles cinétiques ou un état chargé avec rétroaction exigerait un autre calcul. Ces restrictions doivent rester dans l'appendice et dans la phrase de stabilité du corps du manuscrit. Aucun résultat ici ne justifie « théorie complète viable » comme conséquence du seul test T1.

## Livrables proposés

`PROPOSED_MANUSCRIPT_TEXT.md` fournit les insertions anglaises ciblées : domaine spectral, vecteurs, résumé T1, appendice autonome, comparaison de longueur, domaine courbe et rescaling. Aucun fichier du dépôt actif ni aucun contenu GitHub n'a été modifié par cette contrelecture.
