# R63 — Quasi-Fano stricts et fibrés normaux des deux composantes de R62

**Objet.** Fermer le point laissé ouvert en R62 : calculer les groupes
\(H^i(\mathcal O)\) des deux composantes de la fibre centrale, prouver que la
couture est bien une K3 connexe, et identifier les fibrés normaux de la
couture. Les résultats ci-dessous concernent un membre générique lisse de la
sous-famille \(\sigma _5\) construite en R62.

## 1. Verdict

Notons \(X=X_{\Sigma _5}\) le cinq-fold torique relatif lisse de R62,
\(D_p=\{p=0\}\), \(D_m=\{m=0\}\), et

\[
\mathcal Y\in |-K_X|,
\qquad
Y_p=\mathcal Y\cap D_p,
\qquad
Y_m=\mathcal Y\cap D_m.
\]

Posons également

\[
T=D_p\cap D_m,
\qquad
S=\mathcal Y\cap T=Y_p\cap Y_m.
\]

Alors :

| Énoncé | Statut R63 |
|---|---:|
| \(D_p,D_m\) sont des quatre-folds toriques lisses projectifs | démontré |
| \(T\) est un trois-fold torique lisse projectif et connexe | démontré |
| \(S\in |-K_T|\), \(K_S\simeq\mathcal O_S\) | démontré |
| \(h^\bullet(S,\mathcal O_S)=(1,0,1)\) | démontré |
| \(S\) est une K3 lisse connexe | démontré |
| \(-K_{Y_p}\sim S\sim-K_{Y_m}\) | démontré |
| \(h^\bullet(Y_p,\mathcal O) = h^\bullet(Y_m,\mathcal O)=(1,0,0,0)\) | démontré |
| \(Y_p,Y_m\) sont quasi-Fano au sens de Doran–Harder–Thompson | démontré |
| \(N_{S/Y_p}\simeq N_{S/Y_m}\simeq\mathcal O_S\) | démontré |
| \(N_{S/Y_p}\otimes N_{S/Y_m}\simeq\mathcal O_S\) | démontré, et renforcé |
| « weak Fano » au sens \(-K\) nef et gros | faux : \(-K\) est semi-ample mais non gros |

Ainsi R62 peut être renforcé : il ne s'agit plus seulement d'une
« dégénérescence de forme Tyurin ». Sous les hypothèses de généricité et de
lissité déjà certifiées en R62, c'est une **dégénérescence de Tyurin au sens
strict utilisé par Doran–Harder–Thompson**.

## 2. Convention indispensable : trois niveaux distincts

Il ne faut pas confondre :

- \(D_p,D_m\), composantes **toriques ambiantes** de dimension quatre ;
- \(Y_p,Y_m\), composantes **hypersurfaces** de dimension trois ;
- \(T=D_p\cap D_m\), ambiant torique de la couture, et
  \(S=Y_p\cap Y_m\), la surface K3.

Cette distinction rend les deux suites exactes employées plus bas entièrement
transparentes.

## 3. Géométrie torique exacte de la couture ambiante

Les étoiles des cônes \(p\), \(m\) et \(\langle p,m\rangle\) contiennent
respectivement

\[
16,\qquad 20,\qquad 8
\]

cônes maximaux. Après quotient par \(\langle p,m\rangle\), les six rayons de
\(T\), dans les coordonnées \((a,c,d)\), sont

\[
\begin{array}{c|rrrrrr}
 &x_0&x_1&x_2&x_3&x_4&x_7\\ \hline
\nu &(1,0,0)&(-2,-1,0)&(-2,0,-1)&(0,0,1)&(0,1,0)&(-1,0,0).
\end{array}
\]

Les huit cônes maximaux choisissent un rayon dans chacune des trois paires

\[
(x_0,x_7),\qquad(x_1,x_4),\qquad(x_2,x_3).
\]

