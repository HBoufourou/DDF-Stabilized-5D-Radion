# Relecture indépendante du manuscrit révisé

> **Statut au 7 septembre 2026 :** compte rendu conservé de la relecture avant intégration. Les corrections retenues ont été appliquées au manuscrit livré, y compris les quatre précisions finales de notation. Le [bilan final](AUDIT_FR.md) distingue les corrections intégrées des limites scientifiques restantes.

Date : 7 septembre 2026. Fichier effectivement relu : `work/ddf_article1_review_2026_09_07/repository/publications/article_1/manuscript.json`. Relecture ciblée des corrections, avec lecture du corps, de l'annexe A et de l'annexe B ; aucun fichier du manuscrit modifié. Les calculs numériques complets n'ont pas été réexécutés pendant cette dernière passe.

## Conclusion

**Les corrections scientifiques prioritaires sont intégrées. Aucun nouveau contre-exemple physique sérieux ni erreur algébrique bloquante n'a été identifié dans les passages contrôlés.** Le résultat T1 est limité au domaine linéaire propagatif, plat, régulier, avec q≠0 et D₀Dᴸ≠0, et aux opérateurs de bord déclarés. La positivité massive requiert les poids de bord positifs, établis sur la branche principale. Le manuscrit n'en déduit ni théorie DDF complète, ni stabilité non linéaire, ni validation expérimentale.

Il reste une clarification dimensionnelle recommandée dans A0a/A0b et deux précisions de notation. Elles n'altèrent pas les résultats.

## Vérifications scientifiques

- **Annexe B et Hessienne B9a : correctes dans la convention indiquée.** L'expression est le coefficient de ε² pour une variation métrique linéaire γ=e²ᴬ(η+εhφ), et non la dérivée seconde sans division par 2. L'expansion du déterminant fournit h²/8−hμνhμν/4. Avec hμν=2Fημν, elle donne 4F² ; le terme croisé est 4FU′s et U″s²/2=λs². On obtient donc exactement −e⁴ᴬ[λs²+4FU′s+4UF²]φ². Un chemin métrique exponentiel aurait un coefficient de potentiel isolé différent ; le texte spécifie correctement son chemin et ne confond pas les deux.
- **Junctions et candidat X₁ :** la condition anisotrope Ξᵢ+Zᵢ=0 demeure indépendante des projections nulles. Avec qᵢDᵢ≠0, les deux extrémités imposent C=c₁=0. Le candidat négatif reste hors domaine ; les contributions de coin sont conservées, N=Z/2 est explicite, et l'argument de quotient utilise aussi les appariements mixtes. Aucune extension injustifiée du résultat n'a été ajoutée.
- **Secteur vectoriel p²≠0 :** le raisonnement par contrainte mixte dans la jauge normale gaussienne est approprié au système déclaré. □V′=0 implique V′=0 ; le difféomorphisme tangentiel résiduel enlève ce représentant. Les cinq polarisations du tenseur massif incluent ses hélicités un. La preuve n'utilise pas ce raisonnement sur la couche nulle.
- **Section 7 :** la borne inférieure (Λ₅−2λ²v²)/(6B)<h est bien présentée dans un voisinage du fond plat avec événement positif transverse. Les bornes centrales ne remplacent pas les contrôles de régularité. La réponse linéaire exacte au point plat est distinguée de l'approximation à détuning fini.
- **Équation 24b :** les deux bornes sont exactes pour le coefficient dominant. En effet c₀/κ₀=(coth x+1/x)/(2x), tandis que c∞/κ∞=(coth x−1/x)/(2x). La largeur π²/x² et l'erreur O(ε²) après division par le rapport des masses au carré sont correctes à x fixé. Aucune borne erronée cα>1/3 ne subsiste.
- **Unités, limite affine et portée :** le facteur BL³ n'est plus fixé physiquement à un ; la branche affine est séparée de λ→0 à v fini ; les limites faibles sont point par point, et non des bornes uniformes. La conclusion ne revendique pas de prédiction absolue du rayon.

## Dernières corrections de présentation conseillées

1. **A0a/A0b : éviter la redéfinition implicite de I et Nf.** Dans le corps, I a la dimension d'une longueur et Nf celle d'une masse au carré. « In reduced units » laisse encore implicite leur rescaling. Écrire directement :

   `I/L = 1 + 2 ε²⟨a₂⟩ + O(ε⁴)`

   `N_f/(3BL) = 1 + ε²[2⟨a₂⟩ + 2⟨f₂⟩ + ⟨s₁²⟩/6] + O(ε⁴)`.

   Une phrase sans ambiguïté entre le point y=0 et le milieu t=0 serait :

   “For the boundary profile f_b=1+ε²f₂(1/2)+O(ε⁴), inserting 3α_r=[(I/L)f_b²]/[N_f/(3BL)] cancels the identical Planck-volume term and gives (21).”

   Le coefficient (21) demeure inchangé.

2. **Section 5 :** préciser “Use dimensionless coordinates x^μ/L and y/L …”. Le facteur global BL³ suppose également le rescaling des quatre coordonnées de tranche ; ne citer que y/L laisse cette étape sous-entendue.

3. **Avant B10 :** préciser “In (B10)–(B11), h_ab denotes δg_ab and its indices are raised with the background metric.” Le hμν de B1/B9a est une perturbation sans le facteur e²ᴬ, alors que la formule covariante emploie la variation du métrique complet. La convention est standard, mais la préciser évite une fausse incompatibilité de facteurs de warp.

Cette relecture porte sur la cohérence et la formulation du manuscrit révisé. Elle n'est pas un rapport externe de revue et ne statue pas sur une publication ou une procédure arXiv.
