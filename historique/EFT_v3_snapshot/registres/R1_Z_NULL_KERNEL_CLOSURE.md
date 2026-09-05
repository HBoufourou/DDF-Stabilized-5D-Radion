# R1 — Fermeture du noyau nul (Z-light) : T1 sur la branche générique
Date : 03/09/2026. Calculs : sympy, log complet dans R1_04A_log.txt. Aucune valeur propre numérique.

## 0. Point de départ imposé par la rétraction

La rétraction (R1_T1_RETRACTION.md) a établi que le principe variationnel du **secteur scalaire seul** perd la composante ∂_μ∂_ν de la jonction d'Israel à p² = 0 (det des conditions = 3p⁴). La reconstruction devait donc se faire **sans séparation scalaire/TT** et **sans 1/p²**.

**Observation qui rend la reconstruction propre** : à p² = 0, les seules structures tensorielles disponibles sont η_μν et ∂_μ∂_νq, et **∂_μ∂_νq est déjà la polarisation TT-nulle**. Il n'y a donc pas un secteur scalaire à recoller à un secteur TT : il y a **une paramétrisation unique à cinq fonctions**, qui contient les deux par construction.

**Paramétrisation nulle** (p^μ ≠ 0, p² = 0, q = e^{ip·x}) :
g_μν = e^{2A}[(1 + 2Fq)η_μν + 2Ê ∂_μ∂_νq], g_μ5 = ∂_μ(Bq), g_55 = 1 + 2Gq, σ = σ₀ + s q.
(Le champ Ê absorbe l'ancien E scalaire et l'ancien ψ TT : Ê = E + ψ/2.)

## 1. Système de bulk complet [Derived]

Équations d'Einstein 5D + équation scalaire à O(ε), fond vérifié à l'ordre 0 :

- **[m5] : 3M₅³(F′ − A′G) + σ₀′s = 0 — c'est exactement C1**, ici *dérivée de l'équation (μ5) du bulk*, sans aucun argument ADM ni contrainte first-class.
- **[trace], [55], [scal]** : ne contiennent ni B ni Ê ⇒ le sous-secteur (F, G, s) **se ferme sur lui-même**.
- **[dd]** (composante ∂_μ∂_ν) : seule équation portant B et Ê ; en variable χ̂ := B − e^{2A}Ê′ elle devient
  **χ̂′ + 2A′χ̂ = 2F + G**.

## 2. Jauge [Derived]

δF = A′ζ, δG = ζ′, δs = σ₀′ζ, δÊ = λe^{−2A}, δB = −2A′λ + ζ + λ′.
⇒ **χ̂ est invariant sous λ**, et δχ̂ = ζ. Le paramètre λ n'est qu'une reparamétrisation de (Ê, B) : la paire (c du secteur scalaire, u₂ du mode TT) n'est **pas** deux données indépendantes — seule la combinaison présente dans χ̂ l'est. Jauge admissible (branes fixes) : ζ(0) = ζ(L) = 0.

## 3. Contenu invariant : un seul paramètre [Derived]

Avec Q₀ = A′s − σ₀′F (invariant de jauge), la combinaison **σ₀′²(Q₀/σ₀′)′** est une combinaison explicite des équations de bulk (coefficients au log) ⇒ **(Q₀/σ₀′)′ = 0 ⇒ Q₀ = c₁σ₀′**.

**Solution générale du système complet** :
F = A′ζ − c₁, G = ζ′, s = σ₀′ζ, **χ̂ = ζ − (2c₁I + C)e^{−2A}**, I(y) = ∫₀^y e^{2A}.
Paramètres physiques : **c₁** (invariant Q₀) et **C** (constante d'intégration de χ̂). ζ(y) : jauge.

## 4. Jonctions complètes à chaque brane [Derived]

| Composante | Condition | Sur la solution générale |
|---|---|---|
| trace (η_μν) | Π_f = 0 ⟺ 3M₅³p²χ + 4e^{2A}C1 = 0 | à p² = 0 : **automatique** (C1 = 0 est une équation de bulk) |
| **∂_μ∂_ν** | **K̊\|_{∂∂} = −s_i χ̂ = 0 ⟺ χ̂(y_i) = 0** | **la condition perdue par la projection scalaire** |
| scalaire | Π_s = 0 ⟺ s′ = σ₀′G | ⟺ **σ₀″(y_i)·ζ(y_i) = 0** |

Le stress de brane S_μν = −[T_i + J_iσ]γ_μν est isotrope : sa partie sans trace est nulle, d'où χ̂(y_i) = 0 **à chaque brane** (deux conditions, pas une condition de raccord).

## 5. Résolution — branche générique σ₀″(0)σ₀″(L) ≠ 0

1. Π_s ⇒ **ζ(0) = ζ(L) = 0**.
2. χ̂(0) = 0 avec I(0) = 0 ⇒ **C = 0**.
3. χ̂(L) = 0 avec C = 0 ⇒ c₁I_L = 0, I_L > 0 ⇒ **c₁ = 0**.

**Il ne reste que ζ(y) avec ζ(y_i) = 0 : une transformation de jauge admissible.**

## 6. Verdict

**L'espace des solutions physiques du secteur Z-light est trivial sur la branche générique.**
- **Aucun mode scalaire massless propagatif physique** (p² = 0, p^μ ≠ 0).
- La forme présymplectique sur ce noyau est identiquement nulle : il n'y a aucune direction, donc **aucune norme négative possible**. La question « X₁ est-il un ghost ? » est vide : X₁ n'est pas une solution physique.
- **T1 = GREEN sur la branche générique, secteur propagatif** : p² ≠ 0 sain (norme ‖X‖_K > 0, auto-adjonction par sous-espace maximal isotrope, ghost absent — inchangé) ; p² = 0 vide.

**Résultat plus fort que la correction externe R12**, qui laissait survivre une direction c avec u₂ = −2c : la paramétrisation unifiée montre que c et u₂ ne sont pas indépendants (λ est une redondance) et que la constante physique unique C est annulée par la jonction en y = 0.

**Cross-check physique** (lecture, pas justification) : un modèle à deux branes avec stabilisateur ne doit précisément **pas** avoir de scalaire massless — le radion est massif. Le secteur nul vide est ce que la stabilisation est censée produire.

## 7. Domaine et réserves déclarées

- **Domaine du verdict** : p² = 0, p^μ ≠ 0 ; σ₀″(0)σ₀″(L) ≠ 0 ; branche active (Λ₅ > 0, μ_σ² ≥ 0) ; modèle minimal, branes fixes, jauge admissible ζ(y_i) = 0.
- **[Open] σ₀″(y_i) = 0** : ζ(y_i) n'est plus forcé à zéro par Π_s ; le rang du problème de bord change ; à reconstruire séparément, jamais par limite du générique.
- **[Open] Z-static (p^μ = 0)** : non couvert (les facteurs ω, |k⃗| disparaissent). C'est là que vit la question du modulus/radion.
- **[Open] T2 (stabilité tachyonique)** : question distincte de T1 — un tachyon est une instabilité de masse à cinétique positive. Le dossier externe (R14) annonce un critère selon le signe de σ₀″(0)σ₀″(L) : **non vérifié ici**.
- Statuts p² ≠ 0 inchangés et toujours [Derived] dans leurs domaines.