Leurs déterminants valent \(\pm1\), et chacune des douze faces de codimension
un appartient à exactement deux cônes. C'est donc un fan lisse complet.
Les étoiles de \(p\) et de \(m\) ont de même tous leurs murs appariés et leurs
cônes quotients sont unimodulaires. Elles définissent donc des quatre-folds
toriques lisses complets. Comme \(X\to\mathbb A^1\) est projectif et que
\(D_p,D_m\) sont fermés dans sa fibre centrale, ils sont projectifs.
Géométriquement, \(T\) est un fibré torique en \(\mathbb P^1\) sur
\(\mathbb P^1\times\mathbb P^1\), avec deux sections dont les classes diffèrent
de \((2,2)\). À la convention de projectivisation près, on peut l'écrire

\[
T\simeq
\mathbb P_{\mathbb P^1\times\mathbb P^1}
\bigl(\mathcal O\oplus\mathcal O(2,2)\bigr).
\]

Prenons comme base de \(\operatorname{Pic}(T)\)

\[
H_1=[D_1]=[D_4],\qquad
H_2=[D_2]=[D_3],\qquad
F=[D_7].
\]

Les relations de caractères donnent

\[
[D_0]=F+2H_1+2H_2.
\]

La somme des six diviseurs toriques vaut alors

\[
-K_T=2F+4H_1+4H_2=2[D_0].
\]

L'équation de couture de R62,

\[
x_7^2A^0_{4,4}+c\,x_0^2=0,
\]

a précisément cette classe \((4,4,2)\). Donc

\[
\boxed{S\in|-K_T|.}
\]

Ce calcul de classe ne dépend pas du fait que la sous-famille \(\sigma _5\)
n'utilise que 26 des 35 monômes anticanoniques de la couture. R62 a déjà
vérifié qu'un membre générique de ce sous-système est néanmoins lisse.

## 4. Connexité de la couture et calcul de \(h^1(\mathcal O_S)\)

Le trois-fold \(T\) est torique, lisse et projectif. Le résultat standard de
cohomologie torique donne

\[
H^i(T,\mathcal O_T)=0\quad(i>0),
\qquad H^0(T,\mathcal O_T)=\mathbb C.
\]

Comme \(S\in|-K_T|\), sa suite de diviseur est

\[
0\longrightarrow\mathcal O_T(K_T)
\longrightarrow\mathcal O_T
\longrightarrow\mathcal O_S
\longrightarrow0.
\]

Par dualité de Serre sur \(T\),

\[
H^i(T,\mathcal O_T(K_T))
\simeq H^{3-i}(T,\mathcal O_T)^*.
\]

Par conséquent,

\[
H^0(\mathcal O_S)=\mathbb C,
\qquad
H^1(\mathcal O_S)=0,
\qquad
H^2(\mathcal O_S)=\mathbb C.
\]

La première égalité prouve la connexité de \(S\), au lieu de la supposer.
L'adjonction donne

\[
K_S=(K_T+S)|_S\simeq\mathcal O_S.
\]

Une surface lisse projective connexe avec \(K_S\simeq\mathcal O_S\) et
\(h^1(\mathcal O_S)=0\) est une K3. La qualification « K3 de couture » est
donc maintenant démontrée à partir des suites exactes, indépendamment de la
seule présentation comme double couverture.

## 5. Classe anticanonique des deux composantes tridimensionnelles

La coordonnée de base est \(z=pm\), donc

\[
D_p+D_m=\operatorname{div}(z)\sim0.
\]

Puisque \(\mathcal Y\in|-K_X|\), l'adjonction donne

\[
K_{\mathcal Y}\simeq\mathcal O_{\mathcal Y}.
\]

Dans \(\mathcal Y\), les deux composantes de la fibre centrale vérifient

\[
Y_p+Y_m\sim0.
\]

En restreignant à chaque composante,

\[
K_{Y_p}\sim Y_p|_{Y_p}\sim-Y_m|_{Y_p}=-S,
\]

et de même

