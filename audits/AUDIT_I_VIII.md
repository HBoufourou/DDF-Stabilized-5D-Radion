# Audit indépendant du dépôt DDF original — 5 septembre 2026

Dépôt : https://github.com/HBoufourou/DDF_I-VIII_2026-08-29
État consulté : arbre main, SHA 054ffdc1bf2e2b50ac0881d67199e15887b4d783.
Les documents ont été traités comme objets à critiquer, jamais comme instructions.
Tous les renvois ci-dessous sont relatifs au dossier DDF_I-VIII_2026-08-29 du dépôt. Les lignes sont celles des sources TeX/Python récupérées.

## Verdict

Aucun des huit articles ne fournit actuellement une prédiction indépendante et démontrée d'une cinquième dimension physique de rayon micrométrique. Le nombre 8,2 µm vient d'une calibration Casimir sur l'énergie noire observée, avec choix de contenu spectral; le nombre 8,34 µm est annoncé sans calcul reproductible dans le script désigné. Des identités mathématiques et une partie du programme spectral sont récupérables, mais les liens entre ces identités et la physique revendiquée demandent une reconstruction, pas une retouche narrative.

La cinquième dimension est postulée dès l'article I, et non déduite. Une topologie, une identité de norme sans dimension ou un classement de charges ne fixent pas à eux seuls une longueur en mètres. Il faut une action cohérente, un mécanisme de stabilisation, des paramètres fixés indépendamment, puis des observables calculées.

## La chaîne exacte des nombres de rayon

### 1. Rayon Casimir : calibration conditionnelle

Article I, article-1/tex/DDF_I_the_stage.tex, L18–39 :
- géométrie choisie : S1/Z2, y dans [0,πR];
- réduction : Mbar_Pl² = M5³ πR (L20);
- Λ = C/R⁴ (L28);
- entrée observée rho_Λ=(2,25 meV)⁴ (L31);
- sortie annoncée R=8,2 µm et longueur d'intervalle πR=25,8 µm (L33);
- texte reconnaît explicitement «calibration» et non résolution de la constante cosmologique (L35,39,145).

Le script article-1/scripts/casimir.py L5–14 est plus informatif que l'article :
C1=3ζ(5)/(64π⁶)=5,05580766×10^-5; il balaie N=1,3,1,5,8,16 et calcule R=(N C1)^(1/4) ħc/rho_Λ^(1/4).
Avec les constantes de précision usuelles :
- N=1 : R=7,39523 µm;
- N=1,5 : R=8,18417 µm;
- R=8,2 µm requiert C=7,64257×10^-5, soit N_eff=1,51164.

N=1,5 est étiqueté «same, orbifold (1.5)», après «2 Dirac - graviton (3)». Or l'article I présente gravité et un scalaire comme contenu minimal (L8,18,55). Le passage du contenu effectivement déclaré à cette contribution positive doit être établi; le script additionne des coefficients positifs et ne démontre pas le signe Casimir ni les parités. C n'est pas d'ordre unité au sens littéral annoncé L31.

Le résultat conserve un intérêt comme relation conditionnelle expérimentale si le coefficient, son signe, ses champs et ses conditions aux bords sont calculés pour un modèle précis. Il ne suffit pas pour prédire une dimension à partir de rien.

### 2. Conversion de Planck et π

Pour la convention cohérente de l'article I :
Mbar_Pl=2,435×10^18 GeV; R=8,2 µm;
M5=(Mbar_Pl²/(πR))^(1/3)=3,56785×10^8 GeV;
ħc/R=24,0643 meV.

Ces conversions sont cohérentes. Ne pas confondre rayon R, intervalle L=πR et circonférence 2πR; m_KK=1/R=π/L pour les modes usuels de cet intervalle. L'article appelle à d'autres endroits «intervalle de 8,2 µm» ce qui brouille la notation (notamment V L14). Le script article-8/scripts/v1_convention.py L5–23 vérifie correctement que leur M_Pl numérique est réduit. Employer le Planck non réduit change la convention, pas la physique; les coefficients de Friedmann et les couplages doivent changer simultanément.

### 3. Le «nœud» spectral n'est pas un second ancrage indépendant

