# Méta-audit DDF R1–R62 et stratégie de récupération

**Date :** 4 septembre 2026  
**Portée :** série publique DDF I–VIII, dépôt GitHub, archive Zenodo, essai DDF_v3 joint, registres et scripts R11–R62 retrouvés.  
**But :** déterminer ce qui est démontré, ce qui doit être corrigé, et quelle nouvelle chaîne de preuve peut encore préserver l’idée d’un rayon micrométrique \(R\), d’une tour physique et, plus tard seulement, du plan de Fano.

## 1. Verdict exécutif

La conclusion honnête n’est ni « tout est faux », ni « la théorie est déjà prouvée ».

1. **La version unifiée des huit articles n’est pas démontrée.** Le rayon \(R=8{,}2\,\mu{\rm m}\), la tour d’Airy à un seul scalaire, la matière noire, l’énergie sombre, la baryogenèse et le plan de Fano ne sont pas reliés par un même vide et une même action contrôlée.
2. **Une erreur décisive invalide l’ancienne tour d’Article II.** Le spectre annoncé entrelace les spectres de Neumann et de Dirichlet, donc deux domaines auto-adjoints différents. Le propre script public indique qu’un champ unique ne porte qu’une branche. Les nombres peuvent être reproduits, mais leur interprétation comme tour d’un scalaire unique est réfutée.
3. **La valeur exacte de \(R\) n’a jamais été dérivée.** R18 ajuste deux paramètres à deux cibles ; R20 démontre une sous-détermination par une orbite qui redimensionne aussi les coefficients, donc relie plusieurs théories ; R40 corrige l’identification \(A=d=R\). La valeur historique doit devenir un benchmark, pas une prédiction.
4. **Le noyau mathématique le plus fort arrive tard, surtout en R43–R62.** Il comprend une dégénérescence semistable de forme Tyurin, une couture K3 polarisée par \(U(2)\), une LMHS de type \(II_{18}\), une famille relative torique lisse/propre/projective en R62 et un no-go de parité O3/O7 bien délimité. Le qualificatif strict « Tyurin » reste soumis aux vérifications quasi-Fano de R63.
5. **Le no-go R62 ne détruit pas toute tour micrométrique.** Il exclut, sous ses hypothèses, une tour fermée D3/\(C_4\) issue d’une classe isotrope active et paire. Il n’exclut pas une tour KK gravitationnelle d’un éventuel col métrique long, si celui-ci est établi.
6. **La meilleure récupération est donc “DDF spectral”.** Une limite de forme Tyurin est un **candidat** pour produire un col long ; le rayon doit être défini par un spectre métrique encore à calculer ; la tour KK du graviton devient l’hypothèse physique prioritaire ; la tour BPS de Tyurin reste une question distincte dans le parent \(\mathcal N=2\).

En une phrase :

> **DDF peut être sauvée comme programme géométrique et spectral testable, mais pas en conservant toutes les anciennes identifications ni toutes les valeurs historiques.**

## 2. Ce que “sauver DDF” signifie désormais

Il faut séparer cinq objets qui avaient été progressivement confondus :

| Objet | Définition opérationnelle | État après R62 |
|---|---|---|
| \(t_{\rm alg}\) | paramètre complexe de lissage de la famille relative R62 | construit pour le modèle résolu issu de POLY944 |
| \(u_{\rm forme}\) | rapport de périodes ou paramètre de forme ou d’anisotropie | données partielles surtout sur POLY925, non transférables à R62 |
| \(R_{\rm met}\) | longueur propre de la direction longue | non calculée |
| \(R_{\rm spec}\) | rayon obtenu après calibration de la pente, des multiplicités et des conditions aux limites | non calculé |
| \(\gamma_{\rm BPS}\) | classe de charge/tube donnant éventuellement des états BPS | candidate dans le parent \(\mathcal N=2\) de POLY925 ; non reconstruite pour R62 |

La nouvelle chaîne doit être démontrée **séparément pour une géométrie fixée \(X\)** :

\[
\left(t_{\rm alg}^{(X)},u_{\rm forme}^{(X)}\right)
\longrightarrow g_{\rm CY}^{(X)}(t,J)
\longrightarrow \{\lambda_n^{\rm diagnostic}\}
\longrightarrow \ell_{\rm pente},
\]

puis, séparément,

\[
V_{\rm eff}^{(X)}(\mathcal V,\tau_s,\tau_{K3},t,S,U_i,\ldots)
\longrightarrow t_\star,J_\star
\longrightarrow R_{\rm phys}(t_\star,J_\star).
\]

Dans un vrai vide IIB fluxé/orientifoldé, une seconde étape est indispensable :

\[
(g_{\rm CY},\,A_{\rm warp},\,\phi,\,{\rm D7/O7},\,{\rm flux})
\longrightarrow \mathcal O_{\rm spin\,2}^{\rm pondéré}
\longrightarrow \{m_n^2\}
\longrightarrow R_{\rm phys}.
\]

Le Laplacien scalaire de la métrique Calabi–Yau non fluxée n’est qu’un diagnostic. Il ne remplace pas l’opérateur gravitationnel pondéré du fond gauchi.

