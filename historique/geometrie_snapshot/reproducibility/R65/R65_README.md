# Dossier R65 — mode d'emploi

## Verdict

`R65_SPECTRAL_PIPELINE = GO`

Les contrôles intervalles et cercle sont reconnus, y compris leurs
multiplicités. Le mode de Cheeger/tunneling et la contamination transverse
sont rejetés selon les seuils gelés avant calcul.

Ce verdict valide seulement le pipeline scalaire sans dimension. Il ne teste
pas la géométrie DDF, le spectre spin-2, une tour physique, \(R(t)\) ou une
échelle micrométrique.

## Reproduction

~~~bash
python3 r65_spectral_pilot.py
python3 r65_release_gate.py
~~~

## Fichiers principaux

| Fichier | Rôle |
|---|---|
| `R65_PREREGISTRATION.md` | hypothèses, modèles et seuils gelés |
| `R65_CONFIG.json` | configuration lisible par machine |
| `r65_spectral_pilot.py` | calcul des cinq familles spectrales |
| `R65_RESULTS.json` | résultats structurés |
| `R65_SPECTRA.csv` | 750 niveaux |
| `R65_METRICS.csv` | métriques des 25 cas |
| `R65_PROFILES.csv` | profil du premier mode d'haltère |
| `R65_SPECTRAL_DIAGNOSTICS.png` | figure synthétique |
| `R65_CLAIM_LEDGER.csv` | statut exact des affirmations |
| `R65_R66_DECISION.md` | condition de passage à R66 |
| `R65_REPORT.md` | rapport scientifique consolidé |
| `R65_RUN_OUTPUT.txt` | sortie figée du calcul |
| `R65_AUDIT_OUTPUT.txt` | sortie figée de la porte de libération |
| `R65_MANIFEST.sha256` | empreintes internes |

## Suite

R66 doit verrouiller une plateforme géométrique unique avant de construire
une approximation métrique à \(t_\star\ne0\). Un signal scalaire convergent
sera nécessaire avant toute tentative d'interprétation spin-2.


