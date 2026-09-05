# R64 — Addendum d’antériorité du no-go équivariant

**Date :** 4 septembre 2026  
**Objet :** comparaison du candidat `equivariant_nogo.md` avec les résultats
primaires les plus proches, sans revendication de priorité non vérifiée.

## 1. Verdict exécutif

Le candidat R64 contient une proposition mathématique correcte **sous ses
hypothèses locales**, mais son noyau O3/O7 n’est pas une nouveauté physique
large : Kaufmann--Monnee--Weigand--Wiesner ont déjà identifié en 2026 les
obstructions des limites de type II pour les O-types A et B. Dans leur exemple
\(K3\times T^2\) de type B, l’argument qui rend le réseau transverse
anti-invariant et projette ses modes \(C_4\) est presque exactement la moitié
« composantes préservées » du raisonnement R64.

Ce qui **peut** rester propre à R64, à condition de le démontrer globalement et
intégralement, est beaucoup plus étroit : une seule formule de parité

\[
\epsilon_C=-\epsilon_{\Omega_S}
\]

pour les charges propres des tubes de Clemens survivant dans le secteur
vectoriel fermé de \(C_4\), puis son application uniforme aux quatre cases

\[
\{O3/O7,O5/O9\}\times
\{\text{composantes préservées, composantes échangées}\}.
\]

La recherche primaire effectuée ici n’a pas trouvé cette **présentation
uniforme à quatre cases** chez Kaufmann et al., qui travaillent avec les
orientifolds O7/O3, ni chez Grimm--Louis, qui ne traitent pas les
dégénérescences, ni chez Hassfeld et al., qui travaillent dans le parent
\(\mathcal N=2\). Cette absence de collision ne prouve toutefois pas une
priorité. De plus, la conclusion est un corollaire court de la table de parité
de Grimm--Louis, du signe du cercle dans \(uv=t\), et de l’indice de Hodge.

```text
BROAD_ORIENTIFOLD_OBSTRUCTION_NOVELTY = FAIL
O3O7_TYPE_B_LATTICE_IDEA_NOVELTY      = FAIL_OR_VERY_LOW
O3O7_TYPE_A_OBSTRUCTION_NOVELTY       = FAIL
UNIFORM_FOUR_CASE_SIGN_FORMULA         = POSSIBLY_NEW_SYNTHESIS
O5O9_TYURIN_EXTENSION                  = OPEN_NOT_VALIDATED_PHYSICALLY
STANDALONE_THEOREM_PAPER               = NO
PROPOSITION_IN_GEOMETRY_PAPER          = CONDITIONAL_GO
```

## 2. Les quatre signes, et ce qui vient réellement de la littérature

Posons

\[
s=\epsilon_{\Omega_3}\in\{\pm1\},\qquad
\eta=\begin{cases}
+1,&Y_1,Y_2\text{ préservées},\\
-1,&Y_1,Y_2\text{ échangées}.
\end{cases}
\]

Grimm--Louis imposent \(s=-1\) pour O3/O7 et \(s=+1\) pour
O5/O9. Leurs tables 3.2 et 4.1 donnent les vecteurs issus de \(C_4\) dans
\(H^3_+\) pour O3/O7 et dans \(H^3_-\) pour O5/O9. La parité de la
3-forme qui porte un vecteur est donc

\[
q_{C_4}=-s.
\]

Le reste est la dérivation locale de R64. Dans \(uv=t\), l’échange des deux
branches envoie \(d\log u\) sur \(-d\log u\), d’où

\[
\epsilon_{\Omega_S}=s\eta,
\qquad
\epsilon_{\operatorname{Tub}(C)}=\epsilon_C\eta.
\]

Imposer \(\epsilon_{\operatorname{Tub}(C)}=q_{C_4}\) donne

\[
\boxed{\epsilon_C=-\epsilon_{\Omega_S}}.
\]

| Projection | Branches | \(s\) | \(\eta\) | \(\epsilon_{\Omega_S}\) | parité requise de \(C\) |
|---|---|---:|---:|---:|---:|
| O3/O7 | préservées | \(-1\) | \(+1\) | \(-1\), anti-symplectique | \(+1\), invariant |
| O3/O7 | échangées | \(-1\) | \(-1\) | \(+1\), symplectique | \(-1\), anti-invariant |
| O5/O9 | préservées | \(+1\) | \(+1\) | \(+1\), symplectique | \(-1\), anti-invariant |
| O5/O9 | échangées | \(+1\) | \(-1\) | \(-1\), anti-symplectique | \(+1\), invariant |

