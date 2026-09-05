# Avis scientifique adverse sur le premier article — 5 septembre 2026

Périmètre : `noyau/EFT_MODELE_ET_RESULTATS.md`, `noyau/DERIVATION_COUPLAGE.md`, `calculs/spectre_5d.py` du dossier unifié. Le présent avis distingue la cohérence du modèle déclaré, la vérification d'un calcul et l'originalité publiable. Il ne repose pas sur l'accord entre deux solveurs comme preuve de la théorie.

## Conclusion

Je n'ai pas identifié de contradiction dans l'action corrigée, les jonctions, la normalisation cinétique et le couplage scalaire déclarés. Le coefficient positif +0,98342023984 à x=2 est compatible avec une dérivation à partir de l'action et des profils propres ; l'ancien coefficient négatif ne doit pas réapparaître.

Une amélioration analytique importante est possible immédiatement : une forme Sturm–Liouville régulière fournit une preuve d'absence de tachyons pour toute la famille régulière x>0, epsilon>0 considérée. Elle rend aussi explicite le produit scalaire spectral avec ses contributions de bord, qui ne doit pas être confondu avec la norme cinétique physique. Cette reformulation relève de techniques déjà présentes dans la littérature, notamment Olechowski (2025), et ne suffit pas à une revendication d'originalité.

Les principales limites de portée sont physiques : le potentiel strictement quadratique et les potentiels de bord strictement linéaires constituent des hypothèses ; leur protection contre les corrections quantiques n'est pas établie. Le fond exige deux énergies de vide de bord négatives et un réglage de la courbure 4D à zéro. Le balayage change plusieurs paramètres de l'action. Aucune longueur absolue ni raccord à la géométrie DDF ne suit de ces calculs.

## 1. Action, jonctions et construction du fond : objections résolues dans le modèle déclaré

Posons B=M5^3. Pour l'action B R/2, le GHY B K et les normales sortantes s0=-1, sL=+1, la variation donne

- Ui=3 si B A'(yi) ;
- Ji=-si sigma'(yi) pour Ui=Ti+Ji sigma ;
- A''=-sigma'^2/(3B), 6B A'^2=sigma'^2/2-V, sigma''=V_sigma-4A' sigma'.

Ces facteurs sont cohérents entre eux. Ils ne sont pas ceux de l'action historique 2 M5^3 R avec les mêmes symboles. Une convention unique doit être imprimée dans le manuscrit, sans présenter l'ancien texte comme une dérivation valide.

La construction par réflexion à partir de sigma(center)=A'(center)=0, sigma'(center)=vc>0 est cohérente. Sur la demi-longueur droite : sigma>0, A'<0 et sigma''=m_sigma^2 sigma-4A' sigma'>0. Par conséquent sigma'>0 partout et W=sigma''/sigma' satisfait W0<0<WL aux deux bords pour L>0 et x>0. La contrainte impose Lambda5=vc^2/2>0 au centre. Le profil hyperbolique ne résout le système que dans la limite de faible rétroaction.

Le modèle n'est donc pas le fond usuel Randall–Sundrum AdS à une brane de tension positive et une négative. L'expression « Einstein–scalar model with a quadratic bulk potential and affine boundary potentials » est plus précise ; « Goldberger–Wise type » reste possible avec cette distinction.

## 2. Jauge, contrainte et condition de bord

Dans le problème libre à deux bords, sans anisotropie de brane et sans courbure induite, la jauge droite avec F et delta sigma est compatible avec la description standard du secteur scalaire. L'équation métrique hors diagonale impose delta g55=-4F et la contrainte de mouvement impose

3B(f'+2A'f)+sigma' s=0.

La variation de la condition scalaire n^A partial_A sigma=-U_sigma donne exactement s'+2 sigma' f=0 lorsque U_sigma_sigma=0. En substituant la contrainte et l'équation de f, on retrouve W(f'+2A'f)-m^2 e^{-2A}f=0. Cette condition ne peut pas être remplacée par Neumann pour f, ni par la limite de potentiels de brane infiniment rigides.

