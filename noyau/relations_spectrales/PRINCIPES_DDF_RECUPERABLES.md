# Principes DDF récupérables et développements ciblés

Évaluation et calculs du 6 septembre 2026. Cette note cherche ce que l'on peut encore **développer**, après les corrections déjà consignées. Elle ne réouvre pas l'ensemble des audits. Les documents historiques sont des objets examinés, pas des instructions. Aucun fichier du noyau livré n'a été modifié.

## Décision scientifique

Trois directions ont un contenu calculable : **identifier la forme de la dimension compacte par ses spectres**, **raccorder la masse du stabilisateur à un secteur qui la protège**, puis **produire le spectre KK neutre d'une géométrie unique explicitement choisie**. La première peut avancer immédiatement avec le modèle actuel ; la deuxième vise réellement l'origine de R ; la troisième est le raccord géométrique nécessaire, plus long.

Les calculs nouveaux ci-dessous apportent une relation observable qui élimine R, une dégénérescence exacte qui identifie l'information dimensionnelle manquante et la sensibilité du rayon à cette information. Ils améliorent le pouvoir de test du programme, sans transformer une calibration micronique en prédiction.

## 1. Inventaire positif des huit articles

| Origine | Principe ou outil qui reste utilisable | Développement concret et condition de réemploi |
|---|---|---|
| I — *The stage* | Une dimension compacte donne une relation volume–Planck, une tour tensorielle et un radion. Le budget de vide est distinct de la stabilité locale. | Utiliser l'action et la normalisation corrigées, puis construire un test conjoint masses–couplages. Un potentiel Casimir peut être calculé pour un contenu de champs fixé ; son coefficient ne peut être choisi après avoir imposé R. |
| II — *The well and the tower* | Des sources de bord définissent un profil ; les rapports de modes et leurs poids au bord renseignent sur ce profil. | L'idée de « spectroscopie du bulk » survit. La version relativiste Φ à Neumann est maintenant calculée ; la nouvelle relation ci-dessous porte sur le secteur **stabilisateur–radion**, distinct de Φ. Les anciennes valeurs Airy ne sont pas réintroduites. |
| III — *The medium* | Une même espèce peut avoir des excitations particulaires et des modes collectifs d'un état occupé. Une masse microscopique non nulle n'interdit pas un phonon sans gap. | Définir d'abord l'état, sa charge, son action à basse énergie et la source baryonique. Un spectre de particules ne fournit ni l'état collectif ni la RAR. Le développement actif de l'action gravitationnelle doit demeurer une branche explicitement ajoutée. |
| IV — *One scale and its shadow* | Une transmission gravitationnelle de brisure supersymétrique peut donner une masse de module proportionnelle à F/MPlanck. | Définir le secteur de brisure et le coefficient de transmission ; le remplacer par un simple nombre « d'ordre un » ne fixe pas R. La masse des superpartenaires mesurée au collisionneur n'est pas automatiquement √F. |
| V — *Type I prime strings* | Une réduction explicite peut calculer des vecteurs de couplages et des identités de projection. | Sauver l'algèbre canonique et les invariants sous mélange, puis refaire leur raccord dans une seule compactification. Les coefficients physiques de l'ancien montage Type I′/IIB ne passent pas automatiquement dans la géométrie corrigée. |
| VI — *What the candidate geometry implies* | Les identités de norme sous rotation et l'étude de familles géométriques sont des outils solides. | Les transformer en bornes sur des forces à plusieurs portées, ou en classification de familles avec opérateur spectral. Un extremum du potentiel complet est nécessaire pour sélectionner un vide et une longueur. |
| VII — *Seven charge classes* | PG(2,2), les sept vecteurs non nuls de F₂³ et GL(3,2) d'ordre 168 constituent une combinatoire exacte. | Réemploi possible comme classement ou comme candidat à tester contre un groupe d'automorphismes et son action sur les champs. Aucun lien dérivé à μ, R ou a₀ ; cette direction ne mérite pas la priorité pour le premier article physique. |
| VIII — *Vacuum winding and baryogenesis* | Des secteurs de phase, un courant et une évolution hors équilibre peuvent définir un problème distinct de baryogenèse. | Spécifier variété, identifications de bord, action temporelle et violation baryonique. L'enroulement spatial ne fixe ni un potentiel chimique temporel ni le rayon ; c'est un chantier ultérieur. |

Les références originales aux neutrinos rencontrées dans ce corpus concernent notamment les classes de charges de VII. Elles ne constituent pas une action de masse des neutrinos. Introduire fermions de bulk, projections chirales et Yukawas de brane serait une **extension nouvelle**, avec de nouveaux paramètres, et non la récupération d'une prédiction déjà contenue dans les huit articles.

