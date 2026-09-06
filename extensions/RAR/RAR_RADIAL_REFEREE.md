# Relecture ciblée du problème radial RAR

6 septembre 2026. Périmètre : `rar_radial_bvp.py` et solutions du JSON, avec source de Plummer prescrite, densité du condensat non résolue, condition extérieure imposée. Aucune modification du solveur. La validité de l'EFT sur le domaine reste une hypothèse.

## Verdict sur le Jacobien

Les dérivées du code sont correctes. Posons c=χ et

\[
b=\frac{h}{1+c^2}+\frac{2c^2h^3}{9},\qquad
F(h,c)=h^2cQ,\qquad Q=-\frac1{(1+c^2)^2}+\frac{h^2}{9}.
\]

À masse enfermée prescrite, donc à b(s) fixé,

\[
\mu_L=\frac{\partial b}{\partial h}
=\frac1{1+c^2}+\frac{2c^2h^2}{3}>0,
\]

\[
h_c=\frac{2ch/(1+c^2)^2-4ch^3/9}{\mu_L},
\]

\[
F_c\big|_h=h^2\left[Q+\frac{4c^2}{(1+c^2)^3}\right],\quad
F_h=2hcQ+\frac{2h^3c}{9},\quad
\frac{dF}{dc}\bigg|_b=F_c\big|_h+F_hh_c.
\]

Pour Δc=F/ell², l'opérateur linéarisé est −Δ+(dF/dc)/ell². En posant u=sδc, le sous-problème radial devient exactement

\[
\mathcal H u=-u''+\frac1{\ell^2}\frac{dF}{dc}\bigg|_b u,
\qquad u(0)=u(S)=0.
\]

La condition à l'origine traduit la régularité de δc, pas une condition δc(0)=0. La condition extérieure fixe δc(S)=0. La discrétisation tridiagonale affichée correspond bien à cet opérateur. Un contrôle indépendant par dérivées finies à cinq points, résolvant le flux par bissection et sans NumPy/SciPy, donne une erreur maximale |D_num−D_an|/max(1,|D_an|)=4,81×10⁻¹¹ sur 30 couples (b,c).

La positivité de μ_L et de μ_T assure seulement l'ellipticité gravitationnelle à c fixé. Elle n'impose pas la positivité du complément de Schur contenant h_c et ne protège donc pas contre les modes négatifs de H.

## Fonctionnelle d'énergie pour comparer les deux branches

Définissons

\[
G(h,c)=\frac{h^2}{1+c^2}+\frac{c^2h^4}{9},\qquad
W(c;b)=G(h(c;b),c)-2b\,h(c;b).
\]

L'équation ∂G/∂h=2b est précisément le flux, et ∂²G/∂h²=2μ_L>0. Sur cette solution, une expression pratique équivalente est

\[
\boxed{W=-\frac{h^2}{1+c^2}-\frac{c^2h^4}{3}.}
\]

L'identité de Legendre donne W_c=2F et W_cc=2(dF/dc)|_b. La fonctionnelle réduite, à un facteur physique global positif près, est

