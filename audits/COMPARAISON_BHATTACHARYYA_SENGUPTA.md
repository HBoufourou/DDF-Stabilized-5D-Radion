# Comparaison ciblée avec Bhattacharyya–SenGupta (2025)

Contrôle du 6 septembre 2026, limité au texte primaire et à ses sections utiles pour le premier article. Référence : Soham Bhattacharyya et Soumitra SenGupta, *Analyzing the general conditions for modulus stabilization in a warped braneworld*, Eur. Phys. J. C **85**, 1430 (2025), publication le 16 décembre 2025. [Texte intégral et métadonnées](https://link.springer.com/article/10.1140/epjc/s10052-025-15170-1). Entrée BibTeX : `BhattacharyyaSenGupta2025`. Aucun identifiant arXiv n'est ajouté faute de vérification.

## 1. Cartographie du précédent

| Passage primaire | Portée pertinente |
|---|---|
| §§2–3, (2.6), (3.2)–(3.5) | Analyse principale sur AdS RS-I fixé ; bord UV Dirichlet, bord IR linéaire ; perturbations singulières CMS. |
| §4.5, (4.26)–(4.29), annexe A | Exemple BFG avec rétroaction exacte, superpotentiel et bords reconstruits ; ce potentiel n'est pas notre quadratique convexe. |
| §§5–6, (6.3), (6.6) | Conditions approchées de stationnarité et de courbure positive du potentiel du radion, sous les conditions de bord imposées. |
| Fin §6 | Couplage canonique RS usuel via la valeur stabilisée ; aucune formule de notre coefficient c(x,λ̂) identifiée. |
| §7 | Contraintes de somme sur la longueur, sans notre théorème d'existence et d'unicité du bord. |

La citation convient pour situer l'étude des conditions de stabilisation. Il serait incorrect d'affirmer que cet article ignore partout la rétroaction. [Sections citées](https://link.springer.com/article/10.1140/epjc/s10052-025-15170-1).

## 2. Ce que notre comparaison doit effectivement porter

Notre action fixe V=Λ5+μ²σ²/2, avec Λ5>0 et μ²>0, et deux potentiels réfléchis U0=τ+λ(σ+v)², UL=τ+λ(σ−v)². La branche plate a un maximum intérieur du warp, un scalaire impair et des conditions de Robin de raideur finie. Le fond et les perturbations sont obtenus dans le système Einstein–scalaire couplé. La référence précédente ne doit pas remplacer la démonstration de nos jonctions, de l'existence du bord ou de la norme canonique.

La présence du même monôme μ²σ²/2 ne rend pas deux problèmes identiques : le terme constant total, le signe de la courbure de fond, les deux potentiels de bord et la prescription de variation sont également des données physiques. Une contradiction ou une identité des résultats ne peut être déduite d'une simple comparaison des signes de μ².

Le résultat d'existence que notre manuscrit doit énoncer est conditionnel à la branche et aux paramètres de l'action. Il doit séparer l'intersection avec la condition scalaire du bord et la compatibilité gravitationnelle qui fixe la tension plate. Ce résultat ne prédit pas une longueur micrométrique sans les paramètres dimensionnels.

## 3. Nouvelle expression à présenter et limites de sa portée

Ce paragraphe porte sur le calcul DDF communiqué pendant cette relecture, et non sur une expression attribuée à Bhattacharyya–SenGupta. Avec x=μL>0, λ̂=λL≥0, S=sinh x et C=cosh²(x/2), définir

\[
d=x\tanh(x/2)+2\widehat\lambda,
\qquad
\kappa=\frac{4d}{1+dS/(2x)}.
\]

Le coefficient proposé pour le couplage normalisé est

\[
c(x,\widehat\lambda)=\frac{1+S/x}{C}
-\frac{C\kappa^2}{16x^2}\left(\frac{S}{x}-1\right),
\qquad
\alpha_r=\frac13[1+c\epsilon^2+O(\epsilon^4)].
\]

Le manuscrit doit définir précisément ε et conserver cette convention dans ses données. Les expressions ci-dessous sont des conséquences algébriques de cette formule ; elles ne remplacent pas sa dérivation depuis la norme du mode.

À x fixé,

\[
\partial_{\widehat\lambda}\kappa=
\frac{8}{[1+dS/(2x)]^2}>0,
\]

\[
\partial_{\widehat\lambda}c=
-\frac{C\kappa}{8x^2}\left(\frac Sx-1\right)
\partial_{\widehat\lambda}\kappa<0.
\]

La limite rigide donne κ∞=8x/S et

\[
c_\infty(x)=\frac{4(\cosh x-\sinh x/x)}{\sinh^2 x}>0,
\qquad
0<c_\infty\le c(x,\widehat\lambda)\le c(x,0).
\]

La positivité suit de x cosh x−sinh x>0 : cette fonction s'annule en zéro et sa dérivée vaut x sinh x>0. La borne supérieure est le contrôle spectral affine λ̂=0 ; passer à cette limite dans une action quadratique à source affine non nulle nécessite de conserver la source, et non de simplement annuler λ à v fixé.

Ces bornes portent sur le coefficient du développement faible, à x fixé. Elles ne prouvent ni une monotonie non perturbative de αr pour toute rétroaction, ni un ordre universel des couplages entre actions dont la longueur change. Le contrôle numérique doit comparer les résidus exacts dans les mêmes conventions et montrer le régime où le reste O(ε⁴) devient négligeable.

## 4. Formulation éditoriale recommandée

Présenter le travail comme une étude du modèle précis : sélection conditionnelle de longueur, stabilité scalaire et tensorielle, et dépendance des résidus à la raideur des bords. Mettre en avant la formule fermée vérifiée et ses bornes comme résultats de ce calcul, sans « première preuve », « nouvelle loi générale » ou revendication d'une priorité établie.

Cette comparaison ciblée ne relève pas de duplication directe de ces expressions dans les passages examinés ; elle ne constitue pas une recherche d'antériorité exhaustive. Les références Kofman–Martin–Peloso et Olechowski restent nécessaires pour reconnaître respectivement le cadre du couplage avec rétroaction et les critères spectraux avec termes de bord. La comparaison avec Lüst–Nee–Randall reste distincte et utile pour les bords quadratiques et la réponse à une variation de tension.
