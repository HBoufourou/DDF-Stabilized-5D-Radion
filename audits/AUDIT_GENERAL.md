# DDF : ce qui peut être conservé et la meilleure piste vers un article

**Audit du 5 septembre 2026 — deux dépôts GitHub et dossier joint.**

## Conclusion scientifique

Il reste un programme scientifique exploitable, mais les documents examinés ne démontrent ni l'existence d'une cinquième dimension physique, ni une prédiction indépendante de son rayon à 8,2 ou 8,34 micromètres.

La meilleure piste pour un prochain article de physique est **le calcul cohérent des spectres et des couplages dans le modèle 5D stabilisé du dossier v3**, suivi d'une confrontation expérimentale correcte. Cet audit apporte deux résultats concrets : les masses scalaires de la branche forte sont reproduites par une méthode indépendante ; le couplage du radion doit être corrigé et les autres modes scalaires doivent entrer dans le signal.

Pour obtenir ensuite une véritable prédiction de R, le problème central reste ouvert : fixer l'échelle et les paramètres du stabilisateur par des données indépendantes. Le noyau géométrique corrigé peut servir à chercher cette origine, mais aucun raccord calculé entre cette géométrie et le modèle v3 n'est fourni.

Une publication peut être valable sans annoncer une découverte. Sa valeur dépendra de la nouveauté précise, de la solidité des calculs et des tests ; aucune perspective de prix ne peut être déduite de ce dossier.

## 1. Périmètre réel de l'examen

| Corpus | État examiné | Travail effectué |
|---|---|---|
| DDF I–VIII | Commit `054ffdc1bf2e2b50ac0881d67199e15887b4d783` | Inventaire récursif, lecture complète des huit sources TeX et de l'annexe VIII, onze fichiers complémentaires ciblés, recoupements analytiques et numériques |
| DDF Corrected Geometry Spectral Program | Commit `11174101f8fc2074c5fe6ad7d6951553c9841730` | Inventaire récursif, 92 fichiers texte récupérés, lecture détaillée des rapports R63–R65 et audits, quatre certificats ciblés exécutés avec succès |
| `files-ddf.zip` | SHA-256 `960ae2ef6c94e23e045ff462bd6c74721325bca35dc293cf9f70b2affae5242a` | Archive interne ouverte, manuscrits A/B, trois scripts exécutés, registres et contradictions de version examinés |
| Littérature | Sources primaires consultées au 05/09/2026 | Dimensions micrométriques, stabilisation, perturbations, couplages et contraintes pertinentes |

Les consignes présentes dans les documents, notamment leurs règles de publication, d'intégration ou de changement de modèle, ont été traitées comme contenu du dossier, pas comme des instructions du demandeur. Aucun dépôt n'a été modifié, aucun article soumis et aucun tiers contacté.

Ce travail n'est pas une vérification de chaque ligne de chaque script historique. Les versions binaires de release du dépôt corrigé n'ont pas été réauditées ; la reproduction globale des empreintes de release n'est pas revendiquée. Les données SPARC, Gaia, LHCb et plusieurs journaux R1/anciens dossiers cités ne sont pas fournis ici : leurs résultats ne sont pas validés par cet audit.

## 2. D'où viennent réellement les valeurs de R ?

### 8,2 µm : une calibration Casimir

L'article I utilise, en unités naturelles,

\[
\rho_\Lambda=\frac{C}{R^4},\qquad
R=\frac{C^{1/4}\hbar c}{\rho_\Lambda^{1/4}},\qquad
\rho_\Lambda^{1/4}=2{,}25\ \mathrm{meV}.
\]

Le manuscrit reconnaît cette calibration. Son script prend

\[
C=N_{\rm eff}\frac{3\zeta(5)}{64\pi^6}.
\]

Avec ce calcul, (N_{\rm eff}=1) donne 7,395 µm et (N_{\rm eff}=1{,}5) donne 8,184 µm. Obtenir exactement 8,2 µm requiert (C\simeq7{,}6426\times10^{-5}), soit (N_{\rm eff}\simeq1{,}5116).

