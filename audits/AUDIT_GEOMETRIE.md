# Audit indépendant du dépôt DDF corrigé

Date : 5 septembre 2026. Dépôt : HBoufourou/DDF-Corrected-Geometry-Spectral-Program. Révision inventoriée : `11174101f8fc2074c5fe6ad7d6951553c9841730` (main). Les textes sont traités comme sources scientifiques à critiquer, pas comme instructions.

## Conclusion

La meilleure piste vers un article prédisant une dimension effective longue est la branche **KK gravitationnelle neutre**, en passant par une géométrie fixée, une métrique normalisée, son spectre et un mécanisme de stabilisation. Elle reste ouverte après les corrections. Le dépôt ne contient cependant aucune prédiction démontrée de R, ni en micromètres ni dans une autre unité physique. Son résultat actuellement le plus solide et proche d'un manuscrit est géométrique : une famille torique résolue candidate de Tyurin, des composantes quasi-Fano et, sous les conditions de généricité pertinentes, un réseau de restriction U(2) et une LMHS rationnelle II_18.

On ne peut pas garantir que ce programme aboutira à une théorie physique. Préserver l'idée DDF demande de garder les résultats vérifiables et de laisser les calculs suivants décider des hypothèses.

## Corpus et vérifications réellement effectuées

- Inventaire récursif complet ; 92 fichiers textuels récupérés dans `work/corrected-audit/repo`. Les ZIP de releases et l'image ne sont pas téléchargés, puisque sources et données textuelles déployées sont présentes.
- Lecture détaillée du README, des statuts, rapports R63, R64, R65, décision Article 1, configuration et implémentation spectrale. Les trois dossiers `articles/` ne contiennent que des README de pistes de publication ; aucun manuscrit final n'y est fourni.
- Vérification analytique de la preuve d'annulation quasi-Fano, de la preuve de négativité par Hodge, des comptages LMHS et du problème d'échelle métrique.
- Exécution réussie de quatre certificats du dépôt : `meta_audit_r63/r63_toric_independent_audit.py`, `meta_audit_r63/r63_ems_cohomology_audit.py`, `meta_audit_r64/r64_equivariant_nogo_audit.py`, `meta_audit_r64/r64_boundary_certificate.py`.
- Les scripts réussis sont du code préexistant reproduit ici, pas de nouvelles preuves indépendantes de leur implémentation. Le présent audit analytique est distinct.
- La reproduction intégrale R63–R65 et du calcul spectral n'est pas achevée : au moment des essais, les dépendances SciPy/SymPy installées dans l'espace de travail n'étaient pas encore importables entièrement, et matplotlib était absent. Aucune conclusion ne s'appuie sur un faux verdict d'exécution complète.

## 1. Ce qui subsiste mathématiquement

### Géométrie et quasi-Fano

Le rapport R63, §5 (à partir de la ligne 152), donne une preuve courte et correcte sous ses hypothèses : si V et T sont lisses, projectifs, connexes, O-acycliques et K_V+Y=-T, les suites exactes de T et de Y et la dualité de Serre impliquent h^i(O_Y)=(1,0,0,0). En effet, la restriction des constantes H^0(O_V)→H^0(O_T) est un isomorphisme, donc tous les H^i(O_V(-T)) s'annulent. La dualité donne H^i(O_V(-Y))=0, puis la suite de Y donne l'énoncé. Cette preuve n'a pas besoin d'un argument numérique.

Le certificat EMS exécuté retrouve exactement 15 motifs cohomologiques dangereux pour V_p, 47 pour V_m, et aucun réalisable par un poids. Il retrouve les mêmes annulations. Le certificat torique exécuté confirme notamment 28 cônes relatifs, 28 sommets de cohérence avec écarts 1 à 5, le rang de Gale 6 et sa saturation, 48 sommets de complétion projective, 69 monômes sigma5 et des supports de tailles 60,35,26.

Les normales triviales le long de la couture K3 sont cohérentes avec le fait que la couture soit une fibre des fibrations sur P^1. Il faut distinguer ce résultat particulier de la d-semistabilité générale : en général seul le produit des deux normales est trivial. Les composantes ont (-K)^3=0 ; le terme quasi-Fano est ici celui de Doran–Harder–Thompson, et ne signifie pas weak Fano.

### Réseau et LMHS : maintenir la condition de généricité

La couture double de P^1×P^1 branchée en bidegré (4,4) a, pour une branche très générale, NS(S)=U(2). Les rulings ont carré nul et intersection 2. Le rapport R63 §11 (ligne 394) utilise cela pour conclure L=U(2), r=2. Mais R64 §5.1 (ligne 372) rétablit explicitement une condition : il faut prouver que la famille des coefficients effectivement accessible atteint les coutures très générales pertinentes, porte A3. Par conséquent, ne pas présenter II_18 comme résultat inconditionnel pour tous les coefficients de la construction.