Dans chaque ligne, la parité requise est de type \((1,1)\). Dans les lignes
anti-invariantes, elle est orthogonale à une classe de Kähler moyennée. Dans
les lignes invariantes, si le réseau prolongeable stable \(L\) contient une
classe ample, une classe ample invariante appartient à \(L\), et toute classe
active de \(L^\perp\) lui est orthogonale. L’indice de Hodge donne alors
\(C^2<0\) pour \(C\ne0\).

Cette preuve est intrinsèque mais élémentaire. La nouveauté éventuelle ne peut
donc porter ni sur l’indice de Hodge, ni sur les parités de Grimm--Louis ; elle
porterait sur le **recollement de ces ingrédients par la tube map
équivariante**, avec une formulation et une preuve intégrales valables sur une
famille de Tyurin.

## 3. Collision précise avec \(K3\times T^2\)

### 3.1 O-type A de Kaufmann et al.

Dans la section 2.2 de la Partie I, Kaufmann et al. prennent

\[
\Omega_A=\Omega_p(-1)^{F_L}R,
\qquad R:z\mapsto-z
\]

sur le facteur \(T^2\). Les quatre points fixes de \(R\) donnent des O7
enveloppant la K3. La limite \(U\to i\infty\) dégénère le facteur torique.
Dans la description semistable de type II, les deux composantes sont
échangées et la double surface K3 est support de l’O7 : c’est la case O3/O7,
\(\eta=-1\).

La Partie I, définition 2, généralise cette terminologie : O-type A signifie
que le lieu O7 a du support sur une double surface. Pour une dégénérescence à
deux composantes, cela force leur échange et réduit l’intervalle dual à un
point. Dans leur exemple explicite de type II, la limite devient de type I,
donc à distance finie dans l’uplift F-théorie. La Partie II, annexe A.3,
reformule le même phénomène sur la corde EFT : la double surface disparaît et
la corde associée à la limite de type II disparaît également.

Conséquence pour R64 : le sous-énoncé « le secteur anti-invariant de
\(\sigma|_S=\mathrm{id}\) est nul » est vrai, mais physiquement **plus faible**
que l’antériorité. Dans une véritable O-type A à deux composantes, la couture
est un composant du lieu fixe ; l’action induite sur elle est l’identité. Le
cas d’une involution symplectique non triviale de type Nikulin n’est donc pas
le représentant générique à invoquer pour cette branche. Surtout, Kaufmann et
al. ont déjà conclu que la limite de type II elle-même ne survit pas comme
limite à distance infinie après l’uplift quantique.

### 3.2 O-type B de Kaufmann et al.

Dans le même produit,

\[
\Omega_B=\Omega_p(-1)^{F_L}\rho,
\]

où \(\rho\) est anti-symplectique sur K3. Les O7 enveloppent
\(C_I\times T^2\), avec \(C_I\) courbes fixes de \(\rho\). Pour la limite du
module complexe \(U\) de \(T^2\), les composantes de la fibre centrale sont
préservées et l’O7 ne contient pas toute la double surface : c’est la case
O3/O7, \(\eta=+1\).

Après changement de base, le \(T^2\) acquiert une fibre \(I_2\) et la double
surface comporte deux copies de K3 (une seule doit être comptée). Avant
projection, des modes \(C_4\) proviennent de sous-réseaux de la polarisation
et du réseau transverse. Kaufmann et al. montrent que
\(\Lambda_{\mathrm{pol}}\) est invariant tandis que
\(\Lambda_{\mathrm{trans}}\) est anti-invariant sous \(\rho\) ; comme
\(C_4\) est pair pour O3/O7, les modes transverses sont projetés. Leur note 6
donne déjà l’argument de Hodge : un vecteur transverse invariant sous une
involution anti-symplectique serait de type \((1,1)\), donc dans le réseau de
Picard, contradiction sauf zéro.

Il s’agit d’une collision directe avec la logique R64

\[
L^\perp\cap H^2(S,\mathbb Z)^+=0
\]

dans le cas où \(L\) coïncide avec la polarisation et où le membre est assez
général. Kaufmann et al. utilisent cette projection pour obtenir une corde
EFT sous-critique et concluent à une obstruction de Kähler. R64 ne peut donc
pas revendiquer comme nouveau le message « l’orientifold O-type B projette le
secteur transverse de la K3 ».

La généralisation restante est : remplacer le produit \(K3\times T^2\) par
une famille de Tyurin quelconque, ne pas supposer
\(NS(S)=L\), et conclure non pas nécessairement à l’annulation du secteur,
mais à sa négativité définie dès que \(L\) est stable et contient une ample.
Cette extension est raisonnable, mais c’est encore un corollaire de l’indice
de Hodge plutôt qu’un nouveau mécanisme physique.

