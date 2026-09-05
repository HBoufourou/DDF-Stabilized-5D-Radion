# Vérification indépendante du couplage scalaire à la brane

Date : 5 septembre 2026. Statut : calcul indépendant conditionnel, portant sur la normalisation de l'échange scalaire et son développement à faible rétroaction. Aucun verdict expérimental, aucune nouveauté revendiquée.

## 1. Action et conventions effectivement vérifiées

La vérification utilise l'action compatible avec les équations de fond et la contrainte employées par le solveur indépendant :

\[
S=\int d^4x\,dy\sqrt{-g}\left[\frac{M_5^3}{2}\mathcal R
-\frac12(\partial\sigma)^2-V(\sigma)\right]
+M_5^3\int_{\partial M}\sqrt{-\gamma}\,K
-\sum_i\int_i\sqrt{-\gamma}\,U_i(\sigma).
\]

La signature est \((-++++)\), l'intervalle physique est \([0,L]\) et les branes restent à coordonnées fixes. Les potentiels de brane sont linéaires en \(\sigma\), sans terme cinétique de brane ni terme d'Einstein induit. Le secteur matière qui sert de source est supposé minimalement couplé à la métrique induite. On ne suppose pas de couplage direct supplémentaire entre cette matière et \(\sigma\).

**Cette action diffère de celle imprimée dans paperA.tex**, dont le coefficient gravitationnel est \(2M_5^3\). Le noyau unifié choisit désormais la convention M5³ Ricci/2 avec le GHY et les jonctions indiqués dans EFT_MODELE_ET_RESULTATS.md. Les valeurs ci-dessous correspondent à ce choix. L’incohérence subsiste dans le manuscrit historique conservé pour provenance ; ses autres calculs ne sont pas validés rétroactivement par ce choix.

Le fond et les perturbations sont pris sous la forme

\[
ds^2=e^{2A(y)+2F(x,y)}\eta_{\mu\nu}dx^\mu dx^\nu
+e^{-4F(x,y)}dy^2,\qquad
\sigma=\sigma_0(y)+\delta\sigma(x,y).
\]

Ainsi, au premier ordre, \(\delta g_{\mu\nu}=2F g_{\mu\nu}\) et \(\delta g_{55}=-4F\). La forme exponentielle choisie au deuxième ordre est une paramétrisation commode; le résultat quadratique suppose le fond et ses conditions de bord satisfaits.

Pour un mode scalaire massif donné,

\[
F(x,y)=f(y)\chi(x),\qquad \delta\sigma(x,y)=s(y)\chi(x),
\]

avec la contrainte

\[
3M_5^3(f'+2A'f)+\sigma_0's=0.
\]

## 2. Cinétique : la norme de l'archive est la moitié de Z

Dans la décomposition ADM suivant la coordonnée spatiale \(y\), le terme d'Einstein, avec son GHY, comporte

\[
\frac{M_5^3}{2}\int dy\,d^4x\,
N_y\sqrt{-h}\,\mathcal R[h],
\qquad N_y=e^{-2F},\quad h_{\mu\nu}=e^{2A+2F}\eta_{\mu\nu}.
\]

Les termes de courbure extrinsèque ne portent pas de dérivées 4D dans cette jauge. Or

\[
\mathcal R[h]=e^{-2A-2F}\{-6\Box_4F-6(\partial F)^2\},
\]

et donc

\[
N_y\sqrt{-h}\,\mathcal R[h]
=e^{2A}\{-6\Box_4F-6(\partial F)^2\}.
\]

Le premier terme s'intègre en une divergence 4D. Le terme gravitationnel cinétique vaut alors

\[
S^{(2)}_{\mathrm{grav,kin}}
=-3M_5^3\int dy\,d^4x\,e^{2A}(\partial F)^2.
\]

Le terme cinétique 4D du scalaire est

\[
S^{(2)}_{\sigma,\mathrm{kin}}
=-\frac12\int dy\,d^4x\,e^{2A}(\partial\delta\sigma)^2.
\]

Les potentiels de bord n'ajoutent pas de dérivées 4D. Pour le mode choisi,

\[
S^{(2)}_{4,\mathrm{kin}}=-N_f\int d^4x\,(\partial\chi)^2,
\qquad
N_f=\int_0^Ldy\,e^{2A}\left(3M_5^3f^2+\frac12s^2\right).
\]

La convention usuelle \(-Z_f(\partial\chi)^2/2\) donne donc

