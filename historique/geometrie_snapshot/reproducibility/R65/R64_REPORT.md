# R64 — Porte de substance : critère de construction et obstruction parité–Hodge

**Date :** 4 septembre 2026  
**Projet :** DDF I–VIII  
**Dépendance :** la porte géométrique R63 est supposée acquise  
**Objet :** chercher un résultat invariant au-delà de l'exemple POLY944/sigma5, sans déduire artificiellement \(R(t)\), une échelle micrométrique ou une tour quantique.

## 1. Verdict exécutif

R64 a testé les deux voies demandées.

### Voie A — théorème général de construction

La preuve quasi-Fano de R63 se généralise effectivement à toute coupe
anticanonique transverse d'une famille ambiante semi-stable à deux
composantes dont les strates sont \(\mathcal O\)-acycliques. Dans le cas
torique projectif, les annulations requises sont automatiques.

Le résultat est correct et utile comme critère de recherche, mais son
architecture est déjà couverte par les travaux sur les dégénérescences
toriques semi-stables, les *short tops*, les partitions nef et les
dégénérescences de Tyurin. Il ne peut donc pas porter seul la nouveauté de
l'Article 1.

### Voie B — obstruction équivariante générale

R64 obtient un résultat plus fort que le scan de signes de R62 :

> **Obstruction parité–Hodge conditionnelle.** Dans une dégénérescence de Tyurin projective
> à deux composantes, munie d'une involution holomorphe globale compatible
> avec une projection Type IIB standard O3/O7 ou O5/O9, aucun tube propre
> actif survivant comme vecteur fermé de \(C_4\), construit à partir d'une
> classe propre \(C\) de la couture K3, ne peut satisfaire
> \(C^2\geq0\), dès que \(C\neq0\), sous l'hypothèse que la tube map de
> Clemens est équivariante avec le signe de plomberie déclaré.

L'énoncé vaut que l'involution préserve les deux branches ou les échange. Il
ne suppose ni \(L=U(2)\), ni une action torique, ni une action diagonale de
Cox, ni la classification de Nikulin. Son noyau est la formule de parité du
cercle de plomberie suivie de la signature \((3,19)\) de la K3.

Pour toute couture R63 satisfaisant effectivement

\[
\operatorname{NS}(S)=L=U(2),
\]

le secteur actif de la parité exigée est même nul. Sur un lieu de
Noether–Lefschetz, il peut être non nul, mais reste négatif défini.

### Décision R64

~~~text
GENERAL_ANTICANONICAL_CUT_CRITERION = PROVED_BUT_STANDARD
PARITY_HODGE_C4_EIGENTUBE_OBSTRUCTION = CONDITIONAL_RATIONAL_PROPOSITION
FOUR_STANDARD_TRUNCATION_SIGN_CASES = COVERED_CONDITIONALLY
BRANCH_SIGN_CASES = COVERED_CONDITIONALLY
IF_NS_EQUALS_L_EQUALS_U2_REQUIRED_ACTIVE_EIGENLATTICE = ZERO
INTEGRAL_EQUIVARIANT_TUBE_MAP = OPEN
GLOBAL_ORIENTIFOLD_REALIZATIONS = NOT_CONSTRUCTED
R64_INTERNAL_SUBSTANCE_GATE = PASS_NARROW
INDEPENDENT_NOVELTY_CERTIFICATION = OPEN
ARTICLE_1_READY_FOR_SUBMISSION = NO
METRIC_R_AND_MICROMETRIC_SCALE = NOT_DERIVED
NEUTRAL_KK_OR_OPEN_STRING_TOWER = NOT_EXCLUDED
FANO_PLANE = DEFERRED
~~~

Le mot PASS_NARROW signifie qu'un énoncé conceptuel conditionnel subsiste après
suppression des noms POLY944 et sigma5. Il ne signifie ni que sa priorité
bibliographique est certifiée, ni que l'article est prêt.

## 2. Données et conventions

On considère une dégénérescence projective semi-stable de Calabi–Yau
trois-dimensionnels

\[
f:\mathcal Y\longrightarrow\Delta,
\qquad
\mathcal Y_0=Y_1\cup_S Y_2,
\]

où \(\mathcal Y\) est lisse, \(S\) est une K3 lisse et, près de \(S\), la
famille possède le modèle