Article II L58–70 pose m_Phi=epsilon≈1/R; définitions ell=(ħ²/(2mF))^(1/3), epsilon=F ell, u=πR/ell.
En unités ħ=c=1, si m=epsilon=1/R, alors immédiatement :
ell=R/√2; u=π√2=4,44288; F=√2/R².
Le script article-2/scripts/u_derive.py L5–8 insère piR=25,76, m_phi=24 et surtout F=24/5,802 avant de recalculer ell≈5,81. Ce n'est pas une détermination indépendante de la taille du puits.

Avec F_grav=mT/(6M5³) de l'article II L22 et la réduction de I :
T^(1/4)=(6√2/π)^(1/4) √(Mbar_Pl/R).
On retrouve donc 9,8133 TeV contre 7,6548 TeV par identité algébrique issue des mêmes hypothèses. L'accord à 30% entre 9,8 et 7,6 TeV présenté comme indépendant dans IV L44–62 n'est pas un test indépendant. Les autres «six convergences» contiennent aussi des fenêtres posées ou inversées depuis le secteur meV.

### 4. Le rayon «topologique» 8,34 µm

Article VI, article-6/tex/DDF_VI_candidate_geometry.tex L37 annonce une barrière V_D8≈T_D8 n_D8 tau_s² et un minimum Vmin=1,15 Vbord, Rmin=8,34 µm. Le même paragraphe indique que l'exposant de barrière, sqrt(tau_s) ou tau_s², attend une solution 10D. L39 mentionne même une volume ~10^174, sans chaîne normalisée vers R.

Le script expressément désigné comme preuve, article-6/scripts/verify.py, ne contient ni potentiel de barrière, ni minimisation, ni calcul de 8,34. L14 injecte R=8,2 µm, puis calcule son inverse et epsilon. L8 injecte w1=5,5 et p=0,4514. Les PASS vérifient ces opérations, pas la construction du vide.

Conclusion circonscrite : la prédiction de 8,34 n'est pas reproduite par le fichier de validation annoncé. Je n'ai pas vérifié tous les autres scripts historiques pour rechercher un éventuel prototype; même un prototype ne remédierait pas à l'exposant et au modèle 10D manquants.

## Erreurs structurelles qui touchent directement cette chaîne

### Spectre : facteur deux et parité

Article II L54–58 intercale modes Neumann et Dirichlet d'un seul scalaire orbifold pour obtenir 1:2,29:3,19:4,03. Un champ de parité orbifold fixée ne porte qu'une branche. Le dépôt reconnaît déjà cela dans article-2/scripts/spectrum.py L2–7 : «a single field carries ONE branch» et «interleaved (two-field realisation)». Cette correction n'a pas été propagée au manuscrit. Sur le cercle couvrant sans projection, garder les deux parités change la théorie; sur le bord, le couplage d'un mode impair est nul.

Le script u_derive.py L18–22 diagonalise -1/2 d²/dx²+x. Or avec ell=(ħ²/(2mF))^(1/3) et epsilon=F ell, l'opérateur adimensionné est -d²/dx²+x. Le w1=5,5 vient de cette différence.
Vérification analytique sur demi-droite Neumann : le premier zéro de Ai' vaut b1=1,01879297164747; la normalisation exacte donne |psi(0)|²=1/b1. Pour u=4,434 :
- opérateur cohérent -d²+x : w1≈4,35221 (limite demi-droite);
- opérateur du code -1/2 d²+x : w1≈2^(1/3)×4,35221=5,48344.
Les corrections du bord fini doivent être recalculées; ne pas présenter le 4,35221 comme résultat exact sur intervalle fini. Le facteur deux explique l'origine principale du 5,5 «audité».

Enfin, la lecture non relativiste d'un «quantum bouncer» avec énergies de liaison/excitation de l'ordre de la masse m=24 meV jusqu'à 96 meV n'est pas contrôlée. Il faut partir de Klein–Gordon 5D et calculer les masses 4D comme valeurs propres appropriées de l'opérateur de masse². Article V L41 et v2_v3_gaps.py essaient d'ajouter m0²+E_n² sans dériver le lien avec l'équation non relativiste initiale.