## 4. Comparaison avec les O-types A/B généraux de 2603.12315/13470

| Question | Kaufmann et al. | Candidat R64 | Verdict d’antériorité |
|---|---|---|---|
| Classification O-type | A : O7 supporté sur une double surface et graphe non fixé point par point ; B : pas de tel support et graphe fixé point par point | « branches échangées/préservées » | Pour deux composantes O3/O7, c’est essentiellement la même dichotomie ; ne pas la renommer comme nouvelle |
| O-type A, type II | Uplift F-théorie de type I à distance finie ; suppression de la double surface et de la corde EFT | aucun tube propre survivant de norme \(\ge0\) | Résultat R64 plus étroit et physiquement dominé par l’antériorité |
| O-type B, type II | Troncation des modes par parité ; corde sous-critique ; obstruction de Kähler | réseau actif propre survivant négatif défini | Même idée de réseau dans l’exemple \(K3\times T^2\), extension géométrique possible |
| Portée quantique | corrections \(g_s\), corrections de Kähler/instantons, co-scaling requis | énoncé topologique/classique sur charges fermées \(C_4\) | R64 ne prouve pas l’obstruction quantique complète et ne doit pas employer ce vocabulaire sans qualification |
| O5/O9 | non traité par ces deux articles, centrés sur O7/O3 et F-théorie | deux lignes supplémentaires de la table | Lacune bibliographique possible, mais validation physique séparée indispensable |

La Partie II va en outre au-delà du seul exemple produit : pour les limites
regular-fiber de type II, la projection réduit le réseau des deux-formes de la
double surface d’une signature \((3,3+n)\) dans le parent à une signature
\((1,b)\), rend la corde candidate sous-critique, et conduit à une obstruction
de Kähler. Ce résultat rend impossible toute revendication R64 du type
« première obstruction générale des limites de Tyurin orientifoldées ».

## 5. Comparaison avec Hassfeld et al.

Hassfeld--Monnee--Weigand--Wiesner étudient le parent Type IIB
\(\mathcal N=2\), sans quotient orientifold. Pour une dégénérescence de
Tyurin \(X_1\cup_Z X_2\), ils identifient

\[
\operatorname{Gr}_2\simeq
H^2(Z)/(\operatorname{im}i^*+\operatorname{im}j^*)
\simeq\Lambda_{\mathrm{trans}},
\]

de signature \((2,b)\). La 3-classe est décrite par un tube dont la limite est
une fibration \(S^1\) au-dessus d’une classe \(C_0\subset Z\). Leur argument de
multi-enroulement requiert assez de modules de déformation ; par adjonction il
sélectionne le régime

\[
C_0^2\ge0\quad\Longleftrightarrow\quad g(C_0)\ge1.
\]

Le cas \(C_0^2=0\) n’est donc pas le critère complet. Les auteurs proposent
que les indices des multiples soient encodés par des formes
(mock-)modulaires ; cette partie est explicitement conjecturale.

R64 ne remplace ni ne réfute ce mécanisme. Il demande : parmi ces charges du
parent, lesquelles sont des états propres dans le secteur vectoriel fermé de
\(C_4\) qui survit au quotient ? Sous les hypothèses du théorème, ce secteur
est négatif défini, donc disjoint du cône \(C_0^2\ge0\). C’est une
**application orientifoldée** du mécanisme de Hassfeld et al., non une preuve
indépendante de stabilité BPS, de non-annulation des indices, ni de l’absence
de toute tour.

## 6. Comparaison avec Grimm--Louis et statut de O5/O9

Grimm--Louis établissent les données de départ :

- O3/O7 : \(\sigma^*\Omega_3=-\Omega_3\), vecteurs fermés issus de
  \(C_4\) sur \(H^3_+\) ;
- O5/O9 : \(\sigma^*\Omega_3=+\Omega_3\), vecteurs fermés issus de
  \(C_4\) sur \(H^3_-\).

Ils ne traitent ni les dégénérescences de Tyurin, ni la parité du cercle de
plomberie, ni une tube map de Clemens équivariante, ni le cône
\(C^2\ge0\). La formule uniforme de R64 ne leur est donc pas attribuable telle
quelle. Elle se déduit cependant très rapidement de leurs tables une fois le
calcul local \(uv=t\) fourni.

Les deux lignes O5/O9 sont la partie bibliographiquement la moins collisionnée
dans le corpus inspecté, mais aussi la moins validée :

