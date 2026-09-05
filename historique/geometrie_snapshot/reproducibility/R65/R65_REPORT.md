# R65 — Pilote spectral préenregistré

**Date :** 5 septembre 2026  
**Branche :** DDF-KK  
**Dépendance scientifique :** R64 laisse ouverte une tour KK neutre  
**Portée :** validation dimensionnelle d'un pipeline scalaire, sans métrique DDF

## 1. Verdict exécutif

R65 passe sa porte globale : le même pipeline reconnaît trois contrôles
effectivement unidimensionnels et rejette les deux faux positifs annoncés
avant le calcul.

~~~text
R65_PREREGISTERED_PROTOCOL = FROZEN_BEFORE_SUCCESSFUL_RUN
INTERVAL_NEUMANN_CONTROL = PASS
INTERVAL_DIRICHLET_CONTROL = PASS
PERIODIC_CIRCLE_CONTROL = PASS_WITH_REGISTERED_DOUBLETS
TRANSVERSE_CONTAMINATION_CONTROL = REJECTED_5_OF_5
CHEEGER_TUNNELING_CONTROL = REJECTED_4_OF_5
R65_SPECTRAL_PIPELINE = GO
DDF_GEOMETRY_SPECTRUM = NOT_TESTED
SPIN2_KK_SPECTRUM = NOT_TESTED
R_OF_T_AND_MICROMETRIC_SCALE = NOT_DERIVED
FANO_PLANE = DEFERRED
R66_REAL_GEOMETRY_PILOT = AUTHORIZED_AFTER_PLATFORM_LOCK
~~~

Le mot `GO` signifie uniquement que les diagnostics choisis savent distinguer
les cas élémentaires pour lesquels la réponse est connue. Il ne signifie pas
que DDF possède déjà une direction longue ni que les modes scalaires calculés
sont des gravitons KK.

## 2. Protocole effectivement exécuté

Le fichier `R65_CONFIG.json` a gelé cinq paramètres

\[
|t|=10^{-1},10^{-2},10^{-3},10^{-4},10^{-5}
\]

et la règle pilote, purement sans dimension,

\[
L(|t|)=6\bigl(1-\log_{10}|t|\bigr)=12,18,24,30,36.
\]

Pour chaque modèle, 30 niveaux positifs ont été conservés et les dix
premiers ont été classés sans réétiquetage après coup. Deux discrétisations
indépendantes ont été utilisées : volumes finis/différences secondes à
mailles centrées et éléments finis linéaires à masse cohérente. Trois
résolutions ont été calculées dans chaque méthode.

