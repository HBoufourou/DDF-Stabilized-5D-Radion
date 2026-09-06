# DDF : un intervalle stabilisé et un secteur scalaire sombre contrôlé

**Version corrigée du modèle effectif - 6 septembre 2026**

Hicham Boufourou - développement et vérifications assistés par IA.

Dépôt unique : [HBoufourou/DDF-Stabilized-5D-Radion](https://github.com/HBoufourou/DDF-Stabilized-5D-Radion).

## Résumé

Cette version définit DDF comme un modèle classique de gravité à cinq dimensions sur un intervalle physique, stabilisé par un champ scalaire réel et des potentiels quadratiques aux bords. Un champ complexe doté d'une symétrie de phase fournit un secteur sombre minimal. L'action, les paramètres d'entrée, les conditions aux bords et les observables sont explicités dans un même cadre.

Le noyau possède une branche symétrique à longueur déterminée par les couplages, des secteurs scalaire et tensoriel linéairement stables dans le domaine déclaré, et des masses et couplages calculables. Un nouveau prolongement détermine localement la longueur et la courbure à quatre dimensions lorsque la tension commune des bords est fixée indépendamment. Le secteur sombre possède une tour positive, une réduction approchée quantitativement contrôlée et des profils stationnaires chargés dont la stabilité linéaire sonde est établie sur métrique fixe.

Ces résultats définissent un noyau théorique précis. Ils ne prédisent pas encore une longueur micrométrique à partir de constantes indépendamment connues, une abondance cosmologique ou la relation d'accélération radiale des galaxies. L'étude RAR et les candidats de théorie des cordes sont conservés comme extensions évaluées, avec leurs nouvelles solutions et leurs conditions de raccord. Ils ne changent pas implicitement l'action du noyau.

## 1. Ce qui constitue désormais la théorie

**Principe 1 - Une action commune.** Les équations du fond, les conditions aux bords, le spectre et les couplages viennent de la même action. Un paramètre choisi dans cette action reste fixe lorsqu'on cherche une solution. Un nouveau portail, champ ou terme de bord doit apparaître explicitement avant d'être utilisé.

**Principe 2 - Un intervalle physique.** La cinquième coordonnée parcourt [0,L]. Deux frontières délimitent le domaine et portent leurs potentiels. La matière visible est minimale sur le bord y=0. Nous n'ajoutons pas des fluctuations indépendantes d'objets-branes mobiles à ce problème de frontières ; leurs éventuels degrés de liberté demanderaient une autre analyse.

**Principe 3 - Une stabilisation dynamique.** Le scalaire réel préfère des valeurs opposées aux deux extrémités. Sa masse de bulk, les raideurs et les valeurs préférées des bords participent à la détermination de L. Le rayon conventionnel est R0=L/π. En géométrie déformée, la portée du premier graviton massif doit être calculée et peut différer de R0.

**Principe 4 - Un spectre normalisé physiquement.** Les masses seules ne déterminent pas la force. Les normes canoniques et les profils sur la brane fixent également les amplitudes. La stabilité est affirmée uniquement pour les secteurs et conditions réellement traités.

**Principe 5 - Une charge sombre conservée dans l'action minimale.** Le champ complexe Φ possède une symétrie U(1). Celle-ci conserve une charge totale ; elle ne protège pas sa petite masse et ne conserve pas le numéro d'un niveau KK. L'amplitude initiale, la charge et la distribution des modes sont des données d'état tant que leur origine n'a pas été calculée.

**Principe 6 - Des prédictions conditionnelles testables.** Une même action doit servir aux différentes observations. Ses paramètres libres sont déclarés. Ils ne sont pas ajustés séparément pour chaque phénomène puis présentés comme dérivés. Une donnée géométrique sans dimension ne devient une longueur en mètres qu'avec une échelle physique indépendante.

Dans cette version, « noyau fermé » signifie que le modèle et ses règles de calcul sont spécifiés, et que les résultats ci-dessous ont des hypothèses identifiables. Cela ne signifie ni théorie fondamentale complète, ni démonstration de sa vérité expérimentale, ni résolution générale de toute son évolution non linéaire.

## 2. Action et conventions

Nous utilisons la signature (-++++) et ℏ=c=1. Posons B=M5³>0. Les mesures de volume sont celles de la métrique cinq-dimensionnelle g et des métriques induites γ. L'action est

```text
S = ∫bulk √(-g) [ B R5/2 - (∂σ)²/2 - V(σ)
                  - |∂Φ|² - mΦ²|Φ|² - g5|Φ|⁴/2 ]
    + B ∫frontières √(-γ) K
    - ∫bord0 √(-γ) U0(σ) - ∫bordL √(-γ) UL(σ)
    + Svisible[γ0, matière visible].

V(σ) = Λ5 + μ²σ²/2
U0(σ) = τ + λ(σ+v)² ; UL(σ) = τ + λ(σ-v)²
```

K est la trace de la courbure extrinsèque avec normale sortante. Les coefficients du terme d'Einstein et du terme GHY sont respectivement B/2 et B, pour **un seul intervalle**, sans facteur supplémentaire de copie.

Le domaine principal prend μ, λ, v>0, mΦ²>0 et g5≥0. La limite mΦ=0 est un contrôle distinct. Il n'y a dans cette version minimale ni portail direct Φ-matière visible, ni masse de brane pour Φ, ni couplage σ²|Φ|², ni champ χ de modification de la gravité.

| Paramètre | Dimension en puissance de masse | Rôle |
|---|---:|---|
| B=M5³ | 3 | Coefficient gravitationnel |
| μ, λ, mΦ | 1 | Masse du stabilisateur, raideur de bord, masse de bulk de Φ |
| v | 3/2 | Valeur préférée du stabilisateur |
| Λ5 | 5 | Constante de potentiel du bulk |
| τ | 4 | Constante commune des potentiels de bord |
| g5 | -1 | Interaction quartique de Φ |

L'absence des opérateurs additionnels définit la troncature classique retenue ; U(1) ne les interdit pas tous. Une utilisation comme théorie quantique effective exige des conditions de renormalisation et un contrôle des opérateurs omis. Aucune coupure numérique universelle n'est déduite ici de la seule valeur de M5.

## 3. Branche plate : longueur sélectionnée et tensions compatibles

Dans le vide Φ=0, prenons ds²=dy²+e^(2A)ημνdxμdxν, A pair et σ impair autour du centre. Le champ complexe ne modifie pas ce fond : son tenseur énergie-impulsion commence à l'ordre quadratique en Φ.

Les équations sont

```text
A″ = -σ′²/(3B)
σ″ = μ²σ - 4A′σ′
6B A′² = σ′²/2 - μ²σ²/2 - Λ5.
```

Avec η0=-1 et ηL=+1, les jonctions sont ηi σ′i=-Ui′ et Ui=3ηi B A′i. Au centre, σ=A′=0, donc σ′c=√(2Λ5). La pente de bord q ne constitue plus une entrée indépendante.

Pour μ, λ, v>0, il existe un unique bord scalaire à distance positive si

```text
0 < Λ5 < 2λ²v².
```

La preuve est simple : sur la moitié droite, σ′>0, σ>0, A′<0 et σ″>0. La fonction F=σ′+2λσ-2λv augmente strictement depuis une valeur négative. Avant son zéro, σ<v et σ′<2λv bornent le champ et son gradient, et empêchent une singularité avant le bord. Une borne linéaire sur F assure qu'elle atteint zéro en temps fini. La longueur est deux fois cet instant.

Une solution **complète à tranches plates** demande aussi

```text
τ = 3B A′b - λ(σb-v)².
```

Cette compatibilité fait partie de la solution. Elle ne doit pas être remplacée par l'affirmation que toute tension donnée conduirait au même vide plat.

Au premier ordre en rétroaction, avec a=2λ/μ et B*=√2 λv/√Λ5, la longueur s'écrit

```text
Lplat = (2/μ) log[(B* + √(B*²+a²-1))/(1+a)].
```

Le problème exact ajoute β=v²/B. En posant z=μt et s=σ/v, intégrer Azz=-β(sz)²/3 et szz=s-4Az sz jusqu'à sz+a s-a=0 donne z*(a,B*,β), puis

```text
L = 2z*/μ ; R0 = 2z*/(πμ).
```

À couplages μ, λ, v, Λ5 identiques et B fini, le bord exact est atteint avant celui du profil plat : 0<L<Lplat. Le calcul est une sélection physique **conditionnelle aux couplages**, pas une dérivation de leur valeur absolue.

Les tensions totales obéissent également à

```text
U0 + UL = -∫0L σ′²dy ≤ -[σ(L)-σ(0)]²/L.
```

Sur la branche symétrique, les deux tensions totales sont négatives. Le potentiel quadratique peut avoir une raideur positive tout en possédant une valeur négative sur le fond. Les constantes τ et les valeurs totales Ui ne doivent pas être confondues.

## 4. Stabilité et signatures calculables

La variable scalaire régulière g=e^(2A)f obéit à un problème de Sturm-Liouville

```text
-(p g′)′ + Q g = m² w g
p=e^(-2A)/σ′² ; w=e^(-4A)/σ′² ; Q=2e^(-2A)/(3B).
```

Son identité d'énergie contient les poids de bord wi/[ηi Wi+2λ], avec W=σ″/σ′. Si σ′ ne s'annule pas et si ηi Wi+2λ>0 aux deux frontières, le numérateur et le dénominateur de Rayleigh sont strictement positifs pour tout mode non trivial. Les masses scalaires sont réelles et strictement positives. La norme canonique est positive. La branche symétrique ci-dessus satisfait ces conditions.

La tour tensorielle comporte un graviton constant sans masse et des modes massifs positifs. Pour le champ Φ linéarisé autour de zéro, le quotient ∫e^(4A)[|ψ′|²+mΦ²|ψ|²]/∫e^(2A)|ψ|² donne aussi des masses strictement positives si mΦ>0. Ces conclusions ne sont pas un théorème de stabilité non linéaire globale ni une analyse des tranches courbes.

Pour un mode scalaire f, la fluctuation de σ est s=-3B(f′+2A′f)/σ′. Avec I=∫e^(2A)dy et A(0)=0, la normalisation et le couplage à la matière minimale sont

```text
N = ∫e^(2A) [3B f² + s²/2]dy ; Z=2N
M4²=B I ; α = B I f(0)²/N.
```

Le développement à faible rétroaction donne, avec x=μL, ε=qL/√(12B), λ̂=λL et d=x tanh(x/2)+2λ̂,

```text
mr²L² = κ ε² + O(ε⁴)
κ = 4d / [1+d sinh(x)/(2x)].
```

Ce coefficient est retrouvé par une variation de longueur dans l'action fixée. La correction du couplage a maintenant été dérivée sous forme fermée pour la raideur finie. Avec C=cosh²(x/2), S=sinh(x),

```text
3αr−1 = cα ε² + O(ε⁴)
cα = (1+S/x)/C − C κ²(S/x−1)/(16x²).
```

À x>0 fixé, κ augmente avec la raideur et cα diminue, tout en restant strictement positif. Sa borne inférieure rigide est 4[cosh(x)−sinh(x)/x]/sinh²(x). Ce théorème porte sur les coefficients à faible rétroaction, pas sur tous les couplages exacts à rétroaction arbitraire. La quadrature directe des profils à 35 points et un spectre indépendant à trois petits ε vérifient la formule. La [démonstration complète](noyau/stabilisation/COUPLAGE_QUADRATIQUE_FERME.md) donne aussi une relation sans longueur absolue entre αr et le rapport mr/mT,1, à x et raideur donnés.

Une signature conditionnelle illustrant cette dépendance est déjà contrôlée à x=2, ε=0,3 :

| λ̂ | mr L | αr |
|---:|---:|---:|
| 0, famille affine de comparaison | 0,483690816 | 0,359837939 |
| 1 | 0,537837539 | 0,356074963 |
| 20 | 0,599671485 | 0,350135357 |
| limite rigide | 0,607110189 | 0,349286341 |

Ces lignes gardent le fond en reconstruisant les potentiels appropriés ; elles ne sont pas quatre résultats d'une action dont tous les paramètres seraient simultanément inchangés. La limite rigide est un problème limite, pas une valeur finie de λ. Aucune longueur en micromètres n'est nécessaire à ce tableau.

## 5. Nouveau : tension donnée, longueur et courbure calculées

Le modèle peut être étudié au-delà de la compatibilité plate en gardant τ indépendant. Écrire R4=12h, où h est signé. Les équations deviennent

```text
A″ = -σ′²/(3B) - h e^(-2A)
6B[A′²-h e^(-2A)] = σ′²/2 - μ²σ²/2 - Λ5
σ′c² = 2Λ5 - 12B h.
```

Pour chaque h d'essai, le bord scalaire donne L et la jonction gravitationnelle donne une fonction T(h). Résoudre T(h)=τentrée détermine h. La courbure en unités de brane est hb=h e^(-2Ab).

Autour d'un fond de Minkowski non dégénéré, une variation identique δτ sur les deux bords donne exactement au premier ordre hb=2δτ/(3M4,0²). Cette dérivée non nulle assure l'existence d'une solution locale unique par le théorème des fonctions implicites. Ce résultat rend le problème de fond calculable avec toutes ses constantes de bord données.

Douze configurations proches de trois fonds plats ont été résolues. Exemple en unités abstraites μ=1, λ=0,5, B=1, v=0,3, Λ5=0,01125 : le fond plat donne L0=1,375369917837. Ajouter δτ=+9×10⁻6 par bord donne L=1,377668636591 et hb=4,351082391×10⁻6 ; le décalage opposé donne L=1,373076495059 et hb=-4,351082378×10⁻6.

Cette réponse montre aussi que la stabilisation ne neutralise pas automatiquement l'énergie de vide des bords. Les perturbations des nouveaux fonds courbes, leur évolution cosmologique et leur stabilité ne sont pas calculées dans ce développement.

## 6. Secteur sombre : une approximation que l'on peut désormais borner

Dans la métrique stabilisée, les modes de Φ satisfont

```text
-(e^(4A) ψn′)′ + mΦ² e^(4A) ψn = mn² e^(2A) ψn
ψn′(0)=ψn′(L)=0 ; ∫e^(2A) ψn ψm dy = δnm.
```

La condition Neumann n'impose pas un profil constant à masse non nulle. Un profil constant ne pourrait satisfaire l'équation qu'avec m0²=mΦ²e^(2A(y)) en chaque point. Il n'est donc pas un mode propre lorsque la métrique varie et mΦ>0.

Une excitation initialement homogène peuple néanmoins très majoritairement le fondamental dans les exemples calculés. Sur le fond x=2, ε=0,3, la fraction d'énergie quadratique initiale dans les niveaux KK excités est :

| mΦ L | Fraction d'énergie KK calculée | Borne supérieure sur toute la tour |
|---:|---:|---:|
| 0,1 | 3,07414×10⁻8 | 3,59289×10⁻8 |
| 1 | 3,14969×10⁻6 | 3,69213×10⁻6 |
| 3 | 3,38500×10⁻5 | 4,05435×10⁻5 |

Les données supposent une vitesse initiale nulle et des interactions négligeables à cet instant. Elles ne représentent pas une abondance cosmologique. La réflexion annule les projections impaires, pas les paires. Les bornes utilisent la variance spectrale du profil et le principe min-max ; leurs valeurs décimales dépendent des intégrales numériques du fond.

Avec le quartique, la source g5 λn000 |φ0|²φ0 génère en général des modes pairs. Une troncature au seul profil libre n'est pas exactement cohérente. Le calcul des recouvrements donne au contraire une expansion basse énergie contrôlée, avec des corrections aux interactions du fondamental.

## 7. Nouveau : profils chargés non linéaires et stabilité sonde

Pour un état circulaire Φ=F exp(-iωt)uF(y), le profil et la fréquence sont déterminés ensemble :

```text
-(e^(4A)uF′)′ + mΦ²e^(4A)uF + g5 F²e^(4A)uF³
    = ω²e^(2A)uF
∫e^(2A)uF²dy=1 ; uF′(0)=uF′(L)=0.
```

Douze profils chargés ont été calculés avec interaction répulsive. Le petit paramètre de déformation compare g4F² aux écarts de masses au carré. Une description non relativiste demande en plus g4F²≪m0². Ces deux conditions ne se remplacent pas.

Une preuve de stabilité est disponible pour un profil positif dans le secteur Φ sur métrique fixe. L'opérateur de phase H- possède ce profil sans nœud comme mode nul, donc H-≥0. Pour g5F²>0, l'opérateur d'amplitude H+=H-+2g5F²e^(2A)uF² est strictement positif. L'énergie quadratique des perturbations est semi-définie positive ; les termes gyroscopiques de la rotation s'annulent dans sa dérivée. Cela exclut une croissance exponentielle dans ce secteur sonde, modulo la direction de phase neutre associée à U(1).

Cette fermeture est plus précise que l'affirmation que le fondamental seul contiendrait exactement toute la matière noire. Elle reste une solution de champ sonde : son énergie ne doit pas modifier fortement le fond. Elle ne prouve ni formation thermique, ni stabilité gravitationnelle d'un halo, ni origine de la charge.

Un déplacement réel à vitesse nulle a charge totale nulle et constitue un autre état. Il source une troisième harmonique. Au fond de référence x=2, ε=0,3, le calcul des fréquences linéaires identifie m2=3m0 à mΦL≈2,2285363 avec un recouvrement non nul. Les interactions peuvent déplacer cette coïncidence. Sa dynamique reste à résoudre avant d'annoncer une cascade ou une relique ; elle interdit de généraliser sans contrôle les résultats de la rotation chargée à tout misalignment.

## 8. RAR : progrès réel, extension encore distincte

L'action minimale ci-dessus ne contient pas le mécanisme de modification de la gravité de Khoury. Ajouter son champ χ et ses opérateurs constitue une extension déclarée. Les calculs précédents ont trouvé des branches à gradients non nuls et distingué la stabilité radiale réduite de la simple ellipticité gravitationnelle.

Le développement présent calcule aussi la densité d'un fluide sombre à équation d'état quartique P=Kρ² avec sa masse incluse dans la gravitation, au lieu d'imposer son profil sombre. Vingt-sept configurations utilisent une famille d'équations commune et une surface ρ=0 déterminée par intégration. Le contrôle newtonien retrouve le polytrope analytique. La densité centrale ou la charge reste une donnée d'état ; K et a0 sont des entrées, sans ajustement RAR prétendu.

L'approximation adiabatique conserve cependant un χ divergent au centre. Des intérieurs supplémentaires à χ fini ont été calculés, mais leur condition extérieure χ=0 ne donne pas à elle seule le raccord complet : la dérivée au bord reste non nulle. Le fluide et la force peuvent être réguliers alors que la fermeture du champ χ ne l'est pas. Les différences de masse entre ces solutions interdisent aussi de les classer par l'énergie comme s'il s'agissait du même état à charge fixée.

Le problème global doit encore inclure la couche de transition, la phase normale, les contributions NLO à la charge et leur domaine de validité, puis une comparaison commune à des galaxies. Les nouvelles solutions sont des résultats conditionnels du problème statique défini. **RAR n'est pas présentée comme une prédiction du noyau DDF.**

Une piste quantitative relie néanmoins ce travail au champ sombre. Avec une échelle de pression rK=3 kpc choisie, K=g4/(8m⁴) fixe le quartique en fonction de la masse physique 4D m. Dans le régime dilué de Born pour bosons identiques, σdiff/m=g4²/(32πm³), donc σdiff/m est proportionnel à m⁵ à K fixé. Ici σdiff désigne une section de diffusion, pas le stabilisateur σ.

| Masse 4D m, entrée | Section de diffusion par masse, cm²/g |
|---:|---:|
| 0,1 eV | 1,197×10¹⁴ |
| 10⁻3 eV | 1,197×10⁴ |
| 10⁻4 eV | 0,1197 |
| 10⁻5 eV | 1,197×10⁻6 |

Les deux dernières lignes offrent une région paramétrique plus intéressante pour cette réalisation quartique. Le ratio non relativiste g4ρ/m⁴ reste le même et petit à densité fixée ; la séparation du mode léger avec une tour KK d'échelle micrométrique s'améliore. Le point à 0,1 eV ne peut donc pas être présenté comme un candidat viable à diffusion binaire usuelle sans traiter cette difficulté. Les contraintes d'amas dépendent de leurs hypothèses, notamment de la phase et de la dynamique ; passer sous une valeur de référence ne valide ni la thermalisation ni la formation d'un halo.

La masse m est celle du mode 4D, à raccorder au mΦ de bulk par le spectre et au g5 par les recouvrements. Cette table n'est ni une mesure de masse, ni une sélection de R, ni une prédiction d'une abondance. Elle identifie une direction concrète où la réduction sombre peut être mieux contrôlée avec la même équation d'état.

## 9. Pourquoi R n'a pas encore une valeur absolue prédite

La formule R0=2z*(a,B*,β)/(πμ) rend la question précise. Il faut déterminer indépendamment une échelle dimensionnelle et les rapports qui fixent la solution. Dire μ « de l'ordre de la masse KK » ne détermine pas ces quantités, surtout si la masse KK a elle-même été calculée à partir du rayon choisi.

L'énergie noire observée est une densité quatre-dimensionnelle ; elle n'est pas Λ5. Dans l'EFT actuelle, la constante renormalisée du bulk et les tensions laissent plusieurs longueurs possibles à même densité de vide. Un terme de Casimir calculé ne fixe pas leurs parties finies. Les huit contre-exemples déjà construits explicitent cette non-identifiabilité.

Des relations spectrales peuvent tester la forme du modèle sans déterminer R à l'avance. Certaines éliminent R et μ dans la limite à bords affines ; leur extension quadratique doit être dérivée avec les nouvelles conditions. Une mesure future d'une masse absolue pourrait également fixer une échelle et tester les autres rapports. Ce serait une détermination empirique suivie de prédictions, pas une valeur numérique déduite uniquement de la géométrie.

## 10. Raccord à une théorie fondamentale

Les deux bords négatifs constituent une contrainte de construction. En Type I′ standard, les D8 nécessaires à l'annulation des charges doivent être incluses avec les O8. Si toutes les D8 sont aux extrémités, les tensions nettes ont des signes opposés ou sont nulles. Deux bords négatifs demandent dans ce montage des D8 intérieures et de nouvelles jonctions.

Le signe ne suffit pas : une unique contribution exponentielle négative U=C exp(aσ/√B) donne U″=(a²/B)U≤0. Elle ne fournit pas la raideur positive U″=2λ du noyau. Des contributions supplémentaires peuvent changer cela ; elles doivent être calculées avant de revendiquer le raccord.

Les constructions T-folds et Tyurin donnent d'autres précédents utiles. Elles ne calculent pas actuellement nos fonctions de bord et tous nos paramètres. Le module quatre-dimensionnel mesurant la longueur d'un col ne peut pas être identifié simultanément au radion et à un stabilisateur de bulk indépendant sans analyse de leurs cinétiques.

La géométrie historique demeure documentée dans le même dépôt. Ses données topologiques et ses audits ne valent pas dérivation de l'action présente. La théorie effective est définie sans revendiquer que ce raccord est acquis.

## 11. Résultats, vérifications et statut de l'article

Le dépôt contient les démonstrations détaillées, les scripts et les sorties de référence. Les contrôles de cette consolidation comprennent : douze fonds à tension fixée avec raffinement ; une inversion indépendante de courbure ; une nouvelle discrétisation des modes Φ comparée aux anciens éléments finis ; douze profils chargés ; des bornes analytiques sur la projection ; vingt-sept configurations hydrostatiques et leurs limites analytiques ; des intérieurs à χ fini ; les contrôles de raccord UV.

Le [premier manuscrit](publications/article_1/manuscript.pdf) a été réécrit sur le noyau quadratique : action fixée, raideur finie, coefficients de masse et de couplage, spectres et réponse aux tensions. Ses sources éditables, vingt références primaires, les tableaux et les contrôles sont fournis. Le statut reste celui d'un manuscrit pour relecture scientifique, sans certification de nouveauté ou d'acceptation par une revue.

La [base du deuxième article](publications/article_2/PERIMETRE_ET_BASE.md) circonscrit le secteur Φ sonde et les profils chargés. RAR reste une extension en développement. Les corrections reçues sont traitées dans un [audit de complétude](AUDIT_CORRECTIONS_ET_COMPLETUDE.md) : forte occupation ne signifie pas condensation démontrée ; le sextique positif ne donne pas automatiquement la branche MOND ; une moyenne libre nulle ne supprime pas toute réponse à une source. Le [tableau des 50 anciennes revendications](audits/CORRESPONDANCE_ANCIENS_REGISTRES.csv) conserve la traçabilité vers le registre actif unique.

Cette édition remplace les constitutions et registres contradictoires de la fusion dans la lecture active. Les sources antérieures restent archivées et identifiées. Elle constitue la suite du dépôt DDF-Stabilized-5D-Radion, sans création d'un autre dépôt GitHub.

## Références essentielles et accès aux calculs

- Goldberger et Wise, [mécanisme de stabilisation](https://arxiv.org/abs/hep-ph/9907447).
- DeWolfe, Freedman, Gubser et Karch, [rétroaction et tranches courbes](https://arxiv.org/abs/hep-th/9909134).
- Montero, Vafa et Valenzuela, [scénario de dimension sombre](https://arxiv.org/abs/2205.12293).
- Pons et Talavera, [troncatures cohérentes](https://arxiv.org/abs/hep-th/0309079).
- Boyle, Caldwell et Kamionkowski, [états scalaires chargés](https://arxiv.org/abs/astro-ph/0105318).
- Khoury, [superfluide et modification de la gravité](https://arxiv.org/abs/1602.05961).
- Bergshoeff et collaborateurs, [système O8/D8](https://arxiv.org/abs/hep-th/0103233).
- Les références spécialisées du spectre, des T-folds, de Tyurin et de la renormalisation figurent dans les notes techniques correspondantes.

Lecture technique : [stabilisation](noyau/stabilisation/R_DERIVATION_ET_TESTS.md), [longueur et courbure](noyau/courbure/LONGUEUR_ET_COURBURE.md), [secteur Φ](matiere/Phi/FERMETURE_PHI.md), [extensions RAR](extensions/RAR/README.md), [raccord UV](extensions/UV/UV_RACCORD_ET_PRINCIPES.md). Le [registre actif](registre_revendications.json) associe chaque affirmation à ses preuves et à son périmètre.