\[
uv=t.
\]

Le réseau prolongeable est

\[
L=\operatorname{im}\!\left(
H^2(Y_1,\mathbb Z)\oplus H^2(Y_2,\mathbb Z)
\longrightarrow H^2(S,\mathbb Z)
\right),
\]

et le réseau actif est représenté par

\[
\Lambda=L^\perp\subset H^2(S,\mathbb Z).
\]

Lorsque l'identification intégrale entre quotient et orthogonal nécessite
un passage à un sur-réseau, la proposition est lue dans
\(\Lambda_{\mathbb Q}=L_{\mathbb Q}^{\perp}\). Multiplier une classe par un
entier ne change ni sa parité ni le signe de son carré.

Une « classe propre » signifie une classe propre de l'involution :

\[
\sigma^*C=\epsilon_C C,
\qquad \epsilon_C\in\{+1,-1\}.
\]

Cette hypothèse est naturelle pour un état fermé après projection, mais elle
ne traite pas à elle seule la dynamique d'une paire brane–image.

## 3. Voie A : critère général de coupe anticanonique

### 3.1 Lemme d'acyclicité

Soient \(V\) une variété lisse projective connexe et \(T\subset V\) un
diviseur lisse connexe. Si

\[
H^q(V,\mathcal O_V)=H^q(T,\mathcal O_T)=0\quad(q>0),
\]

alors

\[
H^q(V,\mathcal O_V(-T))=0\quad\text{pour tout }q.
\]

En effet, la suite

\[
0\to\mathcal O_V(-T)\to\mathcal O_V\to\mathcal O_T\to0
\]

et l'isomorphisme des constantes \(H^0(\mathcal O_V)\to
H^0(\mathcal O_T)\) donnent immédiatement l'annulation.

Si un diviseur lisse \(Y\subset V\) vérifie

\[
K_V+Y\sim -T,
\]

la dualité de Serre donne ensuite

\[
H^a(V,\mathcal O_V(-Y))^\vee
\simeq H^{\dim V-a}(V,\mathcal O_V(-T))=0.
\]

La suite de \(Y\) implique donc

\[
H^q(Y,\mathcal O_Y)=0\quad(q>0),
\qquad H^0(Y,\mathcal O_Y)=\mathbb C.
\]

### 3.2 Théorème de coupe

Soit \(g:\mathfrak V\to\Delta\) une famille projective semi-stable de
dimension relative quatre, d'espace total lisse, avec

\[
\mathfrak V_0=V_1\cup_TV_2.
\]

On suppose que \(V_1,V_2,T\) et une fibre ambiante générale sont
\(\mathcal O\)-acycliques. Soit
\(\mathfrak Y\in|-K_{\mathfrak V/\Delta}|\) une coupe lisse et transverse à
toutes les strates. Alors

\[
\mathfrak Y_0=Y_1\cup_SY_2,
\qquad Y_i=\mathfrak Y\cap V_i,
\qquad S=\mathfrak Y\cap T,
\]

est une dégénérescence de Tyurin au sens de
Doran–Harder–Thompson :

- la fibre centrale est réduite SNC ;
- \(S\) est une K3 ;
- \(S\in|-K_{Y_i}|\) ;
- \(H^{>0}(Y_i,\mathcal O_{Y_i})=0\), donc les \(Y_i\) sont quasi-Fano ;
- \(N_{S/Y_1}\otimes N_{S/Y_2}\simeq\mathcal O_S\) ;
- la carte logarithmique locale est saturée, \(1\mapsto(1,1)\).

La preuve combine l'adjonction

\[
K_{V_i}+Y_i\sim-T,
\qquad K_{Y_i}\sim-S,
\]

le lemme précédent et les cartes \(t=u,v,uv\). Si chaque composante
ambiante et chaque strate est torique, l'acyclicité du faisceau structural
est automatique.

### 3.3 Portée réelle de la voie A

Ce théorème explique pourquoi les annulations de R63 ne sont pas un hasard
numérique et fournit une porte réutilisable pour scanner d'autres fans. Mais
les cadres de Hu, Davis et al., Doran–Harder–Thompson et
Doran–Kostiuk–You couvrent déjà le principe géométrique général. La voie A
est donc gardée comme lemme de méthode, pas comme revendication de priorité.