Cette architecture suit la distinction mathématique connue entre les
variétés minces convergeant spectralement vers un graphe et les autres
régimes où les sommets/caps peuvent imposer des limites découplées ou des
conditions différentes [Exner–Post](https://arxiv.org/abs/math-ph/0312028).

## 3. Contrôles positifs

Les spectres continus utilisés comme vérité analytique sont séparables :

\[
\lambda_{k,m}^{\rm int}
=\left(\frac{\pi k}{L}\right)^2
 +\left(\frac{\pi m}{b}\right)^2,
\qquad
\lambda_{k,m}^{\rm circ}
=\left(\frac{2\pi k}{L}\right)^2
 +\left(\frac{2\pi m}{b}\right)^2.
\]

Les formulations variationnelles et le problème généralisé
\(K u=\lambda M u\) sont ceux de l'approximation de Galerkin standard des
problèmes propres auto-adjoints ; le comportement de convergence sur le
Laplacien 1D est notamment exposé dans les notes de
[Boffi](https://mate.unipv.it/boffi/download/pavia2017.pdf).

| Contrôle | Erreur max sur \(L_{\rm eff}\) | Résidu quadratique max | Exposant libre \(p\) | Verdict |
|---|---:|---:|---:|---:|
| intervalle Neumann | \(1.16\times10^{-7}\) | \(1.49\times10^{-8}\) | 1.999999–2.000000 | PASS |
| intervalle Dirichlet | \(1.16\times10^{-7}\) | \(1.49\times10^{-8}\) | 1.999999–2.000000 | PASS |
| cercle périodique | \(1.84\times10^{-6}\) | \(2.37\times10^{-7}\) | 1.999991–2.000000 | PASS |

Le cercle est reconnu à partir des dix premiers niveaux distincts, chacun de
multiplicité deux. L'intervalle possède des niveaux longitudinaux simples.
Le pipeline ne confond donc pas le même coefficient quadratique avec la même
topologie.

Sur les trois familles, la dimension de comptage obtenue reste entre
1.000000000 et 1.000000262. Le plus petit gap transverse enregistré vaut
1.44 fois le dixième niveau longitudinal, au-dessus du seuil 1.25.

## 4. Faux positif transverse

Le rectangle de largeur \(b=L/3\) place le premier mode transverse au même
ordre que le niveau longitudinal \(k=3\). Les résultats sont stables sur les
cinq longueurs :

| Diagnostic | Valeur R65 | Seuil |
|---|---:|---:|
| modes transverses parmi les dix premiers | 5 | 0 autorisé |
| gap transverse / niveau longitudinal 10 | 0.09 | au moins 1.25 |
| résidu du fit quadratique | 0.1143 | moins de 0.10 |
| exposant libre | 1.2961 | 1.8–2.2 |
| dimension de comptage | 1.4760 | 0.8–1.2 |

La classification `TRANSVERSE_CONTAMINATED` est donc obtenue sur 5/5 points.
Une succession visuellement régulière de petites valeurs propres ne suffit
pas : les labels propres et le gap sont nécessaires.

## 5. Faux positif de Cheeger/tunneling

Le modèle haltère utilise l'opérateur pondéré

\[
-A^{-1}(A u')'
\]

sur deux caps reliés par un col dont l'aire vaut \(|t|\). Lorsque le col se
ferme, le premier mode devient une différence presque constante entre les
deux caps et sa variation se concentre dans l'étranglement. Ce comportement
est cohérent avec la littérature sur les domaines haltères de Neumann, où la
limite combine les spectres des extrémités et un problème de
Sturm–Liouville dans le col
[Beck–Lyons](https://arxiv.org/abs/2601.17140).

| \(|t|\) | \(\lambda_2/\lambda_1\) | énergie du gradient dans \(|x|<0.75\) | drapeau tunneling |
|---:|---:|---:|---:|
| \(10^{-1}\) | 24.1 | 0.924 | non |
| \(10^{-2}\) | 177 | 0.989 | oui |
| \(10^{-3}\) | 1 640 | 0.9989 | oui |
| \(10^{-4}\) | 16 214 | 0.99988 | oui |
| \(10^{-5}\) | 161 944 | 0.999988 | oui |

Le premier point n'est volontairement pas appelé tunneling : malgré son
isolation, les trois diagnostics de forme du paquet restent encore dans les
fenêtres KK préenregistrées. Les quatre points suivants échouent le paquet
quadratique et dépassent simultanément les seuils d'isolation et de
concentration. La règle demandait au moins 3/5 ; R65 obtient 4/5.

## 6. Erreurs numériques

| Famille | Richardson max | désaccord des méthodes max | résidu algébrique max |
|---|---:|---:|---:|
| produits analytiques | \(9.94\times10^{-4}\) | \(7.90\times10^{-9}\) | \(6.15\times10^{-11}\) |
| haltère pondéré | \(6.90\times10^{-4}\) | \(7.91\times10^{-7}\) | \(2.69\times10^{-6}\) |

Ces valeurs sont très inférieures aux seuils pilotes de 5 %, 5 % et 10 %.
Elles ne préjugent pas de l'erreur de discrétisation d'une métrique
Calabi–Yau six-dimensionnelle non séparable.

## 7. Incident numérique conservé

La première exécution après gel du protocole a retourné `STOP` pour le cercle.
Le générateur de candidats périodiques autorisait alors des indices
transverses au-delà de la fréquence de Nyquist du maillage grossier. Le mode
\(k_y=N\) se repliait artificiellement sur le zéro et produisait des niveaux
dupliqués.

La correction borne désormais les indices discrets par \(N/2\) en périodique
et par le nombre de degrés de liberté dans les cas à bord. Aucun modèle,
seuil, paramètre, longueur ou règle de classification n'a été modifié. Le
préenregistrement conserve donc les mêmes empreintes avant et après cette
correction. Cet incident est une raison supplémentaire de ne jamais accepter
un spectre uniquement parce que sa courbe semble régulière.

## 8. Ce que R65 établit et n'établit pas

R65 établit que le pipeline :

1. récupère \(L\) dans trois géométries séparables ;
2. reconnaît la multiplicité cercle/intervalle ;
3. rejette une contamination transverse ;
4. rejette un petit mode d'étranglement isolé ;
5. donne le même verdict avec deux discrétisations convergentes.

R65 n'établit pas :

- que la famille Tyurin R63 développe un col métrique long ;
- que le Laplacien scalaire possède le spectre du graviton spin-2 ;
- que les corrections de warping, caps, flux et branes préservent le paquet ;
- que la limite exacte \(t=0\) est physiquement admissible ;
- une relation métrique \(R(t)\), une valeur en microns ou une masse KK ;
- la stabilité d'une tour quantique ou son couplage à la matière ;
- un rôle du plan de Fano.

## 9. Décision pour R66

R65 autorise le passage à R66, mais seulement après avoir verrouillé une
plateforme unique. Il est interdit de mélanger la géométrie résolue R63 avec
les périodes, flux ou données D7/O7 d'un autre polytope.

R66 devra d'abord produire un manifeste contenant : polytope, triangulation,
phase, résolution, paramètre de lissage, approximation métrique, opérateur,
mesure, conditions globales et empreintes de toutes les entrées. Il appliquera
ensuite le pipeline scalaire à \(t_\star\ne0\). Le passage au véritable
opérateur spin-2 pondéré ne sera permis qu'après un signal scalaire convergent
et non contaminé.

## 10. Reproductibilité

Commande de calcul :

~~~bash
python3 r65_spectral_pilot.py
~~~

Commande de libération du dossier :

~~~bash
python3 r65_release_gate.py
~~~

Les tableaux complets comportent 750 niveaux spectraux, 25 lignes de
métriques et 801 points de profil. La figure synthétique est
`R65_SPECTRAL_DIAGNOSTICS.png`.

## 11. Références primaires minimales

1. P. Exner, O. Post, *Convergence of spectra of graph-like thin manifolds*,
   [arXiv:math-ph/0312028](https://arxiv.org/abs/math-ph/0312028).
2. N. F. Marshall, *The Stability of the First Neumann Laplacian
   Eigenfunction Under Domain Deformations and Applications*,
   [arXiv:1704.02962](https://arxiv.org/abs/1704.02962).
3. T. Beck, A. Lyons, *Nodal Deficiency of Neumann Eigenfunctions on a
   Symmetric Dumbbell Domain*,
   [arXiv:2601.17140](https://arxiv.org/abs/2601.17140).
4. D. Boffi, *Finite element approximation of eigenvalue problems*, notes de
   cours et références Babuška–Osborn,
   [PDF](https://mate.unipv.it/boffi/download/pavia2017.pdf).


