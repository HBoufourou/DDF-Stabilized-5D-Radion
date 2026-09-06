# Action entièrement fixée : longueur et courbure deviennent deux sorties

6 septembre 2026. Prolongement du calcul à tranches plates. Résultat classique pour la branche symétrique et pour des tensions proches de leur valeur compatible avec Minkowski. Les valeurs numériques utilisent des unités abstraites, sans rayon micrométrique ciblé.

## 1. La condition supplémentaire qui restait à traiter

L'étude précédente fixait μ, λ, v, Λ5 et M5³, calculait une longueur, puis donnait la constante de tension τ requise pour des tranches plates. C'est une condition de compatibilité légitime, mais pas une solution plate pour toute tension indépendante.

Nous fixons maintenant **également τ**, commune aux deux bords. Nous laissons les équations déterminer à la fois L et la courbure à quatre dimensions. Le passage à des tranches de de Sitter ou d'anti-de Sitter en cas de désaccord des tensions appartient déjà au cadre scalaire–gravité classique ; aucune priorité générale n'est revendiquée. Voir [DeWolfe, Freedman, Gubser et Karch, Phys. Rev. D 62, 046008](https://arxiv.org/abs/hep-th/9909134). Le calcul présent porte sur notre potentiel quadratique symétrique et nos conventions d'intervalle physique.

## 2. Équations et données d'entrée

Conserver V=Λ5+μ²σ²/2 et U0=τ+λ(σ+v)², UL=τ+λ(σ−v)². Poser

\[
ds^2=dy^2+e^{2A(y)}\bar g_{\mu\nu}dx^\mu dx^\nu,
\qquad \bar R_{\mu\nu}=3h\bar g_{\mu\nu}.
\]

h est une **courbure signée**, positive pour de Sitter, négative pour anti-de Sitter. Ce symbole n'est ni une accélération galactique ni nécessairement le carré d'un nombre réel dans le cas AdS. Les conventions sont M5³R5/2 et un seul intervalle avec GHY.

Les équations exactes sont

\[
A''=-\frac{\sigma'^2}{3M_5^3}-h e^{-2A},\qquad
\sigma''=\mu^2\sigma-4A'\sigma',
\]
\[
6M_5^3(A'^2-h e^{-2A})=\frac{\sigma'^2}{2}-\frac{\mu^2\sigma^2}{2}-\Lambda_5.
\]

Au centre de réflexion, A(0)=A′(0)=σ(0)=0. La contrainte impose

\[
\sigma'_c=\sqrt{2\Lambda_5-12M_5^3h}.
\]

Pour une valeur d'essai de h, intégrer jusqu'au bord scalaire défini par F=σ′+2λσ−2λv=0. Puis imposer la jonction gravitationnelle complète

\[
T(h)\equiv 3M_5^3A'_b-\lambda(\sigma_b-v)^2=\tau_{\rm entree}.
\]

La racine de T(h)−τ donne h ; l'événement donne L=2t_b. Le code garde μ, λ, v, Λ5, M5³ et τ constants pendant cette résolution. Les tensions ne sont pas réajustées à une longueur cible.

Les unités des coordonnées quatre-dimensionnelles doivent être fixées avant comparaison. La courbure vue sur les deux branes symétriques et le coefficient de gravitation sont

\[
h_b=h e^{-2A_b},\qquad
M_4^2=2M_5^3 e^{-2A_b}\int_0^{t_b} e^{2A(t)}dt.
\]

## 3. Réponse locale et existence d'une solution avec tension imposée

Autour d'une solution de Minkowski non dégénérée, une variation commune δτ ajoute 2δτ à l'énergie de vide quatre-dimensionnelle au premier ordre, en unités de brane. Les variations des profils ne contribuent pas au premier ordre à l'action stationnaire. L'équation d'Einstein effective donne donc

\[
\boxed{h_b=\frac{2\delta\tau}{3M_{4,0}^2}+O(\delta\tau^2).}
\]

M4,0 est calculé au fond plat. Cette relation de premier ordre conserve la rétroaction de ce fond : elle ne suppose pas un profil hyperbolique exactement plat. Comme dh_b/dh=e^(−2Ab)>0 à h=0, on obtient T′(0)>0. Le théorème des fonctions implicites garantit alors une solution **locale unique** h(τ), avec un bord régulier qui varie continûment. Il ne garantit pas l'unicité globale à forte courbure.

La longueur varie également. Le code intègre les équations de sensibilité au paramètre h. Si z=(A,A′,σ,σ′), z_h est sa dérivée à temps fixé et t_h la dérivée de l'instant de bord,

\[
t_h=-\frac{(\sigma')_h+2\lambda\sigma_h}{\sigma''+2\lambda\sigma'},
\qquad \frac{dz_b}{dh}=z_h+z't_h.
\]

En déduire L_h=2t_h et T_h par la règle de chaîne fournit dL/dτ. Cette méthode ne calcule pas une dérivée en conservant artificiellement q, x et ε constants.

En faible rétroaction seulement, le potentiel précédent prédit dL/dτ=4/[L Eσ″(L)]. La réponse exacte enregistrée dans le JSON reste utilisable lorsque cette approximation est insuffisante.

## 4. Contrôle intégré des sources

L'intégration de A″ et les jonctions donnent

\[
\boxed{U_0+U_L=-\int_0^L\sigma'^2dy
-3M_5^3 h\int_0^L e^{-2A}dy.}
\]

Le produit h e^(−2A) est invariant sous une renormalisation constante des coordonnées de brane. À h≥0, cette identité impose une somme strictement négative pour un stabilisateur non constant. À h<0, la deuxième contribution change de signe. Aucun transfert du théorème plat aux solutions AdS n'est effectué sans calcul.

## 5. Résultats effectivement obtenus

Trois familles abstraites utilisent μ=1, λ=0,5, M5³=1 et Λ5=v²/8, avec v=0,02 ; 0,3 ; 1,2. Pour chacune, quatre constantes de tension sont choisies **avant** la résolution : τ=τ0+δτ avec δτ/v²=−10⁻4 ; −10⁻5 ; +10⁻5 ; +10⁻4. τ0 désigne la tension du point plat de référence.

Exemple v=0,3 : τ0=−0,03596816493373043 et L0=1,375369917836534.

| δτ par bord | L calculé | h_b calculé | variation relative de L |
|---:|---:|---:|---:|
| −9×10⁻6 | 1,373076495059 | −4,351082378×10⁻6 | −0,16675 % |
| −9×10⁻7 | 1,375140337788 | −4,351079601×10⁻7 | −0,016692 % |
| +9×10⁻7 | 1,375599550845 | +4,351079602×10⁻7 | +0,016696 % |
| +9×10⁻6 | 1,377668636591 | +4,351082391×10⁻6 | +0,16713 % |

Le signe de h_b suit celui de δτ dans ces exemples. Les variations de tension ne sont pas des estimations de l'énergie noire observée.

Douze résolutions à 2 000 puis 4 000 pas par demi-longueur de référence ont été effectuées. Une inversion par bissection, indépendante des dérivées utilisées par Newton, retrouve une courbure à environ 2,4×10⁻10 près relativement. L'identité analytique dh_b/dτ=2/(3M4²) est vérifiée à moins de 8×10⁻15 relativement sur les trois points plats. Les très petits écarts de raffinement décrivent la cohérence numérique de cette exécution, pas une certification absolue de précision.

Le JSON conserve les profils, toutes les entrées, les dérivées, les historiques de Newton, les résidus de contrainte et l'identité intégrée. Aucun solveur joint dans la fusion n'a été exécuté pour obtenir ces résultats.

## 6. Ce que cette fermeture apporte, et son périmètre

L'action peut désormais être posée avec **toutes ses constantes de brane données** et produire un fond proche de Minkowski. La tension n'a plus à être silencieusement reconstruite pour imposer la platitude. Le calcul montre aussi que le système ne neutralise pas automatiquement une variation de l'énergie des branes : sa courbure y répond au premier ordre.

La stabilité scalaire/tensorielle des tranches courbes n'est pas calculée ici. La preuve spectrale positive du noyau reste celle des fonds plats dans son domaine déclaré. Il n'y a ni solution cosmologique dépendant du temps, ni prédiction de l'énergie noire, ni sélection absolue de R. Une détermination indépendante des couplages demeure nécessaire pour obtenir des micromètres à partir de cette action.

Reproduction : `courbure_action_fixe.py`, bibliothèque standard uniquement ; résultats `courbure_action_fixe.json`.
