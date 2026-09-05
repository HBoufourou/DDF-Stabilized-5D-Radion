# R64 — Critère général de découpe anticanonique donnant une dégénérescence de Tyurin stricte

**Voie A : théorème général au-delà de POLY944/sigma5**  
**Date :** 4 septembre 2026  
**Périmètre :** géométrie algébrique et torique. Aucun rayon métrique, aucune
échelle micrométrique et aucune tour physique ne sont déduits ici.

## 1. Verdict

La preuve quasi-Fano de R63 n'est pas un accident propre aux nombres de
POLY944. Elle est l'instance d'un critère général très simple : une coupe
anticanonique transverse d'une famille ambiante semi-stable à deux composantes
est une dégénérescence de Tyurin stricte dès que les deux composantes
ambiantes, leur intersection et une fibre ambiante générale ont une
cohomologie de faisceau structural triviale en degré positif.

Dans le cas torique, ces annulations sont automatiques. Il reste alors une
porte finie et vérifiable :

1. un éventail relatif lisse et projectif avec fonction primitive de base ;
2. exactement deux rayons verticaux de multiplicité un ;
3. une coupe relative anticanonique ;
4. un certificat de lissité et de transversalité simultané sur le total, les
   deux composantes et leur intersection.

Sous ces hypothèses, la fibre centrale est automatiquement une union de deux
quasi-Fano le long d'un Calabi–Yau anticanonique commun, le produit des deux
fibrés normaux est trivial et le morphisme logarithmique est saturé.

Ce résultat est utile pour rechercher d'autres exemples DDF sans répéter les
calculs cohomologiques de R63. Il ne faut cependant pas le présenter comme un
nouveau théorème profond : ses ingrédients sont standards et la preuve est une
combinaison élémentaire d'adjonction, de deux suites exactes, de l'annulation
torique et de la dualité de Serre. L'apport potentiellement nouveau demeure
l'application complètement certifiée à un éventail explicite non standard,
ou à une classe nouvelle d'éventails qui serait produite par un scan.

## 2. Conventions

On travaille sur un corps algébriquement clos \(k\) de caractéristique zéro.
On note \((\Delta,0)\) une courbe lisse pointée, rétrécie autour de \(0\) de
façon que \(K_\Delta\) et le diviseur \((0)\) soient triviaux comme fibrés.

Une variété projective connexe \(Z\) sera dite **\(\mathcal O\)-acyclique** si

\[
H^0(Z,\mathcal O_Z)=k,
\qquad H^q(Z,\mathcal O_Z)=0\quad(q>0).
\]

Pour le terme « Calabi–Yau », on utilise la convention de
Doran–Harder–Thompson : variété lisse projective, canonique trivial, et
\(H^q(\mathcal O)=0\) pour \(0<q<\dim Z\). Une quasi-Fano est une variété
lisse projective \(Y\) telle que \(H^q(Y,\mathcal O_Y)=0\) pour tout \(q>0\)
et dont le système anticanonique contient un Calabi–Yau lisse.

Le mot « stricte » signifie ici que toutes les conditions de cette définition
sont effectivement démontrées ; il ne signifie pas que \(-K_Y\) est gros ou
ample.

## 3. Lemme cohomologique élémentaire

### Lemme 3.1 — acyclicité du complément d'un diviseur

Soient \(V\) une variété lisse projective connexe et \(T\subset V\) un
diviseur lisse connexe. Si \(V\) et \(T\) sont \(\mathcal O\)-acycliques,
alors

\[
H^q\bigl(V,\mathcal O_V(-T)\bigr)=0
\qquad\text{pour tout }q.
\]

#### Preuve

La suite du diviseur est

\[
0\longrightarrow\mathcal O_V(-T)
\longrightarrow\mathcal O_V
\longrightarrow\mathcal O_T
\longrightarrow0.
\]

La restriction \(H^0(V,\mathcal O_V)=k\to H^0(T,\mathcal O_T)=k\) envoie
\(1\) sur \(1\), donc est un isomorphisme. Tous les groupes supérieurs des
deux derniers termes sont nuls. La suite longue de cohomologie donne
l'annulation annoncée dans tous les degrés. \(\square\)

### Lemme 3.2 — transfert d'acyclicité à la coupe résiduelle

Supposons en plus que \(\dim V=n+1\) et qu'un diviseur lisse \(Y\subset V\)
vérifie

