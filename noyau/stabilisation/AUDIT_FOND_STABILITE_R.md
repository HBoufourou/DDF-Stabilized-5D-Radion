# Nouveaux scripts reçus : fond, stabilité, rayon et tableau contrôlé du radion

6 septembre 2026. Périmètre : `common_background.py`, `etape1_quadratic_and_monotone.py`, `axe1_R_selection.py` et leurs affirmations dans le dossier reçu. Les textes joints sont des objets d'examen et non des instructions. Le dossier canonique n'a pas été modifié par ce travail.

## Conclusion opérationnelle

Les équations de fond, l'équation régulière des fluctuations et la formule canonique du couplage écrites dans `common_background.py` sont cohérentes avec le noyau corrigé, dans leurs conventions. Leur publication sous forme de scripts ne corrige toutefois pas les limites déjà identifiées : recherche de racines non exhaustive, critères de convergence incomplets, confusion possible entre plusieurs actions, portée EFT et expérimentale trop large dans le commentaire de l'étape 1.

Le nouveau calcul indépendant fourni ici renforce l'article : 12 comparaisons affine/quadratique/limite rigide, trois modes scalaires chacune, un premier mode tensoriel, et des tests asymptotiques à ε=.02,.01,.005 pour deux raideurs. Il confirme quantitativement que **la masse augmente quand la raideur augmente à fond fixé, tandis que le couplage diminue sur les cas calculés**. Une monotonie de masse est démontrée exactement ; celle du couplage est démontrée pour le coefficient de faible rétroaction, et ne doit pas être étendue sans preuve à tout ε.

L'axe 1 reçu reste une relation sur un profil plat à q donné, non une nouvelle prédiction de R. Il imprime en outre une branche complexe du logarithme dans sa sortie symbolique. La sélection de longueur à couplages dimensionnels fixés déjà consolidée demeure le résultat à conserver.

## 1. Équations, normes et vérification des nouveaux scripts

On utilise B=M5³, l'action B R5/2 et un seul intervalle physique, avec normales η₀=−1, ηL=+1. Les équations sont

