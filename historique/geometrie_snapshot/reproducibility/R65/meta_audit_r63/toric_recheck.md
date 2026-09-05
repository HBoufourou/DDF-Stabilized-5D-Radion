# R63 — contre-audit indépendant du noyau torique R61–R62

> **Statut documentaire : audit partiel.** Les réserves quasi-Fano formulées
> ci-dessous décrivent l'état avant les preuves cohomologiques ultérieures de
> R63. Elles sont levées par R63_REPORT.md et
> quasifano_normal_bundles.md ; les réserves sur la Gauss–Manin intégrale
> demeurent.

Date : 2026-09-04  
Périmètre : éventail relatif 5D, régularité/unimodularité, cohérence et
projectivité, propreté sur \(\mathbb A^1\), fibre centrale à deux composantes,
support anticanonique et argument SNC.  Le test de parité O3/O7 n'est pas
réaudité ici.

## Verdict

**VERT pour le noyau torique et combinatoire.** Je n'ai trouvé aucune erreur
fatale dans la construction de l'éventail relatif de R62. Un second programme,
écrit sans importer les fonctions de R61 ou R62 et n'utilisant que la
bibliothèque standard de Python, reproduit les certificats essentiels.

**ORANGE pour trois étapes de rédaction mathématique.** La lissité/SNC
générique est bien soutenue par le lieu de base, le jet unité et Bertini, mais
elle n'est pas un calcul exhaustif d'idéal jacobien. L'irréductibilité des deux
composantes est défendue dans le rapport par les discriminants génériquement
non carrés, mais n'est pas certifiée par le script. Enfin, les annulations
quasi-Fano nécessaires au terme « Tyurin strict » restent ouvertes, comme R62
le reconnaît déjà.

Il est donc légitime de conserver R62 comme **dégénérescence semi-stable de
forme Tyurin**. Il n'est pas encore légitime de la présenter comme un théorème
complet de dégénérescence de Tyurin stricte sans fermer les annulations
cohomologiques.

## 1. Intégrité des exécutions R61 et R62

Les deux programmes ont été réexécutés avec Python 3.12.13, assertions actives,
et se terminent avec le code de sortie zéro.

| Fichier | SHA-256 de la sortie enregistrée | SHA-256 de la nouvelle sortie | Résultat |
|---|---|---|---|
| R61 | `850b9ceec588dc8f22b709ca10cffde4cbf95f7457e94cf277d75e2a2595381d` | identique | reproduction exacte |
| R62 | `9b8d3c5642cac79886c243e7ea38985bd6ea58398988e72469f9e7c02240c2bc` | identique | reproduction exacte |

Les fichiers de sortie contiennent respectivement 57 et 56 lignes. Ils se
terminent par les verdicts attendus. **Aucune sortie tronquée ni divergence
silencieuse n'a été détectée.**

Les trois fichiers Python — R61, R62 et le nouveau contre-audit R63 — passent
également la compilation `py_compile`.

## 2. Méthode indépendante R63

Le fichier `r63_toric_independent_audit.py` reconstruit les objets à partir des
rayons publiés, sans SymPy et sans appeler le code antérieur. Il utilise :

1. un déterminant entier de Bareiss indépendant ;
2. un solveur de Gauss exact sur les fractions ;
3. l'énumération complète des sommets des polyèdres normaux ;
4. l'énumération de toutes les faces et non-faces minimales ;
5. l'énumération directe des 104 points duaux bornés par les inégalités des
   rayons ;
6. un calcul indépendant des degrés de Cox, lieux de base monomiaux et jets.

La saturation des six relations de Gale est testée sans calcul de Smith : le
PGCD de tous les mineurs maximaux \(6\times6\) vaut un. Avec une relation de
rang six orthogonale aux onze rayons de rang cinq, cela redonne le même réseau
de relations intégral et primitif.

## 3. Résultats exacts reproduits