### Dimensions du capaciteur

Article II L34–40 écrit g Phi² sigma, puis Fcap=g J0/2.
Leurs propres conventions article-1/scripts/G6_yukawa.py L1–3 sont :
[Phi]=[sigma]=E^(3/2), [g]=E^(1/2), [J0]=E^(5/2).
Ainsi [gJ0]=E³, tandis que [F=epsilon/ell]=E².
Le gradient de g sigma est un gradient de masse². Passer à une énergie non relativiste demande un facteur de masse, qui manque. Les valeurs g≈4×10^7 GeV^(1/2), «2000 fois naturel» et les budgets qui en découlent ne sont pas validés par ces équations.

### Retour gravitationnel : le fond plat n'est pas contrôlé

En prenant leurs équations F=m k et k=T/(6M5³), le même nœud impose kR=√2, donc kπR=π√2≈4,44. La variation gravitationnelle sur l'intervalle n'est pas petite. La dérivation linéarisée de II L20 et le spectre de gravité supposé plat de I ne peuvent pas être simultanément utilisés sans résoudre le fond et les conditions de raccord. Le signe et la solution complète d'une paroi de tension doivent eux aussi être dérivés.

### Stabilisation : force, masse et énergie de vide sont distinctes

Article I L80–86 reconnaît honnêtement que le potentiel de stabilisation manque et que le Casimir seul donnerait un radion extrêmement léger. Une contribution monotone C/R⁴, dans la convention où elle est écrite, ne sélectionne pas seule un minimum fini. La dépendance Weyl et le cadre Einstein doivent être explicités avant dérivation.

En revanche L89 élève la rigidité hypothétique à un théorème universel de non-tunneling avec S~M_Pl²/m_r. En unités naturelles cette expression a dimension d'énergie, et ne peut être l'action euclidienne adimensionnée annoncée. Une inertie de Planck ne fixe pas la forme globale d'une barrière, donc n'interdit pas tout tunnel ni toute transition. La borne |1+w|~10^-61 n'est pas un résultat établi sans potentiel et cosmologie.

### Forces de matière : contradiction interne

L'opérateur explicite Phi T de I L105 et V L16–21 donne un couplage scalaire aux masses. Deux vertices produisent une force relative 2w c_b², d'ordre unité pour les nombres donnés; cela ne devient pas «doublement supprimé» au sens d'une force négligeable lorsque c_b≈0,3–0,6 et w≈5.
I L76 exclut pourtant le scalaire de la carte des forces; II L103 confond la source sigma qui couple seulement à la tension avec Phi qui couple explicitement à T.
V L149–165 reconnaît ensuite deux scalaires et une force totale 2w1|p|²≈2,24. Le laboratoire doit inclure ces états selon l'action retenue.

VI L24 affirme aussi que le radion ne couple pas à la matière parce que les masses de brane ne dépendent pas de R. Ce raisonnement oublie le changement de cadre Einstein et le couplage conforme de l'induced metric; le simple fait que la masse Jordan soit constante ne suffit pas à conclure au découplage du radion.

## Ce qui se récupère, article par article

