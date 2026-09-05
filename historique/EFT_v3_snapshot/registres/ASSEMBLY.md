# DDF v3 — Assemblage : comment les pièces tiennent ensemble
Date : 05/09/2026. Réponse à « séparément ça passe, ensemble ça cale ».
Règle de lecture : chaque pièce porte son étiquette d'origine. **[Established]** = littérature citée ; **[Derived]** = notre audit ; **[Posited]** = hypothèse déclarée ; **[Open]** = calcul non fait.

---

## 1. Le graphe

```
   Λ observée  ──[Established: MVV]──►  R ~ micron (idée), m_KK ~ meV
                                              │
                    ┌─────────────────────────┴──────────────────────────┐
                    ▼                                                    ▼
      Bulk 5D + 2 branes + stabilisateur σ                   Champ de bulk Φ (U(1), |Φ|⁴)
      ─ stable : T1 GREEN, T2 GREEN          [Derived]       ─ tour KK, m_n ~ n·meV        [Derived: profil]
      ─ radion α_r = 1/3                     [Established]   ─ couplage brane g₅|ψ₁(0)|²   [Posited: valeur]
      ─ radion lourd si βL ≳ 0,5 (voie I)    [Derived, expl.]         │
      ─ EFT à σ₀ ~ M₅^{3/2}                  [Open: porte]            │
                    │                                    ┌─────────────┴──────────────┐
                    │                                    ▼                            ▼
                    │                          Étages supérieurs          Rez-de-chaussée condensé
                    │                          = CDM (misalignment)       = superfluide, w = 1/2
                    │                          [Open: relique au R validé] [Derived: RAR passée 0,1451 dex]
                    │                                    │   drip |Φ|⁴  [Posited]     │
                    │                                    └────────────►───────────────┘
                    │                                                                 │
                    ▼                                                                 ▼
        Signature gravité sub-mm :                                    Kelvons → RAR (a₀ = cH₀/2π)
        Δ(r) = α_r e^{−r/λ_r} + (8/3)Σe^{−nr/R}   [Derived]           [Derived, R11 kelvons à faire]
                    │                                                                 │
                    ▼                                                                 ▼
        Balances de torsion (α95)                  Galaxies (SPARC) ✓ ; binaires larges (Paper I, publié) ✓
        [juge X-6b, digitisation requise]          amas (phase mixte, BK) ; U-1, C-5 [Open]
                                                                 │
                                    LHCb #109/#110 ◄─────────────┘
                                    borne sur g₅ côté quark b = test partiel de U-1   [juge, date]
```

**Aucune arête n'est une contradiction.** Les arêtes rouges du programme sont des [Open] (calculs à faire) et une [Posited] (le drip).

---

## 2. La cohérence d'échelle que personne n'avait relevée

| Source | Échelle | Statut |
|---|---|---|
| Dimension sombre : m_KK ~ Λ^{1/4} | ~ meV | [Established] MVV |
| Matière noire superfluide (Berezhiani–Khoury) | m ~ eV, auto-interaction forte | [Established] BK |
| Rez-de-chaussée condensé de CDD | m₁ ~ 1/R ~ meV (micron) à ~eV (sub-micron) | [Derived: profil] |

**Même décade, trois origines indépendantes.** C'est ce qui rend l'assemblage non arbitraire — et c'est une cohérence de classe, pas une prédiction.

---

## 3. Où ça « calait » réellement — et ce que ça demande

| Blocage perçu | Nature réelle | Résolution |
|---|---|---|
| Micron + radion léger → cinquième force | **tension réelle** | voie I : βL ≳ 0,5 ⇒ λ_r ≈ 26–37 μm à 8,2 μm ; fond existe, T2 vert ; porte EFT à argumenter |
| 8,2 dérivé du Casimir | mort (signe faux) | R n'est plus dérivé du Casimir ; il est hérité de Λ [Established] et **validé** par le juge radion |
| Tour = CDM | jamais calculé | abondance relique par misalignment au R validé [Open] |
| Rez-de-chaussée alimenté | drip [Posited] | passer à [Derived] par le calcul des recouvrements |Φ|⁴ entre étages, ou déclarer la mort |
| Spectre d'Airy de Φ | lié au puits linéaire de v1 | la voie I relâche la linéarité ⇒ spectre à recalculer dans le puits non linéaire ; Article IX ne décrit plus la tour physique |
| DE | jamais expliquée | E2 : Λ est une entrée (cité) ; ne plus promettre |

---

## 4. Le rôle exact de LHCb

- Productions #109/#110 : désintégrations de hadrons beaux, pipeline validé sur 26 fichiers, lacune déclarée « production prompte non couverte » (correction (c)).
- Ce que le résultat donne : **une borne** sur le couplage de brane de la tour au quark b — via B → K + invisible (émission dans la tour).
- Pourquoi c'est bien placé : c'est **le même couplage g₅|ψ₁(0)|²** que CDD IV utilise pour l'interaction phonon–baryon de la RAR. Le collisionneur borne côté b ce que la galaxie fixe côté baryons ⇒ **test partiel de U-1** (universalité), qui est [Open] dans CDD I.
- Ce que ce n'est pas : une confirmation de la 5D. Un signal serait « un état invisible dans les désintégrations b », pas « DDF ».
- Quand : à l'arrivée des productions ; 2018 indisponible jusqu'en 2028.

---

## 5. L'équilibre boîte / littérature, rendu explicite

**Hors de la boîte (à nous, à défendre)** : le rez-de-chaussée condensé à enchevêtrement de vortex et kelvons comme porteurs de la RAR ; la tour à deux rôles ; le pont « condensat dans la dimension sombre » ; la carte d'exclusion du radion ; l'extension du critère de stabilité au warp non monotone.

**Dans la littérature (cité, jamais revendiqué)** : R micronique depuis Λ ; dark gravitons ; superfluide → MOND ; le critère de stabilité ; le cadre par intervalle ; α_r = 1/3 ; a₀ ≈ cH₀.

**La règle** : une pièce hors de la boîte n'entre dans l'assemblage que si elle a passé un juge (la RAR l'a fait ; les binaires larges l'ont fait). Une pièce de littérature n'est jamais recalculée pour être revendiquée — elle est citée.

---

## 6. Ordre d'exécution

1. Digitisation α95 → relance de la carte → voie I (m_r spectral, EFT). **Sortie : R validé, radion réglé.**
2. Au R validé : spectre de Φ dans le puits non linéaire → relique des étages supérieurs → drip → R11 kelvons → U-1/C-5 → trois signatures létales avec données en main.
3. LHCb à l'arrivée des productions : borne sur g₅, croisée avec la RAR.
4. DE : citée. Protocole DR4 : intouché, 2/12/2026.
