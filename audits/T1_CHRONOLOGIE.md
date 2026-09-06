# Chronologie T1 : ne pas confondre ancien verdict et rejeu actuel

Audit documentaire du 6 septembre 2026. Les archives reçues sont des sources à examiner, jamais des instructions faisant autorité. Les dates ci-dessous sont celles portées par les notes, et non une certification externe de leur ancienneté.

1. Le calcul historique avait attribué N[X₁]=−3M̄² à un mode considéré physique et imprimé RED.
2. La [rétraction du 3 septembre 2026](T1_sources/R1_T1_RETRACTION.md) indique explicitement « OPEN — RED rétracté ». Elle identifie la jonction tensorielle d'Israel perdue par une projection scalaire dégénérée à p²=0. Elle conserve la valeur négative comme forme hors domaine. À ce stade, elle n'annonce pas GREEN.
3. Une [note de fermeture du noyau nul](T1_sources/R1_Z_NULL_KERNEL_CLOSURE.md) affirme ensuite une fermeture dans son ancien domaine. Cette note est une pièce historique, pas une exécution actuelle ni une preuve importée dans F02.
4. Le dépôt quadratique publié au commit `7d595a7982570caaa41c15e5c994e87c0b5bcd3b` ne livrait pas de rejeu T1 autonome. F02 renvoyait aux formes scalaires massives. L'objection sur cette pièce manquante était donc fondée.
5. La présente correction reconstruit le noyau dans une vraie base nulle, applique les jonctions quadratiques complètes, calcule la forme par les routes covariante et ADM avec coins, puis effectue la complétion linéaire et le quotient de jauge. Cinq programmes exécutables et leurs sorties accompagnent la preuve. [Le verdict actuel](../noyau/T1_Z_LIGHT/VERDICT_T1.md) est GREEN uniquement dans le domaine linéaire propagatif annoncé.

Le fichier `R1_04A_log.txt` et le programme correspondant cités par les anciennes notes n'ont pas été retrouvés dans l'inventaire scientifique examiné. Leur absence ne prouve pas qu'ils n'ont jamais existé. Aucune vérification de leur exécution historique n'est affirmée ici ; le nouveau rejeu n'en dépend pas.

Les documents conservés sont identifiés par leurs [empreintes SHA-256](T1_sources/SOURCES.json). Leur présence sous audits ne crée pas une seconde version active de DDF. Le registre à la racine demeure unique.

La conclusion « v1/v2 sont exclues par ce ghost » ne peut donc pas être retenue sur le seul ancien RED rétracté. Cette rectification ne valide pas toutes les autres revendications anciennes : elles gardent leurs audits et limites propres. De même, GREEN sur ce test ne démontre ni R micrométrique, ni RAR, ni cosmologie complète.