\[
K_{Y_m}\sim-S.
\]

Ainsi

\[
\boxed{-K_{Y_p}\sim S\sim-K_{Y_m}.}
\]

La même égalité s'obtient dans les quatre-folds toriques. Si
\(V_p=D_p\) et \(V_m=D_m\), alors

\[
K_{V_j}+Y_j\sim-T,
\qquad j=p,m.
\]

Cette seconde écriture est celle qui ferme le calcul cohomologique.

## 6. Calcul de \(H^i(Y_p,\mathcal O)\) et \(H^i(Y_m,\mathcal O)\)

Fixons \(j=p\) ou \(m\) et écrivons \(V=V_j\), \(Y=Y_j\). Les variétés
\(V\) et \(T\) sont toriques lisses projectives et connexes. La suite

\[
0\longrightarrow\mathcal O_V(-T)
\longrightarrow\mathcal O_V
\longrightarrow\mathcal O_T
\longrightarrow0
\]

et l'isomorphisme de restriction des constantes
\(H^0(\mathcal O_V)\to H^0(\mathcal O_T)\) impliquent

\[
H^q(V,\mathcal O_V(-T))=0
\quad\text{pour tout }q.
\]

Or

\[
K_V+Y\sim-T.
\]

La dualité de Serre en dimension quatre donne donc

\[
H^k(V,\mathcal O_V(-Y))
\simeq
H^{4-k}(V,\mathcal O_V(K_V+Y))^*
=H^{4-k}(V,\mathcal O_V(-T))^*=0.
\]

Enfin, la suite de l'hypersurface

\[
0\longrightarrow\mathcal O_V(-Y)
\longrightarrow\mathcal O_V
\longrightarrow\mathcal O_Y
\longrightarrow0
\]

donne

\[
H^i(Y,\mathcal O_Y)\simeq H^i(V,\mathcal O_V).
\]

Comme \(V\) est torique lisse projectif,

\[
\boxed{
h^\bullet(Y_p,\mathcal O_{Y_p})
=h^\bullet(Y_m,\mathcal O_{Y_m})
=(1,0,0,0).
}
\]

Il ne s'agit pas d'un comptage numérique conjectural : la conclusion découle
de deux suites exactes, de la dualité de Serre et de l'annulation torique de
\(H^{>0}(\mathcal O)\).

## 7. Les fibrés normaux, pas seulement leur produit

R61 avait seulement requis

\[
N_{S/Y_p}\otimes N_{S/Y_m}\simeq\mathcal O_S.
\]

Les données SR de R62 donnent davantage. Sur \(V_p\), le caractère
\(q+s\) définit un morphisme torique

\[
f_p:V_p\longrightarrow\mathbb P^1
\]

dont les rayons non nuls sont

\[
x_5\mapsto-1,qquad m\mapsto+1.
\]

Le diviseur \(T=\{m=0\}\) est donc une fibre, linéairement équivalente à
\(D_5\). La relation SR \(x_5m\in SR\) montre que les deux fibres sont
disjointes. Par suite

\[
N_{T/V_p}=\mathcal O_T(T)\simeq\mathcal O_T.
\]

Sur \(V_m\), le caractère \(q\) définit

\[
f_m:V_m\longrightarrow\mathbb P^1,
\]

avec

\[
p\mapsto-1,qquad x_6,E\mapsto+1.
\]

Ici \(T=\{p=0\}\) est la fibre opposée à la fibre réductible
\(D_6\cup D_E\). Les relations SR

\[
x_6p\in SR,
\qquad
Ep\in SR
\]

les rendent disjointes. Donc

\[
N_{T/V_m}=\mathcal O_T(T)\simeq\mathcal O_T.
\]

La transversalité de \(S=Y_j\cap T\) permet de restreindre ces fibrés :

\[
\boxed{
N_{S/Y_p}=\mathcal O_S(D_m)\simeq\mathcal O_S,
\qquad
N_{S/Y_m}=\mathcal O_S(D_p)\simeq\mathcal O_S.
}
\]