## 4. Voie B : proposition uniforme conditionnelle de parité–Hodge

### 4.1 Hypothèses exactes

On ajoute aux données du §2 :

1. une involution holomorphe
   \(\sigma:\mathcal Y\to\mathcal Y\) au-dessus de l'identité de
   \(\Delta\) ;
2. une action qui préserve séparément \(Y_1,Y_2\), ou les échange ;
3. une projection Type IIB standard O3/O7 ou O5/O9 ;
4. une classe active non nulle \(C\in\Lambda_{\mathbb Q}\), propre sous
   \(\sigma\) ;
5. la naturalité équivariante du tube de Clemens ;
6. la demande que \(\operatorname{Tub}(C)\) appartienne au secteur interne de
   \(H^3\) qui fournit un vecteur fermé de \(C_4\).

La projectivité et la globalité de \(\sigma\) fournissent une classe ample
invariante \(h\in L\) : si \(\mathcal H\) est relativement ample, alors
\(\mathcal H\otimes\sigma^*\mathcal H\) l'est encore, et sa restriction à
\(S\) est invariante et prolongeable.

### 4.2 Calcul complet des signes

Posons

\[
s=\epsilon_{\Omega_3}=\begin{cases}
-1,&\text{O3/O7},\\
+1,&\text{O5/O9},
\end{cases}
\qquad
\eta=\begin{cases}
+1,&Y_1,Y_2\text{ préservées},\\
-1,&Y_1,Y_2\text{ échangées}.
\end{cases}
\]

Dans le modèle \(uv=t\),

\[
\Omega_3=\Omega_S\wedge d\log u.
\]

Si les branches sont échangées,
\(d\log u\mapsto d\log v=-d\log u\). Ainsi

\[
\epsilon_{\Omega_S}=s\eta.
\]

La naturalité de la construction du tube donne

\[
\sigma_*\operatorname{Tub}(C)
=\eta\operatorname{Tub}(\sigma_*C),
\qquad
\epsilon_{\operatorname{Tub}(C)}=\eta\epsilon_C.
\]

Les tables de réduction de \(C_4\) donnent :

- O3/O7 : les vecteurs fermés proviennent de \(H^3_+\) ;
- O5/O9 : ils proviennent de \(H^3_-\).

Dans les deux cas, la parité interne requise vaut \(-s\). Par conséquent

\[
\eta\epsilon_C=-s
\quad\Longrightarrow\quad
\boxed{\epsilon_C=-\epsilon_{\Omega_S}}.
\]

La classe de couture et la forme holomorphe ont toujours des parités
opposées. Les quatre cas sont :

| Projection | Branches | \(\epsilon_{\Omega_S}\) | \(\epsilon_C\) requis |
|---|---|---:|---:|
| O3/O7 | préservées | \(-1\) | \(+1\) |
| O3/O7 | échangées | \(+1\) | \(-1\) |
| O5/O9 | préservées | \(+1\) | \(-1\) |
| O5/O9 | échangées | \(-1\) | \(+1\) |

Cette table inclut le cas où l'échange des branches induit l'identité sur
\(S\). Dans ce cas, le secteur anti-invariant de \(S\) est simplement nul ;
on ne doit pas invoquer \(E_8(-2)\).

### 4.3 Lemme du trois-plan positif

Le plan réel

\[
P_\Omega=\langle\Re\Omega_S,\Im\Omega_S\rangle
\]

est positif défini. La classe de Kähler \(h\) est positive et orthogonale à
\(P_\Omega\). Ainsi

\[
P=\langle\Re\Omega_S,\Im\Omega_S,h\rangle
\]

est un trois-plan positif maximal dans \(H^2(S,\mathbb R)\), de signature
\((3,19)\). Son orthogonal \(P^\perp\) est négatif défini.

Comme \(\epsilon_C=-\epsilon_{\Omega_S}\), l'invariance de l'accouplement
donne

\[
(C,\Omega_S)
=(\sigma C,\sigma\Omega_S)
=-(C,\Omega_S)=0.
\]

Donc \(C\perp P_\Omega\). Il reste à montrer \(C\perp h\).

- Si \(\epsilon_C=-1\), cela suit de la parité de \(C\) et de l'invariance de
  \(h\).
