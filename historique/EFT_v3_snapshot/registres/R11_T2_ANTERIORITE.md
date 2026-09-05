# R11 — Antériorité de classe du critère T2. **La classe est occupée ; notre critère coïncide.**
Date : 03/09/2026. Recherche d'antériorité exécutée avant toute revendication, conformément à R11.

## 1. Référence principale

**J. Lesgourgues & L. Sorbo, « Goldberger-Wise variations: stabilizing brane models with a bulk scalar », hep-th/0310007, Phys. Rev. D 69 (2004) 084010.**

Ils analysent le spectre des perturbations scalaires de modèles à une et deux branes en 4+1 dimensions avec un scalaire de bulk, potentiels de bulk et de brane arbitraires, **sans approximation et sans référence à un potentiel spécifique**. Leur objectif déclaré est exactement le nôtre : fournir des critères disant quand des modes tachyoniques apparaissent.

Leurs quantités de bord :
**g_± ≡ H(y_±) − φ₀″(y_±)/φ₀′(y_±) ∓ ½a(y_±)·d²U_±/dφ²**, H ≡ a′/a en coordonnée conforme.

**Leur théorème (deux branes, a(y) monotone)** : condition **nécessaire et suffisante** de stabilité :
**g₊ < 0, g₋ > 0, et φ₀′(y) ≠ 0 partout.**

**Leur théorème (une brane)** : toujours instable, quels que soient les potentiels.

**Leur condition de zéro-mode** : un mode de masse nulle existe **si et seulement si** g₊ = 0, ou g₋ = 0, ou φ₀′(y₋) = 0, ou φ₀′(y₊) = 0.

## 2. Comparaison avec notre critère — coïncidence exacte [Derived]

Notre constitution impose des **potentiels de brane linéaires** U_i = T_i + J_iσ, donc **d²U/dφ² = 0**. Conversion de leur coordonnée conforme à notre coordonnée propre (a = e^A, ∂_{y_c} = a∂_y) :
H = A′e^A ; φ₀″/φ₀′ = e^A(A′ + σ₀″/σ₀′)
⇒ **g_i = −e^{A}·σ₀″(y_i)/σ₀′(y_i)**.

Leur critère, réécrit de façon covariante par rapport à l'orientation (s₀ = −1, s_L = +1) :
g₋ > 0 et g₊ < 0 ⟺ **s_i·g_i < 0** ⟺ **s_i·σ₀″(y_i)/σ₀′(y_i) > 0**.

> **C'est exactement notre critère T2.** Notre condition de carte σ₀′ ≠ 0 est exactement leur troisième condition φ₀′ ≠ 0.
> Leur remarque « le choix H > 0 donnerait g₊ > 0, g₋ < 0 » est le même énoncé dans l'étiquetage retourné (g est impair sous y → −y, comme s_i) : la forme s_ig_i < 0 est invariante. **Aucune divergence.**

**Cross-check T1** : leur condition de zéro-mode donne « mode massless ⟺ σ₀″(y_i) = 0 ou σ₀′(y_i) = 0 ». Notre T1 a trouvé le secteur massless **vide** sur la branche générique σ₀″(y_i) ≠ 0, et l'a laissé [Open] exactement sur σ₀″(y_i) = 0. **Accord parfait, par deux méthodes indépendantes.**

## 3. Ce qui ne peut plus être revendiqué

- **Le critère T2 lui-même** : [Established, Lesgourgues–Sorbo 2004]. À citer, jamais à revendiquer.
- L'instabilité générique du modèle à **une** brane : [Established, idem].
- La condition d'existence d'un zéro-mode : [Established, idem ; voir aussi Mukohyama–Kofman hep-th/0112115].
- Le critère externe R14 (signe de σ₀″(0)σ₀″(L)) : c'est le critère Lesgourgues–Sorbo pour σ₀ monotone.
- La conjecture « tachyons sauf si σ₀ monotone » : Tanaka–Montes, hep-th/0001092 — démontrée par LS comme la condition φ₀′ ≠ 0.
- Généralisation multibrane : arXiv:2408.15343 (2024), conditions nécessaires et suffisantes pour les radions massless et tachyoniques.

## 4. Ce qui reste défendable — et c'est précis

**(i) Méthode.** Leur preuve est un argument d'espace des phases / tir (comportement de F(m²) entre m² = 0 et m² → −∞). La nôtre est une **identité d'énergie à positivité manifeste** :
**m²‖X‖_K² = ½∫₀^L e^{4A}𝒢²dy + Σ_i s_i(e^{4A}σ₀″/2σ₀′)|_{y_i}s(y_i)²**, 𝒢 = (s′+2σ₀′f) − σ₀″s/σ₀′.
Différente en nature : constructive, locale, avec autovalidation par la condition de bord naturelle.

**(ii) Domaine — le point le plus important.** Leur théorème **suppose a(y) monotone** (H ≠ 0 partout) ; ils écrivent explicitement que le cas U₊ = U₋ rend a(y) non monotone entre les branes et que **leur analyse ne tient pas** dans ce cas.
Or **notre identité ne fait aucune hypothèse sur le warp** : elle est régulière en A′ = 0 (le facteur A′ s'annule dans P̃_Q(𝒟Q₀)² = ½e^{4A}𝒢²). Et **le fond DDF est précisément le cas symétrique** que leur théorème exclut : σ₀ impaire autour de L/2, A′(L/2) = 0.
> **Notre contribution couvre exactement le cas que le théorème publié laisse de côté.**
C'est aussi ce qui explique rétrospectivement pourquoi la condition (C1) « warp à maximum intérieur » était apparue dans la carte I puis s'était révélée être un artefact : c'est la trace de l'hypothèse de monotonie dont notre dérivation régulière s'affranchit.

**(iii) Le secteur nul (T1).** Leur analyse porte sur le spectre massif et l'existence de zéro-modes ; notre traitement du cône nul (p² = 0, p^μ ≠ 0) avec la dégénérescence scalaire/TT, la jonction ∂∂ perdue par projection, et le secteur statique, est d'une autre nature — R11 séparé encore à faire.

## 5. Conséquence sur Paper A

Le plan de Paper A doit être révisé : il ne peut plus être « nous dérivons un critère de stabilité », mais

> **« Une identité d'énergie régulière pour le secteur scalaire des modèles à deux branes stabilisés : preuve alternative du critère de stabilité, extension au warp non monotone, et analyse du cône nul. »**

Structure : (1) l'identité et sa preuve ; (2) récupération du critère de Lesgourgues–Sorbo comme corollaire, dans leur domaine ; (3) l'extension au cas non monotone, avec le fond symétrique comme application ; (4) le secteur nul (T1) ; (5) le patron d'erreur N°5 comme note de méthode.

Plus étroit qu'annoncé — et entièrement défendable.

## 6. R11 restants

- **α_r = 1/3** (couplage du radion) : R11 à exécuter avant Paper B. Références à vérifier en priorité : Csáki–Graesser–Kribs hep-th/0008151 ; Kofman–Martin–Peloso hep-ph/0401189 ; Goldberger–Wise ; la littérature « radion couplings ».
- **T1 / secteur nul** : R11 à exécuter (dégénérescence scalaire–TT sur le cône nul, jonction ∂∂).
