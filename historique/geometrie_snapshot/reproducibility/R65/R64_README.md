# Dossier R64 — mode d'emploi

## Résultat

R64 a testé les deux routes du seuil de substance.

- Le critère général de coupe anticanonique est démontré, mais ses ingrédients
  sont standards dans la littérature torique/Tyurin.
- Une proposition rationnelle uniforme parité–Hodge est démontrée sous des hypothèses
  explicites : pour O3/O7 ou O5/O9, avec branches préservées ou échangées,
  aucun tube propre actif survivant dans le secteur vectoriel fermé de
  \(C_4\) ne peut provenir d'une classe non nulle de carré \(C^2\geq0\).
- Si la couture R63 satisfait \(NS(S)=L=U(2)\), le secteur propre requis est
  nul. L'application au membre très général reste conditionnelle à la porte
  de dominance des coefficients.

Ce résultat ne touche ni la tour KK neutre, ni les secteurs ouverts ou
brane–image, ni la tour candidate du parent \(\mathcal N=2\). Il ne dérive
pas \(R(t)\), une valeur micrométrique ou le plan de Fano.

## Commande unique

~~~bash
python3 r64_substance_gate.py
~~~

La commande :

1. rejoue la porte R63 ;
2. exécute trois certificats R64 indépendants ;
3. vérifie la table complète des quatre parités orientifold ;
4. contrôle le manifeste et les limites obligatoires des claims ;
5. garde ouverte la tube map intégrale équivariante et refuse de conclure à
   une tour, à une valeur micrométrique ou à une
   disponibilité immédiate de l'Article 1.

## Pièces principales

| Fichier | Rôle |
|---|---|
| R64_REPORT.md | rapport consolidé faisant autorité |
| R64_CLAIM_LEDGER.csv | registre des affirmations, réfutations et limites |
| R64_DATA_MANIFEST.json | hypothèses et conclusions lisibles par machine |
| R64_ERRATA_R62_R63.md | corrections de portée imposées par R64 |
| R64_ARTICLE1_DECISION.md | décision éditoriale et travaux encore bloquants |
| R64_GITHUB_SYNC_NOTE.md | audit du README public et correction requise avant diffusion |
| R64_AUDIT_OUTPUT.txt | sortie figée de la porte |
| R64_MANIFEST.sha256 | empreintes des pièces reproductibles |
| r64_substance_gate.py | lanceur bloquant |
| meta_audit_r64/ | preuves spécialisées, contre-exemples et pré-rapports |

## Lecture du verdict

La ligne R64_INTERNAL_SUBSTANCE_GATE = PASS_NARROW signifie qu'un résultat
conditionnel subsiste au-delà de l'exemple. La nouveauté large échoue toutefois
contre la littérature récente. La formule uniforme à quatre cas doit être
présentée comme proposition conditionnelle dans un article géométrique
étroit, pas comme article autonome.

## Étape suivante

R65 est le pilote spectral préenregistré. Son but sera de vérifier qu'un
pipeline numérique distingue une vraie famille KK unidimensionnelle d'un
petit mode de Cheeger/tunneling et d'excitations transverses.