\[
\boxed{Z_f=2N_f,\qquad \varphi_f=\sqrt{2N_f}\,\chi.}
\]

La contrainte doit être imposée dans les profils physiques. On ne déduit pas la cinétique uniquement de l'identité énergétique ou de sa normalisation arbitraire : elle vient ici explicitement de l'action quadratique.

## 3. Couplage à une source et amplitude Yukawa

La variation minimale de l'action matière sur la brane \(y_b\) est

\[
\delta S_m=\frac12\int d^4x\sqrt{-\gamma}\,T^{\mu\nu}\delta\gamma_{\mu\nu}
=\int d^4x\sqrt{-\gamma}\, f(y_b)\chi T^\mu{}_{\mu}.
\]

Dans les coordonnées physiques de la brane, avec \(A(y_b)=0\), le couplage canonique est

\[
g_f=\frac{f(y_b)}{\sqrt{2N_f}}.
\]

L'échange d'un scalaire canonique fournit entre deux sources non relativistes sur cette même brane

\[
V_f(r)=-\frac{g_f^2m_1m_2}{4\pi r}e^{-m_fr}.
\]

Sans terme d'Einstein de brane, le mode tensoriel sans masse donne

\[
\overline M_{\rm Pl}^{\,2}=M_5^3\int_0^L e^{2A}dy,
\qquad G_T=\frac{1}{8\pi\overline M_{\rm Pl}^{\,2}}.
\]

La force de Yukawa relative à cette gravité tensorielle est donc

\[
\boxed{\alpha_f=2\overline M_{\rm Pl}^{\,2}g_f^2
=\frac{\overline M_{\rm Pl}^{\,2}f(y_b)^2}{N_f}.}
\]

Le résultat ne dépend pas de la normalisation choisie pour \((f,s)\). Dans la limite plate \(f=\) constante, \(s=0\), il redonne \(\alpha_f=1/3\).

Si le scalaire est encore effectif à la distance où l'on détermine expérimentalement la constante de Newton, \(G_T\) et la constante mesurée ne doivent pas être confondus : la convention du potentiel et le raccord expérimental doivent être adaptés. Pour des échanges de portée micrométrique et une détermination de \(G\) à distance macroscopique, ce problème ne se présente pas au même ordre. Cela ne remplace pas une analyse de données.

## 4. Développement analytique à faible rétroaction

On reprend les paramètres du solveur indépendant, \(L=M_5^3=1\), \(\mu=2\), \(q=\sqrt{12}\,\epsilon\), et le fond symétrique autour de \(t=y-1/2=0\). La coordonnée \(t\) appartient à \([-1/2,1/2]\). La symétrie autorise des intégrales doubles sur \([0,1/2]\).

Définissons

\[
C=\cosh^2 1,\qquad
v_1(t)=\frac{\sqrt{12}\cosh(2t)}{\cosh1},\qquad
\kappa=\frac{8\tanh1}{\cosh^2 1}=2.558800033796898.
\]