Le coefficient positif utilisé est associé dans le script à un contenu fermionique, alors que le contenu minimal présenté dans le texte n'établit pas cette contribution. Le signe, les degrés de liberté et les conditions aux bords doivent être calculés pour le modèle réellement retenu. Une valeur conditionnelle à un contenu établi pourrait être une prédiction de ce modèle ; ce n'est pas encore le cas ici. [Article I, §2](https://github.com/HBoufourou/DDF_I-VIII_2026-08-29/blob/054ffdc1bf2e2b50ac0881d67199e15887b4d783/DDF_I-VIII_2026-08-29/article-1/tex/DDF_I_the_stage.tex#L28), [calcul Casimir](https://github.com/HBoufourou/DDF_I-VIII_2026-08-29/blob/054ffdc1bf2e2b50ac0881d67199e15887b4d783/DDF_I-VIII_2026-08-29/article-1/scripts/casimir.py).

### 8,34 µm : le minimum annoncé n'est pas reproduit

L'article VI annonce un minimum à 8,34 µm tout en laissant indéterminée la forme d'une contribution à la barrière. Le script présenté comme validation ne minimise pas ce potentiel : il insère R=8,2 µm, puis effectue des conversions. Ce fichier ne démontre donc pas la valeur de 8,34 µm. [Manuscrit VI](https://github.com/HBoufourou/DDF_I-VIII_2026-08-29/blob/054ffdc1bf2e2b50ac0881d67199e15887b4d783/DDF_I-VIII_2026-08-29/article-6/tex/DDF_VI_candidate_geometry.tex#L37), [script annoncé](https://github.com/HBoufourou/DDF_I-VIII_2026-08-29/blob/054ffdc1bf2e2b50ac0881d67199e15887b4d783/DDF_I-VIII_2026-08-29/article-6/scripts/verify.py).

### Le dossier v3 conserve un rayon choisi

La fonction principale de `voieI/mr_spectral.py`, ligne 72, reçoit explicitement `Rstar_um=8.2`. Les masses sans dimension sont calculées ; leur conversion en micromètres utilise ensuite ce rayon. La constitution v3 le reconnaît correctement. En revanche, son étiquette « Established » pour une cinquième dimension micrométrique prête à confusion : une proposition publiée n'est pas une existence expérimentale établie.

Le scénario de Montero–Vafa–Valenzuela propose déjà une longueur de l'ordre de \(\lambda\rho_\Lambda^{-1/4}\), avec un coefficient estimé et des conjectures de gravité quantique. Il ne détermine pas spécifiquement 8,2 µm et ne constitue pas une détection. [The Dark Dimension and the Swampland](https://arxiv.org/html/2205.12293v2).

## 3. Ce qui reste des huit articles

| Article | Partie à conserver ou retravailler | Principal obstacle physique |
|---|---|---|
| I — cadre | Réduction volume–Planck, calcul Casimir conditionnel, formulation d'un modèle effectif | Stabilisation absente et forces scalaires traitées contradictoirement |
| II — puits/tour | Problème spectral et profils de bord | Dimensions de la pente, facteur deux dans l'opérateur, mélange des parités, approximation non relativiste |
| III — milieu | Hypothèse de condensat et programme phénoménologique distinct | Microphysique des phonons, taux de transition et données nécessaires non démontrés ici |
| IV — échelles | Relations dimensionnelles explicitement conditionnelles | Plusieurs « convergences indépendantes » utilisent les mêmes entrées |
| V — construction cordiste | Certaines identités de norme et de projection | Raccord entre géométries, matière, vide et paramètres non établi |
| VI — géométrie candidate | Identités algébriques sous hypothèses | Minimum à 8,34 µm non reproduit ; cosmologie et stabilisation incomplètes |
| VII — Fano | Combinatoire de sept classes modulo deux | Automorphisme combinatoire non démontré comme symétrie physique |
| VIII — baryogenèse | Piste distincte à reconstruire | Enroulement sur intervalle, potentiel chimique et violation baryonique non dérivés |

Deux défauts de l'article II sont particulièrement faciles à vérifier. Avec ses dimensions de champs, (gJ_0) a dimension énergie³ alors que la pente (F=\epsilon/\ell) a dimension énergie² : il manque la conversion d'un gradient de masse² en pente d'énergie. Ensuite, avec (\ell=(\hbar^2/2mF)^{1/3}), l'opérateur adimensionné est \(-d^2/dx^2+x\), tandis qu'un script utilise \(-\tfrac12d^2/dx^2+x\). Cela explique l'essentiel du poids de bord 5,5 annoncé. Le dépôt contient déjà une correction de la parité dans un script qui n'a pas été propagée au manuscrit. [Article II](https://github.com/HBoufourou/DDF_I-VIII_2026-08-29/blob/054ffdc1bf2e2b50ac0881d67199e15887b4d783/DDF_I-VIII_2026-08-29/article-2/tex/DDF_II_the_well_and_the_tower.tex), [opérateur numérique](https://github.com/HBoufourou/DDF_I-VIII_2026-08-29/blob/054ffdc1bf2e2b50ac0881d67199e15887b4d783/DDF_I-VIII_2026-08-29/article-2/scripts/u_derive.py), [parités](https://github.com/HBoufourou/DDF_I-VIII_2026-08-29/blob/054ffdc1bf2e2b50ac0881d67199e15887b4d783/DDF_I-VIII_2026-08-29/article-2/scripts/spectrum.py).

Le rapprochement des échelles 9,8 et 7,6 TeV n'est pas un second ancrage : en imposant (m=\epsilon=1/R), les relations du dossier donnent directement

\[
\ell=R/\sqrt2,\quad F=\sqrt2/R^2,\quad
T^{1/4}=(6\sqrt2/\pi)^{1/4}\sqrt{\bar M_{\rm Pl}/R}.
\]

Le facteur 1,282 entre les deux échelles vient de ces mêmes hypothèses. Ce résultat retire une fausse confirmation, sans interdire d'étudier un modèle correctement défini.

## 4. Le dépôt corrigé conserve un noyau mathématique utile

Les preuves et certificats examinés soutiennent une construction torique résolue et des composantes quasi-Fano dans le domaine énoncé. Les résultats (U(2)) et (II_{18}) doivent garder la condition de généricité effective appelée A3. Quatre contrôles ciblés passent : géométrie torique indépendante, cohomologie EMS, signes/parités R64, frontières LMHS.

L'obstruction R64 vise un mécanisme particulier de tubes propres actifs du secteur fermé C4. Elle ne condamne pas toute dimension supplémentaire, ni une tour KK gravitationnelle neutre. Cette dernière reste une direction rationnelle du programme. [Rapports R63–R64](https://github.com/HBoufourou/DDF-Corrected-Geometry-Spectral-Program/tree/11174101f8fc2074c5fe6ad7d6951553c9841730/reproducibility/R65), [registre actuel](https://github.com/HBoufourou/DDF-Corrected-Geometry-Spectral-Program/blob/11174101f8fc2074c5fe6ad7d6951553c9841730/CLAIMS_CURRENT.csv).

Le pilote R65 impose la longueur (L(t)=6(1-\log_{10}|t|)) et utilise des contrôles de géométrie connue. Il ne calcule pas encore le spectre d'une métrique DDF réelle. [Pilote spectral, ligne 45](https://github.com/HBoufourou/DDF-Corrected-Geometry-Spectral-Program/blob/11174101f8fc2074c5fe6ad7d6951553c9841730/software/r65_spectral_pilot.py#L45).

Un argument indépendant explique pourquoi les seules données actuelles ne fixent pas de micromètre :

\[
g\longmapsto a^2g\quad\Rightarrow\quad
\lambda_n\longmapsto a^{-2}\lambda_n,\qquad R\longmapsto aR.
\]

Cette transformation conserve les données algébriques utilisées tout en changeant les longueurs. Il manque une métrique normalisée et une stabilisation. Un col long n'est pas automatiquement un cercle de grand rayon : localement, la couture peut comporter à la fois un cercle et un intervalle.

## 5. Le dossier v3 : corrections nécessaires avant publication

### A. Normalisation de l'action

`paperA/paperA.tex`, lignes 103–121, imprime une action avec (2M_5^3\mathcal R), mais ses équations correspondent à (M_5^3\mathcal R/2).

La variation directe de

\[
S=\int\sqrt{-g}\,[c\mathcal R-\tfrac12(\partial\sigma)^2-V]
\]

donne, pour la métrique utilisée,

\[
A''=-\frac{\sigma'^2}{6c},\qquad
12cA'^2=\tfrac12\sigma'^2-V.
\]

Il faut donc harmoniser action, terme GHY, jonctions, masse de Planck et conventions des paramètres. Les calculs indépendants ci-dessous adoptent explicitement (c=M_5^3/2), cohérent avec les équations du code. Le facteur quatre est réparable comme incohérence de convention, mais ne doit pas rester dans un manuscrit soumis.

### B. Profil hyperbolique présenté comme fond exact

Le profil (\sigma\propto\sinh[m(y-L/2)]) vérifie (\sigma''=m^2\sigma). L'équation couplée exige (\sigma''=m^2\sigma-4A'\sigma'). Les deux ne sont pas simultanément exactes pour un stabilisateur non trivial et un potentiel quadratique. Le profil analytique est une approximation sans rétroaction ; le fond numérique couplé doit le remplacer dans l'application exacte du manuscrit A.

### C. L'antériorité de l'article A doit être réévaluée

Les identités algébriques du script A passent. Cela n'établit pas leur nouveauté ni toute la dérivation depuis l'action imprimée. L'article d'Olechowski, publié en 2025, possède déjà un problème de Sturm–Liouville et une identité variationnelle sans division par la dérivée du warp, y compris en forte rétroaction. Ses équations 25–26, 46 et 48–50 sont une antériorité directement pertinente. Il faut comparer explicitement les variables, les bords et les hypothèses ; l'argument de nouveauté fondé seulement sur la restriction de Lesgourgues–Sorbo ne suffit plus. La présentation particulière de l'identité DDF peut conserver un intérêt méthodologique, à vérifier. [Stability of multibrane models](https://arxiv.org/html/2408.15343v2).

Le registre v3 dit aussi « si et seulement si » là où son identité démontre directement une condition suffisante. Une réciproque doit avoir sa preuve et son domaine propres ; elle ne vient pas de la seule positivité d'une somme.

### D. La carte d'exclusion ne manque pas seulement de données

Dans `paperB/exclusion_map.py`, la fonction `verdict` compare (\Delta(r=\lambda)/\alpha_{95}(\lambda)). Or la courbe publiée borne l'amplitude d'un potentiel Yukawa après calcul du signal expérimental. Déjà pour un unique Yukawa, (\Delta_V(\lambda)=\alpha/e), et non \(\alpha\). Cette comparaison est incorrecte même si tous les points du CSV sont remplis.

De plus, le scan des fonds n'est pas implémenté : la ligne 88 reste une invitation à insérer la grille. Les fenêtres nanométriques et le facteur d'exclusion 258 ne sont donc pas reproduits par le programme fourni.

Les 38,6 µm de Lee concernent \(\alpha=1\), à 95 %, dans le modèle Yukawa testé ; ce nombre n'est pas une frontière universelle pour le signal radion + tours. Les masses étendues, couples, paramètres instrumentaux et corrélations doivent être pris en compte, ou une borne conservative explicitement démontrée. [Lee et al., 2020](https://arxiv.org/pdf/2002.11761).

Il faut aussi distinguer correction au **potentiel** et correction à la **force** : la seconde contient (1+r/\lambda). Les couleurs du script spectral sont un indicateur interne, pas une exclusion ou une validation expérimentale.

## 6. Résultat conservé et approfondi : spectre et couplages

### Méthode indépendante

Le fond est résolu depuis son centre de symétrie, avec (L=M_5^3=1), (m_\sigma L=2) et \(\epsilon=\beta L\). Pour les fluctuations, on utilise (f), régulier lorsque (A'=0), au lieu de la variable singulière du script initial :

\[
f''+(2A'-2W)f'+(4A''-4A'W+m^2e^{-2A})f=0,
\qquad W=\sigma''/\sigma'.
\]

La condition de bord est

\[
W(f'+2A'f)-m^2e^{-2A}f=0,
\qquad
s=-3M_5^3(f'+2A'f)/\sigma'.
\]

Cette méthode évite le raccord de Frobenius et ne divise jamais par (A'). L'identité énergétique du dossier est contrôlée sur les modes obtenus. Le secteur tensoriel est calculé séparément, avec (h''+4A'h'+m_T^2e^{-2A}h=0) et conditions de Neumann.

### Résultats numériques

Ici (R_0=L/\pi) est **choisi** à 8,2 µm pour comparer au dossier. \(\lambda_r=\hbar c/m_r\) désigne la portée du radion ; \(\lambda_{T1}\) celle du premier mode tensoriel massif.

| ε | m_r L | λ_r pour R₀=8,2 µm | α_r calculé | λ_T1 | α_T1 |
|---:|---:|---:|---:|---:|---:|
| 0,050 | 0,080014 | 321,96 µm | 0,33415 | 8,193 µm | 2,66789 |
| 0,143 | 0,229415 | 112,29 µm | 0,33986 | 8,148 µm | 2,67641 |
| 0,400 | 0,645056 | 39,94 µm | 0,37716 | 7,862 µm | 2,73193 |
| 0,530 | 0,850124 | 30,30 µm | 0,40227 | 7,675 µm | 2,76969 |
| 0,700 | 1,104504 | 23,32 µm | 0,43591 | 7,428 µm | 2,82169 |
| 0,900 | 1,378494 | 18,69 µm | 0,47270 | 7,152 µm | 2,88197 |

Les masses reproduisent les valeurs correspondantes du dossier. Les trois premiers modes scalaires ont été calculés à chaque point. À ε=0,53, un resserrement de tolérance par un facteur 100 change (m_r L) d'environ (1{,}1\times10^{-11}) ; le résidu relatif de l'identité énergétique est inférieur à (2\times10^{-12}) pour ces trois modes dans ce calcul affiné. Ce sont des contrôles numériques, pas une preuve de convergence globale ni un scan complet du modèle.

### Une correction substantielle du couplage

Pour matière minimale sur le bord, sans cinétique de brane ni couplage direct additionnel au stabilisateur, la normalisation donne

\[
N_n=\int_0^L e^{2A}(3M_5^3 f_n^2+s_n^2/2)dy,
\quad
\bar M_{\rm Pl}^2=M_5^3\int_0^L e^{2A}dy,
\quad
\alpha_{s,n}=\frac{\bar M_{\rm Pl}^2 f_n(0)^2}{N_n}.
\]

La cinétique canonique a coefficient (Z_n=2N_n), et le couplage à la trace vaut (f_n(0)/\sqrt{2N_n}). Une seconde dérivation analytique retrouve, à (m_\sigma L=2),

\[
\boxed{\alpha_r=\frac13[1+0{,}98342024\,\epsilon^2+O(\epsilon^4)]}.
\]

Le signe est opposé au coefficient −0,634 du dossier. À ε=0,53, le calcul modal donne 0,40227, contre environ 0,27397 avec sa formule approximative. La stabilisation alourdit le radion, mais ne réduit pas automatiquement sa force.

Les autres modes scalaires ne disparaissent pas : à ce même point, leurs deux premières contributions supplémentaires ont \((\lambda,\alpha)\simeq(9{,}713\,\mu m,0{,}09157)\) et \((5{,}949\,\mu m,0{,}02564)\). Il faut les inclure selon la précision requise.

Les couplages tensoriels dépendent également des profils. L'amplitude plate 8/3 et l'espacement (n/R_0) ne sont plus exacts sur le fond déformé ; le calcul tensoriel explique les dernières colonnes du tableau. [Formalisme des propagateurs et profils, Callin–Ravndal](https://arxiv.org/pdf/hep-ph/0403302).

**Statut de cet apport : calcul indépendant dans le secteur gravité + stabilisateur explicitement défini.** Il ne comprend pas un fond condensé non nul de Φ, des termes de brane supplémentaires, une cosmologie complète ou une validation expérimentale. Sa nouveauté bibliographique n'est pas revendiquée.

## 7. La piste prioritaire pour l'article

**Sujet proposé : « Spectres et couplages de modèles 5D symétriques stabilisés : implications pour les dimensions micrométriques ».**

Le résultat à viser est une relation testable entre masse du radion, masses KK et amplitudes de force, avec erreurs et domaine de validité. Le rayon devient un paramètre à contraindre tant que son origine n'est pas calculée.

| Étape | Sortie concrète attendue | État après cet audit |
|---|---|---|
| Action et conventions | Une convention cohérente pour action, fond, bords et Planck | Incohérence identifiée ; convention cohérente utilisée dans le recalcul |
| Modes physiques | Spectres scalaires/tensoriels, profils et normes | Trois modes scalaires et premier tensoriel calculés sur six points à x=2 |
| Dépendance aux paramètres | Cartes en x et ε, limites analytiques, sensibilité aux bords | À étendre ; x=2 n'est pas une sélection physique |
| Domaine de validité | Courbure, gradients, opérateurs supplémentaires, corrections quantiques | À établir ; amplitude de champ seule insuffisante pour trancher |
| Signal expérimental | Somme des modes convoluée avec la réponse des expériences | À construire ; test fourni à remplacer |
| Nouveauté | Comparaison aux résultats de stabilisation, couplages et contraintes déjà publiés | Recherche ciblée à compléter avant revendication |

Le potentiel minimal, les tensions et les paramètres ne doivent pas être modifiés implicitement à chaque étape pour obtenir la fenêtre souhaitée. Explorer d'autres choix est légitime : il faut les déclarer et montrer la sensibilité des résultats.

Les mécanismes Casimir et la stabilisation d'une dimension longue ont une littérature ancienne et récente. Une construction explicite de 2026 traite déjà la stabilisation pour ADD et la dimension sombre : la contribution DDF devra être plus précise que l'affirmation « une stabilisation existe ». [Ponton–Poppitz](https://arxiv.org/abs/hep-ph/0105021), [Braun–Cicoli–Milioli–Valandro](https://arxiv.org/abs/2606.19440).

## 8. Ce qu'il faut en plus pour prédire réellement R

### Le paramètre dimensionnel manquant est visible

Le programme v3 fixe (x=m_\sigma L=2). Par conséquent,

\[
R_0=\frac{L}{\pi}=\frac{2\hbar c}{\pi m_\sigma c^2}.
\]

Tant que (m_\sigma) n'est pas fixé indépendamment, cette égalité ne sélectionne pas R. Prendre R=8,2 µm revient ici à prendre (m_\sigma c^2\simeq15{,}32\) meV. De même, la relation de Planck fixe M₅ une fois L choisi ; elle ne fixe pas séparément L et M₅.

### La stabilisation seule ne garantit pas une prédiction

Exemple analytique de réduction plate, en cadre Einstein 4D, avec longueur de référence fixe :

\[
V_E(R)=A/R+B/R^2+C/R^6.
\]

Ces termes représentent une énergie du volume, une somme de tensions et un Casimir sans masse, avec facteurs constants absorbés. À un rayon choisi R*, posons \(z=C/R_*^6\) et \(\rho=V(R_*)\). Les conditions de valeur du vide et de stationnarité donnent

\[
A/R_*=2\rho+4z,\qquad B/R_*^2=-\rho-5z,
\qquad V''(R_*)=(20z-2\rho)/R_*^2.
\]

Avec A et B libres, on peut ainsi construire un minimum stable pour des rayons choisis, lorsque (z>\rho/10). Cela ne prédit aucun de ces rayons. Le Casimir seul est monotone. Cet exemple n'est pas le potentiel complet du modèle fortement stabilisé ; il illustre pourquoi il faut fixer les coefficients indépendamment.

### Deux niveaux d'ambition possibles

1. **Prédiction conditionnelle de physique effective.** Des paramètres fixés par certaines mesures déterminent d'autres observables qui n'ont pas servi à l'ajustement. C'est une ambition scientifique valable et plus proche des calculs disponibles.
2. **Prédiction du rayon depuis la géométrie DDF.** Il faut une métrique sur la même famille résolue, un opérateur physique spin-2, le raccord aux paramètres 5D, un potentiel effectif et sa matrice de masses, puis la stabilité aux corrections. Ajouter côte à côte les dossiers géométrique et EFT ne calcule pas ces liens. La feuille de route R66–R68 identifie déjà ces problèmes. [Feuille de route corrigée](https://github.com/HBoufourou/DDF-Corrected-Geometry-Spectral-Program/blob/11174101f8fc2074c5fe6ad7d6951553c9841730/docs/ROADMAP_R66_R70.md).

Il est permis d'utiliser l'énergie noire observée comme entrée, mais il faut alors annoncer une prédiction conditionnelle à cette entrée et aux autres paramètres. La faute serait de présenter la valeur réinjectée ou ajustée comme un résultat indépendant.

## 9. Contraintes à appliquer sans les universaliser

Une dimension gravitationnelle de quelques micromètres n'est pas universellement exclue par la seule expérience de Lee : son étude donne notamment R<30 µm dans son modèle toroïdal. Cela ne valide pas DDF et ne traite pas automatiquement ses modes scalaires supplémentaires. [Lee et al.](https://arxiv.org/pdf/2002.11761).

Si des neutrinos se propagent dans la dimension, les contraintes peuvent être nettement plus fortes. Un modèle LED minimal donne (R<0{,}58\) µm ou (0{,}12\) µm à 99 %, selon l'ordre des masses et pour le neutrino le plus léger sans masse. Les masses de volume modifient ces conclusions : elles ne se transplantent pas à tout modèle 5D. [Analyse réacteurs](https://arxiv.org/abs/2510.12900), [modèles avec masses de volume](https://arxiv.org/abs/2508.04274).

La cosmologie et l'astrophysique dépendent aussi du contenu et de la production des modes. Il faut les recalculer pour la réalisation retenue, sans réutiliser automatiquement une affirmation de matière noire ou d'énergie noire des anciens articles. [Contraintes stellaires sur les grandes dimensions](https://arxiv.org/abs/2510.18975).

## Décision recommandée

Conserver la branche de stabilisation forte comme **candidat calculable**, corriger son couplage et construire son signal complet. Conserver le noyau géométrique avec ses conditions explicites. Retirer des revendications actuelles la prédiction indépendante de 8,2/8,34 µm, les exclusions/validations issues du test inadéquat et l'affirmation d'une cinquième dimension établie.

Le prochain résultat décisif est une carte physique fiable qui dise, pour une action et des paramètres donnés, quelles combinaisons de rayon, masses et couplages survivent. Le passage ultérieur à une prédiction de R demandera une origine indépendante des paramètres. C'est là que se situe le travail scientifique restant.