## 2. Développement A — Identifier la forme avant de fixer l'échelle

### 2.1 Relation nouvelle entre observables sans R

Portée : action sur l'intervalle physique, potentiel de bulk Λ₅+μ²σ²/2, potentiels de brane **affines**, branche symétrique, matière minimale sur un bord, faible rétroaction à x=μL>0 fixé. Les masses m_s1 et m_s2 désignent les deux excitations du secteur stabilisateur au-dessus du radion ; ce ne sont pas les modes du champ complexe Φ.

À ε→0, le radion tend vers le mode gravitationnel sans masse. Les fluctuations canoniques du stabilisateur obéissent séparément à

\[
 -s''+\mu^2s=m^2s,\qquad s'(0)=s'(L)=0.
\]

Il en résulte

\[
 m_{s1}L=x+O(\epsilon^2),\quad
 m_{s2}L=\sqrt{x^2+\pi^2}+O(\epsilon^2),\quad
 m_{T1}L=\pi+O(\epsilon^2).
\]

Le premier de ces modes est le mode constant de σ à rétroaction nulle. La variable métrique f utilisée à ε≠0 a la parité opposée à la fluctuation scalaire correspondante via la contrainte ; elle est singulière si l'on impose σ′=0 avant de prendre la limite. La dérivation utilise donc les fluctuations canoniques à ε=0, pas une substitution interdite dans l'équation divisée par σ′.

Le noyau a déjà établi

\[
3\alpha_r-1=D(x)(m_rL)^2+O(\epsilon^4),\quad
D(x)=\frac{1+T^2+2T/x}{4xT},\quad T=\tanh(x/2).
\]

Définissons ζ=m_s1/m_T1 et η=m_r/m_T1. Alors x=πζ+O(ε²). Comme η²=O(ε²), remplacer x par πζ ne modifie le résultat qu'à l'ordre ε⁴. On obtient la fermeture observable

\[
\boxed{3\alpha_r-1=\pi^2D(\pi\zeta)\eta^2+O(\epsilon^4).}
\]

Elle ne contient ni longueur L ni masse μ en entrée. Une seconde fermeture, moins précise à l'ordre considéré, est

\[
\frac{m_{s2}^2-m_{s1}^2}{m_{T1}^2}=1+O(\epsilon^2).
\]

Ces relations permettent d'estimer x avec un rapport de masses et de **tester** la branche par un couplage supplémentaire. Elles ne sont pas une identification unique parmi toutes les théories 5D. Une source supplémentaire, un terme cinétique de brane ou une courbure U″ non nulle change le problème et peut introduire de nouveaux paramètres de forme. En particulier, le développement récent à branes quadratiques ne peut pas être inséré dans cette formule sans nouvelle dérivation.

### 2.2 Vérification numérique bornée

`principles_calculs.py` utilise uniquement la bibliothèque standard, lit les résultats affines certifiés du noyau et conserve leurs empreintes SHA-256. Il n'ajuste aucun paramètre. Les nombres ne sont pas de nouvelles mesures ni un nouveau calcul indépendant des valeurs propres.

On note E la différence entre les deux côtés de la relation encadrée et δ=3αr−1.

| x | ε | x estimé par πm_s1/m_T1 | E/ε⁴ | \|E/δ\| |
|---:|---:|---:|---:|---:|
| 1 | 0,05 | 1,016949 | 2,40651 | 0,3595 % |
| 2 | 0,05 | 2,006006 | 0,705669 | 0,1800 % |
| 2 | 0,143 | 2,047732 | 0,662484 | 1,4139 % |
| 3 | 0,05 | 3,002748 | 0,130355 | 0,0746 % |
| 2 | 0,4 | 2,310678 | 0,438768 | 8,5438 % |
| 2 | 0,53 | 2,482457 | 0,330774 | 12,6208 % |

À x=2, les deux petits ε sont compatibles avec le reste O(ε⁴) dérivé analytiquement ; ils ne suffisent pas à donner une borne uniforme sur ce reste. Les lignes ε=0,4 et 0,53 montrent pourquoi il faut employer le spectre exact hors du régime perturbatif. La fermeture des masses a des résidus 5,38×10⁻⁴ et 4,23×10⁻³ pour x=2, ε=0,05 et 0,143.

