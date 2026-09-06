# Couplage du radion à raideur finie : expression fermée et bornes

6 septembre 2026. Résultat du modèle classique déclaré, à l'ordre ε². La nouveauté bibliographique de cette spécialisation n'est pas établie par le calcul.

## Domaine et conventions

On conserve la famille symétrique à x=μL>0, ε=qL/√(12M5³), avec deux raideurs égales λ̂=λL≥0. Chaque fond est reconstruit avec ses propres constantes de bord ; un spectre est ensuite celui d'une action fixée. Le cas affine λ̂=0 est une famille de comparaison, pas la limite à v fini des potentiels λ(σ∓v)². Aucune cinétique de brane ou interaction directe matière–σ n'est ajoutée.

Avec C=cosh²(x/2), S=sinh(x), T=tanh(x/2), d=xT+2λ̂, le coefficient de masse déjà dérivé est

\[
\kappa=\frac{4d}{1+dS/(2x)},\qquad m_r^2 L^2=\kappa\epsilon^2+O(\epsilon^4).
\]

## Dérivation du coefficient de couplage

Dans les unités L=M5³=1, t=y−1/2, les profils de premier ordre donnent

\[
b(t)=\frac{8t\cosh^2(xt)}{C}-\frac{\kappa\sinh(2xt)}{2x},\qquad
v_1=\sqrt{12/C}\cosh(xt),\qquad s_1=-3b/v_1,
\]
\[
f_2(t)=\frac{4t^2+2t\sinh(2xt)/x}{C}-\frac{\kappa[\cosh(2xt)-1]}{4x^2}.
\]

La norme physique, et non le seul produit scalaire spectral, impose

\[
3\alpha_r-1=c_\alpha\epsilon^2+O(\epsilon^4),\qquad
c_\alpha=2[f_2(1/2)-\langle f_2\rangle]-\frac{\langle s_1^2\rangle}{6}.
\]

En posant H=cosh(x), les deux contributions séparées sont

\[
2[f_2(1/2)-\langle f_2\rangle]
=\frac{4/3+2S/x-2H/x^2+2S/x^3}{C}
-\frac{\kappa}{2x^2}(H-S/x),
\]
\[
\frac{\langle s_1^2\rangle}{6}
=\frac{1/3+S/x-2H/x^2+2S/x^3}{C}
-\frac{\kappa}{2x^2}(H-S/x)
+\frac{C\kappa^2}{16x^2}(S/x-1).
\]

Les termes linéaires en κ s'annulent exactement. Il reste

\[
\boxed{c_\alpha(x,\widehat\lambda)=\frac{1+S/x}{C}
-\frac{C\kappa(x,\widehat\lambda)^2}{16x^2}(S/x-1).}
\]

Les intégrales ici sont celles du profil de perturbation avant simplification ; elles ne sont pas un ajustement des masses ou des résidus numériques.

## Positivité et ordre en raideur

Pour x>0, S/x>1 et κ augmente strictement avec λ̂. Le coefficient cα diminue donc strictement avec λ̂. Ses limites sont

\[
c_0=\frac{1+T^2+2T/x}{C},\qquad
c_\infty=\frac{4[\cosh x-\sinh(x)/x]}{\sinh^2x}.
\]

La dérivée de x cosh x−sinh x vaut x sinh x>0 et cette fonction s'annule à x=0. Ainsi c∞>0 pour x>0 et

\[
0<c_\infty\le c_\alpha(x,\widehat\lambda)\le c_0.
\]

Le couplage dépasse donc 1/3 pour une rétroaction suffisamment faible à x et λ̂ fixés, pour toute raideur non négative de cette famille. Augmenter la raideur réduit la correction dominante du couplage, tandis que la masse augmente. Ce résultat ne fixe pas le signe du changement exact de couplage à rétroaction arbitraire. La limite raide est un problème limite distinct d'une valeur finie comme λ̂=20.

## Relation testable sans longueur absolue

L'élimination de ε donne, toujours à x et λ̂ fixés,

\[
3\alpha_r-1=\frac{c_\alpha}{\kappa}(m_rL)^2+O(\epsilon^4).
\]

En introduisant le premier mode tensoriel mT,1 L=π+O(ε²), on obtient aussi

\[
3\alpha_r-1=\frac{\pi^2c_\alpha}{\kappa}\left(\frac{m_r}{m_{T,1}}\right)^2+O(\epsilon^4).
\]

Cette relation n'exige pas de valeur de R. Elle conserve deux paramètres de forme x et λ̂ et ne prédit pas seule une longueur absolue. Sa validité asymptotique est une conséquence de l'expansion, pas un verdict expérimental.

## Vérifications

`weak_coupling_quadratic.py` intègre séparément f2 et s1² sur l'intervalle entier avec deux maillages de Simpson, pour 35 couples (x,λ̂). L'écart maximal entre quadrature et formule fermée est inférieur à 4,7×10⁻14 ; l'écart de raffinement est inférieur à 7×10⁻13 dans cette grille. Ces chiffres vérifient une intégrale numérique, pas la précision physique de l'EFT.

Un problème spectral Legendre–Galerkin indépendant, documenté dans `AUDIT_FOND_STABILITE_R.md`, contrôle la limite de faible ε sans utiliser κ ou cα pour calculer les valeurs propres. Les sorties restent conservées avec les résolutions. Au point x=2, les valeurs théoriques sont cα=0,839948683 pour λ̂=1 et cα=0,622678119 pour λ̂=20.

Le théorème d'ordre des masses à fond fixé découle aussi du principe min–max appliqué au dénominateur spectral avec ses poids de bord. L'ordre de cα prouvé ici est un résultat distinct, limité au coefficient de faible rétroaction.