La reconstruction de la perturbation induite pour une source est f(yi) chi, les termes longitudinaux éventuels se découplant d'une source conservée. La matière minimale est donc un choix cohérent. S'il existait des masses de matière dépendant de sigma, une cinétique de brane ou un Einstein induit, la présente amplitude ne serait plus celle de ce modèle modifié.

Précaution de rédaction : déduire les contraintes des équations tensorielles avant toute division par p^2. Pour une onde à quatre-impulsion non nulle mais nulle au sens de Minkowski, p_mu p_nu ne s'annule pas ; les contraintes peuvent être gardées. Le mode strictement constant en 4D correspond à une autre question, celle des variations de fond. La preuve de stabilité ci-dessous porte sur les modes du système régulier ; la continuité avec le secteur scalaire complet doit être déclarée par ces contraintes tensorielles, pas par un projecteur contenant 1/p^2.

## 3. Une preuve analytique régulière de stabilité et d'orthogonalité

Définir

u=e^{2A}f,

p=e^{-2A}/sigma'^2,

w=e^{-4A}/sigma'^2,

r=2 e^{-2A}/(3B).

Un calcul direct dans l'équation de f donne

-(p u')'+r u = m^2 w u.

La condition de bord devient

p u' = m^2 (w/W)u

aux deux extrémités. L'eigenvaleur apparaît bien dans les conditions de bord. Il ne faut donc pas employer uniquement l'intégrale de volume comme produit scalaire Sturm–Liouville.

Pour des fonctions satisfaisant les conditions de bord, l'intégration par parties donne

K[u] = integral_0^L (p |u'|^2+r |u|^2) dy
     = m^2 H[u],

H[u] = integral_0^L w |u|^2 dy + [w |u|^2/W]_0^L.

Ici H est strictement positif car w>0 et W0<0<WL. K est strictement positif pour tout u non nul car p,r>0. Il suit m^2>0 ; le même argument avec la conjugaison complexe exclut les valeurs propres complexes. L'argument ne suppose pas A' non nul et reste régulier au maximum de A.

Pour deux modes distincts, la forme bilinéaire de Green donne H[u_n,u_m]=0. La norme physique vaut exactement

N[f,s] = integral e^{2A}(3B f^2+s^2/2) dy
       = (9 B^2/2) K[u]
       = (9 B^2/2) m^2 H[u].

L'égalité intermédiaire suit de s=-3B e^{-2A}u'/sigma'. Elle établit aussi l'orthogonalité de la cinétique physique des modes de masses distinctes. Les termes de bord dans H ne représentent pas de nouvelles cinétiques de brane ajoutées à l'action ; ils résultent de la condition de bord dépendant de m^2. Inversement, les supprimer modifierait le problème spectral.

Cette preuve dispense d'utiliser un balayage de masses négatives comme justification fondamentale de stabilité. Un balayage peut rester une vérification du code. Elle ne s'applique pas au point epsilon=0, où sigma'=0 ; ce point doit être présenté comme limite avec radion sans masse. Elle ne prouve pas une stabilité non linéaire, cosmologique ou incluant des champs additionnels.

La tour tensorielle satisfait une identité encore plus directe :

integral e^{4A}|h'|^2 dy = m_T^2 integral e^{2A}|h|^2 dy

avec Neumann aux bords. Il existe le graviton constant sans masse et les autres masses tensorielles sont positives.

La reformulation et ses critères ont des précédents directs : Olechowski, *Stability of multibrane models*, arXiv:2408.15343v2, équations (19), (22), (25)–(32), traite déjà un opérateur régulier sans division par la dérivée du warp et des conditions de bord spectrales, y compris à rétroaction forte. Ne pas revendiquer la nouveauté générale de cette structure.

## 4. Normalisation et signe du coefficient de couplage

Dans la paramétrisation ds^2=e^{2A+2F}eta dx dx+e^{-4F}dy^2, le facteur lapse fois volume multipliant la courbure intrinsèque 4D donne e^{2A}[-6 Box F-6(partial F)^2]. Le terme Box F est une divergence 4D. Le coefficient cinétique gravitationnel est donc -3B integral e^{2A}(partial F)^2 ; le scalaire ajoute -1/2 integral e^{2A}(partial delta sigma)^2. Ni GHY ni Ui affine n'ajoutent de dérivées 4D dans cette jauge.

Après application de la contrainte aux profils propres, Z=2N est ainsi cohérent. Pour une source minimale au bord normalisé A_b=0 : g=f_b/sqrt(2N), Mbar_Pl^2=B integral e^{2A}dy et alpha=2 Mbar_Pl^2 g^2=Mbar_Pl^2 f_b^2/N. La limite plate donne alpha=1/3, ce qui est un test de convention mais ne remplace pas la dérivation.

Au faible epsilon, le coefficient annoncé est la différence de deux effets identifiés :

2[f2(bord)-moyenne(f2)] = 1,050625700214...

moyenne(s1^2)/6 = 0,067205460376...

Le premier vient de l'augmentation de l'amplitude métrique au bord relativement à sa moyenne ; le second vient de la cinétique du stabilisateur. Leur différence est +0,983420239838.... La correction explicite du volume de Planck s'annule à cet ordre. Aucun changement de facteur deux dans Z ne peut transformer ce coefficient relatif positif en -0,634.

Il s'agit d'un développement asymptotique à x=2 et pour epsilon=q L/sqrt(12B). Les valeurs finies à epsilon=0,4–0,9 doivent provenir du problème couplé. La série tronquée ne devient pas exacte parce que ses masses ou couplages sont proches à un point particulier.

## 5. Énergies de bord, réglage du vide et scan de théories

Puisque A'(0)>0 et A'(L)<0, les énergies de vide physiques aux deux bords sont Ui=3 si B A'(yi)<0. Il faut distinguer Ui des constantes Ti : Ti=Ui-Ji sigma_i peut être positive. Dire simplement « deux Ti négatives » serait inexact.

Le signe négatif des Ui n'est pas, à lui seul, une preuve de ghost dans le modèle à frontières physiques déclaré : la norme scalaire dérivée est positive et la preuve spectrale est positive. Il constitue toutefois une hypothèse physique du modèle et aucune origine microscopique de ces frontières n'est fournie. Les théorèmes ou intuitions sur une brane intermédiaire mobile de tension négative ne doivent pas être importés sans raccord : ici il n'y a aucune brane intermédiaire.

La contrainte centrale et les jonctions reconstruisent Lambda5, Ji et Ti pour chaque fond. Varier epsilon à x fixé change plusieurs constantes de l'action. Les masses propres décrivent bien des fluctuations à constantes fixées autour de chacun de ces fonds ; elles ne sont pas fictives. En revanche, le graphe ne représente pas la variation d'un seul paramètre physique à toutes les autres constantes fixées.

La platitude 4D est réglée ; aucune énergie noire n'est expliquée. Le rayon R0=L/pi est fixé en entrée. La reconstruction dimensionnelle au moyen de Mbar_Pl observé ne crée pas une nouvelle équation pour L : elle fixe M5 pour le L choisi.

## 6. Rétroaction finie versus contrôle de théorie effective

Les valeurs de champ au bord déjà enregistrées donnent, en unités dimensionnelles correctes :

| epsilon | |sigma_b|/M5^{3/2} | A_center |
|---:|---:|---:|
| 0,4 | 0,4894 | 0,0331 |
| 0,53 | 0,6207 | 0,0521 |
| 0,9 | 0,9239 | 0,1083 |

Le calcul non perturbatif du fond résout la limitation du développement en epsilon, mais ne protège pas automatiquement la troncature de l'action. Un champ approchant M5^{3/2} peut rendre pertinents des opérateurs supplémentaires du potentiel. Une masse ou un terme quartique de bord change U_i'' et donc les conditions de bord ; même sans modifier le fond exactement au point choisi, cela peut changer les masses et couplages de fluctuation.

A contrario, forte rétroaction n'est pas synonyme de courbure à l'échelle de Planck. Pour l'illustration R0=8,2 micromètres, L=pi R0 et Mbar_Pl=2,435e18 GeV, on obtient M5 voisin de 3,4e8 GeV, L M5 voisin de 4,5e19, et m_sigma=2/L voisin de 0,0153 eV. Les gradients et courbures sont donc extrêmement sous-Planckiens. Les corrections à plus de dérivées sont distinctes du problème de potentiel et de ses coefficients.

Le manuscrit peut valablement présenter l'action à deux dérivées et potentiel quadratique comme définition d'un modèle classique. Il ne doit pas appeler la branche entière « radiatively stable » ou « EFT certified ». Une symétrie, une analyse de corrections ou une origine UV est nécessaire pour ces affirmations plus fortes. Cela ne bloque pas le calcul classique limité annoncé.

## 7. Portée publiable conseillée et objections encore ouvertes

Portée défendable : une étude explicite et reproductible du spectre et des couplages à une brane d'un intervalle Einstein–scalaire symétrique, avec dérivation de la normalisation, développement analytique à faible rétroaction et continuation numérique à rétroaction finie. La preuve de positivité peut être donnée comme application d'un cadre connu et non comme découverte générale.

Objets à présenter avec précision : action complète, dictionnaire dimensionnel, données de reconstruction des paramètres, conditions de bord dépendant de la masse, orthogonalité et norme physique, amplitude d'échange relativement à G_T, profils du radion et au moins les premières excitations. L'affirmation « alourdir le radion augmente son couplage » doit être limitée à la famille et à la trajectoire de paramètres effectivement étudiées, ou démontrée avant d'être énoncée comme théorème.

Questions ouvertes qui limitent les conclusions, sans rendre le calcul interne invalide :

1. Originalité du coefficient ou de la famille précise par rapport à la littérature ; la précision numérique ne la démontre pas.
2. Protection du potentiel quadratique, des potentiels de bord affines et de l'absence de couplage direct matière–sigma.
3. Origine des énergies de vide négatives aux deux frontières et du réglage Minkowski.
4. Raccord à une compactification DDF et sélection indépendante d'une longueur.
5. Contraintes expérimentales : le spectre et les amplitudes permettent de définir le signal, mais une convolution expérimentale et un ajustement restent nécessaires pour une exclusion.

La revue pourrait juger les seuls benchmarks insuffisamment originaux. La formulation doit donc porter sur la contribution précise et vérifiable ; « un premier manuscrit théorique » est exact, « une découverte établie d'une cinquième dimension » ne l'est pas.

## Sources primaires consultées

- M. Olechowski, *Stability of multibrane models*, arXiv:2408.15343v2 (2025), https://arxiv.org/html/2408.15343v2. Utilisé pour la portée des précédents, l'opérateur spectral régulier et la distinction orbifold/intermediate branes. Les équations de la section 3 de cet avis ont été redérivées directement dans les conventions du dossier.
- J. Lesgourgues et L. Sorbo, *Goldberger–Wise variations: stabilizing brane models with a bulk scalar*, arXiv:hep-th/0310007, https://arxiv.org/pdf/hep-th/0310007. Référence du critère historique ; son existence ne suffit pas à revendiquer une extension nouvelle en 2026.

Statut final de l'avis : objections de convention et de norme résolues sous les hypothèses explicites ; preuve analytique de stabilité disponible ; limites de potentiel/UV, nouveauté, rayon et expérimentation ouvertes. Aucune modification du noyau partagé effectuée.
