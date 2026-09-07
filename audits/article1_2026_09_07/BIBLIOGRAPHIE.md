# Article 1: audit bibliographique et matrice d'antériorité

> **Statut au 7 septembre 2026 :** compte rendu conservé de la relecture avant intégration. Les corrections retenues ont été appliquées au manuscrit livré, y compris les quatre précisions finales de notation. Le [bilan final](AUDIT_FR.md) distingue les corrections intégrées des limites scientifiques restantes.

Audit ciblé du 7 septembre 2026. Source examinée : `publications/article_1/manuscript.json`, vingt notices de `references.bib`, et les trois audits bibliographiques antérieurs. Les équations ci-dessous suivent la numérotation du manuscrit examiné. Cette note ne certifie ni priorité, ni acceptabilité éditoriale, ni viabilité de DDF.

## Résultat utile pour la révision

Les vingt références existent et leurs identifiants principaux concordent. Les notices récentes [9], [15] et [20] ne sont pas fictives : leurs années de publication différentes des identifiants arXiv sont normales. Le problème le plus important est l'antériorité scientifique, plutôt qu'une fausse référence.

Une référence très proche manque : **Girmohanta et al., JHEP 08 (2024) 229**, sur les potentiels de brane de rigidité finie. Par ailleurs, **Olechowski démontre explicitement** la croissance de la plus petite masse avec la rigidité à fond fixé. Ces sujets ne peuvent donc pas constituer en eux-mêmes la nouveauté de l'article.

Le meilleur contenu distinct restant à défendre est la formule particulière du résidu canonique `c_alpha(x,lambda_hat)`, valable au premier ordre de rétroaction mais sans expansion en rigidité inverse, ses bornes analytiques et le théorème d'événement pour le potentiel quadratique positif et la branche symétrique considérés. Je n'ai pas identifié leurs expressions identiques dans les passages comparés. Cette absence observée n'établit pas une priorité ; une formule différente de modèle ne garantit pas non plus une contribution assez substantielle pour une revue.

## Matrice résultat / précédent / différence / travail nécessaire

| Résultat du manuscrit | Précédent primaire lu | Même résultat ou différence précise | Conséquence pour le manuscrit |
|---|---|---|---|
| Stabilisation par un scalaire de volume et des potentiels aux bouts | Goldberger–Wise [1], DeWolfe et al. [2] | Mécanisme déjà établi ; une distance déterminée et un réglage pour Minkowski existaient déjà. | Présenter comme cadre connu. |
| Action sur un intervalle avec GHY et jonctions | Carena–Lykken–Park [13] | Formalisme établi. | Citer pour les conventions ; pas de nouveauté générale. |
| Warp non monotone et symétrie de réflexion | Medina–Pontón [8], §§2–3 | Géométrie réfléchie avec scalaire impair déjà étudiée ; potentiels de superpotentiel différents. | La géométrie seule ne distingue pas l'article. |
| Existence unique du premier événement scalaire si `0<Lambda5<2 lambda² v²` | [1,2], Bhattacharyya–SenGupta [20] | Leur stabilisation ne fournit pas le même théorème pour ce système positif quadratique et ses Robin symétriques. | Conserver le théorème spécifique, toutes ses hypothèses et la tension compatible séparée. |
| Formule de longueur dans la limite plate, puis `L_backreacted<L_flat` | [2,20] | La sélection de longueur est connue ; cette formule Robin et cette comparaison concernent le modèle déclaré. | Ne pas annoncer une prédiction absolue de rayon. Montrer la comparaison à paramètres d'action identiques. |
| Forme de Sturm–Liouville et masses positives | Lesgourgues–Sorbo [5], Olechowski [6] | Méthode générale ancienne ; [6] traite les poids de bord. Le résultat de [5] cité dans son §III suppose aussi un warp dérivé non nul, condition absente au centre de notre branche. | Utiliser [6] et la démonstration régulière propre au manuscrit pour le point de retournement ; ne pas attribuer à [5] une hypothèse qu'il ne couvre pas. |
| Produit scalaire spectral contenant des poids aux bouts | Girmohanta et al. [23], §2.2, eqs.2.42–2.46 ; [6] eq.47 | Même enjeu structurel à rigidité finie, avec variables et facteurs de convention différents. | Ajouter [23] près de la forme spectrale ; distinguer le produit spectral de la norme cinétique physique. |
| Norme physique et résidu de matière `alpha=BI f(0)²/Nf` | Kofman–Martin–Peloso [4], eqs.3–4 | Normalisation canonique et couplage à partir du profil sont des méthodes générales déjà fournies. | Revendiquer le coefficient évalué dans notre modèle, pas une nouvelle méthode de normalisation. |
| Masse croissante avec rigidité à fond fixé | Olechowski [6], §4.3, eq.47 et note6 | Affirmation explicite déjà prouvée ; la note6 explique aussi comment changer `U''` sans changer le fond. | Attribution directe indispensable. Le contrôle numérique est une reproduction spécialisée. |
| Masse et profil à faible rétroaction, rigidité finie | Girmohanta et al. [23], eqs.3.6–3.7 | Calcul précédent en `l²` et `1/gamma²` pour une branche DFGK ; notre coefficient garde la dépendance complète en rigidité d'un autre fond. | Comparaison obligatoire ; ne pas dire que les travaux antérieurs imposent tous la rigidité infinie. |
| Formule22 pour `c_alpha` et bornes23 | [4,8,23], et George–McDonald [GM] | Aucun coefficient identique identifié. [GM] évalue son couplage au seul ordre dominant, avec la correction `O(l²)` laissée dans son eq.70. | Candidat principal de contribution propre, sous réserve d'un examen expert et d'antériorité plus large. |
| Relation masse/résidu24 | Eqs.19 et22 du manuscrit ; comparaison [4,23,GM] | Élimination algébrique de `epsilon`, pas une troisième information indépendante. | L'appeler corollaire du coefficient de résidu. Sa pente dépend encore de `x` et de la rigidité. |
| Réponse linéaire à la tension, eq.26 | DeWolfe et al. [2], Lüst–Nee–Randall [9], eq.4.23 publiée | Réponse au vide non supprimée déjà connue ; coefficient de notre convention : deux tensions identiques, `R4=12h`. | Présenter comme spécialisation et contrôle de cohérence, pas résolution de la constante cosmologique. |
| Coefficient tensoriel plat `8/3` relatif à `G_T` | Callin–Ravndal [10], eqs.67–69 ; Kehagias–Sfetsos [16] | Projecteur massif/massless `4/3` fois rapport des profils `2`. [16] donne `alpha=2n` pour ses exemples toroïdaux, sans être la source du `8/3`. | La correction actuelle est justifiée. Ne pas affirmer une équivalence universelle des normalisations des deux articles. |
| Test null T1 / Z-light | Supplément séparé du dossier | Contrôle interne du domaine et des bords ; il répare un déficit de validation. | Ne prouve ni originalité du papier de stabilisation ni théorie DDF complète. |
| Rayon micrométrique, signal multimode, DDF complète | [11,12,15] motivent des questions distinctes | Aucun ajustement expérimental, sélection absolue de l'échelle ou modèle complet dérivé ici. | Limites actuelles à conserver. |

