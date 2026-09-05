# Secteur 5D effectif : modèle, stabilité et résultats

**Modèle du premier manuscrit de recherche.** Les conventions ci-dessous définissent le secteur actif du dépôt. Elles intègrent les corrections du recalcul initial et le développement analytique général. Le détail des démonstrations figure dans [ANALYTIQUE_ET_STABILITE.md](ANALYTIQUE_ET_STABILITE.md); le [manuscrit anglais](../article/manuscript.pdf) les présente avec les résultats et leur contexte bibliographique.

## Action et bords

Signature (-++++), intervalle physique y∈[0,L], orientations s0=-1 et sL=+1 :

\[
S=\int d^4x\,dy\sqrt{-g}\left[\frac{M_5^3}{2}\mathcal R
-\frac12(\partial\sigma)^2-\Lambda_5-\frac12\mu^2\sigma^2\right]
+M_5^3\int_{\partial M}\sqrt{-\gamma}K
-\sum_i\int_i\sqrt{-\gamma}(T_i+J_i\sigma)+S_m[\gamma_0].
\]

La source de matière est minimale sur la brane y=0. Il n'y a ni terme cinétique de brane, ni Einstein induit, ni couplage direct supplémentaire matière–sigma. Aucun autre champ scalaire Phi n'est présent dans cette action. Son ajout, même avec un fond nul, demanderait une vérification des mélanges et des sources.

Avec ds²=e^{2A(y)}ημνdxμdxν+dy² :

\[
A''=-\frac{\sigma'^2}{3M_5^3},\qquad
6M_5^3 A'^2=\frac{\sigma'^2}{2}-\Lambda_5-\frac{\mu^2\sigma^2}{2},
\qquad \sigma''=\mu^2\sigma-4A'\sigma'.
\]

Les jonctions de cette action sur intervalle sont U_i=3s_iM5³A'(y_i) et J_i=-s_i sigma'(y_i), avec U_i=T_i+J_i sigma(y_i). Le coefficient gravitationnel 2M5³ Ricci imprimé dans l'ancien manuscrit A correspond à d'autres coefficients : il appartient à l'historique et ne définit pas les calculs actifs.

## Construction et paramètres de la famille

On définit x=mu L>0 et epsilon=qL/sqrt(12M5³)>0, avec sigma'(0)=sigma'(L)=q. Les unités de calcul sont L=M5³=1. La réflexion combinée à sigma→-sigma impose sigma(L/2)=0 et A'(L/2)=0; A(0)=A(L)=0 fixe les unités physiques aux branes.

Le tir depuis le centre ajuste sigma'(L/2) pour obtenir q au bord. La contrainte fixe alors Lambda5=sigma'(L/2)²/2>0. Les tensions nécessaires suivent des jonctions, T_i=3s_iM5³A'(y_i)-J_i sigma(y_i). Le potentiel évalué au bord U_i doit être distingué du terme constant T_i.

En changeant x ou epsilon, certains paramètres de l'action reconstruite changent. Il s'agit d'une famille de fonds définis ainsi, pas d'une variation du rayon à toutes les constantes d'une seule action fixées. Les sections 4D sont Minkowski : aucune énergie noire observée n'est dérivée.

La branche est définie tant que le fond reste régulier sur l'intervalle. Sur sa moitié droite, sigma>0, sigma'>0, A'<0 et W=sigma''/sigma'>0; la réflexion donne W(0)<0<W(L). Le profil hyperbolique sans rétroaction est une approximation faible, non une solution exacte du système couplé.

## Fluctuations et normalisation physique

Pour les modes scalaires, dans la jauge à branes fixes indiquée dans [DERIVATION_COUPLAGE.md](DERIVATION_COUPLAGE.md), poser W=sigma''/sigma' :