Ainsi la condition de d-semistabilité est satisfaite terme par terme :

\[
N_{S/Y_p}\otimes N_{S/Y_m}
\simeq\mathcal O_S.
\]

Localement, c'est cohérent avec le modèle lisse \(uv=t\) de R62 ; le présent
calcul identifie en plus les classes globales des deux normales.

## 8. Quasi-Fano oui, weak Fano non

Doran, Harder et Thompson appellent quasi-Fano une variété lisse dont le
système anticanonique contient un membre Calabi–Yau lisse et telle que
\(H^i(\mathcal O)=0\) pour tout \(i>0\). C'est exactement ce qui vient d'être
prouvé pour \(Y_p\) et \(Y_m\), avec le membre anticanonique \(S\).

Il existe une autre convention dans laquelle « quasi-Fano » est employé comme
synonyme, ou presque, de *weak Fano*, ce qui exigerait \(-K\) nef et gros. Il
faut l'éviter ici. Dans les deux composantes,

\[
\mathcal O_{Y_j}(-K_{Y_j})\simeq
\mathcal O_{Y_j}(S)\simeq(f_j|_{Y_j})^*\mathcal O_{\mathbb P^1}(1).
\]

La classe est semi-ample et nef, mais

\[
(-K_{Y_j})^3=S^3=0.
\]

Elle n'est donc pas grosse. Les deux bâtiments sont des quasi-Fano au sens
Tyurin/DHT, et non des weak Fano.

## 9. Ce qui est fermé et ce qui reste à faire

### Fermé en R63

- les annulations \(H^i(Y_p,\mathcal O)=H^i(Y_m,\mathcal O)=0\) pour
  \(i>0\) ;
- la connexité de \(S\) et \(h^1(S,\mathcal O_S)=0\) ;
- le caractère anticanonique de \(S\) dans chaque composante ;
- l'identification individuelle des deux fibrés normaux ;
- le passage de « forme Tyurin » à « Tyurin stricte » dans la convention DHT.

### Ne découle pas de R63

- une valeur physique de \(R\) ;
- un spectre KK ;
- la stabilité de la tour D3/BPS ;
- un orientifold échappant au no-go de R62 ;
- une classification de toutes les déformations ou de tous les modèles
  birationnels des deux quasi-Fano.

R63 renforce donc l'article géométrique, mais ne doit pas être présenté comme
une preuve phénoménologique de DDF.

## 10. Reproductibilité et statut des entrées

Le certificat exécutable est :

`meta_audit_r63/r63_quasifano_certificate.py`

Il vérifie exactement :

- les étoiles des deux composantes et de leur intersection ;
- l'unimodularité et la complétude combinatoire du fan de \(T\) ;
- la matrice de classes de diviseurs de \(T\) ;
- \([S]=-K_T=(4,4,2)\) ;
- les deux morphismes toriques vers \(\mathbb P^1\) ;
- les non-faces SR qui rendent les fibres opposées disjointes.

Les passages aux cohomologies utilisent trois théorèmes standards clairement
séparés du calcul : annulation de \(H^{>0}(\mathcal O)\) pour une variété
torique complète, dualité de Serre et suites exactes de diviseurs de Cartier.

Exécution :

```bash
python3 meta_audit_r63/r63_quasifano_certificate.py
```

Référence pour la définition employée : C. F. Doran, A. Harder,
A. Y. Thompson, *Mirror symmetry, Tyurin degenerations and fibrations on
Calabi–Yau manifolds*, §2.1, arXiv:1601.08110.

## 11. Verdict final R63-A

\[
\boxed{
Y_p\cup_S Y_m
\text{ est une dégénérescence de Tyurin stricte,}
\quad
N_{S/Y_p}=N_{S/Y_m}=\mathcal O_S.
}
\]

La réserve « quasi-Fano non calculé » de R62 est levée.

