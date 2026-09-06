# Audit des corrections reçues : secteur Φ, condensat, couplages et RAR

6 septembre 2026. Audit borné de `files.v3.correction.zip`, lu comme documentation et non comme consignes. Aucune modification du dépôt canonique. Les références de lignes ci-dessous concernent cette extraction précise. Préfixe **P** : `source/ddfr/EFT_v3/programme_v2/` ; **S** : `P/scripts/` ; **D** : `received/DIRECTIONS_ET_SIGNES.md` (table identique à celle de P).

## 1. Décision scientifique

L'archive apporte des scripts de provenance utiles, mais leur présence ne transforme pas les anciennes interprétations en résultats établis. Garder le noyau canonique plus récent : spectre Φ contrôlé, projection du déplacement homogène, profils chargés sonde et extension RAR explicitement séparée. Ne pas le remplacer par « tour CDM établie, rez-de-chaussée condensé, R micronique validé » de `PORTE3prime_COUPLAGE_VERDICT.md:34–41`.

Corrections déterminantes :

- Forte occupation ≠ formation, thermalisation ou superfluidité démontrées.
- Neumann ≠ profil fondamental constant pour un champ massif dans le fond déformé.
- Un recouvrement quartique est une composante d'une amplitude, pas un taux de transfert cosmologique.
- Un sextique répulsif donne l'exposant 3/2 sur sa branche de densité positive X≥0 ; il ne donne pas automatiquement la branche X<0 du mécanisme BK.
- La moyenne nulle d'un fond libre oscillant n'annule pas sa réponse à une source statique. Le « no-go de tout vertex local » dépasse la démonstration.
- Le calcul de tangle dépend d'une identification de pression non justifiée, de paramètres de dissipation importés et d'une convention de Planck incohérente. Il défavorise ce scénario chiffré, pas tous les kelvons.
- « Gravité universelle » ne signifie pas « boost identique pour toutes les binaires ». Une prédiction DR4 exige le problème local avec environnement et conditions aux limites.

## 2. Scripts reçus : calcul exact, approximation et limites

### 2.1 `etape3a_phi_sector.py`

Lignes 11–14 : bonne équation de réduction,

