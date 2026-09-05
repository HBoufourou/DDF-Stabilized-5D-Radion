# R62 — Audit terminal de la dégénérescence de forme Tyurin

## Éventail relatif 5D, lissité SNC et obstruction de parité O3/O7

**Projet :** DDF I–VIII  
**Auteur du projet :** Hicham Boufourou  
**Date de l’audit :** 4 septembre 2026  
**Statut :** calcul exact reproductible ; résultat géométrique positif et stop-test orientifold négatif

---

## 1. Conclusion exécutive

R62 sépare définitivement deux questions qui avaient été mélangées dans les versions antérieures.

1. **La géométrie semi-stable de forme Tyurin est sauvée.** Il existe un éventail torique relatif explicite de dimension cinq, régulier, cohérent, projectif et propre au-dessus de \(\mathbb A^1\). L’hypersurface relative générique est lisse. Sa fibre centrale est réduite, à croisements normaux simples, et possède exactement deux composantes irréductibles lisses se coupant transversalement le long d’une K3 lisse.

2. **La tour fermée orientifold \(\mathcal N=1\) visée n’est pas sauvée dans le cadre testé.** Les 512 relèvements diagonaux de signes donnent 16 classes ambiantes, puis huit caractères effectifs sur la K3 de recollement. Aucune involution holomorphe non symplectique ne laisse, dans le réseau invariant actif requis, une direction isotrope paire pour le mécanisme du tube fermé. L’échange des deux composantes de Tyurin n’aide pas : il impose alors un cycle anti-invariant dans un réseau négatif défini \(E_8(-2)\).

Le résultat correct à publier est donc :

> **Une dégénérescence résolue, semi-stable et explicite de forme Tyurin, de type II, avec un mécanisme géométrique candidat de tour dans la théorie parentale \(\mathcal N=2\), accompagnée d’une obstruction démontrée à sa projection par le mécanisme du tube isotrope actif dans une théorie \(\mathcal N=1\) de type O3/O7.**

L’idée de \(R\) est conservée comme paramètre métrique/radion candidat, à relier ultérieurement au modèle algébrique et à stabiliser. Le paramètre effectivement construit ici est le paramètre de lissage \(t=z=pm\). **R62 ne démontre ni l’identification métrique \(R=R(t)\), ni une valeur micrométrique de \(R\).** Le plan de Fano reste différé : il ne doit pas intervenir dans l’article 1.

---

## 2. Portée logique du résultat

| Niveau | Statut après R62 | Formulation autorisée |
|---|---:|---|
| Éventail relatif 5D | démontré par calcul exact | régulier, cohérent, propre sur \(\mathbb A^1\) |
| Fibre centrale | démontré pour un membre générique | deux composantes irréductibles lisses, réduites, SNC |
| K3 de recollement | démontré génériquement | lisse |
| Lieu naïf horizontal | démontré génériquement avec R60 | 16 composantes ; conifold transversal hors de leur collision avec la fibre centrale |
| LMHS \(\sigma_5\) | la condition géométrique de R61 est levée | décomposition équivariante certifiée pour un membre générique |
| Tour parentale \(\mathcal N=2\) | conservée comme candidate | support du mécanisme de Hassfeld et al., sans calcul des invariants BPS |
| Tour fermée \(C_4\), O3/O7, \(\mathcal N=1\) | mécanisme testé exclu | obstruction de parité et de signature |
| Rayon \(R\) micrométrique | non dérivé | motivation phénoménologique seulement |
| Plan de Fano | non testé ici | à traiter dans un travail ultérieur |

Le mot « Tyurin » est employé dans ce rapport au sens **de forme Tyurin** : famille CY semi-stable à deux composantes réunies le long d’un diviseur K3 anticanonique commun. Pour revendiquer une dégénérescence de Tyurin stricte au sens quasi-Fano, il reste à vérifier explicitement \(H^i(Y_p,\mathcal O_{Y_p})=H^i(Y_m,\mathcal O_{Y_m})=0\) pour \(i>0\).

Le no-go de R62 n’est **pas** un théorème contre toute réalisation imaginable. Il vise précisément : une involution holomorphe O3/O7 fibrée sur \(t\), préservant \(L=U(2)\), un cycle fermé propre obtenu par le mécanisme du tube isotrope actif, un état propre de l’involution et le secteur vectoriel fermé provenant de \(C_4\). Les cycles brane–image non propres, les secteurs ouverts, une action non géométrique, une autre polarisation ou une autre compactification ne sont pas couverts.

---

## 3. Données toriques de départ

On travaille dans \(N\simeq\mathbb Z^4\), avec les rayons résolus, dans l’ordre \((x_0,\ldots,x_7,E)\),

