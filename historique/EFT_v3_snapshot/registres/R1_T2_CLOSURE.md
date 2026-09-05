# R1 — T2 : FERMETURE. Identité régulière exacte, critère final, verdict GREEN sans réserve.
Date : 03/09/2026. Calculs sympy, log dans R1_04A_log.txt. Aucune valeur propre numérique.
Lève la réserve de R1_T2_CHART_II.md et supersède la condition (C1) de R1_T2_CRITERION.md.

## 1. L'identité, exacte et entièrement régulière [Derived]

Avec **𝒢 := (s′ + 2σ₀′f) − σ₀″s/σ₀′** (aucun A′), sur la surface de contrainte C1 = 0 :

**2·V_bulk = ½e^{4A}𝒢² + d/dy[𝒢_y]**, résidu symbolique **exactement 0**, avec
**𝒢_y = 28M₅³e^{4A}A′f² − (4/3)σ₀′e^{4A}fs + (e^{4A}σ₀″/(2σ₀′))s²**
(dérivée totale calculée **en utilisant C1**, comme il se doit ; contrôle croisé sur un fond explicite exact — Λ₅ = 0, μ_σ² = 0, e^{4A} = 1 − 4βy, σ₀′ = q₀e^{−4A} — résidu 0).

Contrôle préalable de V_bulk : EL_f[V] − (𝔸X)_f = 0 et EL_s[V] − (𝔸X)_s = 0 contre l'opérateur 𝔸 certifié.

## 2. Le terme de bord : toute la dépendance en f s'annule [Derived]

Avec le terme de brane certifié restreint à la contrainte, **GB|img = s_i e^{4A}(14M₅³A′f² − (2/3)σ₀′fs)**, la forme de bord totale vaut

**s_i𝒢_y − 2·GB|img = s_i · (e^{4A}σ₀″/(2σ₀′)) · s(y_i)²**

(les termes en f², fs s'annulent exactement ; le résidu vaut s_i e^{4A}s²(μ_σ²σ₀ − 4A′σ₀′ − σ₀″)/(2σ₀′) ≡ 0 par la relation de fond σ₀″ = μ_σ²σ₀ − 4A′σ₀′).

**Autovalidation** : la condition de bord naturelle de la fonctionnelle obtenue,
e^{4A}𝒢 + 2ε_i s = 0 avec ε_i := e^{4A}σ₀″/(2σ₀′), se réduit à **s′ + 2σ₀′f = 0** — exactement la BC certifiée. La normalisation du terme de brane n'a donc pas été choisie : elle est fixée et vérifiée.

## 3. Identité finale

> **m²·‖X‖_K² = ½∫₀^L e^{4A}𝒢² dy + Σ_i s_i (e^{4A}σ₀″/(2σ₀′))|_{y_i} · s(y_i)²**
> ‖X‖_K² = ∫₀^L e^{2A}(3M₅³f² + ½s²)dy > 0

Aucun A′, aucun 1/p², aucune condition de bord dépendante de m², aucun intermédiaire singulier. Le terme de bulk est manifestement ≥ 0.

## 4. Critère T2 final [Derived]

> **s_i · σ₀″(y_i)/σ₀′(y_i) ≥ 0 aux deux branes ⇒ m² ≥ 0 : T2 GREEN.**
> Avec s₀ = −1, s_L = +1 : **σ₀″(0)/σ₀′(0) ≤ 0 ET σ₀″(L)/σ₀′(L) ≥ 0.**

**(C1) est SUPERSEDED** : la condition « warp à maximum intérieur, A′(0) > 0 > A′(L) » était un **artefact du facteur intégrant singulier** P̃_QW ∝ 1/A′² de la carte I. Le critère régulier **ne dépend pas du warp** — seul le profil du stabilisateur aux branes compte.

**Réconciliation avec le critère externe R14** : si σ₀′ garde un signe constant (σ₀ monotone), le critère devient **σ₀″(0)·σ₀″(L) ≤ 0** — exactement l'énoncé annoncé ailleurs, désormais dérivé et généralisé.

## 5. Application au fond DDF [Derived]

Fond GW symétrique σ₀ = (q/m_σ)sinh[m_σ(y − L/2)]/cosh(x/2) : σ₀″/σ₀′ = m_σ tanh[m_σ(y − L/2)].
- en y = 0 : négatif, et s₀ = −1 ⇒ s₀·(σ₀″/σ₀′)|₀ = +m_σ tanh(x/2) ≥ 0 ✓
- en y = L : positif, et s_L = +1 ⇒ +m_σ tanh(x/2) ≥ 0 ✓

> **CRITÈRE SATISFAIT AUX DEUX BRANES ⇒ m² ≥ 0 ⇒ T2 = GREEN, sans réserve.**

## 6. Bilan des portails

| Portail | Verdict | Domaine |
|---|---|---|
| **T1** (ghost) | **GREEN** | branche générique σ₀″(y_i) ≠ 0, trois secteurs (p² ≠ 0 sain ; p² = 0 vide ; p^μ = 0 sans radion massless) |
| **T2** (tachyon) | **GREEN** | fond GW symétrique ; critère général s_iσ₀″/σ₀′ ≥ 0, régulier et sans condition sur le warp |

**La construction minimale DDF passe les deux portails de stabilité.**

Statuts restants, tous **phénoménologiques et non structurels** : l'échelle (8,2 μm exclu ×258, région vivante nanométrique) ; le mécanisme de matière noire ; la digitisation officielle des courbes α95 ; la sous-branche σ₀″(y_i) = 0 (T2 trivialement GREEN, T1 [Open]) ; le blast radius du signe d'Israel sur le corpus phase 1.