\[
K_V+Y\sim -T.
\]

Alors

\[
H^q(Y,\mathcal O_Y)=0\quad(q>0),
\qquad H^0(Y,\mathcal O_Y)=k.
\]

#### Preuve

La dualité de Serre et le lemme 3.1 donnent, pour tout \(a\),

\[
\begin{aligned}
H^a\bigl(V,\mathcal O_V(-Y)\bigr)^\vee
&\simeq
H^{n+1-a}\bigl(V,\mathcal O_V(K_V+Y)\bigr)\\
&\simeq H^{n+1-a}\bigl(V,\mathcal O_V(-T)\bigr)=0.
\end{aligned}
\]

La suite

\[
0\longrightarrow\mathcal O_V(-Y)
\longrightarrow\mathcal O_V
\longrightarrow\mathcal O_Y
\longrightarrow0
\]

identifie alors \(H^q(Y,\mathcal O_Y)\) à
\(H^q(V,\mathcal O_V)\), ce qui conclut. \(\square\)

### Remarque sur la minimalité

Pour le seul lemme 3.2, l'hypothèse exactement utilisée est

\[
H^q(V,\mathcal O_V)=0\ (q>0),\quad H^0(V,\mathcal O_V)=k,
\quad
H^q(V,\mathcal O_V(-T))=0\ (q\ge0).
\]

L'acyclicité séparée de \(V\) et \(T\) est un critère géométrique plus facile
à vérifier, et elle produit automatiquement la dernière ligne. Aucune
positivité de \(-K_Y\), aucun calcul de polytope et aucune hypothèse torique ne
sont nécessaires aux deux lemmes.

## 4. Théorème général de découpe anticanonique

### Théorème 4.1 — critère ambiant à deux composantes

Soit \(n\ge2\). Soit

\[
g:\mathfrak V\longrightarrow\Delta
\]

une famille projective semi-stable de dimension relative \(n+1\), avec
\(\mathfrak V\) lisse, lisse sur \(\Delta^*=\Delta\setminus\{0\}\), et

\[
\mathfrak V_0=V_1\cup_T V_2,
\]

où \(V_1,V_2\) sont lisses et se rencontrent transversalement le long du
diviseur lisse connexe \(T\). Supposons :

1. une fibre ambiante lisse générale \(A=\mathfrak V_t\), les variétés
   \(V_1,V_2\) et \(T\) sont \(\mathcal O\)-acycliques ;
2. \(\mathfrak Y\subset\mathfrak V\) est un diviseur relatif anticanonique,
   
   \[
   \mathcal O_{\mathfrak V}(\mathfrak Y)
   \simeq\omega_{\mathfrak V/\Delta}^{-1};
   \]
3. \(\mathfrak Y\) est lisse et la paire
   \(\mathfrak Y+V_1+V_2\) est à croisements normaux simples ; de façon
   équivalente ici, \(\mathfrak Y\) rencontre transversalement
   \(V_1,V_2,T\).

Posons

\[
Y_i=\mathfrak Y\cap V_i,
\qquad S=\mathfrak Y\cap T=Y_1\cap Y_2.
\]

Alors :

1. \(f=g|_{\mathfrak Y}:\mathfrak Y\to\Delta\) est projectif et
   semi-stable, lisse sur \(\Delta^*\), avec
   
   \[
   \mathfrak Y_0=Y_1\cup_S Y_2
   \]
   
   réduite SNC ;
2. chaque fibre générale \(\mathfrak Y_t\) est un Calabi–Yau de dimension
   \(n\) ;
3. \(S\) est un Calabi–Yau lisse de dimension \(n-1\) ;
4. pour \(i=1,2\),
   
   \[
   -K_{Y_i}\sim S,
   \qquad H^q(Y_i,\mathcal O_{Y_i})=0\quad(q>0),
   \]
   
   donc \(Y_i\) est quasi-Fano ;
5. le produit des fibrés normaux est trivial :
   
   \[
   N_{S/Y_1}\otimes N_{S/Y_2}\simeq\mathcal O_S;
   \]
6. munie des structures logarithmiques divisorielles, la famille est
   log-lisse et saturée ; en particulier elle est d-semi-stable ;
7. \(f\) est une dégénérescence de Tyurin stricte au sens
   Doran–Harder–Thompson.

### Preuve