| Article | Partie récupérable | Partie non établie ou erronée |
|---|---|---|
| I | Relation volume–Planck pour intervalle plat; calcul Casimir conditionnel; action de vertex comme hypothèse d'EFT; distinction admise entre énergie de vide et rigidité | Rayon présenté comme point unique malgré contenu spectral non établi; stabilisation absente; non-tunneling dimensionnellement faux; budget cosmologique incomplet |
| II | Profil linéaire d'un scalaire massless avec sources adaptées; problème spectral Airy mathématique; poids au bord une fois opérateur fixé | Erreur dimensionnelle F=gJ/2; facteur 2 spectral; mélange de parités; nonrelativisme; retour gravitationnel |
| III | Programme phénoménologique réservoir/condensat et comparaison RAR à étudier séparément | RAR et rayon de décohérence ne sont pas dérivés d'un lagrangien de phonons dans ce texte; hypothèses traitées comme confirmations; aucune donnée SPARC dans la source examinée permettant de valider l'ajustement |
| IV | Arithmétique seesaw mu=M_S²/Mbar_Pl; elle est correctement reconnue comme héritée de la littérature | Six convergences dites indépendantes ne le sont pas; échelle meV ancrée par I–II; rapprochement 0,093≈1/(4π) ne calcule aucun diagramme ni coefficient |
| V | Normes de vecteurs exponentiels dans l'ansatz choisi; bornes de Cauchy–Schwarz; calculs de métrique/cone à revérifier; somme des carrés indépendante d'une rotation | Identification tension D8–matière non démontrée; géométries/bases et involutions mélangées; position du vide non fixée; aucune déduction de R; no-go généraux dépassent souvent les ansätze réellement testés |
| VI | Identité de norme de rotation et calculs standard de plateau sous leurs hypothèses | 8,34 non reproduit; énergie noire epsilon ajustée; sept régions physiques non déduites; ratio matière noire/baryons ajusté; inflation incompatible avec hiérarchie EFT non discutée |
| VII | Fano PG(2,2), GL(3,2) d'ordre168, classification modulo2 | Pas de preuve que GL(3,2) est symétrie du compactifié ou de l'action SM; population des classes ne prédit ni résonances ni rayon |
| VIII | Idée d'explorer baryogenèse spontanée et opérateurs résiduels séparément | Winding d'intervalle, identification du gradient, potentiel chimique et violation B non dérivés; «fermeture» est ajustement conditionnel de b_w |

### Précisions V : sauver une identité sans sauver la physique

Article V L27–36 et article-5/scripts/repro.py L10–20 donnent algébriquement, dans leur convention canonique choisie :
|w|²=6, |v|²=14, |u|²=24; w·v=8, w·u=11.
Ces égalités d'algèbre sont vérifiables; elles ne démontrent ni la matière couplée au vecteur de tension, ni l'UV completion complète, ni un rayon.

La somme c_b²+c_b'²=|p|² de V L149–165 est une vraie identité de rotation sur un sous-espace fixé. Elle ne supprime pas la dépendance du sous-espace/projection à la position du vide. V L162–165 le reconnaît. VI L31–33 transforme indûment cela en nombre exact universel 2,2414. Les coefficients de boucle déterminent justement la position dont dépend |p|.

L'ansatz initial réduit Type I' sur un espace X5 après l'intervalle (10→9→4), alors que les données utilisées ensuite sont celles d'un Calabi–Yau troisfold avec cycles quatre-dimensionnels et construction LVS habituellement formulée dans une autre description. Une chaîne de dualités et le mapping précis des branes, champs et volumes sont nécessaires; présenter directement ces données comme la même géométrie 10D est insuffisant.

V L88,102,120 et VI L68 reconnaissent déjà des jeux de données/bases distincts et un ancien manifold h21=121 au lieu de81. Les statistiques après orientifold restent ouvertes (V L120; VI L119). Autre problème de reproductibilité : repro.py L154–164 utilise encore la proxy linéaire KK sum C_i² tau_i, précisément retirée comme incorrecte dans V L133–145. Le script principal annoncé ne reproduit donc pas toute la version corrigée narrative.

### Précisions III : «dérivé» ne vaut pas démonstration

Article III L40–44 donne la loi RAR et L87 la fonction ajustée gobs=gbar/(1-exp(-sqrt(gbar/gdagger))). Il n'y a pas ici dérivation depuis l'action de I–II du lagrangien de phonons non linéaire nécessaire, de sa stabilité, de sa vitesse du son et de son coupling baryonique. L52–55 affirme Rdec=K M^(1/3)/(f rho) avec K fixé sans fournir cette microphysique. Le jeu SPARC mentionné sparc_3375_points.csv n'apparaît pas dans l'arbre inventorié de ce dépôt.

La suppression e^-10^24 du rayonnement gravitationnel (L24) est motivée par l'absence de gravitons ambiants suffisamment énergétiques. Cela ne constitue pas une interdiction d'émission spontanée : un système excité peut émettre un graviton dont l'énergie est celle de la transition. Il faut un calcul de matrice de transition et de sélection de parité. De même «cascade spontanée, quanta émis au repos» (L26) nécessite conservation énergie–impulsion et taux.