\[
-(e^{4A}\psi_n')'+m_\Phi^2e^{4A}\psi_n=m_n^2e^{2A}\psi_n.
\]

Lignes 23–26 : bonne normalisation ∫e²ᴬψnψm=δnm et bon poids **e⁴ᴬ** du quartique. Le même poids e⁴ᴬ vaut pour le sextique local ; e⁶ᴬ écrit dans `ETAPE4_KELVONS_VERDICT.md:48` et `ETAPE4prime_BK_EN_5D.md:45` est faux. Les dimensions sont [ψ]=M¹ᐟ², [∫e⁴ᴬψ⁴]=M et [∫e⁴ᴬψ⁶]=M². Les couplages 4D valent g5 fois le premier et g6,5 fois le second.

Ligne 28 : le cas sans masse introduit artificiellement mΦ²=10⁻⁹ pour rechercher les modes excités, puis reconstruit leur profil à mΦ²=0. C'est une erreur de cohérence minuscule à la précision imprimée, pas une procédure exacte. Conserver le mode nul explicite et rechercher les racines positives du même opérateur. Lignes 19–22 : un balayage de changements de signe et `except: pass` ne garantissent ni le nombre de modes ni la convergence. Le fond commun masque les avertissements et ne contrôle pas `fsolve`/`solve_ivp.success`. Les références FEM/Galerkin canoniques sont plus sûres.

La table reçue est compatible aux chiffres imprimés avec les FEM déjà recalculées, notamment m₂L=7,078464185 et λ₂₀₀₀≈−0,00599907072 pour mΦL=3. Elle ne contient **aucun calcul de taux**. Dans un U(1) exact, une désintégration permise est n⁺→0⁺+0⁺+0⁻, sous mn>3m0 ; elle est fermée pour n=2,mΦL=3. La parité n impaire interdit le recouvrement λn000 seulement si le fond, les interactions et les bords respectent la réflexion. Un portail sur une seule brane peut la briser. Au faible warp, l'amplitude est O(A), donc le taux, lorsqu'il est ouvert, est O(A²), multiplié par le couplage au carré et l'espace de phase.

De même, nn→00 au repos produit des quanta du mode fondamental de momentum √(mn²−m0²), pas automatiquement des quanta au repos du condensat. Les facteurs de Bose concernent les modes finaux effectivement occupés. Une occupation importante à momentum quasi nul ne garantit pas l'amplification de ces sorties rapides.

### 2.2 `etape3bcd_scales_relic_condensate.py`

Lignes 6–16 : MPl=1,22×10¹⁹ GeV est **non réduit**, adapté à H=1,66√g* T²/MPl. Ce choix est correct ici, mais ne doit pas être transféré à la formule BK utilisant le Planck réduit. M5=10⁹ GeV est posé indépendamment de L ; il n'est pas reconstruit avec Mbar_Pl²=M5³∫e²ᴬdy. Les rapports de champ imprimés ne certifient donc pas à eux seuls un raccord à la gravité observée.

Lignes 17–33 : estimation par raccord de lois d'échelle, H≈meff choisi, amplitude initiale ajustée pour Ωh²=0,12. Ce n'est ni une abondance prédite ni une intégration de Boltzmann/champ cosmologique. L'usage d'un même `gstar` pour énergie et entropie et Tx=Tosc φx/φi omet les changements de g*s entre phases. Le « contrôle » ultraléger vaut 0,053, ce qui confirme une estimation de convention, pas une validation précise à 0,1. Il faut examiner fréquence, température de début, réchauffement, coupure et transitions ; certaines lignes quartiques exigent une fréquence initiale supérieure à l'échelle 1/g5 qu'elles affichent ailleurs. Une petite amplitude en unités M5 ne résout pas cette difficulté.

Lignes 34–37 : le mot `condense`/`OUI` est à remplacer par **forte dégénérescence de phase sous les conventions indiquées**. Le script mélange la longueur h/(mv) avec le seuil thermique ζ(3/2). Pour v=200 km/s défini comme dispersion unidimensionnelle, T=mv² et λth=√(2π)/(mv) : à ρ=0,4 GeV/cm³, mcrit=15,8054 eV. Le choix historique 2π/(mv) donne 31,4865 eV. La différence est conventionnelle et non une découverte de seuil. Si v est une vitesse quadratique tridimensionnelle, la conversion de température change encore. Aucun de ces nombres ne garantit relaxation, fraction condensée ou superfluidité ; la condition de thermalisation est distincte dans [Berezhiani–Khoury, §1 et §2](https://arxiv.org/pdf/1507.01019).

Lignes 38–41 : EOS quartique P=g4ρ²/(8m⁴), cs²=g4ρ/(4m⁴), et rayon d'un polytrope newtonien n=1 sont cohérents sous les approximations GP/Thomas–Fermi. Ce rayon n'est pas celui d'un halo MONDien ou d'un traceur dans un potentiel externe. La quantité 1/g5 est une échelle dimensionnelle naïve de forte interaction, pas une borne universelle de validité dérivée d'un calcul d'unitarité.

**Homogénéité.** `received/CE_QUI_MANQUE_2026-09-06.md`, C.4, doit conserver le correctif canonique : si mΦ≠0, ψ0 constante exigerait m0²=mΦ²e²ᴬ(y), impossible lorsque A varie. Dans le problème libre x=2, ε=0,30, déplacement constant et vitesse initiale nulle, les fractions d'énergie initiale excitées déjà contrôlées sont 3,14969×10⁻⁶ pour mΦL=1 et 3,38500×10⁻⁵ pour mΦL=3, avec bornes sur toute la tour. Il s'agit de fractions d'énergie initiale, pas de fractions de relique. Les profils chargés non linéaires du canonique sont des états présupposés ; leur existence et leur stabilité sonde ne calculent pas leur formation.

### 2.3 `etape4prime_BK_derivation.py`

Lignes 7–11 : la simplification est correcte **si l'action BK est postulée**, si le gradient domine X et si la symétrie sphérique/source ponctuelle est retenue :

\[
P=-\frac23\Lambda|\nabla\theta|^3,\quad
\nabla\cdot(|\nabla\theta|\nabla\theta)=\frac{\alpha\rho_b}{2\bar M_{\rm Pl}},\quad
a_0=\frac{\alpha^3\Lambda^2}{\bar M_{\rm Pl}},\quad
\rho_s=\frac{2m^2\bar M_{\rm Pl}}\alpha a_\phi.
\]

Ces identités n'établissent ni l'action BK depuis Φ, ni un halo, ni sa stabilité. Pour X<0, PXX<0 dans ce P(X) à température nulle ; l'instabilité du terme cinétique de phonon est explicitement discutée dans [BK, §4.1–4.2](https://arxiv.org/pdf/1507.01019). Il est inexact de traiter l'action à température nulle comme une réalisation finale saine en rappelant seulement plus tard une « instabilité de gradient ».

La décroissance radiale n'est pas universelle. Dans la formule sphérique profonde, ρs∝√Mb(r)/r, donc d lnρs/d ln r=½d lnMb/d ln r−1. Il faut d lnMb/d ln r<2. Pour une masse de Plummer formellement insérée, la pente vaut (b²−2r²)/[2(r²+b²)] ; elle change de signe à r=b/√2. Ce n'est pas une validation de l'approximation profonde au centre, mais cela interdit d'inférer une monotonie globale de la seule proportionnalité ρs∝aφ.

Le texte voisin utilise une borne fs≤2–3 % attribuée à Paper I pour imposer des masses. Cette traduction n'est pas fournie par le script. Le papier de binaires traite un boost et des contaminations ; sans modèle liant le boost à fs et à l'environnement, retirer ces exclusions de masse. Les estimations de densité restent conditionnelles à l'action, à α et aux données locales.

### 2.4 `etape4_kelvon_kill.py`

Ligne 7 : erreur de convention. Dans a0=α³Λ²/Mbar_Pl, il faut 2,435×10²⁷ eV et non 1,22×10²⁸ eV. Pour α=1, Λ≈0,80096 meV et non 1,79285 meV. En gardant **toutes les autres hypothèses du script** à m=0,3 eV, fs=0,03, log=10, χ2=0,3, la cellule corrigée donne ℓv=4,13294 µm, v/c=0,3183, g4 seuil≈4450, τ=2,8874×10⁻¹³ s et puissance/(ρDM H0)=7,65×10²⁶. L'ordre de grandeur reste très défavorable au scénario posé ; il n'acquiert pas pour autant le statut de résultat universel.

Les égalités de lignes 14–15 ne dérivent ni la pression des kelvons, ni le coefficient de dissipation d'un milieu sombre. La loi de Vinen, le logarithme constant et la vitesse assignée sont des hypothèses. Les régimes de turbulence ne partagent pas tous une loi unique de décroissance : une expérience primaire de turbulence quasi classique trouve notamment L∝t⁻³ᐟ², [Walmsley et al.](https://arxiv.org/abs/0710.1033). Cette source sur l'hélium ne fournit pas χ2 du modèle sombre. L'échec d'une hiérarchie ℓv≫ξ indique aussi qu'on sort du domaine du calcul en vortex distincts ; il ne permet pas de calculer avec précision la durée de vie dans ce domaine invalide.

`ETAPE4_KELVONS_VERDICT.md:10` assimile sans justification le remplissage d'une bande à la thermodynamique des kelvons. Le calcul

\[
\int_{-\sqrt{2m_k\mu}}^{\sqrt{2m_k\mu}}
\frac{dk}{2\pi}(\mu-k^2/(2m_k))
=\frac{2\sqrt2}{3\pi}\sqrt{m_k}\mu^{3/2}
\]

est celui d'une bande de **fermions libres spinless** remplie à T=0 (ou d'un modèle effectivement fermionisé à démontrer). Les modes de Kelvin du condensat sont des excitations de Nambu–Goldstone bosoniques ; voir la construction effective de [Kobayashi–Nitta](https://arxiv.org/abs/1307.6632). Pour des bosons libres avec dispersion k²/(2mk), le grand ensemble exige μk≤0 ; à T>0 la pression est √(mk/2π)T³ᐟ²Li3/2(e^(μk/T)), et non ce remplissage à μk>0. Le seul comptage d/z ne fixe donc pas le mécanisme revendiqué. Les interactions, l'éventuelle conservation des quasi-particules et l'identification de μk au X du phonon restent à établir.

## 3. Sextique : résultat analytique utilisable et obstruction précise

Avec V4=(g4/2)|φ|⁴, V6=(g6/3)|φ|⁶, φ=√(n/2m)e^(−imt+iϑ), l'énergie d'interaction NR vaut

\[
e(n)=a n^2+b n^3,\quad a=\frac{g_4}{8m^2}\ge0,
\quad b=\frac{g_6}{24m^3}\ge0.
\]

En négligeant la pression quantique, éliminer la densité signifie **maximiser nX−e(n) sous n≥0**, et non prolonger une racine sans contrainte. Pour X≤0, n=0 et P=0. Pour X>0,

\[
n=\frac{2X}{2a+\sqrt{4a^2+12bX}},\quad
P=a n^2+2b n^3,
\]

avec la limite n=X/(2a) si b=0. Pour a=0, X=g6n²/(8m³)>0 et P=g6n³/(12m³). Le dictionnaire **g6,4=1/Λ²** avec l'EOS BK positive est correct dans ces conventions. Il ne fournit ni la continuation P∝X√|X| pour X<0, ni θρb, ni les termes de température finie. La différence de branche est un obstacle réel à l'identification automatique sextique=MOND, pas un théorème interdisant toute extension.

`ETAPE4_KELVONS_VERDICT.md:12,33,38` emploie l'identité relativiste ρ=2XPX−P et annonce w=cs²=1/2. Ce X est pourtant un potentiel chimique non relativiste, X=ϑdot−mU−(∇ϑ)²/(2m). Ici la densité massique dominante est mn ; sur la branche sextique homogène, **cs²=PX/(mPXX)=2X/m**, et P/(mn)=2X/(3m), tous deux petits dans le régime NR. La relation w=1/2 d'une autre k-essence ne doit pas être importée.

Le contrôle livré compare la solution analytique contrainte à une maximisation numérique indépendante pour quartique, sextique et mélange, avec X positif, nul et négatif. Ce calcul teste le domaine de la branche ; il ne simule pas un halo.

## 4. Porte 3′ : ce qu'une moyenne temporelle peut et ne peut pas démontrer

### 4.1 Obstruction globale admissible

Une action locale **univaluée**, construite uniquement à partir d'une phase compacte θ∼θ+2π, d'amplitudes et d'opérateurs ordinaires des baryons, ne peut contenir exactement c θρb sur tout le cercle des phases : le terme change sous θ→θ+2π pour une source arbitraire non topologique. C'est une obstruction de globalité dans cette classe. Elle n'interdit pas un développement local autour d'une phase, un secteur avec branches supplémentaires ou des degrés de liberté additionnels ; leur fonctionnement et leur durée de validité devraient être dérivés.

Ainsi, remplacer `PORTE3prime:16,21` par « aucun raccord global de θρb n'est construit dans notre action minimale compacte » ; supprimer « en 5D ni ailleurs ». [Berezhiani et al.](https://arxiv.org/pdf/1810.09474) présentent l'origine microscopique du couplage comme ouverte. [Mistele](https://arxiv.org/html/1909.05710v2) distingue équilibre exact et équilibre approximatif lorsque la charge n'est que lentement violée ; il ne démontre pas l'impossibilité absolue de tout potentiel chimique ni la disparition de toute force.

### 4.2 Contre-exemple de réponse locale, calculé séparément

Prenons un scalaire réel libre massif avec terme local J(x)φ. C'est aussi la composante réelle d'un champ complexe avec portail explicitement brisant U(1), donc un membre de la classe (i) de Porte 3′. Pour une source statique,

\[
(-\Delta+m^2)\phi_J=J,\quad
\phi=\phi_{\rm libre}(t)+\phi_J,\quad
E_{\rm échange}=-\frac12\int J(-\Delta+m^2)^{-1}J.
\]

La moyenne d'une oscillation libre peut être nulle tandis que φJ ne l'est pas. Le noyau tridimensionnel est e^(−mr)/(4πr). L'approximation de contact J²/m² n'est que le début du développement à impulsion |k|≪m ; elle ne justifie pas une absence exacte de portée.

Pour un mode spatial et une source allumée à t=0, avec données initiales nulles,

\[
\ddot\phi_k+\omega_k^2\phi_k=J_k,\quad
\langle\phi_k\rangle_T=\frac{J_k}{\omega_k^2}
\left[1-\frac{\sin(\omega_kT)}{\omega_kT}\right].
\]

Le script intègre cette équation par RK4 avec 4096,8192,16384 pas ; l'erreur sur la moyenne tombe de 5,14×10⁻⁹ à 1,98×10⁻¹¹ pour T=100,37, ω=√2, J=1. Il ne choisit pas un nombre entier de périodes pour forcer l'annulation.

Le second contrôle résout indépendamment le problème elliptique pour deux sources planes lisses, **à supports disjoints**, centrées en ±2, demi-largeur 0,5, m=1, bords ±12. L'interaction exacte sur la droite infinie est −0,009461474204 par unité d'aire. La discrétisation 3072 cellules donne −0,009461496648, erreur relative 2,37×10⁻⁶ ; les raffinements successifs ont un ordre approchant 2. Le petit effet des bords finis est distinct de l'erreur de maillage. Cette interaction non nulle réfute « contact donc aucune force » ; son domaine est l'échange linéaire de portée Compton. Elle n'établit ni un couplage acceptable expérimentalement, ni une force MONDienne de portée galactique. Le noyau canonique ne contient pas ce portail tant qu'il n'est pas ajouté à l'action.

### 4.3 Couplages invariants U(1)

`PORTE3prime:12` : pour [Ob]=4, le coefficient de Φ^k Ob est M5^(−3k/2), non M5^(−3/2) pour tout k. Après projection, le facteur ψ0(b)^k doit rester explicite. Même pour k=1, le pont de volume vaut exactement c ψ0(b)√I/Mbar_Pl, I=∫e²ᴬdy ; il ne fixe pas une structure de phase ou un α BK.

`PORTE3prime:13` : dans l'approximation plate du tableau, avec la convention écrite d'un potentiel de densité positif, Vb=cρb/(2m Mbar_Pl²), **X→X−Vb**. En fond déformé, remplacer c par c Iψ0(b)². Le facteur 1/m manque dans le texte. c>0 tend à diminuer la densité où ρb augmente ; c<0 fait l'inverse. L'énoncé « poussé là où sont les baryons » n'est donc pas indépendant du signe. Le ratio c/(m²r) n'est pas sans dimension et ne peut être un rapport de forces.

Un condensat quartique homogène stable offre un second diagnostic. Pour

\[
E=\int[\frac{(\nabla\sqrt n)^2}{2m}+\frac{g}{2}n^2+V_b n-\mu n],
\]

la réponse linéaire est

\[
\delta n(k)=-\frac{V_b(k)}{g+k^2/(4mn_0)}.
\]

Elle possède une longueur de réponse ξresp=(4mgn0)^(-1/2), différente selon convention de la longueur de guérison usuelle. Le contact δn≈−Vb/g est seulement la limite kξresp≪1. Cette réponse avec gradients n'est pas une dérivation MOND, mais interdit de qualifier tout couplage de densité de contact strict. Le tableau numérique livré donne la réduction de réponse 1/(1+k²ξresp²), sans revendiquer une simulation astrophysique.

`PORTE3prime:14` : f(n)∂μθ Jμ=∂μ[fθJμ]−θ[f∂μJμ+Jμ∂μf]. La conservation de J ne supprime pas le second terme quand f varie. Pour un état précisément stationnaire avec J spatial nul et f statique, cet opérateur peut rester trivial dans les équations de phase ; on ne peut étendre ce cas à tous les profils, courants, perturbations ou couplages tensoriels. Dans une interaction jΦ·Jb, le facteur de densité fait partie du problème et doit être varié lui aussi.

## 5. Khoury, halos et DR4

`PORTE3prime:27` décrit mal Khoury 2016 comme la seule gravité de masse d'un profil. Les opérateurs à gradients modifient l'équation gravitationnelle elle-même ; [Khoury, §1 et §3](https://arxiv.org/pdf/1602.05961) distingue explicitement ce mécanisme d'une force de phonon et permet d'autres EOS. Aucune contradiction obligatoire avec une fraction 3 % n'en découle, d'autant que cette borne indépendante n'est pas établie ici.

Le canonique possède déjà une extension conditionnelle plus précise : opérateurs gravitationnels déclarés, branches radiales, et fermeture hydrostatique. La positivité d'un opérateur radial réduit ne vaut pas stabilité dynamique complète. Les intérieurs à χ(S)=0 mais χ′(S)≠0 ne sont pas globalement raccordés à χextérieur=0 sans couche de surface ou solution extérieure. Conserver ces résultats et ces réserves ; ne pas revenir à « seule piste non calculée ».

Pour DR4, une loi universelle signifie mêmes équations gravitationnelles pour les sources et sondes appropriées ; elle ne fixe pas une valeur de boost indépendante de l'accélération externe, de l'orientation, de la séparation, des phases du milieu et des limites. Inversement, renoncer à expliquer RAR ne prouve pas un boost rigoureusement nul. La branche Newtonienne du noyau minimal, ses forces de courte portée et les effets d'environnement doivent être distingués d'une prédiction instrumentale/catalogue. Ne geler aucun nombre nouveau avant ce calcul.

## 6. Réponse aux points de l'avis Article 1 concernés ici

| Objection de `audits/AVIS_ARTICLE1.md` | Réponse et conséquence pour l'article |
|---|---|
| §1–4 : conventions, contraintes, norme physique, précédent spectral | Les scripts matière n'apportent pas de nouveau contrôle de la gravitation. Conserver la démonstration canonique et la norme avec sa portée, sans présenter la reproduction d'un nombre comme preuve nouvelle. |
| §2, §5–6 : matière minimale et opérateurs additionnels | Tout portail Φ–baryons ou σ–matière doit être écrit dans une extension avant d'en utiliser le Yukawa. Le noyau à Φ=0 n'a pas d'échange linéaire de Φ par sa seule gravitation. |
| §5 : deux énergies de bord négatives, réglage du vide | Déjà traités dans le canonique `THEORIE_DDF.md`, §3 et §5 ; pas résolus par le secteur Φ. Les constantes de bord et leurs valeurs totales restent distinctes. |
| §6 : contrôle quantique | U(1) protège la charge, pas la masse ni tous les opérateurs permis. Le caractère positif des spectres sonde et le faible warp ne certifient pas une protection radiative. |
| §7.1 : originalité | Le calcul BK reçu reproduit des identités connues ; le contre-exemple local et le Legendre de cette note sont des contrôles standards, pas des revendications de nouveauté. |
| §7.4 : sélection d'une longueur | Les améliorations canoniques à action fixée sont à garder. Aucun de ces scripts matière ne fixe une valeur micrométrique à partir de constantes indépendamment connues. |
| §7.5 : tests expérimentaux | Retirer « les deux Yukawas passent » et fs≤3 % de cet ensemble sans modèle expérimental correspondant. L'existence d'une amplitude ne vaut ni exclusion ni validation. |

Le spectre stabilisé reste le premier article le plus mûr. La projection et le profil Φ peuvent être présentés dans une étude de sonde contrôlée, sans promesse de relique ou de superfluide. Ces corrections ne rendent pas le noyau inutilisable ; elles empêchent de faire porter à l'article 1 des conclusions cosmologiques ou MOND qui ne sont pas ses résultats.

## 7. Reproduction et portée des contrôles de cette étape

Les quatre scripts reçus et `common_background.py` ont été lus avant exécution. Les scripts 3bcd et 4 ont été réexécutés, avec destinations exclusivement dans `matter_rar/`. Leurs sorties reproduisent les valeurs reçues, y compris les erreurs d'interprétation et de convention signalées : cette concordance ne les corrige pas.

Une copie isolée du script 3a a été tentée avec le runtime nouvellement installé ; l'import `scipy.integrate` n'était pas disponible dans cet environnement au moment du contrôle. Aucun nouveau succès de reproduction 3a n'est revendiqué ici. La comparaison des valeurs reçues avec les sorties FEM canoniques déjà contrôlées est distincte de cette tentative. SymPy n'est pas requis par notre calcul autonome ; l'étape 4′ est contrôlée analytiquement ici, sans revendiquer l'exécution de son code SymPy.

`local_coupling_checks.py` est autonome, Python standard uniquement, sans accès réseau ni chemins absolus. Sa sortie `local_coupling_checks.json` contient les hypothèses, les raffinements et les valeurs. Il n'exécute pas les scripts reçus et ne mesure ni une probabilité de succès de DDF, ni une abondance, ni une contrainte expérimentale.

## Complément du contrôle de livraison

Après cet audit initial, les six scripts scientifiques reçus ont été exécutés dans l’environnement du coordinateur. L’étape 3a aboutit ; seul un résidu impair change de 7,63×10⁻13 à 7,62×10⁻13. Le rapport `audits/REJEU_SCRIPTS_RECUS.json` à la racine et les sorties sous `audits/rejeu_scripts_recus/` établissent ce statut final. Les scripts reçus originaux restent dans les archives sauvegardées localement, hors de l'arbre publié. Les échecs d’import éventuellement mentionnés plus haut décrivent seulement l’environnement de la première relecture.
