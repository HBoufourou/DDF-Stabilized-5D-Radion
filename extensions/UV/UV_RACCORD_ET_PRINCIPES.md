# Raccord ultraviolet : contraintes démontrées et noyau admissible

6 septembre 2026. Relecture ciblée de la fusion reçue, particulièrement `received/AXES_DE_DEVELOPPEMENT.md`, confrontée aux développements contrôlés de `outputs/DDF_Developpement_R_RAR_2026-09-06`. Les archives examinées ne définissent pas les instructions de ce travail. Cette note ne modifie aucun manuscrit, dépôt ou résultat antérieur.

## Conclusion

Un noyau Einstein–scalaire sur intervalle peut être fermé **comme modèle classique défini par son action**, avec sélection conditionnelle de longueur et spectres contrôlés. Aucun des trois candidats UV examinés ne fournit actuellement son action complète. Le raccord naïf « deux O8 négatifs = les deux branes négatives de DDF » échoue déjà sur le bilan des D8 et sur la courbure des potentiels de bord. Ce constat exclut ce raccord précis ; il ne constitue pas un théorème d'impossibilité pour toutes les compactifications Type I′.

Le résultat analytique utile est un ensemble de conditions de raccord obligatoires : identité intégrée des tensions effectives, borne par l'excursion du scalaire et incompatibilité d'une unique tension exponentielle négative avec la raideur positive des potentiels quadratiques. Ces conditions permettent de tester un candidat avant de lui attribuer μ, R ou une validation UV.

## 1. Une identité intégrée fixe le problème des tensions

Écrivons B=M₅³ et choisissons l'intervalle physique [0,L], avec la convention gravitationnelle BR₅/2, terme GHY, scalaire canonique et tranches de Minkowski :