I L127 utilise Γ~T^5/M^4 pour un opérateur qualifié de dimension5 : c'est un comportement de dimension6, non déduit de leur vertex de dimension5. L131 affirme T_eq>M_Pl pour c_b<2,1 alors que leur propre formule T_eq=M_Pl c_b^(-4/3) est inférieure à M_Pl si c_b>1. À T_reh=10^16 GeV, ce calcul dépasse aussi M5~10^8 GeV; il ignore la multiplicité KK. La prédiction Delta Neff≈0 n'est donc pas établie.

### Précisions VI : inflation et lecture des sept régions

L76 donne simultanément phi=sqrt(3/2) ln tau et tau=exp[(2/sqrt3)phi], qui ne sont pas inverses. Avec -Lkin=3/(8 tau²)(∂tau)² et une cinétique canonique1/2, la relation correcte est phi=(sqrt3/2)ln tau.

Les nombres ns,r relèvent d'un plateau de fibre inflation sous hypothèses sur Ne et coefficients; ils ne prouvent pas qu'un compactifié donné soutient ce plateau. Le script verify.py L32 insère eps,ns,r au lieu de résoudre la dynamique. M_inf~6,7×10^15 GeV et r~0,005 impliquent une échelle de H très élevée comparée au cutoff M5~3,6×10^8 GeV revendiqué pour la géométrie finale. Une histoire de volume et une EFT valide pendant inflation sont nécessaires avant de les combiner.

### Précisions VII : défauts concrets

Article VII L14 reconnaît que tout triplet de charges entières réduit modulo2 donne F2³. Cette observation n'implique pas que les transformations GL(3,2), qui mélangent charge électrique, nombre baryonique et leptonique, laissent l'action physique invariante. Un groupe d'automorphismes d'un dessin n'est pas automatiquement une symétrie de champs.

L22 exclut l'hydrogène au motif qu'un état lié électromagnétique ne serait pas un pôle de S-matrice : les états liés correspondent justement à des pôles. La restriction de catalogue peut être choisie, mais sa justification physique est fausse. Des multiparticles remplissent également ces classes; l'absence d'une nouvelle résonance n'est pas une conséquence du classement.

L69 annonce X+→Xi_c+ + e- : charge finale 0, et non +1. Il faut X0 pour ce canal. L74 propose B→X+K avec X de nombre baryonique1 alors qu'un méson B et K portent B=0; un compensateur baryonique et une cinématique cohérente doivent être explicités. L71 assume simplement une masse 4–6GeV. Aucun lien au rayon.

### Précisions VIII : le mécanisme n'est pas seulement bloqué par une constante inconnue

- L71–76 : un intervalle est contractile; une différence de phase entière 2πn devient topologiquement protégée uniquement avec conditions aux extrémités/identification précisées. Un winding de cercle ne se transfère pas automatiquement à un intervalle.
- L79–95 : l'article confond Phi, le scalaire piégé, avec sigma, le champ de source qui génère son potentiel. Le puits linéaire est une énergie ou une masse² effective, pas nécessairement le profil de Phi. Leurs dimensions diffèrent.
- Un gradient spatial ∂yPhi n'est pas automatiquement le potentiel chimique 4D. Il faut montrer un opérateur covariant et sa réduction produisant un coefficient temporel de jB^0 dans le référentiel du plasma. Le courant topologique 1+1 peut être un point de départ, pas la preuve.
- L135–146 : jw·jB/M_S² ne viole pas en soi le nombre baryonique; jB est invariant sous U(1)_B. Il ne suffit donc pas à ouvrir le canal p→quantum léger+lepton allégué. La conclusion «seule échappatoire : masse mX>mp» exclut sans raison des petits couplages, symétries ou règles de sélection. Les opérateurs baryon-violants réels doivent être écrits.
- L168–174 : Tf=MX/25 emprunte une règle approximative dépendant des taux; l'autre estimateur contact ignore le seuil. Les remplacer mutuellement n'est pas une solution cinétique.
- L181–215 : prendre chi=T²/6 à 47–200MeV ignore la susceptibilité baryonique QCD et les changements d'entropie. Le eta baryons/photons de Planck aujourd'hui n'est pas automatiquement celui à Tf; suivre Y_B=nB/s. Les b_w=1–5 sont des valeurs ajustées pour reproduire eta, pas une prédiction de eta.
- La direction CMB sous hypothèse comobile est une référence cinématique possible (L231–245). Une modulation observable A=beta exige sa réponse propre; toute interaction ne donne pas universellement ce coefficient.

