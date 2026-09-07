# Relecture mathématique adversariale de l'article 1

> **Statut au 7 septembre 2026 :** compte rendu conservé de la relecture avant intégration. Les corrections retenues ont été appliquées au manuscrit livré, y compris les quatre précisions finales de notation. Le [bilan final](AUDIT_FR.md) distingue les corrections intégrées des limites scientifiques restantes.

7 septembre 2026. Lecture intégrale du manuscrit Markdown, des deux avis fournis, des équations et des données de calcul pertinentes. Les avis sont traités comme des propositions à vérifier, sans valeur de certification. Aucun fichier de `outputs` n'a été modifié par cet audit.

Version lue : `publications/article_1/manuscript.md`, SHA256 `19330d84d8b2f6310eb9f0b217849c00c1768cc5bc07c4eb304379690a0cf363`.

## Conclusion limitée

Les objections sur une prétendue borne \(c_\alpha>1/3\) et sur un facteur supplémentaire \(\eta_i\) devant \(2\lambda\) ne décrivent pas les équations du manuscrit : ce sont des erreurs du deuxième avis. Les coefficients imprimés, l'annulation du volume de Planck, les poids de bord, les monotonies déclarées et la comparaison des longueurs ont été re-dérivés et sont cohérents dans leurs domaines.

Le défaut substantiel de la version lue reste son traitement trop implicite du cône nul en section 4. La phrase « deriving the tensorial constraints before dividing » ne montre pas au lecteur pourquoi le candidat X₁ est hors domaine. Le nouveau calcul T1 doit être incorporé au manuscrit ou dans une annexe accessible et explicitement citée. La positivité du problème massif ne suffit pas, à elle seule, à présenter cette étape comme démontrée dans l'article.

Je n'ai pas identifié d'autre erreur de signe ou de facteur dans les équations (1)–(28), (A1)–(A2), après les contrôles exposés ci-dessous. Cette conclusion n'est ni une preuve d'absence de toute erreur, ni une certification de nouveauté, de publication ou de viabilité complète. Les douze spectres numériques ne sont pas recalculés par mon script indépendant ; leur rejeu est une tâche séparée du coordinateur.

## 1. La borne contestée : le manuscrit et l'avis ne disent pas la même chose

L'article écrit en (21) \(3\alpha_r-1=c_\alpha\epsilon^2+O(\epsilon^4)\), puis en (23)

\[
0<c_\infty(x)\le c_\alpha(x,\widehat\lambda)\le c_0(x).
\]

Il n'écrit pas \(c_\alpha>1/3\). Le coefficient \(c_\alpha\) et le résidu \(\alpha_r\) ne sont pas le même objet. Une correction dominante positive implique \(\alpha_r>1/3\) pour \(\epsilon\) suffisamment petit à paramètres de forme fixés, sous contrôle du reste ; elle ne donne pas une borne globale à amplitude arbitraire.

La proposition supplémentaire de l'avis serait fausse :

| x | c∞ | cα(x,20) |
|---:|---:|---:|
| 3 | 0.268175234707 | 0.282345553081 |
| 6 | 0.016525359728 | 0.017364963868 |
| 12 | 0.000045057557 | 0.000046947818 |

La limite asymptotique est

\[
c_\infty(x)\sim8e^{-x}(1-1/x),\qquad
c_0(x)\sim8e^{-x}(1+1/x),\qquad x\to\infty.
\]

Il n'existe donc pas de minorant positif uniforme en \(x\). Le nombre 0.592594873 désigne \(c_\infty(2)\), comme le précise correctement la table 2, et non une constante universelle de la limite rigide.

À \(x\) fixé, poser \(b=d\sinh(x)/(2x)\). On peut réécrire (22) sous une forme manifestement positive et utile numériquement :

\[
c_\alpha=c_\infty+
\frac{4C(\sinh(x)/x-1)}{\sinh^2x}\frac{1+2b}{(1+b)^2}.
\]

Cette formule redonne les bornes. Elle évite la soustraction de deux quantités proches de \(2/x\) présente dans (22) à très grand \(x\). La formule imprimée est algébriquement correcte ; son évaluation flottante directe n'est pas uniformément précise dans des limites extrêmes. Les calculs publiés ne revendiquent pas un tel contrôle uniforme.