Le prochain calcul utile serait la même élimination pour la famille quadratique, en conservant explicitement b=LU″ comme paramètre supplémentaire et en réservant un mode additionnel pour le déterminer. Il faut tester le rang du jacobien des observables, pas supposer que trois nombres identifient toujours trois paramètres.

### 2.3 Ce qui survit de la règle de somme de V–VI

Soit un vecteur g de couplages à la matière dans une base de scalaires **canoniques**, et β_i=2(g·e_i)² les amplitudes Yukawa positives dans la base de masse orthonormée. Alors

\[
\sum_i\beta_i=2|g|^2.
\]

Cette identité est indépendante de la rotation. La force mesurée à distance r dépend toutefois du noyau

\[
Y(r)=\sum_i\beta_i e^{-m_i r},\qquad
e^{-m_{\max}r}\sum_i\beta_i\leq Y(r)\leq
e^{-m_{\min}r}\sum_i\beta_i.
\]

Pour la **correction au potentiel** normalisée ici, la somme seule suffit si les masses sont égales, ou approximativement si rΔm≪1. Une somme constante ne garantit pas une même forme du potentiel quand les portées diffèrent. De plus,

\[
\frac{d^2}{dr^2}\ln Y(r)=\mathrm{Var}_{r}(m_i)\geq0.
\]

C'est une borne et un test de forme récupérables sans reprendre la valeur historique 2,2414. La variance utilise les poids β_i exp(−m_i r)/Y. Ces formules supposent un ensemble de modes de norme positive, une source sur le même bord et des échanges linéaires ; elles ne s'appliquent pas directement à un régime collectif non linéaire. Le véritable facteur de correction à la **force** contient en plus (1+m_i r).

## 3. Développement B — Une origine de μ qui puisse réellement fixer R

### 3.1 La liberté d'échelle restante est exacte dans le modèle tronqué

Écrivons B=M₅³. À partir d'une solution, définissons pour s>0

\[
\begin{aligned}
&L_s=sL,\quad B_s=B/s,\quad \mu_s=\mu/s,\quad
q_s=q/s^{3/2},\\
&\Lambda_{5,s}=\Lambda_5/s^3,\quad
T_{i,s}=T_i/s^2,\quad J_{i,s}=J_i/s^{3/2},\\
&A_s(y_s)=A(y_s/s),\quad
\sigma_s(y_s)=\sigma(y_s/s)/\sqrt{s}.
\end{aligned}
\]

La substitution dans les équations de fond et conditions de bord les conserve. Pour les branes quadratiques, il suffit d'ajouter U″_s=U″/s et de redimensionner de la même manière les valeurs centrales de σ. Les paramètres x, ε et b restent fixes.

La masse de Planck mesurée reste **identique** :

\[
\bar M_{\rm Pl,s}^2=B_s\int_0^{L_s}e^{2A_s}dy_s
=B\int_0^Le^{2A}dy.
\]

Les masses spectrales se multiplient par 1/s ; les rapports de masses et les amplitudes Yukawa restent identiques. Pour le scalaire, le profil canonique de fluctuation se transforme comme σ/√s, et les deux termes de N=∫e²ᴬ[3Bf²+s_fluct²/2]dy restent invariants. Il s'agit d'une famille **d'actions différentes**, pas d'une symétrie qui ferait varier le rayon dans une action fixée.

Cela prouve précisément que ni la gravitation 4D normalisée ni les rapports spectraux ne peuvent sélectionner la longueur absolue quand les paramètres d'action ne sont pas fixés ailleurs. Le script vérifie les invariants algébriques sur trois facteurs d'échelle ; son exemple numérique n'est pas présenté comme un fond résolu. Les conditions de validité de l'EFT et les opérateurs omis doivent être recontrôlés si s varie fortement.

Une masse KK absolue détectée fournirait une **mesure conditionnelle** de L après identification de la forme du modèle. Une prédiction indépendante exige qu'au moins une combinaison dimensionnelle de l'action soit fixée par une autre construction ou observation. Ajouter a₀ comme coefficient libre de l'action galactique ne lève pas cette liberté : aucune équation active ne relie a₀ à ces paramètres 5D.

### 3.2 La stabilisation ne supprime pas la sensibilité paramétrique

Au premier ordre en rétroaction, la relation déjà dérivée dans le noyau est

\[
L=\frac2\mu\operatorname{arcosh}z,\qquad
z=\frac{q}{\sqrt{2\Lambda_5}}>1.
\]

La dérivée nouvelle explicite son pouvoir prédictif :

\[
\boxed{d\ln L=-d\ln\mu+
\frac{2\coth(x/2)}x\,d\ln z.}
\]