- Si \(\epsilon_C=+1\), alors
  \(\epsilon_{\Omega_S}=-1\). L'activité donne \(C\in L^\perp\), tandis que
  \(h\in L\).

Dans tous les cas, \(C\in P^\perp\). Par conséquent

\[
\boxed{C\neq0\ \Longrightarrow\ C^2<0.}
\]

### 4.4 Proposition conditionnelle de non-existence

Sous les six hypothèses du §4.1, il n'existe aucune classe propre active non
nulle dont le tube survive comme vecteur fermé de \(C_4\) et dont le carré
soit nul ou positif.

Le mécanisme de Hassfeld–Monnee–Weigand–Wiesner demande précisément des
classes \(C_0^2\ge0\) pour obtenir, après rotation hyperkählérienne, une
courbe de genre au moins un et argumenter en faveur d'états multi-enroulés.
R64 exclut donc tout le cône non négatif de ce **mécanisme fermé propre**,
pas seulement le cas isotrope \(C^2=0\).

Cette phrase ne transforme pas l'argument physique de non-annulation des
indices BPS en théorème mathématique. Elle montre seulement qu'aucune charge
survivante dans la classe testée ne satisfait sa condition géométrique
nécessaire.

## 5. Application à la couture R63

### 5.1 Réseau très général — corollaire conditionnel

La couture R63 est une double couverture

\[
S\longrightarrow\mathbb P^1\times\mathbb P^1
\]

ramifiée sur une courbe \((4,4)\). Si la sous-famille de coefficients R63
atteint bien le point très général de la famille pertinente — la porte A3
reste à fermer — alors

\[
\operatorname{NS}(S)=L=U(2),
\qquad
G_L=\begin{pmatrix}0&2\\2&0\end{pmatrix}.
\]

La parité opposée à celle de \(\Omega_S\) place \(C\) dans
\(H^{1,1}(S)\cap H^2(S,\mathbb Q)=\operatorname{NS}(S)_{\mathbb Q}\).
L'activité impose en même temps \(C\in L_{\mathbb Q}^{\perp}\). Puisque
\(L\) est non dégénéré,

\[
\boxed{C=0.}
\]

Le renforcement « secteur nul » exige donc \(NS(S)=L=U(2)\) et reste
conditionnel à A3 pour l'application R63. La proposition de négativité
défini, lui, reste valable sur les spécialisations de
Noether–Lefschetz.

### 5.2 Classification entière recoupée

Le certificat indépendant donne

\[
O(U(2),\mathbb Z)=\{I,-I,S,-S\},
\qquad S(h_1)=h_2,
\]

et seuls \(I,S\) préservent la composante ample. Les seuls isotropes
primitifs de \(U(2)\) sont

\[
\pm h_1,\quad\pm h_2.
\]

Ils appartiennent à \(L\), pas au secteur actif \(L^\perp\). Pour une K3
très générale de cette famille, le recollement discriminant et Torelli
laissent seulement l'identité et l'involution de revêtement.

Le fan de couture possède huit automorphismes de réseau, mais le fan résolu
quatre-dimensionnel n'admet aucun automorphisme de réseau échangeant les deux
tops. Cette dernière phrase ne classe pas les automorphismes non toriques ou
les modèles reliés par flops.

### 5.3 Correction de portée de R62–R63

Le scan des \(512\) signes reste exhaustif uniquement pour les changements
diagonaux des neuf coordonnées de Cox. En revanche, la preuve du no-go ne
dépend plus de ce scan.

L'ancienne justification de la branche échangée par
\(H^2(S)^-\simeq E_8(-2)\) n'est correcte que pour une involution
symplectique non triviale sur \(S\). R64 la remplace par le lemme du
trois-plan positif, qui couvre aussi \(\sigma|_S=\mathrm{id}\).

## 6. Contre-exemples et frontières

Les hypothèses ne peuvent pas être supprimées sans changer le verdict.

### 6.1 Sans activité

L'involution de revêtement fixe les classes isotropes \(h_1,h_2\in L\).
L'affirmation « aucune classe paire isotrope n'existe » serait donc fausse.
Ces classes meurent dans le gradin actif parce qu'elles sont prolongeables.

### 6.2 Sans classe ample prolongeable

