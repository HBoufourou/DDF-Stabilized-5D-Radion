# Conditions de bord, positivité et contrôle spectral quadratique

Extraits techniques des calculs contrôlés du 6 septembre 2026. La définition active et la portée sont celles de THEORIE_DDF.md à la racine. Les anciens audits complets sont conservés dans les archives.

## 2. Modèle quadratique à poser explicitement

Utiliser l'action sur un seul intervalle physique et les normales eta_0=-1, eta_L=+1 :

\[
S=\int_0^L\sqrt{-g}\,[M_5^3\mathcal R/2-(\partial\sigma)^2/2-V]
+M_5^3\int_{\partial M}\sqrt{-\gamma}K
-\sum_i\int_i\sqrt{-\gamma}\,U_i+S_m[\gamma_0].
\]

Les mesures 4D sont implicites. Poser

\[
U_i(\sigma)=\tau_i+\lambda_i(\sigma-v_i)^2,
\quad U_i''=2\lambda_i,
\quad U_i'=2\lambda_i(\sigma-v_i).
\]

Les lambda_i ont dimension de masse, donc la raideur sans dimension est lambda_hat_i=lambda_i L. Pour un fond déjà choisi, notant q_i=sigma'(y_i), les jonctions imposent

\[
v_i=\sigma_i+\frac{\eta_iq_i}{2\lambda_i},\qquad
\tau_i=3\eta_iM_5^3 A_i'-\frac{q_i^2}{4\lambda_i}.
\]

Ces formules valent pour lambda_i>0. Le fond impose toujours la **valeur totale** U_i(sigma_i)=3 eta_i M5³ A'_i. Il ne faut pas confondre cette valeur, qui intervient dans la courbure extrinsèque, avec la constante nue tau_i du potentiel quadratique.

La limite lambda→0 de cette paramétrisation à q_i fixé envoie v_i et tau_i à l'infini avec des annulations. Le cas linéaire est plus proprement défini comme une action séparée U_i=T_i+J_i sigma. À raideur égale et sources symétriques, on peut conserver la réflexion combinée à sigma→−sigma. Sinon la symétrie des fluctuations n'est plus acquise.

## 3. Les nouvelles conditions de bord sont correctes, mais leur domaine doit être complété

Avec la jauge fixe du dépôt corrigé, F=f(y)chi(x), delta sigma=s(y)chi(x), la contrainte et l'équation régulière de bulk restent