| Objet | Résultat indépendant | Statut |
|---|---:|---|
| cônes maximaux du fan résolu 4D | 20 | exact |
| déterminants 4D | \(|\det|=1\) pour les 20 | exact |
| cônes maximaux relatifs 5D | 28 | exact |
| répartition bas / haut / couture | \(8/12/8\) | exact |
| déterminants 5D | \(|\det|=1\) pour les 28 | exact |
| rang des relations de Gale | 6 | exact |
| PGCD des mineurs maximaux de Gale | 1 | réseau saturé |
| sommets du polyèdre de cohérence | 28 | exact |
| ensembles de facettes actives | exactement les 28 cônes | exact |
| écarts stricts | \(\{1,2,3,4,5\}\) | exact |
| murs relatifs | 60 internes, 20 de bord | exact |
| sommets/cônes de la complétion | 48 | exact |
| murs de la complétion | 120, tous appariés deux à deux | exact |
| déterminants de la complétion | \(|\det|=1\) | exact |
| liens centraux \(D_p,D_m,S\) | \(16,20,8\) cônes | exact |
| points du polytope dual résolu | 104 | exact |
| support invariant \(\sigma_5\) | 69 monômes | exact |
| histogramme de hauteur | \(9,26,9,25\) pour \(q=-1,0,1,2\) | exact |
| degré commun de Cox | \((4,4,3,2,-1,0)\) | anticanonique |
| supports sur \(p=0,m=0,S\) | \(60,35,26\) | exact |
| lieu de base total | \(x_6=x_7=0\) | exact |
| lieux de base des restrictions | \(\varnothing,(x_6=x_7=0),\varnothing\) | exact |
| jet transversal | \(x_0^2E^2x_6\) | exact |

## 4. Cohérence, projectivité et propreté

La vérification polytopale est solide. Le polyèdre défini par les onze
inégalités possède exactement 28 sommets simples entiers et leurs cônes
normaux sont exactement les 28 cônes proposés. Cela prouve simultanément que
les cônes ne se chevauchent pas incorrectement et que l'éventail est cohérent.

Après ajout du rayon \(\nu_\infty=(0,0,0,0,-1)\), le polyèdre devient borné et
son éventail normal possède exactement 48 cônes maximaux unimodulaires. Le fan
complété est donc complet, lisse et projectif.

La projection sur la cinquième coordonnée envoie les neuf rayons anciens sur
zéro, \(p,m\) sur \(+1\), et \(\nu_\infty\) sur \(-1\). Les seuls cônes retirés
de la complétion sont ceux de l'étoile de \(\nu_\infty\), qui sont entièrement
dans le demi-espace négatif. Le support restant est donc exactement

\[
N_{\mathbb R}\times\mathbb R_{\ge0}
=\pi_N^{-1}(\mathbb R_{\ge0}).
\]

Le critère torique de propreté au-dessus de \(\mathbb A^1\) est ainsi satisfait.
La restriction du morphisme projectif complété sur \(\mathbb P^1\) fournit la
projectivité relative.

## 5. Fibre centrale et SNC : ce qui est fermé

La fonction de base correspond au caractère dont les valuations sont zéro sur
les neuf rayons horizontaux et un sur \(p,m\). Dans les coordonnées de Cox,

\[
z=pm,
\qquad \operatorname{div}(z)=D_p+D_m.
\]

Les coefficients valent un, donc la fibre torique centrale est réduite et
possède exactement deux diviseurs toriques. La régularité du fan donne des
coordonnées locales \(z=u\), \(z=v\) ou \(z=uv\), donc le modèle torique
ambiant est localement SNC.

Pour l'hypersurface :

- le support est anticanonique ;
- l'unique lieu de base total est \(x_6=x_7=0\) ;
- les relations SR y imposent \(x_0E\ne0\) ;
- le terme \(c x_0^2E^2x_6\), pour \(c\ne0\), donne
  \(\partial P/\partial x_6=cx_0^2E^2\ne0\) ;
- les systèmes restreints à la première composante et à la couture sont sans
  point de base ; la seconde composante possède le même lieu de base traité
  par le même jet.

En caractéristique zéro, l'argument « jet unité sur le lieu de base + Bertini
hors du lieu de base », appliqué simultanément à un ensemble ouvert de
coefficients généraux, soutient bien la lissité du total, des composantes et de
la couture. Une couture lisse dans l'intersection torique transverse implique
alors la transversalité des deux composantes dans l'hypersurface totale.

## 6. Points à renforcer avant dépôt

### 6.1 Irréductibilité — renforcement court nécessaire