| x | z | ∂lnL/∂lnz |
|---:|---:|---:|
| 0,1 | 1,001250 | 400,333 |
| 0,5 | 1,031413 | 16,332 |
| 1 | 1,127626 | 4,328 |
| 2 | 1,543081 | 1,313 |
| 3 | 2,352410 | 0,737 |

La stabilité locale du radion peut donc coexister avec une grande sensibilité près de z=1. Ces dérivées sont locales et ne permettent pas d'extrapoler une variation qui traverserait z=1. Pour R=L/π, la même formule logarithmique vaut. Une valeur précise de μ ne suffit toujours pas : le rapport z et l'ajustement de l'énergie de vide doivent aussi être déterminés.

### 3.3 Protection : séparer trois objets

**μ**, masse du stabilisateur réel σ ; **mΦ**, masse du champ complexe ; et **l'énergie d'un phonon** dans un état occupé sont trois objets différents. Sous Φ→exp(iθ)Φ, l'opérateur |Φ|² reste invariant. L'U(1) conserve une charge et peut garantir un mode de phase sans gap lorsqu'il est spontanément brisé dans un état approprié ; il ne protège pas à lui seul la petite valeur de mΦ, et encore moins μ. Une interaction g₅|Φ|⁴ autorise, par comptage de puissance en cinq dimensions, une correction de masse d'ordre g₅Λ_UV³, avec facteur de boucle dépendant des conventions et de la définition du seuil. Ce n'est pas une valeur calculée de la correction dans une complétion UV donnée.

Pour σ, une translation constante pourrait servir de symétrie protectrice, mais il faut examiner l'action entière. Le terme μ²σ² la brise ; les tadpoles de bord ont une variation pondérée par les deux volumes induits. J₀+J_L=0 sur un fond de volumes égaux ne constitue pas, à lui seul, une invariance de l'action avec métriques et matière fluctuantes. Les portails éventuels doivent participer à la même analyse de symétrie.

La route supersymétrique de IV est plus concrète si elle est écrite avec un secteur X dont la composante auxiliaire vaut F et un multiplet contenant le stabilisateur. Un opérateur de transmission de type X†X S†S/M_*² donne schématiquement m_S²=c|F|²/M_*². Il reste à calculer c, à préciser M_*, le signe physique, les termes de bord et le raccord de ce champ 4D à σ en 5D. Ce schéma est un **candidat ajouté**, pas une complétion déjà construite.

Si ce raccord donnait effectivement μ=c_μF/MPlanck, le rayon serait, au même ordre perturbatif,

\[
R=\frac{2\bar M_{\rm Pl}}{\pi c_\mu F}\operatorname{arcosh}z.
\]

Cette équation expose les trois données qu'il faut fixer indépendamment : F, c_μ et z. Qualifier c_μ et z de nombres « d'ordre un » fournit une plage d'échelles, pas une valeur exacte de R.

