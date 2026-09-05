# R64 — Errata et précisions obligatoires pour R62–R63

**Date :** 4 septembre 2026

R64 ne modifie pas la validation géométrique R63. Il corrige la portée du
stop-test orientifold et plusieurs formulations de nouveauté.

## 1. Carré nul contre carré non négatif

R62 formulait principalement l'obstruction pour un tube isotrope
\(C^2=0\). Le mécanisme de multi-enroulement discuté par Hassfeld et al.
utilise la condition plus large

\[
C^2\geq0.
\]

La seule absence d'isotropes ne suffisait donc pas. R64 remplace cet argument
par la négativité définie de tout le secteur propre requis. La conclusion
correcte est :

> aucun tube propre actif fermé \(C_4\) survivant dans le cadre déclaré ne
> provient d'une classe non nulle de carré nul ou positif.

## 2. Portée du scan des 512 signes

Le scan reste exhaustif pour les changements diagonaux de signe des neuf
coordonnées de Cox et pour le support polynomial déclaré. Il ne classifie pas
tous les automorphismes de la K3, du Calabi–Yau ou de la famille.

Le no-go R64 est distinct du scan : sa preuve intrinsèque, conditionnelle à
la tube map équivariante, vaut pour toute involution holomorphe globale
satisfaisant les hypothèses du rapport, diagonale ou non.

## 3. Branche échangée et identité sur la couture

R62 utilisait \(H^2(S,\mathbb Z)^-\simeq E_8(-2)\) dans la branche
symplectique. Cette identification suppose une involution symplectique non
triviale sur \(S\).

Une involution qui échange les deux composantes peut restreindre à l'identité
sur la couture. Dans ce cas, le secteur anti-invariant est nul et
\(E_8(-2)\) ne doit pas être invoqué. Le lemme du trois-plan positif de R64
couvre simultanément les actions triviale et non triviale.

## 4. Deux familles de projections Type IIB

R62 traitait O3/O7. R64 introduit la convention uniforme

\[
s=\epsilon_{\Omega_3},\qquad
s=-1\ \text{pour O3/O7},\quad s=+1\ \text{pour O5/O9}.
\]

Comme les vecteurs fermés de \(C_4\) appartiennent respectivement à
\(H^3_+\) et \(H^3_-\), leur parité interne est toujours \(-s\). Avec le
signe de branche \(\eta\), on obtient

\[
\epsilon_C=-s\eta=-\epsilon_{\Omega_S}.
\]

## 5. Niveau intégral

R64 prouve conditionnellement la négativité sur l'orthogonal actif rationnel,
sous l'hypothèse de naturalité équivariante de la tube map. Cela suffit pour
exclure une classe intégrale non nulle de carré non négatif : tout
représentant rationnel peut être multiplié par un entier sans changer le
signe de son carré.

La construction intégrale complète du quotient
\(H^2(S,\mathbb Z)/L\), de ses cosets discriminants et de son morphisme de
tube vers \(H_3(Y_t,\mathbb Z)\) reste ouverte.

R64 ne calcule toujours pas la forme de Smith de la monodromie de
Gauss–Manin intégrale complète. L'erratum R63 sur ce point reste en vigueur.

## 6. Nouveauté

Le polytope résolu est identifié à une forme normale déjà répertoriée dans
Kreuzer–Skarke. Il est interdit de le qualifier de nouveau.

Les constructions générales torique/Tyurin et le message large
d'obstruction des limites orientifold possèdent des antériorités directes.
La seule formulation potentiellement distincte de R64 est la proposition
uniforme à quatre cas et son application précise au paquet relatif R63. Sa
priorité reste à faire vérifier extérieurement.

## 7. Formulations qui restent interdites

- « toutes les tours sont exclues » ;
- « l'orientifold DDF complet est construit » ;
- « la tour parentale \(\mathcal N=2\) est démontrée » ;
- « \(R=R(t)\) est dérivé » ;
- « l'épaisseur du bulk est prédite en microns » ;
- « le plan de Fano organise sept charges physiques » ;
- « l'Article 1 peut être resoumis à arXiv ».