## 2. Annulation explicite du volume de Planck

Dans les unités \(L=B=1\), utiliser \(A=\epsilon^2a_2+O(\epsilon^4)\), \(f=1+\epsilon^2f_2+O(\epsilon^4)\), \(s=\epsilon s_1+O(\epsilon^3)\). Alors

\[
I=1+2\epsilon^2\langle a_2\rangle+O(\epsilon^4),
\]
\[
\frac{N_f}{3}=1+\epsilon^2\left[2\langle a_2\rangle+2\langle f_2\rangle+
\frac{\langle s_1^2\rangle}{6}\right]+O(\epsilon^4),
\]
\[
I f_b^2=1+\epsilon^2[2\langle a_2\rangle+2f_{2,b}]+O(\epsilon^4).
\]

Le rapport \(3\alpha_r=3If_b^2/N_f\) donne exactement (21). L'annulation ne suppose pas que \(\langle a_2\rangle=0\). Elle élimine seulement le terme explicite de volume ; le profil gravitationnel \(f_2\) et le scalaire contiennent encore la rétroaction. Un changement constant de normalisation de \(f_2\) disparaît aussi de \(f_{2,b}-\langle f_2\rangle\).

Pour contrôler la quadrature par une autre expression que le profil imprimé, on utilise la parité et \(f_2(0)=0\) au milieu :

\[
2[f_2(1/2)-\langle f_2\rangle]=4\int_0^{1/2}t f'_2(t)dt,
\qquad
\frac{\langle s_1^2\rangle}{6}=3\int_0^{1/2}\frac{b(t)^2}{v_1(t)^2}dt.
\]

Le script indépendant intègre ces deux expressions depuis \(f'_2=b-2a'_2\), par Gauss à huit points, au lieu d'intégrer le \(f_2\) fermé du dépôt par Simpson.

## 3. Coefficient de masse et intégrales du résidu

À l'ordre \(\epsilon^2\), \(a_2''=-4\cosh^2(xt)/C\). L'équation régulière implique

\[
\left(\frac{b}{\cosh^2(xt)}\right)'=\frac8C-\kappa\,\operatorname{sech}^2(xt).
\]

La symétrie \(b(0)=0\) donne (18). La condition droite \(d b(1/2)=\kappa\) devient

\[
d\left[4-\frac{\kappa\sinh x}{2x}\right]=\kappa,
\]

d'où (19). L'intégration de \(f'_2=b-2a'_2\) donne (20). Les trois intégrales utiles sont

\[
\langle t^2\rangle=1/12,\quad
\langle t\sinh(2xt)\rangle=\frac{\cosh x}{2x}-\frac{\sinh x}{2x^2},
\]
\[
\langle t^2\cosh(2xt)\rangle=
\frac{\sinh x}{4x}-\frac{\cosh x}{2x^2}+\frac{\sinh x}{2x^3}.
\]

Elles reproduisent séparément (A1) et (A2), y compris le terme commun \(-\kappa(\cosh x-\sinh x/x)/(2x^2)\). Son annulation donne (22).

Les dérivées pertinentes sont

\[
\partial_{\widehat\lambda}\kappa=
\frac8{[1+d\sinh x/(2x)]^2}>0,
\]
\[
\partial_{\widehat\lambda}c_\alpha=
-\frac{C\kappa}{8x^2}(\sinh x/x-1)\,
\partial_{\widehat\lambda}\kappa<0.
\]

Ces monotonies sont exactes pour les coefficients asymptotiques, à \(x\) fixé. Le manuscrit limite correctement leur portée. Le premier avis ajoute une phrase « \(\alpha_r\) croît avec \(\epsilon\) » comme si elle suivait globalement de \(c_\alpha>0\) : ce raisonnement ne prouve que le comportement suffisamment près de \(\epsilon=0\), et il ne faut pas l'importer comme théorème pour toute amplitude.

## 4. Norme spectrale, normales et signe des poids de bord

