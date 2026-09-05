# Voie I — le radion spectral sur le fond backreacté : **8,2 μm revient**
Date : 05/09/2026. Statut : **exploratoire, NOUVEAU MODÈLE (R9)** — branche « stabilisation forte », hors constitution v1. Aucun certificat ; numérique déclaré.

## 1. Méthode
- Fond couplé résolu exactement (BVP) : A″ = −σ′²/3M₅³, σ″ = μ²σ − 4A′σ′, sources de brane linéaires σ′(0) = σ′(L) = q, fond Z₂-symétrique (σ(L/2) = 0, A′(L/2) = 0), x = m_σL = 2, unités L = 1, M₅³ = 1.
- Équation master certifiée : Q₀″ + (4A′ − 2A″/A′)Q₀′ + [m²e^{−2A} − V_Q]Q₀ = 0, V_Q = μ² + 4A″ + 2μ²σ₀σ₀′/(3M₅³A′). Contrôle : Q₀ = σ₀′ l'annule à 10⁻¹⁶ (m² = 0).
- Condition de bord à paramètre spectral certifiée : (m² + ν_i)Q₀′ = ν_iW_iQ₀ aux branes, ν_i = e^{2A}σ₀′σ₀″/(3M₅³A′)|_{y_i}, W = σ₀″/σ₀′ (forme polynomiale en m², sans pôle).
- Point singulier régulier y = L/2 (A′ = 0 ; indices {0, 3}, sans log) : **tir bilatéral** depuis les deux branes (amorti des deux côtés) et raccord par le **déterminant de Frobenius** avec la série exacte à l'ordre u⁹ (coefficients par différentiation symbolique des équations de fond, symétrie exacte forcée : A^{(impair)}(L/2) = 0, σ^{(pair)}(L/2) = 0), pont à d = 0,02.
- Racines de F(m²) par balayage + brentq ; m_KK := π/L.

## 2. Contrôles du pipeline
| Contrôle | Résultat |
|---|---|
| Zéro-mode spurieux du master seul (exclu physiquement par T1) | F(10⁻⁹) = 10⁻¹⁰…10⁻¹¹ ✓ |
| Accord avec la formule moduli-space à petit βL | +0,3 % (0,05), +1,0 % (0,10), +2,1 % (0,143) — ordre de la correction certifiée A7 ✓ |
| Deux tentatives précédentes rejetées par ce même contrôle | pont RK4 (amplification (0,5/d)²), série tronquée à u² (c₃ fictif antisymétrique) — trace conservée |

## 3. Résultats
| βL | m₁L (spectral) | m₁/m_KK | moduli | écart | m₂L | m₃L | λ_r à R* = 8,2 μm | radion vs ancre (Lee 38,6 μm) |
|---|---|---|---|---|---|---|---|---|
| 0,050 | 0,0800 | 0,026 | 0,0798 | +0,3 % | 2,01 | 3,73 | 322 μm | ROUGE |
| 0,100 | 0,1602 | 0,051 | 0,1586 | +1,0 % | 2,03 | 3,75 | 161 μm | ROUGE |
| 0,143 (plafond v1) | 0,2294 | 0,073 | 0,2248 | +2,1 % | 2,06 | 3,78 | 112 μm | ROUGE |
| 0,300 | 0,4837 | 0,154 | 0,4469 | +8,2 % | 2,25 | 3,95 | 53 μm | ORANGE |
| **0,530** | **0,8501** | **0,271** | 0,7040 | +20,8 % | 2,65 | 4,33 | **30,3 μm** | **VERT** |
| 0,700 | 1,1045 | 0,352 | 0,8464 | +30,5 % | 2,99 | 4,66 | 23,3 μm | VERT |
| 0,900 | 1,3785 | 0,439 | 0,9754 | +41,3 % | 3,41 | 5,07 | 18,7 μm | VERT |

**Le radion spectral est plus lourd que l'estimation moduli-space à stabilisation forte** (+21 à +41 %) — dans le sens favorable. Le seuil VERT à l'ancre (λ_r ≤ 38,6 μm) est franchi vers **βL ≈ 0,40**.

## 4. Ce qui est établi et ce qui reste
- **[Derived, numérique déclaré]** : dans la classe auditée (bulk + 2 branes + stabilisateur GW, potentiels de brane linéaires), un fond à βL ≳ 0,4 **existe**, satisfait la condition de carte (σ₀′ > 0) et **le critère T2 exact avec marge croissante**, a une backreaction de 3–11 %, et porte un radion de portée **λ_r ≈ 19–38 μm à R* = 8,2 μm**, où α_r = 1/3 passe l'ancre expérimentale.
- **Portes restantes** : (i) **EFT** — σ₀/M₅^{3/2} ≈ √12·βL/x ≈ 0,7–1,6 à βL = 0,4–0,9 : régime de backreaction exacte, à argumenter à la DeWolfe–Freedman–Gubser–Karch (porte, pas kill) ; (ii) **digitisation officielle** des courbes α95 pour le verdict phénoménologique (l'ancre seule ne suffit pas à publier) ; (iii) la tour KK à R = 8,2 μm : (8/3)e^{−38,6/8,2} ≈ 0,024 à l'ancre — passe ; (iv) c_α à stabilisation forte : la correction −0,634(βL)² devient O(10 %), à recalculer sur le fond (l'ancre α_r = 1/3 tient).
- **Ce que ce n'est pas** : ni une prédiction de 8,2 μm (R reste hérité de Λ, cité), ni un certificat de la constitution v1 (c'en est une extension déclarée).

## 5. Conséquence pour v3
Le micron n'est plus une idée dont la version perturbative est réfutée et la version forte non calculée : **la version forte est calculée, et elle vit.** La constitution v3 s'ouvre sur la branche « stabilisation forte » avec, pour juges déjà en place : T1, T2 (exact, indépendant de βL), la carte du radion, et — à l'arrivée des productions — LHCb sur le couplage de brane.