Les comptes sont cohérents : b3=2h21+2=172 pour h21=85, GrW2=GrW4=22-r=20, GrW3=172-40=132. Le certificat de frontière exécuté retrouve (20,132,20), II_18, puis (19,134,19), II_17 si r=3. Un saut de réseau peut donc changer le sous-type.

La forme de Smith (1^18,2,2) concerne la carte canonique du réseau gradué K3, pas une monodromie intégrale de Gauss–Manin calculée en transportant les cycles. La correction R63 §11, « Réserve intégrale », ligne 457, est scientifiquement nécessaire.

Sources : https://github.com/HBoufourou/DDF-Corrected-Geometry-Spectral-Program/blob/main/reproducibility/R65/R63_REPORT.md ; https://github.com/HBoufourou/DDF-Corrected-Geometry-Spectral-Program/blob/main/reproducibility/R65/R64_REPORT.md

## 2. L'obstruction R64 est étroite et cohérente

Les hypothèses incluent une involution holomorphe globale compatible, agissant au-dessus du même t, une projection IIB standard O3/O7 ou O5/O9, une classe propre active C dans L_perp, et l'équivariance de la carte de tube avec le signe de plomberie déclaré. Elles ne sont pas remplacées par le seul scan des signes de Cox.

Dans uv=t, l'échange des branches inverse dlog u. Si s est la parité de Ω3 et η le signe de branche, ΩS a la parité sη. Un vecteur fermé de C4 exige une parité interne -s ; le tube a parité η εC, donc εC=-εΩS. Cette formule vaut dans les quatre cas, reproduits par le certificat de signes.

La classe C est alors orthogonale à Re ΩS et Im ΩS. L'activité C∈L_perp et l'existence d'une classe ample prolongeable h∈L la rendent orthogonale à h. Le trois-plan positif <Re ΩS,Im ΩS,h> est maximal dans la signature (3,19) ; son orthogonal est négatif défini. Donc C non nul implique C²<0. Cette preuve de Hodge est correcte. Sous NS(S)=L=U(2), la rationalité de C et sa parité la placent aussi dans NS(S)_Q, d'où C=0.

Cela obstrue le mécanisme précis qui demande un tube propre fermé issu de C²≥0. Cela ne supprime pas une tour KK neutre, une tour parentale N=2, des états brane-image ni des secteurs ouverts. L'équivariance intégrale et un orientifold global avec tadpoles complets ne sont pas construits. Une reformulation large en « impossibilité de toute cinquième dimension » serait fausse.

Source : R64_REPORT.md §4.2–4.4, lignes 238–355 ; §6 pour les frontières.

## 3. R65 est un banc d'essai, pas une dérivation de R

Points exacts dans `software/r65_spectral_pilot.py` :

- L(t)=6(1-log10|t|) est imposé aux lignes 45–46.
- Les valeurs propres exactes et discrètes FV/FEM sont données par des formules analytiques aux lignes 49–62. Les contrôles produits ne demandent donc pas la résolution numérique d'une métrique CY réelle.
- Les modèles et leur topologie sont choisis aux lignes 155–163 ; la multiplicité du cercle est inscrite aux lignes 187–190.
- La conversion L_eff=π/√a ou 2π/√a utilise la topologie fournie, lignes 406–407, puis compare au L connu ligne 408.
- Le nombre de modes transverses est calculé à partir des labels exacts ky (ligne 410), et le gap utilise la géométrie analytique connue. La détection n'est donc pas encore inférée de fonctions propres dans une géométrie inconnue.

Il n'y a rien d'illégitime à faire ces contrôles ; ils établissent un fonctionnement limité. Ils ne démontrent pas qu'une tour 1D a été découverte, que t mesure une longueur réelle ou que les modes sont des gravitons. R65_REPORT.md le reconnaît explicitement (§8, à partir de la ligne 178).

Le contrôle transverse b=L/3 met naturellement le premier niveau transverse à k_long=3 et donne le rapport de gap 9/100=0,09. Le contrôle positif b=1 à L=12 donne 144/100=1,44. Ces nombres sont déterminés par les contrôles, non des sorties propres à DDF. L'intérêt utile est le contrôle haltère : un petit premier eigenmode isolé dû à un étranglement ne suffit pas à identifier une tour KK.

