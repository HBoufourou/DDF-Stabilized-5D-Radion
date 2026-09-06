# Longueur stabilisée à couplages fixés : dérivation, solution avec rétroaction et identifiabilité

6 septembre 2026. Développement nouveau, distinct de l'audit des archives. Aucun dossier publié ni dépôt GitHub modifié. Les tests utilisent des unités abstraites ; aucune valeur micrométrique n'est choisie comme cible.

## Résultat central

On peut désormais déterminer la longueur **à partir de couplages dimensionnels donnés**, au lieu de choisir L et de reconstruire tous les couplages. Pour la branche symétrique quadratique, le problème exact avec rétroaction possède une condition simple d'existence et un unique point de bord. La stabilité du secteur sigma y est automatique dans le domaine régulier étudié.

Ce progrès ne fournit pas encore une valeur indépendante de R : il manque l'origine ou la mesure indépendante des couplages d'entrée. La constante de tension nécessaire à des tranches plates doit également satisfaire sa condition de compatibilité. L'énergie noire observée et un calcul Casimir ne suppriment pas ces paramètres libres à eux seuls.

## 1. Action et paramètres réellement fixés

On conserve un seul intervalle physique [0,L], la convention M5³ R/2, le terme GHY, un stabilisateur canonique et des sources de matière minimales. Poser

\[
V(\sigma)=\Lambda_5+\frac12\mu^2\sigma^2,
\quad U_0(\sigma)=\tau_0+\lambda(\sigma+v)^2,
\quad U_L(\sigma)=\tau_L+\lambda(\sigma-v)^2.
\]

Les paramètres mu, lambda, v et Lambda5 sont dimensionnels et maintenus constants lorsque L varie, ainsi que M5³. Leurs dimensions sont respectivement masse, masse, masse^(3/2), masse^5. Les tau_i ont dimension masse^4. Pour une action exactement symétrique avec les deux bords échangés par sigma→−sigma, il faut tau_0=tau_L=tau et des raideurs égales. Des tensions indépendantes inégales demanderaient un autre fond.

Dans ce calcul, **q n'est plus une donnée fixe** : c'est la dérivée du profil à la longueur obtenue. Les quantités x=muL, lambda_hat=lambdaL et epsilon=qL/sqrt(12M5³) deviennent elles aussi des sorties. Les conserver simultanément constants lors d'une variation de L reviendrait à changer l'action.

## 2. Intégration exacte du scalaire sur l'intervalle plat

Cette section résout exactement le problème scalaire sur une métrique plate. Son emploi comme potentiel de radion est un développement à faible rétroaction, et non la solution exacte du système Einstein–scalaire.

Définir

\[
u=\frac{\mu L}{2},\quad a=\frac{2\lambda}{\mu},\quad T=\tanh u.
\]

La solution impaire et sa condition de Robin donnent

\[
\sigma(y)=\frac{q(L)}{\mu\cosh u}\sinh[\mu(y-L/2)],
\quad q(L)=\frac{2\lambda v}{1+aT},
\quad \sigma_b=\frac{qT}{\mu}.
\]

La condition droite est sigma'_b=2lambda(v−sigma_b) et celle de gauche lui correspond par réflexion. Sur cette solution,