\[
3M_5^3(f'+2A'f)+\sigma's=0,
\]
\[
f''+(2A'-2W)f'+(4A''-4A'W+m^2e^{-2A})f=0,
\quad W=\sigma''/\sigma'.
\]

Perturber la jonction n·partial sigma=−U_i' donne

\[
s_i'+2\sigma_i'f_i+\eta_i U_i''s_i=0.
\]

En posant B=f'+2A'f, le bulk donne B'=2WB−2A''f−m²e^(−2A)f. Substitution de s=−3M5³B/sigma' et A''=−sigma'²/(3M5³) conduit exactement à

\[
D_iB_i=m^2e^{-2A_i}f_i,\qquad
D_i=W_i+\eta_iU_i''=W_i+2\eta_i\lambda_i.
\]

Le facteur 2 n'est pas à laisser « à fixer » : il provient ici de la définition choisie U=lambda(sigma−v)². Pour comparer à un article utilisant U=lambda(sigma−v)²/2 ou deux copies d'intervalle, il faut convertir l'action entière. Une validation interne de la BC ne corrige pas automatiquement une action imprimée avec un autre coefficient d'Einstein.

## 4. Preuve de stabilité et dépendance exacte à la raideur

La substitution régulière g=e^(2A)f donne

\[
-(pg')'+Qg=m^2wg,
\quad p=\frac{e^{-2A}}{\sigma'^2}>0,
\quad w=\frac{e^{-4A}}{\sigma'^2}>0,
\quad Q=\frac{2e^{-2A}}{3M_5^3}>0.
\]

La BC devient g'_i=m²e^(−2A_i)g_i/D_i. Tant que les D_i sont non nuls, l'intégration par parties produit

\[
\int_0^L(p|g'|^2+Q|g|^2)dy
=m^2\left[\int_0^Lw|g|^2dy+
\sum_i\frac{w_i|g_i|^2}{\eta_iW_i+U_i''}\right].
\]

**Si le fond est lisse, sigma' ne s'annule pas et eta_i W_i+2lambda_i>0 aux deux bords, tout eigenmode scalaire non trivial de ce problème possède m² réel strictement positif.** C'est la version robuste à utiliser. Elle s'applique au fond symétrique comme aux trois fonds monotones réellement intégrés ci-dessous.

Le signe large ≥0 donné dans le ZIP implique seulement une conclusion non négative via l'identité d'énergie : le cas d'égalité peut changer le rang des conditions, autoriser un mode nul et doit être traité séparément. Dans le nouveau modèle, **le lieu dégénéré est D_i=0**, et non sigma_i''=0 pris isolément. Par exemple W_0=0 n'est pas dégénéré si lambda_0>0.

À fond fixé et dans le domaine strictement positif, augmenter lambda_i diminue le dénominateur de Rayleigh pour chaque fonction test, tandis que le numérateur reste fixe. Le principe min–max implique donc que les masses scalaires ordonnées ne diminuent pas avec la raideur. C'est un résultat plus précis que « les termes quadratiques aident » : il concerne les eigenvaleurs à fond fixé, pas un changement simultané du fond. Il ne fournit pas un signe universel pour la dérivée du couplage.

La limite lambda_i→infini supprime les poids spectraux de bord et impose g'_i=0, soit B_i=0 et s_i=0 : elle donne un plafond spectral fini. **lambda_hat=20 n'est pas mathématiquement la limite infiniment raide.** Le gain déclaré « maximal en limite raide +24 % » n'est pas établi par une ligne finie à 20. L'ordre de grandeur de saturation est crédible, pas le statut de maximum exact.

La norme canonique reste, en l'absence de cinétiques ajoutées sur les branes,

\[
N_f=\int e^{2A}(3M_5^3f^2+s^2/2)dy,\quad Z_f=2N_f,
\]
\[
\alpha_f=\frac{M_5^3 I f(0)^2}{N_f},\quad I=\int e^{2A}dy.
\]

Le facteur M5³ manque à la formule du ZIP si on quitte ses unités M5³=1. Il n'y a pas de régression numérique de facteur deux dans la formule de programme_v2, mais il faut conserver explicitement Z=2N et Mbar_Pl²=M5³I.

## 5. Développement analytique neuf pour les branes quadratiques

Ce calcul est indépendant des nouveaux nombres du ZIP et n'utilise pas son code historique. À x=muL>0 et lambda_hat=lambdaL≥0 fixés, dans le fond symétrique avec les deux raideurs égales, écrire t=y/L−1/2, C=cosh²(x/2), T=tanh(x/2). Pour L=M5³=1 :

\[
\sigma'=\epsilon v_1+O(\epsilon^3),\quad
v_1=\sqrt{12}\cosh(xt)/\sqrt C,
\quad A=\epsilon^2a_2+O(\epsilon^4).
\]

Le développement f=1+epsilon² f2 et m²L²=kappa epsilon² conduit toujours à

\[
b(t)=\frac{8t\cosh^2(xt)}C-\frac{\kappa\sinh(2xt)}{2x},
\quad b=f_2'+2a_2'.
\]

Seule la BC change, d b(1/2)=kappa avec d=xT+2lambda_hat. D'où

\[
\boxed{\kappa(x,\widehat\lambda)=
\frac{4d}{1+d\sinh(x)/(2x)},\qquad d=x\tanh(x/2)+2\widehat\lambda.}
\]

Elle redonne exactement la formule linéaire 4xT/C à lambda=0, et tend vers 8x/sinh(x) en limite raide. Les autres profils restent

\[
f_2(t)=\frac{4t^2+2t\sinh(2xt)/x}{C}
-\frac{\kappa[\cosh(2xt)-1]}{4x^2},
\quad s_1=-3b/v_1.
\]

Le couplage est donc calculable sans ajustement spectral par

\[
c_\alpha(x,\widehat\lambda)=2[f_2(1/2)-\langle f_2\rangle]
-\langle s_1^2\rangle/6.
\]

La formule fermée antérieure c_alpha=sech²(x/2)[1+tanh²(x/2)+2tanh(x/2)/x] concerne **lambda=0 seulement**. Résultats d'intégration indépendante des profils à x=2 :

| lambda_hat | kappa | c_alpha | mL dominant à epsilon=.3 | alpha dominant à epsilon=.3 |
|---:|---:|---:|---:|---:|
| 0 | 2.558800034 | 0.983420240 | 0.479887490 | 0.362835941 |
| 1 | 3.359794733 | 0.839948683 | 0.549892286 | 0.358531794 |
| 20 | 4.297387689 | 0.622678119 | 0.621904247 | 0.352013677 |
| infini | 4.411529036 | 0.592594873 | 0.630109207 | 0.351111180 |

Les deux dernières colonnes sont **asymptotiques**, pas des reproductions du spectre fini à epsilon=.3. Elles sont compatibles avec la tendance des tableaux et montrent explicitement pourquoi il faut redéfinir les coefficients dans le nouveau modèle. En limite de faible epsilon, le rapport maximal de masse raide/linéaire à x=2 est environ 1.313, et non 1.24 universellement. Le calcul fini ajouté ultérieurement est distingué en section 13.


## 13. Prolongement réalisé : spectres FEM de la branche symétrique quadratique

Un script autonome supplémentaire, `quadratic_fem.py`, a été préparé et exécuté dans le contexte parent avec NumPy/SciPy. Il reprend la méthode éléments finis P1 de la base corrigée sans importer ni exécuter un solveur de l'archive : fond symétrique intégré par DOP853, quadrature de Gauss à huit points par cellule, matrices du problème positif et poids spectraux de bord

\[
\mathcal D[g]=\int w g^2dy+
\frac{g(0)^2+g(L)^2}{q^2(W_L+2\lambda)},\qquad A_i=0.
\]

À lambda infini, les poids de bord valent zéro ; il s'agit du problème limite rigide, distinct d'une action à coefficient fini. La même métrique est conservée en reconstruisant les minima et tensions lorsque la raideur varie. Ce calcul porte sur les trois premiers modes scalaires, pas sur Phi, le spectre monotone ni les expériences.

### Résultats finis à x=2, epsilon=.3

Les estimations du tableau emploient Richardson après vérification de l'ordre de convergence sur les maillages 256, 512 et 1024. Les douze masses (trois modes à quatre raideurs) ont des ordres entre 1.9994 et 2.0001, et les douze amplitudes entre 1.9995 et 2.0001. Les plus grands écarts relatifs internes entre la dernière grille et l'extrapolation sont 1.46×10^-6 pour les masses et 3.99×10^-6 pour les amplitudes. Ce sont des indicateurs de convergence numérique, pas des erreurs physiques de l'EFT.

| lambda_hat | m_radion L | alpha_radion | portée si R=3 µm |
|---:|---:|---:|---:|
| 0 | 0.483690816 | 0.359837939 | 19.485129 µm |
| 1 | 0.537837539 | 0.356074963 | 17.523466 µm |
| 20 | 0.599671485 | 0.350135357 | 15.716568 µm |
| infini | 0.607110189 | 0.349286341 | 15.523999 µm |

Les nombres arrondis de `ETAPE1_FOND_ET_STABILITE.md` pour les trois premières lignes sont donc reproduits par ce calcul spectral indépendant. Le gain de masse réellement saturé, au point epsilon=.3, vaut **+25.52 %**, au lieu de qualifier la ligne lambda_hat=20 de maximum à +24 %. La hausse des trois eigenvaleurs avec la raideur et leur positivité ont été vérifiées par assertions dans le script. La baisse de l'amplitude figurant dans ce tableau est un résultat de cette famille ; ce n'est pas une loi générale sur tout potentiel de brane.

### Vérification faible epsilon à lambda_hat=1

Le coefficient analytique est kappa=3.3597947329 et c_alpha=0.83994868323. Deux nouveaux points donnent :

| epsilon | (mL)²/epsilon² | (3alpha−1)/epsilon² |
|---:|---:|---:|
| .010 | 3.359617771 | 0.839843628 |
| .005 | 3.359749932 | 0.839922314 |
| limite analytique | 3.359794733 | 0.839948683 |

Les erreurs relatives par rapport aux coefficients analytiques diminuent d'un facteur 3.95 pour kappa et 3.98 pour c_alpha quand epsilon est divisé par deux, ce qui est compatible avec des corrections d'ordre epsilon² aux coefficients extraits. Ce contrôle vérifie en particulier que la généralisation du coefficient de couplage est associée à la nouvelle BC, et pas seulement à une reprise du nombre .983420 de la branche linéaire.

La convergence de maillage de ces **très petites masses** atteint le bruit d'arrondi : l'ordre deux n'est pas résolu et aucune extrapolation de masse n'est utilisée. Les masses du tableau proviennent donc du maillage le plus fin. Les amplitudes ont des ordres mesurés de 1.981 et 2.036 et permettent ici l'extrapolation indiquée. Le rapport d'erreur proche de quatre est un diagnostic asymptotique, pas une borne rigoureuse sur le reste. Les sorties gardent chaque choix d'estimation et ses indicateurs.

### Correction numérique nécessaire à la norme

Pour un mode presque constant à très faible epsilon, calculer directement g^T K g soustrait de grandes contributions voisines de la matrice de rigidité. Une première exécution a montré que cette annulation dégradait le petit coefficient c_alpha extrait de 3alpha−1. Le script a été corrigé pour intégrer **avant assemblage** les quantités positives :

\[
N_f=\frac92\sum_{\mathrm{cellules}}\sum_{\mathrm{Gauss}}
\omega\,\Delta y\,[p(g')^2+Qg^2].
\]

Il utilise cette valeur pour la normalisation canonique Z=2N et le couplage ; g^T K g reste uniquement un diagnostic d'annulation. La comparaison N=(9/2)m²D reste enregistrée : son plus grand résidu relatif est environ 1.7×10^-7 sur l'ensemble, dominé par les très faibles masses. On ne transforme pas cette limite d'arrondi en un défaut physique du modèle.

**Statut amélioré après ce prolongement :** les signatures de la branche S quadratique à x=2, epsilon=.3 sont maintenant reproduites, y compris une vraie limite rigide et un contrôle indépendant de faible epsilon. Le choix de raideur physique, le statut EFT, les sources monotones asymétriques, la cosmologie/Phi et l'exclusion expérimentale restent ceux exposés ci-dessus. L'article principal validé peut être conservé ; ces résultats forment une annexe nouvelle concrète et vérifiable.

Reproduction complète : `quadratic_fem.py`, sortie `quadratic_fem.json` ; convention, cas calculés, paramètres de brane reconstruits, trois modes par maillage, normes, résidus et critères d'extrapolation sont consignés dans ce JSON.