#### Étape 1 — forme locale et platitude

La semi-stabilité de \(g\) et la transversalité donnent, après changement de
coordonnées étale ou analytique, les modèles

\[
t=u,
\qquad t=v,
\qquad t=uv
\]

sur \(\mathfrak Y\). Ainsi \(t\) est un non-diviseur de zéro,
\(f\) est plat, et la fibre centrale est réduite avec exactement les deux
composantes \(Y_1,Y_2\), qui se coupent transversalement le long de \(S\).

#### Étape 2 — identités d'adjonction

Comme \(V_1+V_2=g^*(0)\), sa restriction à chaque composante est triviale et

\[
V_i|_{V_i}\sim-T.
\]

L'adjonction dans \(\mathfrak V\), avec
\(\mathfrak Y\sim-K_{\mathfrak V/\Delta}\), donne

\[
K_{V_i}+Y_i\sim -T.
\]

En restreignant à \(Y_i\),

\[
K_{Y_i}\sim-S.
\]

En appliquant l'adjonction à \(T\subset V_i\),

\[
K_T+S=(K_{V_i}+T+Y_i)|_T\sim0.
\]

Enfin, sur une fibre lisse \(A\), la coupe
\(\mathfrak Y_t\) appartient à \(|-K_A|\), donc

\[
K_{\mathfrak Y_t}\simeq\mathcal O_{\mathfrak Y_t}.
\]

#### Étape 3 — cohomologie des deux quasi-Fano

Les lemmes 3.1 et 3.2, appliqués à \((V_i,T,Y_i)\), donnent

\[
H^q(Y_i,\mathcal O_{Y_i})=0\quad(q>0),
\qquad H^0(Y_i,\mathcal O_{Y_i})=k.
\]

Le dernier groupe prouve la connexité. Comme \(Y_i\) est lisse, ses
composantes irréductibles seraient ouvertes et fermées ; il est donc
irréductible.

#### Étape 4 — la couture est Calabi–Yau

Puisque \(S\sim-K_T\), la suite

\[
0\longrightarrow\mathcal O_T(K_T)
\longrightarrow\mathcal O_T
\longrightarrow\mathcal O_S
\longrightarrow0
\]

et la dualité de Serre sur le \(n\)-fold \(T\) donnent

\[
H^0(S,\mathcal O_S)=k,
\qquad
H^q(S,\mathcal O_S)=0\quad(0<q<n-1),
\qquad
H^{n-1}(S,\mathcal O_S)=k.
\]

Avec \(K_S\simeq\mathcal O_S\), ceci prouve que \(S\) est Calabi–Yau.
Pour \(n=3\), \(S\) est une K3.

#### Étape 5 — les fibres générales sont Calabi–Yau

Sur \(A\), on a la suite anticanonique

\[
0\longrightarrow\mathcal O_A(K_A)
\longrightarrow\mathcal O_A
\longrightarrow\mathcal O_{\mathfrak Y_t}
\longrightarrow0.
\]

L'acyclicité de \(A\) et la dualité de Serre donnent

\[
H^q(\mathfrak Y_t,\mathcal O)=0\quad(0<q<n),
\qquad H^n(\mathfrak Y_t,\mathcal O)=k.
\]

Avec le canonique trivial, c'est la condition Calabi–Yau annoncée.

#### Étape 6 — normales et logarithmes

Dans \(\mathfrak Y\),

\[
Y_1+Y_2=f^*(0).
\]

En restreignant à \(S\),

\[
\begin{aligned}
N_{S/Y_1}\otimes N_{S/Y_2}
&\simeq
\mathcal O_{\mathfrak Y}(Y_2)|_S
\otimes\mathcal O_{\mathfrak Y}(Y_1)|_S\\
&\simeq\mathcal O_{\mathfrak Y}(Y_1+Y_2)|_S
\simeq\mathcal O_S.
\end{aligned}
\]

Sur \(S\), la carte caractéristique est

\[
\mathbb N\longrightarrow\mathbb N^2,
\qquad1\longmapsto(1,1).
\]

Son conoyau en groupes est libre. La carte est primitive et saturée. Le
faisceau \(T^1\) de la fibre centrale est précisément le produit des deux
normales ci-dessus ; il est trivial, avec la section de lissage fournie par
\(t\). Ceci prouve la log-lissité saturée et la d-semistabilité. Toutes les
conditions de Tyurin sont maintenant vérifiées. \(\square\)