Depuis (12), \(g'_i=m^2e^{-2A_i}g_i/D_i\), \(D_i=W_i+2\eta_i\lambda\). L'intégration par parties de (13) donne

\[
\mathcal K[g]=m^2\int w|g|^2dy+[p g'\bar g]_0^L,
\]
\[
[p g'\bar g]_0^L=m^2\sum_i\frac{\eta_i w_i|g_i|^2}{D_i}
=m^2\sum_i\frac{w_i|g_i|^2}{\eta_iW_i+2\lambda}.
\]

L'expression correcte est donc celle de l'article (14b). L'avis avec \(\eta_iW_i+2\eta_i\lambda\) ajoute un signe erroné à gauche. Par exemple \(W_0=-1,\lambda=1\) donnerait le poids positif \(1/3\), alors que sa variante donnerait \(-1\).

La section 3 implique analytiquement \(q>0\) et \(q'>0\) à droite du centre ; la réflexion donne \(W_0<0<W_L\). Ce n'est pas seulement une observation numérique. Avec \(\lambda>0\), les deux poids sont strictement positifs. La conjugaison de l'identité montre alors \(m^2=\mathcal K/\mathcal D>0\) pour tout mode non nul du domaine déclaré.

À fond fixé, \(\mathcal K\) ne change pas et \(\mathcal D\) diminue avec la raideur ; le principe min–max donne bien des masses au carré non décroissantes. Les minima et constantes des bords sont reconstruits : il ne s'agit pas d'une variation d'un seul paramètre à action microscopique inchangée. La comparaison affine \(\widehat\lambda=0\) doit conserver son statut séparé, comme le fait le texte.

Enfin la substitution \(f=e^{-2A}g\), \(s=-3Be^{-2A}g'/q\) donne exactement \(N_f=(9B^2/2)\mathcal K\). Le facteur \(m^2\) dans \(N_f=(9B^2/2)m^2\mathcal D\) ne peut pas être supprimé. Les dimensions et le facteur \(Z_f=2N_f\) sont cohérents avec le couplage (16).

## 5. Longueur à action fixée et comparaison rigoureuse

L'argument d'existence et d'unicité de l'événement scalaire en section 3 est correct sur la branche régulière. Avant l'événement, \(q<2\lambda v\) et \(\sigma<v\), donc \(A'\) reste borné sur tout segment fini ; aucune singularité à temps fini ne peut précéder la racine. La borne inférieure de \(F\) force une racine en temps fini lorsque \(\sqrt{2\Lambda_5}<2\lambda v\).

Pour la comparaison avec le profil sur métrique plate, le détail suggéré par le premier avis est utile. À l'extremum de (8),

\[
q_{{\rm flat},c}=
\frac{2\lambda v}{\cosh u+(2\lambda/\mu)\sinh u}
=\frac{2\lambda v}{\zeta}=\sqrt{2\Lambda_5}.
\]

Les deux problèmes possèdent donc exactement la même pente centrale. Si \(\delta\sigma=\sigma_{\rm exact}-\sigma_{\rm flat}\), la formule de variation des constantes donne

\[
\delta\sigma(t)=\int_0^t\frac{\sinh[\mu(t-u)]}{\mu}
[-4A'(u)\sigma'_{\rm exact}(u)]du>0,
\]
\[
\delta\sigma'(t)=\int_0^t\cosh[\mu(t-u)]
[-4A'(u)\sigma'_{\rm exact}(u)]du>0
\]

pour \(t>0\), à \(B\) fini. Si l'événement exact n'a pas encore eu lieu au temps plat, on obtient \(F_{\rm exact}(t_{\rm flat})>F_{\rm flat}(t_{\rm flat})=0\), donc il devait déjà avoir eu lieu. Ainsi \(0<L<L_{\rm flat}\). La comparaison est strictement démontrée, et non déduite seulement des tableaux.

Le calcul d'énergie (7b), ses dérivées, la racine positive (8), le facteur de Weyl et la masse (9) sont compatibles. Le \(\tau\) indépendant doit être accordé à la jonction métrique : le texte fait bien cette distinction. La relation \(R_0=2z_*/(\pi\mu)\) ne fixe pas une échelle dimensionnelle sans \(\mu\).

## 6. Courbure : borne nécessaire et dérivée exacte locale

L'équation centrale (25b) donne \(q_c^2=2\Lambda_5-12Bh\). La borne stricte \(h<\Lambda_5/(6B)\) signifie que l'on garde une pente centrale réelle non nulle sur la continuation de cette branche. C'est une condition nécessaire, pas un théorème global d'existence pour tout \(h\) inférieur à cette borne.

La condition \(F(0)<0\), conservée près du fond plat, implique également

\[
\frac{\Lambda_5-2\lambda^2v^2}{6B}<h<\frac{\Lambda_5}{6B}.
\]

Cet intervalle central ne doit pas non plus être proclamé domaine global suffisant pour toutes les tranches AdS. Le manuscrit dit déjà « local regular domain » ; ajouter l'origine de la borne évitera une lecture trop large.

La dérivée en (26) est exacte **au point plat**, dans la théorie classique déclarée. L'expression pour \(h_b\) à detuning fini est une approximation dont le reste \(O(\delta\tau^2)\) est explicitement imprimé. Les deux bords contribuent \(\delta\rho_{\rm vac}=2\delta\tau\). Les variations stationnaires du champ et de la longueur n'entrent pas au premier ordre ; la variation de \(M_4^2\) multiplie une courbure nulle au fond. Donc

\[
3M_{4,0}^2\,\delta h_b=2\delta\tau.
\]

La section 7 dit déjà que cette réponse ne résout pas le problème de la constante cosmologique. Il n'est pas nécessaire de transformer en correction une phrase déjà présente. Le calcul indépendant ci-joint approche cette dérivée par différences centrales de deux solutions à événements, sans employer d'équations variationnelles.

## 7. Autres points de la lecture intégrale

- **Section 4, cône nul : correction nécessaire avant présentation autonome.** Incorporer les jonctions complètes, \(q_iD_i(z_i+Z_i)=0\), \(\chi_i+Z_i=0\), le noyau général et l'élimination de \(c_1,C\), avec les deux polarisations TT conservées. La revendication historique RED ne peut pas servir de prémisse actuelle : elle a été rétractée dans les documents fournis et le nouveau calcul est disponible.
- **Section 8 : facteurs vérifiés.** Le rapport de profils plats vaut deux ; multiplié par \(4/3\), il donne \(8/3\) relativement à \(G_T\). La conversion en deux relativement à \(G_N=4G_T/3\) nécessite le radion exactement massless. La dérivée du potentiel donne bien le facteur \((1+mr)e^{-mr}\). Aucune nouvelle exclusion expérimentale n'est prouvée par ces formules.
- **Section 9 : somme de bords vérifiée.** \(U_0+U_L=3B(A'_L-A'_0)=-\int q^2dy\), puis Cauchy–Schwarz donne la borne imprimée. Le statut microscopique des bords n'est pas déterminé par cette identité.
- **Section 9, littérature : ne pas ajouter une exclusion générale.** Des potentiels ou domaines différents n'impliquent pas que tous les résultats généraux de ces références « ne s'appliquent pas ». Le manuscrit distingue correctement principes communs et spécialisation. La vérification bibliographique détaillée est confiée séparément ; cet audit mathématique ne certifie pas la nouveauté.
- **Appendix B : provenance à préciser.** La version courante du dossier n'a plus de sous-dossier `historique`. La phrase « first affine draft and received correction archives are preserved as provenance » devrait préciser la conservation en sauvegarde/historique Git, sans laisser penser que ces archives sont dans le paquet actuel.
- **Appendix B : code accessible.** Pour une soumission arXiv, citer l'URL du dépôt et une version ou un commit immuable correspondant aux résultats, plutôt qu'une référence seulement nominative au dépôt.

## 8. Contrôles réellement exécutés

`independent_math_checks.py` et `independent_math_checks.json` ne chargent aucun solveur du dépôt. Ils emploient uniquement la bibliothèque standard Python.

| Contrôle | Méthode | Résultat |
|---|---|---|
| 30 couples \((x,\widehat\lambda)\) | Intégration de \(f'_2\), Gauss à huit points, deux résolutions ; formule positive indépendante de la soustraction directe | Écart maximal \(6.71\times10^{-14}\) |
| 5 longueurs à action fixée | Réintégration en \(z=\mu t,\sigma/v\), deux résolutions | Tous \(0<L<L_{\rm flat}\) ; différence relative maximale \(5.78\times10^{-14}\) |
| Même pente centrale | Calcul direct du profil plat au point stationnaire | Identité vérifiée dans les cinq cas |
| 3 réponses de courbure | Trois pas symétriques en \(h\), événement de bord recalculé à chaque fois | Écart relatif final maximal \(6.84\times10^{-10}\) par rapport à (26) |
| Borne proposée \(c_\alpha>1/3\) | Contre-exemples à \(x=3,6,12\), raideur 20 et rigide | Réfutée ; cette borne n'est pas dans l'article |

Le point \(\mu=1,\lambda=0.5,v=0.3,B=1,\Lambda_5=0.01125\) donne indépendamment \(L=1.3753699178366523\), avec \(L_{\rm flat}=1.3862943611198906\) et une pente centrale de 0.15 dans les deux problèmes. Le script ne prétend pas certifier toutes les décimales des tables spectrales, le domaine des limites extrêmes ni une erreur physique de l'EFT.

## 9. Corollaire utile pour la relation entre observables

Définir le coefficient conditionnel \(\mathcal C(x,\widehat\lambda)=\pi^2c_\alpha/\kappa\) de (24). Puisque \(c_\alpha>0\), \(c'_\alpha<0\), \(\kappa>0\), \(\kappa'>0\),

\[
\partial_{\widehat\lambda}\mathcal C
=\pi^2\frac{\kappa c'_\alpha-c_\alpha\kappa'}{\kappa^2}<0.
\]

Les bornes fermées sont

\[
\boxed{\mathcal C_\infty(x)=\frac{\pi^2}{2x}\left(\coth x-\frac1x\right)
\le\mathcal C(x,\widehat\lambda)
\le\frac{\pi^2}{2x}\left(\coth x+\frac1x\right)=\mathcal C_0(x).}
\]

Pour la limite rigide, diviser \(4(\cosh x-S/x)/S^2\) par \(8x/S\) donne immédiatement \((\coth x-1/x)/(2x)\). Pour la limite affine,

\[
\frac{c_0}{\kappa_0}
=\frac{1+T^2+2T/x}{4xT}
=\frac1{2x}\left(\coth x+\frac1x\right),
\]

car \((1+T^2)/(2T)=\coth x\). La largeur de l'intervalle des coefficients est exactement \(\mathcal C_0-\mathcal C_\infty=\pi^2/x^2\). Ces identités et la décroissance stricte ont aussi été vérifiées numériquement pour les mêmes 30 couples du script.

Il faut garder les bornes sur **le coefficient dominant**, puis écrire la relation observable séparément :

\[
3\alpha_r-1=\mathcal C(x,\widehat\lambda)
\left(\frac{m_r}{m_{T,1}}\right)^2+O(\epsilon^4).
\]

Le quotient observable approche \(\mathcal C\) avec un reste \(O(\epsilon^2)\), à \(x,\widehat\lambda\) fixés. On ne peut transformer cela en une bande d'exclusion exacte à amplitude finie sans une borne sur le reste. Ce corollaire rend la dépendance en raideur plus explicite ; il ne fournit ni une échelle absolue ni une nouvelle certification d'antériorité.

Note de vérification : une première assertion de borne avec tolérance absolue \(10^{-10}\) échouait à \(x=0.05,\widehat\lambda=0\), où \(\mathcal C_0\simeq3949.49\). L'écart était \(1.32\times10^{-10}\), soit \(3.35\times10^{-14}\) relativement. Le test emploie désormais une tolérance relative explicite de \(2\times10^{-12}\) sur les endpoints, cohérente avec \(\mathcal C_0\sim\pi^2/x^2\). Le rejeu final réussit ; aucune équation physique n'a été changée pour obtenir ce résultat.