Le script imprime « exactement deux composantes », mais ne factorise aucun
polynôme. Le rapport donne un argument raisonnable : sur le tore dense de
chaque diviseur central, l'équation est quadratique en \(x_0\) et son
discriminant est génériquement non carré. Pour transformer cela en certificat
de publication, il faut ajouter l'un des deux éléments suivants :

- un lemme algébrique explicite sur le corps des fonctions, avec une
  spécialisation de coefficients dont le discriminant est manifestement non
  carré ; ou
- une factorisation/saturation exacte dans Singular ou Macaulay2 pour une
  spécialisation rationnelle lisse, suivie de l'argument d'ouverture générique.

Ce point est **réparable** et ne remet pas en cause le fan.

### 6.2 Lissité — préciser la portée du certificat

Les lignes `SMOOTH / SMOOTH / SMOOTH` sont des conclusions imprimées après les
tests de lieu de base ; elles ne proviennent pas d'une saturation globale de
l'idéal jacobien. La preuve par Bertini est acceptable, mais l'article doit
énoncer clairement le corps de base, la généralité des coefficients et le
lemme appliqué. Un contrôle CAS sur une spécialisation serait une excellente
contre-vérification, pas une condition logique absolue.

### 6.3 Platitude — écrire le lemme local

La platitude est expliquée dans le texte et non testée par le script. Il faut
écrire proprement : dans chaque anneau local régulier du total torique,
\(z=u,v\) ou \(uv\) ; comme \(P\) n'a ni \(u\) ni \(v\) comme facteur,
\(z\) est non-diviseur de zéro modulo \(P\). La famille hypersurface est alors
sans torsion sur la courbe régulière, donc plate au voisinage de zéro.

### 6.4 Les seize lieux horizontaux — résultat partiellement codé en dur

La valeur 16 est produite dans R62 par l'expression déjà entrée
`2*4 + 2*4`. Le script ne redérive ni les bidegrés \((2,2),(4,4)\) depuis
l'anneau de Chow, ni la transversalité globale. Cette valeur ne doit pas être
présentée comme un résultat autonome du calcul Python. Ajouter un petit calcul
d'intersection dans l'anneau de Chow relatif fermerait ce point.

### 6.5 Tyurin strict et LMHS

Les conditions

\[
H^i(Y_p,\mathcal O_{Y_p})=H^i(Y_m,\mathcal O_{Y_m})=0,
\qquad i>0,
\]

ne sont pas calculées. R62 le dit correctement. Elles constituent la tâche
centrale de R63 avant d'utiliser sans réserve « dégénérescence de Tyurin ».

De plus, la mention `II_18` de R61 utilise les formules standard de LMHS, le
rang de restriction deux et un réseau actif écrit explicitement. Le script
vérifie l'algèbre du modèle de monodromie, mais ne reconstruit pas à lui seul le
morphisme de Clemens--Schmid de la famille relative. Dans l'article, ce résultat
doit être présenté comme une application d'un théorème clairement cité, avec
vérification séparée de ses hypothèses.

## 7. Corrections mineures de présentation du script R62

1. Plusieurs verdicts finaux sont des chaînes littérales. Les assertions qui
   les soutiennent existent, mais les valeurs calculées devraient être passées
   directement aux fonctions d'affichage pour éviter toute divergence future.
2. La ligne `smooth completion cones / paired walls` imprime le nombre de
   sommets du polyèdre complété comme premier nombre. Il vaut bien 48, comme le
   nombre de cônes normaux maximaux, mais le nom de variable devrait être
   corrigé pour que le certificat soit lisible.
3. `generic horizontal intersections 16` est une entrée arithmétique codée en
   dur, pas une énumération des intersections.

Ces points n'altèrent aucun résultat exact reproduit.

## 8. Décision R63 pour cette branche

La construction R62 passe le contre-audit torique. La suite rationnelle est :

1. conserver définitivement les rayons, les 28 cônes et le support relatif ;
2. ajouter un certificat CAS de spécialisation pour lissité/irréductibilité ;
3. calculer les cohomologies des deux composantes et la d-semistabilité avec
   les suites exactes adaptées ;
4. seulement après ces contrôles, figer le théorème géométrique destiné à
   l'article.

Le contre-audit ne dérive aucune longueur physique \(R\), aucune échelle
micrométrique et aucun spectre KK. Ces questions restent indépendantes du
succès du certificat torique.