À ce jour, \(t_{\rm alg}^{(944{\rm \,res})}\) vient de R62, tandis que plusieurs données de forme/périodes viennent de POLY925. Elles ne peuvent pas occuper la même chaîne. Pour DDF-KK, il faut reconstruire explicitement \(t_{\rm alg}^{(925)}\) compatible avec le fond choisi ; pour DDF-G, il faut calculer les périodes propres au modèle résolu.

On ne posera plus \(t=u=R\). On ne choisira plus \(R\) au début du calcul.

Pour un paquet effectivement unidimensionnel, la forme générale à comparer est

\[
\lambda_n \simeq c+a(n+\delta)^2.
\]

La quantité brute \(\ell_{\rm pente}=a^{-1/2}\) n’est pas encore une longueur géométrique. Pour un intervalle simple, \(a=\pi^2/L_{\rm eff}^2\), tandis qu’un cercle utilise une autre convention et d’autres multiplicités. Les conditions aux limites, le déphasage \(\delta\), les caps et le warping doivent fixer la conversion vers \(R_{\rm phys}\). Si aucun paquet stable ne suit une loi unidimensionnelle après ces contrôles, la branche DDF-KK du modèle testé échoue.

## 3. Pourquoi plusieurs IA ont pu confirmer une chaîne incorrecte

Les validations antérieures n’étaient pas nécessairement mensongères : elles validaient souvent une implication locale **si les hypothèses fournies étaient acceptées**. Ce n’est pas la même chose qu’une preuve indépendante du modèle complet.

Les mécanismes d’erreur observés ici sont concrets :

- **réutilisation des mêmes hypothèses** d’une conversation à l’autre, donnant une apparence de consensus sans indépendance réelle ;
- **reproductibilité confondue avec vérité physique** : un script peut reproduire exactement le nombre construit par ses entrées ;
- **deux opérateurs confondus avec une tour** : Neumann et Dirichlet ont été concaténés dans l’ancienne tour d’Airy ;
- **test de tachyon incapable de voir le signe** : le script auxiliaire local **r14_scan.py** applique \(\max(\lambda,0)\), donc ne peut pas servir de détecteur de valeurs propres négatives. Cela ne réfute pas l’identité d’énergie de la branche sans tachyon ; le côté produit positif dépend encore d’un signe WKB à détailler ;
- **ajustement présenté comme prédiction** : R18 utilise deux paramètres pour deux cibles ;
- **sortie réinjectée comme entrée** : des coefficients de brane sont reconstruits depuis la solution, puis la solution est citée comme témoin ;
- **objets de géométries différentes transportés sans morphisme** : flux, périodes ou charges de POLY925 ne se transfèrent pas automatiquement à POLY944 ou au modèle résolu \((5,85)\) ;
- **erreur de catégorie** : une orbite de monodromie n’est pas une tour d’états stables, et une charge centrale linéaire n’est pas un spectre KK ;
- **coïncidences dépendantes comptées comme confirmations indépendantes**. Par exemple,

\[
\frac{\hbar c}{8{,}2\,\mu{\rm m}}\simeq 24{,}1\,{\rm meV}.
\]

La proximité entre \(8{,}2\,\mu{\rm m}\) et \(24\,{\rm meV}\) est donc essentiellement la même relation \(m\sim1/R\), pas une seconde prédiction indépendante.

La règle à adopter désormais est simple : chaque résultat doit indiquer son **action**, son **domaine**, ses **entrées indépendantes**, son **observable**, son **test fatal** et la géométrie exacte à laquelle il appartient.

Ce méta-audit est lui-même assisté par IA. Il constitue une reconstruction contradictoire et traçable, pas une expertise indépendante. Une validation scientifique réelle exige une nouvelle dérivation humaine, un code indépendant, une recherche d’antériorité complète et un referee externe compétent.

## 4. Échelle de preuve utilisée

| Niveau | Qualification | Exigence |
|---|---|---|
| A | démontré dans le domaine annoncé | preuve analytique ou certificat exact, hypothèses explicites, pas de contradiction active |
| B | calcul reproductible mais borné | code reroulé, résultat limité à un modèle/scan clairement défini |
| C | candidat conditionnel | dépend de données globales, de stabilité ou d’un secteur non construit |
| D | ajustement ou motivation | utile pour orienter, mais pas une prédiction |
| E | réfuté, rétracté ou non traçable | contradiction, résultat supersédé, ou artefact primaire absent |

Le registre exhaustif associé contient une ligne pour chaque R. Deux historiques différents portent les numéros R37 et R38 ; ils sont donc séparés en **R37/R38-HM** et **R37/R38-IIB**.

## 5. Révision des huit articles publics