Dans \(U(2)\), si l'on remplace \(L\) par le sous-réseau dégénéré
\(L_0=\mathbb Zh_1\), alors \(h_1\in L_0^\perp\) et \(h_1^2=0\). La
projectivité équivariante, qui fournit \(h\in L\), est donc essentielle.

### 6.3 Dans le parent \(\mathcal N=2\)

Pour R63,

\[
L^\perp\simeq U\oplus U(2)\oplus E_8(-1)^{\oplus2}
\]

a signature \((2,18)\) et contient des isotropes primitifs. R64 ne réfute pas
la tour parentale candidate ; il démontre que la projection fermée propre
testée sélectionne la mauvaise parité pour ses classes non négatives.

### 6.4 Sans état propre

Une classe \(C\) et son image \(\sigma C\) peuvent former une paire sans que
\(C\) soit propre. Les combinaisons projetées doivent alors être étudiées
avec leurs charges, leur calibration et leur stabilité. R64 ne transforme
pas ce problème dynamique en un simple calcul de réseau.

### 6.5 Hors du cadre géométrique

Ne sont pas couverts : actions anti-holomorphes ou non géométriques, action
non triviale sur le paramètre \(t\), dégénérescences à plus de deux
composantes, secteurs ouverts ou relatifs, flux, tadpoles, corrections
quantiques, et co-scaling des modules de Kähler.

## 7. Antériorité et nouveauté

### 7.1 Ce qui est déjà connu

- Les constructions toriques semi-stables et de Tyurin issues de
  partitions/tops sont antérieures à DDF.
- La double K3 \((4,4)\), sa polarisation très générale \(U(2)\) et
  l'arithmétique élémentaire de ce réseau sont connues.
- Les limites de Tyurin comme limites de type II et le mécanisme de tours
  D3 parentales ont été analysés par Hassfeld et al.
- Kaufmann et al. ont déjà montré, dans un exemple
  \(K3\times T^2\) O-type B, qu'une involution anti-symplectique projette le
  réseau transverse pertinent, et ont formulé des obstructions O-type A/B
  beaucoup plus générales au niveau F-théorie et corrections quantiques.
- L'idée « limite de Tyurin + direction interne longue/micrométrique » a une
  collision directe avec Braun–Cicoli–Milioli–Valandro (2026).

### 7.2 Raffinement exact apporté par R64

Le candidat propre à R64 est l'assemblage suivant :

1. formule uniforme \(\epsilon_C=-\epsilon_{\Omega_S}\) ;
2. preuve par le trois-plan positif pour toute K3 de couture projective ;
3. couverture simultanée O3/O7 et O5/O9 ;
4. couverture des branches préservées et échangées, y compris l'identité sur
   la couture ;
5. exclusion de toutes les normes \(C^2\ge0\), pas seulement des isotropes ;
6. corollaire de nullité conditionnel à \(NS(S)=L=U(2)\).

Le cœur Hodge est élémentaire et le message physique général possède une
antériorité proche. R64 ne revendique donc ni « premier no-go », ni
« classification de tous les orientifolds ». La priorité de cette
formulation précise reste à faire vérifier par un spécialiste externe.

### 7.3 Identification intrinsèque du modèle

La recherche R64 identifie le polytope résolu à une forme normale déjà
présente dans Kreuzer–Skarke, d'empreinte

\[
M:104\ 14,\quad N:10\ 8,\quad H:(5,85).
\]

Le polytope n'est donc pas nouveau. Restent potentiellement propres au
dossier : la phase résolue, la correction simultanée des seize ODP, le fan
relatif, la paire exacte de quasi-Fano et le morphisme de restriction. Leur
non-collision complète n'est pas encore démontrée.

## 8. Décision éditoriale pour l'Article 1

R64 change la stratégie, mais n'autorise pas un dépôt immédiat.

L'Article 1 le plus défendable serait un article étroit de géométrie
computationnelle :

> résolution crépante des seize ODP de la phase choisie, extension en une
> famille de Tyurin explicite, calcul du réseau de restriction et de la LMHS,
> puis proposition équivariante de parité–Hodge clairement conditionnelle.

Avant envoi à une revue avec évaluation par les pairs, il faut encore :

1. intégrer la forme normale Kreuzer–Skarke et la matrice unimodulaire dans
   le manuscrit ;
2. donner les seize modèles locaux ODP et certifier la résolution simultanée ;
3. fermer la dominance de la famille de coefficients vers les branches
   \((4,4)\), ou affaiblir proprement « très général » ;