\[
\begin{aligned}
\nu_0&=(1,0,0,0),              &\nu_1&=(-2,0,-1,0),\\
\nu_2&=(-2,0,0,-1),            &\nu_3&=(0,0,0,1),\\
\nu_4&=(0,0,1,0),              &\nu_5&=(-1,-1,0,0),\\
\nu_6&=(0,1,0,0),              &\nu_7&=(-1,0,0,0),\\
\nu_E&=(1,1,0,0).&&
\end{aligned}
\]

L’idéal de Stanley–Reisner du quatre-fold ambiant résolu est engendré par les sept paires

\[
x_0x_7,\quad x_1x_4,\quad x_2x_3,\quad x_5x_6,
\quad x_0x_6,\quad x_5E,\quad x_7E.
\]

La nouvelle construction relative vit dans

\[
N'=N\oplus\mathbb Z\simeq\mathbb Z^5.
\]

Les neuf rayons résolus deviennent \(\widetilde\nu_i=(\nu_i,0)\), et l’on ajoute

\[
\nu_p=\nu_{\zeta_+}=(0,-1,0,0,1),\qquad
\nu_m=\nu_{\zeta_-}=(0,0,0,0,1).
\]

La convention est reliée à celle de R61 par un cisaillement unimodulaire. La relation

\[
-\nu_5+\nu_7+\nu_p-\nu_m=0
\]

reproduit exactement la sixième ligne de charges utilisée en R61.

Dans l’ordre \((x_0,\ldots,x_7,E,p,m)\), une matrice complète de charges est

\[
Q=\begin{pmatrix}
2&1&0&0&1&0&0&0&0&0&0\\
2&0&1&1&0&0&0&0&0&0&0\\
1&0&0&0&0&1&1&0&0&0&0\\
1&0&0&0&0&0&0&1&0&0&0\\
-1&0&0&0&0&0&-1&0&1&0&0\\
0&0&0&0&0&-1&0&1&0&1&-1
\end{pmatrix}.
\]

Son rang est six, \(Q\,V^{\mathsf T}=0\), et sa forme normale de Smith a pour diagonale

\[
(1,1,1,1,1,1).
\]

Il n’y a donc pas de torsion cachée dans le quotient de Cox utilisé.

---

## 4. Éventail relatif explicite

Avec \(p=\zeta_+\) et \(m=\zeta_-\), les 28 cônes maximaux de dimension cinq sont les suivants.

### 4.1 Huit cônes du top inférieur avec \(p\)

\[
0125p,\ 0135p,\ 0245p,\ 0345p,\
1257p,\ 1357p,\ 2457p,\ 3457p.
\]

### 4.2 Douze cônes du top supérieur avec \(m\)

\[
\begin{gathered}
012Em,\ 013Em,\ 024Em,\ 034Em,\\
1267m,\ 126Em,\ 1367m,\ 136Em,\\
2467m,\ 246Em,\ 3467m,\ 346Em.
\end{gathered}
\]

### 4.3 Huit cônes de couture

\[
012pm,\ 013pm,\ 024pm,\ 034pm,\
127pm,\ 137pm,\ 247pm,\ 347pm.
\]

Chaque déterminant maximal vaut \(\pm1\). L’ambiant relatif est donc régulier.

### 4.4 Certificat de cohérence

Le vecteur entier de hauteurs

\[
h=(0,0,0,5,5,0,5,2,4,0,3)
\]

définit le polyèdre non borné