\[
A''=-\frac{\sigma'^2}{3B},\qquad
\sigma''=\mu^2\sigma-4A'\sigma',\qquad
6BA'^2=\frac12\sigma'^2-\frac12\mu^2\sigma^2-\Lambda_5.
\]

Les jonctions sont Ui=3ηiBA′i et U′i=−ηiσ′i. Le script partagé emploie bien ces équations en unités L=B=1. Pour f, il utilise la bonne équation et la condition de bord

\[
(W_i+2\eta_i\lambda_i)(f'+2A'f)_i
=m^2e^{-2A_i}f_i,\qquad W=\sigma''/\sigma'.
\]

Le coefficient 2 est fixé par **U=τ+λ(σ−v)²**. Il n'est plus « à fixer dans le manuscrit ». Un autre coefficient devant le carré ou une autre action d'orbifold exige une conversion des conventions, pas une ambiguïté dans ce modèle.

La formule de `coupling` est également correcte pour B=1 et la source à y=0 normalisée A₀=0 :

\[
\alpha=\frac{I f_0^2}{N},\quad
I=\int e^{2A}dy,\quad
N=\int e^{2A}\left(3f^2+\frac{s^2}{2}\right)dy,
\quad s=-\frac{3(f'+2A'f)}{\sigma'}.
\]

En unités générales, le numérateur est Mbar_Pl² f₀², avec Mbar_Pl²=B I. La cinétique canonique est Z=2N ; aucun changement de cette convention n'est justifié par la nouvelle archive.

### Fragilités du calcul joint, à ne pas confondre avec une erreur des équations

- Le tir `fsolve` ne demande pas le drapeau de convergence ni un test obligatoire des résidus finaux. Les avertissements sont supprimés globalement. La réussite de `solve_ivp` et la contrainte ne sont pas exigées avant d'évaluer un spectre.
- `solve_mode` n'exige pas non plus la réussite de l'intégration. La division par W₀−2λ présuppose que cette quantité ne s'annule pas.
- La variable parcourue par `spectrum` est **m²**, bien que ses noms `m` et `mmax` suggèrent parfois m. Le balayage positif commence à 10⁻⁴, se termine à une valeur finie, conserve les changements de signe et applique un filtre arbitraire sur leur taille. Il peut rater des modes très légers ou des racines ; il ne démontre aucune absence de tachyon et ne garantit pas qu'il a trouvé les trois premiers modes.
- La grille contient deux fois certains points de raccord. Une racine exactement sur un point de grille pourrait être comptée deux fois sans déduplication explicite. Les exceptions ignorées peuvent masquer un échec local.

Ces observations ne prouvent pas que les valeurs effectivement imprimées sont fausses. Le nouveau calcul variationnel ci-dessous les contrôle par une autre discrétisation, avec produit scalaire de bord explicite et raffinement.

Le rejeu direct de `etape1_quadratic_and_monotone.py` a été tenté après lecture. Dans l'environnement de cette sous-tâche, il s'est arrêté avant le calcul sur `ModuleNotFoundError: No module named 'scipy.integrate'`, malgré le chemin du runtime nouvellement installé. Ce statut n'est pas un échec physique du modèle. Les résultats numériques de cette note proviennent du nouveau solveur NumPy, intégralement exécuté. Un éventuel rejeu réussi par le processus principal doit être enregistré séparément.

## 2. Preuve de stabilité et monotonie exacte de la masse

Posons g=e^(2A)f et

\[
p=\frac{e^{-2A}}{\sigma'^2},\quad
w=\frac{e^{-4A}}{\sigma'^2},\quad
Q=\frac{2e^{-2A}}{3B},\quad B_i=\eta_iW_i+2\lambda_i.
\]

L'énergie et le produit scalaire spectral sont

\[
K[g]=\int(p|g'|^2+Q|g|^2)dy,
\qquad D[g]=\int w|g|^2dy+\sum_i\frac{w_i|g_i|^2}{B_i}.
\]

Si le fond est régulier, σ′ ne s'annule pas et **B_i>0**, alors K=m²D impose m² réel strictement positif. La norme physique vaut N=(9B²/2)K. Sur la branche symétrique à q>0, μ>0, on a W₀<0<WL ; tout λ≥0 satisfait donc ces conditions. La positivité ne dépend pas d'un balayage numérique.

Le critère imprimé avec « ≥0 » demande une réserve : à B_i=0, cette forme à poids de bord n'est plus définie. Les conditions originales doivent être examinées sans division ; la preuve strictement positive ne se transporte pas à ce point dégénéré. Le point σ′=0 est lui aussi hors du domaine de la variable régulière choisie.

À **fond fixé**, avec la même raideur λ aux deux bords, K ne change pas tandis que D diminue lorsque λ augmente. Pour un mode simple, la formule de Hellmann–Feynman donne

\[
\boxed{\frac{d m_n^2}{d\lambda}
=\frac{2m_n^2}{D[g_n]}
\sum_i\frac{w_i|g_n(y_i)|^2}{B_i^2}>0.}
\]

Pour une raideur finie dans ce domaine, un mode non trivial ne peut s'annuler à un bord : sa condition de bord imposerait aussi sa dérivée nulle. L'inégalité est donc stricte. Le principe min–max donne aussi l'ordre global des valeurs propres. La limite λ→∞ donne le problème régulier à g′=0, avec poids de bord nul ; sa masse reste finie. **λhat=20 n'est pas cette limite**, même si les résultats s'en rapprochent.

La formule de α comporte en plus le profil au bord. Aucune monotonie générale de α ne suit de ce raisonnement. Le tableau ci-dessous donne d'ailleurs un contre-exemple à « alourdir le radion augmente son couplage » : à ε=.30, passer de l'affine au quadratique λhat=1 augmente mL de .483691 à .537838 mais réduit α de .359838 à .356075.

## 3. Tensions : valeurs physiques, constantes et trajectoires d'action

La distinction de l'avis adverse est conservée. Sur la branche symétrique, A′₀>0>A′L, donc les deux **valeurs physiques** Ui=3ηiBA′i sont négatives. À fond fixé, elles ne changent pas avec la raideur.

Pour les bords affines Ui=Ti+Jiσ, on reconstruit Ji=−ηiq et Ti=Ui−Jiσi. Les Ti peuvent être positifs ; les appeler automatiquement « tensions nues négatives » serait faux.

Pour les bords quadratiques,

\[
v_i=\sigma_i+\frac{\eta_iq_i}{2\lambda_i},\qquad
\tau_i=U_i-\frac{q_i^2}{4\lambda_i}.
\]

Les τi symétriques sont alors strictement négatifs et inférieurs aux Ui. À q_i et fond fixés, augmenter λi les fait **remonter** vers Ui, puisque dτi/dλi=q_i²/(4λ_i²)>0. Cela ne répare pas le signe physique de Ui.

Le tableau affine/quadratique conserve le même fond en modifiant les vi et τi selon ces formules. Il compare donc des actions numériquement différentes. À λ→0 avec q fixé, vi et τi divergent : l'affine est une famille de référence séparée, ou une limite singulière avec soustraction de constantes. Ce n'est pas la limite λ→0 à v fini, dans laquelle le stabilisateur de brane disparaît. Le manuscrit unifié peut montrer les deux familles sans les identifier abusivement.

## 4. Branche monotone : résultats conservables et contre-exemple au passage à la limite

Pour la construction jointe,

\[
A'(0)=-a_0<0,\quad \sigma'(0)=q>0,
\quad\sigma(0)=-\frac{4a_0q}{\mu^2}-\Delta,
\quad W_0=-\frac{\mu^2\Delta}{q}.
\]

A′ reste négatif tant que le fond existe, car A″≤0. En revanche, σ′>0 partout et WL>0 ne sont pas garantis par les seules données initiales : ils doivent être établis sur chaque solution. Pour Δ>0, B₀=−W₀ est positif dans le cas affine. Les énergies physiques satisfont U₀=3Ba₀>0 et UL<0. Une constante quadratique τ₀ pourrait pourtant être négative si le terme q²/(4λ) dépasse U₀ ; « brane positive » doit préciser qu'il s'agit de U₀.

Le nouveau code réintègre les douze points de l'archive, avec 2048 puis 4096 pas. Trois atteignent L=1 dans le domaine régulier attendu : ε=.30, Δ=.20 et a₀=.02,.10,.20. Leurs données omises dans la synthèse initiale sont importantes :

| a₀ | Λ5 | U₀ | UL | σL/M5^(3/2) | qL/q₀ | A(L) |
|---:|---:|---:|---:|---:|---:|---:|
| .02 | .440108 | +.06 | −7.349499 | 1.888209 | 8.983613 | −.397863 |
| .10 | .295262 | +.30 | −9.023876 | 1.918325 | 10.710162 | −.502412 |
| .20 | −.032677 | +.60 | −11.970552 | 1.987085 | 13.837265 | −.641245 |

Les variations relatives de qL entre les deux résolutions sont inférieures à 6×10⁻¹¹ et les résidus de contrainte finaux restent sous 5×10⁻¹¹ pour ces trois cas. Ces valeurs confirment le fond, pas la protection de son potentiel : σL dépasse l'échelle de champ gravitationnelle et la pente au bord droit est multipliée par 9 à 14. La troisième solution a Λ5<0 ; elle n'appartient donc pas au domaine positif de la branche symétrique principale.

Pour les neuf autres cas, l'intégration atteint un seuil d'amplitude fixé avant L=1. Le code le signale comme un arrêt numérique de cette trajectoire, et non comme un théorème de non-existence pour toute une région de paramètres. Les trois spectres monotones anciens ne sont pas recalculés ici ; la nouvelle table d'article porte sur le domaine symétrique contrôlé.

La phrase « a₀→0 donne la moitié droite du fond symétrique » est **fausse à Δ fixé non nul**. Le contre-exemple Δ=.20 conserve σ(0)=−.20 et W₀=−.769800 à ε=.30 ; ni σ(0) ni W₀ ne s'annule. Pour retrouver le centre de réflexion, il faut aussi Δ→0, et redéfinir la longueur si l'intervalle est une demi-branche. À λ=0, B₀ tend alors vers zéro : cette limite est précisément exclue de la preuve de positivité à poids de bord fini.

## 5. Axe 1 : une identité de jonction plate, avec la bonne branche réelle

Le profil hyperbolique du script résout l'équation de σ **sans rétroaction**. Avec q pris comme donnée et U=τ+λ(σ−v)², la condition droite donne

\[
z=\frac{\mu v}{q}-\frac{\mu}{2\lambda},\qquad
L=\frac{2}{\mu}\operatorname{artanh}z,
\qquad \boxed{0<z<1.}
\]

La condition complète à raideur finie inclut donc 2λv>q, ainsi que la borne supérieure z<1. La limite rigide L=(2/μ)artanh(μv/q), avec 0<μv/q<1, est correcte dans ce problème plat à q fixé.

La sortie jointe imprime cependant `2*log(-sqrt(...))`. Dans le domaine réel positif, le signe moins place le logarithme sur une branche complexe. Par exemple μ=1, λ=.5, v=.3, q=.2 donne z=.5 et la solution réelle μL=log3. L'expression imprimée vaut log3+2πi sur la branche principale complexe. Le JSON contient cette vérification sans SymPy. Il faut sélectionner explicitement la solution réelle positive plutôt que le premier élément de `solve`.

Surtout, q n'est pas une constante indépendante du potentiel quadratique fixé. Les paramètres de l'action sont μ, λ, v, Λ5, τ et M5. La contrainte et les jonctions fixent q et L ensemble. Le résultat à conserver dans le noyau, déjà démontré, est :

\[
a=2\lambda/\mu,\quad B_*={\sqrt2\lambda v}/{\sqrt{\Lambda_5}},
\quad L_{\rm plat}=\frac2\mu\log\frac{B_*+\sqrt{B_*^2+a^2-1}}{1+a},
\]

avec 0<Λ5<2λ²v² et compatibilité de la tension pour un vide plat. Avec rétroaction, β=v²/M5³ intervient et la longueur exacte est obtenue par l'événement σ′+2λσ−2λv=0. Sa valeur reste conditionnelle aux couplages. Les nombres de l'axe 1 sont des conversions de **R déjà choisi**, et n'apportent aucune sélection absolue de micromètres.

## 6. Tableau d'article recalculé : R₀=3 μm choisi en entrée

Conventions : x=μL=2, ε=qL/√(12M5³), L=πR₀. Les masses ci-dessous sont mesurées dans les coordonnées physiques du bord y=0, normalisé A₀=0. Pour le potentiel d'échange du radion, V(r)=−G_T m_am_b[1+α_r exp(−r/ℓ_r)]/r, on a ℓ_r=L/(m_rL). Il s'agit de α **dans le potentiel**, pas d'une correction constante de force ; la force comporte en plus 1+r/ℓ_r. Les autres modes doivent être ajoutés lorsqu'ils contribuent.

| ε | Famille de bord | λhat | m_rL | α_r | ℓ_r pour R₀=3 μm |
|---:|---|---:|---:|---:|---:|
| .10 | affine | 0 | .160207966 | .336569452 | 58.828398 μm |
| .10 | quadratique | 1 | .182819029 | .336098739 | 51.552500 μm |
| .10 | quadratique | 20 | .206387319 | .335382388 | 45.665490 μm |
| .10 | limite rigide | ∞ | .209090378 | .335282827 | 45.075140 μm |
| .30 | affine | 0 | .483690816 | .359837939 | 19.485129 μm |
| .30 | quadratique | 1 | .537837539 | .356074963 | 17.523466 μm |
| .30 | quadratique | 20 | .599671485 | .350135357 | 15.716568 μm |
| .30 | limite rigide | ∞ | .607110189 | .349286341 | 15.523999 μm |
| .53 | affine | 0 | .850123905 | .402266532 | 11.086358 μm |
| .53 | quadratique | 1 | .913273271 | .393030956 | 10.319779 μm |
| .53 | quadratique | 20 | .997568727 | .377352763 | 9.447748 μm |
| .53 | limite rigide | ∞ | 1.008673393 | .374980829 | 9.343736 μm |

À x, ε et λhat fixés, changer seulement le rayon de référence multiplie ces portées par R₀/(3 μm) et divise les masses physiques par le même facteur ; α ne change pas. Cette mise à l'échelle compare des actions dimensionnelles différentes. Elle ne permet pas de changer L tout en prétendant que tous les coefficients dimensionnels demeurent fixés.

Le gain réellement asymptotique entre l'affine et le bord rigide vaut **30,51 %**, **25,52 %**, **18,65 %** pour ε=.10,.30,.53. Les « +24 % » et « +17 % » de l'archive correspondent approximativement à λhat=20, et ne doivent pas être appelés gains maximaux.

La portée du premier tenseur calculé vaut respectivement 2.990594, 2.924379 et 2.808064 μm. Elle diffère de R₀ lorsque le fond est déformé. Le rapport m_rL/π imprimé dans l'ancien script est un rapport à la masse KK **plate**, pas au premier tenseur exact. Le JSON fournit ce dernier rapport sans cette approximation.

Ce tableau ne définit aucune fenêtre expérimentale « confortable ». Sans fonction de réponse et ajustement expérimental, il ne montre ni exclusion de 8,2 μm ni validation universelle de 1–5 μm. Les nombres de champ demeurent également des entrées du contrôle EFT : σb/M5^(3/2)=.131181, .378164, .620743 et A_c=.00246529,.02007230,.05212303 pour les trois ε. Un faible A ne protège pas à lui seul le potentiel quadratique.

## 7. Nouveau contrôle spectral du coefficient quadratique faible rétroaction

La simplification analytique proposée dans cette étape est vérifiée indépendamment par le spectre, sans fournir ses coefficients au solveur. Pour C=cosh²(x/2), S=sinh x et d=x tanh(x/2)+2λhat,

\[
\kappa=\frac{4d}{1+dS/(2x)},\qquad
\boxed{c_\alpha=\frac{1+S/x}{C}
-\frac{C\kappa^2}{16x^2}(S/x-1).}
\]

Les définitions asymptotiques sont m_r²L²=κε²+O(ε⁴) et 3α_r−1=c_α ε²+O(ε⁴), pour **x et λhat fixés**. La dérivation de profils complète est donnée dans le document analytique du processus principal ; ici le contrôle est spectral.

Cette expression reproduit l'affine λhat=0. Comme S/x−1>0 et κ augmente avec λhat, c_α diminue à cet ordre. Sa limite est

\[
c_\infty=\frac{4[\cosh x-\sinh(x)/x]}{\sinh^2x}>0.
\]

La positivité suit de x cosh x−sinh x>0 pour x>0, dont la dérivée vaut x sinh x. Par conséquent 0<c_∞≤c_α≤c_affine pour λhat≥0. Ce résultat porte sur un coefficient asymptotique ; il ne prouve pas à lui seul une monotonie du couplage exact à toute rétroaction.

| λhat | ε | m_r²L²/ε² calculé | (3α_r−1)/ε² calculé |
|---:|---:|---:|---:|
| 1 | .020 | 3.359086868 | .839528553 |
| 1 | .010 | 3.359617709 | .839843594 |
| 1 | .005 | 3.359750473 | .839922408 |
| 1 | limite analytique | 3.359794733 | .839948683 |
| 20 | .020 | 4.295850561 | .622353836 |
| 20 | .010 | 4.297003212 | .622597002 |
| 20 | .005 | 4.297291558 | .622657837 |
| 20 | limite analytique | 4.297387689 | .622678119 |

En divisant ε par deux, les écarts à la limite sont divisés par un facteur compris entre 3,9977 et 3,9997 pour ces tests. C'est le comportement O(ε²) attendu pour les coefficients extraits. Il s'agit d'un contrôle plus exigeant qu'un seul accord à ε=.30.

## 8. Méthode numérique nouvelle et réponse à l'avis sur l'article

`radion_comparison.py` est portable et utilise seulement NumPy et la bibliothèque standard. Il réintègre les fonds par RK4 depuis leur centre de réflexion, avec 4096 puis 8192 pas par demi-intervalle. Les contraintes des fonds symétriques restent sous 1,5×10⁻¹⁴ et les variations de A entre les deux résolutions sous 3×10⁻¹⁶. L'accord au niveau de l'arrondi n'est pas interprété comme un ordre de convergence mesuré.

L'opérateur scalaire utilise une base de Legendre complète dans H¹, avec 20,32,48 fonctions et 256,384,512 points de Gauss. Les matrices incluent les poids spectraux de bord. La petite valeur propre est affinée par un complément de Schur du bloc pair, sans série analytique injectée : cela évite la perte relative de précision quand ε tend vers zéro. La norme physique est intégrée sous sa forme positive, sans soustraction de grandes contributions d'une matrice de différences.

Les trois modes conservés à chacun des douze points varient de moins de 3,2×10⁻¹² relativement entre les deux dernières bases, pour masses et α. À ε=.30, les comparaisons aux anciens résultats FEM sélectionnés sont inférieures à 1,4×10⁻¹¹ relativement. Le cas affine ε=.53 est aussi comparé au tir antérieur de haute précision. Ces accords testent les calculs ; ils ne constituent pas une preuve de nouveauté scientifique ou une validation expérimentale.

Réponse aux points pertinents de `AVIS_ARTICLE1.md` :

- **Conventions et norme :** conservées ; aucun retour au coefficient d'Einstein historique ou au c_α négatif rétracté. La norme K est explicitement distinguée du produit scalaire D, et Z=2N reste fixé.
- **Preuve plutôt que balayage :** la positivité est donnée avec σ′≠0 et B_i>0. Les points dégénérés ne sont pas absorbés dans un « ≥0 » imprécis. La monotonie de masse avec raideur est ajoutée avec sa trajectoire exacte de paramètres.
- **Familles et tensions :** U_i, T_i et τ_i sont séparés ; le passage affine/quadratique est une comparaison d'actions reconstruites. La sélection de L à action fixée reste un autre problème, déjà résolu conditionnellement dans le noyau.
- **Contenu d'article :** le noyau quadratique peut désormais être présenté avec un coefficient analytique compact, ses bornes en raideur, le contrôle faible ε et le tableau à rétroaction finie. L'affine sert de limite de comparaison explicitement nommée. Cette combinaison renforce l'étude de cas ; elle n'établit pas une priorité générale sur la stabilisation ou les méthodes spectrales.
- **Limites physiques :** origine des énergies de bord, protection des potentiels, raccord UV, origine indépendante des couplages dimensionnels, choix de la courbure cosmologique et confrontation instrumentale restent à déclarer. Une même publication peut résoudre le problème classique qu'elle définit sans prétendre avoir résolu ces questions.

Le résultat utile de cette archive est donc l'explicitation de certains calculs, complétée ici par des contrôles et dérivations plus solides. Elle ne justifie pas de remplacer le noyau canonique par ses anciennes conclusions de rayon validé, de domaine EFT garanti ou de monotonicité universelle des couplages.

## Fichiers reproductibles

- `radion_comparison.py` et `radion_comparison.json` : nouvelles solutions, table physique conditionnelle, comparaisons, bornes et contrôles asymptotiques.
- `input_data/quadratic_fem.json` et `input_data/spectre_5d.json` : références numériques auditées ; leurs scripts ne sont pas exécutés et aucune formule analytique n'est utilisée comme oracle spectral.
- `original_replay_status.json` : statut précis du rejeu original dans cette sous-tâche.

Exécution : `python radion_comparison.py --radius-um 3`. Le choix de rayon peut être modifié explicitement ; il reste une entrée de comparaison.

## Complément du contrôle de livraison

Le coordinateur a ensuite réexécuté le script original de l’étape 1 avec SciPy. Il termine sans erreur et retrouve les nombres à la précision affichée ; sa sortie manquante a été sauvegardée. La valeur de référence .483724 imprimée dans le script est incohérente avec son propre résultat .483691 pour ε=.3. Le rapport final est `audits/REJEU_SCRIPTS_RECUS.json` à la racine. Le contrôle Galerkin a également été rejoué par le lanceur canonique avec comparaison des JSON.