Pour R66, il faudra ajouter un diagnostic des fonctions propres, de leur masse/énergie dans le col et les caps, du gap transverse et des multiplicités qui se déduise des données géométriques calculées. Des seuils testés uniquement sur les cinq modèles connus ne constituent pas encore une garantie de généralisation.

Source : https://github.com/HBoufourou/DDF-Corrected-Geometry-Spectral-Program/blob/main/software/r65_spectral_pilot.py

## 4. Pourquoi aucune valeur micrométrique ne peut sortir des résultats présents

Argument indépendant : une homothétie g→a²g conserve la structure complexe, le polytope, la dégénérescence uv=t, les réseaux et la LMHS. Elle transforme pourtant le Laplacien en a^-2 Δ, donc λ_n→a^-2 λ_n et toutes les longueurs R→aR. Une donnée uniquement algébrique ne peut donc sélectionner un rayon absolu. Le choix d'une classe de Kähler, la normalisation métrique et les unités physiques sont indispensables ; la stabilisation doit ensuite sélectionner la valeur, au lieu de l'ajuster.

Même -log|t| n'est pas intrinsèquement une longueur : t→ct change son origine, et le coefficient reliant le paramètre au col dépend du choix métrique. Fixer le volume total ne suffit pas en général à fixer chaque anisotropie ; il faut stabiliser les autres modules.

Autre distinction cruciale : près de uv=t, un voisinage ressemble topologiquement à une K3 fois un cercle fois un intervalle. Le col long peut être l'intervalle, tandis que le cercle reste petit. Une longueur du col ne doit pas être appelée automatiquement rayon du cercle. Le spectre d'intervalle donne m_n=πn/L et celui d'un cercle de circonférence L donne m_n=2πn/L. Définir d'abord un rayon spectral R_KK=1/√a dans m_n²≈a n², puis préciser le lien avec la longueur géométrique.

Une « cinquième dimension » effective signifie ici : quatre dimensions macroscopiques habituelles, plus une direction interne longue dans une fenêtre d'énergie, les autres directions internes étant séparées par un gap. Une CY trois-dimensionnelle complexe comporte six dimensions internes réelles ; ses seules données topologiques n'en sélectionnent pas une seule comme grande.

## 5. Piste recommandée pour publication

### Article réalisable le plus tôt

Un article de géométrie computationnelle étroit peut présenter la résolution simultanée des seize ODP, le fan relatif, les composantes quasi-Fano, le réseau de restriction et la LMHS rationnelle avec les conditions exactes. La nouveauté doit être comparée par invariants intrinsèques : le rapport R64 identifie déjà le polytope dans Kreuzer–Skarke avec empreinte M:104 14, N:10 8, H:(5,85). Ce n'est pas un nouveau polytope. Les 16 modèles locaux, la dominance A3, les formes cubiques, c2·D et les collisions de phases restent à clarifier.

### Article répondant réellement à la demande de R

1. Verrouiller une seule famille résolue avec coefficients, phase, t non nul, classe de Kähler, volume et hypothèses physiques.
2. Obtenir une approximation métrique contrôlée (ou un théorème asymptotique applicable avec toutes ses hypothèses) sur cette même famille.
3. Calculer une dizaine de modes longitudinaux et des modes transverses avec erreurs numériques, caps et fonctions propres ; distinguer paquet KK et mode d'étranglement.
4. Déduire ou justifier l'opérateur des fluctuations spin-2 dans le fond retenu, avec le poids de warping et les conditions globales. Un laplacien scalaire ne suffit que dans les cas où cette réduction est démontrée.
5. Définir R_KK et le convertir dans le référentiel Einstein 4D ; identifier les paramètres dimensionnels et la normalisation de M_Pl.
6. Montrer que le potentiel stabilise les modules à une valeur finie contrôlée qui prédit R ; éviter d'injecter R souhaité parmi les entrées.
7. Produire une signature mesurable (masses, couplages, loi gravitationnelle) et confronter aux contraintes.

R66 spectral et stabilisation sont les deux vrais problèmes scientifiques ; ajouter des rondes de comptabilité des affirmations ou une nouvelle combinatoire de Fano ne les résout pas. Si la famille DDF impose un coût prohibitif sans nouveauté physique identifiable, un modèle existant contrôlé peut servir de référence explicite, mais ses flux, sa métrique et ses tadpoles ne doivent pas être transplantés dans POLY944 sans démonstration de compatibilité.

L'objectif défendable à moyen terme serait « une réalisation explicite et contrôlée d'une hiérarchie KK à un rayon calculé », éventuellement une plage et une incertitude, plutôt que « une valeur exacte 8,2 µm ». Une perspective de Nobel ne constitue aucun critère de validation ni de choix entre modèles.