1. Kaufmann et al. ne les couvrent pas par leur analyse F-théorie O7/O3 ;
2. il faut vérifier que l’involution du **total espace** réalise réellement la
   projection O5/O9 choisie et que son lieu fixe/tadpole est admissible ;
3. il faut vérifier l’action orientifold complète sur l’état D3, et pas
   seulement la parité de la forme harmonique couplée à \(C_4\) ;
4. les secteurs ouverts, brane--image, relatifs et non propres ne sont pas
   classifiés ;
5. la survie d’une limite à distance infinie et sa physique quantique ne
   découlent pas du seul no-go de réseau.

Ainsi, « extension O5/O9 » doit rester **proposition conditionnelle**, jamais
« première obstruction O5/O9 » avant une recherche ciblée supplémentaire et
une validation du quotient global.

## 7. Formulation publiable minimale

Une formulation prudente possible est :

> **Proposition (obstruction de parité des tubes fermés).** Soit une
> dégénérescence de Tyurin projective à deux composantes, munie d’une
> involution holomorphe au-dessus de l’identité de la base et d’une tube map
> équivariante. Supposons que le réseau prolongeable soit stable et contienne
> une classe ample lorsque la parité survivante est invariante. Pour les
> projections standards O3/O7 ou O5/O9, toute charge propre active dont le
> tube appartient au secteur vectoriel fermé survivant de \(C_4\) a carré
> strictement négatif. Elle ne peut donc réaliser la classe de carré
> non négatif utilisée dans le mécanisme de multi-enroulement de Hassfeld et
> al.

Puis ajouter immédiatement :

> Cette proposition est une synthèse de la parité du secteur \(C_4\), du
> signe local du cercle de plomberie et de l’indice de Hodge. Elle ne constitue
> pas une nouvelle obstruction quantique générale ; pour O3/O7, elle recoupe
> les obstructions O-type A/B de Kaufmann et al., notamment la projection du
> réseau transverse dans leur exemple \(K3\times T^2\).

La proposition mérite une place dans un article seulement si R64 fournit en
plus :

- l’involution du total espace relatif et son action sur \(t\) ;
- la preuve intégrale de l’équivariance de la tube map, y compris les
  saturations/cosets de discriminant ;
- l’identification exacte du réseau prolongeable \(L\) dans le modèle R63 ;
- la vérification que les charges physiques considérées sont bien des états
  propres fermés et que la projection D3 est cohérente ;
- une section explicite « différence avec 2603.12315/13470 ».

Sans ces éléments, le résultat reste une note d’audit utile, pas une
substance suffisante pour un article autonome.

## 8. Sources primaires utilisées

1. T. W. Grimm, J. Louis, *The effective action of N=1 Calabi--Yau
   orientifolds*, Nucl. Phys. B **699** (2004) 387--426,
   [arXiv:hep-th/0403067](https://arxiv.org/abs/hep-th/0403067),
   tables 3.2 et 4.1,
   [doi:10.1016/j.nuclphysb.2004.08.005](https://doi.org/10.1016/j.nuclphysb.2004.08.005).
2. B. Hassfeld, J. Monnee, T. Weigand, M. Wiesner, *Emergent Strings in
   Type IIB Calabi--Yau Compactifications*, JHEP **01** (2026) 140,
   [arXiv:2504.01066v3](https://arxiv.org/abs/2504.01066), §§2.2, 3.1,
   [doi:10.1007/JHEP01(2026)140](https://doi.org/10.1007/JHEP01(2026)140).
3. L. Kaufmann, J. Monnee, T. Weigand, M. Wiesner, *Quantum obstructions for
   N=1 infinite distance limits — Part I: \(g_s\) obstructions*,
   [arXiv:2603.12315v2](https://arxiv.org/abs/2603.12315), §§2.2, 3.3,
   4.2, [doi:10.1103/blb9-hrwd](https://doi.org/10.1103/blb9-hrwd).
4. L. Kaufmann, J. Monnee, T. Weigand, M. Wiesner, *Quantum obstructions for
   N=1 infinite distance limits — Part II: Kähler obstructions*,
   [arXiv:2603.13470](https://arxiv.org/abs/2603.13470), §§2.2, 5.1 et
   app. A.3, [doi:10.1103/ypyx-mg6r](https://doi.org/10.1103/ypyx-mg6r).

Toutes les comparaisons ci-dessus sont limitées à ces sources primaires. Le
verdict de nouveauté est un état de recherche au 4 septembre 2026, non une
preuve bibliographique d’absence d’antériorité.

