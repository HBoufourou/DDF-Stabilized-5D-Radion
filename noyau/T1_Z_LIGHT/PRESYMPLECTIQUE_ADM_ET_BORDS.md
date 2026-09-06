# Rejeu de la forme présymplectique : deux routes et bord de l’intervalle

Calcul indépendant du 6 septembre 2026. Auteur du dossier scientifique : Hicham Boufourou. Cette note ne transforme pas une configuration hors domaine en état physique. Le test d’admissibilité par les jonctions complètes est distinct du calcul de la forme.

## 1. Convention et quantité calculée

On note B=M5³>0, a=e^A, I=∫₀ᴸa²dy et M̄²=BI. L’action est EH B/2, GHY B, un seul intervalle et potentiels de bord Uᵢ=τᵢ+λᵢ(σ−vᵢ)². Les normales sortantes sont η₀=−1 et ηᴸ=+1. La signature est −++++.

La perturbation scalaire, dans un représentant E=0, est

\[
\delta g_{\mu\nu}=2a^2F\eta_{\mu\nu}q,
\quad \delta g_{\mu y}=b\,\partial_\mu q,
\quad \delta g_{yy}=2Gq,
\quad \delta\sigma=sq,
\quad q=e^{-i\omega t+ikz},\quad \omega=k>0.
\]

Ce choix ne divise pas par p². On peut annuler E par une transformation longitudinale avant la restriction p²=0. L’usage de ce représentant pour le courant n’autorise pas à supprimer la jonction tensorielle anisotrope.

On définit Z par Ω(q*,q)=2iω Z, par unité de volume spatial dans cette normalisation de q. La norme quadratique employée par le dossier est N=Z/2. Une amplitude réelle u(x) d’action −Z(∂u)²/2 a donc Z>0. C’est cette convention qui permet de comparer le nombre historique −3M̄² avec le N_f du manuscrit.

## 2. Route ADM : momenta et angle au coin

Avec la normale temporelle future et K_ab=(dot h_ab−D_aN_b−D_bN_a)/(2N), poser H=F−A′b. Les extrinsèques linéarisées utiles sont