4. comparer la forme cubique, \(c_2\cdot D\), la phase/SR et le fan relatif
   aux collisions \((5,85)\) connues ;
5. faire relire séparément la proposition équivariante par un géomètre K3 et un
   spécialiste des orientifolds.

La décision d'arXiv interdit une simple resoumission du manuscrit refusé. Le
chemin sûr est donc : article réellement reconstruit, soumission à une revue
conventionnelle, puis appel arXiv uniquement si la revue accepte et fournit
le DOI ou la preuve de statut demandée.

Le dépôt GitHub public a également été contrôlé au commit
054ffdc1bf2e2b50ac0881d67199e15887b4d783. Son README présente encore
\(8.2\,\mu\mathrm m\) et les anciens articles comme un cadre consolidé avec
preuves certifiées. Cela contredit les frontières R63–R64. Aucune écriture
distante n'a été effectuée : le dépôt doit d'abord être transformé en archive
historique avec errata, puis recevoir le nouveau paquet dans un emplacement
séparé après validation humaine.

## 9. Conséquence pour la théorie DDF

R64 ne « tue » pas DDF. Il sépare désormais trois branches :

- **DDF-G :** noyau géométrique Tyurin R63, conservé ;
- **DDF-KK :** recherche d'une tour neutre métrique, non touchée par le
  no-go \(C_4\) ;
- **DDF-BPS :** tour candidate dans le parent \(\mathcal N=2\), conservée,
  mais sa descente fermée propre standard est obstruée.

L'étape R65 reste donc le pilote spectral préenregistré. R66 appliquera le
pipeline à une géométrie unique. Ni le rayon \(R\), ni sa relation à \(t\),
ni une valeur en microns ne doivent être choisis avant ces calculs. Le plan
de Fano reste différé jusqu'à l'existence d'un réseau de charges physiques
et d'une tour calculée.

## 10. Reproductibilité

Commande unique :

~~~bash
python3 r64_substance_gate.py
~~~

Les certificats spécialisés sont :

- meta_audit_r64/r64_equivariant_nogo_audit.py ;
- meta_audit_r64/r64_lattice_classification.py ;
- meta_audit_r64/r64_boundary_certificate.py ;
- les rapports contradictoires de meta_audit_r64/.

## 11. Sources primaires minimales

1. S. Hu, *Semi-Stable Degeneration of Toric Varieties and Their
   Hypersurfaces*, [arXiv:math/0110091](https://arxiv.org/abs/math/0110091).
2. R. Davis et al., *Short Tops and Semistable Degenerations*,
   [arXiv:1307.6514](https://arxiv.org/abs/1307.6514).
3. C. F. Doran, A. Harder, A. Thompson, *Mirror symmetry, Tyurin
   degenerations and fibrations on Calabi–Yau manifolds*,
   [arXiv:1601.08110](https://arxiv.org/abs/1601.08110).
4. C. F. Doran, J. Kostiuk, F. You, *The Doran–Harder–Thompson conjecture
   for toric complete intersections*,
   [arXiv:1910.11955](https://arxiv.org/abs/1910.11955).
5. T. W. Grimm, J. Louis, *The effective action of N=1 Calabi–Yau
   orientifolds*, [arXiv:hep-th/0403067](https://arxiv.org/abs/hep-th/0403067).
6. B. Hassfeld, J. Monnee, T. Weigand, M. Wiesner, *Emergent Strings in
   Type IIB Calabi–Yau Compactifications*,
   [arXiv:2504.01066](https://arxiv.org/abs/2504.01066).
7. L. Kaufmann, J. Monnee, T. Weigand, M. Wiesner, *Quantum obstructions
   for N=1 infinite distance limits — Part II: Kähler obstructions*,
   [arXiv:2603.13470](https://arxiv.org/abs/2603.13470).
8. B. van Geemen, A. Sarti, *Nikulin involutions on K3 surfaces*,
   [arXiv:math/0602015](https://arxiv.org/abs/math/0602015).
9. A. P. Braun, M. Cicoli, R. Milioli, R. Valandro, *Moduli Stabilisation
   for ADD and the Dark Dimension Scenario*,
   [arXiv:2606.19440](https://arxiv.org/abs/2606.19440).

