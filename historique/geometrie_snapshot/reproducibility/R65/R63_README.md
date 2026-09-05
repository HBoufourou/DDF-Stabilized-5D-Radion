# Dossier R63 — mode d'emploi

## Résultat

La porte mathématique est positive : dégénérescence de Tyurin stricte au sens
DHT et LMHS rationnelle \(\mathrm{II}_{18}\) pour une couture très générale.
La SNF de la Gauss–Manin intégrale, \(R(t)\), l'échelle micrométrique et la
tour physique restent ouverts.

## Commande unique

~~~bash
python3 r63_strict_tyurin_gate.py
~~~

La commande :

1. reproduit octet par octet les sorties R61 et R62 ;
2. exécute deux contre-audits indépendants du fan et du Jacobien ;
3. vérifie le certificat torique/quasi-Fano ;
4. exécute le second calcul EMS des cohomologies ;
5. contrôle la présence des rapports et les limites obligatoires des claims.

## Pièces principales

| Fichier | Rôle |
|---|---|
| R63_REPORT.md | rapport consolidé faisant autorité |
| R63_CLAIM_LEDGER.csv | registre des affirmations et limites |
| R63_MANIFEST.sha256 | empreintes SHA-256 des pièces reproductibles |
| R63_ERRATA_R61_R62.md | corrections obligatoires des rapports antérieurs |
| R63_AUDIT_OUTPUT.txt | sortie figée de la porte principale |
| r63_strict_tyurin_gate.py | lanceur bloquant |
| r63_independent_lattice_fan.py | contre-audit réseau/fan |
| r63_independent_jacobian_snc.py | contre-audit monômes/Jacobien/SNC |
| meta_audit_r63/ | rapports spécialisés et certificats complémentaires |

## Statut de livraison

R63 est un dossier de recherche complet pour cette porte. Ce n'est pas encore
le dossier final d'un article : le manuscrit LaTeX/PDF, la comparaison
d'antériorité intrinsèque et une lecture experte externe restent à produire.

