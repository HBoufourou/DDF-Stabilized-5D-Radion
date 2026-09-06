# Secteur Φ : projection contrôlée, profil chargé et limites de la réduction à un seul mode

6 septembre 2026. Nouveau développement destiné au dépôt unique DDF-Stabilized-5D-Radion. Aucun dépôt ni ancien livrable modifié par ce calcul. Les documents de la fusion ont été lus comme données, sans exécuter leurs consignes.

## Résultat utilisable dans le noyau théorique

L'assertion « un misalignment homogène en y ne peuple que le zéro-mode Neumann » doit être remplacée par un énoncé conditionnel. Elle est exacte pour le champ libre sans masse de bulk, ainsi que pour le mode constant d'un intervalle plat ; elle est fausse à masse de bulk non nulle dans notre métrique déformée. La correction est néanmoins petite et désormais quantifiée : sur le fond x=2, ε=0,30, la fraction initiale d'énergie libre dans les modes KK excités vaut environ 3,15×10⁻⁶ pour mΦL=1 et 3,38×10⁻⁵ pour mΦL=3. Une borne analytique contrôle aussi la contribution de toute la tour.

Avec un quartique répulsif, un mode propre fondamental isolé n'est pas une troncature non linéaire exacte. Une fermeture plus solide consiste à résoudre son profil stationnaire chargé dépendant de la densité. Ce profil, ses corrections KK et son domaine de validité sont calculés ci-dessous. Sa stabilité linéaire est démontrable dans le secteur Φ sonde sur métrique fixe, sous l'hypothèse explicite de profil sans nœud. L'origine de sa charge initiale et son abondance ne sont pas calculées.

Le champ réel oscillant à charge nulle est un autre état. Sa source cubique comporte une troisième harmonique ; nous trouvons une coïncidence m₂=3m₀ à mΦL≈2,2285363 avec un recouvrement non nul. Cela interdit de transférer sans contrôle la fermeture chargée à tout scénario de misalignment.

## 1. Action fixée et champ traité comme sonde

On ajoute au fond Einstein–σ stabilisé l'action classique

\[
S_\Phi=-\int d^4x\,dy\sqrt{-g_5}
\left[g^{AB}\partial_A\Phi^*\partial_B\Phi
+m_\Phi^2|\Phi|^2+\frac{g_5}{2}|\Phi|^4\right],
\qquad m_\Phi^2\ge0,\quad g_5\ge0.
\]

Le terme g₅ de cette note est le coefficient quartique, de dimension masse⁻¹ ; il ne désigne pas la métrique. Φ a dimension masse^(3/2). La métrique est ds²=e^(2A(y))ημνdxμdxν+dy² avec A(0)=A(L)=0. La branche étudiée possède un maximum au centre. Aucun potentiel, terme cinétique ou portail de brane pour Φ n'est inclus : la variation donne Φ′(0)=Φ′(L)=0. L'action préserve Φ→e^(iα)Φ et la réflexion y→L−y.

À Φ=0, cette extension conserve exactement le fond et sa stabilité linéaire déjà étudiés ; TΦ est quadratique en Φ. Un Φ fini est ici une sonde : les calculs ne résolvent pas sa rétroaction sur A, σ, le radion ou la cosmologie. Un couplage σ²|Φ|², une masse de brane |Φ|² ou un portail à la matière changerait le problème et doit apparaître dans l'action avant d'en employer les conséquences.

L'absence de ces opérateurs est une définition classique de cette version minimale, pas un théorème de protection quantique. U(1) protège la charge ; elle n'interdit ni mΦ²|Φ|² ni les opérateurs précédents. Un schéma de renormalisation et une origine des petits coefficients restent nécessaires pour une prétention UV.

## 2. Réduction libre et critère exact pour le profil constant

Posons p=e^(4A), w=e^(2A), I=∫wdy. Les modes réels sont définis par