\[
P_h=\{y\in M'_{\mathbb R}:\langle y,\nu_j\rangle\le h_j\}.
\]

Le calcul rationnel exact donne :

- 28 sommets entiers ;
- cinq facettes actives à chaque sommet ;
- les 28 cônes normaux sont exactement les cônes listés ci-dessus ;
- tous les écarts stricts sont dans \(\{1,2,3,4,5\}\) ;
- 60 murs internes et 20 murs de bord.

L’éventail est donc polytopal et cohérent. En notant \(s\) la cinquième coordonnée duale, le cône de récession de \(P_h\), dans \(M'_{\mathbb R}\), est engendré par

\[
-e_5^*=(0,0,0,0,-1).
\]

Il faut distinguer ce vecteur dual du nouveau rayon du fan

\[
\nu_\infty=-e_5=(0,0,0,0,-1)\in N'.
\]

En posant

\[
\overline P=P_h\cap\{-s\le1\},
\]

on ajoute les 20 cônes \(\sigma\cup\{\nu_\infty\}\), où \(\sigma\) parcourt les 20 cônes maximaux du fan quatre-dimensionnel résolu. Le fan complété possède exactement 48 cônes maximaux, tous unimodulaires, et 120 murs appariés deux à deux. Il est complet, lisse et cohérent.

### 4.5 Propreté sur la droite affine

Soit \(\pi_N:N'\to\mathbb Z\) la projection sur la dernière coordonnée. Tous les rayons \(\widetilde\nu_i\) sont envoyés sur zéro, tandis que \(p\) et \(m\) sont envoyés sur \(+1\). L’éventail \(\Sigma_5\) n’est pas complet absolument, mais son support est

\[
|\Sigma_5|=\pi_N^{-1}(\mathbb R_{\ge0})
=N_{\mathbb R}\times\mathbb R_{\ge0},
\]

qui est l’image réciproque du cône de \(\mathbb A^1\). Le critère torique de propreté s’applique donc au morphisme

\[
\pi:X_{\Sigma_5}\longrightarrow\mathbb A^1.
\]

La complétion précédente définit un morphisme projectif vers \(\mathbb P^1\). Sa restriction au-dessus de \(\mathbb A^1\) prouve aussi la projectivité relative de \(\pi\).

### 4.6 Platitude et semi-stabilité locale

Dans chaque carte unimodulaire, la fonction de base prend l’une des formes

\[
z=u,\qquad z=v,\qquad z=uv.
\]

Dans les anneaux locaux au-dessus de zéro, \(z\) est un non-diviseur de zéro. Pour l’hypersurface générique, \(P\) n’est divisible ni par \(p\) ni par \(m\), de sorte qu’aucune composante de \(Y\) n’est contenue dans la fibre centrale ; \(z\) reste un non-diviseur de zéro dans \(\mathcal O_Y\). Comme \(Y\) est Cohen–Macaulay — et même lisse génériquement d’après la section suivante — et que la base est une courbe régulière, le morphisme devient plat après rétrécissement autour de zéro. C’est exactement la platitude locale requise. Avec la réduction et les croisements normaux simples démontrés ci-dessous, on obtient une dégénérescence semi-stable au voisinage de zéro.

### 4.7 Idéal de Stanley–Reisner relatif

Les non-faces minimales sont exactement

\[
\begin{gathered}
x_0x_6,\ x_0x_7,\ x_1x_4,\ x_2x_3,\ x_5x_6,\\
x_5E,\ x_5m,\ x_6p,\ x_7E,\ Ep.
\end{gathered}
\]

La coordonnée de base est

\[
z=pm.
\]

Ainsi

\[
\operatorname{div}(z)=D_p+D_m
\]

avec multiplicité un sur chaque composante. La fibre torique centrale est exactement \(D_p\cup D_m\), sans troisième composante issue de \(x_6E\). Les liens combinatoires de \(D_p\), \(D_m\) et de leur intersection possèdent respectivement 16, 20 et 8 cônes maximaux.

---

## 5. Hypersurface relative et test jacobien

La famille \(\sigma_5\) est représentée par

\[
\begin{aligned}
P={}&p\,x_0x_5^2x_7A^-_{22}
 +x_5^2x_6x_7^2A^0_{44}
 +c\,x_0^2E^2x_6\\
&+m\,x_0E^2x_6^2x_7A^+_{22}
 +m^2E^2x_6^3x_7^2A^{++}_{44}.
\end{aligned}
\]

Les indices indiquent les bidegrés sur la base \(\mathbb P^1\times\mathbb P^1\). Le support contient 69 monômes, répartis selon la hauteur \(q\) comme

\[
q=-1:9,\qquad q=0:26,\qquad q=1:9,\qquad q=2:25.
\]

Tous les monômes ont le même multidegré de Cox

\[
(4,4,3,2,-1,0).
\]

Ce degré est exactement la somme des onze colonnes de \(Q\). La famille est donc anticanonique dans l’ambiant relatif.

### 5.1 Lissité de l’espace total

Le seul lieu de base torique minimal du système total est

\[
\{x_6=x_7=0\}.
\]

Sur ce lieu, les relations de Stanley–Reisner imposent \(x_0\ne0\) et \(E\ne0\). Le monôme

\[
c\,x_0^2E^2x_6
\]

donne, pour \(c\ne0\), le jet transversal unité

\[
\frac{\partial P}{\partial x_6}=c\,x_0^2E^2\ne0.
\]

L’espace total est donc lisse sur le lieu de base ; hors de ce lieu, Bertini s’applique au système mobile. Un membre générique de la famille relative résolue est lisse.

### 5.2 Les deux composantes et la couture

Les supports restreints à \(p=0\), \(m=0\), puis \(p=m=0\), contiennent respectivement

\[
60,\qquad35,\qquad26
\]

monômes. Leurs lieux de base minimaux sont

\[
\varnothing,\qquad \{x_6=x_7=0\},\qquad\varnothing.
\]

Le même jet unité traite le lieu de base de la deuxième composante. La couture possède notamment l’équation de double couverture

\[
x_7^2A^0_{44}+c\,x_0^2=0,
\]

et sa branche générique est lisse.

### 5.3 Irréductibilité et propriété anticanonique de la couture

La lissité seule ne suffirait pas à prouver que chaque morceau est irréductible. Ici on peut fermer ce point directement.

Sur \(D_p\), les relations \(x_6p,Ep\in SR\) rendent \(x_6\) et \(E\) inversibles. Après division par \(x_6\), l’équation est quadratique en \(x_0\) :

\[
cE^2x_0^2+mE^2x_6x_7A^+_{22}x_0
+x_7^2\bigl(x_5^2A^0_{44}+m^2E^2x_6^2A^{++}_{44}\bigr).
\]

Son discriminant est génériquement non carré dans le corps des fonctions, grâce en particulier au coefficient indépendant de \(A^0_{44}\). Sur \(D_m\), \(x_5\) est inversible et l’équation est encore quadratique en \(x_0\), avec discriminant, à un carré inversible près,

\[
p^2x_5^2(A^-_{22})^2-4cE^2x_6^2A^0_{44},
\]

également génériquement non carré. Les hypersurfaces sur les tores denses sont donc irréductibles. Aucun facteur de bord supplémentaire ne subsiste : les seuls facteurs communs éventuels sont précisément des coordonnées inversibles sur le diviseur considéré. Ainsi \(Y_p\) et \(Y_m\) sont génériquement irréductibles.

Enfin \(Y_p+Y_m=\operatorname{div}(z)\) dans \(Y\), dont le fibré canonique est trivial par adjonction anticanonique. Une seconde application de l’adjonction donne

\[
K_{Y_p}+S=0,\qquad K_{Y_m}+S=0.
\]

La couture \(S\) est donc anticanonique dans les deux composantes. Les annulations cohomologiques quasi-Fano ne sont toutefois pas calculées ici, d’où l’expression prudente « de forme Tyurin ».

Par conséquent,

\[
Y_0=Y_p\cup_S Y_m
\]

est réduite, possède exactement deux composantes irréductibles lisses et celles-ci se rencontrent transversalement le long d’une K3 lisse \(S\). C’est une fibre centrale SNC.

---

## 6. Les seize branches horizontales et la correction importante de R62

L’intersection horizontale transverse

\[
A^-_{22}=A^0_{44}=0
\]

sur \(\mathbb P^1\times\mathbb P^1\) contient

\[
(2,2)\cdot(4,4)=2\cdot4+2\cdot4=16
\]

points distincts lorsque \(A^-_{22}\) et \(A^0_{44}\) sont généraux et transverses. Sur le modèle naïf, ces branches sont de type conifold transversal pour \(p\ne0\). Après la modification semi-stable et la petite résolution étudiée en R60, leurs préimages donnent seize surfaces réglées, fibrées en courbes exceptionnelles \(\mathbb P^1\) au-dessus de la base.

Mais l’ancien modèle relatif pré-semi-stable possède un détail qui ne devait pas être omis. Sur la carte \(m=1\), donc \(p=z\), considérons la strate

\[
S_0=\{x_0=x_6=0,\ x_5x_7\ne0\}.
\]

Après saturation par les unités, les deux jets normaux sont

\[
\partial_{x_0}P=pA^-_{22},\qquad
\partial_{x_6}P=A^0_{44}.
\]

L’idéal jacobien local pertinent se décompose donc, pour des coefficients génériques, comme

\[
\begin{aligned}
(x_0,x_6,pA^-_{22},A^0_{44})
={}&(x_0,x_6,A^-_{22},A^0_{44})\\
&\cap(x_0,x_6,p,A^0_{44}).
\end{aligned}
\]

Le premier idéal décrit les 16 composantes horizontales. Le second décrit une **courbe verticale supplémentaire** dans ce modèle naïf. Les deux se rencontrent dans la fibre \(p=0\), où le modèle local est plus dégénéré qu’un conifold ordinaire. Il est donc incorrect de parler de « seize sections conifold » jusque sur la fibre centrale.

Cette courbe ne contredit pas la lissité du modèle stable résolu. Elle est absente de ce dernier parce que

\[
x_6p\in SR,
\]

donc la strate naïve \(p=x_6=0\) n’existe plus. Une seconde relation,

\[
Ep\in SR,
\]

contrôle les exceptionnels horizontaux et implique

\[
E=0\Longrightarrow p\ne0.
\]

Sur \(z=pm=0\), le lieu exceptionnel résolu appartient alors au côté \(m=0\) et ne rencontre jamais la couture \(p=m=0\). Pour des intersections initiales transverses, les seize surfaces exceptionnelles sont deux à deux disjointes et leurs \(\mathbb P^1\) centraux sont disjoints de \(S\). L’indépendance de \(dA^-_{22}\) et \(dA^0_{44}\), combinée au fait que \((x_0,x_6)\) ne s’annule pas simultanément sur chaque \(\mathbb P^1\), exclut une singularité résiduelle générique le long de ces exceptionnels.

---

## 7. Scan exhaustif des caractères diagonaux sur la K3

Le scan commence avec les 35 monômes de la K3 de couture non contrainte, et non avec les seuls 26 monômes invariants de \(\sigma_5\). Les \(2^9=512\) choix de signes des coordonnées de Cox, quotientés par les cinq lignes de jauge, donnent

\[
512/2^5=16
\]

classes ambiantes \((A,B,C,D)\). Le caractère transverse \(B\) devient invisible après restriction à la tranche \(q=0\). On obtient donc huit caractères effectifs \((A,C,D)\) sur la couture. Chaque motif de couture possède deux relèvements ambiants, chacun avec 32 représentants de Cox, soit 64 relèvements au total. Les deux espaces propres du polynôme sont ensuite testés séparément ; le passage de \(P\) à \(-P\) n’est pas utilisé comme quotient d’automorphismes.

Dans la convention algorithmique, \(A\) est le signe de la coordonnée de double couverture \(Y\) après complétion du carré, et \(C,D\) sont les deux caractères indépendants de la base. Le signe de la forme holomorphe est

\[
\sigma^*\Omega_S=(-1)^{A+C+D}\Omega_S.
\]

Posons précisément

\[
A_\pm=L^\perp\cap H^2(S,\mathbb Z)^\pm,
\qquad L=U(2).
\]

La dernière colonne donne la signature de \(A_+\), le réseau invariant orthogonal à la polarisation. Il ne faut pas le confondre avec un quotient \(H^2/L\), ni avec le secteur anti-invariant requis lorsque les deux tops sont échangés.

| Caractère | Monômes propres | Action sur \(\Omega_S\) | Type géométrique | Signature de \(A_+\) |
|---:|---:|:---:|---|---:|
| 000 | 35 | \(+\) | identité | \((2,18)\) |
| 001 | 22 | \(-\) | non symplectique, deux courbes elliptiques | \((0,8)\) |
| 010 | 22 | \(-\) | non symplectique, deux courbes elliptiques | \((0,8)\) |
| 011 | 19 | \(+\) | involution symplectique de Nikulin | \((2,10)\) |
| 100 | 26 | \(-\) | involution de la double couverture | \((0,0)\) |
| 101 | 19 | \(+\) | involution symplectique de Nikulin | \((2,10)\) |
| 110 | 19 | \(+\) | involution symplectique de Nikulin | \((2,10)\) |
| 111 | 18 | \(-\) | involution d’Enriques | \((0,8)\) |

Les seuls caractères dont \(A_+\) est indéfini sont

\[
011,\quad101,\quad110,
\]

mais ils sont tous **symplectiques**. Dans ces familles, une involution de Nikulin impose en outre un saut de Picard et l’inclusion de \(E_8(-2)\) dans \(NS(S)\) ; elles ne sont donc pas des membres génériques de la seule famille \(U(2)\)-polarisée. Aucun caractère non symplectique ne donne une direction positive dans \(A_+\). En particulier, aucun ne donne un vecteur isotrope non nul dans ce réseau.

Pour chacun des sept caractères non triviaux, le scan teste aussi l’espace propre opposé du polynôme. Celui-ci omet l’unique terme \(x_0^2\) ; tous ses termes restants sont divisibles par \(x_7\). Il définit donc un diviseur réductible et ne fournit pas une seconde famille K3 lisse. Pour le caractère trivial 000, l’espace opposé est nul.

---

## 8. Stop-test de parité O3/O7

Près de la couture, le lissage local s’écrit

\[
uv=t,
\]

et la forme holomorphe limite prend la forme

\[
\Omega_3=\Omega_S\wedge d\!\log u.
\]

Pour une classe intégrale \(C\in H_2(S,\mathbb Z)\), pas nécessairement algébrique, la construction de Clemens fournit un cycle tube

\[
\operatorname{Tub}(C)\in H_3(Y_t,\mathbb Z),
\]

localement fibré en \(S^1\) au-dessus de \(C\). On ne suppose pas ici que cette fibration cercle est globalement le produit \(C\times S^1\).

Dans les calculs de réseau ci-dessous, la dualité de Poincaré identifie la classe homologique \(C\) à sa classe dans \(H^2(S,\mathbb Z)\).

Notons \(\eta=+1\) si l’involution préserve les deux branches et \(\eta=-1\) si elle échange \(u\) et \(v\). Dans le second cas, \(d\log v=-d\log u\).

Une projection O3/O7 holomorphe impose

\[
\sigma^*\Omega_3=-\Omega_3.
\]

Le secteur vectoriel fermé provenant de \(C_4\) est porté par \(H^3_+\). Le tube doit donc être pair. Si \(\epsilon_C\) désigne la parité de \(C\), alors \(\epsilon_{\rm tube}=\eta\epsilon_C\), et les deux contraintes sont

\[
\epsilon_{\Omega_S}\eta=-1,
\qquad
\epsilon_C\eta=+1.
\]

### 8.1 Branches préservées

Ici \(\eta=+1\). Il faut

\[
\Omega_S\ \text{anti-invariante},\qquad C\ \text{invariante}.
\]

L’involution sur \(S\) doit donc être holomorphe non symplectique, avec \(\sigma^*\Omega_S=-\Omega_S\). Son réseau invariant est hyperbolique de signature \((1,r-1)\). La polarisation de couture

\[
L=U(2)
\]

est invariante et contient déjà l’unique direction positive. Le réseau invariant actif \(A_+=L^\perp\cap H^2(S,\mathbb Z)^+\) est donc négatif défini. Tout vecteur actif non nul vérifie \(C^2<0\), et

\[
C^2=0\Longrightarrow C=0.
\]

Il n’existe pas de tube actif isotrope non nul dans le secteur pair requis.

### 8.2 Branches échangées

Ici \(\eta=-1\). Il faut

\[
\Omega_S\ \text{invariante},\qquad C\ \text{anti-invariante}.
\]

L’involution sur \(S\) doit donc être symplectique. Pour une involution de Nikulin non triviale,

\[
H^2(S,\mathbb Z)^-\simeq E_8(-2),
\]

qui est négatif défini. Plus précisément, le secteur actif requis est

\[
A_-=L^\perp\cap H^2(S,\mathbb Z)^-\subseteq E_8(-2),
\]

et il est donc lui-même négatif défini. Pour l’identité, l’espace anti-invariant est nul. Là encore, aucun \(C\ne0\) isotrope n’existe.

### 8.3 L’échange torique échoue aussi directement

Dans l’éventail résolu actuel, les rayons hors de la tranche centrale ont les multiplicités de la coordonnée de top \(q_{\rm top}\)

\[
q_{\rm top}=-1:1,\qquad q_{\rm top}=+1:2.
\]

Un automorphisme torique échangeant les deux tops ne peut donc pas bijecter les rayons. Ce constat combinatoire est plus spécifique que l’obstruction de réseau ci-dessus, laquelle subsiste même si l’on postule un échange non torique.

### 8.4 Verdict exact

> **Dans le cadre holomorphe O3/O7 standard testé — action fibrée sur \(t\), préservation de \(L\), cycle propre et état propre de l’involution — le mécanisme du tube isotrope actif ne produit aucun cycle fermé pair susceptible de porter la tour \(C_4\) recherchée.**

Ce verdict suffit pour arrêter la recherche de caractères diagonaux supplémentaires : le scan est exhaustif.

---

## 9. LMHS équivariante désormais certifiée

R61 avait donné une décomposition conditionnelle, sous réserve d’un modèle relatif lisse et SNC. Les sections 4 et 5 lèvent cette réserve pour un membre générique de \(\sigma_5\).

La décomposition des nombres de Hodge est

\[
h^{2,1}_+=34,\qquad h^{2,1}_-=51.
\]

Par conséquent,

\[
\dim H^3_+=68,\qquad \dim H^3_-=104.
\]

Pour la structure mixte limite,

\[
\dim\operatorname{Gr}^W_{2,+}
=\dim\operatorname{Gr}^W_{4,+}=0,
\]

\[
\dim\operatorname{Gr}^W_{2,-}
=\dim\operatorname{Gr}^W_{4,-}=20,
\]

et

\[
\dim\operatorname{Gr}^W_{3,+}=68,
\qquad
\dim\operatorname{Gr}^W_{3,-}=64.
\]

La somme totale vaut bien

\[
68+104=172=2h^{2,1}+2.
\]

Le résultat de type \(\mathrm{II}_{18}\) et son réseau actif de rang 20 restent donc des résultats de la géométrie parentale. Ce qui échoue n’est pas la dégénérescence, mais le choix simultané de la parité O3/O7, du secteur fermé \(C_4\) et du mécanisme du tube isotrope actif.

---

## 10. Conséquence physique : ce que l’on peut et ne peut pas dire

La littérature récente construit, pour une classe de limites de Tyurin de type II dans les compactifications IIB parentales \(\mathcal N=2\), des cycles spéciaux lagrangiens et argumente en faveur de tours de particules BPS issues de D3 enroulées. La signature \((2,18)\) de R62 place ce modèle dans la structure de réseau pertinente, mais R62 ne calcule ni les invariants BPS ni la stabilité multi-enroulée de ce modèle précis. Il établit donc le **support géométrique d’un mécanisme candidat**, pas l’existence complète de la tour quantique.

Après projection O3/O7, la situation change : les formes de degré trois se séparent en secteurs pair et impair et les vecteurs fermés de \(C_4\) appartiennent au secteur pair. Dans le cadre étudié par Enríquez Rojo et Plauschinn, les D3 sur trois-cycles ne préservent pas la même supersymétrie que les plans O3/O7 ; elles ne sont donc pas BPS et sont en général instables. Cette conclusion ne doit pas être extrapolée automatiquement à des cycles singuliers ou à des configurations brane–image différentes. Même la découverte future d’une classe isotrope différente nécessiterait une analyse indépendante de stabilité.

La formulation sûre est :

- \(t=pm\) est le paramètre algébrique de lissage effectivement construit et contrôlé ;
- \(R\) est un paramètre métrique/radion supplémentaire inspiré des scénarios anisotropes, dont la relation à \(t\) n’est pas dérivée ici ;
- la limite fournit le support géométrique du mécanisme candidat de tour parentale \(\mathcal N=2\) discuté par Hassfeld et al. ;
- R62 exclut la réalisation de sa version fermée \(C_4\) par un tube isotrope actif propre dans l’orientifold O3/O7 testé ;
- aucune équation de R62 ne fixe \(R\) en microns ;
- relier \(R\) à \(\mathcal O(1\!-!40)\,\mu\mathrm m\) exige encore stabilisation des modules, échelle de corde, volume, couplage, potentiel et contraintes phénoménologiques.

Les travaux sur la Dark Dimension, les volumes LVS anisotropes et les tests de la loi de Newton jouent trois rôles distincts : scénario théorique, mécanisme possible de stabilisation et borne expérimentale. Ils fournissent une **motivation et une cible**, jamais une prédiction de l’épaisseur du bulk de ce modèle précis. Dans le paramétrage de Braun et al., la grande direction \(R\) est en outre un intervalle distingué de la petite boucle utilisée dans la construction des trois-cycles ; cette identification métrique ne découle pas de la seule LMHS.

---

## 11. Décision pour la série DDF

### 11.1 À conserver

- le paramètre \(R\), conservé comme hypothèse métrique/radion à construire et stabiliser, distincte de \(t\) ;
- la dégénérescence CY semi-stable de forme Tyurin et ses deux composantes ;
- la petite résolution projective du modèle \((h^{1,1},h^{2,1})=(5,85)\) ;
- la couture K3 polarisée par \(L=U(2)\) ;
- la limite de type \(\mathrm{II}_{18}\), le réseau actif de rang 20 et le mécanisme candidat de tour parentale \(\mathcal N=2\) ;
- le calcul d’obstruction orientifold, qui devient un résultat propre à ce modèle au lieu d’être caché.

### 11.2 À retirer de l’article 1

- toute affirmation selon laquelle l’épaisseur du bulk est déjà calculée en microns ;
- toute affirmation d’une tour BPS fermée \(\mathcal N=1\) dans le quotient O3/O7 actuel ;
- l’assertion que le modèle relatif naïf n’a que seize sections singulières ;
- les scans de flux, la cosmologie quantitative et les prédictions numériques non dérivées ;
- le plan de Fano.

### 11.3 À différer

- une autre projection ou une autre polarisation de couture ;
- les branes-image et secteurs ouverts ;
- la stabilisation quantitative de \(R\) ;
- le plan de Fano comme structure combinatoire secondaire ;
- un modèle explicitement conçu pour une tour \(\mathcal N=1\), au lieu d’imposer celle-ci après coup au modèle actuel.

---

## 12. Article 1 recommandé maintenant

Il faut arrêter l’escalade R63–R100 sur ce modèle et rédiger l’article 1 autour du résultat solide obtenu.

**Titre de travail :**

> *A Resolved Toric Tyurin-Type Degeneration with Type-II\(_{18}\) Monodromy and an O3/O7 Parity Obstruction*

**Plan proposé :**

1. Modèle torique, polytope et petite résolution projective ;
2. construction explicite de l’éventail relatif 5D ;
3. certificat de cohérence, propreté et idéal SR ;
4. équation relative, analyse du lieu de base et preuve SNC ;
5. traitement honnête des seize branches conifold hors centre et de la courbe verticale naïve ;
6. couture K3, propriété anticanonique, statut quasi-Fano restant et LMHS de type \(\mathrm{II}_{18}\) ;
7. support du mécanisme candidat de tour dans la théorie parentale \(\mathcal N=2\) ;
8. scan exhaustif des involutions et obstruction O3/O7 ;
9. limites : pas de stabilisation, pas de rayon micrométrique dérivé, pas de résultat Fano.

Cette structure transforme une faiblesse de l’ancienne version — l’orientifold forcé — en une conclusion vérifiable et réfutable.

Compte tenu de la réponse d’arXiv, il ne faut pas soumettre de nouveau directement le manuscrit rejeté. La voie prudente est : soumission à une revue avec évaluation par les pairs, révision selon les rapports, puis appel arXiv seulement après acceptation et obtention d’un DOI, conformément au message reçu.

---

## 13. Reproductibilité

Le certificat autonome est fourni dans :

`r62_stable_fan_parity_stop_audit.py`

Exécution :

```bash
python3 r62_stable_fan_parity_stop_audit.py
```

Le script utilise uniquement de l’arithmétique entière/rationnelle pour :

- les déterminants des 28 cônes ;
- la forme normale de Smith ;
- les sommets du polyèdre de cohérence ;
- les 48 cônes unimodulaires et les 120 murs de la complétion ;
- les non-faces minimales ;
- les supports monomiaux et lieux de base ;
- les 512 relèvements de signes ;
- l’égalité entre les huit motifs de signes et les huit caractères \((A,C,D)\) ;
- l’identité monomiale de l’idéal jacobien local pré-semi-stable, après identification directe des deux jets dans l’équation locale.

Les identifications et signatures des réseaux d’involutions K3 sont des **entrées théoriques** issues de la classification de Nikulin et de sa littérature dérivée ; le script en vérifie la cohérence avec la combinatoire et le stop-test, mais ne redémontre pas la classification. De même, la transversalité générique des 16 intersections utilise Bézout/Bertini et la structure locale de R60. Pour la partie effectivement codée, les assertions sont bloquantes : une incohérence arrête l’exécution.

Le fichier `R62_AUDIT_OUTPUT.txt` contient la sortie de référence attendue.

---

## 14. Références principales utilisées pour le contrôle

1. A. P. Braun, M. Cicoli, R. Milioli, R. Valandro, *Moduli Stabilisation for ADD and the Dark Dimension Scenario*, [arXiv:2606.19440](https://arxiv.org/abs/2606.19440).
2. R. Davis et al., *Short Tops and Semistable Degenerations*, **Experimental Mathematics** 23 (2014) 351–362, [doi:10.1080/10586458.2014.910848](https://doi.org/10.1080/10586458.2014.910848).
3. B. van Geemen, A. Sarti, *Nikulin Involutions on K3 Surfaces*, [arXiv:math/0602015](https://arxiv.org/abs/math/0602015).
4. A. Garbagnati, A. Sarti, *On symplectic and non-symplectic automorphisms of K3 surfaces*, **Rev. Mat. Iberoam.** 29 (2013) 135–162, [doi:10.4171/RMI/716](https://doi.org/10.4171/RMI/716).
5. M. Artebani, A. Sarti, S. Taki, *K3 surfaces with non-symplectic automorphisms of prime order*, [arXiv:0903.3481](https://arxiv.org/abs/0903.3481).
6. T. W. Grimm, J. Louis, *The effective action of N=1 Calabi–Yau orientifolds*, [arXiv:hep-th/0403067](https://arxiv.org/abs/hep-th/0403067).
7. B. Hassfeld, J. Monnee, T. Weigand, M. Wiesner, *Emergent strings in Type IIB Calabi–Yau compactifications*, **JHEP** 01 (2026) 140, [doi:10.1007/JHEP01(2026)140](https://doi.org/10.1007/JHEP01(2026)140).
8. M. Enríquez Rojo, E. Plauschinn, *Swampland conjectures for type IIB orientifolds with closed-string U(1)s*, **JHEP** 07 (2020) 026, [doi:10.1007/JHEP07(2020)026](https://doi.org/10.1007/JHEP07(2020)026).
9. C. F. Doran, A. Harder, A. Y. Thompson, *Mirror symmetry, Tyurin degenerations and fibrations on Calabi–Yau manifolds*, [arXiv:1601.08110](https://arxiv.org/abs/1601.08110).
10. M. Montero, C. Vafa, I. Valenzuela, *The Dark Dimension and the Swampland*, **JHEP** 02 (2023) 022, [doi:10.1007/JHEP02(2023)022](https://doi.org/10.1007/JHEP02(2023)022).
11. M. Cicoli, C. P. Burgess, F. Quevedo, *Anisotropic Modulus Stabilisation: Strings at LHC Scales with Micron-sized Extra Dimensions*, **JHEP** 10 (2011) 119, [arXiv:1105.2107](https://arxiv.org/abs/1105.2107).
12. J. G. Lee et al., *New Test of the Gravitational \(1/r^2\) Law at Separations down to 52 μm*, **Phys. Rev. Lett.** 124 (2020) 101101, [arXiv:2002.11761](https://arxiv.org/abs/2002.11761).
13. D. Cox, J. Little, H. Schenck, *Toric Varieties*, Graduate Studies in Mathematics 124, AMS (2011).
14. The Stacks Project, *Bertini theorems*, Section 33.47, Tag 0FD4, [stacks.math.columbia.edu/tag/0FD4](https://stacks.math.columbia.edu/tag/0FD4).

---

## 15. Verdict R62

\[
\boxed{\text{Forme Tyurin semi-stable validée ; mécanisme du tube fermé O3/O7 obstrué dans le cadre testé.}}
\]

Décision : **geler la géométrie parentale et son mécanisme candidat \(\mathcal N=2\), rédiger l’article 1, différer Fano et ne revendiquer ni relation \(R(t)\) ni valeur micrométrique de \(R\).**

