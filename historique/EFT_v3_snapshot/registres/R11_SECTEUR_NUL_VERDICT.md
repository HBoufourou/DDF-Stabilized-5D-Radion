# R11 — Secteur nul : lecture intégrale de hep-ph/0506305. **Verdict : rétrogradation.**
Date : 03/09/2026. Lecture complète de Carena, Lykken & Park, « The Interval Approach to Braneworld Gravity », hep-ph/0506305.

## 1. Ce que fait cet article — et c'est beaucoup

C'est **notre méthodologie**, publiée en 2005 :
- approche par **intervalle** avec un **principe d'action** (pas de projection Z₂, pas de jonctions imposées à la main) ;
- terme de Gibbons–Hawking, et **équations « brane-boundary » obtenues par variation** avec des fluctuations métriques qui **ne s'annulent pas** au bord — c'est exactement le point de départ de notre programme (leur éq. 5.24 est la variation complète) ;
- traitement **séparé de p² = 0**, avec la décomposition tensorielle **dégénérée** (leur Annexe, éq. 9) contenant explicitement le terme **−p_μp_ν φ̄₁**, qui est traceless-transverse à p² = 0 ;
- « straight gauges », et le résultat central : **aucun mode de brane-bending physique** ; le secteur massless = graviton + radion.

## 2. Le point décisif pour nous

**Ils imposent l'équation de bord comme équation TENSORIELLE, puis la décomposent** — jamais comme projection sur des variations scalaires. Conséquence directe : dans le cas plat, leur éq. (3.53) 0 = [t̄′_μν − p_μp_ν φ̄₁′] se scinde en (3.54) [t̄′_μν] = 0 **et (3.55) [φ̄₁′] = 0** ; en RS, (4.43) et **(4.44) [e^{−2ky}φ̄₁′] = 0**.

> **La composante ∂_μ∂_ν de la condition de bord à p² = 0 est retenue et imposée séparément dans la littérature depuis 2005.**

⇒ Notre « patron d'erreur N°5 » n'est pas une découverte sur la physique : c'est **une erreur que nous avons commise et que la méthodologie publiée évite par construction**. Elle garde sa valeur comme leçon de méthode dans notre registre interne, pas comme contribution.

## 3. Ce que cet article ne fait PAS

**Aucun scalaire de bulk.** Leurs modèles sont : gravité + tensions de brane + termes cinétiques de brane, sur fonds plat, RS, et AdS₅/AdS₄ général. Donc :
- pas de stabilisateur, pas de σ, pas de σ₀″/σ₀′ ;
- **leur radion est massless et physique** — précisément parce que rien ne le stabilise ;
- la structure que nous avons trouvée (χ̂ = B − e^{2A}Ê′, jonction ∂∂ ⇒ χ̂(y_i) = 0 aux deux branes, jonction scalaire ⇒ σ₀″(y_i)ζ(y_i) = 0, d'où le noyau nul vide) n'y figure pas, faute de stabilisateur.

## 4. Mais notre résultat T1 est quand même établi — par ailleurs

« Aucun mode massless sur la branche générique σ₀″(y_i) ≠ 0 » est **exactement** la condition de zéro-mode de Lesgourgues–Sorbo (zéro-mode ⟺ g₊ = 0, g₋ = 0, φ₀′(y₋) = 0 ou φ₀′(y₊) = 0, c'est-à-dire σ₀″(y_i) = 0 ou σ₀′(y_i) = 0).

⇒ **Notre T1 est une re-dérivation, par le secteur nul, d'un résultat [Established].** Cohérence de trois méthodes indépendantes — c'est un contrôle de qualité, pas une contribution.

## 5. Conséquence : Paper A rétréci une seconde fois

Ne subsistent comme contributions :

1. **L'identité d'énergie régulière** : m²‖X‖_K² = ½∫₀^L e^{4A}𝒢²dy + Σ_i s_i(e^{4A}σ₀″/2σ₀′)|_{y_i}s(y_i)², avec 𝒢 = (s′ + 2σ₀′f) − σ₀″s/σ₀′. Constructive, à positivité manifeste, autovalidée par la condition de bord naturelle, sans aucun A′ ni 1/p². **Méthode alternative, pas résultat nouveau** — et son précédent tensoriel direct est Mukohyama–Kofman (hep-th/0112115).
2. **L'extension au warp non monotone** — la seule contribution de domaine. Lesgourgues–Sorbo supposent a(y) monotone et écrivent explicitement que le cas U₊ = U₋ (warp non monotone) échappe à leur analyse ; Carena–Lykken–Park n'ont pas de scalaire de bulk. **Le fond DDF Z₂-symétrique tombe exactement dans cet interstice.**

**Titre honnête de Paper A** : *« Une identité d'énergie régulière pour le secteur scalaire des modèles à deux branes stabilisés : preuve alternative du critère de stabilité et extension au warp non monotone. »*
Format : note courte (méthode + extension), avec Lesgourgues–Sorbo récupéré en corollaire dans son domaine, Carena–Lykken–Park cité pour le cadre par intervalle, Mukohyama–Kofman pour le précédent de la méthode. **La section « secteur nul » disparaît comme contribution** et devient un contrôle de cohérence.

## 6. Registre R11 final

| Objet | Statut |
|---|---|
| Cadre par intervalle, action, équations de bord par variation | [Established] Carena–Lykken–Park hep-ph/0506305 |
| Décomposition dégénérée à p² = 0 ; composante ∂∂ de la condition de bord | [Established] idem, éq. (9), (3.53–3.55), (4.43–4.44) |
| Patron d'erreur N°5 | **erreur interne**, valeur pédagogique seulement |
| Absence de mode massless si σ₀″(y_i) ≠ 0 (T1) | [Established] Lesgourgues–Sorbo — notre dérivation = re-dérivation |
| Critère T2 (warp monotone) | [Established] Lesgourgues–Sorbo |
| Identité d'énergie régulière (méthode) | [Derived] ; précédent tensoriel Mukohyama–Kofman |
| **Extension au warp non monotone** | **[Derived] — seule contribution de domaine** |
| α_r = 1/3 | [Established] Adelberger et al. |
| **Carte d'exclusion GW, no-go du micron** (Paper B) | **[Derived, conditionnel digitisation]** |

**Bilan** : deux contributions défendables subsistent — l'extension non monotone (Paper A, note courte) et la carte d'exclusion du radion (Paper B). Tout le reste est cité.