\[
\delta K_{ij}=aH\delta_{ij}\dot q,
\qquad\delta K_{yy}=a^{-1}(G-b')\dot q,
\qquad\delta K_{iy}=0.
\]

Les momenta canoniques sont π^{ab}=(B/2)√h(K^{ab}−h^{ab}K) et π_σ=√h n^A∂_Aσ. On obtient

\[
\delta\pi^{ij}=\frac B2(-2H-G+b')\delta^{ij}\dot q,
\quad\delta\pi^{yy}=-\frac{3B}{2}a^2H\dot q,
\quad\delta\pi_\sigma=a^2(s-\sigma'b)\dot q.
\]

Le coefficient canonique de volume, tiré de δπ∧δh+δπ_σ∧δσ, vaut

\[
z_{\mathrm{ADM}}=a^2[-6BFH-3BFG+3BFb'-3BGH+s^2-\sigma'bs]. \tag{1}
\]

Les surfaces t=constante et y=yᵢ ne restent pas orthogonales lorsque δg_ty≠0. Leur angle linéarisé, en convention de normale temporelle future, est βᵢ=−ηᵢbᵢ dot q/aᵢ. Le terme canonique au coin est −B∫√γ₃ δβ. Il donne

\[
Z_{\mathrm{ADM+coin}}=\int_0^L z_{\mathrm{ADM}}dy
-3B[a^2Fb]_0^L. \tag{2}
\]

La convention de normale temporelle passée employée dans l’appendice A de Harlow–Wu inverse simultanément β et son momentum et donne la même forme. Le terme d’angle suit la décomposition de Gauss–Codazzi du EH+GHY et ne constitue pas une nouvelle cinétique de brane ajoutée au modèle.

**Piège identifié pendant ce contrôle.** Insérer N_y=b dot q dans l’action avant de lire le coefficient de dot q² est une substitution qui dépend des dérivées. Le coefficient résultant

\[
\int a^2\{-3BH(H+G-b')+(s-\sigma'b)^2/2\}dy
\]

n’est pas la contraction canonique Ω(X*,X). Pour X₁ il est positif alors que la contraction de volume (1) est nulle. Le script le conserve comme diagnostic explicitement étiqueté, jamais comme norme physique.

## 3. Route covariante : courant de volume et correction GHY

La variation directe du lagrangien donne

\[
\theta^a=\frac B2(\nabla_b h^{ab}-\nabla^a h)-\nabla^a\sigma\,\delta\sigma,
\quad\Theta=\theta\mathbin{\lrcorner}\epsilon,
\quad\omega=\delta_1\Theta(\delta_2)-\delta_2\Theta(\delta_1).
\]

Pour vérifier le calcul indépendamment de l’ADM, le programme contracte les composantes de δ₁θ(δ₂), y compris δ√−g, les deux métriques inverses et δΓ. Il ne reprend pas (1) pour construire ce courant covariant. La contraction se réduit à

\[
z_{\mathrm{LW}}-z_{\mathrm{ADM}}
=-\frac B2[a^2b(2F+G)]'. \tag{3}
\]

Le GHY intervient via la variation au bord :

\[
(\Theta+\delta\ell)|_\Gamma
=\text{jonctions}\cdot\delta\text{champs}+dC,
\quad C=c\mathbin{\lrcorner}\epsilon_\Gamma,
\quad c^a=-\frac B2\gamma^{ab}n^c h_{bc}.
\]

Les jonctions naturelles d’Israel et du scalaire annulent le premier terme sur le vrai domaine. Les identités de variation de Harlow–Wu s’appliquent ; leurs conditions de Dirichlet utilisées comme exemple ne sont pas substituées aux jonctions DDF.

L’orientation de Σ est dx¹∧dx²∧dx³∧dy ; celle de ∂Σ donne C₀−Cᴸ. Le terme −∫∂ΣδC ajoute donc

\[
Z_C=-\frac B2[a^2b(4F-G)]_0^L. \tag{4}
\]

Cette expression provient de la variation explicite des quatre facteurs √−γ, γ^{00}, n^y et n^0 dans C. Dans le programme, ces quatre variations sont contractées séparément. L’addition de (3) et (4) redonne exactement (2), sans régler le signe sur le résultat historique.

Les potentiels λᵢ(σ−vᵢ)² n’ont pas de dérivée temporelle dans ce représentant à bords fixes et n’ajoutent pas de courant présymplectique autonome. Ils modifient la jonction scalaire et le domaine admissible via Uᵢ″=2λᵢ. Leur Hessienne ne suffit donc pas à changer le signe d’une configuration X₁ hors domaine.

## 4. X₁ : reproduction exacte du nombre et interprétation

Pour F=−1, G=s=0 et b=−2I(y)a⁻², I′=a², on a b′=−2−2A′b=2H. Les momenta π^{ij},π^{iy} sont nuls ; les π^{yy},π_σ éventuellement non nuls ne sont appariés à aucune perturbation de h_yy ou de σ. Ainsi z_ADM=0 point par point.

Les deux décompositions donnent :

| Route | Volume Z | Bord Z | Total Z | N=Z/2 |
|---|---:|---:|---:|---:|
| Covariante Θ−dC | −2BI | −4BI | −6BI | **−3BI** |
| ADM et angle | 0 | −6BI | −6BI | **−3BI** |

Le nombre historique est donc reproduit dans les conventions actuelles. **Il reste une évaluation de la forme prolongée sur une configuration hors domaine tant que X₁ ne satisfait pas la jonction anisotrope complète.** Une évaluation négative hors de l’espace tangent aux solutions admissibles n’est pas la preuve d’un ghost. L’action quadratique et les conditions de bord doivent être traitées ensemble.

## 5. Noyau de jauge et pairing, au-delà de la seule norme propre

Pour une transformation normale (F,G,s,b)=(A′ζ,ζ′,σ′ζ,ζ), H=0 et s−σ′b=0. La contribution ADM de volume est identiquement nulle. À bords fixes, ζ(yᵢ)=0 : le coin est nul aussi. La route covariante donne la même annulation après intégration de (3) et addition de (4).

On peut contrôler également l’appariement avec un perturbation générale Y satisfaisant la contrainte linéarisée C₁=3B(F′−A′G)+σ′s=0. La polarisation de (1), avec A″=−σ′²/(3B), donne

\[
Z_{\mathrm{ADM}}(Y,\mathcal L_\zeta g)
=-\frac{3B}{2}[a^2(F-A'b)\zeta]_0^L.
\]

Le coin ajoute −(3B/2)[a²(Fζ+A′bζ)] et le résultat complet devient

\[
Z(Y,\mathcal L_\zeta g)=-3B[a^2F\zeta]_0^L=0
\quad\text{si}\quad\zeta_0=\zeta_L=0. \tag{5}
\]

C’est une direction du noyau de la forme, et pas seulement une direction de norme propre nulle. Une preuve de quotient ne peut pas se limiter à Ω(X,X)=0, identité qui vaut pour toute forme antisymétrique réelle.

## 6. Complétion de jauge au bord : sens et portée

Les positions et coordonnées des deux bords peuvent être décrites par des applications de plongement. Au premier ordre, introduire leurs déplacements Xᵢ^A et δ_ξXᵢ^A=−ξ^A|ᵢ. Leur partie tangente se décompose en un déplacement temporel Xᵢ^T et un déplacement longitudinal spatial Xᵢ^L. Les deux sont définis avec |k|≠0, sans projecteur 1/p². Les transformations T et L sont ainsi traitées même sur p²=0. Pour une description avec bords mobiles, la composante normale Xᵢ^y doit aussi être conservée ; dans le représentant de branes fixes Xᵢ^y=0, la jauge normale admissible est précisément ζᵢ=0.

Les variations habillées sont

\[
\bar h_{AB}=h_{AB}+\mathcal L_Xg_{AB},
\qquad \bar s=s+X^y\sigma',
\]

où X est une extension dans un voisinage des bords. En particulier

\[
\delta\bar\gamma_{\mu\nu}
=h_{\mu\nu}|_i+2A'_i\gamma_{\mu\nu}X_i^y
 +(\mathcal L_{X_i^\parallel}\gamma)_{\mu\nu},
\quad \delta\bar\sigma_i=s_i+\sigma'_iX_i^y.
\]

La complétion linéaire de la forme est son tiré-en-arrière par ces champs habillés, avec le GHY et son coin inclus : Ω_ext=𝒟*Ω. Pour une direction de jauge combinée (h,s,X)=(ℒ_ξg,ξ^yσ′,−ξ), 𝒟 donne exactement zéro. Par conséquent Ω_ext(δ_ξ,δ)=0 pour tout δ, y compris les transformations T,L,ζ non nulles dans les coordonnées du bord. Le quotient retire ces directions conjointes, sans supprimer une véritable déformation des champs habillés.

Ce tiré-en-arrière résulte de la linéarisation de **la même action** exprimée sur les plongements, EH, scalaire, GHY et potentiels Uᵢ inclus ; ce n’est pas un choix arbitraire d’une nouvelle forme. Deux extensions de X ayant les mêmes valeurs aux bords diffèrent par une transformation de jauge de volume admissible ; après le quotient, elles décrivent le même état. La méthode générale des champs de plongement est présentée dans [Speranza, *Local phase space and edge modes for diffeomorphism-invariant theories*, sections 3 et 4](https://arxiv.org/html/1706.05061).

Il s’agit ici d’une complétion linéaire comme variables de plongement et d’un quotient de jauge. Cette note ne prétend pas avoir construit une nouvelle théorie non linéaire de degrés de liberté de bord, ni analysé une algèbre indépendante de charges de surface. Le test propagatif demandé n’exige aucun nouvel opérateur de bord.

## 7. Ancrages physiques positifs

Dans le représentant massif b=0,G=−2F, les deux routes donnent

\[
Z_f=\int a^2(6BF^2+s^2)dy=2N_f>0.
\]

Ce contrôle recolle exactement la convention du manuscrit. Il ne remplace pas l’examen séparé du domaine nul.

Pour les deux polarisations physiques du graviton de masse nulle, h_ij=a²t e_ij q, e_ii=0, k_i e_ij=0 et e_ij e_ij=2. Le mode de profil constant soumis aux jonctions tensorielles donne, dans les deux routes,

\[
Z_{TT}=\frac B4\int a^2t^2 e_{ij}e_{ij}dy
=\frac{BI}{2}t^2>0.
\]

Il n’y a pas de coin pour ces représentants avec h_ty=0. Le programme vérifie explicitement la polarisation + ; la rotation dans le plan transverse donne la polarisation ×. L’élimination du scalaire nul par les jonctions ne doit donc jamais être décrite comme la disparition de tout le secteur nul : le graviton usuel demeure.

## 8. Contrôles reproductibles et limites

`covariant_adm_current.py` utilise uniquement la bibliothèque standard Python. Cent jeux déterministes de composantes vérifient (3) et l’addition des coins, avec un résidu absolu maximal 2,31×10⁻¹⁴. Les entrées de ces contrôles de contraction ne sont pas annoncées comme cent fonds solutions. Huit exemples explicites couvrent X₁, des représentants de jauge, l’ancrage N_f et la polarisation TT. Le fichier JSON conserve séparément courant de volume, correction exacte, convention Z/N et statut hors domaine de X₁.

La contraction tensorielle et la variation de C sont indépendantes des expressions de momenta ADM. Le calcul n’utilise pas les fichiers historiques cités comme R1_04A_log.txt, qui n’ont pas été retrouvés dans les sources examinées.

La conclusion sur l’absence physique de X₁ requiert en plus le calcul des jonctions de la nouvelle action. Les secteurs statiques p^μ=0, les surfaces de paramètres où Dᵢ=0, les fluctuations autour de tranches courbes et une théorie complète de DDF ne sont pas clos par cette note.

Source primaire pour les identités de variation et la place des coins : [Harlow et Wu, *Covariant phase space with boundaries*, équations 106, 109–111 et appendice A](https://arxiv.org/html/1906.08616). Les réductions aux profils DDF et les contractions numériques présentées ici sont des calculs de ce rejeu.