## 5. Corollaire torique fini

### Corollaire 5.1 — porte combinatoire/anticanonique

Soit \(N'\simeq\mathbb Z^{n+2}\), soit
\(\ell\in M'=\operatorname{Hom}(N',\mathbb Z)\) primitive, et soit
\(\Sigma\) un éventail rationnel. Supposons :

**T1 — régularité.** Tous les cônes maximaux pertinents sont unimodulaires ;
\(X_\Sigma\) est lisse.

**T2 — deux rayons verticaux réduits.** Pour les générateurs primitifs des
rayons,

\[
\ell(v_\rho)=0
\]

sauf pour exactement deux rayons \(p,m\), pour lesquels

\[
\ell(v_p)=\ell(v_m)=1.
\]

Le cône \(\langle v_p,v_m\rangle\) appartient à \(\Sigma\).

**T3 — propreté et projectivité relatives.** Le support vérifie

\[
|\Sigma|=\ell^{-1}(\mathbb R_{\ge0}),
\]

et \(\Sigma\) admet une fonction de support intégrale strictement convexe
relative. Le morphisme torique

\[
g:X_\Sigma\longrightarrow\mathbb A^1
\]

est alors propre et projectif.

**T4 — coupe anticanonique.** Un système linéaire

\[
W\subset H^0(X_\Sigma,\omega^{-1}_{X_\Sigma/\mathbb A^1})
\]

contient un ouvert de sections \(s\) tel que \(\mathfrak Y_s=(s=0)\) soit
lisse et rencontre transversalement les quatre strates

\[
X_\Sigma,quad D_p,quad D_m,quad D_p\cap D_m.
\]

Alors tout \(s\) dans cet ouvert définit une dégénérescence de Tyurin stricte
de Calabi–Yau \(n\)-dimensionnels.

#### Justification

Le caractère \(\chi^\ell\) vérifie

\[
\operatorname{div}(\chi^\ell)=D_p+D_m.
\]

La fibre torique centrale est donc réduite et possède exactement deux
composantes. La régularité donne les cartes \(t=u,t=v,t=uv\). Les étoiles de
\(p,m\) et \(\langle p,m\rangle\), quotientées par leurs rayons, donnent des
variétés toriques lisses complètes \(V_p,V_m,T\). La fibre torique générale
est elle aussi lisse et complète, la primitivité de \(\ell\) assurant la
connexité. Toutes ces variétés sont \(\mathcal O\)-acycliques. Le théorème 4.1
s'applique.

### Comment certifier T4 sans supposer le système complet

La base-liberté de \(-K\) suffit mais n'est pas nécessaire. Une sous-famille
comme sigma5 peut passer T4 par le certificat stratifié suivant :

1. calculer exactement le lieu de base de \(W\) sur chacune des strates ;
2. appliquer Bertini hors de ces lieux de base ;
3. sur chaque lieu de base, exhiber un coefficient et une dérivée transverse
   qui ne s'annule nulle part, les autres termes n'annulant pas ce jet ;
4. vérifier que les quatre conditions sont satisfaites simultanément sur un
   même ouvert non vide de coefficients.

Une simple ligne imprimée « smooth » ne suffit pas : il faut soit une preuve
de Bertini avec jet explicite, soit une saturation exacte de l'idéal
jacobien pour une spécialisation et un argument d'ouverture.

## 6. Renforcement optionnel : normales individuellement triviales

Le théorème ne donne en général que

\[
N_{S/Y_1}\otimes N_{S/Y_2}\simeq\mathcal O_S.
\]

Pour obtenir les deux trivialités séparées, il suffit d'ajouter : pour chaque
\(i\), le diviseur \(T\subset V_i\) est une fibre réduite d'un morphisme

\[
h_i:V_i\longrightarrow C_i
\]

vers une courbe lisse. Alors

\[
\mathcal O_{V_i}(T)|_T\simeq\mathcal O_T
\]

et, par transversalité du carré \(S=Y_i\cap T\),

\[
N_{S/Y_i}\simeq N_{T/V_i}|_S\simeq\mathcal O_S.
\]

Dans un modèle torique, cette hypothèse se certifie par un caractère primitif
dont \(T\) est une fibre de multiplicité un, avec une fibre opposée disjointe.
C'est exactement le renforcement particulier trouvé pour POLY944/sigma5.