Le fond admet \(\sigma_0'=\epsilon v_1+O(\epsilon^3)\) et \(A=\epsilon^2a_2+O(\epsilon^4)\), avec

\[
a_2'(t)=-\frac{2t+\tfrac12\sinh(4t)}{C}.
\]

La constante additive de \(a_2\) fixe \(A(y_b)=0\) et s'annule finalement dans le coefficient de couplage.

Pour le mode pair le plus léger, choisissons \(f(0)=1\) au centre et écrivons

\[
f=1+\epsilon^2f_2+O(\epsilon^4),\qquad
m_r^2=\kappa\epsilon^2+O(\epsilon^4).
\]

L'équation régulière utilisée est

\[
f''+(2A'-2W)f'+(4A''-4A'W+m_r^2e^{-2A})f=0,
\quad W=\frac{\sigma_0''}{\sigma_0'},
\]

avec la condition aux branes

\[
W(f'+2A'f)-m_r^2e^{-2A}f=0.
\]

À l'ordre \(\epsilon^2\), on définit \(b=f_2'+2a_2'\). Puisque \(W_0=2\tanh(2t)\),

\[
b'-2W_0b=\frac23v_1^2-\kappa,\qquad b(0)=0.
\]

La solution est

\[
b(t)=\frac{8t\cosh^2(2t)}{C}-\frac\kappa4\sinh(4t).
\]

La condition de bord \(2\tanh1\,b(1/2)=\kappa\) fixe la valeur de \(\kappa\) donnée plus haut. L'intégration de \(f_2'=b-2a_2'\), avec \(f_2(0)=0\), donne

\[
\boxed{f_2(t)=\frac{4t^2+t\sinh(4t)}{C}
-\frac\kappa{16}[\cosh(4t)-1].}
\]

La contrainte fixe

\[
s(t)=-3\epsilon\frac{b(t)}{v_1(t)}+O(\epsilon^3).
\]

Notons \(\langle h\rangle=\int_{-1/2}^{1/2}h(t)dt\). En développant le quotient \(\overline M_{\rm Pl}^{\,2}f_b^2/N_f\), les corrections explicites de volume \(\langle a_2\rangle\) s'annulent :

\[
\alpha_r=\frac13\left[1+c_\alpha\epsilon^2+O(\epsilon^4)\right],
\]

\[
\boxed{c_\alpha=2\{f_2(1/2)-\langle f_2\rangle\}
-\frac16\left\langle\left(\frac{3b}{v_1}\right)^2\right\rangle.}
\]

L'évaluation indépendante des intégrales explicites par Simpson, 10 000 sous-intervalles sur la demi-longueur, donne :

| Quantité | Valeur |
|---|---:|
| \(f_2(1/2)\) | 0.7398243458386384 |
| \(\langle f_2\rangle\) | 0.21451149573154715 |
| \(\langle(3b/v_1)^2\rangle\) | 0.40323276225392163 |
| \(c_\alpha\) | **+0.983420239838529** |

Le signe positif et le coefficient sont donc obtenus à partir d'un développement analytique des équations régulières, indépendamment du calcul spectral à rétroaction finie. Ils ne correspondent pas au coefficient \(-0.634\) employé dans paper B. La différence ne se réduit pas à un facteur deux dans la normalisation de l'échange. La dérivation moduli-space de l'archive doit être confrontée aux profils des modes propres et aux conventions cohérentes de l'action.

Les valeurs spectrales finies du solveur parent, par exemple \(\alpha_r\simeq0.33415\) à \(\epsilon=0.05\) et \(0.37716\) à \(\epsilon=0.4\), sont compatibles avec la tendance positive. Le développement à l'ordre \(\epsilon^2\) ne doit pas être utilisé comme résultat exact à rétroaction forte.

## 5. Réserves et portée du résultat

- Le coefficient calculé utilise la définition précise \(\epsilon=qL/\sqrt{12M_5^3}\) et \(\mu L=2\), avec les conventions de dimensions correspondantes. Une autre définition de \(\beta L\) doit être raccordée explicitement avant de comparer les nombres.
- Le résultat concerne le secteur métrique–\(\sigma\). Un éventuel autre scalaire \(\Phi\) dont le fond est nul n'est pas inclus. Dans l'action complète il faut vérifier son absence de mélange quadratique et de source directe de brane; le seul énoncé \(\Phi_0=0\) ne remplace pas cette vérification.
- Une cinétique ou une courbure induite de brane, des masses de matière dépendant de \(\sigma\), ou un couplage non minimal modifient respectivement la norme, le Planck effectif ou la source. Ils exigeraient un nouveau calcul.
- Le couplage est celui d'une source sur une brane fixe, dans la jauge choisie, et suppose l'identification correcte avec la perturbation induite physique. Si l'on change de jauge avec déplacement de brane, il faut inclure la combinaison invariante correspondante.
- Les modes scalaires massifs supérieurs ont eux aussi des couplages \(\alpha_{s,n}=\overline M_{\rm Pl}^{\,2}f_n(y_b)^2/N_n\). Le potentiel complet doit inclure leur somme et la tour tensorielle, avec ses profils normalisés. Le radion seul n'est pas nécessairement tout le signal.
- Cette vérification ne prouve ni l'exhaustivité du spectre, ni l'absence de tous les modes pathologiques, ni l'accord aux contraintes expérimentales. Elle ne sélectionne pas un rayon physique absolu et ne constitue pas une détection d'une cinquième dimension.

Références contextuelles vérifiées : la normalisation tensorielle et son facteur de polarisation doivent être distingués de cette normalisation scalaire ([Callin et Ravndal, 2004](https://arxiv.org/pdf/hep-ph/0403302)); les résultats de balance de torsion sont des ajustements de couples pour des potentiels spécifiés ([Lee et al., 2020](https://arxiv.org/pdf/2002.11761)). Les calculs des sections 2–4 de la présente note sont effectués ici à partir de l'action et des équations indiquées.
