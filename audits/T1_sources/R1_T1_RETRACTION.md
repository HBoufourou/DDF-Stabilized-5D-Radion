# R1 — Rétraction du verdict T1 = RED (03/09/2026)

**Statut courant : T1 = [OPEN — RED rétracté]. Pas GREEN.**
Origine : objection R12 du dossier externe `DDF_v2_FINAL_ANALYSIS_R11_R38_2026-09-03`, **re-dérivée intégralement dans les conventions DDF** avant acceptation (aucune autorité bibliographique n'a servi de juge ; log complet dans R1_04A_log.txt).

## 1. Le défaut, énoncé exactement

Dans le secteur scalaire, la partie (μν) de la jonction d'Israel a la structure générale
**𝒥_μν = α η_μν + β ∂_μ∂_ν**.
Les seules variations disponibles dans le secteur scalaire sont δF (structure η_μν) et δE (structure ∂_μ∂_ν), et elles ne testent 𝒥_μν que par les projections
- δF → η^{μν}𝒥_μν = 4α − βp²
- δE → ∂_μ∂_ν𝒥^{μν} = −p²(α − βp²)

**Déterminant de la matrice des conditions = 3p⁴** [Derived].
- p² ≠ 0 : rang 2 ⇒ α = β = 0, la jonction tensorielle complète est récupérée. Notre traitement était donc correct sur tout le secteur massif.
- **p² = 0 : rang 1. La ligne δE s'annule identiquement. β n'est plus testé.** La condition portée par β disparaît du principe variationnel scalaire — non parce qu'elle est satisfaite, mais parce que la projection l'annihile.

C'est la trace exacte de ce que nos propres momenta certifiés affichaient sans que nous l'ayons lu ainsi :
**Π_e = −(k²/2)e^{4A}·C1** (double divergence ⇒ facteur p²) et
**Π_f = 0 ⟺ 3M₅³p²χ + 4e^{2A}C1 = 0** (le facteur p² devant χ).
Nous avions conclu « à p² = 0, Π_f est automatique donc aucune condition sur χ|∂ ». La conclusion correcte est : « à p² = 0, la projection scalaire ne voit plus la condition sur χ|∂ ».

Raison géométrique : à p² = 0, ∂_μ∂_νq est **simultanément** de forme scalaire et transverse-sans-trace (η^{μν}∂_μ∂_νq = □₄q = 0, ∂^μ∂_μ∂_νq = ∂_ν□₄q = 0). Les secteurs scalaire et TT se recouvrent, et la séparation utilisée partout ailleurs (projecteur P⁽²⁾ ∝ 1/(k²−ω²), singulier exactement en p² = 0) cesse d'être une carte admissible.

## 2. La condition manquante, calculée dans nos conventions

Calcul direct de la courbure extrinsèque depuis la métrique (scalaires F, B, G, E, s + mode TT-nul ψ de structure ∂_μ∂_ν) :
**partie sans trace : K̊|_{∂∂} = −s_i[χ − (e^{2A}/2)ψ′]**, χ = B − e^{2A}E′ [Derived].
Le stress de brane S_μν = −[T_i + J_iσ]γ_μν est isotrope : aucune partie sans trace. La jonction exige donc
**χ_i = (e^{2A_i}/2)ψ′(y_i)** à chaque brane.

Contrôles :
- **Bulk (μν), composante ∂_μ∂_ν, sur la famille Z-light** : 2A′B + B′ + 2c₁ = 0 identiquement ⇒ **X₁ satisfait l'équation de bulk** dans cette composante (notre analyse de bulk était complète). [Derived]
- **Équation du mode TT-nul** : la partie ψ de l'équation de bulk se réduit, par l'idéal du fond, à **ψ″ + 4A′ψ′ = 0 ⇒ ψ′ = u₂e^{−4A}** (mode TT sans masse). [Derived]
- **Oracle p² ≠ 0** : la même condition sans trace redonne χ|∂ = 0, c'est-à-dire notre Π_f = 0 avec C1 = 0. [Derived]

## 3. Conséquence sur X₁

u₂ est un unique coefficient de bulk, commun aux deux branes :
**e^{2A_i}χ_i = u₂/2 aux deux endpoints ⇒ e^{2A_0}χ_0 = e^{2A_L}χ_L.**
Sur la famille Z-light avec la jonction scalaire ζ_eff(y_i) = 0 : e^{2A_i}χ_i = −(c + 2c₁I_i), I_0 = 0 ⇒
**−c = −(c + 2c₁I_L) ⇒ c₁I_L = 0 ⇒ c₁ = 0** (I_L > 0). [Derived]

**X₁ (c₁ = 1, c = 0) viole la jonction d'Israel complète sur le cône nul : il n'appartient pas à l'espace physique des solutions à bord.**
N₁₁ = −3M₅³I_L reste le calcul correct de la forme présymplectique **sur une configuration hors domaine** ; ce n'est pas la norme d'un ghost.

## 4. Statuts (R12 : une seule vérité active, historique conservé)

| Objet | Ancien | Nouveau |
|---|---|---|
| X₁ | physique, hors orbite | **exclu par la jonction TT/∂∂ complète [Derived]** |
| N₁₁ = −3M₅³I_L | norme physique négative | forme calculée hors domaine [Derived] |
| ghost_{Z-light} | present [Derived] | **[RETRACTED]** |
| T1 branche générique | RED | **[OPEN — RED rétracté]** (pas GREEN) |
| secteur p² ≠ 0 | sain | **inchangé** [Derived] — le défaut est strictement confiné au cône nul |
| Z-static p^μ = 0 | autopsie | [Open], à réintégrer |
| σ₀″(y_i) = 0 | [Open] | inchangé |

**Ce qui n'est PAS retiré** : toute la chaîne p² ≠ 0 (master 𝓛_Q, reconstruction equivalence, atlas, auto-adjonction par sous-espace maximal isotrope, ‖X‖_K > 0, ghost_{p²≠0} absent), les deux routes présymplectiques, le corner n₅′, l'ancre TT, GZ5, la complétion edge. Ces résultats restent [Derived] dans leurs domaines.

## 5. R9 non violée

Aucun paramètre ni terme de l'action modifié (U_i, J_i, V_σ, Λ₅, BC inchangés) ; aucun champ ni contre-terme ajouté. La condition manquante était **déjà contenue** dans la variation complète de l'action — la partie sans trace de la jonction d'Israel — et a été perdue par une projection qui dégénère sur le cône nul. C'est une contradiction mathématique interne explicite, seul motif admis de réouverture.

## 6. Patron d'erreur N°5 (registre méthode)

**« Une projection qui dégénère sur une sous-variété du domaine transforme une condition en identité vide. »**
Signature : un facteur p² (ou k², ou tout symbole s'annulant sur la sous-variété étudiée) devant la condition. Contre-mesure obligatoire : avant tout verdict sur une sous-variété, **re-dériver le jeu complet de conditions de bord sur cette sous-variété**, jamais réutiliser celles du secteur générique — exactement ce que nous avions fait pour les contraintes de bulk C1, C2 (re-dérivées à p² = 0 depuis les contraintes first-class), et omis pour les jonctions.

## 7. Suite requise avant tout nouveau verdict

Reconstruction complète du noyau nul, sans projecteur 1/p² :
1. base nulle (p^μ, n^μ, e_1^μ, e_2^μ), décomposition sans 1/p² ;
2. système bulk couplé complet : scalaires (F, G, B, E, s) **et** branche TT-nulle ψ ;
3. jonctions trace, scalaire **et** ∂∂/TT ;
4. forme présymplectique sur le vrai noyau, classification de la direction restante (c, u₂ = −2c) ;
5. vérifier qu'aucune combinaison survivante ne porte une norme négative ;
6. traiter séparément Z-static (p^μ = 0).
Seulement ensuite : T1 = GREEN ou RED sur un domaine explicitement déclaré.