Dimopoulos et Giudice exposent bien m_module∼F/MPlanck avec coefficient dépendant des couplages. Leur équation (3) distingue en outre la masse du secteur visible de F et de la masse des messagers : on ne doit donc pas appeler une particule à 7,6 TeV une mesure directe de √F. [Source primaire, §1–2 et équation (3)](https://arxiv.org/pdf/hep-ph/9602350).

**Livrable décisif suivant :** une action de transmission et son registre d'opérateurs permis/interdits, avec un calcul de seuil de δμ² et δJ_i. Ce travail pourrait préserver une échelle meV. Il ne faut pas lui demander simultanément de démontrer la RAR et de fixer la cosmologie.

## 4. Développement C — Faire de la géométrie une origine du spectre neutre

Les résultats torique, quasi-Fano et de structure de Hodge de la géométrie corrigée restent des données mathématiques utiles sous leurs hypothèses explicites. Le diagnostic défavorable sur certains tubes **actifs de C₄** n'est pas une exclusion de la tour gravitationnelle neutre. Cette distinction ouvre un vrai calcul qui ne réutilise pas une filiation invalidée.

Le chemin concret est : choisir une seule famille et son involution ; construire une approximation métrique compatible ; fixer l'opérateur spin 2 avec la mesure correcte ; établir une séparation entre modes longitudinaux et transverses ; calculer rapports et recouvrements. Une métrique jouet permet une validation de méthode, pas une identification avec la métrique Ricci-plate de cette famille.

Le dossier R65 propose déjà deux plateformes : la géométrie résolue R63/POLY944, ou la plateforme POLY925 de la littérature. Il faut garder une même plateforme pour le lissage, les périodes, les flux et les tadpoles. La route DDF la plus continue est POLY944 ; emprunter les paramètres stabilisateurs de POLY925 produirait une dépendance circulaire masquée par un changement de variété.

Une étape bornée utile serait de calculer, sur la même approximation métrique, des bornes variationnelles et un rapport de gaps longitudinal/transverse, puis leurs variations avec le paramètre de dégénérescence. L'objectif est de tester l'existence d'un régime **effectivement 5D**. Aucun invariant purement topologique ne fixe la longueur absolue : sous g→a²g, les longueurs sont multipliées par a et les valeurs propres du Laplacien par a⁻², sans changer la topologie. Le potentiel des modules doit ensuite fixer a.

Il existe désormais un travail antérieur explicite associant dégénérescence de Tyurin, compactification IIB anisotrope et stabilisation de modules pour ADD/DD. Il faut comparer le mécanisme et les données de variété ; la seule association « Tyurin + dimension sombre » ne peut être revendiquée comme nouvelle. [Braun, Cicoli, Milioli et Valandro, prépublication du 17 juin 2026](https://arxiv.org/abs/2606.19440).

## 5. Dépendances à conserver visibles

| Question | Entrées dont elle dépend aujourd'hui | Ce qui constituerait un test supplémentaire |
|---|---|---|
| Rapports et couplages radion/KK | Action, x, ε, conditions de bord et source de matière | Un mode ou couplage réservé après détermination des paramètres de forme |
| Valeur absolue de R | Paramètres dimensionnels ou masse absolue mesurée | Un mécanisme extérieur fixant μ et z, puis comparaison avec une portée |
| Protection de μ et mΦ | Symétrie de l'action entière, seuils et portails | Calcul de corrections après introduction des interactions nécessaires |
| État collectif galactique | Charge/occupation initiales, interactions, évolution | Existence et stabilité de la solution de halo, puis réponse à la source baryonique |
| RAR et a₀ | Nouvelle action galactique et ses coefficients | Déduction de ses opérateurs/coefficient depuis le secteur 5D ; prédictions de lentillage et dépendance à l'environnement |
| Vide géométrique | Famille, flux, branes et potentiel de modules | Minimum complet et raccord numérique vers les paramètres 5D |

Ne pas compter comme confirmations indépendantes μ=1/R, √(μMPlanck) et un rayon déduit à nouveau de ce même μ. Ne pas déterminer un coefficient sur la RAR puis citer la RAR comme validation de ce coefficient. Ne pas inférer qu'une phase sans gap existe parce que la masse de Φ est petite. Ne pas emprunter une action ou un flux d'une autre variété sans raccord démontré.

**Ordre conseillé :** ajouter les relations de spectroscopie au programme existant ; choisir ensuite un seul mécanisme protecteur et ses opérateurs ; maintenir la construction métrique comme raccord géométrique parallèle. Le premier de ces développements est déjà une amélioration analytique concrète. Le second peut, s'il aboutit, commencer à transformer le rayon en prédiction. La RAR demeure une branche supplémentaire dont le raccord doit être calculé.

## Sources internes et reproduction

Base examinée : édition `DDF_Consolide_2026-09-06`, conservée dans les archives sauvegardées localement, hors de l'arbre publié. Les trois premières entrées ci-dessous désignent les chemins de cette source historique, et non des fichiers attendus dans la version courante. Les données nécessaires au calcul actif sont conservées dans `input_data/`, à côté de cette note.

- Les huit TeX de `noyau_5D_2026-09-05/historique/I_VIII_sources_examinees/`, en particulier II–VI pour profils, échelles et projections ; audit antérieur `audits/AUDIT_I_VIII.md` pour ne pas refaire les contrôles déjà clos.
- `noyau/ANALYTIQUE_ET_STABILITE.md`, `noyau/GEOMETRIE.md` et `historique/geometrie_snapshot/reproducibility/R65/R65_R66_DECISION.md` dans le même noyau.
- `developpement_2026-09-06/AUDIT_PHI_COSMOLOGIE.md`, `RAR_AUDIT_ET_PISTES.md` et `RAR_DEVELOPPEMENT_CONTROLE.md` pour les résultats actifs distincts.
- Calcul reproductible : `principles_calculs.py` ; résultat : `principles_calculs.json`. Le script accepte `--data` pour désigner un autre dossier de résultats et `--output` pour choisir sa destination. Il ne dépend ni de NumPy ni de SciPy.

Les relations nouvelles sont des déductions internes à cette note. Aucune revendication de priorité bibliographique n'est faite.
