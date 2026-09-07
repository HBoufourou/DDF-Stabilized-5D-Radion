# État scientifique de la version canonique DDF

6 septembre 2026. Le statut porte sur des modèles et des régimes définis, sans certification expérimentale.

| Résultat | Statut précis | Limite principale |
|---|---|---|
| Action Einstein–σ et branes quadratiques | Définition explicite du noyau classique | Paramètres renormalisés libres ; origine UV non dérivée |
| Longueur à couplages donnés | Existence et unicité sur la branche plate déclarée | Tension compatible requise pour Minkowski |
| Spectre scalaire et tensoriel | Positivité linéaire et calculs contrôlés | Fonds plats réguliers ; pas stabilité non linéaire globale |
| Longueur et courbure à tension donnée | Branche locale calculée, dérivées et raffinements contrôlés | Spectre des tranches courbes non traité |
| Secteur Φ autour de zéro | Tour positive et fond conservé | Action minimale sans portails ajoutés |
| Profil homogène en y | Projection calculée et bornes sur toute la tour | Fraction d'énergie initiale, pas relique |
| Profils chargés avec quartique | Solutions et stabilité linéaire sonde | Métrique fixe ; charge et formation présupposées |
| RAR à source prescrite | Branches radiales et comparaisons d'énergie | Pas condensat complet ni action 5D dérivée |
| Halos à densité déterminée | Équilibre hydrostatique et surface calculés | Limites centrales/du raccord, charge NLO et stabilité globale ouvertes |
| Identification O8 / bords DDF | Raccord naïf réfuté dans la classe examinée | Pas une impossibilité générale pour Type I′ |
| R en micromètres | Non prédit indépendamment | μ et rapports de couplages doivent être déterminés |
| Accord aux expériences | Aucun verdict nouveau | Réponse des détecteurs et tests statistiques requis |

Le modèle possède des paramètres, comme toute théorie effective. Cela ne le rend pas faux ; cela limite le nombre de quantités prédites sans données supplémentaires. En revanche, une hypothèse ne doit pas être rebaptisée mesure ou dérivation.

Le résultat le plus mûr pour renforcer l'article est le secteur stabilisé à action fixée. Les profils Φ offrent un développement complémentaire précis. Les nouvelles solutions RAR ne permettent pas encore d'annoncer une explication des galaxies. La nouveauté bibliographique et l'intérêt éditorial des contributions demandent une évaluation externe.

Les résultats numériques sont conservés avec leurs paramètres. Une précision de raffinement ne constitue pas une mesure de l'erreur physique du modèle. Les bornes analytiques ont également leur domaine déclaré ; leurs valeurs numériques ne sont pas des intervalles certifiés.

## Renforcement de la correction

Le coefficient fermé cα(x,λ̂) et ses bornes positives sont maintenant dérivés et contrôlés. Les douze comparaisons Galerkin complètent les références FEM ; six petits ε contrôlent l’approche des coefficients. La relation au rapport mr/mT,1 élimine R à l’ordre déclaré, mais conserve les paramètres de forme.

Le premier manuscrit actif se trouve dans `publications/article_1/`, avec une action quadratique cohérente. La base Φ est dans `publications/article_2/`. Les contre-exemples sur les couplages et le domaine du sextique corrigent les anciens no-go trop larges, sans créer une dérivation MOND. La nouveauté, la publication et les observations restent distinctes de la vérification interne.

## Secteur nul explicitement rejoué

[T1 / Z-light](noyau/T1_Z_LIGHT/VERDICT_T1.md) donne **GREEN pour le domaine linéaire propagatif plat, q non nul, Dᵢ non nul et quotient de jauge déclaré**. Les conditions tensorielles complètes excluent X₁ ; ses deux calculs de forme retrouvent N=−3M̄² hors domaine. Le quotient scalaire/longitudinal nul est trivial, tandis que les deux polarisations du graviton restent positives. Les cinq programmes sont effectivement rejoués dans un répertoire neuf, avec [rapport](verification/T1_REPLAY_EXECUTED.json).

La stabilité massive conserve sa condition de poids de bord positifs. Le secteur p^μ=0, les points q=0 ou Dᵢ=0, les tranches courbes, les corrections quantiques et la stabilité non linéaire restent hors de ce résultat. T1 est un contrôle interne distinct d’E01 ; ni la valeur absolue de R ni la RAR ne sont dérivées par ce verdict.

## Révision du premier article du 7 septembre

La preuve T1 est intégrée au manuscrit. Les corrections bibliographiques, le domaine local de courbure et les bornes asymptotiques sont détaillés dans [le rapport de relecture](audits/article1_2026_09_07/AUDIT_FR.md). Les calculs du noyau sont reproduits ; la nouveauté et la substantialité éditoriale restent à apprécier extérieurement.
