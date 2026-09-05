# R63 — Audit bibliographique ciblé : Tyurin strict, couture (U(2)), type (II_{18}) et obstruction O3/O7

**Date de recherche : 4 septembre 2026.**  Cette note ne juge que le noyau R62–R63. Elle utilise en priorité les articles de recherche originaux et distingue ce qui est standard de ce qui peut encore constituer un résultat propre au modèle.

## Verdict exécutif

1. **R63 peut fermer le mot « Tyurin strict »** si le calcul annoncé prouve bien
   \[
   H^i(Y_p,\mathcal O_{Y_p})=H^i(Y_m,\mathcal O_{Y_m})=0\qquad(i>0).
   \]
   Dans la convention de Doran–Harder–Thompson, les autres ingrédients sont déjà présents dans R62 : (Y_p,Y_m) lisses, couture (S) lisse Calabi–Yau et (S\in|-K_{Y_p}|\cap|-K_{Y_m}|), espace total lisse et rencontre normale.
2. **La d-semistabilité ne devrait pas rester une hypothèse numérique.** Pour la famille lisse de R62 avec
   (Y_0=Y_p+Y_m=\operatorname{div}(t)), elle découle globalement de
   \[
   N_{S/Y_p}\otimes N_{S/Y_m}
   \simeq \mathcal O_{\mathcal Y}(Y_m+Y_p)|_S
   \simeq \mathcal O_S.
   \]
   Il faut écrire cette identité de fibrés et pas seulement vérifier le modèle local (uv=t).
3. **Ne sont pas nouveaux isolément :** la construction torique semistable par tops, la couture K3 double de (\mathbb P^1\times\mathbb P^1) branchée en ((4,4)), sa polarisation (U(2)), l'étiquette (II_{18}), la distinction d'orientifolds échangeant ou préservant les composantes, ni la difficulté générale des tours D3 après projection O3/O7.
4. **Candidat d'originalité défendable :** la combinaison, pour le modèle résolu précis issu de `POLY944`, d'un certificat d'éventail relatif, de la restriction intégrale primitive (U(2)), des données discriminantes, de la classification exhaustive des caractères diagonaux de Cox déclarés et d'un théorème de signature excluant une classe isotrope active de la bonne parité dans l'ansatz O3/O7. Aucune source trouvée ne contient ce résultat exact. Cela reste un **indice**, pas une preuve d'antériorité exhaustive.
5. **La littérature 2026 rend la barre plus haute.** Kaufmann–Monnee–Weigand–Wiesner traitent déjà les limites de type II avec orientifolds de type A/B et leurs obstructions quantiques; Braun–Cicoli–Milioli–Valandro relient déjà une limite de Tyurin à une dimension longue micrométrique dans un programme LVS. L'article DDF doit donc vendre le **modèle exact et son obstruction intégrale**, pas « Tyurin produit une dimension sombre ».

## 1. Définitions strictes à employer

### 1.1 Quasi-Fano et dégénérescence de Tyurin

Doran–Harder–Thompson donnent la convention directement applicable :

- une variété lisse (X) est **quasi-Fano** si (|-K_X|) contient un membre Calabi–Yau lisse et si (H^i(X,\mathcal O_X)=0) pour tout (i>0);
- une **dégénérescence de Tyurin** (\mathcal V\to\Delta) a espace total lisse et fibre centrale (X_1\cup_ZX_2), où les deux composantes sont quasi-Fano et se rencontrent normalement le long d'un (Z) lisse anticanonique dans chacune.

