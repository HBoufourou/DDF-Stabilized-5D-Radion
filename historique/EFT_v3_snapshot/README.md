# DDF v3 — dossier complet (branche EFT/IR)
**Hicham Boufourou**, chercheur indépendant, Ingelmunster, Belgique — mis à jour le 5 septembre 2026

## État au 05/09/2026 — ce qui a changé depuis le 03/09
- **`CONSTITUTION_v3.md`** : le R0 de la version 3 — même action maîtresse, **branche « stabilisation forte » βL ∈ [0,4 ; 0,9] déclarée ouverte** (les plafonds v1 étaient des choix de modélisation, pas des limites physiques) ; R hérité de Λ (cité) et validé par ses juges, jamais dérivé ; Λ = entrée ; radion = signature, pas matière noire.
- **`voieI/`** : le calcul décisif — **m_r spectral réel** sur le fond backreacté (`mr_spectral.py`, `VOIE_I_SPECTRAL.md`). Pipeline validé (zéro-mode spurieux retrouvé à 10⁻¹⁰ ; accord moduli à petit βL +0,3/+1,0/+2,1 %). **Résultat : λ_r = 19–38 μm à R* = 8,2 μm pour βL ≥ 0,4 — le micron revient dans la classe auditée**, avec fond existant, carte OK, T2 exact satisfait. Portes : EFT à σ₀ ~ M₅^{3/2}, digitisation, c_α(βL).
- **`registres/MECHANISM_EXCLUSION_MAP.md`** : carte d'exclusion des mécanismes DM/DE (survivants : rez-de-chaussée condensé non radionique + étages supérieurs ; DE = entrée).
- **`registres/ASSEMBLY.md`** : le graphe d'assemblage — aucune arête contradictoire, trois calculs [Open], une tension (radion) résolue par la voie I ; rôle exact de LHCb.
- **`CLAIMS_v3.csv`** : registre des revendications v3 (18 lignes, ids V3-xxx) au format du dépôt existant.
- **`INTEGRATION_AVEC_DEPOT_EXISTANT.md`** : comment ce dossier s'emboîte dans `DDF-Corrected-Geometry-Spectral-Program` (recommandé : sous-dossier `DDF-EFT/`, numérotation E-, fusion des registres, R68 pointe sur voieI).

Reproduction : `python3 paperA/verify_identity.py` (sympy, secondes) ; `python3 voieI/mr_spectral.py` (scipy+sympy, ~2 min) ; `python3 paperB/exclusion_map.py` (s'arrête volontairement sans digitisation).

---

## Contenu

```
registres/
  R11_REGISTRE.csv          24 lignes : ce qui est cité (20), ce qui est revendiqué (3), interne (1)
  STATUS.json               statuts complets, morts documentées, dettes ouvertes, règle R9
paperA/
  paperA.tex                article A, prêt à compiler
  verify_identity.py        6 contrôles symboliques, tous passés (sympy, quelques secondes)
  results.json              identité, critère, contribution de domaine, liste des contrôles
paperB/
  paperB.tex                article B, marqué DRAFT et bloqué
  exclusion_map.py          refuse volontairement tout verdict sans digitisation officielle
  alpha95_SCREENING_SLOT.csv   1 point ancré (Lee 38,6 μm), 11 slots à remplir
  parameters.json           constantes citées / dérivées, seuils pré-enregistrés, résultat conditionnel
```

Reproduction : `python3 paperA/verify_identity.py` (sympy). Compilation :
`pdflatex paperA.tex`, `pdflatex paperB.tex`.

---

## Où en est chaque article

### Paper A — « A regular energy identity… » — **rédigeable maintenant**

**Ce qu'il contient, après deux rétrogradations R11.** Le critère de stabilité
n'est pas revendiqué : il est de Lesgourgues & Sorbo (2004). Le cadre par
intervalle avec principe d'action et le traitement du cône nul ne sont pas
revendiqués : ils sont de Carena, Lykken & Park (2005). La technique
d'identité d'énergie a son précédent chez Mukohyama & Kofman (2002).

Restent **deux** choses :

1. **L'identité constructive**
   m²‖X‖² = ½∫e^{4A}𝒢² + Σ_i s_i(e^{4A}σ₀″/2σ₀′)s(y_i)²,
   régulière (aucun A′, aucun 1/p², aucune condition de bord dépendante de m²),
   et **autovalidée** : sa condition de bord naturelle *est* la jonction certifiée.
2. **La validité sans hypothèse de warp monotone** — la seule contribution de
   domaine. Lesgourgues & Sorbo supposent a(y) monotone et écrivent
   explicitement que le cas U₊ = U₋ leur échappe ; Carena–Lykken–Park n'ont pas
   de scalaire de bulk. Le fond GW Z₂-symétrique tombe exactement dans cet
   interstice, et c'est le fond du programme.

**Format** : note courte. **Blocage** : aucun sur le fond ; il reste
l'**endossement** (gr-qc ou hep-th, non acquis — l'auto-endossement obtenu via
Paper I vaut pour astro-ph).

**Condition de mort** : si le critère apparaît publié dans cette généralité, ou
si un traitement non monotone existe déjà, A devient une note de méthode
interne et n'est pas soumis.