## 7. Application mécanique à R63

Le dictionnaire entre le corollaire et les données déjà certifiées est :

| Porte générale | Donnée POLY944/sigma5 | Verdict |
|---|---|---:|
| rang de \(N'\) | \(5=n+2\), donc \(n=3\) | oui |
| éventail lisse | 28 cônes maximaux, déterminants \(\pm1\) | oui |
| caractère primitif | ordres \((0^9,1,1)\) | oui |
| deux composantes | \(D_p,D_m\), \(t=pm\) | oui |
| couture non vide | huit cônes contenant \(p,m\) | oui |
| projectivité relative | hauteurs cohérentes et complétion à 48 cônes | oui |
| degré anticanonique | \((4,4,3,2,-1,0)=\sum_\rho[D_\rho]\) | oui |
| transversalité | Bertini + jet \(c x_0^2E^2x_6\), \(c\ne0\) | oui |
| étoiles complètes | \(16/20/8\) cônes pour \(V_p,V_m,T\) | oui |
| normales séparées | deux caractères primitifs vers \(\mathbb P^1\) | oui |

Ainsi le résultat strict de R63 se déduit du critère général une fois les
données finies de cette table établies. Les valeurs \(16,20,8\), les degrés
de Cox et la forme précise du jet restent propres à POLY944 ; le raisonnement
qui les transforme en quasi-Fano et en Tyurin stricte ne l'est pas.

## 8. Ce que le théorème donne encore, et ce qu'il ne donne pas

### 8.1 Conséquences générales certaines

- Le canonique relatif de \(\mathfrak Y/\Delta\) est trivial.
- La monodromie locale est unipotente, puisque la famille est semi-stable.
- Comme il n'existe aucune intersection triple de composantes, le complexe de
  poids de \(H^n\) n'a que les poids \(n-1,n,n+1\). On obtient la borne
  
  \[
  N^2=0.
  \]
- La classe anticanonique de chaque composante est effective ; aucune
  amplitude ou grosseur n'est forcée.

### 8.2 Données non déterminées par le critère

- \(N\) peut être nul ou non nul ; le mot « type II » au sens strict exige
  encore \(N\ne0\).
- En dimension trois, le sous-type \(\mathrm{II}_b\) dépend du rang de l'image
  de restriction
  
  \[
  H^2(Y_1)\oplus H^2(Y_2)\longrightarrow H^2(S).
  \]
  
  Le critère ne force donc pas \(\mathrm{II}_{18}\).
- Il ne calcule pas la matrice intégrale de Gauss–Manin ni sa forme normale de
  Smith.
- Il ne donne aucune métrique Ricci-plate, aucune relation \(R(t)\), aucune
  valeur propre du Laplacien, aucune masse \(n/R\), aucun invariant BPS et
  aucune stabilité quantique.
- Il n'implique pas une projection orientifold compatible.

## 9. Contre-exemples et rôle exact des hypothèses

### 9.1 Sans la classe anticanonique, la couture n'est pas anticanonique

Prenons \(V=\mathbb P^{n+1}\), \(T=H\) un hyperplan, et une hypersurface
lisse \(Y_d\) de degré \(d\). Alors

\[
K_V+Y_d\sim(d-n-2)H,
\]

tandis que \(-T=-H\). L'identité nécessaire vaut uniquement pour
\(d=n+1\). Sur \(Y_d\),

\[
-K_{Y_d}=(n+2-d)H|_{Y_d},
\qquad S=T\cap Y_d\sim H|_{Y_d}.
\]

Donc \(S\in|-K_{Y_d}|\) seulement si \(d=n+1\). La lissité et l'acyclicité de
l'ambiant ne compensent pas un mauvais degré.

### 9.2 Sans acyclicité, l'identité de classes ne suffit pas

Soit \(E\) une courbe elliptique,

\[
V=E\times\mathbb P^n,
\qquad T=E\times H.
\]

En notant encore \(H\) le tiré en arrière de l'hyperplan,

\[
-K_V-T=nH.
\]

Un membre lisse est

\[
Y=E\times F_n,
\]

où \(F_n\subset\mathbb P^n\) est une hypersurface lisse de degré \(n\). On a
bien \(K_V+Y=-T\) et \(-K_Y=S=T\cap Y\), mais Künneth donne

\[
H^1(Y,\mathcal O_Y)\supseteq H^1(E,\mathcal O_E)\simeq k.
\]

Ainsi \(Y\) n'est pas quasi-Fano. C'est un contre-exemple direct à toute
affirmation selon laquelle l'adjonction seule prouverait le mot quasi-Fano.

### 9.3 Sans transversalité, les mêmes classes peuvent être singulières

Dans \(\mathbb P^{n+1}\), un membre spécial de degré \(n+1\) peut être
réductible, par exemple

\[
Y=H_1\cup F_n.
\]

Il possède la bonne classe \(-K_V-T\) pour \(T=H\), mais il n'est ni lisse ni
irréductible. Plus près de R63, choisir
\(A^0_{44}=B_{22}^2\) rend l'équation de couture

\[
x_7^2B_{22}^2+c x_0^2
\]

factorisable sur \(\mathbb C\). La condition « coefficients généraux » est
donc une hypothèse mathématique réelle, pas une précaution éditoriale.

### 9.4 Sans multiplicité un, la famille n'est pas semi-stable

Dans un espace total lisse, le morphisme local

\[
t=u^k v\qquad(k>1)
\]

a une fibre centrale contenant \(\{u=0\}\) avec multiplicité \(k\). Elle
n'est pas réduite. Le modèle

\[
xy=t^k
\]

possède quant à lui le bon support réduit, mais son espace total est singulier
à l'origine pour \(k>1\) et requiert réduction semi-stable. Les coefficients
\(\ell(v_p)=\ell(v_m)=1\) ne peuvent donc pas être remplacés par de simples
coefficients positifs.

### 9.5 Avec trois composantes, on sort de la définition de Tyurin

Dans le modèle local \(t=uvw\), la fibre centrale a trois composantes. Sur la
composante \(u=0\), l'adjonction donne en général

\[
-K_{Y_u}\sim S_{uv}+S_{uw},
\]

et non un unique diviseur anticanonique commun aux deux côtés. On obtient une
dégénérescence semi-stable à plusieurs composantes, mais pas une
dégénérescence de Tyurin à deux pièces.

### 9.6 Les normales séparées n'ont pas à être triviales

Soit \(L\) un fibré en droites non trivial sur une variété lisse \(S\). Dans
le fibré total \(L\oplus L^{-1}\), l'équation globale

\[
xy=t
\]

donne localement une famille SNC à deux branches. Les deux normales de la
section \(S\) sont \(L\) et \(L^{-1}\). Leur produit est trivial, mais aucune
des deux ne l'est nécessairement. La trivialité individuelle de R63 est donc
une propriété supplémentaire de ses fibrations toriques vers
\(\mathbb P^1\), pas une conséquence formelle de Tyurin.

### 9.7 Quasi-Fano ne signifie pas weak Fano

Le critère ne force pas \((-K_{Y_i})^n>0\). R63 lui-même fournit un exemple où

\[
-K_{Y_i}\sim S,
\qquad (-K_{Y_i})^3=0.
\]

Les composantes sont quasi-Fano au sens cohomologique utilisé pour Tyurin,
mais ne sont pas weak Fano. Remplacer ces deux expressions l'une par l'autre
rendrait le théorème faux.

## 10. Classification honnête de l'originalité

| Élément | Nature | Formulation recommandée |
|---|---|---|
| construction de dégénérescences semi-stables par géométrie torique | standard | citer Hu |
| définition quasi-Fano/Tyurin | standard | citer Doran–Harder–Thompson |
| \(H^{>0}(\mathcal O)=0\) pour une variété torique complète | standard | citer une référence torique |
| adjonction, dualité de Serre et suites de diviseurs | standard | ne pas revendiquer comme nouveau |
| lemme 3.1 + lemme 3.2 assemblés | élémentaire | présenter comme proposition de travail |
| porte finie T1–T4 | synthèse réutilisable | utile méthodologiquement, nouveauté non revendiquée |
| application exacte au fan POLY944/sigma5 | potentiellement nouvelle | défendre par données intrinsèques, pas par le nom local |
| double preuve de l'acyclicité dans cet exemple | potentiellement nouvelle comme certificat | distinguer preuve conceptuelle et contre-calcul EMS |
| normales individuellement triviales dans cet exemple | donnée géométrique spécifique | peut renforcer l'application |
| toute famille issue de la porte aurait \(\mathrm{II}_{18}\) | faux | recalculer le réseau de restriction dans chaque cas |

Une recherche ciblée n'a pas trouvé cette proposition sous exactement la même
forme, mais une absence de résultat de recherche ne prouve jamais la
nouveauté. Les travaux de Hu construisent déjà des dégénérescences
semi-stables de variétés toriques et de leurs hypersurfaces, y compris des
exemples à deux composantes. Doran–Harder–Thompson fixent déjà la notion de
Tyurin utilisée ici. Il serait donc imprudent de vendre le théorème 4.1 seul
comme contribution originale. Sa valeur est de transformer une vérification
cas par cas en une porte rigoureuse et de concentrer l'originalité sur les
données explicites qui franchissent cette porte.

## 11. Formulation publiable proposée

La formulation forte mais défendable est :

> We give an explicit smooth projective toric morphism to a disc whose
> reduced central fibre has two components. We formulate an
> \(\mathcal O\)-acyclic anticanonical slicing criterion and verify all its
> hypotheses for the specified fan and linear subsystem. It follows that the
> resulting Calabi–Yau hypersurface family is a strict Tyurin degeneration.

La formulation à éviter est :

> We discovered that anticanonical toric degenerations are Tyurin
> degenerations.

Cette seconde phrase serait trop générale, déjà proche de constructions
standards, et fausse sans la porte de transversalité et les deux composantes
réduites.

## 12. Utilité pour la suite de R64

Pour scanner d'autres modèles, il suffit désormais de produire, pour chaque
candidat, un manifeste contenant :

1. rayons primitifs, cônes maximaux et déterminants ;
2. caractère primitif \(\ell\) et ordres sur tous les rayons ;
3. certificat de support propre et fonction de support projective ;
4. étoiles quotientées de \(p,m,\langle p,m\rangle\) ;
5. degré de la coupe et égalité avec \(-K_{/\Delta}\) ;
6. supports restreints et certificat de lissité/transversalité ;
7. seulement après cette porte, calcul du réseau de restriction et de la
   LMHS.

Cette procédure peut trouver une famille nouvelle avec un autre réseau de
couture et un autre sous-type de monodromie. Elle ne peut, à elle seule,
produire \(R(t)\) ou une tour physique.

## 13. Sources primaires

1. C. F. Doran, A. Harder, A. Y. Thompson,
   *Mirror symmetry, Tyurin degenerations and fibrations on Calabi–Yau
   manifolds*, Proc. Symp. Pure Math. 96 (2017), 93–131,
   <https://arxiv.org/abs/1601.08110>.
2. S. Hu, *Semi-Stable Degeneration of Toric Varieties and Their
   Hypersurfaces*, Comm. Anal. Geom. 14 (2006), 59–89,
   <https://arxiv.org/abs/math/0110091>.
3. D. Eisenbud, M. Mustaţă, M. Stillman,
   *Cohomology on Toric Varieties and Local Cohomology with Monomial
   Supports*, J. Symbolic Comput. 29 (2000), 583–600,
   <https://arxiv.org/abs/math/0001159>.
4. The Stacks Project, *Semistable reduction*, Tag 0CDB,
   <https://stacks.math.columbia.edu/tag/0CDB>.
5. J. H. M. Steenbrink, *Limits of Hodge structures*, Invent. Math. 31
   (1976), 229–257, <https://doi.org/10.1007/BF01403146>.
6. C. F. Doran, A. Thompson, *The Mirror Clemens–Schmid Sequence*,
   <https://arxiv.org/abs/2109.04849>.

## 14. Conclusion de la voie A

\[
\boxed{
\text{éventail relatif lisse à deux rayons primitifs}
+\text{ coupe anticanonique transverse}
\Longrightarrow
\text{Tyurin stricte}
}
\]

à condition de conserver explicitement propreté/projectivité et
\(\mathcal O\)-acyclicité des strates, cette dernière étant automatique dans
le cas torique complet.

Le résultat réellement récupéré au-delà de POLY944 n'est donc pas une valeur
universelle ni un nouveau mécanisme physique : c'est un **critère de
construction dimension-indépendant**, assez fort pour générer et certifier
d'autres exemples, mais dont la nouveauté doit rester attribuée aux exemples
intrinsèques obtenus plutôt qu'aux ingrédients standards de la preuve.

