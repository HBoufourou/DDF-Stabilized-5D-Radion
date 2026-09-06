# T1 / Z-light : verdict après rejeu sur l'action quadratique

**T1 = GREEN dans le domaine linéaire propagatif déclaré ci-dessous.** Le mode X₁ est exclu par les jonctions complètes. Sa forme négative est reproduite, mais elle ne constitue pas la norme d'un état physique admissible.

Date : 6 septembre 2026. Ce complément concerne le même modèle DDF-Stabilized-5D-Radion et le premier manuscrit de stabilisation. Il ne change aucun potentiel, paramètre ou condition aux limites pour obtenir le verdict.

## Domaine exact

Un intervalle physique fini et régulier ; B=M₅³>0 ; tranches de Minkowski ; scalaire canonique stabilisateur avec q=σ₀′ non nul partout ; EH B/2, GHY B et seuls potentiels isotropes Uᵢ=τᵢ+λᵢ(σ−vᵢ)² aux bords ; matière au vide. Le test nul utilise p²=0 et p^μ≠0, sans projecteur 1/p². Les intégrales de modes sont comprises par unité de volume Fourier, ou pour des paquets sans charge supplémentaire à l'infini spatial.

Le domaine nul exige Dᵢ=Wᵢ+ηᵢUᵢ″≠0, W=σ₀″/σ₀′. Le bilan avec les modes massifs de F02 exige aussi ηᵢWᵢ+Uᵢ″>0. La branche symétrique principale avec μ>0, Λ₅>0 et λᵢ>0 satisfait ces conditions tant que le fond est régulier. Les deux polarisations du graviton sans masse demeurent physiques et positives.

Sont hors verdict : p^μ=0, q=0, Dᵢ=0, fonds courbes, nouvelles cinétiques ou nouveaux champs sur les branes, états matériels occupés avec rétroaction, stabilité non linéaire et corrections quantiques.

## 1. Le candidat est passé dans les nouvelles jonctions

Poser I(y)=∫₀ʸe²ᴬdu et χ=B₅−e²ᴬÊ′, où B₅ désigne le décalage métrique, distinct de B=M₅³. La reconstruction complète donne

\[
F=A'z-c_1,\quad G=z',\quad s=\sigma_0'z,
\qquad \chi=z-(2c_1I+C)e^{-2A}.
\]

Elle inclut le traitement des composantes supplémentaires d'une vraie base nulle, et non seulement un ansatz scalaire supposé complet. Pour les positions de brane Zᵢ et θᵢ=zᵢ+Zᵢ, les jonctions de la même action sont

\[
q_iD_i\theta_i=0,\qquad \chi_i+Z_i=0.
\]

Sur les bords fixes, X₁ correspond à c₁=1, C=z=0. Il satisfait le bulk et la jonction scalaire, quelle que soit la rigidité finie, mais

\[
\chi_0=0,\qquad \chi_L=-2I_Le^{-2A_L}\ne0.
\]

Il viole donc la jonction tensorielle sans trace au bord droit. Ses projections scalaire de trace et de double divergence sont nulles malgré ce résidu tensoriel non nul. La condition ne peut pas être perdue en projetant par p²=0. Déplacer le bord pour réparer Israel produit qᴸDᴸZᴸ≠0 et viole la jonction scalaire générique.

La rigidité ne constitue pas un nouveau mécanisme de sauvetage : le problème ancien à potentiels affines devait lui aussi respecter la jonction tensorielle complète. Le nouveau calcul adapte explicitement le coefficient Dᵢ aux potentiels quadratiques.

## 2. La valeur −3M̄² est reproduite par deux routes

Avec Ω(X*₁,X₁)=2iωZ et N=Z/2, M̄²=BIᴸ, les résultats sont :

| Route, termes conservés | Volume Z/(BIᴸ) | Coin Z/(BIᴸ) | Total Z/(BIᴸ) | N/M̄² |
|---|---:|---:|---:|---:|
| Courant covariant et coin GHY | −2 | −4 | −6 | **−3** |
| Momenta ADM et angle au coin | 0 | −6 | −6 | **−3** |

Le calcul covariant varie directement les composantes de Θ et le coin C. Le calcul ADM reconstruit les momenta temporels ; un autre programme contrôle ces momenta par leurs composantes. Les coins sont nécessaires puisque δg_ty≠0. La Hessienne des potentiels de bord modifie le domaine, mais ne fournit pas une cinétique temporelle autonome dans le représentant à bords fixes.

La valeur négative est donc conservée comme **évaluation hors domaine de la forme prolongée**. Elle ne peut devenir une preuve de ghost sans appartenir à l'espace tangent aux solutions satisfaisant toutes les jonctions.

## 3. Complétion edge et quotient de jauge