### Paper B — « The radion constrains the dark dimension » — **bloqué, et le blocage est sain**

**La niche est confirmée par R11, et elle est bonne.** Montero, Vafa et
Valenzuela déclarent eux-mêmes le problème du radion ouvert dans JHEP 02 (2023)
022 ; un article de 2026 trouve le radion trop léger dans une réalisation
Casimir. Personne n'a produit, pour un fond stabilisé Goldberger–Wise, une carte
d'exclusion où α_r et λ_r sont **dérivés du fond**. B revendique **la carte et
son verdict** — le micron exclu par son propre radion, fenêtre survivante
nanométrique — pas le couplage (α_r = 1/3 est cité).

**Blocage unique et bloquant** : la digitisation officielle des courbes α95.
Le juge X-6b est gelé ; la courbe de screening actuelle a **un** point ancré et
des incertitudes de facteur 2–3 ailleurs. Elle suffit à trier l'espace des
paramètres, pas à publier une exclusion. `exclusion_map.py` s'arrête de lui-même
tant que le CSV n'est pas rempli — c'est délibéré.

**À faire, dans l'ordre** : (1) obtenir la digitisation (demande aux auteurs, ou
extraction traçable des figures publiées avec incertitudes) ; (2) relancer le
scan ; (3) si le verdict tient, rédiger ; (4) endossement.

**Condition de mort** : si la digitisation officielle déplace la région verte
jusqu'à réhabiliter le micron, la thèse centrale tombe et B devient une carte de
contraintes sans no-go.

### Paper C — condensat de bulk et RAR — **n'existe pas encore, et c'est correct**

L'idée : un condensat vivant dans la dimension sombre, dont le phonon donne la
relation d'accélération radiale et dont la tour donne la signature en gravité
sub-millimétrique. R11 a montré que le pont est réellement libre : Berezhiani &
Khoury posent un axion 4D sans dimension supplémentaire ; Kao (2006) est un
modèle-jouet ; personne ne les a réunis.

**Trois portes, toutes fermées aujourd'hui.**

1. B doit survivre à la digitisation.
2. **La tour passe de meV à 3–70 eV** dans la fenêtre nanométrique. Tout
   mécanisme de matière noire doit être **reconstruit** à cette échelle — les
   Parties III et IV de CDD ne se transposent pas.
3. Le lien Λ ↔ L par la conjecture de distance, qui donnait le micron, doit être
   re-dérivé ou abandonné.

**Un garde-fou à écrire avant toute rédaction** : la relation
a₀ ≈ cH₀ ~ m_KK²/M̄ est une **coïncidence de classe** (les deux descendent de Λ,
et Milgrom l'a notée dès l'origine). Elle donne au pont sa colonne vertébrale ;
elle ne doit **jamais** être présentée comme une prédiction.

---

## Calendrier — « c'est à quand »

La seule date dure du programme n'est aucune de celles-ci : c'est **Gaia DR4**.

| Échéance | Objet | Dépend de |
|---|---|---|
| **maintenant → octobre** | rédaction de **Paper A** | rien |
| **maintenant, en parallèle** | demande de digitisation α95 | tiers |
| **maintenant, en parallèle** | recherche d'un **endosseur gr-qc/hep-th** | tiers |
| **11 novembre 2026** | **gel v1.0 du protocole DR4** | portée s_max du nul DR3 + incertitudes par bin + ta validation de la correction Art. III §8(ii) |
| **18 novembre 2026** | Zenodo + horodatage OTS | gel |
| **22 novembre 2026** | dépôt arXiv du protocole | gel + endossement astro-ph (acquis) |
| **2 décembre 2026** | **sortie Gaia DR4** | — |
| **dès digitisation reçue** | scan, puis rédaction de **Paper B** | digitisation |
| **2027, si B survit** | ouverture de **Paper C** | B + mécanisme reconstruit à l'échelle eV |
| **en continu** | v2 Zenodo du corpus I–VIII : corrections (a)–(m), certificats R1, carte d'exclusion | rien |

**Le protocole DR4 ne dépend d'aucune de ces décisions et ne doit pas être
retardé par elles.** C'est la seule pièce du programme avec une date imposée de
l'extérieur.

**Réponse courte.** Paper A : quelques semaines de rédaction, soumission
possible dès l'endossement obtenu — donc plausiblement **octobre–novembre 2026**.
Paper B : **indéterminé, gouverné par la digitisation** ; si elle arrive en
octobre, soumission début 2027. Paper C : **2027 au plus tôt, et seulement si**
les trois portes s'ouvrent — sinon il n'existe pas, et on le dit.

---

## Règle R9, rappelée

Aucune modification de U_i, J_i, V_σ, Λ₅, des conditions de bord, ni ajout de
champ, de terme cinétique de brane ou de contre-terme destiné à déplacer une
conclusion. Toute modification de cette nature ouvre un **nouveau modèle**, avec
son registre, sa carte d'exclusion et son R1.

## Ce qui est vivant hors de ce dossier

Paper I (arXiv:2608.24556, publié) ; le protocole Gaia DR4 ; la couche milieu de
CDD (RAR, w = 1/2) ; les théorèmes mathématiques (ζ_well, pôle Robin) ; et la
machinerie R1 elle-même, réutilisable pour toute construction à deux branes.