\[
f''+(2A'-2W)f'+(4A''-4A'W+m^2e^{-2A})f=0,
\qquad s=-3M_5^3\frac{f'+2A'f}{\sigma'}.
\]

Aux deux bords :

\[
W(f'+2A'f)-m^2e^{-2A}f=0.
\]

Cette formulation ne divise pas par A' au centre. Elle exige sigma' non nul. Le point epsilon=0 et les autres limites dégénérées doivent être étudiés avec leurs équations propres.

La norme issue de l'action et la masse de Planck effective sont

\[
N_n=\int_0^L e^{2A}\left(3M_5^3f_n^2+\frac{s_n^2}{2}\right)dy,
\qquad
\overline M_{\rm Pl}^2=M_5^3\int_0^L e^{2A}dy.
\]

La cinétique canonique vaut Z_n=2N_n. Pour une source minimale sur la brane y=0, le couplage canonique et l'amplitude de Yukawa sont

\[
g_n=\frac{f_n(0)}{\sqrt{2N_n}},\qquad
\alpha_{s,n}=2\overline M_{\rm Pl}^2g_n^2
=\frac{\overline M_{\rm Pl}^2f_n(0)^2}{N_n}.
\]

Les amplitudes alpha sont définies relativement au potentiel tensoriel sans masse, avec G_T=1/(8 pi Mbar_Pl²). Si un scalaire contribue encore à la distance de mesure de G, ce raccord expérimental doit être réévalué.

Les méthodes de normalisation et de couplage pour fonds généraux ont une antériorité explicite, notamment [Kofman–Martin–Peloso](https://arxiv.org/abs/hep-ph/0401189). Le résultat présent est leur application cohérente aux conventions et au modèle étudiés; voir [l'analyse d'antériorité](../audits/ANTERIORITE_ARTICLE1.md).

## Preuves de stabilité linéaire du modèle retenu

Poser Q=e^{2A}f et définir

\[
p=\frac{e^{-2A}}{\sigma'^2},\qquad
w=\frac{e^{-4A}}{\sigma'^2},\qquad
v=\frac{2e^{-2A}}{3M_5^3}.
\]

L'équation devient -(pQ')'+vQ=m²wQ. Les conditions aux bords donnent Q'=m²e^{-2A}Q/W. L'intégration par parties conduit à

\[
m^2=
\frac{\int_0^L(pQ'^2+vQ^2)\,dy}
{\int_0^L wQ^2\,dy+
w(L)Q(L)^2/W(L)-w(0)Q(0)^2/W(0)}.
\]

Le numérateur et le dénominateur sont strictement positifs pour tout mode non trivial admissible sur la branche régulière : p,w,v>0 et W(0)<0<W(L). Il n'y a donc ni masse² négative ni mode scalaire nul pour epsilon>0 dans ce secteur. La positivité de sa cinétique est établie séparément par N_n>0. Ce raisonnement est une spécialisation du cadre Sturm–Liouville connu; il ne dépend pas de trouver numériquement toutes les racines.

Pour le secteur tensoriel, h''+4A'h'+m_T²e^{-2A}h=0 avec conditions de Neumann donne

\[
m_T^2=\frac{\int_0^L e^{4A}h'^2\,dy}{\int_0^L e^{2A}h^2\,dy}\ge0.
\]

Le mode sans masse est constant. Les modes massifs ont une norme positive; leurs amplitudes sont alpha_T,n=(4/3) I h_n(0)²/∫e^{2A}h_n²dy, avec I=∫e^{2A}dy. La tour plate d'amplitudes 8/3 et de masses n/R0 est une limite, non une expression exacte pour tout fond.

Ces preuves portent sur les petites perturbations des secteurs scalaire et tensoriel de l'action annoncée. Elles n'établissent pas une stabilité non linéaire ou quantique et ne couvrent pas les champs/opérateurs supplémentaires absents de cette action.

## Développement général à faible rétroaction

Pour x>0 fixé :

\[
m_r^2L^2=\kappa(x)\epsilon^2+O(\epsilon^4),
\qquad
\kappa(x)=4x\tanh(x/2)\operatorname{sech}^2(x/2),
\]

\[
\alpha_r=\frac13[1+c_\alpha(x)\epsilon^2+O(\epsilon^4)],
\qquad
c_\alpha(x)=\operatorname{sech}^2(x/2)
\left[1+\tanh^2(x/2)+\frac{2\tanh(x/2)}{x}\right]>0.
\]

À x=2, kappa≈2,5588000338 et c_alpha≈+0,98342023984, conformément au recalcul antérieur du cas particulier. La positivité concerne la première correction au couplage dans cette famille. Elle ne signifie pas que le couplage est monotone à toute amplitude pour tous les modèles 5D. À rétroaction finie, utiliser les profils et normes calculés.

## Résultats numériques et couverture

Les résultats à x=2 se trouvent dans [RESUME.md](../resultats/RESUME.md) et [spectre_5d.json](../resultats/spectre_5d.json). À epsilon=0,53 : m_r L≈0,850124 et alpha_r≈0,40227. Les deux modes scalaires suivants ont mL≈2,65214 et 4,33035, avec alpha≈0,09157 et 0,02564.

L'[extension numérique](../resultats/extension_x.json) considère x=1 et x=3, chacun à epsilon=0,05 et 0,4, avec trois modes scalaires et trois modes tensoriels massifs par point. Par exemple, à epsilon=0,4, le radion a mL≈0,635686 et alpha≈0,403629 pour x=1; mL≈0,548726 et alpha≈0,354124 pour x=3.

Les résidus de fond et de bords, le raccord de norme et le [contrôle de convergence par éléments finis](../resultats/fem_verification.json) permettent d'évaluer les calculs. La couverture numérique reste finie. La stabilité du secteur repose sur les preuves ci-dessus; l'erreur due aux modes omis dans un signal doit encore être estimée pour l'observable choisie.

Pour la conversion illustrative R0=L/pi=8,2 µm, le point x=2, epsilon=0,53 donne lambda_r≈30,303 µm. La portée du premier mode tensoriel est alors ≈7,675 µm. R0 et le rayon défini par la portée du premier graviton massif diffèrent lorsque la métrique se déforme.

## Signal et rayon

En unités naturelles, la correction au potentiel entre sources sur la même brane est

\[
\Delta_V(r)=\sum_n\alpha_{s,n}e^{-m_{s,n}r}
+\sum_{n>0}\alpha_{T,n}e^{-m_{T,n}r}.
\]

La correction à la force comporte les facteurs (1+m_n r). Une expérience avec masses étendues demande une convolution avec sa géométrie et une analyse des incertitudes/corrélations. La courbe alpha95(lambda) n'est pas une mesure de Delta à r=lambda. Aucune exclusion expérimentale n'est revendiquée dans le premier manuscrit.

R0 reste une entrée dimensionnelle. L'équation x=mu L donne R0=x/(pi mu) en unités naturelles : prédire R demande de fixer mu et les autres paramètres indépendamment. Le raccord de cette action à la géométrie DDF demeure ouvert.