## Comparaisons les plus proches

**Girmohanta et al. [23].** Les eqs.2.9–2.16 utilisent `W=6k/kappa²-u phi²`, un scalaire exponentiel et un potentiel avec constante négative et terme quartique. Notre scalaire impair traversant zéro avec `Lambda5>0` n'est donc pas cette solution renommée. Aucun résidu de type22 n'a été identifié dans le texte ou l'annexe lus. [Texte primaire intégral](https://arxiv.org/html/2404.05141v2).

**Olechowski [6].** Voir directement l'eq.47 et le §4.3, sous-titre `B_j<0`, avec sa note6. Le potentiel particulier simplifie nos conditions, mais ne rend pas nouvelle la preuve de monotonie. [Texte primaire](https://arxiv.org/html/2408.15343v2).

**Lüst–Nee–Randall [9].** Utiliser la version publiée : eq.3.13 pour les classes de potentiels, eq.3.21 pour la rigidité finie, eq.4.23 pour `delta V_eff=delta T_IR phi_0^4`. Leur résultat RS hiérarchique tronqué sur deux branes linéaires n'exclut pas notre volume positif. [PDF publié, 33 pages](https://link.springer.com/content/pdf/10.1007/JHEP06(2026)130.pdf).

**Bhattacharyya–SenGupta [20].** CMS emploie généralement Dirichlet UV/linéaire IR sur AdS. Le §4.5 BFG contient une rétroaction exacte. La note1 précise que, hors §7, leur potentiel radion considère le secteur GW. Ces différences précisent la matrice ; elles n'impliquent pas l'inapplicabilité de toute leur analyse. [Article intégral](https://link.springer.com/article/10.1140/epjc/s10052-025-15170-1).

**Boos et al. [7].** Leur exemple appelé « symmetric » fixe `A(0)=A(L)` ; après l'eq.73, les auteurs précisent que le warp n'est pas réfléchi autour de `L/2`. L'introduction actuelle attribue donc trop à [7] lorsqu'elle le joint à [8] comme précédent de réflexion. Distinguer explicitement égalité des valeurs aux bouts et invariance de réflexion. [PDF](https://arxiv.org/pdf/hep-th/0412204).

**Medina–Pontón [8].** La réflexion et les modes pairs/impairs de la géométrie sont de vrais précédents. Leurs exemples suivent un superpotentiel linéaire ou cubique ; les conditions scalaires utilisées pour le spectre fixent les fluctuations aux extrémités. Les profils et le potentiel ne sont pas ceux du présent modèle à rigidité quadratique finie. [PDF, §§2–3](https://arxiv.org/pdf/1012.5298).

**George–McDonald [GM].** Précédent utile supplémentaire : action d'intervalle, termes de courbure de brane et norme générale (eq.61). Leur calcul de masse §5.1 prend explicitement les potentiels raides ; l'eq.70 laisse la correction de couplage `O(l²)` non évaluée. La présence de leur paramètre de courbure `v_i` ne doit pas être confondue avec notre rigidité de potentiel. [PDF](https://arxiv.org/pdf/1107.0755).

**Cui–Ning [15].** Le radion trop léger concerne leur potentiel Casimir et son absence d'écran dans ce régime. Le §4 explique pourquoi un chameleon ordinaire échoue dans ce modèle, puis envisage un mécanisme avec axion. Cela n'établit ni une impossibilité de toute stabilisation Casimir, ni une viabilité expérimentale du présent intervalle. [PDF publié](https://link.springer.com/content/pdf/10.1007/JHEP02(2026)156.pdf).

## Notices contrôlées et sources effectivement ouvertes

`references_reviewed.bib` conserve les vingt entrées et ajoute Harlow–Wu [21], Speranza [22] et Girmohanta et al. [23]. George–McDonald [GM] reste dans additional_reading.bib, sans numéro de manuscrit. Les liens ci-dessous sont des pages primaires consultées, pas des résultats de recherche. Pour les références anciennes, le contrôle porte sur auteurs, titre, année, revue/article et DOI ; il ne constitue pas une lecture intégrale de chacun des vingt articles.

| Réf. | Auteurs abrégés ; record vérifié | Source primaire |
|---|---|---|
| 1 | Goldberger–Wise ; PRL83,4922–4925 (1999) ; 10.1103/PhysRevLett.83.4922 | [arXiv hep-ph/9907447](https://arxiv.org/abs/hep-ph/9907447) |
| 2 | DeWolfe–Freedman–Gubser–Karch ; PRD62,046008 (2000) ; 10.1103/PhysRevD.62.046008 | [arXiv hep-th/9909134](https://arxiv.org/abs/hep-th/9909134) |
| 3 | Csáki–Graesser–Kribs ; PRD63,065002 (2001) ; 10.1103/PhysRevD.63.065002 | [arXiv hep-th/0008151](https://arxiv.org/abs/hep-th/0008151) |
| 4 | Kofman–Martin–Peloso ; PRD70,085015 (2004) ; 10.1103/PhysRevD.70.085015 | [arXiv hep-ph/0401189](https://arxiv.org/abs/hep-ph/0401189) |
| 5 | Lesgourgues–Sorbo ; PRD69,084010 (2004) ; 10.1103/PhysRevD.69.084010 | [arXiv hep-th/0310007](https://arxiv.org/abs/hep-th/0310007) |
| 6 | Olechowski ; NPB1011,116807 (2025) ; 10.1016/j.nuclphysb.2025.116807 | [arXiv 2408.15343](https://arxiv.org/abs/2408.15343) |
| 7 | Boos–Mikhailov–Smolyakov–Volobuev ; NPB717,19–33 (2005) ; 10.1016/j.nuclphysb.2005.04.012 | [arXiv hep-th/0412204](https://arxiv.org/abs/hep-th/0412204) |
| 8 | Medina–Pontón ; JHEP06(2011)009 ; 10.1007/JHEP06(2011)009 | [arXiv 1012.5298](https://arxiv.org/abs/1012.5298) |
| 9 | **Severin Lüst, Michael Nee, Lisa Randall** ; JHEP06(2026)130 ; publié **2026-06-11** | [Éditeur](https://link.springer.com/article/10.1007/JHEP06(2026)130), [arXiv 2510.11771](https://arxiv.org/abs/2510.11771) |
| 10 | Callin–Ravndal ; PRD70,104009 (2004) ; 10.1103/PhysRevD.70.104009 | [arXiv hep-ph/0403302](https://arxiv.org/abs/hep-ph/0403302) |
| 11 | Lee–Adelberger–Cook–Fleischer–Heckel ; PRL124,101101 (2020) ; 10.1103/PhysRevLett.124.101101 | [arXiv 2002.11761](https://arxiv.org/abs/2002.11761) |
| 12 | Montero–Vafa–Valenzuela ; JHEP02(2023)022 ; 10.1007/JHEP02(2023)022 | [arXiv 2205.12293](https://arxiv.org/abs/2205.12293) |
| 13 | Carena–Lykken–Park ; PRD72,084017 (2005) ; 10.1103/PhysRevD.72.084017 | [arXiv hep-ph/0506305](https://arxiv.org/abs/hep-ph/0506305) |
| 14 | Mukohyama–Kofman ; PRD65,124025 (2002) ; 10.1103/PhysRevD.65.124025 | [arXiv hep-th/0112115](https://arxiv.org/abs/hep-th/0112115) |
| 15 | **Chuanxin Cui, Sirui Ning** ; JHEP02(2026)156 ; publié **2026-02-16** | [Éditeur](https://link.springer.com/article/10.1007/JHEP02(2026)156), [arXiv 2310.19592](https://arxiv.org/abs/2310.19592) |
| 16 | Kehagias–Sfetsos ; PLB472,39–44 (2000) ; 10.1016/S0370-2693(99)01421-5 | [arXiv hep-ph/9905417](https://arxiv.org/abs/hep-ph/9905417) |
| 17 | Gibbons–Kallosh–Linde ; JHEP01(2001)022 ; 10.1088/1126-6708/2001/01/022 | [arXiv hep-th/0011225](https://arxiv.org/abs/hep-th/0011225) |
| 18 | Georgi–Grant–Hailu ; PLB506,207–214 (2001) ; 10.1016/S0370-2693(01)00408-7 | [arXiv hep-ph/0012379](https://arxiv.org/abs/hep-ph/0012379) |
| 19 | Pilo–Rattazzi–Zaffaroni ; JHEP07(2000)056 ; 10.1088/1126-6708/2000/07/056 | [arXiv hep-th/0004028](https://arxiv.org/abs/hep-th/0004028) |
| 20 | **Soham Bhattacharyya, Soumitra SenGupta** ; EPJC85,1430 (2025) ; publié **2025-12-16** | [Éditeur](https://link.springer.com/article/10.1140/epjc/s10052-025-15170-1) |
| 21 ajouté | Daniel Harlow–Jie-qiang Wu ; JHEP10(2020)146 ; publié **2020-10-22** | [Éditeur](https://link.springer.com/article/10.1007/JHEP10(2020)146), [arXiv 1906.08616](https://arxiv.org/abs/1906.08616) |
| 22 ajouté | Antony J. Speranza ; JHEP02(2018)021 ; DOI **10.1007/JHEP02(2018)021** | [Éditeur](https://link.springer.com/article/10.1007/JHEP02(2018)021), [arXiv 1706.05061](https://arxiv.org/abs/1706.05061) |
| 23 ajouté | Girmohanta–Nakai–Suzuki–Wang–Xu ; JHEP08(2024)229 ; publié **2024-08-29** | [Éditeur](https://link.springer.com/article/10.1007/JHEP08(2024)229), [arXiv 2404.05141](https://arxiv.org/abs/2404.05141) |
| GM facultatif | George–McDonald ; PRD84,064007 (2011) ; 10.1103/PhysRevD.84.064007 | [arXiv 1107.0755](https://arxiv.org/abs/1107.0755) |

[9] : reçu 2025-11-25, révisé 2026-03-24, accepté 2026-04-21. [15] : reçu 2025-11-17, révisé 2025-12-30, accepté 2026-01-05. [20] : reçu 2025-09-15, accepté 2025-12-03. L'avis de mise à jour du 2026-03-10 de [20] concerne les déclarations données/code, pas un résultat mathématique corrigé. Aucun identifiant arXiv de [20] n'a été vérifié ; ne pas en inventer.

## Ce qui doit changer avant envoi à une revue

1. Ajouter [23], reconnaître explicitement [6] pour la monotonie et le changement de rigidité à fond fixé, et corriger l'attribution de réflexion à [7].
2. Remplacer la référence à la comparaison « preprint v2 » de [9] par la version publiée et ses numéros d'équations. Les anciennes notes citant l'eq.94 doivent indiquer la correspondance à l'eq.4.23 publiée.
3. Faire des eqs.22–23 et du théorème d'existence précis le centre de la contribution. Le nombre d'audits et la quantité de code ne remplacent pas une question scientifique distincte.
4. Éviter de compter l'eq.24 et la réponse linéaire au vide comme deux découvertes supplémentaires. Fournir la table de correspondance d'hypothèses, au moins sous forme concise dans le papier.
5. Une révision de présentation ne suffit pas à démontrer la substantialité. Une lecture par un chercheur du domaine doit notamment juger l'intérêt du coefficient de résidu pour cette branche, les hypothèses des deux bords physiques, et la pertinence d'une extension au-delà de l'exemple quadratique. Il n'est pas possible de garantir le résultat éditorial par cet audit.

La recherche a suivi les références proches et des requêtes sur les potentiels finis, la rétroaction, les couplages et les expressions hyperboliques. Elle n'a pas exploré exhaustivement toutes les thèses, actes, reformulations, citations ultérieures et articles non indexés. Les conclusions « formule non identifiée » doivent garder ce sens limité.