| Article | Idée centrale | Verdict après R62 | Ce qui peut rester |
|---|---|---|---|
| I | EFT 5D, Casimir, \(R=8{,}2\,\mu{\rm m}\) | architecture conditionnelle ; valeur non dérivée ; durée de vie sans solution de bounce ; \(w\) sans EFT cosmologique/solution FRW | seulement les sous-résultats explicitement redérivés : motivation dimensionnelle et relation de Planck conditionnelle |
| II | un scalaire dans un puits linéaire produit la tour entrelacée | **interprétation monoscalaire réfutée** | chaque branche d’Airy seulement comme spectre mathématique d’un opérateur choisi ; un nouveau modèle relativiste à deux secteurs demanderait un audit complet |
| III | tour supérieure comme réservoir de matière noire et fondamental comme médiateur | **à mettre en quarantaine** : transition, cascade, condensat, RAR, taux et screening ne sont pas dérivés d’une même EFT | aucune revendication physique avant une vraie tour, une cinétique microscopique et une équation de Boltzmann |
| IV | échelle “ombre” et convergence de plusieurs nombres | les “six origines” partagent largement \(R\), \(m_\Phi\), le puits ou une échelle supposée ; pas une preuve | section historique/motivation, sans langage de prédiction ni facteur de boucle non calculé |
| V | plongement Type I′, identités de normes, candidat POLY3181 | branche historique supersédée par les audits géométriques ultérieurs | méthodes de contrôle de normes et leçons négatives |
| VI | géométrie fixant \(R\), énergie sombre et inflation K3 | \(R\) et la cosmologie ne sont pas dérivés dans un même vide | mécanisme LVS/Tyurin-type comme programme R65–R68 |
| VII | sept classes organisées par le plan de Fano | structure combinatoire, pas mécanisme dynamique | travail séparé après preuve de \(R\) et de la tour |
| VIII | baryogenèse par winding du vide | conditionnel à une normalisation microscopique absente | projet indépendant, après stabilisation et spectre |

Pour l’Article I, les facteurs historiques “65 sous la sensibilité” et “exclusion \(\times258\)” ne sont pas publiables sans courbe expérimentale officiellement numérisée et sans signal total tour + radion/scalaires.

Pour l’Article III, les défauts sont indépendants de la seule erreur d’Airy : la suppression \(e^{-10^{24}}\) d’une transition n’est pas dérivée, une interaction quartique n’implique pas à elle seule une cascade vers un condensat, l’occupation de phase ne fixe pas le couplage, la RAR est ajustée plutôt que déduite, et le screening de \(\Phi\) ne supprime pas automatiquement les réponses radion/KK.

**Décision éditoriale :** ne pas tenter de réparer les huit articles simultanément. Les figer comme archive datée, publier une note claire de corrections, puis reconstruire deux manuscrits plus étroits.

## 6. Résultat du méta-audit R1–R62

### 6.1 R1–R13 — EFT initiale, tour d’Airy et secteur nul

Attention à la nomenclature : le jalon « R1 eigenmode » et les fichiers **R1_\*** consacrés plus tard à la stabilité sont deux historiques différents. La correction du ghost ne certifie pas la tour d’Airy.

- **R1 :** les deux suites d’Airy sont reproductibles, mais leur entrelacement appartient à deux opérateurs. La tour monoscalaire est retirée.
- **R2–R8 :** l’EFT et certaines réductions sont conditionnelles ; \(R\) reste une entrée ; la naturalité et l’unification par \(\Phi\) ne passent pas. L’inventaire public mélange en outre \(\Phi\), le champ source \(\sigma\) et un stabilisateur éventuel : la stabilité du dernier ne certifie pas automatiquement l’action publique I–II.
- **R9 :** la discipline “pas de réparation ad hoc” reste une très bonne règle méthodologique.
- **R10 :** aucun certificat autonome n’a été retrouvé ; statut non traçable.
- **R11 :** l’antériorité réduit fortement la nouveauté annoncée du secteur scalaire.
- **R12–R13 :** la correction du faux ghost \(X_1\) et le quotient du noyau nul sont dérivés dans l’action et le domaine internes, pour des branes fixes et des endpoints génériques. Les journaux R1 originaux n’étant pas tous disponibles, ce n’est pas une validation universelle. Ils ne fixent ni \(R\), ni l’UV, ni la cosmologie.

**Acquis récupérable :** une note technique bornée sur les jonctions et le noyau nul.  
**À retirer :** la tour entrelacée d’un scalaire unique et toute phénoménologie qui en dépend.

### 6.2 R14–R21 — stabilité 5D et tentative micrométrique