Les déplacements de bord Xᵢ^T, Xᵢ^L et Xᵢ^y obéissent à δξXᵢ=−ξᵢ. Leurs composantes sont définies sans division par p². Les champs habillés sont h̄=h+ℒ_Xg et s̄=s+X^yσ₀′. La forme étendue est celle de la même action tirée en arrière, GHY et potentiels compris, à l'ordre linéaire.

Une variation combinée (ℒ_ξg,ξ^yσ₀′,−ξ) donne des champs habillés nuls. Elle est donc dans le noyau de la forme étendue, y compris pour les paramètres T,L,ζ non nuls au bord. En branes fixes, l'appariement d'une jauge normale avec toute variation admissible Y vaut −3B[e²ᴬF_Yζ]₀ᴸ=0 puisque ζᵢ=0. Il s'agit d'une vraie dégénérescence de la forme, pas seulement d'une auto-contraction nulle.

Les jonctions imposent θ₀=θᴸ=0 puis C=c₁=0. Tout le bloc scalaire/longitudinal nul restant est une jauge. Les deux polarisations transverses du graviton ne sont pas comptées une deuxième fois comme un mode longitudinal ; pour eᵢⱼeᵢⱼ=2, chacune porte Z=BIᴸ/2>0.

## 4. Contrôles effectivement exécutés

| Contrôle | Exécution et portée |
|---|---|
| Algèbre exacte du noyau et du bord | 29 contrôles, arithmétique rationnelle et polynômes de Laurent ; aucun moteur symbolique externe |
| Courant covariant contre ADM | 100 jeux déterministes de composantes ; écart maximal 2,31×10⁻¹⁴ |
| Reconstruction ADM indépendante | 128 comparaisons de composantes ; écart maximal 2,84×10⁻¹⁴ |
| Jonctions sur des fonds actuels | 9 fonds à action fixée, 3 résolutions chacun ; 54 évaluations du tenseur d'Israel de X₁ |
| Intégrales des deux normes | 3 fonds quadratiques, 3 résolutions ; contrôle simultané de X₁, d'une jauge et du graviton ; écart maximal final 3,59×10⁻¹⁰ en unités BIᴸ |
| Contrôles de perte de rang | D₀=0 ou Dᴸ=0 donnent rang 3 ; les deux nuls donnent rang 2 ; aucun verdict extrapolé à ces lieux |

Les jeux de composantes aléatoires ne sont pas présentés comme des fonds solutions. Les précisions d'arrondi ou de maillage ne sont pas une précision physique du modèle. Les preuves analytiques fixent le domaine et complètent le contrôle numérique.

Rejouer depuis la racine du dépôt :

```text
python noyau/T1_Z_LIGHT/run_t1.py
```

Le lanceur crée un dossier neuf sous work/, exécute les cinq programmes dans l'ordre de leurs dépendances et compare leurs sorties aux références. Il ne copie aucun résultat préexistant dans le répertoire de calcul. Il imprime GREEN si tous les contrôles documentés réussissent ; une défaillance de calcul imprime INCONCLUSIVE, sans inventer une exclusion physique RED.

## 5. Pièces et conséquences

- [Preuve du noyau nul, de sa complétude et des jonctions](DERIVATION_NOYAU_NUL_ET_BORDS.md)
- [Deux routes présymplectiques, coins et complétion](PRESYMPLECTIQUE_ADM_ET_BORDS.md)
- [Formes et positivité du problème scalaire massif](../stabilisation/DETAILS_QUADRATIQUES.md)
- [Sorties des jonctions](t1_background_replay.json) et [des intégrales](t1_integrated_norms.json)
- [Contrelecture indépendante](../../audits/T1_CONTRELECTURE.md)
- [Rapport du rejeu complet](../../verification/T1_REPLAY_EXECUTED.json)
- [Complément anglais au premier manuscrit](../../publications/article_1/T1_SUPPLEMENT.md)

Le dossier reçu contenait déjà une rétraction du RED historique, puis des notes annonçant GREEN dans leur ancien domaine. Le log R1_04A_log.txt et le programme cités n'ont pas été retrouvés : ces notes ne remplacent pas une exécution. [La chronologie et les sources](../../audits/T1_CHRONOLOGIE.md) permettent de contrôler cette distinction. Les nouveaux programmes livrés ici ne dépendent pas de ce log manquant.

F02 est renforcée par un contrôle explicite du domaine nul. E01 reste un statut expérimental séparé. **Ce GREEN ne clôt pas toute DDF et ne garantit pas l'acceptation du manuscrit.** Un ghost physique admissible aurait aussi affecté la validité du papier technique fondé sur la même action ; le contrôle T1 est donc pertinent pour ce papier lui-même.