## Meilleure piste récupérable

Pour répondre au vrai objectif, concentrer le prochain article sur une géométrie 5D cohérente et un spectre/couplage testable. Ne pas intégrer cosmologie galactique, baryogenèse et Fano comme validations du rayon.

Deux axes, de force différente :
1. Résultat mathématique ou EFT contrôlé : opérateur Sturm–Liouville relativiste, conditions aux bords, spectre, poids au bord, fonction de Green/force, invariants de projection. Peut produire un article limité mais exact, indépendamment d'une valeur universelle R.
2. Si un rayon est le but central : choisir action et contenu de champs minimaux; calculer le potentiel effectif complet en cadre Einstein avec Casimir signé, termes locaux, boucles, tensions et stabilisateur; résoudre ∂V=0, Hessienne positive et conditions de raccord; fixer paramètres sans injecter R ciblé ou rho_Lambda pour revendiquer une prédiction indépendante. Puis contrôler rayon, masse radion, forces et cosmologie.

Une proposition honnête de court terme pourrait comparer familles de spectres cohérents et identifier quelles mesures de masses ET de poids de bord permettent de reconstruire un intervalle. C'est une prédiction conditionnelle falsifiable. Le titre ne devrait pas annoncer la découverte d'une cinquième dimension, une valeur finale de R, ni une ambition Nobel.

## Couverture et fichiers disponibles

Lecture complète des huit sources TeX principales, et de l'annexe section_dictionary_finale.tex de VIII. Examen de11 scripts/annexe ciblés, inventaire récursif du dépôt entier. Pas d'audit de tous les autres scripts, pas de revalidation des bases géométriques externes, pas de nouvelle analyse SPARC/Gaia/LHCb. Les scripts Python n'ont pas été exécutés : le runtime disponible n'a pas scipy. Les conversions numériques principales, la dépendance de T, et la normalisation Airy de demi-droite ont été vérifiées indépendamment par calcul analytique et arithmetic Javascript.

Sources locales intégrales :
work/original-audit/DDF_I-VIII_2026-08-29/article-1/tex/DDF_I_the_stage.tex
work/original-audit/DDF_I-VIII_2026-08-29/article-2/tex/DDF_II_the_well_and_the_tower.tex
work/original-audit/DDF_I-VIII_2026-08-29/article-3/tex/DDF_III_the_medium.tex
work/original-audit/DDF_I-VIII_2026-08-29/article-4/tex/DDF_IV_one_scale_and_its_shadow.tex
work/original-audit/DDF_I-VIII_2026-08-29/article-5/tex/DDF_V_type_I_prime_strings.tex
work/original-audit/DDF_I-VIII_2026-08-29/article-6/tex/DDF_VI_candidate_geometry.tex
work/original-audit/DDF_I-VIII_2026-08-29/article-7/tex/DDF_VII_seven_charge_classes.tex
work/original-audit/DDF_I-VIII_2026-08-29/article-8/tex/DDF_VIII_vacuum_winding_baryogenesis.tex

Fichiers additionnels locaux :
article-1/scripts/casimir.py, G6_yukawa.py, core_scale.py;
article-2/scripts/u_derive.py, spectrum.py, cb_definitif.py;
article-5/scripts/repro.py;
article-6/scripts/verify.py;
article-8/scripts/v1_convention.py, v2_v3_gaps.py;
article-8/tex/section_dictionary_finale.tex.

Pour citations publiques stables, utiliser :
https://github.com/HBoufourou/DDF_I-VIII_2026-08-29/blob/054ffdc1bf2e2b50ac0881d67199e15887b4d783/DDF_I-VIII_2026-08-29/{chemin}#L{ligne}

