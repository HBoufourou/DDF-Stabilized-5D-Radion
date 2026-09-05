# R1 — Secteur Z-static (p^μ = 0) : fermeture
Date : 03/09/2026. Calculs sympy, log dans R1_04A_log.txt. Aucune valeur propre numérique.
Prérequis : R1_Z_NULL_KERNEL_CLOSURE.md (Z-light fermé), R1_T1_RETRACTION.md (patron d'erreur N°5).

## 0. Discipline imposée par la sous-branche

À p^μ = 0 les facteurs ω et |k⃗| disparaissent : **C1 n'est pas imposée par le bulk** et ne doit pas être injectée. Le patron N°5 s'applique intégralement — le jeu complet de conditions est re-dérivé sur la sous-variété, jamais transporté depuis le générique.

**Contenu de champ [Derived]** : q = const ⇒ g_μ5 = ∂_μ(Bq) = 0 et 2Ê∂_μ∂_νq = 0. **B et Ê disparaissent** ; il reste (F, G, s). La jauge se réduit à ζ(y) : le paramètre λ disparaît aussi (il n'agissait que sur Ê, B).

## 1. Bulk [Derived]

Trois équations pour (F, G, s) : (μν), (55), scalaire. L'équation (μ5) est identiquement nulle — **C1 n'est effectivement pas une contrainte de bulk**.
Mais le système impose une équation du premier ordre sur C1 := 3M₅³(F′ − A′G) + σ₀′s :
**C1′ + 4A′C1 = −e^{−2A}·[bulk (μν)] − ½·[bulk (55)]** (coefficients au log)
⇒ **(e^{4A}C1)′ = 0 ⇒ C1 = κ e^{−4A}**, une constante κ.

## 2. Jonctions [Derived]

**(μν)** : avec K_μν − Kγ_μν = −(U_i/M₅³)γ_μν et le fond certifié (ordre 0 : −3s_iA′γ_μν, U_i = 3s_iM₅³A′, J_i = −s_iσ₀′ ; résidu d'ordre 0 nul ⇒ normalisation calée), l'ordre 1 vaut **−(s_ie^{2A}/M₅³)·C1** ⇒ **C1|_{y_i} = 0**.
Combiné au bulk : C1(0) = 0 ⇒ κ = 0 ⇒ **C1 ≡ 0 dans tout le bulk statique**, sans aucune division par ω ni □₄.

**Scalaire** (Π_s certifié) : s′ = σ₀′G ⟺ **σ₀″(y_i)·ζ(y_i) = 0**.

**∂∂** : inexistante à p^μ = 0 (aucune structure ∂_μ∂_ν) — la condition qui tuait c₁ dans Z-light n'a pas d'analogue ici.

## 3. Solution générale et résolution [Derived]

Avec C1 ≡ 0, le système {(μν), (55), scalaire} est résolu par
**F = A′ζ − c₁, G = ζ′, s = σ₀′ζ** (les trois équations et C1 s'annulent identiquement ; vérifié).
Branche générique σ₀″(y_i) ≠ 0 ⇒ **ζ(0) = ζ(L) = 0** ; **c₁ n'est pas contraint**.

## 4. Nature du mode survivant

Représentant ζ = 0 : **F = −c₁ (constant en y), G = 0, s = 0**.
C'est exactement le difféomorphisme 4D ξ^μ = c₁x^μ : δg_μν = −(∂_μξ_ν + ∂_νξ_μ) = −2c₁g_μν ⇒ δF = −c₁, δG = δs = 0.
⇒ **le mode c₁ est une dilatation globale des coordonnées 4D** — une transformation large, absente du groupe ζ à p^μ = 0 par construction (ξ^μ ∝ p^μλ dégénère). Il ne modifie ni la géométrie du bulk, ni le profil du scalaire, ni la séparation des branes.

**Pas de zéro-mode radion [Derived]** : la variation de la distance propre entre branes vaut
δL = ∫₀^L G dy = ∫₀^L ζ′ dy = ζ(L) − ζ(0) = **0** pour toute solution admissible.
Aucune solution statique ne déplace les branes l'une par rapport à l'autre.

**Norme** : le courant présymplectique est proportionnel à ω ; à ω = 0 il est identiquement nul. La direction c₁ a donc une norme symplectique nulle : ce n'est pas un degré de liberté propagatif, et **aucune norme négative n'apparaît**.

## 5. Verdict Z-static

**Sur la branche générique (σ₀″(0)σ₀″(L) ≠ 0) :**
- C1 ≡ 0 dans tout le bulk, dérivée sans division par ω ni □₄ ;
- l'espace des solutions modulo jauge admissible est de dimension 1, engendré par la dilatation globale 4D ;
- **aucun zéro-mode radion** : la séparation des branes est rigide au niveau linéaire ;
- **aucune norme négative** ; le secteur statique n'est pas propagatif.

**⇒ T1 est fermé sur la branche générique dans les deux secteurs :**
p² ≠ 0 sain (norme ‖X‖_K > 0, auto-adjonction certifiée) ; p² = 0, p^μ ≠ 0 vide ; p^μ = 0 sans mode physique propagatif ni radion massless.
**T1 = GREEN [branche générique, modèle minimal, branes fixes].**

## 6. Réserves déclarées (inchangées)

- **[Open] σ₀″(y_i) = 0** : ζ(y_i) n'est plus forcé à zéro ; le rang du problème de bord change dans Z-light ET dans Z-static ; à reconstruire séparément, jamais par limite du générique.
- **[Open] T2 — stabilité tachyonique** : question distincte (m² < 0 à cinétique positive). Le fait qu'il n'y ait pas de zéro-mode ne dit rien du signe du spectre massif. Le dossier externe (R14) annonce un critère selon le signe de σ₀″(0)σ₀″(L) — **non vérifié ici**.
- **[Open]** statut des transformations 4D larges (dilatation) : non nécessaire pour T1, la norme étant nulle dans tous les cas.
