# RAR : raccord 5D des coefficients et obstacles identifiés

6 septembre 2026. Développement théorique avant publication. Complément à `RAR_AUDIT_ET_PISTES.md`, section 5. Le présent calcul ne résout pas un halo : il examine les champs et opérateurs que le système statique proposé demanderait en cinq dimensions. Les identités et exemples dimensionnés sont contrôlés par `rar_matching_checks.py`, avec export `rar_matching_checks.json`.

**Résultat : un raccord formel des coefficients est possible avec un nouveau champ et de nouveaux opérateurs, mais il ne découle pas de l'action DDF minimale.** Le volume compact ne fixe ni l'accélération a₀ ni la normalisation Z. Un profil non constant ne conserve pas automatiquement la fonction rationnelle de Khoury; une simple contribution de brane positive laisse un terme gravitationnel résiduel. L'amplitude de Φ ne peut pas être substituée au champ χ indépendant sans changer les équations. Ces conclusions délimitent un modèle testable, sans inventer de complétion UV.

## 1. Conventions et correction du signe de phase

On prend la signature (−,+,+,+), le Planck réduit M₄, un potentiel gravitationnel U et un champ complexe 4D canonique φ. Une convention cohérente est

\[
\phi=\sqrt{\frac n{2m}}e^{-i\Theta},\qquad
\Theta=mt+\vartheta,\qquad
X=\dot\vartheta-mU-\frac{|\nabla\vartheta|^2}{2m}.
\tag{1}
\]

En effet, le terme temporel de \(-|\partial\phi|^2-m^2|\phi|^2\), à amplitude constante, est

\[
\frac n{2m}[(m+\dot\vartheta)^2-m^2]
=n\dot\vartheta+\frac n{2m}\dot\vartheta^2.
\tag{2}
\]

Le second terme est sous-dominant dans la limite non relativiste. La convention antérieure \(e^{-imt+i\vartheta}\) donne au contraire \(-n\dot\vartheta\). Il faut donc changer le signe de ϑ dans l'exponentielle, ou celui de son dérivé temporel dans X. Les calculs statiques déjà écrits sont inchangés après cette redéfinition cohérente.

L'invariant relativiste est

\[
Y=-\frac12g^{\mu\nu}\partial_\mu\Theta\partial_\nu\Theta
=\frac{m^2}{2}+mX+O(\dot\vartheta^2,U^2,U\dot\vartheta).
\tag{3}
\]