- **R14 :** critère spectral conditionnel intéressant dans l’action minimale à un scalaire, avec \(U_i''=0\), \(\sigma'_0\neq0\) et endpoints génériques. L’identité d’énergie traite la branche sans tachyon ; le signe WKB utilisé pour l’existence d’un tachyon quand le produit est positif doit devenir un lemme détaillé ; la surface marginale reste ouverte. Le clipping du script auxiliaire n’invalide pas le côté identité d’énergie. Le critère monotone est déjà connu chez Lesgourgues–Sorbo ; seules l’identité régulière et l’extension non monotone peuvent encore être nouvelles après recherche.
- **R15–R16 :** sous-détermination et témoins numériques ; les coefficients de brane ne sont pas indépendants.
- **R17 :** \(L\simeq\pi R\) est surtout une convention spectrale quasi plate.
- **R18 :** témoin ajusté, deux paramètres pour deux cibles, proche d’une frontière marginale.
- **R19 :** confrontation expérimentale limitée au secteur TT ; il manque le propagateur matière–matière complet, invariant de jauge, avec tous les scalaires légers, mélanges métriques et conditions de source aux bords.
- **R20 :** résultat négatif fort mais borné : l’orbite d’échelle change les coefficients dimensionnés, donc relie une famille de théories. Elle démontre la sous-détermination tant que la microphysique ne fixe pas ces coefficients ; ce n’est pas une direction plate d’une action fixée.
- **R21 :** BVP utile mais paramètres encore hérités de cibles ; il obtient une réponse locale \(k>0\) autour d’une racine reconstruite, pas un vide de Sitter global avec spectre courbe stable.

**Acquis récupérable :** laboratoire 5D et méthodes spectrales.  
**Test obligatoire :** réponse linéaire complète et invariant de jauge, sans double comptage du bending, avec coefficients fixés avant la résolution.

### 6.3 R22–R38-HM — branche Hořava–Witten/hétérotique

- **R22–R25 :** l’intervalle hétérotique est une architecture distincte, pas une dérivation de l’action DDF. Le benchmark R24 produit une longueur environ \(26{,}3\) ordres sous \(8{,}2\,\mu{\rm m}\).
- **R26–R34 :** plusieurs no-go bornés et calculs de cohomologie sont utiles, mais aucun même vide ne ferme \(R\), matière noire et énergie sombre.
- **R35–R38-HM :** l’étoile SU(4) et les scans CAD sont une branche mathématique incomplète ; la couverture n’autorise pas un no-go global. R37-HM/R38-HM ne sont actuellement traçables que par un rapport secondaire : leurs codes et rapports primaires doivent être récupérés avant citation.

**Acquis récupérable :** résultats négatifs bornés sur le Schoen, surtout le no-go SU(3) R34, et conventions corrigées.  
**Décision :** arrêter cette branche comme voie principale vers le micron ; éventuel article négatif séparé après restauration des artefacts primaires. DDF-HM ne doit plus être présenté comme l’UV de R18 sans un uplift et un BVP communs.

### 6.4 R37-IIB–R42 — pivot Type IIB et sélection géométrique

- **R37-IIB :** POLY1185 est un candidat anisotrope mais sans del Pezzo **torique** diagonal répertorié et avec 236 modules ouverts. Le scan primitif \(\pm12\) mentionné dans le rapport n’est pas présent dans le script retrouvé.
- **R38-IIB :** le scan sélectionne POLY1176 avec K3, dP8 et orientifold ; le bloc de flux reste abstrait et \(R=0{,}1\,\mu{\rm m}\) est une cible.
- **R39 :** chambre de Kähler et trajectoire de contraction indépendante du dP8 dans la chambre torique héritée sont utiles ; contraction physique complète, E3/Pfaffien et modes chargés ne sont pas fermés.
- **R40 :** correction essentielle : le saxion \(A\), le module kählérien \(d\) et le rayon physique \(R\) ne sont pas identiques. Le type \(II_2\) concerne ici la monodromie de grande structure complexe du miroir associée à \(d\to\infty\) ; il ne doit pas être confondu avec la limite de Tyurin \(II_{18}\) ultérieure.
- **R41 :** potentiel LVS importé compatible comme mécanisme, mais winding non établi et coefficient de boucle résolu à rebours ; les données nécessaires ne sont pas dérivées pour POLY1176.
- **R42 :** pivot raisonnable vers CQSV POLYID 925 ; son identification torique avec Altman #1206 est exacte à une transformation \(GL(4,\mathbb Z)\), permutation et données SR près. Ses périodes et ses flux doivent toutefois être recalculés dans cette géométrie.

**Acquis récupérable :** entonnoir géométrique et mécanisme d’anisotropie.  
**Interdiction :** ne plus transporter un bloc de flux abstrait entre modèles.

### 6.5 R43–R53 — Tyurin, LMHS, réseaux et recollement

- **R43–R44 :** correction du paramètre primitif et obtention, sur le gradué et avec un marquage abstrait, du réseau
  \(U\oplus U(2)\oplus E_8(-1)^2\), avec facteurs de Smith \((1^{18},2,2)\). Le transport depuis une base globale de \(H^3(X,\mathbb Z)\) n’est pas construit.
- **R45–R46 :** candidats de flux locaux ; R45 tombe sur des hyperplans de racines, R46 les évite numériquement mais ne stabilise pas les 79 modules restants.
- **R47 :** identité de rang \(98=18+79+1\), pas une solution F-term ; la torsion éventuelle de \(H^3\) n’est pas calculée.
- **R48–R50 :** noyaux GKZ saturés et identité scalaire hypergéométrique exacte sur une tranche à huit points ; cela ne constitue ni la VHS intégrale globale ni des fonctions relatives complètes.
- **R51–R52 :** correction K-théorique importante ; retirer l’ancien argument de rang \(10+8+2\).
- **R53 :** distance asymptotique et monodromie sont des données Hodge ; elles ne prouvent pas une tour d’états.

**Acquis récupérable :** un noyau de réseau et une structure graduée Tyurin/\(II_{18}\)/\(U(2)\), à raccorder encore à \(H^3(X,\mathbb Z)\).  
**À retirer :** tout énoncé “orbite = tour KK” sans indice d’états ni spectre métrique.

### 6.6 R54–R62 — tour candidate, changements de modèle et no-go orientifold

- **R54–R55 :** une classe primitive isotrope et un tube local existent comme candidats ; stabilité à un corps et indice BPS non calculés.
- **R56 :** modularité de niveau 2 et classe orthogonale aux flux de l’ancien modèle ; \(h^{2,1}_+=0\) projette le vecteur fermé recherché.
- **R57–R58 :** scan d’involutions puis faux sauvetage par \(t\mapsto-t\) ; le verdict de tube pair de R58 est rétracté.
- **R59 :** POLY944 non résolu possède 16 points doubles ordinaires génériques.
- **R60 :** petite résolution crépante/projective et branche triple ; les anciennes classes de parité avaient été calculées sur la mauvaise surface.
- **R61 :** vraie couture \(U(2)\), LMHS \(II_{18}\), mais aucune classe isotrope active paire pour les involutions testées.
- **R62 :** famille relative 5D explicite, lisse/cohérente/propre, fibre centrale SNC à deux composantes et no-go O3/O7 ciblé. Les conditions quasi-Fano strictes, les périodes/GKZ propres au modèle résolu, la métrique, la tour et \(R(t)\) restent ouverts.

**Acquis récupérable :** meilleur candidat d’article mathématique.  
**À abandonner dans cette architecture :** la tour D3/\(C_4\) paire standard comme tour DDF en \(\mathcal N=1\).

## 7. Rétractions et corrections obligatoires

Ces points doivent apparaître explicitement dans toute nouvelle version ou note de corrections :

1. la tour d’Airy entrelacée n’est pas celle d’un scalaire unique ;
2. \(8{,}2\,\mu{\rm m}\) et \(24\,{\rm meV}\) ne sont pas deux confirmations indépendantes ;
3. le script auxiliaire tronqué ne peut pas justifier R14 ; l’identité d’énergie et le lemme WKB doivent être audités séparément ;
4. R18 est un ajustement, R19 un test TT seulement, R20 une non-identifiabilité ;
5. la branche hétérotique testée ne conserve pas l’échelle micrométrique ;
6. \(t_{\rm alg}\), \(u_{\rm forme}\), \(d\) et \(R\) sont distincts ;
7. les flux Q472/Q585 et \(C_{\rm safe}\) ne se transportent pas entre POLY925, POLY944 et le modèle résolu ;
8. retirer en R43 le paramètre \(z^4\) non primitif et le bloc \(\operatorname{diag}(2,4)\) non horizontal ; noter que Q464 laisse un mode complexe plat ;
9. retirer les interprétations supersédées de R51, R58 et R60 ;
10. une orbite de monodromie ou \(m(n\gamma)=n\,m(\gamma)\) n’est pas une tour KK ;
11. le no-go R62 est précis, non universel, et ne porte pas sur les modes gravitationnels d’un éventuel col métrique long.

Le no-go utilise six hypothèses qu’il faut conserver avec l’énoncé : involution holomorphe d’ordre deux de type O3/O7 ; famille et paramètre de lissage préservés ; polarisation \(L=U(2)\) stable avec une direction ample positive invariante ; cycle propre vecteur de l’involution ; classe isotrope dans le réseau actif orthogonal ; vecteur fermé issu de \(C_4/H^3_+\). Le scan fini est exhaustif pour les caractères diagonaux de signes dans l’ansatz Cox déclaré, pas pour toutes les involutions imaginables.

## 8. Ce qui justifie encore une cible micrométrique

La littérature ne fixe pas une unique “épaisseur du bulk” avec une définition commune. Elle parle selon les cas d’un rayon de compactification, d’une grande base, d’une longueur effective ou d’une dimension mésoscopique. Elle soutient néanmoins une **fenêtre de travail**, pas la valeur historique exacte :

| Référence | Résultat pertinent | Ce qu’elle ne prouve pas pour DDF |
|---|---|---|
| Cicoli–Burgess–Quevedo, JHEP 10 (2011) 119 | compactifications IIB/LVS avec deux dimensions micrométriques | ni une dimension unique, ni \(8{,}2\,\mu{\rm m}\) |
| Montero–Vafa–Valenzuela, JHEP 02 (2023) 022 | une dimension mésoscopique \(\ell\sim\Lambda^{-1/4}\sim10^{-6}\,{\rm m}\) dans le scénario Dark Dimension | la conjecture ne construit pas le vide DDF |
| Law-Smith–Obied–Prabhu–Vafa, JHEP 06 (2024) 047 | contraintes donnant une taille effective de l’ordre de \(1\) à \(30\,\mu{\rm m}\) | résultat conditionnel au scénario de gravitons décroissants |
| Obied–Dvorkin–Gonzalo–Vafa, Phys. Rev. D 109 (2024) 063540 | combinaison de contraintes favorisant environ \(1\) à \(10\,\mu{\rm m}\) | ne sélectionne pas la géométrie DDF |
| Braun–Cicoli–Milioli–Valandro, arXiv:2606.19440 | IIB/LVS avec une ou deux grandes dimensions ; Tyurin peut rendre la base effectivement 1D | réglages et pont métrique détaillé restent à contrôler |
| Blumenhagen–Paraskevopoulou, JHEP 07 (2026) 247 | autre route Hořava–Witten micrométrique, avec tadpoles symétriques proposés | ne répare pas automatiquement les no-go du benchmark DDF-HM |

Conclusion : utiliser d’abord une fenêtre mésoscopique externe \(L_{\rm cible}=O(1\!-\!10)\,\mu{\rm m}\), éventuellement élargie à \(30\,\mu{\rm m}\) pour les comparaisons. Elle ne devient un rayon spectral qu’après calibration des conditions aux limites, du facteur géométrique et de l’opérateur physique. La valeur calculée doit rester une sortie, jamais un filtre de sélection.

## 9. Architecture recommandée

### 9.1 DDF-G — noyau géométrique

Objet : modèle résolu de R62, couture K3, \(U(2)\), LMHS \(II_{18}\), famille relative et obstruction du tube isotrope fermé \(C_4\) dans l’ansatz O3/O7 testé.

Condition de publication :

- vérifier la définition stricte de Tyurin/quasi-Fano et la d-semistabilité ; un échec du seul mot « quasi-Fano » n’annule pas forcément un résultat plus étroit sur une dégénérescence semistable à couture K3 ;
- rerouler l’éventail, la lissité et le Jacobien dans un second système de calcul ;
- extraire un résultat original au-delà d’un exemple : théorème de construction, classification d’involutions ou no-go équivariant avec domaine précis.

Cette branche ne revendique ni micron, ni matière noire.

### 9.2 DDF-KK — branche physique prioritaire

Objet : tester l’existence d’une longue direction métrique finie et d’une tour KK gravitationnelle.

Le no-go \(C_4\) n’agit pas directement sur les fluctuations de la métrique. La projection orientifold et les conditions de bord devront tout de même être calculées ; elles ne doivent pas être supposées.

Pour éviter une nouvelle fusion de modèles, la plateforme rapide recommandée est **fixée à POLY925/#1206**. La géométrie R62 reste DDF-G tant que son propre vide n’est pas reconstruit.

| Branche | Identité à verrouiller dans un manifeste |
|---|---|
| DDF-G | résolution issue de POLY944, \((h^{1,1},h^{2,1})=(5,85)\), famille R62 ; le budget \(L=24\) appartient à la pile D7/O7 locale considérée, pas à la géométrie seule |
| DDF-KK rapide | Altman #1206 \(\simeq\) CQSV POLYID 925 / KSID 928, triangulation 14, \((4,98)\) ; \(L=758\) appartient à la configuration D7/O7 publiée, à distinguer de l’entrée brute D3W |

Avant tout calcul, un fichier manifeste doit fixer polytope, triangulation, phase, résolution, involution, configuration D7/O7, formule de tadpole et hash des données. Il doit aussi certifier que la famille de lissage choisie est compatible simultanément avec la triangulation 14, l’involution et cette configuration de branes ; l’isomorphisme du CY ne suffit pas à identifier le fond gauchi. Il est interdit de mélanger la géométrie R62 avec les flux ou périodes de POLY925. Construire DDF-KK sur R62 reste possible, mais cela exige de refaire périodes, flux, tadpoles, D7/O7 et stabilisation pour sa propre configuration.

### 9.3 DDF-BPS — branche parallèle dans le parent \(\mathcal N=2\)

Plateforme fixée : parent non orientifoldé \(\mathcal N=2\) de POLY925, où la classe isotrope candidate a été définie. La couture finale R62 ne possède pas encore de \(T^3\) global ni de classe physique correspondante.

Objet : déterminer si les multiples de cette classe isotrope correspondent à des états à un corps.

Preuve requise : dictionnaire miroir intégral, fonction génératrice ou théorème garantissant une infinité de classes non nulles, traitement réduit/rationnel des classes non primitives, chambre asymptotique de stabilité et loi de masse. Une liste finie de coefficients GV/DT sert de contrôle, pas de preuve d’une tour infinie. Cette branche peut réussir même si aucune descente BPS \(\mathcal N=1\) n’existe.

### 9.4 Branches différées

- tour ouverte D7 ou paire brane/image ;
- orientifold O5/O9 ;
- miroir IIA comme outil de calcul ;
- quotient CHL/niveau 2 exploitant \(U(2)\) et \((\mathbb Z/2)^2\).

Elles ne doivent pas être développées simultanément. Une seule sera choisie après les portes spectrales.

Le diagnostic F-théorie n’est pas une option concurrente : avant toute revendication O3/O7 \(\mathcal N=1\), il faut contrôler la position de l’O7 par rapport à la dégénérescence, les corrections à couplage fini et le co-scaling des modules de Kähler.

## 10. Feuille de route R63–R70

| Révision | Question | Livrable minimal | Critère d’arrêt |
|---|---|---|---|
| **R63 — Tyurin strict** | R62 satisfait-il toutes les hypothèses géométriques ? | cohomologies, anti-canonique, normal bundles comme fibrés, canonique relatif/log de la famille, d-semistabilité, Clemens–Schmid, second CAS | retirer le qualificatif strict si nécessaire ; arrêter seulement si aucun théorème semistable plus étroit ne survit |
| **R64 — substance** | le résultat dépasse-t-il un exemple connu ? | théorème/classification/no-go général, preuve et contre-exemples | pas d’Article 1 autonome sans nouveauté identifiable |
| **R65 — pilote spectral** | la chaîne numérique distingue-t-elle un cylindre 1D de faux positifs ? | opérateurs tests, caps/BC, 10–30 modes, au moins trois résolutions, compteur spectral | l’échec tue le pipeline ou l’ansatz semi-plat testé, pas encore la vraie géométrie |
| **R66 — vraie famille POLY925** | cette géométrie développe-t-elle le paquet voulu ? | diagnostic CY puis opérateur spin-2 gauchi, projection, localisation, gap et erreurs | garder cette route seulement si convergence et séparation des autres tours |
| **R67 — pont POLY925** | \(t_{\rm alg}^{(925)}\), périodes, métrique et longueur calibrée sont-ils reliés ? | loi avec incertitudes sur plusieurs trajectoires | retirer toute formule \(R(t)\) instable |
| **R68 — stabilisation étagée** | une troncature contrôlée sélectionne-t-elle une longueur, quelle qu’elle soit ? | hiérarchie d’intégration, potentiel et budget d’erreur, Hessienne, tadpole, gate F-théorie, couplages | aucune valeur micrométrique revendiquée si un paramètre clé est imposé ou une correction domine |
| **R69 — BPS parent** | la classe isotrope porte-t-elle une infinité d’états stables ? | dictionnaire miroir, génératrice/théorème d’infinité, invariants de contrôle et chambre asymptotique | pas de tour BPS sans non-annulation infinie et stabilité |
| **R70 — porte \(\mathcal N=1\)** | quelle unique architecture lourde poursuivre ? | matrice parité/tadpole/corrections/coût et un seul gagnant | si aucune passe, garder BPS en \(\mathcal N=2\) et la branche KK comme programme bosonique à compléter |

R63 et R65 peuvent commencer en parallèle. Le plan de Fano ne revient qu’après un succès de R64 et au moins un signal spectral en R65–R66.

## 11. Protocole numérique de R65

Le premier test ne doit pas attendre une métrique Calabi–Yau complète. Il valide une méthode numérique, pas DDF :

1. construire un modèle analytique ou semi-plat avec caps globaux, longueur et conditions aux limites contrôlées ;
2. choisir cinq valeurs du paramètre de lissage, espacées logarithmiquement ;
3. calculer le zéro-mode, les multiplicités et les 10 à 30 premières valeurs propres scalaires ;
4. refaire le calcul à au moins trois résolutions, avec extrapolation ou une seconde discrétisation indépendante ;
5. comparer \(a(n+\delta)^2+c\) aux lois concurrentes, sans assigner \(n\) après coup ;
6. comparer cercle, intervalle, mode de Cheeger/tunneling et excitations transverses ;
7. vérifier la fonction de comptage \(N(\lambda)\sim\sqrt{\lambda}\) sur une fenêtre contrôlée ;
8. inspecter les fonctions propres : elles doivent s’étendre le long du col, pas se localiser sur un cap ou un défaut numérique ;
9. quantifier le gap transverse selon un seuil préenregistré ;
10. contrôler la dépendance aux caps, aux conditions aux limites et au maillage ;
11. fixer avant le calcul les normes de résidu et tolérances du pilote ;
12. réserver le calcul spin-2 au fond global, avec l’opérateur pondéré approprié.

Le calcul physique doit rester à \(t=t_\star\neq0\), donc à distance finie. Les travaux récents sur les obstructions quantiques des limites infinies en \(\mathcal N=1\) rendent imprudent de faire dépendre DDF de la limite exacte \(t=0\).

## 12. Article 1 : écrire maintenant, soumettre après R63–R64

Il est utile de commencer le manuscrit dès maintenant comme structure de travail, mais pas de le soumettre avant les deux portes mathématiques.

**Titre provisoire :**

> *A resolved toric Tyurin-type degeneration with \(II_{18}\) LMHS and a closed-\(C_4\) isotropic-tube obstruction in the tested O3/O7 ansatz*

**Contenu autorisé :**

1. construction torique relative ;
2. lissité, propreté, projectivité et fibre SNC ;
3. couture K3, polarisation \(U(2)\) et LMHS \(II_{18}\), avec hypothèses de saturation/unipotence explicites ;
4. scan exact des relèvements diagonaux de signes/Cox dans l’ansatz déclaré, en distinguant ceux qui s’étendent à la famille ;
5. théorème/no-go du tube fermé \(C_4\) avec ses six hypothèses ;
6. fichiers de vérification et limites.

**Contenu à exclure :**

- \(R=8{,}2\,\mu{\rm m}\) ;
- tour KK ou BPS non calculée ;
- matière noire, énergie sombre, inflation, baryogenèse ;
- plan de Fano ;
- ancienne tour d’Airy.

Un second CAS contrôle le calcul, pas l’originalité. R64 exige donc une recherche bibliographique complète et l’avis préalable d’un géomètre externe. Si aucune nouveauté ne dépasse une instanciation connue, le résultat devient un appendice/dataset de DDF-KK et non un article autonome.

L’Article 2 éventuel serait physique et spectral :

> *Finite Tyurin necks and an emergent one-dimensional Kaluza–Klein spectrum in a stabilised Type-IIB compactification*

Il ne sera légitime qu’après R65–R68.

## 13. Stratégie vis-à-vis d’arXiv

Le refus reçu ne prouve pas que chaque calcul est faux ; il indique que le manuscrit soumis n’a pas été jugé suffisamment substantiel/original pour arXiv. Mais leur message interdit une simple resoumission et n’envisage un appel qu’après acceptation par une revue à comité de lecture avec DOI.

Conséquence pratique :

- ne pas renvoyer l’ancien Article III sous un autre titre ;
- publier une note publique de corrections sur Zenodo/GitHub ;
- obtenir d’abord un manuscrit étroit, une preuve centrale et un rapport externe ;
- viser la revue et le processus de peer review ;
- utiliser ensuite le DOI si un appel arXiv devient utile.

## 14. Décision immédiate

La prochaine étape n’est pas une nouvelle couche de spéculation. Elle comporte **deux travaux en parallèle**, sans renumérotation concurrente :

1. **R63 puis R64 :** fermer le statut Tyurin-type/strict et tester l’originalité de R62 ;
2. **R65 :** valider le pipeline spectral sur un modèle pilote.

Si les deux passent, DDF possède :

- un manuscrit mathématique candidat, prêt pour expertise externe ;
- un pipeline ouvrant une route physique vers \(R\) et une tour, pas encore une preuve du modèle ;
- une séparation propre entre preuve, cible phénoménologique et conjecture.

Si R65 échoue, il faudra abandonner ou réparer l’ansatz semi-plat et le pipeline testés. Seul un échec de R66 sur la vraie géométrie, ou une obstruction analytique, peut condamner l’interprétation “une dimension longue” de cette plateforme.

## 15. Artefacts et traçabilité

- registre exhaustif : **DDF_R1_R62_REGISTRE.csv** ;
- audits détaillés : **meta_audit/audit_R1_R13.md**, **audit_R14_R25.md**, **audit_R26_R38.md**, **audit_R39_R50.md**, **audit_R51_R62.md** ;
- comparaison indépendante des routes : **meta_audit/salvage_architectures.md** ;
- résumé décisionnel : **meta_audit/routes_summary.md**.

Ces audits sont des pièces de travail antérieures à la dernière relecture contradictoire. En cas de formulation divergente, le présent audit maître et la feuille de route corrigée font foi.

## 16. Références externes principales

1. M. Cicoli, C. P. Burgess, F. Quevedo, *Anisotropic Modulus Stabilisation: Strings at LHC Scales with Micron-sized Extra Dimensions*, JHEP 10 (2011) 119, [DOI](https://doi.org/10.1007/JHEP10(2011)119).
2. M. Montero, C. Vafa, I. Valenzuela, *The Dark Dimension and the Swampland*, JHEP 02 (2023) 022, [arXiv:2205.12293](https://arxiv.org/abs/2205.12293).
3. J. A. P. Law-Smith, G. Obied, A. Prabhu, C. Vafa, *Astrophysical Constraints on Decaying Dark Gravitons*, JHEP 06 (2024) 047, [arXiv:2307.11048](https://arxiv.org/abs/2307.11048).
4. G. Obied, C. Dvorkin, E. Gonzalo, C. Vafa, *Dark Dimension and Decaying Dark Matter Gravitons*, Phys. Rev. D 109 (2024) 063540, [arXiv:2311.05318](https://arxiv.org/abs/2311.05318).
5. A. P. Braun, M. Cicoli, R. Milioli, R. Valandro, *Moduli Stabilisation for ADD and the Dark Dimension Scenario*, [arXiv:2606.19440](https://arxiv.org/abs/2606.19440).
6. R. Blumenhagen, A. Paraskevopoulou, *Towards the Realization of the Dark Dimension Scenario in Hořava–Witten Theory*, JHEP 07 (2026) 247, [arXiv:2605.11068](https://arxiv.org/abs/2605.11068).
7. L. Kaufmann, J. Monnee, T. Weigand, M. Wiesner, *Quantum obstructions for \(N=1\) infinite distance limits — Part II: Kähler obstructions*, [arXiv:2603.13470](https://arxiv.org/abs/2603.13470).

---

**Verdict final :** conserver \(R\) comme observable à dériver, la tour comme spectre KK à calculer, une limite Tyurin-type comme mécanisme géométrique candidat, et Fano comme programme ultérieur. Abandonner l’idée que ces quatre éléments sont déjà reliés par les anciens Articles I–VIII.

