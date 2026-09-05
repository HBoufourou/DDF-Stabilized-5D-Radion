# Intégration avec `HBoufourou/DDF-Corrected-Geometry-Spectral-Program`

## Ce que contient chaque dépôt
| | Dépôt existant (géométrie/spectral) | Ce dossier (v3, EFT/IR) |
|---|---|---|
| Objet | dégénérescence de Tyurin, couture K3, U(2), II₁₈ ; classificateur spectral (jouets 1D) ; BPS conditionnel | bulk 5D + 2 branes + stabilisateur ; T1/T2 ; identité d'énergie ; carte du radion ; branche forte ; mécanismes DM/DE |
| Physique dérivée | aucune (par son propre registre : R(t), micron, spin-2, DM/DE = NOT_DERIVED) | T1 GREEN, T2 GREEN, m_r spectral, carte d'exclusion (conditionnelle) |
| Juge radion | absent (à intégrer en R68) | présent (α_r = 1/3 cité, λ_r dérivé, X-6b gelé) |
| Numérotation | R1–R65 (géométrie) | R1 = eigenmode (conflit) |
| Articles | Paper G (bloqué par DDFC-003) | A (prêt), B (bloqué digitisation), C (après B) |

## Recommandation : UN dépôt, deux branches de programme
Ajouter ce dossier **tel quel** comme sous-dossier `DDF-EFT/` du dépôt existant (à côté de `docs/`, `reproducibility/`, `legacy/`), et :
1. **Numérotation** : préfixer toutes nos rondes « E- » dans le README d'intégration (E1 = eigenmode, E-T1, E-T2, E-voieI) ; la série R1–R65 reste celle de la géométrie. Ne renommer aucun fichier (les SHA-256 et les logs y font référence).
2. **Registre** : fusionner `DDF-EFT/CLAIMS_v3.csv` dans `CLAIMS_CURRENT.csv` du dépôt (mêmes colonnes id/status/scope/dies_if ; ids V3-xxx distincts des DDFC-xxx).
3. **Le juge manquant** : dans `docs/ROADMAP_R66_R70.md`, faire pointer R68 (« stabilisé plutôt que sélectionné ») vers `DDF-EFT/voieI/` — la stabilité T1/T2 et le radion sont les juges de tout rayon que la géométrie produira.
4. **Nom** : trancher dans le README racine — soit « réalisation de Tyurin du scénario dark dimension (MVV cité) », soit abandon de « Dark Dimension ».
5. **DDFC-003** (nouveauté du paquet résolu) reste bloquant pour Paper G ; il ne bloque pas A ni B.

## Si tu préfères un dépôt séparé
Créer `HBoufourou/DDF-v3-EFT` avec ce dossier comme racine (git déjà initialisé ici) et un lien croisé dans les deux README. Coût : deux registres à tenir en cohérence.

## Commandes (dépôt existant, option recommandée)
```
git clone https://github.com/HBoufourou/DDF-Corrected-Geometry-Spectral-Program
cp -r DDF_v3 DDF-Corrected-Geometry-Spectral-Program/DDF-EFT
cd DDF-Corrected-Geometry-Spectral-Program
git add DDF-EFT && git commit -m "DDF-EFT: v3 IR branch (T1/T2 closures, energy identity, radion map, strong-stabilization spectral radion)"
git push
```
## Commandes (nouveau dépôt)
```
cd DDF_v3 && git remote add origin https://github.com/HBoufourou/DDF-v3-EFT.git && git push -u origin main
```