Ainsi [X] = 1, [Y] = 2, [n] = 3, [U] = [ϑ] = 0 en unités de masse. Cette distinction évite de confondre les formules non relativistes avec un k-essence relativiste. Voir [Son, action effective des superfluides](https://arxiv.org/abs/hep-ph/0204199) et [Khoury, équations (62)–(65)](https://arxiv.org/pdf/1602.05961).

Pour le sextique répulsif retenu, \(e(n)=g_{6,4}n^3/(24m^3)\), les équations locales restent

\[
n=\sqrt{\frac{8m^3X}{g_{6,4}}},\quad X>0,\qquad
P=\frac{g_{6,4}\rho_s^3}{12m^6},\quad
c_s^2=\frac{2X}{m}=3\frac P{\rho_s},\quad \rho_s\simeq mn.
\tag{4}
\]

Le raccord de g₆ n'engendre pas la branche BK négative; [l'appendice de BK 2015](https://arxiv.org/pdf/1507.01019) établit déjà cette limite. Le choix sextique est permis comme équation d'état d'un condensat stable dans la piste gravitationnelle. Il n'y fixe pas la loi de force.

## 2. Quelle cible 4D faut-il raccorder ?

Le système statique étudié emploie une phase sans écoulement, X = μ_c − mU, et la fonctionnelle

\[
\mathcal I=\int d^3x\left[
\frac{Z^2}{2}|\nabla\chi|^2+
M_4^2g^2\left(\frac1{1+\chi^2}+\frac{\chi^2g^2}{9a_0^2}\right)
+e(n)+\frac{|\nabla n|^2}{8mn}
+U(\rho_b+\rho_{KK}+mn)-\mu_c n\right],
\quad g=|\nabla U|.
\tag{5}
\]

χ est sans dimension; son champ canoniquement normalisé, si la cinétique temporelle a le même coefficient, est q = Zχ. On a [Z] = [a₀] = 1, [M₄²] = 2. Trois coefficients différents apparaissent : M₄², Z² et M₄²/(9a₀²). Une seule relation de volume ne peut les déterminer tous.

Le coefficient à raccorder au niveau d'une covariantisation est notamment

\[
\mathcal L_4\supset\frac{M_4^2}{2}R_4
\left[\frac1{1+\chi^2}
+\frac{\chi^2(\partial Y)^2}{9m^4a_0^2}\right].
\tag{6}
\]

L'équation (6) **n'est pas à elle seule la théorie recherchée**. Khoury montre que ce choix naïf donne un glissement entre potentiels de lentillage et de dynamique. Sa construction ajoute des opérateurs du fluide normal et du superfluide; ses équations comportent des dérivées temporelles supérieures, dont la position des modes supplémentaires par rapport à la coupure doit être contrôlée. Voir [Khoury 2016, §6, équations (67)–(73)](https://arxiv.org/pdf/1602.05961).

Les relations qui suivent raccordent donc des **coefficients nécessaires**, pas une action complète déjà saine. Elles sont utiles précisément parce qu'elles rendent visibles les ingrédients manquants.

## 3. Champ réel dans le bulk : normalisation et paramètres libres

On conserve d'abord le fond d'intervalle comme référence de calcul :

\[
ds_5^2=e^{2A(y)}g_{\mu\nu}(x)dx^\mu dx^\nu+dy^2,
\quad I_2=\int_0^Ldy\,e^{2A},\quad M_4^2=M_5^3I_2.
\tag{7}
\]

Cette dernière identité suppose l'absence de terme d'Einstein induit sur les branes à χ = 0. Il faut la modifier si un tel terme est ajouté. Le Planck mesuré est normalisé dans la phase gravitationnelle de référence.

Introduisons un réel H₅, de dimension 3/2, et un ansatz de mode

\[
H_5(x,y)=\zeta(y)\chi(x)=h(y)q(x),
\quad \zeta=Zh,\quad
\int dy\,e^{2A}h^2=1.
\tag{8}
\]

Pour une cinétique 5D canonique,

\[
Z^2=\int dy\,e^{2A}\zeta^2,\qquad [h]=\frac12.
\tag{9}
\]

Un terme de bord \(-k_i(\partial H_5)^2/(2\mathcal M_i)\), avec k_i sans dimension, ajouterait \(e^{2A_i}k_i\zeta_i^2/\mathcal M_i\) à Z². La positivité de la norme totale serait alors une condition supplémentaire.

La normalisation canonique ne fixe pas Z : elle fixe q. Z est l'échelle qui relie q au champ sans dimension présent dans la fonction d'interaction. Il faut connaître cette fonction et ses coefficients pour le déterminer. De même, la masse 4D de H₅ et son profil doivent être calculés avec sa nouvelle action et ses conditions de bord; ils ne sont pas ceux de Φ ou du radion par simple changement de nom.

### Une obstruction exacte due au profil

Supposons qu'on postule dans le bulk une fonction rationnelle

\[
F_5(H_5)=\frac1{1+H_5^2/f_5^2},\qquad [f_5]=\frac32.
\tag{10}
\]

Pour le coefficient de R₄, la réduction donne, dans l'approximation de profil fixé,

\[
F_4(\chi)=\left\langle\frac1{1+s(y)^2\chi^2}\right\rangle,
\quad s=\frac\zeta{f_5},\quad
\langle B\rangle=\frac1{I_2}\int dy\,e^{2A}B.
\tag{11}
\]

Après normalisation de χ pour que \(\langle s^2\rangle=1\), son développement est

\[
F_4=1-\chi^2+\langle s^4\rangle\chi^4+O(\chi^6),
\qquad \langle s^4\rangle-1=\operatorname{Var}(s^2)\geq0.
\tag{12}
\]

La cible \(1/(1+\chi^2)\) exige déjà \(\operatorname{Var}(s^2)=0\). Sous mesure positive, cela impose s² constant presque partout. Le constat n'est pas une approximation numérique ni une recherche bibliographique négative : c'est une obstruction algébrique pour cette classe de fonctions et un profil fixé.

Par exemple, si s² prend les valeurs 1/2 et 3/2 avec poids égaux, le coefficient quartique est 1,25 et F₄(1) = 0,533333, contre 0,5 pour la cible. Ce profil à deux valeurs sert seulement à illustrer le théorème; ce n'est pas un mode DDF.

Un profil constant, comme celui d'un scalaire libre sans masse avec Neumann homogène **avant** introduction des nouveaux couplages, évite cette obstruction. Un choix de fonctions de Wilson dépendant de y ou de σ peut aussi compenser les moments, mais introduit de nouvelles fonctions à déterminer. Un tel ajustement ne devient pas une prédiction géométrique.

## 4. Quels opérateurs 5D peuvent porter ces coefficients ?

### 4.1 La substitution R₄ → R₅ n'est pas innocente

Sur le fond, \(R_5=-8A''-20(A')^2\) est généralement non nul. Un opérateur \(-\xi_5H_5^2R_5/2\) apporte un potentiel de masse local \(\xi_5R_5\) à H₅ et modifie aussi ses conditions de bord quand les termes de Gibbons–Hawking associés sont inclus. On ne peut donc garder gratuitement un mode constant sans masse. Le spectre réel demande l'opérateur complet, les termes de bord et les éventuelles annulations : la seule contribution de courbure dans le bulk n'est pas une formule de masse du mode 4D.

Par ailleurs, si \(Y_5=e^{-2A}Y_4\),

\[
G^{AB}\partial_AY_5\partial_BY_5
=e^{-6A}(\partial Y_4)^2
+4(A')^2e^{-4A}Y_4^2.
\tag{13}
\]

Le deuxième terme provient du gradient dans la dimension compacte. Même un état 4D homogène le possède lorsque A' ≠ 0. L'oublier transforme le modèle pendant la réduction.

### 4.2 Une classe projetée explicite pour le comptage

Pour isoler les gradients 4D, on peut envisager une classe **nouvelle** d'opérateurs définis sur les tranches du stabilisateur. Lorsque \((\nabla\sigma)^2>0\), poser

\[
N_A=\frac{\nabla_A\sigma}{\sqrt{(\nabla\sigma)^2}},
\quad h_{AB}=G_{AB}-N_AN_B,
\quad D_A=h_A{}^B\nabla_B.
\tag{14}
\]

N est spacelike; il ne définit pas le référentiel temporel du fluide. La courbure intrinsèque des tranches peut s'écrire, par Gauss,

\[
\mathcal R_\parallel=R_5-2R_{AB}N^AN^B+K^2-K_{AB}K^{AB}
=e^{-2A}R_4
\tag{15}
\]

sur l'ansatz de référence. La combinaison est covariante si σ est traité comme un champ, mais elle ajoute des dérivées et des couplages au stabilisateur. Elle n'appartient pas à l'action minimale du premier article. Sa limite σ' → 0 est singulière et sa dégénérescence dynamique n'est pas démontrée ici.

Une classe permettant le raccord de coefficients serait

\[
\Delta\mathcal L_5=
\frac{M_5^3}{2}[F_5(H_5)-1]\mathcal R_\parallel
+\frac{D_5}{2}H_5^2\mathcal R_\parallel(DY_5)^2
+\mathcal L_{5,\,\mathrm{compl}},
\tag{16}
\]

ajoutée à l'Einstein–Hilbert 5D de référence et à la cinétique de H₅. \(\mathcal L_{5,\mathrm{compl}}\) désigne les opérateurs encore à spécifier pour les contraintes, le lentillage, la composante normale et les termes de bord. Ce symbole ne prétend pas qu'ils existent déjà sous une forme vérifiée. La seule partie explicitement écrite ne fournit pas la bonne gravité relativiste.

Le comptage est exact :

| Objet | Dimension de masse |
|---|---:|
| H₅ | 3/2 |
| \(\mathcal R_\parallel\) | 2 |
| Y₅ et \((DY_5)^2\) | 2 et 6 |
| coefficient ξ₅ de \(-H_5^2\mathcal R_\parallel/2\) | 0 |
| coefficient D₅ de \(H_5^2\mathcal R_\parallel(DY_5)^2/2\) | −6 |
| \(\int e^{-4A}\zeta^2dy\) | 2 |

La projection retire le second terme de (13), et l'opérateur de dimension élevée porte la mesure de réduction

\[
\sqrt{-G}\,\mathcal R_\parallel(DY_5)^2H_5^2
\longrightarrow\sqrt{-g}\,e^{-4A}\zeta^2\chi^2R_4(\partial Y_4)^2.
\tag{17}
\]

Ce poids e^(−4A) est propre à cet opérateur avec dérivées et courbure. Il ne remplace pas le poids e^(4A) des potentiels quartiques ou sextiques déjà corrigés.

### 4.3 Relations de raccord à vérifier

Pour un coefficient ξ₅ constant et une cinétique canonique, le terme quadratique de F₄ impose

\[
\boxed{\xi_5Z^2=M_4^2.}
\tag{18}
\]

En notant \(J_{-4}=\int dy\,e^{-4A}\zeta^2\), le second opérateur doit satisfaire

\[
\boxed{D_5J_{-4}=\frac{M_4^2}{9m^4a_0^2},\qquad
a_0^2=\frac{M_4^2}{9D_5m^4J_{-4}}.}
\tag{19}
\]

Le signe D₅ > 0 est requis par cette cible lorsque la norme est positive. Écrire \(D_5=c_D/\mathcal M^6\) sépare une échelle et un coefficient de Wilson sans dimension; leur choix reste libre. L'inverse sixième racine de D₅, à elle seule, n'est pas une coupure physique prouvée : celle-ci dépend aussi des normalisations du fond et des interactions entre modes.

L'équation (18) ne contrôle que le terme en χ². L'équation (12), puis les moments supérieurs, sont nécessaires pour la fonction complète à χ non petit. L'équation (19) ne contrôle qu'un opérateur de la complétion. Les termes permettant les bonnes contraintes métriques doivent aussi être raccordés, avec leurs propres poids.

### 4.4 Limite plate : le rayon s'élimine

Pour A = 0 et H₅ = f₅χ constant, la fonction (10) se réduit exactement à celle de Khoury et

\[
Z^2=f_5^2L,\quad M_4^2=M_5^3L,\quad J_{-4}=f_5^2L=Z^2.
\tag{20}
\]

On obtient alors

\[
\boxed{\xi_5=\frac{M_5^3}{f_5^2}=\frac{M_4^2}{Z^2},\qquad
a_0^2=\frac{M_5^3}{9D_5 f_5^2m^4}.}
\tag{21}
\]

**L a disparu du dernier rapport.** Avec ces coefficients fondamentaux fixés, agrandir le volume ne sélectionne pas a₀. Si l'on impose M₄ mesuré et choisit L, on peut en déduire M₅; cela ne fixe toujours pas f₅, D₅ ou m. Une relation observée entre a₀ et R aurait besoin d'une dynamique supplémentaire ou d'autres mesures de ces coefficients.

Ce résultat est un raccord constructif limité : les coefficients écrits peuvent être choisis pour reproduire les coefficients 4D. Il ne prouve ni l'existence d'une troncature cohérente, ni l'absence de modes supplémentaires, ni la stabilité radiative de ces choix.

## 5. Diagnostic dimensionné : Z est aussi une condition dynamique

À g = a₀ maintenu fixé, sur le minimum adiabatique de la cible, la courbure locale du potentiel divisée par Z² donne le diagnostic de masse à fond gravitationnel prescrit :

\[
m_\chi^2=\frac{16}{27}\frac{M_4^2a_0^2}{Z^2},\qquad
m_\chi r=\frac4{3\sqrt3}\sqrt{\xi_5}\,\frac{a_0^{SI}r^{SI}}{c^2}.
\tag{22}
\]

Avec a₀ = 1,2×10^(−10) m/s² et r = 10 kpc, \(a_0r/c^2=4,1199\times10^{-7}\). La condition mχr = 1 correspond à ξ₅ ≈ 9,94×10¹² dans la classe (18). Un suivi adiabatique marqué demande davantage. Un coefficient ξ₅ de l'ordre de un donne Z de l'ordre de M₄ et échoue à ce diagnostic galactique local.

Le potentiel auto-cohérent peut répondre à une perturbation de χ. En géométrie radiale, après élimination de g à flux gravitationnel fixé, la courbure devient le complément de Schur \(V_{\chi\chi}-V_{\chi g}^2/V_{gg}\). Au même point g = a₀, χ² = 2, son coefficient est \(64M_4^2a_0^2/135\), au lieu de \(16M_4^2a_0^2/27\), soit un facteur 4/5. Le diagnostic mχr = 1 donnerait alors ξ₅ ≈ 1,243×10¹³. Ni l'un ni l'autre de ces contrôles locaux n'est une analyse de stabilité du halo entier ou de propagation relativiste.

Cela ne constitue pas un no-go contre Khoury : Z y est un paramètre indépendant. Cela montre qu'un raccord minimal à coefficient non minimal d'ordre un n'explique pas ce paramètre. Un grand ξ₅ exige un examen des interactions et de la coupure après normalisation canonique; cet audit ne lui attribue pas un seuil universel.

Les exemples numériques prennent un intervalle **plat**, R = 3 μm imposé, m = 0,1 eV imposé et M₄ = 2,435×10²⁷ eV. Ils calculent M₅, f₅², ξ₅ et D₅ pour plusieurs Z, puis retrouvent le a₀ imposé par (21). Ce test valide le raccord dimensionnel et illustre ses libertés; ce n'est pas une nouvelle estimation de a₀.

La discussion originale de Z distingue suivi adiabatique et corrections quantiques, avec un domaine approximatif dépendant des accélérations étudiées; voir [Khoury, équations (32)–(43)](https://arxiv.org/pdf/1602.05961). Son équation (44) concerne \(w=P/\rho\), et non une relation entre a₀ et un rayon compact.

## 6. Variante : χ localisé sur une brane

Un champ sans dimension χ sur la brane i avec cinétique \(-Z_i^2(\partial\chi)^2/2\) possède, dans les coordonnées de g₄,

\[
Z_4^2=e^{2A_i}Z_i^2.
\tag{23}
\]

Un terme d'Einstein de brane \(M_i^2f_i(\chi)R[\gamma_i]/2\) contribue \(e^{2A_i}M_i^2 f_i(\chi)\) au coefficient gravitationnel 4D. Aux bords du fond symétrique de référence A_i = 0, les facteurs de redshift sont égaux à un.

Supposons que le bulk reste Einsteinien et que la seule modification soit une contribution de brane positive \(f_i=1/(1+\chi^2)\). En définissant

\[
\gamma=\frac{e^{2A_i}M_i^2}{M_5^3I_2+e^{2A_i}M_i^2},\qquad 0\leq\gamma<1,
\]

la fonction réduite est

\[
F_4(\chi)=1-\gamma+\frac\gamma{1+\chi^2},\qquad
\lim_{|\chi|\to\infty}F_4=1-\gamma>0.
\tag{24}
\]

Cette classe n'atteint pas la cible dont le premier terme tend vers zéro. En ajoutant le terme positif en g⁴χ² de (5), le plancher reste présent : le régime modifié peut exister dans une fenêtre, mais il ne garde pas la même asymptotique jusqu'à g → 0. Si γ est proche de un, cette fenêtre peut être large; il faut la calculer.

Éliminer ce plancher demande que la modification affecte aussi le secteur de volume, que la gravité de brane domine de manière appropriée, ou que d'autres opérateurs compensent le terme résiduel. Une contribution d'Einstein négative de brane n'est pas un raccourci validé : la positivité du mode graviton intégré ne prouve pas celle de toute la tour KK.

Pour le champ canonique local q_i = Z_iχ, l'opérateur \(D_iq_i^2R[\gamma_i](D Y_i)^2/2\) a [D_i] = −6. À phase commune Y_i = e^(−2A_i)Y₄, son coefficient réduit en χ vaut \(D_iZ_i^2e^{-4A_i}/2\). Le raccord analogue à (19) est donc

\[
D_iZ_i^2e^{-4A_i}=\frac{M_4^2}{9m^4a_0^2}.
\tag{25}
\]

Les masses et accélérations dans le membre droit sont exprimées dans les coordonnées 4D choisies. Cette identité n'élimine ni le plancher (24), ni les opérateurs complémentaires requis par le lentillage.

## 7. Peut-on éviter un champ nouveau ?

### 7.1 Identifier χ à l'amplitude de Φ change le problème

Si l'on pose pour le mode 4D

\[
\phi=\frac{Z\chi}{\sqrt2}e^{-i\Theta},
\tag{26}
\]

la cinétique radiale donne bien \(-Z^2(\partial\chi)^2/2\), mais la densité n'est plus indépendante :

\[
n=mZ^2\chi^2,\qquad \rho_s=m^2Z^2\chi^2.
\tag{27}
\]

Pour le sextique, la partie non relativiste devient

\[
\mathcal L_{NR}\supset mZ^2\chi^2X-
\frac{g_{6,4}Z^6\chi^6}{24}-\frac{Z^2}{2}|\nabla\chi|^2.
\tag{28}
\]

Elle contient une force de rappel dépendant de X et une interaction χ⁶, absentes du potentiel en χ seul dans (5). On ne peut plus faire varier n et χ indépendamment. La condition locale du condensat serait \(\chi^4=8mX/(g_{6,4}Z^4)\), et non \(\chi^2=3a_0/g-1\) en général.

Imposer tout de même la dernière égalité donnerait \(\rho_s=m^2Z^2(3a_0/g-1)\). Elle diverge lorsque g → 0 et s'annule à g = 3a₀, exactement là où l'EFT de phase perd son support. Les gradients et un véritable changement de phase pourraient modifier ce comportement; ils définiraient une **autre** théorie à résoudre, pas une identification sans conséquence.

Le potentiel minimal en \(|\Phi|\) ne produit pas les opérateurs (16). Les ajouter peut être envisagé, mais modifie le spectre, le fond et les couplages déjà testés. La phase peut servir à construire Y et le référentiel du fluide; elle ne fournit pas gratuitement un second champ auxiliaire indépendant.

### 7.2 Identifier χ au radion ou au stabilisateur conserve une masse de rappel

Un mode scalaire existant, canoniquement normalisé q = Zχ avec masse positive m_*, apporte \(m_*^2Z^2\chi^2/2\) au potentiel. À χ = 0, la courbure totale de la cible serait

\[
V_{\chi\chi}(0)=m_*^2Z^2+
2M_4^2g^2\left(-1+\frac{g^2}{9a_0^2}\right).
\tag{29}
\]

Pour qu'elle devienne négative quelque part, il faut

\[
m_*^2Z^2<\frac92M_4^2a_0^2.
\tag{30}
\]

Même dans ce cas, elle redevient positive lorsque g → 0 si m_* ≠ 0 : la branche MOND asymptotique de la cible n'est plus obtenue. Une annulation ou un mécanisme d'environnement peut changer cette conclusion; cela demande de modifier l'action et de refaire la stabilisation. Le radion de portée micrométrique déjà calculé ne constitue donc pas le χ sans potentiel de (5).

## 8. Covariance et conditions de santé encore nécessaires

Le potentiel U et le seul gradient |∇U| ne sont pas des scalaires 5D généraux. Il faut préciser le champ temporel du fluide, la géométrie induite, le couplage de la matière et les contraintes métriques. Le vecteur spacelike N de (14) ne remplit pas le rôle du vecteur timelike du fluide normal.

En particulier, écrire un scalaire \(R F(Y,\partial Y)\) assure une covariance formelle, pas des équations saines. Y contient déjà une dérivée de Θ; ∂Y contient ses dérivées secondes. Les opérateurs complémentaires peuvent ajouter d'autres dérivées. Une action acceptable doit soit vérifier des contraintes de dégénérescence éliminant les modes indésirables, soit situer explicitement les modes supplémentaires au-dessus d'une coupure utilisable sur le fond retenu. La stabilité statique de (5) ne suffit pas.

Les contrôles à effectuer sur une action complète choisie sont concrets : norme de tous les modes, matrice cinétique après élimination des contraintes, symbole principal et propagation, masse de χ sur les deux branches, limite de phase normale, nouvelle tour KK et conditions de bord, couplage de la métrique physique aux photons et aux baryons, puis domaine de validité des opérateurs. Des problèmes d'hyperbolicité existent dans certaines complétions de SFDM examinées par [Hertzberg, Litterer et Shah](https://arxiv.org/abs/2105.02241); ce résultat n'est pas une exclusion de toutes les constructions possibles.

La preuve du premier article concerne son action scalaire–gravité donnée. Elle ne s'étend pas automatiquement à une théorie contenant (16), à un couplage de courbure de brane ou à une identification nouvelle de l'amplitude sombre.

## 9. L'alternative à deux champs n'est pas un raccourci de raccord

[Mistele 2021](https://arxiv.org/abs/2009.03003) sépare le champ qui porte le potentiel chimique de celui qui médie la force, puis ajoute un secteur superfluide standard pour corriger la stabilité. Les équations (15), (24)–(34) explicitent cette séparation; l'appendice B propose des champs complexes associés. L'origine du couplage brisant la symétrie phase–baryons y reste ouverte. Cette option offre une seconde architecture à comparer, mais ne dérive ni les coefficients de DDF ni un couplage global linéaire depuis un unique champ compact. Elle ajoute des degrés de liberté et des opérateurs distincts de la voie gravitationnelle χ.

Le résultat récent utile est donc une leçon de structure : séparer des rôles physiques peut éviter une contradiction, mais cette séparation doit apparaître dans l'action et dans les comptages. Deux noms attribués au même mode ne créent pas deux variations indépendantes.

## 10. Décision de développement et résultat publiable limité

La prochaine action candidate peut conserver le noyau de stabilisation comme fond de référence et **ajouter explicitement H₅**, avec un profil, une cinétique, une protection ou un réglage de son potentiel, et des opérateurs de gravité déclarés. Les relations (12), (18), (19) et leurs équivalents de brane fournissent des tests de raccord avant tout ajustement de galaxies. Un profil constant donne un premier point de comparaison calculable; sa survie après couplage doit être vérifiée.

Le système radial χ–U du travail parallèle teste la fonctionnelle (5). Il ne vérifie ni (16), ni ses opérateurs complémentaires, ni la stabilité relativiste. Un accord radial établirait un résultat pour cette EFT statique; le lien à R ne pourrait être revendiqué qu'après un calcul supplémentaire fixant les coefficients libres autrement que par les valeurs recherchées.

Le présent développement fournit quatre résultats limités mais exploitables : une correction de convention de phase; des relations de normalisation et de dimensions explicites; une obstruction par les moments des profils et un plancher pour la variante de brane positive; l'impossibilité d'identifier sans modification l'auxiliaire χ à la densité indépendante ou à un radion massif. Une étude technique peut s'appuyer sur ces propositions après examen d'antériorité. Aucune priorité générale ni solution de la RAR n'est revendiquée.

### Références primaires

- D. T. Son, *Low-Energy Quantum Effective Action for Relativistic Superfluids* (2002), [arXiv:hep-ph/0204199](https://arxiv.org/abs/hep-ph/0204199).
- L. Berezhiani et J. Khoury, *Theory of Dark Matter Superfluidity*, Phys. Rev. D 92, 103510 (2015), [arXiv:1507.01019](https://arxiv.org/abs/1507.01019), [DOI](https://doi.org/10.1103/PhysRevD.92.103510). Appendice : sextique et branche physique.
- J. Khoury, *Another Path for the Emergence of Modified Galactic Dynamics from Dark Matter Superfluidity*, Phys. Rev. D 93, 103533 (2016), [arXiv:1602.05961](https://arxiv.org/abs/1602.05961), [DOI](https://doi.org/10.1103/PhysRevD.93.103533). Équations (18)–(29), (32)–(44), (62)–(73).
- T. Mistele, *Three problems of superfluid dark matter and their solution*, JCAP 01 (2021) 025, [arXiv:2009.03003](https://arxiv.org/abs/2009.03003), [DOI](https://doi.org/10.1088/1475-7516/2021/01/025).
- M. P. Hertzberg, J. A. Litterer et N. Shah, *Acausality in Superfluid Dark Matter and MOND-like Theories*, JCAP 11 (2021) 015, [arXiv:2105.02241](https://arxiv.org/abs/2105.02241), [DOI](https://doi.org/10.1088/1475-7516/2021/11/015).

Les métadonnées et les passages utilisés ont été consultés dans les articles des auteurs. Le mapping de coefficients, les tests de profils et les exemples numériques ci-dessus sont les calculs de cette note; ils ne sont pas attribués aux articles cités.
