# R11 — Antériorité : (A) couplage du radion α_r = 1/3 ; (B) secteur nul (T1)
Date : 03/09/2026. Recherche exécutée avant toute revendication.

---

# A. α_r = 1/3 — **[Established]. À citer, jamais à revendiquer.**

## A.1 Le résultat est standard, et utilisé par les expérimentateurs eux-mêmes

Adelberger, Heckel, Hoyle et al., **hep-ph/0611223** (« Particle Physics Implications of a Recent Test of the Gravitational Inverse Square Law ») donnent explicitement, pour l'échange de radion dans n dimensions supplémentaires,

**α = n/(n+2)**, λ ≈ 2,4·(1 TeV/M_*c²)² mm,

et **citent nommément le cas n = 1 : α = 1/3** (avec n = 6 : α = 3/4). Ils soulignent que la force médiée par le radion est souvent l'effet à plus longue portée des dimensions supplémentaires, parce qu'elle ne décroît pas quand leur nombre augmente.

Le résultat Eöt-Wash (« Submillimeter Test of the Gravitational Inverse-Square Law ») contraint directement les **scénarios de dimensions supplémentaires stabilisés par radions** à M_* ≳ 3,0 TeV, indépendamment du nombre de dimensions.

Origine structurelle, également standard : le radion d'une seule dimension supplémentaire est un scalaire de Brans–Dicke avec **ω = 0**, d'où α = 1/(2ω+3) = 1/3 (voir la discussion PPN dans arXiv:0901.4530, qui rappelle qu'une dimension compacte se représente par un dilaton de ω = 0).

## A.2 Ce qui ne peut plus être revendiqué

- α_r = 1/3 pour une dimension supplémentaire : **[Established]**.
- La forme du signal Yukawa V = −(Gm₁m₂/r)(1 + αe^{−r/λ}) : **[Established]**.
- La contrainte torsion-balance sur les scénarios stabilisés par radion : **[Established]**.
- Le α = 8n/3 de la tour KK : **[Established]** (Kehagias–Sfetsos, hep-ph/9905417), déjà sourcé dans CDD Partie II.

**Conséquence directe sur le post-mortem** : la cause C4 (« juges gratuits non convoqués ») est confirmée dans les termes les plus durs — le juge qui a tué le benchmark 8,2 μm n'était pas seulement dans notre bibliothèque, il est dans le résumé même des articles Eöt-Wash.

## A.3 Ce qui reste défendable pour Paper B

**Le problème du radion dans la dimension sombre est connu et déclaré ouvert par les auteurs du scénario eux-mêmes.** Montero–Vafa–Valenzuela (JHEP 02 (2023) 022) écrivent qu'il faut découpler le radion du secteur de matière pour éviter les ennuis avec les contraintes de cinquième force, suggèrent soit de l'alourdir soit de supprimer ses couplages, et qualifient cela de question intéressante à explorer dans le futur.
Une réalisation récente (JHEP 02 (2026) 156, stabilisation Casimir du SM dans la dimension sombre) trouve **le radion trop léger pour survivre aux tests système-solaire**, et invoque des mécanismes d'écrantage (caméléon) comme issue possible. Convergence notable : le `radion.py` de CDD Partie II concluait déjà « Casimir-only stabilisation EXCLUDED ».

**La niche de Paper B est donc précise** : personne n'a produit, pour un fond **stabilisé à la Goldberger–Wise**, une carte d'exclusion quantitative où α_r et λ_r sont **dérivés du fond**, confrontant le signal conjoint
**Δ(r) = α_r e^{−r/λ_r} + (8/3)Σ_n e^{−nr/R}**
aux courbes de balance de torsion. Ce que Paper B revendique n'est pas le couplage, c'est **la carte et son verdict** : l'échelle micronique est exclue par son propre radion, et la fenêtre survivante est nanométrique.

Statuts pour Paper B : α_r = 1/3 **[Established, cité]** ; la correction c_α = −0,634(βL)² **[Derived, moduli-space]** ; λ_r dérivé du fond **[Derived]** ; **la carte d'exclusion et le no-go du micron [Derived, conditionnel à la digitisation officielle]**.

---

# B. Secteur nul (T1) — **partiellement occupé ; R11 à compléter**

## B.1 Ce qui existe

- **« The Interval Approach to Braneworld Gravity », hep-ph/0506305, §4.2 « p² = 0 »** : utilise explicitement une décomposition tensorielle **massless** contenant le terme **−a²p_μp_ν φ̄₁**, c'est-à-dire exactement la structure qui, chez nous, rend ∂_μ∂_νq simultanément scalaire et transverse-sans-trace. **La dégénérescence de la décomposition SVT sur le cône nul, en gravité de braneworld sur intervalle, est donc traitée dans la littérature.** À lire intégralement avant toute revendication sur le secteur nul.
- **Mukohyama & Kofman, hep-th/0112115** : démontrent la positivité du secteur tenseur par **exactement notre technique d'identité d'énergie** — η^{μν}k_μk_ν ∫e^A F² = −∫e^{−3A}[(e^{2A}F)′]² ≤ 0. C'est le précédent méthodologique direct de notre identité m²‖X‖_K² = ½∫e^{4A}𝒢² + bord, dans le secteur tensoriel.
- Condition d'existence d'un zéro-mode : Lesgourgues–Sorbo (voir R11_T2_ANTERIORITE.md) et Mukohyama–Kofman.

## B.2 Ce qui reste candidat

Non trouvé dans cette passe, donc **[Candidate, R11 partiel]** — à confirmer par lecture intégrale de hep-ph/0506305 :
- l'énoncé quantitatif de la **perte de la jonction ∂_μ∂_ν par le principe variationnel scalaire à p² = 0** (déterminant des conditions = 3p⁴, rang 1 à p² = 0) ;
- la conclusion que le **noyau nul physique est vide** sur la branche générique σ₀″(y_i) ≠ 0 ;
- le traitement du secteur strictement statique donnant l'absence de zéro-mode radion avec δL = ∫G dy = 0.

## B.3 Conséquence sur Paper A

La section « secteur nul » ne peut pas être présentée comme neuve tant que hep-ph/0506305 n'a pas été lu en entier. Deux issues : soit la perte de la jonction ∂∂ y figure et notre apport se réduit au **patron d'erreur N°5** comme leçon de méthode (ce qui reste une contribution légitime, mais mineure) ; soit elle n'y figure pas et la section tient. **À trancher avant rédaction.**

---

# C. Registre R11 consolidé

| Objet | Statut | Référence |
|---|---|---|
| Critère T2 (2 branes, warp monotone) | [Established] | Lesgourgues–Sorbo hep-th/0310007 |
| **Extension au warp non monotone** | **[Derived, défendable]** | — (LS excluent explicitement ce cas) |
| Méthode : identité d'énergie à positivité manifeste | [Derived] ; précédent tensoriel | Mukohyama–Kofman hep-th/0112115 |
| α_r = 1/3 (n = 1) | [Established] | Adelberger et al. hep-ph/0611223 |
| α_KK = 8n/3 | [Established] | Kehagias–Sfetsos hep-ph/9905417 |
| Problème du radion dans la dimension sombre | [Established, question ouverte déclarée] | Montero–Vafa–Valenzuela JHEP 02(2023)022 ; JHEP 02(2026)156 |
| **Carte d'exclusion GW + no-go du micron** | **[Derived, conditionnel digitisation]** | — |
| Dégénérescence SVT à p² = 0 en braneworld | [Established] | hep-ph/0506305 §4.2 |
| Perte de la jonction ∂∂ à p² = 0 ; noyau nul vide | **[Candidate, R11 à compléter]** | lecture intégrale hep-ph/0506305 requise |