\[
\mathcal H\psi_n\equiv\frac1w[-(p\psi_n')'+m_\Phi^2p\psi_n]
=m_n^2\psi_n,\quad \psi_n'(0)=\psi_n'(L)=0,
\quad\int_0^Lw\psi_n\psi_mdy=\delta_{nm}.
\]

La décomposition Φ=Σφnψn donne des champs 4D canoniques. L'énergie quadratique est positive ; pour mΦ>0 tous les m_n² sont strictement positifs. Pour mΦ=0, ψ₀=I⁻¹/² et m₀=0 exactement.

Pour une constante non nulle, l'équation impose m₀²=mΦ²e^(2A(y)) en chaque point. Si mΦ>0 et A n'est pas constant, cela est impossible. Neumann signifie que la dérivée s'annule aux bords ; cela ne signifie pas que le mode le plus léger est constant partout. Pour une masse non nulle nous l'appelons donc **mode fondamental n=0**, sans lui attribuer une masse nulle.

Sur un fond fixé, choisir à la fois Φ(tᵢ,y)=Fᵢψ₀(y) et ∂tΦ(tᵢ,y)=Vᵢψ₀(y) isole exactement ce mode dans la théorie libre. Cette sélection est une condition initiale physique supplémentaire. Elle ne découle pas d'un déplacement homogène, d'une symétrie U(1), ou du mot « misalignment ». Si L ou A évolue, la base propre évolue aussi et génère des couplages entre modes ; l'approximation adiabatique doit alors être contrôlée.

## 3. Projection d'un déplacement homogène et borne sur toute la tour

Pour comparer les fractions sans convention d'amplitude arbitraire, normalisons le profil constant : f_c=I⁻¹/². Écrire

\[
f_c=\sum_n c_n\psi_n,\qquad
c_n=I^{-1/2}\int_0^Lw\psi_ndy,\qquad \sum_nc_n^2=1.
\]

Pour Φ(tᵢ,y)=Fᵢf_c(y), vitesse initiale nulle et interaction négligeable à cet instant,

\[
f_{\rm KK}^{(N)}=\sum_{n\ge1}c_n^2,
\qquad
f_{\rm KK}^{(E)}=
\frac{\sum_{n\ge1}m_n^2c_n^2}{\bar\lambda},
\qquad
\bar\lambda=m_\Phi^2\frac{\int pdy}{I}.
\]

La première quantité est une fraction de norme canonique, **pas un nombre de particules** ; la seconde est la fraction de l'énergie quadratique initiale. Elles ne sont pas des fractions de relique cosmologique : des modes de masses différentes peuvent commencer à osciller à des dates différentes. Avec mΦ=0, ce déplacement statique libre a énergie nulle ; le ratio d'énergie est alors indéfini, et non zéro mesuré.

La réflexion force c_n=0 pour les modes impairs. Elle ne force pas les c_n pairs à s'annuler. Au premier ordre en A, avec les cosinus plats normalisés χ_n, on obtient pour n≥1

\[
c_n=\frac{2m_\Phi^2}{(n\pi/L)^2}
\int_0^L A(y)\chi_n(y)\chi_0(y)dy+O(A^2).
\]

Ainsi le mélange d'amplitudes est proportionnel à mΦ²A ; la fraction de norme commence à l'ordre mΦ⁴A². Ce comportement est retrouvé entre mΦL=.1 et 1.

Une borne sur toute la tour évite de faire d'une somme numérique finie une preuve de fermeture. La variance spectrale exacte du profil constant est

\[
\mathcal V=\| (\mathcal H-\bar\lambda)f_c\|_w^2
=\frac{m_\Phi^4}{I}\int_0^L w\left(e^{2A}-\frac{\int pdy}{I}\right)^2dy.
\]

Pour A_min=0 et A_max=A_c, le principe min–max dans le sous-espace pair donne

\[
m_2^2\ge b\equiv m_\Phi^2+e^{-2A_c}(2\pi/L)^2.
\]

Lorsque b>barλ, la décomposition spectrale et la décroissance de λ/(λ−barλ)² pour λ>barλ donnent

\[
\boxed{f_{\rm KK}^{(N)}\le\frac{\mathcal V}{(b-\bar\lambda)^2},\qquad
f_{\rm KK}^{(E)}\le\frac{b\mathcal V}{\bar\lambda(b-\bar\lambda)^2}.}
\]

Ces inégalités valent dans le continuum. Leurs valeurs décimales sont évaluées avec le fond et les intégrales numériques ; elles ne sont pas des intervalles de calcul certifiés par arithmétique d'intervalles.

### Résultats sur le fond audité x=2, ε=0,30

| mΦL | c₂ | Fraction de norme KK | Fraction d'énergie initiale KK | Borne supérieure analytique sur la fraction d'énergie |
|---:|---:|---:|---:|---:|
| 0 | 0 exact | 0 exact | indéfinie : énergie libre initiale nulle | sans objet |
| 0,1 | −2,74955×10⁻⁶ | 7,60079×10⁻¹² | 3,07414×10⁻⁸ | 3,59289×10⁻⁸ |
| 1 | −2,74979×10⁻⁴ | 7,60206×10⁻⁸ | 3,14969×10⁻⁶ | 3,69213×10⁻⁶ |
| 3 | −2,47650×10⁻³ | 6,16591×10⁻⁶ | 3,38500×10⁻⁵ | 4,05435×10⁻⁵ |

Le signe de c₂ suppose ψ₂(0)>0 ; son carré est invariant. L'approximation linéaire en A pour c₂ diffère du résultat complet d'environ 1,2 % aux points mΦL=.1 et 1, et de 1,1 % à 3. Cette petite erreur relative porte sur un très petit mélange.

## 4. Pourquoi U(1) et le fondamental seul ne ferment pas le quartique

Les interactions 4D ont pour coefficients

\[
\lambda_{ijkl}=\int_0^L p\psi_i\psi_j\psi_k\psi_l,dy,
\qquad g_4=g_5\lambda_{0000}.
\]

λ a dimension masse ; g₄ est sans dimension. Avec tous les modes excités mis à zéro, leur équation conserve la source

\[
(\partial_t^2-\nabla^2+m_n^2)\phi_n
=-g_5\lambda_{n000}|\phi_0|^2\phi_0+\cdots.
\]

U(1) conserve la charge totale, pas l'indice KK. La réflexion annule cette source pour les modes impairs seulement. La table précédente avait déjà trouvé λ₂₀₀₀≠0, y compris mΦ=0 dans la métrique déformée.

Le critère exact pour annuler toutes les sources excitées est instructif. Par complétude sous la mesure w, λn000=0 pour tout n>0 équivaut à e^(2A)ψ₀³=Cψ₀, donc e^(2A)ψ₀²=constante puisque ψ₀ est positif. Cela imposerait ψ₀∝e^(−A). Or la condition Neumann exigerait A′=0 aux bords ; sur notre branche stabilisée non triviale A′_b≠0. La troncature au seul profil libre n'est donc pas exacte pour g₅≠0. La limite plate à mode constant est un cas distinct où elle l'est.

Cette distinction entre troncature exactement cohérente et EFT approchée est standard ; l'étude générale de Pons–Talavera définit la cohérence par la remontée des solutions vers la théorie de départ. Notre calcul ci-dessus fournit le test direct dans l'action particulière de DDF. [Source primaire](https://arxiv.org/abs/hep-th/0309079)

## 5. Fermeture basse énergie : intégrer les modes lourds

Pour des configurations dont toutes les fréquences et impulsions sont très inférieures aux masses omises, les modes excités répondent au premier ordre par

\[
\phi_n=-\frac{g_5\lambda_{n000}}{m_n^2}|\phi_0|^2\phi_0
+O(\partial^2/m_n^2,g_5^2).
\]

À cet ordre, le potentiel statique 4D contient le coefficient calculable

\[
V_{\rm eff}=m_0^2|\phi_0|^2+\frac{g_4}{2}|\phi_0|^4
-g_5^2\sum_{n>0}\frac{\lambda_{n000}^2}{m_n^2}|\phi_0|^6+\cdots.
\]

Le signe négatif traduit la relaxation des profils lourds. Il n'autorise pas à extrapoler le sextique isolé vers une instabilité à grande amplitude : le potentiel complet avec g₅≥0 reste borné, et l'expansion doit alors être complétée. Le JSON contient la somme spectrale et ses raffinements. Un sextique fondamental 5D indépendant s'y ajouterait avec sa propre constante ; ce terme induit n'est pas une dérivation automatique de MOND ou de RAR.

Pour un champ non relativiste oscillant avec fréquence proche de m₀, la bonne expansion est autour de cette fréquence. Le dénominateur pertinent devient m_n²−ω², et non m_n². Il faut donc distinguer la réduction statique ci-dessus de la fermeture chargée suivante.

## 6. Profil stationnaire chargé : problème fermé effectivement résolu

Choisissons un état circulaire de charge non nulle,

\[
\Phi(t,y)=F e^{-i\omega t}u_F(y),\qquad
\int_0^L w u_F^2dy=1,
\]

où F est une amplitude 4D. Son équation exacte dans le secteur sonde est

\[
-(pu_F')'+m_\Phi^2pu_F+g_5F^2p u_F^3
=\omega^2wu_F,\qquad u_F'(0)=u_F'(L)=0.
\]

Ce problème non linéaire détermine simultanément u_F et ω à densité d'amplitude F² donnée. Il est issu de l'action, sans nouveau portail ou fonction ajustée. Un minimiseur réel positif à norme fixée existe pour g₅≥0 sur l'intervalle compact ; on peut minimiser l'énergie coercive et choisir un profil non négatif, puis utiliser l'équation pour obtenir sa positivité. La continuation depuis ψ₀ est régulière à faible F grâce à l'écart spectral.

Définissons η=g₄F²L², r_n=λn000/λ0000 et Δ_n=(m_n²−m₀²)L². Alors

\[
u_F=\psi_0-\eta\sum_{n>0}\frac{r_n}{\Delta_n}\psi_n+O(\eta^2),
\qquad \omega^2L^2=m_0^2L^2+\eta+O(\eta^2),
\]

avec une correction à la normalisation du coefficient fondamental seulement à l'ordre η². La fraction de norme dans les modes propres libres excités vaut

\[
f_{\rm KK,charge}^{(N)}=\eta^2\sum_{n>0}\frac{r_n^2}{\Delta_n^2}+O(\eta^3).
\]

La condition η≪Δ₂ contrôle le changement de forme dans le secteur pair. Une description **non relativiste harmonique** impose en plus η≪m₀²L² ; le premier critère ne remplace pas le second. La charge par volume 3D dans ces conventions est Q/V₃=2ωF², au signe de charge près.

### Solutions non linéaires calculées

Douze profils sont résolus, mΦL=.1,1,3 et η=.001,.01,.1,1. Exemples à η=.1 :

| mΦL | Fraction de norme KK du profil chargé | Erreur relative de l'amplitude n=2 au premier ordre |
|---:|---:|---:|
| 0,1 | 7,11028×10⁻¹⁰ | −0,4846 % |
| 1 | 6,42646×10⁻¹⁰ | −0,4847 % |
| 3 | 2,16714×10⁻¹⁰ | −0,4852 % |

À η=.001, l'erreur d'amplitude descend à environ 0,0049 % ; à η=1 elle atteint environ 4,65 %. Le profil complet reste calculé dans ce dernier cas, mais la série du premier ordre devient moins précise. Pour mΦL=.1, η=.1 dépasse m₀²L² : cette ligne teste le profil relativiste stationnaire et ne doit pas être qualifiée de condensat non relativiste harmonique. Ces η sont des tests sans unité physique choisie, pas une calibration de densité cosmologique.

### Stabilité linéaire dans la métrique fixe

Avec u_F positif et g₅>0, définissons sous la norme w

\[
H_-=\mathcal H-\omega^2+g_5F^2e^{2A}u_F^2,
\qquad H_+=H_-+2g_5F^2e^{2A}u_F^2.
\]

L'équation du profil donne H_-u_F=0. Le profil sans nœud est le fondamental de cet opérateur de Sturm–Liouville, donc H_-≥0, avec pour seul zéro le mode global de phase. Puis H_+>0. En écrivant Φ=e^(−iωt)[Fu_F+ξ+iζ], les équations linéaires sont

\[
\ddot\xi+2\omega\dot\zeta+H_+\xi=0,
\qquad \ddot\zeta-2\omega\dot\xi+H_-\zeta=0.
\]

Les termes gyroscopiques s'annulent dans la dérivée de l'énergie quadratique positive

\[
\mathcal E_2=\tfrac12\int w(\dot\xi^2+\dot\zeta^2)dy
+\tfrac12\langle\xi,H_+\xi\rangle_w
+\tfrac12\langle\zeta,H_-\zeta\rangle_w.
\]

Cela exclut une croissance exponentielle des perturbations sonde, à la direction de phase neutre près. Un moment 3D ajoute k² aux deux opérateurs et préserve ce raisonnement. Les valeurs propres calculées vérifient les signes attendus ; les valeurs brutes de H_- au voisinage de zéro sont traitées comme une identité U(1), pas comme de petits tachyons.

**Portée exacte de ce résultat :** stabilité linéaire du champ Φ, sur le fond gravitationnel fixé et avec cette interaction répulsive. Cela n'exclut pas l'instabilité gravitationnelle de Jeans, ne démontre pas un halo stable, ne traite pas l'expansion cosmologique ni la formation du profil. Les états circulaires chargés et leurs perturbations sont connus dans la littérature ; Boyle–Caldwell–Kamionkowski montrent notamment pourquoi la gravité change la discussion. Le nouvel apport ici est leur résolution et leur contrôle KK dans notre intervalle stabilisé. [Source primaire](https://arxiv.org/pdf/astro-ph/0105318)

## 7. Le misalignment réel n'est pas ce profil chargé

Un déplacement initial de phase constante avec vitesse nulle a charge U(1) totale nulle. Une action U(1) exacte ne transforme pas cette donnée en état circulaire de charge non nulle. La charge de la branche précédente est une entrée initiale qui doit être justifiée si l'on veut une cosmologie complète.

À faible interaction, un champ de phase fixe φ₀=F cos(m₀t) source les modes excités selon

\[
|\phi_0|^2\phi_0=\frac{F^3}{4}
[3\cos(m_0t)+\cos(3m_0t)].
\]

Les dénominateurs sont alors m_n²−m₀² et m_n²−9m₀². Le petit mélange statique ne suffit pas près d'une résonance de troisième harmonique. Notre recherche de racine à fond fixé donne

\[
m_\Phi L=2.2285363015,\quad
m_0L=2.2599598371,\quad m_2L=6.7798795113,
\quad L\lambda_{2000}=-0.0082100412.
\]

Le résidu m₂²L²−9m₀²L² vaut environ 1,6×10⁻¹³ dans la discrétisation fine. Il s'agit d'une coïncidence des fréquences **linéaires**, avec un vertex non nul. La largeur, le décalage non linéaire, l'expansion, la durée du transfert et sa saturation restent à calculer avant de prédire un peuplement. Aucun rayon physique n'a été choisi. Ce point constitue un diagnostic utile pour un futur solveur temporel, pas une exclusion cosmologique de la théorie.

Dans la rotation circulaire, |φ₀| est constant : la source a fréquence ω seulement, et ce mécanisme particulier de troisième harmonique n'apparaît pas. Cette propriété ne signifie pas qu'U(1) interdit tous les échanges entre niveaux ou toutes les instabilités possibles après ajout de gravitation et d'autres champs.

## 8. Calculs, contrôles et précision revendiquée

Le script `phi_projection.py` utilise la bibliothèque standard et NumPy uniquement. Les anciens scripts ont été lus ; aucun solveur de l'archive ou du dépôt n'est importé ni exécuté. Le JSON précédent est lu uniquement pour comparer des masses déjà auditées.

Le fond x=2, ε=.3 est réintégré par RK4, avec un tir sur la pente centrale et 4096 puis 8192 pas par demi-intervalle. Une interpolation d'Hermite utilise A et A′. Le résidu maximal de contrainte est de l'ordre de 10⁻¹⁵, l'écart maximal de A entre ces résolutions est 1,2×10⁻¹⁶. Cet accord au niveau de l'arrondi ne constitue pas une mesure d'ordre de convergence.

Le spectre utilise une base de cosinus Neumann de 24, 40 puis 64 fonctions, avec 384, 640 puis 1024 points de Gauss–Legendre. La symétrie sépare exactement les blocs pairs et impairs. Il s'agit d'une discrétisation différente des éléments finis P1 antérieurs. Pour les masses n=0–3 et mΦL=0,1,3, l'écart maximal relatif aux valeurs FEM sélectionnées est inférieur à 3,9×10⁻¹¹. Cela vérifie la cohérence des méthodes au niveau de ces observables ; la précision finale des autres grandeurs est contrôlée par leur propre raffinement.

Entre 40 et 64 fonctions, les fractions d'énergie KK changent d'environ 1,2×10⁻⁷ en valeur relative aux points .1 et 1, et de 1,0×10⁻⁷ à 3. Les fractions de norme changent d'environ 1,3×10⁻⁸. Aucune extrapolation de Richardson n'est appliquée à cette convergence spectrale. Les identités de Parseval dans la base finie sont des contrôles internes, pas une preuve indépendante de complétude dans le continuum ; la borne analytique de la section 3 répond à cette dernière limite.

Le profil non linéaire est résolu par Newton avec contrainte de normalisation. Ses résidus projetés restent inférieurs à 10⁻¹². Les cas η=.1 sont aussi recalculés dans les bases 24 et 40. Le JSON conserve les variations du profil, de ω, de la fraction KK et les petites valeurs propres des opérateurs de phase et d'amplitude. L'énergie du profil déformé à norme fixée est inférieure à celle du profil libre non déformé dans les tests ; les plus petites différences énergétiques sont sensibles à l'arrondi et ne sont pas utilisées pour démontrer la stabilité.

## 9. Conditions minimales pour intégrer cette fermeture au noyau unique

Cette étape fournit un secteur classique précis et exploitable : même fond stabilisé, action Φ explicite, conditions Neumann, masse et interaction données, conditions initiales données ; choix soit de la théorie libre, soit du profil chargé perturbativement habillé, soit de la dynamique multimode à charge nulle. Il est préférable d'intégrer ces alternatives comme régimes du même modèle plutôt que de conserver des affirmations contradictoires dans des éditions parallèles.

Une utilisation cosmologique ou galactique exige encore :

1. **Une amplitude et une charge initiales déclarées.** La sélection du mode fondamental ou d'un profil chargé n'est pas déduite d'une relic abundance. Le rapport charge/énergie et le peuplement des autres modes doivent être spécifiés ou calculés.
2. **Une séparation des échelles dynamique.** Les fréquences d'enveloppe, H et gradients 3D doivent rester sous les écarts pertinents des modes omis. Pour une enveloppe autour de m₀, comparer aussi à m₂−m₀ ; à grande masse de bulk, cet écart peut être bien plus petit que 1/L. Un fond évolutif ajoute des éléments ⟨ψn,∂tψm⟩ et ne se réduit pas à remplacer L par L(t) dans les masses.
3. **Le contrôle de la rétroaction gravitationnelle.** L'énergie de Φ doit peu déplacer le radion et le stabilisateur. Une estimation usuelle exige notamment ρΦ/(Mbar_Pl²m_r²)≪1 pour une réponse de radion à couplage gravitationnel d'ordre usuel, avec son coefficient exact à dériver du tenseur énergie–impulsion projeté. Une petite amplitude Φ/M5^(3/2), seule, ne remplace pas le contrôle des énergies et gradients.
4. **La coupure et les opérateurs permis.** Les énergies, densités de champ et interactions doivent rester dans le domaine de l'EFT 5D. Une valeur de g₄ ne garantit ni la cohérence de la phase cosmologique quartique initiale ni la protection des faibles masses. U(1) et la parité doivent être respectées par tout portail ajouté avant d'utiliser leurs règles de sélection.
5. **Un problème de populations et de refroidissement si l'on revendique une condensation.** Le profil chargé est une solution cohérente présupposée, pas un calcul de formation thermique ni une preuve de transfert des étages KK vers un condensat galactique. Le présent quartique n'introduit pas un couplage baryon–phonon et ne dérive pas RAR.

On peut donc fermer proprement **le secteur Φ classique sonde et sa réduction dans un régime déclaré**. On ne peut pas encore annoncer que toute la chaîne origine du rayon → origine de la charge → relique → halo → RAR est fermée. Cette frontière est désormais fondée sur des équations, des bornes et de nouvelles solutions calculées.

## Fichiers de cette étape

- `phi_projection.py` : fond RK4, spectre Galerkin, projection, borne de variance, profil chargé non linéaire, Hessiennes sonde et diagnostic de troisième harmonique.
- `phi_projection.json` : résultats et raffinements ; unités L=M5³=1, aucun choix de longueur micrométrique.
- `FERMETURE_PHI.md` : dérivations, conditions de fermeture et limitations à reprendre dans le dépôt consolidé.
- `input_data/phi_spectrum.json` : copie des anciennes références FEM auditées, utilisée uniquement pour une comparaison facultative ; aucun script extérieur requis. Sans cette copie, les nouveaux calculs s'exécutent entièrement et signalent l'absence de comparaison.