\[
\boxed{\mathcal E[c]=\int_0^S ds\,s^2
\left[\ell^2(c')^2+W(c;b(s))\right].}
\]

Elle a exactement pour équation d'Euler–Lagrange le BVP du code. Son Hessien radial est 2ell² H après passage à u et élimination des termes de bord. Comparer E des deux solutions est donc un test énergétique cohérent, pour **les mêmes A, f, ell, S, condition χ(S) et choix de référence du potentiel gravitationnel extérieur**. Le terme de bord issu de l'intégration de la source gravitationnelle s'annule dans cette différence lorsque cette référence est la même.

Pour réduire le fond commun, on peut calculer ∫s²[ell²(c′)²+W+b²] : le terme ajouté dépend uniquement de la source prescrite et ne change ni l'ordre des énergies ni les équations. Il faut intégrer le profil et sa dérivée issus du solveur sur un maillage suffisamment fin, puis contrôler la différence d'énergie sous raffinement. Une énergie plus basse choisit une branche parmi celles comparées ; elle ne démontre pas le minimum global parmi toutes les solutions, et ne compare pas des halos auto-cohérents puisque leur densité n'est pas résolue.

## Signe négatif : contrôle variationnel indépendant

Sur les branches initiales à cœur presque nul, une fonction test u=sin(πs/a) pour 0<s<a, prolongée par zéro pour a≤s≤S, fournit

\[
\mathcal R[u]=\frac{\pi^2}{a^2}+
\frac2a\int_0^a ds\,\frac{dF/dc}{\ell^2}\sin^2(\pi s/a).
\]

Elle est admissible pour la forme quadratique, malgré le saut de sa dérivée au raccord. Le script indépendant `rar_radial_referee_checks.py` utilise le χ archivé interpolé linéairement et une quadrature de Simpson à 4096 intervalles :

| A | ell | a | Quotient de Rayleigh | Première valeur propre du code |
|---:|---:|---:|---:|---:|
| 10 | 0,1 | 0,45 | −105,9869 | −119,3853 |
| 10 | 0,03 | 0,35 | −1756,9733 | −2138,0830 |

Ces valeurs donnent un contrôle numérique du signe négatif indépendant de la matrice tridiagonale. Ce ne sont pas des bornes certifiées incluant les erreurs du fond et de son interpolation. Leur signe fortement négatif est néanmoins cohérent avec les valeurs propres annoncées et ne dépend pas d'une petite erreur près de zéro.

Le faible champ baryonique au cœur explique le mécanisme : à c=0, h=b et dF/dc=b²(−1+b²/9), négatif pour 0<b<3. Une coquille de plus forte accélération peut séparer ce cœur du domaine externe de χ non nul. La continuation à partir d'une solution presque constante peut donc aboutir à une branche stationnaire au cœur instable. Un profil initial avec bosse centrale positive permet de chercher une autre branche.

## Portée des nouvelles branches

La recherche complémentaire a trouvé des branches à cœur positif pour A=10 : χ(0)≈0,76462 à ell=0,1 et χ(0)≈1,23393 à ell=0,03. La relecture finale a vérifié ces résultats directement dans `rar_radial_bvp.json`, ainsi que les contrôles d'énergie et de raffinement, sans réexécuter le solveur.

| ell | Première valeur propre à 2400 intervalles | À 4800 intervalles | E(cœur positif)−E(cœur presque nul) |
|---:|---:|---:|---:|
| 0,1 | 0,1604173773 | 0,1604174202 | −0,001612471664 |
| 0,03 | 0,7403835106 | 0,7403838511 | −0,003599137101 |

Les deux dernières valeurs propres proviennent des solutions à tolérance du BVP resserrée. Les changements relatifs maximaux d'accélération sont 1,41×10⁻⁸ et 5,04×10⁻⁹. Les différences d'énergie ci-dessus sont celles des branches du jeu initial, également reprises dans `radial_summary.json`. Leur signe est robuste devant les variations de quadrature enregistrées (jusqu'à 2,43×10⁻¹² pour ces énergies) et devant le changement d'énergie lors du resserrement de la tolérance du BVP (environ 3,33×10⁻¹⁰ et 5,04×10⁻¹¹). La nouvelle branche est donc favorisée énergétiquement parmi les deux solutions comparées, sous les conditions prescrites.

Une valeur propre négative signifie une direction négative de l'énergie **statique réduite**. Si χ a une cinétique canonique positive et si la gravitation est traitée comme contrainte instantanée avec source fixée, elle correspond à une instabilité radiale exponentielle dans ce modèle conditionnel. Elle ne signifie pas un ghost, qui concernerait le signe cinétique. Inversement, une première valeur propre positive établit au plus l'absence de direction négative dans le sous-problème radial contrôlé et ses conditions de bord. Elle ne valide ni la dynamique du condensat, ni les perturbations angulaires du système couplé, ni une complétion relativiste.

Formulation conseillée : « Deux branches stationnaires ont été trouvées sous les mêmes conditions prescrites. La branche à cœur presque nul présente un mode radial négatif de l'énergie réduite, tandis que la branche à cœur positif n'en présente pas dans le calcul radial contrôlé sous raffinement. Cette sélection conditionnelle ne constitue pas une démonstration de stabilité d'un halo superfluide complet. »

Le JSON final précise correctement que le contrôle inclut la courbure de l'énergie radiale réduite à source fixée, sans couvrir la stabilité temporelle, angulaire, du condensat ou relativiste du système complet. L'observation antérieure sur la formulation de cette limitation est donc résolue.

Fichiers du contrôle indépendant : `rar_radial_referee_checks.py` et `rar_radial_referee_checks.json`. Aucune recherche d'autres paramètres ou ajustement observationnel n'a été effectué.