\[
\int_0^L\frac12(\sigma'^2+\mu^2\sigma^2)dy
=\frac12[\sigma\sigma']_0^L=\sigma_bq.
\]

En ajoutant les deux potentiels quadratiques sans leurs constantes, l'énergie se simplifie :

\[
\boxed{E_\sigma(L)=\frac{2\lambda v^2}{1+(2\lambda/\mu)\tanh(\mu L/2)}.}
\]

Le potentiel de Jordan au premier ordre non trivial en rétroaction est donc

\[
V_J(L)=\Lambda_5L+\tau_0+\tau_L+E_\sigma(L).
\]

Les corrections gravitationnelles au profil, au potentiel et à la cinétique doivent être incluses à l'ordre suivant. La solution avec rétroaction de la section 5 traite directement le fond, sans extrapoler cette formule plate.

## 3. Minimum de Minkowski et formule fermée de longueur

Poser H(u)=cosh u+a sinh u et K(u)=sinh u+a cosh u. Alors

\[
E_\sigma'=-\frac{2\lambda^2v^2}{H^2},
\qquad E_\sigma''=\frac{2\mu\lambda^2v^2K}{H^3}>0.
\]

Un vide de Minkowski exige V_J=V_J'=0. La première condition de stationnarité est

\[
\Lambda_5=\frac{2\lambda^2v^2}{H(u_*)^2}.
\]

Puisque H(0)=1 et H croît strictement pour mu,lambda>0, il existe une unique longueur positive si et seulement si

\[
\boxed{0<\Lambda_5<2\lambda^2v^2.}
\]

Avec B=sqrt(2)lambda v/sqrt(Lambda5)>1, cette longueur vaut

\[
\boxed{L_{\rm plat}=\frac2\mu
\ln\!\left[\frac{B+\sqrt{B^2+a^2-1}}{1+a}\right].}
\]

La constante commune de tension doit ensuite satisfaire

\[
2\tau=-\Lambda_5L_{\rm plat}-E_\sigma(L_{\rm plat}).
\]

**Si tau est donné indépendamment et ne vérifie pas cette relation, ces paramètres ne décrivent pas ce vide de Minkowski.** On ne peut pas ignorer la condition, ni ajuster silencieusement tau pour prétendre que tous les paramètres ont été prédits. La stationnarité sélectionne la longueur à partir de mu,lambda,v,Lambda5 ; la condition de vide plat impose une relation supplémentaire entre les couplages.

Le rayon conventionnel utilisé dans les tableaux précédents est R0=L/pi. La portée du premier graviton massif devient différente de R0 lorsque la métrique est déformée.

Cas limites utiles :

- lambda→infini à mu,v,Lambda5 fixés donne sigma_b→v et L_plat→(2/mu)asinh(mu v/sqrt(2Lambda5)).
- Pour mu→0 à lambda,v fixés, E_sigma→2lambda v²/(1+lambdaL). Le scalaire sans masse dans le bulk peut donc encore stabiliser avec des valeurs préférées différentes aux deux bords ; une origine indépendante de lambda,v,Lambda5 reste nécessaire.
- À lambda=0 avec v fini, le terme stabilisateur de brane disparaît. Ce n'est pas la limite linéaire à source q fixée, laquelle exige de faire varier v avec lambda et de soustraire une constante divergente.

## 4. Cadre d'Einstein, masse et concordance avec le calcul spectral

Au premier ordre en rétroaction, le coefficient gravitationnel de Jordan est M5³L. Pour une longueur de référence L_ref fixe,

\[
g^E_{\mu\nu}=(L/L_{\rm ref})g^J_{\mu\nu},\quad
V_E=(L_{\rm ref}/L)^2V_J,
\quad \varphi=\sqrt{3/2}\,\overline M_{\rm Pl}\ln(L/L_{\rm ref}).
\]

Au minimum Minkowski V_J=V_J'=0, la transformation de Weyl ne change pas le signe de la dérivée seconde. Avec L_ref=L_* et Mbar_Pl²=M5³L_* :

\[
m_r^2=\frac{2L_*^2}{3\overline M_{\rm Pl}^2}
E_\sigma''(L_*)>0.
\]

Comme E_sigma''(L_*)=mu Lambda5 K_*/H_*, cela donne

\[
\frac{m_r^2L_*^2}{\epsilon^2}
=\frac{4x(T+a)}{\cosh^2(x/2)(1+aT)}
=\frac{4d}{1+d\sinh(x)/(2x)},
\quad d=xT+2\widehat\lambda.
\]

C'est **exactement le coefficient kappa(x,lambda_hat)** obtenu indépendamment par les équations régulières et vérifié dans le solveur FEM quadratique. Cette concordance est une vérification nouvelle entre une variation de longueur à action fixée et le spectre des fluctuations, à l'ordre où le potentiel plat est valide.

Au-delà du voisinage du minimum, il faut aussi conserver le facteur de Weyl. Dans ce potentiel EFT tronqué, V_J est convexe, vaut zéro au minimum Minkowski et croît à grande L ; pourtant V_E tend vers zéro par valeurs positives quand L→infini. Une barrière sépare le minimum de cette limite de décompactification. Les tests la localisent sans la confondre avec un deuxième minimum. Dans cette approximation, un petit vide de de Sitter serait métastable vis-à-vis de la région asymptotique. Ni un calcul de tunneling ni une solution exacte à tranches courbes n'ont été effectués ; la validité de l'approximation sur toute une trajectoire de décompactification reste à vérifier.

## 5. Solution exacte avec rétroaction : la longueur devient un événement de bord

Pour les tranches de Minkowski, les équations exactes en coordonnée propre sont

\[
A''=-\frac{\sigma'^2}{3M_5^3},\quad
\sigma''=\mu^2\sigma-4A'\sigma',\quad
6M_5^3A'^2=\frac12\sigma'^2-\frac12\mu^2\sigma^2-\Lambda_5.
\]

Placer l'origine t=0 au centre de réflexion. La symétrie fixe sigma(0)=A'(0)=0, et la contrainte fixe alors **sigma'(0)=sqrt(2Lambda5)**. A(0) est une normalisation de coordonnées qui sera choisie après l'intégration. Il n'existe plus de pente centrale libre à ajuster pour reproduire une longueur déjà choisie.

Intégrer vers la droite jusqu'à la première racine de

\[
F(t)=\sigma'(t)+2\lambda\sigma(t)-2\lambda v=0.
\]

Le bord est t=t_* et la longueur cherchée est L_exact=2t_*.

Une écriture sans dimension rend explicites toutes les entrées de la prédiction conditionnelle. Poser z=mu t, s=sigma/v, a=2lambda/mu, B=sqrt(2)lambda v/sqrt(Lambda5) et beta=v²/M5³. Alors

\[
A_{zz}=-\frac{\beta}{3}s_z^2,\qquad
s_{zz}=s-4A_zs_z,\qquad
s(0)=A_z(0)=0,\quad s_z(0)=a/B.
\]

Si z_*(a,B,beta) est l'unique racine positive de s_z+a s−a=0,

\[
\boxed{L_{\rm exact}=\frac{2z_*(a,B,\beta)}{\mu},\qquad
R_0=\frac{2z_*(a,B,\beta)}{\pi\mu}.}
\]

Cette formule expose le rapport supplémentaire beta qui contrôle la rétroaction. La forme fermée de la section 3 est sa limite beta→0 ; utiliser seulement a et B pour la longueur exacte omettrait la dépendance à M5.

### Existence, unicité et régularité avant le bord

Pour t>0 tant que le fond est régulier, sigma'>0, sigma>0 et A'<0. En effet A''<0, puis sigma''=mu²sigma−4A'sigma'>0. Il en résulte F'=sigma''+2lambda sigma'>0. Au centre, F(0)=sqrt(2Lambda5)−2lambda v.

Si 0<Lambda5<2lambda²v², on a F(0)<0. Avant son premier zéro, F<0 implique sigma<v et sigma'<2lambda v. Ces bornes empêchent une explosion du champ ou de A' en temps fini avant le bord. De plus sigma'≥sqrt(2Lambda5), donc

\[
F(t)\geq\sqrt{2\Lambda_5}
+2\lambda\sqrt{2\Lambda_5}\,t-2\lambda v.
\]

Une racine existe donc en temps fini, et sa stricte monotonie la rend unique. Si sqrt(2Lambda5)≥2lambda v, F est déjà non négatif au centre et ne peut s'annuler à une distance positive. **La même condition d'existence que dans le calcul plat est donc exacte pour cette branche.**

Les sources restantes doivent satisfaire les jonctions d'Einstein. La constante commune exigée est

\[
\boxed{\tau_{\rm requis}=3M_5^3A'_b-\lambda(\sigma_b-v)^2.}
\]

Cette valeur est une condition de compatibilité du vide plat. Si la tension indépendante de l'action est différente, ce n'est pas une solution de l'action complète à tranches plates. Il faudrait résoudre le problème à tranches courbes ou changer explicitement les paramètres. Les sources totales U_b=3M5³A'_b restent négatives ; l'existence et la stabilité spectrale ne résolvent pas leur origine microscopique.

### Borne exacte sur la correction de longueur

Avec la même pente centrale sqrt(2Lambda5), l'équation avec rétroaction a sigma''≥mu²sigma et atteint des valeurs sigma et sigma' au moins aussi grandes que le profil plat, strictement plus grandes pour t>0 à M5 fini. Le bord Robin est donc rencontré plus tôt :

\[
\boxed{0<L_{\rm exact}<L_{\rm plat}.}
\]

Cette comparaison porte sur **mu,lambda,v,Lambda5 fixés**. Elle ne compare pas deux tableaux calculés à x et epsilon fixés, car ces derniers varient avec la longueur obtenue.

### Stabilité de ce fond exact

Sur la demi-branche droite,

\[
W=\frac{\sigma''}{\sigma'}=\frac{\mu^2\sigma}{\sigma'}-4A'>0.
\]

La réflexion donne W_0<0<W_L. Avec U_i''=2lambda>0, les deux facteurs eta_iW_i+2lambda sont strictement positifs. Sigma' ne s'annule pas. Le quotient positif de l'audit quadratique s'applique donc immédiatement : aucun eigenmode scalaire non trivial du secteur inclus n'a m²≤0 ; la norme canonique est positive. La tour tensorielle comporte le mode constant sans masse et des masses positives. Cela ne couvre ni Phi, ni la stabilité quantique, ni l'UV.

## 6. Tests numériques effectivement exécutés

`r_fixed_action_checks.py` utilise uniquement la bibliothèque standard. Il n'importe aucun ancien solveur. Les tests de potentiel, de dérivées et d'identifiabilité sont séparés du solveur exact de fond.

- Neuf vecteurs de test sans dimension, a∈{.2,1,3} et B∈{1.1,2,5}, vérifient la formule de longueur par une racine numérique indépendante, l'énergie par intégration du profil et les deux conditions de Robin.
- La dérivée seconde de V_E par différences finies concorde avec la formule analytique ; le plus grand écart relatif est 2.7×10^-8.
- La masse du potentiel et kappa spectral coïncident algébriquement et numériquement. Des dérivées logarithmiques contrôlent la dépendance aux paramètres.
- Huit contre-exemples d'identifiabilité construisent plusieurs longueurs stables avec la même densité de vide et les mêmes mu,lambda,v, avant et après ajout d'un terme Casimir de test.
- Quatre fonds avec rétroaction sont intégrés à deux résolutions, 4000 et 8000 pas par demi-longueur plate. La condition de bord est localisée par bissection dans le dernier pas RK4.

Pour ces derniers tests, on fixe mu=1, lambda=.5, M5³=1 et B=2, donc Lambda5=v²/8. Les valeurs de v ci-dessous constituent des exemples abstraits pour vérifier l'effet de la rétroaction ; elles ne fixent aucune échelle physique. La formule plate donne toujours L_plat=2 ln 2=1.3862943611.

| v en unités de test | L_exact | epsilon à la solution | correction L/L_plat−1 | tau requis par bord |
|---:|---:|---:|---:|---:|
| .02 | 1.386245229 | .005002270 | −0.003544 % | −.0001596583 |
| .30 | 1.375369918 | .074737973 | −0.788032 % | −.0359681649 |
| .70 | 1.329781196 | .171398769 | −4.076563 % | −.1968722169 |
| 1.20 | 1.237628509 | .282649119 | −10.723974 % | −.5850359886 |

Les changements relatifs de longueur entre les deux maillages sont inférieurs à 8×10^-14, les résidus de contrainte à 1.6×10^-15 et ceux de la condition scalaire à 4×10^-18 dans ces exécutions. Ces nombres mesurent la reproductibilité des tests, pas la précision physique du modèle. Les tensions indiquent la condition que doit vérifier chaque action pour que le fond calculé soit une solution complète.

## 7. Pourquoi ces résultats ne donnent pas encore une valeur indépendante de R

La formule plate L=(2/mu)f(a,B) sépare un facteur dimensionnel et deux rapports indépendants ; avec rétroaction, elle devient L=(2/mu)z_*(a,B,beta). Connaître les nombres a, B et beta sans connaître mu ne donne pas une longueur en mètres. Même mu connu ne suffit pas si les ratios lambda/mu, lambda v/sqrt(Lambda5) et v²/M5³ restent libres.

La sensibilité peut être quantifiée. En notant u=muL/2 et K=sinh u+a cosh u, à mu,lambda,v,Lambda5 variables indépendantes :

\[
\frac{\partial\ln L}{\partial\ln\mu}
=-1+\frac{a\sinh u}{uK},\quad
\frac{\partial\ln L}{\partial\ln\lambda}=\frac{\cosh u}{uK},
\]
\[
\frac{\partial\ln L}{\partial\ln v}=\frac{B}{uK},\quad
\frac{\partial\ln L}{\partial\ln\Lambda_5}=-\frac{B}{2uK}.
\]

Près de B=1, la longueur tend vers zéro et sa sensibilité relative augmente : l'ajustement des paramètres peut être important. Les valeurs de ces dérivées sont reproduites par variation numérique des couplages.

La mesure de Mbar_Pl²=M5³∫e^(2A)dy contraint une combinaison du volume et de M5. Elle fixe L si M5 et la forme de la métrique sont déterminés indépendamment. Employer pour M5 une valeur déjà inférée de R par la relation de volume ne fournit pas une deuxième contrainte.

## 8. L'énergie noire observée ne lève pas seule la dégénérescence

Il faut distinguer la constante de bulk Lambda5 de la densité de vide 4D rho_Lambda. Pour une densité positive, on doit stationnariser **V_E**, pas V_J. Au point où L_ref=L_* :

\[
V_J(L_*)=\rho_\Lambda,\quad V_J'(L_*)=2\rho_\Lambda/L_*.
\]

Écrire N(L)=E_sigma(L)+V_C^J(L), où V_C désigne toute contribution Casimir calculée. Pour chaque longueur candidate, les choix

\[
\boxed{\Lambda_5=2\rho_\Lambda/L-N'(L),}
\qquad
\boxed{\tau_0+\tau_L=-\rho_\Lambda+LN'(L)-N(L)}
\]

satisfont exactement les deux conditions au niveau de cette EFT. Le Hessien Einstein vaut

\[
V_E''=N''(L)-2\rho_\Lambda/L^2.
\]

Il reste positif pour une large région où la stabilisation est beaucoup plus forte que la courbure cosmologique. **Plusieurs valeurs de L produisent donc la même énergie noire tant que Lambda5 et la somme de tensions renormalisées sont libres.** Les huit exemples numériques vérifient cette non-identifiabilité. Ils ne constituent pas des prédictions de leurs longueurs.

Une petite énergie cosmologique demande finalement des tranches 5D courbes. Les formules ci-dessus décrivent leur EFT à faible courbure ; les quatre fonds exacts de la section 6 restent des fonds de Minkowski. Une dérivation complète à de Sitter n'est pas prétendue accomplie.

## 9. Casimir : calcul physique, contretermes et échelle du radion

La contribution à une boucle s'obtient à partir des vrais spectres et conditions aux bords, schématiquement

\[
V_C^J(L)=\sum_j\frac{(-1)^{F_j}d_j}{2}
\sum_n\int\frac{d^4k}{(2\pi)^4}\ln[k^2+m_{j,n}(L)^2]
\quad\hbox{avec soustractions locales}.
\]

Il faut fixer les degrés de liberté, masses, conditions de bord, ghosts de jauge, mélange stabilisateur–gravité et conditions de renormalisation. Pour un scalaire réel massless avec conditions NN ou DD identiques sur **un intervalle physique**, la partie non locale plate est

\[
V_C^J(L)=-\frac{3\zeta(5)}{128\pi^2L^4}.
\]

Le coefficient est négatif, environ −0.002462408/L^4. Le passage à un cercle, le comptage des copies, les statistiques et la définition R=L/pi changent le raccord ; on ne choisit pas le signe ou un multiplicateur pour reproduire une longueur. Ce terme illustratif n'est pas le déterminant complet de DDF.

Les contretermes de bulk et de brane ont des coefficients renormalisés physiques qui doivent être fixés par des conditions indépendantes. Le calcul de la partie non locale ne calcule pas leurs valeurs finies. Cette distinction est explicite dans le traitement de Garriga–Pujolàs–Tanaka, notamment sa discussion des renormalisations finies et conditions de tensions. [Source primaire](https://arxiv.org/pdf/hep-th/0004109)

Un diagnostic indépendant de l'ordre de grandeur est également utile. Pour un simple terme C/L^4, si les termes locaux sont réglés pour un minimum Minkowski, le rayon est accompagné de

\[
m_{r,C}^2=\frac{40C}{3\overline M_{\rm Pl}^2L^4}.
\]

Il faut C>0 pour que cet exemple soit stable ; le seul boson NN/DD ci-dessus a l'autre signe. Même une contribution positive de quelques degrés de liberté donne une masse de radion extrêmement petite quand 1/L est une énergie de l'ordre du meV à .1 eV. Le code évalue l'échelle absolue correspondante entre environ 7×10^-35 et 7×10^-31 eV pour trois inverses de longueur de test, sans choisir de rayon préféré. Elle est incomparable au radion de l'ordre du meV ou centième d'eV de la stabilisation classique modérée.

À l'inverse, pour un minimum classique déjà stabilisé avec m_r²≈kappa epsilon²/L², l'ajout perturbatif C/L^4, avec les paramètres locaux classiques maintenus fixes, produit au premier ordre

\[
\frac{\delta L}{L}\simeq
\frac{4C}{\kappa\epsilon^2\overline M_{\rm Pl}^2L^2}.
\]

Le code trouve des modules de déplacement entre 5×10^-63 et 5×10^-59 pour les exemples d'échelle testés. Le coefficient change si les contretermes sont ensuite réajustés, mais la suppression paramétrique reste immense dans ce régime. **Un petit Casimir calculable ne peut donc pas choisir efficacement la longueur d'un puits classique déjà aussi raide.** Cette conclusion suppose peu de champs faiblement couplés, sans énormes multiplicités ni structure spectrale singulière. Ce n'est pas une impossibilité pour toute théorie concevable.

## 10. Ce que disent les sources primaires, sans leur faire prédire DDF

**Goldberger–Wise.** Le mécanisme de 1999 stabilise un modulus à partir des paramètres d'un scalaire de bulk et de ses interactions de brane. Le travail conserve un réglage de la constante cosmologique 4D. Il motive l'étude à action fixée ; ses potentiels quartiques dans le cadre RS ne donnent pas directement les constantes du modèle symétrique quadratique présent. [Article original](https://arxiv.org/pdf/hep-ph/9907447)

**Montero–Vafa–Valenzuela.** Le scénario relie une échelle de tour à l'énergie noire via des hypothèses de Swampland. La version publiée écrit l=lambda_MVV rho_Lambda^(-1/4) avec un coefficient estimé, notamment dans la région 10^-1–10^-3. L'estimation Casimir présentée par les auteurs ne fixe pas les paramètres mu,lambda,v,Lambda5,tau de notre action. lambda_MVV ne doit surtout pas être confondu avec la raideur dimensionnelle lambda. Leur échelle est une motivation théorique conditionnelle, pas une mesure de R ni une sélection unique dans DDF. [Version publiée, sections 3 et 5](https://arxiv.org/html/2205.12293v3)

**Cui–Ning, 2026.** Leur réalisation Casimir du scénario comporte un radion trop léger pour les tests de gravité sous ses hypothèses minimales. La version consultée discute ensuite un dispositif d'écrantage supplémentaire, avec des éléments restant ouverts. Ce travail ne fournit pas une validation du radion gravitationnellement couplé de DDF. [Article](https://arxiv.org/html/2310.19592v3), [publication JHEP](https://doi.org/10.1007/JHEP02(2026)156)

**Katayama et collaborateurs, 2026.** Leur étude de quintessence Casimir illustre la dépendance au contenu du bulk et aux couplages matière–radion. Un potentiel cosmologique lent et un radion lourd de courte portée sont deux régimes différents. Les nouveaux champs et couplages qu'ils posent ne sont pas des résultats dérivés de notre action. [Prépublication](https://arxiv.org/html/2603.19819v1)

Aucune priorité générale n'est revendiquée pour la stabilisation, la renormalisation ou le traitement du modulus. Le nouvel apport local est la caractérisation explicite de cette branche quadratique à couplages fixés, sa longueur avec rétroaction, ses contrôles et ses limites d'identifiabilité.

## 11. Pistes ayant le meilleur potentiel après ce calcul

1. **Fixer une véritable entrée dimensionnelle indépendante.** Une dérivation de mu et des rapports a, B et beta transformerait la sélection exacte en prédiction dimensionnelle ; à faible rétroaction, a et B suffisent au premier ordre. Une détermination indépendante de M5 et du profil gravitationnel pourrait aussi exploiter la mesure de la masse de Planck. Le mécanisme doit être fourni par une action ou un compactifié explicite ; identifier simplement mu à une masse de neutrino connue serait une nouvelle hypothèse, pas une dérivation. Les nombres topologiques et les rapports spectraux de la géométrie DDF ne fixent pas une longueur physique tant qu'une liberté d'échelle persiste.
2. **Compléter le modèle à action fixée avec la constante cosmologique.** Le solveur d'événement peut servir de noyau à un BVP à tranches légèrement courbes, en gardant toutes les tensions d'entrée. Il faut contrôler la compatibilité des paramètres plutôt que reconstruire chaque tension après avoir choisi un rayon.
3. **Définir un mécanisme de protection des faibles masses et des potentiels de brane.** Une symétrie ou une réalisation UV peut rendre les coefficients prédictifs et radiativement stables. Ajouter des termes pour déplacer un minimum sans cette justification diminue l'identifiabilité.
4. **Utiliser des relations spectrales pour tester le modèle même si R reste libre.** Les masses relatives, profils et amplitudes corrèlent plusieurs observables. Une détection de tour pourrait déterminer L empiriquement et tester ces rapports ; elle ne serait pas une prédiction a priori de L, mais constituerait une épreuve scientifique réelle.
5. **Calculer le Casimir renormalisé comme correction et contrôle de cohérence.** Son contenu et ses conditions de renormalisation doivent être fixés avant confrontation à rho_Lambda. Dans le puits classique lourd actuel, son rôle naturel est une très petite correction, pas un mécanisme capable de sélectionner une longueur micrométrique indépendamment des couplages classiques.

La priorité scientifique réaliste est donc : **exploiter la longueur à couplages fixés désormais calculable, puis obtenir l'un de ces couplages d'une source indépendante**. Il n'est pas utile de rechercher un coefficient numérique reproduisant à nouveau 8.2 µm. Le présent développement a une conclusion positive — une sélection conditionnelle exacte et stable — et une conclusion limitante démontrée — l'observation de l'énergie noire ne suffit pas à rendre R identifiable dans l'EFT actuelle.

## Fichiers reproductibles

- `r_fixed_action_checks.py` : bibliothèque standard uniquement ; tests du potentiel, racines, Hessien, sensitivités, contre-exemples d'identifiabilité, ordres de grandeur Casimir et solveur RK4 du fond à longueur inconnue.
- `r_fixed_action_checks.json` : paramètres de chaque test, longueurs obtenues, tensions requises, résidus et comparaison des maillages.

Aucun de ces tests n'a choisi une nouvelle valeur physique de R. Les quatre longueurs avec rétroaction sont exprimées dans les unités des couplages de test mu=1, non en micromètres.