Source primaire : C. F. Doran, A. Harder, A. Thompson, *Mirror symmetry, Tyurin degenerations and fibrations on Calabi–Yau manifolds*, §2.1, Proc. Symp. Pure Math. 96 (2017), 93–131, [arXiv:1601.08110](https://arxiv.org/abs/1601.08110).

**Conséquence pour R63.** Dans cette convention précise, il n'est pas nécessaire d'ajouter séparément « (-K) gros et nef ». D'autres auteurs emploient « quasi-Fano » ou « weak Fano » autrement; l'article doit annoncer sa convention et ne pas les mélanger. Pour R62, la seule lacune visible vers cette définition est l'annulation de tous les (H^i(\mathcal O)), sous réserve que les preuves de lissité et d'adjonction soient reprises humainement.

### 1.2 d-semistabilité

Pour une variété SNC (X=X_1\cup_ZX_2) sans lieu triple,

\[
T_X^1:=\mathcal E xt^1(\Omega_X,\mathcal O_X)|_Z
\simeq N_{Z/X_1}\otimes N_{Z/X_2}.
\]

La d-semistabilité signifie (T_X^1\simeq\mathcal O_Z); dans le cas à deux composantes, c'est exactement la condition des fibrés normaux inverses. C'est la condition introduite dans le formalisme de Friedman et utilisée par Kawamata–Namikawa :

- R. Friedman, *Global smoothings of varieties with normal crossings*, Ann. of Math. **118** (1983), 75–114, [doi:10.2307/2006955](https://doi.org/10.2307/2006955).
- Y. Kawamata, Y. Namikawa, *Logarithmic deformations of normal crossing varieties and smoothing of degenerate Calabi–Yau varieties*, Invent. Math. **118** (1994), 395–409, [doi:10.1007/BF01231538](https://doi.org/10.1007/BF01231538), [copie auteur](https://imperium.lenin.ru/~kaledin/math/pdf/kawa-naka.pdf).

Le théorème de lissage de Kawamata–Namikawa a des hypothèses globales (Kähler/projectif, log Calabi–Yau, d-semistabilité et hypothèses cohomologiques dans sa forme originale). Il ne faut pas écrire « d-semistable implique lissable » sans les citer. Ici, l'existence du lissage n'a de toute façon pas à être déduite d'un théorème abstrait : R62 affirme déjà construire une famille semistable à espace total lisse. Cette construction rend la condition des normaux nécessaire et fournit sa preuve par restriction du diviseur principal (\operatorname{div}(t)).

### 1.3 Checklist minimale pour déclarer R63 « Tyurin strict »

| Condition | Statut R62 | Fermeture attendue en R63 |
|---|---|---|
| espace total lisse | certifié génériquement | reprendre le lemme de Jacobien/Bertini |
| fibre centrale réduite SNC, deux composantes | certifié | reprendre multiplicité un et (uv=t) |
| (Y_p,Y_m,S) lisses et irréductibles | certifié génériquement | préciser l'ouvert de paramètres |
| (S) K3 et (S\in|-K_{Y_i}|) | certifié par double couverture/adjonction | reprendre les fibrés, pas seulement les classes numériques |
| (H^i(Y_i,\mathcal O_{Y_i})=0), tout (i>0) | ouvert en R62 | calcul exact R63 |
| (N_{S/Y_p}\otimes N_{S/Y_m}\simeq\mathcal O_S) | impliqué par la famille | écrire la restriction de (Y_p+Y_m=\operatorname{div}(t)) |
| polarisation commune | (U(2)), image primitive | donner la matrice et le Smith |

## 2. Source exacte et méthode pour les annulations toriques

Soit (A=X_\Sigma) une variété torique complète simpliciale de dimension (d), (D=\sum_\rho a_\rho D_\rho), et (m\in M). Posons

\[
I_D(m)=\{\rho\in\Sigma(1):\langle m,v_\rho\rangle+a_\rho<0\}.
\]

Si (P) est le complexe simplicial des rayons de (\Sigma), alors (P_{\le I_D(m)}) désigne le **sous-complexe induit** sur ces rayons. La forme Čech/Alexander-duale donne, avec les conventions usuelles de cohomologie réduite,

\[
H^p(A,\mathcal O_A(D))_m
\simeq \widetilde H^{p-1}\!\left(P_{\le I_D(m)};k\right).
\]

Pour (p=0), on utilise la convention (\widetilde H^{-1}(\varnothing;k)=k). Pour éviter tout décalage silencieux, le certificat R63 doit tester au moins un cas de contrôle ((\mathbb P^1,\mathcal O(-2)) ou (\mathbb P^n,\mathcal O(-n-1))).

Sources primaires précises :

- D. Eisenbud, M. Mustaţă, M. Stillman (**EMS**), *Cohomology on Toric Varieties and Local Cohomology with Monomial Supports*, Theorem 2.7, J. Symbolic Comput. **29** (2000), 583–600, [arXiv:math/0001159](https://arxiv.org/abs/math/0001159). Leur forme exacte est
  (H^p_*(\mathcal O_X)_{\mathbf q}\simeq H^p_{Y_I}(|\Sigma|)), (I=\operatorname{neg}(\mathbf q)), donc une cohomologie réduite du complément/nerf.
- S.-Y. Jow, *Cohomology of toric line bundles via simplicial Alexander duality*, Proposition 3.1 et preuve du Théorème 1.1, [arXiv:1006.0780](https://arxiv.org/abs/1006.0780). Les lignes finales de la dualité identifient précisément le morceau gradué à (\widetilde H^{p-1}(P_{\le I})).
- L. Borisov, Z. Hua, *On the conjecture of King for smooth toric Deligne–Mumford stacks*, Proposition 4.1 et Proposition 4.3, Adv. Math. **221** (2009), 277–301, [arXiv:0801.2812](https://arxiv.org/abs/0801.2812), [doi:10.1016/j.aim.2008.11.017](https://doi.org/10.1016/j.aim.2008.11.017). Ils donnent la version Cox par les présentations intégrales du fibré et les complexes `Supp(r)`, ainsi que le critère des ensembles interdits.

On a toujours la décomposition en caractères

\[
H^p(A,\mathcal O_A(D))=\bigoplus_{m\in M}H^p(A,\mathcal O_A(D))_m.
\]

**Point de rigueur important.** Scanner (m) dans une boîte arbitraire ne prouve pas une annulation. Une preuve finie doit soit :

1. énumérer les patrons de signes réalisables (I_D(m)), calculer leur homologie réduite et résoudre exactement les systèmes d'inégalités entières correspondants; soit
2. utiliser les ensembles/cônes interdits de Borisov–Hua; soit
3. établir une borne polyédrique exacte couvrant tous les (m) contributeurs.

Pour un ambiant torique complet, le faisceau structural ne nécessite aucun scan : (D=0) est nef et le théorème d'annulation de Demazure donne

\[
H^i(A,\mathcal O_A)=0\qquad(i>0).
\]

Sources primaires : M. Demazure, *Sous-groupes algébriques de rang maximum du groupe de Cremona*, Ann. Sci. ÉNS **3** (1970), 507–588, [doi:10.24033/asens.1201](https://doi.org/10.24033/asens.1201); M. Mustaţă, *Vanishing Theorems on Toric Varieties*, Tohoku Math. J. **54** (2002), 451–470, [arXiv:math/0001142](https://arxiv.org/abs/math/0001142), [doi:10.2748/tmj/1113247605](https://doi.org/10.2748/tmj/1113247605).

Pour chaque composante (Y_i\subset A_i), la suite à calculer est

\[
0\longrightarrow\mathcal O_{A_i}(-Y_i)
\longrightarrow\mathcal O_{A_i}
\longrightarrow\mathcal O_{Y_i}\longrightarrow0.
\]

Comme les groupes supérieurs de (\mathcal O_{A_i}) s'annulent, le problème se réduit aux groupes de (\mathcal O_{A_i}(-Y_i)), avec les décalages exacts de la suite longue. Le dossier de dépôt doit inclure : fan complet de chaque (A_i), coefficients du diviseur (-Y_i), patrons (I(m)), Betti réduits, preuve de complétude de l'énumération et un contrôle indépendant (Macaulay2/Sage/Singular si possible).

## 3. Antériorités directes

| Élément R62–R63 | Antériorité primaire | Verdict prudent |
|---|---|---|
| hypersurface CY3 semistable issue d'un top 5D régulier | Davis et al., Théorème 2.2 et Corollaire 2.4 | méthode des *short tops* standard; l'éventail exact peut rester nouveau |
| bloc torique construit à partir d'un *projecting top* | Braun, §2.2 | notion et méthode standard; elles ne portent pas la nouveauté de `POLY944` |
| K3 double de (\mathbb P^1\times\mathbb P^1), branche ((4,4)), polarisation (U(2)) | Laza–O'Grady; Garbagnati–Salgado, Prop. 3.6 | modèle et dimension 18 standards |
| type (II_b) et rang actif (2+b) | Grimm–Rühle–van de Heisteeg; Hassfeld et al. | (b=18) est attendu pour une polarisation générique de rang 2 |
| tours D3 dans le parent (\mathcal N=2) près d'une Tyurin | Hassfeld et al. | mécanisme général déjà publié; il faut calculer le modèle précis |
| orientifold O3/O7 : D3 sur 3-cycles non BPS/instables en général | Enríquez Rojo–Plauschinn | difficulté physique non nouvelle |
| Type II avec composantes préservées/échangées sous orientifold | Kaufmann et al., parties I–II, types O-B/O-A | taxonomie et obstructions quantiques déjà publiées en 2026 |
| involution symplectique K3 : réseau anti-invariant (E_8(-2)) | van Geemen–Sarti | ingrédient de réseau standard |
| obstruction **intégrale** du tube actif isotrope dans le modèle `POLY944` résolu | aucun résultat identique trouvé | candidat original, à isoler comme théorème conditionnel |

Références primaires de ce tableau :

- R. Davis, C. Doran, A. Gewiss, A. Novoseltsev, D. Skjorshammer, A. Syryczuk, U. Whitcher, *Short Tops and Semistable Degenerations*, Experiment. Math. **23** (2014), 351–362, [arXiv:1307.6514](https://arxiv.org/abs/1307.6514), [doi:10.1080/10586458.2014.910848](https://doi.org/10.1080/10586458.2014.910848). Leur définition de « semistable » est exactement : espace total non singulier et fibre centrale réduite à composantes lisses se croisant normalement.
- A. P. Braun, *Tops as Building Blocks for (G_2) Manifolds*, §2.2 (« Ad hoc construction, projecting tops and elementary properties »), JHEP **10** (2017) 083, [arXiv:1602.03521](https://arxiv.org/abs/1602.03521), [doi:10.1007/JHEP10(2017)083](https://doi.org/10.1007/JHEP10(2017)083). Un *projecting top* est un top dont la projection sur l'hyperplan du polytope réflexif de bord reste contenue dans ce polytope. C'est une condition combinatoire suffisante de la construction de blocs, non une signature propre à DDF.
- R. Laza, K. O'Grady, *GIT versus Baily–Borel compactification for K3's which are double covers of (\mathbb P^1\times\mathbb P^1)*, Adv. Math. **383** (2021), 107680, [arXiv:1801.04845](https://arxiv.org/abs/1801.04845).
- A. Garbagnati, C. Salgado, *Rank jumps and Multisections of elliptic fibrations on K3 surfaces*, Forum Math. Sigma **14** (2026), e1, Proposition 3.6, [arXiv:2505.15159](https://arxiv.org/abs/2505.15159), [doi:10.1017/fms.2025.10149](https://doi.org/10.1017/fms.2025.10149). La famille générique (U(2))-polarisée est précisément la famille 18-dimensionnelle de doubles couvertures branchées en ((4,4)).
- T. W. Grimm, F. Rühle, D. van de Heisteeg, *Classifying Calabi–Yau threefolds using infinite distance limits*, Commun. Math. Phys. **382** (2021), 239–275, [arXiv:1910.02963](https://arxiv.org/abs/1910.02963), [doi:10.1007/s00220-021-03972-9](https://doi.org/10.1007/s00220-021-03972-9).
- B. Hassfeld, J. Monnee, T. Weigand, M. Wiesner, *Emergent Strings in Type IIB Calabi–Yau Compactifications*, JHEP **01** (2026) 140, [arXiv:2504.01066](https://arxiv.org/abs/2504.01066), [doi:10.1007/JHEP01(2026)140](https://doi.org/10.1007/JHEP01(2026)140). Ils traitent les Tyurin (II_b), (0\le b\le19), le réseau transverse de rang (2+b) et les tubes spéciaux lagrangiens/D3.
- M. Enríquez Rojo, E. Plauschinn, *Swampland conjectures for type IIB orientifolds with closed-string U(1)s*, JHEP **07** (2020) 026, [arXiv:2002.04050](https://arxiv.org/abs/2002.04050). Ils montrent que, dans leur cadre O3/O7, les D3 sur 3-cycles ne préservent pas la même supersymétrie que les plans; les cycles impairs donnent des états massifs non chargés et les pairs des états chargés de volume nul, avec difficulté de stabilité des tours.
- B. van Geemen, A. Sarti, *Nikulin involutions on K3 surfaces*, Math. Z. **255** (2007), 731–753, [arXiv:math/0602015](https://arxiv.org/abs/math/0602015). Pour une involution symplectique non triviale, l'orthogonal du réseau invariant dans (H^2(S,\mathbb Z)) est (E_8(-2)).
- L. Kaufmann, J. Monnee, T. Weigand, M. Wiesner, *Quantum obstructions for (\mathcal N=1) infinite distance limits — Part I: (g_s) obstructions*, Phys. Rev. D **113** (2026) 126027, [arXiv:2603.12315](https://arxiv.org/abs/2603.12315); et *Part II: Kähler obstructions*, Phys. Rev. D **113** (2026) 126028, [arXiv:2603.13470](https://arxiv.org/abs/2603.13470). La partie I distingue déjà les actions O-type A (composantes échangées, graphe réduit) et O-type B (composantes préservées), y compris pour une limite de type II; la partie II traite explicitement une action anti-symplectique sur la K3.

**Portée exacte des sources LMHS.** Grimm–Rühle–van de Heisteeg et Hassfeld et al. étayent l'étiquette rationnelle/réelle (II_b), le rang transverse (2+b) et le mécanisme tubulaire. Ils ne fournissent pas, dans la généralité revendiquée ici, un théorème intégral identifiant automatiquement
\[
N:\operatorname{Gr}^{W}_{4}\longrightarrow\operatorname{Gr}^{W}_{2}
\quad\text{à}\quad
T(S)\longrightarrow\Lambda_{K3}/L
\]
avec saturation, noyau/cokernel et torsion contrôlés. Aucune source primaire exacte pour cet énoncé intégral complet n'a été trouvée. Par conséquent, l'étiquette (II_{18}) peut être motivée par la littérature, mais le Smith normal form, la primitivité et le discriminant ((\mathbb Z/2)^2) doivent être démontrés directement pour le modèle; ils ne peuvent pas être importés d'un énoncé LMHS rationnel.

Deux autres signaux de densité du domaine :

- C. Doran, B. Pioline, T. Schimannek, *Enumerative geometry and modularity in two-modulus K3-fibered Calabi–Yau threefolds*, Adv. Theor. Math. Phys. **30** (2026), 729–869, [arXiv:2408.02994](https://arxiv.org/abs/2408.02994), [doi:10.4310/ATMP.260522000535](https://doi.org/10.4310/ATMP.260522000535) : 39 paires miroir avec dégénérescences de Tyurin explicites et invariants énumératifs/modulaires.
- A. P. Braun, M. Cicoli, R. Milioli, R. Valandro, *Moduli Stabilisation for ADD and the Dark Dimension Scenario*, [arXiv:2606.19440](https://arxiv.org/abs/2606.19440) : modèle IIB/LVS, limite de Tyurin et interprétation en dimension longue de taille micrométrique. Leur hiérarchie de flux de structure complexe reste en partie programmatique, mais l'idée « Tyurin + dimension sombre » n'est plus une revendication d'originalité possible.

## 4. Formulation susceptible de devenir un vrai résultat

Le scan des 512 signes est utile comme certificat du modèle, mais le cœur publiable devrait être extrait en deux propositions indépendantes du nombre 512.

### Proposition A — composantes préservées

Soit (S) une K3 projective munie d'une involution holomorphe non symplectique (\sigma). Supposons qu'une polarisation prolongeable (L\subset H^2(S,\mathbb Z)^\sigma) contienne une classe ample. Par le théorème de l'indice de Hodge, le réseau invariant a signature ((1,r-1)); son sous-réseau

\[
A_+=(L^\perp\cap H^2(S,\mathbb Z)^\sigma)
\]

est donc négatif défini. Il ne contient aucun vecteur isotrope non nul.

### Proposition B — composantes échangées

Si la contrainte O3/O7 rend l'action induite sur (S) symplectique et si le tube pair demande une classe anti-invariante, alors ce secteur vaut (E_8(-2)) pour une involution de Nikulin non triviale (et zéro pour l'identité). Il est négatif défini et sans isotrope non nul.

### Corollaire à annoncer avec ses hypothèses

Sous les six hypothèses déjà isolées par R62 — involution holomorphe O3/O7, compatibilité avec le lissage, préservation de (L), cycle fermé propre, classe tubulaire isotrope dans (L^\perp), état propre de parité et vecteur fermé issu de (C_4/H^3_+) — le mécanisme du tube actif ne fournit pas la tour fermée recherchée.

**Limite indispensable :** les 512 relèvements ne sont exhaustifs que parmi les caractères diagonaux de signes de l'ansatz Cox et de la sous-famille déclarée. Ils ne classifient ni toutes les automorphismes de la K3, ni toutes les involutions du CY résolu, ni les secteurs ouverts/relatifs/non géométriques.

## 5. Verdict d'originalité et formulations à éviter

### Originalité plausible, sous réserve de vérification

- première construction publiée de **ce** modèle relatif résolu issu de `POLY944`, avec données complètes et reproductibles;
- calcul intégral de l'image primitive (U(2)), de son discriminant ((\mathbb Z/2)^2), et raccord explicite au bloc actif;
- classification des involutions diagonales de Cox de l'ansatz précis;
- théorème conditionnel de non-existence d'une classe isotrope active ayant la parité (C_4) requise;
- éventuelle fermeture de « Tyurin strict » par un certificat complet de cohomologie torique.

### Non-original ou insuffisant seul

- « nous construisons une dégénérescence torique de Tyurin »;
- « la couture est une K3 (U(2)) double de (\mathbb P^1\times\mathbb P^1) branchée en ((4,4)) »;
- « la limite est (II_{18}) » sans matrice de monodromie/saturation;
- « une limite de Tyurin engendre une tour D3/BPS » sans invariants/stabilité dans le modèle;
- « l'orientifold obstrue la limite » sans distinguer l'obstruction de parité R62 des obstructions quantiques A/B déjà étudiées en 2026;
- « (R\) est micrométrique » tant qu'aucune métrique Ricci-plate, aucun spectre KK et aucune relation (R(t)) ne sont calculés.

### Formulations recommandées

> *We construct an explicit resolved toric semistable degeneration associated with the chosen POLY944 phase. After an exact toric-cohomology calculation, its two components satisfy the stated quasi-Fano convention, so the degeneration is Tyurin in that convention.*

et, séparément,

> *Within the stated Cox-diagonal O3/O7 ansatz, an invariant-lattice signature argument excludes any non-zero isotropic active class of the parity required by the closed (C_4) tube mechanism.*

Ne pas fusionner ces deux résultats avec une affirmation de tour physique, de stabilisation ou de rayon micrométrique.

## 6. Limites de la recherche d'antériorité

Les recherches ont croisé les expressions `POLY944`, `(5,85) Tyurin`, `U(2) Tyurin O3/O7`, `C4 isotropic tube`, les titres et les bibliographies des sources ci-dessus. Aucun article indexé ne reproduit l'énoncé intégral précis de R62. Les identifiants `POLYxxx` étant propres à certaines bases/scripts et mal indexés, l'absence de résultat ne prouve pas la nouveauté. Avant dépôt, il faut encore :

**Résultat de la recherche exacte `POLY944` / `sigma5`.** Aucun article indexé n'a été trouvé sous `POLY944`, `POLY 944`, `POLY944 Tyurin`, `POLY944 sigma5` ou l'association `(5,85) Tyurin degeneration`. Sous ces libellés, l'exemple **semble donc non publié**, mais ce constat ne constitue pas une preuve de nouveauté : `sigma5` ressemble à un nom de cône/phase local au calcul et `POLY944` peut changer d'identifiant d'une base à l'autre. La comparaison par sommets, matrice de poids, triangulation/SR-idéal et nombres de Hodge est indispensable avant d'écrire « first example ».

1. comparer les coordonnées/réseaux de `POLY944` aux bases Kreuzer–Skarke et orientifold publiques, pas seulement le nom local;
2. rechercher par matrice de poids, Hodge ((5,85)), sommets du polytope et involution;
3. envoyer un préprint privé à un spécialiste des dégénérescences toriques/K3 et à un spécialiste des orientifolds;
4. présenter l'originalité comme « à notre connaissance » jusqu'à retour de pairs.

**Verdict final :** le noyau possède une voie de récupération crédible, mais son originalité ne réside ni dans (U(2)), ni dans (II_{18}), ni dans l'idée générale de Tyurin. Elle réside, si les certificats résistent à une vérification indépendante, dans la combinaison **modèle torique résolu précis + intégralité + classification équivariante bornée + obstruction de signature clairement hypothésée**.