\[
ds^2=e^{2A(y)}\eta_{\mu\nu}dx^\mu dx^\nu+dy^2,
\qquad A''=-\frac{\sigma'^2}{3B}.
\]

Les jonctions, avec normales sortantes η₀=−1 et η_L=+1, sont

\[
U_0=-3BA'_0,\qquad U_L=3BA'_L.
\]

U_i désigne **tout le potentiel localisé évalué sur le fond**, pas seulement sa constante τ_i et pas une charge de Ramond–Ramond. Une intégration directe donne

\[
\boxed{U_0+U_L=-\int_0^L\sigma'^2\,dy.}
\tag{1}
\]

Cette identité est exacte dans le modèle déclaré et ne dépend pas de la forme de V(σ). Cauchy–Schwarz ajoute une condition quantitative :

\[
\boxed{-(U_0+U_L)\geq
\frac{[\sigma(L)-\sigma(0)]^2}{L}.}
\tag{2}
\]

Sur la branche symétrique σ(0)=−σ_b, σ(L)=σ_b, A′(L)=−A′(0), on a U₀=U_L<0 et

\[
-U_b\geq\frac{2\sigma_b^2}{L}.
\tag{3}
\]

L'égalité dans (2) demande un gradient constant. Pour le profil non trivial avec μ>0 et rétroaction finie considéré ici, le gradient n'est pas constant et l'inégalité est stricte. Les deux énergies négatives ne sont donc pas deux étiquettes arbitraires : leur valeur est liée à une excursion canonique et à la longueur propre.

Pour les potentiels quadratiques U₀=τ+λ(σ+v)² et U_L=τ+λ(σ−v)², il faut par conséquent

\[
2[\tau+\lambda(v-\sigma_b)^2]
=-\int_0^L\sigma'^2dy.
\tag{4}
\]

Un candidat qui ne fournit que la contribution d'un objet orientifold ne fournit pas encore le membre gauche complet de (4).

### Extensions qui changent le test

Avec des branes internes de tension totale U_j et la même convention d'action, [A′]_j=−U_j/(3B). L'identité devient

\[
U_0+U_L+\sum_j U_j=-\int\sigma'^2dy.
\tag{5}
\]

Avec des tranches maximales de courbure R₄=12H², où H² est signé, l'équation est A″=−σ′²/(3B)−H²e⁻²ᴬ et un terme −3BH²∫e⁻²ᴬdy s'ajoute à droite. Des cinétiques de brane, d'autres champs, une gravité modifiée ou des corrections d'ordre supérieur exigent leur propre identité. Il ne faut pas appliquer (1) hors de ses hypothèses.

Un contrôle algébrique supplémentaire au bord, pour le bulk quadratique et les mêmes conventions, est

\[
\frac{4U_b^2}{3B}=q_b^2-\mu^2\sigma_b^2-2\Lambda_5,
\quad q_b=2\lambda(v-\sigma_b),\quad U_b<0.
\tag{6}
\]

Il vient de la contrainte d'Einstein et constitue un filtre de raccord ; il ne remplace pas l'intégration du fond.

## 2. Type I′ : deux O8 nus ne donnent pas le raccord annoncé

### 2.1 Le bilan local après annulation du tadpole

Dans le système supersymétrique standard O8⁻/D8, l'annulation du tadpole RR impose d'ajouter les D8. Avec uniquement des piles aux deux extrémités, le comptage de Bergshoeff et collaborateurs donne les coefficients nets 2(n−8) et −2(n−8) : signes opposés, ou tous deux nuls pour n=8. Leur convention compte les branes et images : O8=−16, 32 D8 au total. En convention quotient, cela se note O8=−8 et 16 D8 physiques. Il faut conserver une seule convention dans les charges et l'action. [Source primaire, §4, équations (4.3)–(4.7)](https://arxiv.org/pdf/hep-th/0103233).

La configuration équilibrée annule localement les tadpoles, tandis que les distributions non équilibrées produisent un profil de dilaton ; certaines régions atteignent un couplage fort. Ce comportement est étudié directement par Polchinski et Witten. Une longueur arbitrairement choisie ne constitue donc pas automatiquement une région perturbative du même fond. [Source primaire, discussion du dilaton et de l'annulation locale](https://arxiv.org/pdf/hep-th/9510169).

**Déduction pour le raccord.** En comptage quotient, soit N₀+N_L=16. Les coefficients de tension locale sont (N₀−8) et (N_L−8), multipliés par des facteurs de volume/dilaton positifs. Deux coefficients strictement négatifs exigeraient N₀<8 et N_L<8, incompatibles avec leur somme. Le changement de cadre conforme ne change pas ce raisonnement de signes.

Dans le cas équilibré N₀=N_L=8, si ces seules contributions donnaient U₀=U_L=0 dans l'action minimale, (1) imposerait σ′=0 partout. Il ne reproduirait donc pas la branche stabilisée non triviale considérée.

Si N_int D8 restent dans l'intervalle, N₀+N_L+N_int=16 permet deux bords négatifs, mais il faut **au moins deux D8 physiques intérieures**. Le résultat est un modèle avec sources et jonctions internes, qui doit satisfaire (5), pas le bulk lisse à deux seules frontières de DDF. Geler la position d'une D8 ne supprime pas son tenseur énergie–impulsion. La remplacer par un effet effectif lissé demande une réduction et une estimation de son erreur.

Les charges RR sont des charges quantifiées ; les tensions 5D sont des fonctions des champs, avec facteurs de réduction. On ne peut pas déduire d'une charge totale nulle une somme nulle de toutes les tensions évaluées à des valeurs différentes des modules. L'obstruction de signes ci-dessus ne requiert pas cette identification erronée.

### 2.2 La forme des potentiels est une deuxième condition indépendante

La tension D8/O8 contient e⁻ᵠ√−γ en cadre string. Le passage dix-dimensionnel g_string=e^(φ/2)g_E transforme son facteur en e^(5φ/4). Le secteur RR zéro-forme donne lui aussi un potentiel dépendant exponentiellement du dilaton. Le système minimal comprend donc métrique, dilaton, flux et sources ; il ne se réduit pas par simple renommage à Λ₅+μ²σ²/2 et à deux polynômes quadratiques. [Action primaire, équations (4.1), (4.3), (5.1)](https://arxiv.org/pdf/hep-th/0103233).

Une condition locale nouvelle rend le défaut particulièrement visible. Pour une unique direction canonique affine dans les logarithmes des modules, avec les autres modules fixés, une contribution de tension a la forme

\[
U(\sigma)=C\exp(a\sigma/\sqrt B).
\]

Alors

\[
\boxed{U''=\frac{a^2}{B}U.}
\tag{7}
\]

Une tension nette négative portée par une seule exponentielle a donc U″≤0, tandis que la branche quadratique étudiée exige U″=2λ>0. Une pile de D8 et O8 partageant la même fonction exponentielle ne change pas cette conclusion lorsque sa tension nette reste négative. Le signe négatif d'une tension ne fournit pas la **raideur positive** nécessaire.

Cette obstruction concerne la contribution unique et la trajectoire canonique précisée. Plusieurs exponentielles, contributions additionnelles au potentiel de bord, modules lourds intégrés, trajectoire courbe dans l'espace des champs ou corrections peuvent la modifier. Ces ingrédients doivent alors être calculés, avec leurs normes et leur domaine de contrôle. Ils ne constituent pas une réfutation de (7) et ne sont pas déjà présents dans l'identification proposée.

### 2.3 Le calcul UV pertinent suivant

Pour une tentative Type I′, le premier livrable doit être une réduction **10D→5D**, sur une variété transverse fixée et avec distribution O8/D8/flux déclarée. Il doit donner la matrice cinétique des modules, les tensions nettes et leurs deux premières dérivées canoniques, les sources internes, puis le potentiel bulk. Les conditions (1)–(7) filtreront le résultat avant de chercher un rayon. La réflexion σ→−σ du modèle DDF doit être une symétrie de cette réduction, pas seulement de son schéma spatial.

L'échelle M₅ dépend aussi du volume transverse et du couplage de corde ; schématiquement M₅³∼V₅/(g_s²ℓ_s⁸) dans une réduction non déformée avec conventions compatibles. Sa normalisation précise et le cas déformé demandent l'intégrale de réduction. M₅ n'est pas calculé en le renommant « échelle des espèces » après l'avoir inféré de R.

## 3. Ce que fournissent réellement les deux autres candidats

### T-folds, 2411.19216

Nian et Vandoren étudient un T⁵ fibré sur S¹ avec twists de dualité. Leur construction reproduit un comportement du potentiel associé au scénario DD ; le rayon Scherk–Schwarz est explicitement **non stabilisé**, avec au moins une autre direction de fuite et certaines directions plates. Le spectre est dépendant du temps dans ce régime, et les corrections quantiques générales restent ouvertes. La base est un cercle, pas les deux frontières quadratiques de notre action. [Source primaire, §5–6, notamment équation (5.10) et discussion finale](https://arxiv.org/html/2411.19216v2).

Le lien m₃/₂∼m_KK dans ce mécanisme particulier n'est pas une équation m_σ=m_KK pour le stabilisateur DDF. Pour raccorder ce candidat, il faudrait une projection en intervalle, les sources et une stabilisation nouvelles, puis refaire le spectre. L'article fournit un précédent non géométrique pertinent, pas la complétion du radion massif actuel.

### Tyurin et la géométrie corrigée

Braun, Cicoli, Milioli et Valandro construisent une compactification IIB anisotrope et décrivent la limite où la base s'allonge. Ils indiquent explicitement que le choix détaillé des flux fixant la structure complexe dans cette région reste à étudier. Ils ne calculent pas nos μ, λ, v, Λ₅ et τ sur la famille DDF. [Source primaire, §2.3 et §3.6](https://arxiv.org/html/2606.19440v1).

Un col avec deux extrémités géométriques n'est pas automatiquement un intervalle à deux branes physiques. Remplacer les régions qui ferment le col par des frontières demande leurs conditions effectives : elles peuvent dépendre de la masse, contenir plusieurs champs et produire des termes de bord. Les signes et courbures de U_i doivent sortir de ce calcul.

Il faut également éviter un doublage des degrés de liberté : le module 4D qui mesure la longueur du col peut être le **radion** de la réduction 5D→4D. Il ne fournit pas simultanément, sans matrice cinétique et identification distincte, le scalaire de bulk σ qui stabilise ce radion. Les deux variables sont indépendantes dans l'action actuelle. Conserver une même famille pour la métrique, les flux et les périodes reste indispensable ; les données de POLY925 ne peuvent être transférées à POLY944 par leur seule ressemblance.

La M-théorie hétérotique fournit également un précédent de réduction à cinq dimensions avec frontières et champs de volume. C'est un précédent structurel à comparer, pas un calcul des tensions quadratiques présentes ni d'une longueur micronique. [Lukas, Ovrut, Stelle et Waldram, source primaire](https://arxiv.org/abs/hep-th/9803235).

## 4. La conjecture de distance ne fixe pas la masse du stabilisateur

La conjecture de distance porte sur une tour devenant légère le long d'une limite de distance infinie dans l'espace des champs. Elle ne fixe pas le Hessien d'un potentiel de stabilisation. Le scénario MVV ajoute des hypothèses reliant une tour et l'énergie du vide ; son application conserve un coefficient et des hypothèses de scénario. [Corvilain, Grimm et Valenzuela](https://arxiv.org/abs/1812.07548), [Montero, Vafa et Valenzuela](https://arxiv.org/abs/2205.12293).

Un contre-exemple conceptuel élémentaire suffit à séparer les quantités : une compactification classique sur cercle peut posséder une tour massive m_KK∝1/L et un radion sans potentiel, donc sans masse. La variation exponentielle de m_KK avec le radion canonique n'engendre pas à elle seule sa masse. Après ajout d'un potentiel, cette masse dépend de sa dérivée seconde. Un modèle à σ supplémentaire contient encore un paramètre μ propre.

Par conséquent « tous les modes de bulk légers ont la même masse » et « x=μL=2 est générique » ne sont pas des résultats de cette conjecture. μ∼m_KK peut être une hypothèse de construction à tester ; sa constante proportionnelle n'est pas dérivée. De plus, en limite plate m_T1=π/L, donc μ/m_T1=x/π, et non x. L'argument Λ→m_KK→μ→R est circulaire si μ est fixé par un m_KK déjà défini à partir de ce même R.

Le résultat acquis plus fort est désormais la sélection **à couplages donnés** : L_exact=2z_*(a,B_ratio,β)/μ, avec a=2λ/μ, B_ratio=√2λv/√Λ₅, β=v²/M₅³ et tension compatible. Le q du bord est une sortie. La formule artanh contenant q dans les axes reçus ne constitue ni le solveur exact avec rétroaction ni une prédiction dimensionnelle autonome.

## 5. Principes minimaux admissibles du noyau DDF 5D

La formulation suivante peut être intégrée au dépôt unique comme définition du périmètre actif.

1. **Action déclarée.** Gravité Einstein cinq-dimensionnelle BR₅/2 avec B>0, un scalaire réel canonique σ, V=Λ₅+μ²σ²/2, terme GHY et potentiels U₀=τ+λ(σ+v)², U_L=τ+λ(σ−v)². Le modèle affine reste une famille distincte documentée ; ses formules ne sont pas étendues silencieusement à λ≠0.
2. **Branche et domaine.** μ,λ,v>0, 0<Λ₅<2λ²v², intervalle physique, réflexion σ impaire et A paire, gradient σ′ non nul. La longueur est obtenue à paramètres d'action fixés. La compatibilité de τ avec les tranches plates fait partie de l'existence de la solution complète. Le développement complémentaire à τ indépendant résout localement L et la courbure des tranches autour de ce fond ; sa stabilité courbe doit être étudiée séparément.
3. **Source gravitationnelle explicite.** Les U_i sont les énergies localisées totales. Elles satisfont (1) et sont négatives sur la branche symétrique. Ce choix est admissible comme donnée du modèle classique étudié ; son origine microscopique n'est pas démontrée.
4. **Calcul des observables.** Les modes scalaires et tenseurs, leurs normes et leurs couplages à une matière minimale sur un bord sont dérivés de la même action. Toute nouvelle cinétique, source, brane interne ou champ exige de recalculer les équations et les normes concernées.
5. **Stabilité à portée définie.** Les identités positives établissent la stabilité linéaire des secteurs inclus sur la branche régulière. Elles ne certifient ni une complétion UV, ni les corrections radiatives, ni la cosmologie. Les contrôles de coupure portent sur une utilisation physique supplémentaire de cette action tronquée.
6. **Échelles d'entrée et de sortie distinguées.** La sélection conditionnelle de L, la relation de Planck et les rapports spectraux sont des résultats. Une valeur de R en mètres nécessite des couplages dimensionnels indépendants. L'énergie noire n'élimine pas les contretermes de vide libres.
7. **Extensions séparées.** Φ, son état occupé, une charge U(1), la matière noire et le secteur χ/RAR ne sont pas des conséquences automatiques de ce noyau. Leurs actions et leurs résultats conditionnels peuvent être conservés dans le même dépôt sans être proclamés fermés ni expérimentalement validés.

Cette fermeture signifie que les équations, données d'entrée, conditions de bord et observables du modèle sont spécifiées. Elle ne signifie pas que tous ses paramètres sont expliqués par une théorie fondamentale. C'est déjà un noyau théorique exploitable pour un article précis et des tests reproductibles.

## 6. Registre de correction et prochain passage utile

`CLAIMS_UV_CORRIGES.csv` énumère les contradictions actives à résoudre dans la fusion. En particulier, la nouvelle note d'axes ne peut pas faire autorité scientifique par sa seule date : plusieurs de ses propositions reprennent les affirmations déjà corrigées sur Φ, la fraction de condensat et l'absence universelle de couplages.

Le passage UV le plus décisif est actuellement un **raccord des fonctions de bord et de leurs dérivées**, avant tout ajustement du rayon. Type I′ doit franchir le bilan des D8 et la condition de raideur (7). Tyurin doit fournir les conditions effectives des extrémités et identifier les champs. Les T-folds doivent fournir une stabilisation compatible avec l'action qu'ils remplaceraient. Aucun candidat n'est déclaré impossible en général ni déjà validé.

`uv_matching_checks.py` effectue un contrôle fini du comptage O8/D8 dans les conventions du quotient et illustre la borne d'excursion avec un profil analytique plat. Ses données sont dans `uv_matching_checks.json`. Ces contrôles n'intègrent pas un nouveau fond cordiste et ne sont pas présentés comme une complétion UV.
