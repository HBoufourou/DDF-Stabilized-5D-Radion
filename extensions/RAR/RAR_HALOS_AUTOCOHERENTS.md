# Halos calculés par équilibre hydrostatique : extension RAR conditionnelle

Date : 6 septembre 2026. Cette note prolonge le problème radial à densité sombre prescrite. Elle calcule maintenant la densité, sa masse gravitationnelle et son bord à partir d'une équation d'état commune. Le modèle non relativiste ci-dessous est **posé comme extension** ; il n'est pas dérivé de l'action canonique 5D de DDF. Ni la formation d'un condensat, ni sa température, ni une valeur prédite de la cinquième dimension n'en découlent.

Le résultat concret comprend 27 halos adiabatiques, trois intérieurs avec gradients de χ, les profils et des contrôles numériques reproductibles. Il montre aussi une obstruction utile : inclure réellement la masse du condensat ne produit pas automatiquement une relation d'accélération dépendant seulement des baryons.

## 1. Fonctionnelle statique et source cohérente

En unités ℏ=c=1, M₄²=(8πG)⁻¹. U est le potentiel gravitationnel, g=|∇U|, ρ est la densité matérielle de masse au premier ordre en dérivées (LO), et ρb est la source baryonique prescrite. On étudie la fonctionnelle stationnaire

\[
\mathcal I=\int d^3x\left[
 M_4^2\frac{|\nabla U|^2}{1+\chi^2}
 +\frac{M_4^2\chi^2}{9a_0^2}|\nabla U|^4
 +\frac{Z^2}{2}|\nabla\chi|^2
 +K\rho^2+U(\rho_b+\rho)-\nu\rho\right]. \tag{1}
\]

Ce n'est pas une preuve de positivité de l'énergie du système gravitant. Dans cette fermeture, ν est un multiplicateur fixant l'intégrale de ρ pour une solution sélectionnée ; donner ρ(0) est une autre manière de paramétrer la famille d'équilibres. K>0 et Z²>0 sont des paramètres communs. La gravité à deux champs suit l'extension de Khoury ; notre calcul conserve explicitement la source sombre variable. [Khoury, *Another Path for the Emergence of Modified Galactic Dynamics from Dark Matter Superfluidity*, 2016, §§3 et 5](https://arxiv.org/abs/1602.05961).

La variation indépendante de ρ, U et χ donne, dans le fluide :

\[
 2K\rho+U=\nu,\qquad P=K\rho^2,\qquad 2K\rho'=-g, \tag{2}
\]
\[
 \nabla\!\cdot\![\mu(h,\chi)\nabla U]=4\pi G(\rho_b+\rho),\quad
 \mu(h,\chi)=\frac1{1+\chi^2}+\frac{2\chi^2h^2}{9},\quad h=g/a_0, \tag{3}
\]
\[
 Z^2\Delta\chi=2M_4^2a_0^2h^2\chi
 \left[-\frac1{(1+\chi^2)^2}+\frac{h^2}{9}\right]. \tag{4}
\]

La contrainte ρ≥0 donne ρ=max[(ν−U)/(2K),0] dans l'approximation de Thomas–Fermi. La densité du condensat apparaît donc dans la même équation gravitationnelle que les baryons. La remplacer après coup par un profil choisi, ou l'omettre dans (3) tout en la conservant dans (2), serait une fermeture différente.

Une action de phase locale compatible avec le terme matériel est P(X)=X²/(4Km²), pour X>0, avec X=∂tϑ−mU−|∇ϑ|²/(2m). Elle donne ρ=mP_X et P=Kρ² **au niveau LO**. La convention correspondante pour le scalaire complexe est φ=ψ e⁻ⁱᵐᵗ/√(2m), ψ=√n e⁻ⁱϑ. Pour V₄=(g₄/2)|φ|⁴, on obtient K=g₄/(8m⁴). Cette égalité fixe les conventions de l'estimation numérique ; elle n'identifie pas les nouveaux opérateurs gravitationnels de (1) à ceux du noyau DDF.

Si l'on exige en plus le raccord précis à l'opérateur de phase de Khoury L_NLO=−C|∇X|², C=M₄²g²χ²/(9m²a₀²), la densité de charge conservée améliorée est n_cons=P_X+2∇·(C∇X). Au repos, ∇X=−m∇U, donc

\[
 m n_{\rm cons}=\rho-\frac{2M_4^2}{9a_0^2}\nabla\!\cdot(\chi^2g^2\nabla U). \tag{4a}
\]

Les variations statiques (2)–(4) restent cohérentes, mais ρ n'est pas la charge exacte locale du modèle à dérivées supérieures. Sur une sphère s=S, l'intégrale de (4a), exprimée en unités M*, est v(S)−S²χ²(S)h³(S)/9. Elle coïncide avec v(S) pour les conditions χ(S)=0 de la section 6. Pour les intérieurs adiabatiques, la charge intégrée complète exige l'extérieur et ses flux ; elle n'est pas déterminée ici. Les « masses sombres » des tableaux désignent donc précisément l'intégrale de la source matérielle LO ρ dans (3), et non une identité universelle avec la charge 5D.

Les conditions locales K>0, P_XX>0 et Z²>0 ne prouvent pas la stabilité globale du halo. À χ fixé, le coefficient radial gravitationnel vaut 1/(1+χ²)+2χ²h²/3>0. Le spectre couplé fluide–χ–gravité, les fluctuations temporelles et la complétion covariante restent à examiner.

## 2. Échelles communes et problème à frontière libre

On définit

\[
 r_K=\sqrt{\frac{K}{2\pi G}},\quad
 \rho_* = \frac{a_0}{4\pi G r_K},\quad
 M_* = \frac{a_0r_K^2}{G}=4\pi\rho_*r_K^3,
\]
\[
 s=r/r_K,\quad u=\rho/\rho_*,\quad v=M_{\rm sf}(<r)/M_*,\quad
 A=M_b/M_*,\quad B=r_b/r_K.
\]

Les baryons suivent un modèle sphérique de Plummer, utilisé ici comme banc mathématique :

\[
 m_b(s)=A\frac{s^3}{(s^2+B^2)^{3/2}},\qquad
 \rho_b/\rho_* =\frac{3AB^2}{(s^2+B^2)^{5/2}}.
\]

Le système hydrostatique devient simplement

\[
 u'=-h,\qquad v'=s^2u,\qquad
 b(s)=\frac{v+m_b(s)}{s^2}=\mu(h,\chi)h. \tag{5}
\]

Conditions centrales : u(0)=uc>0, v(0)=0. La surface S est le **premier zéro** de u. Aucun rayon de halo n'est imposé. La masse finale v(S) est une sortie. La charge/masse totale ou uc demeure une donnée d'état ; ni la régularité ni K ne sélectionnent seuls sa valeur. La normalisation additive de U est absorbée dans ν, utile notamment lorsque le potentiel MOND isolé n'a pas une limite finie à l'infini.

Le bord u(S)=0 est un bord du modèle de fluide sans pression quantique. Il ne représente pas une température critique calculée. Une phase normale extérieure, des gradients de l'amplitude et un environnement peuvent remplacer ce bord par un raccord ou une queue.

## 3. Fermeture adiabatique : résultat et limites au centre

Négliger les gradients de χ et minimiser à g fixé donne χ=0 pour h≥3, et χ²=3/h−1 pour 0<h<3. La loi algébrique exacte associée à (1) est

\[
 b=\mathcal B(h)=
 \begin{cases}h^2-2h^3/9,&0\leq h<3,\\h,&h\geq3.\end{cases} \tag{6}
\]

Ce n'est pas l'interpolation CDD h=√(b²+b). Les comparaisons ci-dessous utilisent (6) à la fois pour la solution complète et pour sa référence baryonique, afin de mesurer le rôle de la masse sombre. Le JSON fournit également la référence CDD, séparément.

L'équation de Lane–Emden modifiée résultante est

\[
 \frac1{s^2}\frac{d}{ds}[s^2\mathcal B(-u')]
 =u+\frac{3AB^2}{(s^2+B^2)^{5/2}},\qquad u'\leq0. \tag{7}
\]

En régime MOND profond, remplacer ℬ(h) par h². Sans baryons et avec uc=1, on retrouve le problème n=2 de l'équation (52) de Khoury. **n=2 désigne ici l'exposant de P(X), tandis que P∝ρ² correspond à l'indice polytropique newtonien usuel 1.** [Source primaire, §5, équations (48)–(52) et tableau 1](https://arxiv.org/pdf/1602.05961).

Posons c₀=uc/3+A/B³. Au centre, (5)–(6) donnent

\[
 h=\sqrt{c_0s}+O(s),\quad
 u=uc-\frac23\sqrt{c_0}s^{3/2}-\frac{c_0s^2}{18}+O(s^{5/2}),
\]
\[
 v=\frac{uc\,s^3}{3}-\frac4{27}\sqrt{c_0}s^{9/2}
 -\frac{c_0s^5}{90}+\cdots,\qquad
 \chi\sim\sqrt3(c_0s)^{-1/4}. \tag{8}
\]

Ainsi la densité est finie, sa dérivée s'annule, et l'accélération tend vers zéro. Cependant χ diverge et U'' diverge comme s⁻¹ᐟ². Il s'agit d'une solution centrale faible du problème adiabatique dégénéré, **pas d'un fond complet lisse à deux champs**. La description adiabatique devient aussi non uniforme au passage h=3, où ℬ′(h) tend vers zéro depuis la branche inférieure. Les résultats numériques ci-dessous ne suppriment aucune de ces limites.

## 4. Grille commune et résultats

Les mêmes paramètres physiques sont employés pour tous les cas : a₀=1,2×10⁻¹⁰ m/s² et rK=3 kpc, donc K=3,59360×10³⁰ m⁵ kg⁻¹ s⁻². Cela donne ρ*=1,54559×10⁻²¹ kg/m³=0,8670 GeV/cm³, M*=7,74819×10⁹ masses solaires et cs=105,397√u km/s. Il s'agit d'entrées illustratives, pas de valeurs mesurées ou ajustées par notre calcul.

Pour m=0,1 eV pris comme autre entrée commune, K=0,00927678 eV⁻⁴ et g₄=7,42143×10⁻⁶ dans la convention donnée plus haut. cs²/c²=1,23598×10⁻⁷u reste petit dans la grille. La longueur ℏ/(2mcs) vaut 2,806 mm à u=1 : cela motive l'approximation de Thomas–Fermi dans un intérieur variant sur des kiloparsecs, mais elle diverge à la surface. Ce contrôle ne teste ni la thermalisation ni la condensation.

Un contrôle particulaire empêche de présenter ce point illustratif comme viable. Dans la limite diluée de Born pour bosons identiques, g_NR=g₄/(4m²), a_sc=g₄/(16πm), σ=8πa_sc² ; ces relations donnent σ/m=g₄²/(32πm³). Après conversion, le point m=0,1 eV donne **σ/m=1,19668×10¹⁴ cm²/g**. Ce résultat est très éloigné des contraintes usuelles sur une matière sombre dominante à diffusion binaire indépendante de la vitesse. À titre de comparaison, les simulations du Bullet Cluster de Randall et al. donnent une limite conditionnelle de 0,7 cm²/g avec une hypothèse sur les rapports masse/luminosité initiaux. [Randall et al., *Constraints on the Self-Interaction Cross-Section of Dark Matter from Numerical Simulations of the Merging Galaxy Cluster 1E 0657-56*, 2008](https://arxiv.org/abs/0704.0261).

À K fixé, σ/m∝m⁵ : imposer seulement la valeur de référence 1 cm²/g déplacerait m vers 1,52899×10⁻⁴ eV. C'est une conversion paramétrique, pas une prédiction ni un domaine astrophysique validé. Une éventuelle réponse collective différente en amas doit être calculée avant d'écarter ces contraintes. Les 27 solutions hydrostatiques dépendent de K et a₀, donc restent les mêmes sous ce changement de m accompagné du changement de g₄ requis ; leur réalisation microscopique reste à établir.

Voici une fenêtre **paramétrique**, gardant exactement le même K et les mêmes profils. Pour comparer au secteur 5D, on choisit séparément L=1 micromètre, uniquement comme entrée illustrative. Alors ℏc/L=0,197327 eV ; dans l'intervalle plat de référence le premier mode KK non nul aurait πℏc/L=0,619921 eV.

| mΦ (eV) | g₄ | σ/m en cm²/g, limite de Born | mΦL/(ℏc) | longueur de cicatrisation à ρ* |
|---:|---:|---:|---:|---:|
| 10⁻¹ | 7,4214×10⁻⁶ | 1,1967×10¹⁴ | 0,50677 | 2,806 mm |
| 10⁻³ | 7,4214×10⁻¹⁴ | 1,1967×10⁴ | 0,0050677 | 0,2806 m |
| 10⁻⁴ | 7,4214×10⁻¹⁸ | 0,11967 | 0,00050677 | 2,806 m |
| 10⁻⁵ | 7,4214×10⁻²² | 1,1967×10⁻⁶ | 0,000050677 | 28,06 m |

À la densité galactique explicitement choisie ρ*=1,54559×10⁻²¹ kg/m³, le paramètre non relativiste g₄ρ*/mΦ⁴=8Kρ*/c²=4,94392×10⁻⁷ est **identique** sur les quatre lignes. Même à 10ρ*, il reste 4,94392×10⁻⁶. Les trois petites masses séparent mieux mΦ et ℏc/L, et les deux dernières passent sous la valeur illustrative σ/m=1 cm²/g dans le calcul de collision. Cela fournit une piste concrète pour le raccord des paramètres du mode léger ; cela ne démontre ni son origine, ni sa naturalité, ni la stabilité de la troncation KK avec interactions. Dans un fond courbe, le spectre réel doit être calculé et mΦ désigne ici la masse effective à quatre dimensions.

Le test de collision suppose une phase traitable par diffusion binaire de particules identiques, diluée, avec interaction de contact au régime de Born ; les contraintes d'amas ne sont donc pas une exclusion universelle des phases collectives de Khoury. Inversement, invoquer une phase collective ne les annule pas sans calcul. La thermalisation, la densité de charge, la formation cosmologique et les fluctuations doivent encore sélectionner ou rejeter ces exemples.

La grille cartésienne est uc∈{0,1;1;10}, A∈{0,1;1;10}, B∈{0,5;1;2}. Aucun de ces 27 points n'a été ajusté à une galaxie ou à la RAR. Chaque uc est appliqué à toutes les masses et tailles baryoniques de la grille. Le tableau présente la tranche B=1.

| uc | A | S=Rhalo/rK | Msf,total/Mb,total | f(r=rb) | Δ à r=rb, dex |
|---:|---:|---:|---:|---:|---:|
| 0,1 | 0,1 | 0,594207 | 0,021619 | hors fluide | — |
| 0,1 | 1 | 0,275774 | 0,0002313 | hors fluide | — |
| 0,1 | 10 | 0,121394 | 0,00000204 | hors fluide | — |
| 1 | 0,1 | 2,063954 | 8,10924 | 6,7602 | +0,4643 |
| 1 | 1 | 1,428488 | 0,262140 | 0,4929 | +0,0962 |
| 1 | 10 | 0,480138 | 0,001362 | hors fluide | — |
| 10 | 0,1 | 3,137002 | 312,498 | 84,7649 | +1,1981 |
| 10 | 1 | 3,078117 | 28,4546 | 8,3405 | +0,7112 |
| 10 | 10 | 2,191310 | 0,839028 | 0,6707 | +0,2229 |

Ici f(r)=Msf(<r)/Mb(<r), et Δ=log₁₀[h(bbar+v/s²)/h(bbar)]. Ce sont des rapports de masses **enfermées** à r, distincts du rapport total dans la quatrième colonne. Une case hors fluide ne constitue pas une réussite RAR : la continuation physique extérieure n'est pas calculée. Sur la grille complète, 14/27 halos atteignent rb, 7/27 atteignent 2rb, 5/27 atteignent 3rb. Ce comptage décrit uniquement cette grille arbitraire, sans probabilité astrophysique.

## 5. Obstruction analytique et portée RAR

Dans le régime profond où la source sombre et les baryons subissent la même gravité,

\[
 \frac{g_{\rm total}}{g_{\rm baryons\ seuls}}\simeq\sqrt{1+f(r)},\qquad
 \Delta\simeq\tfrac12\log_{10}[1+f(r)]. \tag{9}
\]

Pour exiger un surplus maximal δ dex dans ce régime, il faut f≤10²ᵟ−1 ; δ=0,1 impose f≤0,5849. C'est une conséquence du modèle, pas une borne issue d'un ajustement statistique.

Une obstruction supplémentaire découle de la régularité des densités :

\[
 f(0^+)=\frac{uc\,B^3}{3A},\qquad
 \Delta(0^+)\simeq\tfrac12\log_{10}\left(1+\frac{uc\,B^3}{3A}\right). \tag{10}
\]

Tant que uc est un paramètre d'état libre, les mêmes baryons autorisent différentes accélérations. L'équilibre seul ne sélectionne donc pas une RAR baryonique unique. Des corrélations d'état issues de la formation, une faible fraction sombre dans la région observée ou une autre fermeture peuvent changer ce diagnostic ; elles doivent être calculées, pas présumées. La nécessité de distinguer masse totale et masse baryonique est déjà identifiée dans la discussion de Khoury après son équation (61). [Source primaire, §5](https://arxiv.org/pdf/1602.05961).

Nos cas uc=0,1 ont souvent peu de masse sombre mais un petit domaine de fluide. Augmenter uc peut étendre le domaine tout en produisant un surplus gravitationnel important. Cela quantifie une tension de cette réalisation ; cela ne prouve pas l'impossibilité de toutes les EOS, de toutes les conditions de formation, ou de toutes les variantes de gravité modifiée.

## 6. Gradients de χ : trois intérieurs réguliers calculés

On restaure (4) en posant

\[
 \ell=\frac{Z}{\sqrt2M_4a_0r_K},\qquad
 \chi''+\frac2s\chi'=
 \frac{h^2\chi}{\ell^2}\left[-(1+\chi^2)^{-2}+h^2/9\right]. \tag{11}
\]

À chaque pas, h est la racine positive de h/(1+χ²)+2χ²h³/9=b. Le centre fini χ(0)=χc, χ′(0)=0 possède l'expansion

\[
 h=(1+\chi_c^2)c_0s+O(s^3),\quad
 u=uc-\tfrac12(1+\chi_c^2)c_0s^2+\cdots,
\]
\[
 \chi=\chi_c-\frac{c_0^2\chi_c}{20\ell^2}s^4+\cdots. \tag{12}
\]

La singularité centrale de l'approximation adiabatique est alors absente. On impose **pour ce problème intérieur seulement** χ(S)=0 au premier zéro de u, puis on ajuste χc par tir. On conserve une branche sans zéro intérieur de χ, trouvée à la frontière du domaine de tirs positifs dans les encadrements documentés. Cela ne prouve pas l'unicité des solutions.

Pour A=B=uc=1, les sorties sont :

| ell | χc | S | Msf,total/Mb,total | χ′(S) | Δ(rb), dex |
|---:|---:|---:|---:|---:|---:|
| 0,3 | 0,66942734 | 1,92515217 | 0,51881895 | −0,365103 | +0,01414 |
| 0,1 | 1,61837908 | 1,48221762 | 0,25585530 | −3,174515 | +0,11270 |
| 0,03 | 1,94948777 | 1,44096537 | 0,26014426 | −13,454833 | +0,09675 |

Chaque ell représente un choix commun de Z pour une théorie ; on ne l'ajuste pas à chaque galaxie. Cette série ne balaie qu'une configuration baryonique. Un petit écart à rb n'est pas une réussite sur toute la courbe : pour ell=0,3, Δ(0,1rb)=−0,2351 dex. À χ fini, l'approximation (9) n'est plus applicable ; les corrections gravitationnelles et la masse sombre agissent ensemble.

**Ce ne sont pas encore des halos globaux physiquement raccordés.** Comme χ′(S) est non nul, on ne peut pas coller ces intérieurs à un extérieur identiquement χ=0 sans une source de surface. Il faut résoudre l'extérieur et la continuité du flux de χ, ou dériver une action de surface/une transition de phase. De plus, la masse totale sombre diffère entre les trois solutions : comparer directement leurs énergies ne serait pas un test à charge fixée. Aucun spectre de stabilité couplé n'a été calculé ici.

## 7. Vérifications et fichiers reproductibles

- `halo_hydrostatic.py` : solveur standard Python, Dormand–Prince 5(4) adaptatif, événement premier zéro par bissection, interpolation cubique de Hermite pour les profils ; résultats dans `halo_hydrostatic.json`.
- `halo_chi_boundary.py` : tir à centre régulier, frontière χ imposée, contrôles de convergence ; résultats dans `halo_chi_boundary.json`.
- `gradient_halo_scan.py` et son JSON : exploration préalable des tirs, y compris des branches à nœuds. Ce balayage n'est pas un catalogue de solutions physiques sélectionnées.

Les scripts ne dépendent que de la bibliothèque standard Python et écrivent leurs JSON à côté d'eux par défaut. Depuis le dossier qui les contient :

```text
python halo_hydrostatic.py
python halo_chi_boundary.py
```

Le benchmark newtonien sans baryons donne u=sin(s)/s, S=π, v(S)=π. Les erreurs numériques sont 1,0×10⁻¹³ sur S, 3,1×10⁻¹¹ sur v et 1,6×10⁻¹⁰ au maximum sur 299 points du profil interpolé. Le benchmark MOND profond sans baryons donne S=2,24224861 et |u′(S)|=0,45979063 ; le tableau primaire arrondit à 2,25 et 0,46, ce qui est un contrôle de cohérence, pas une référence de haute précision.

Pour trois cas adiabatiques représentatifs, resserrer la tolérance de 10⁻⁸ à 2×10⁻¹¹ change S de moins de 3,4×10⁻⁷ relativement et la masse de moins de 1,2×10⁻⁶. Ces différences mesurent une convergence, pas une borne d'erreur rigoureuse pour tous les profils. Pour les trois tirs à χ fini, la condition |χ(S)|/χc est inférieure à 3,1×10⁻⁹ et les variations relatives de S et M sont inférieures à 2×10⁻¹⁰ entre les tolérances testées. La précision numérique ne valide pas la condition extérieure choisie.

## 8. Ce qui a avancé et la prochaine fermeture nécessaire

Le profil sombre n'est plus une entrée arbitraire : il est calculé avec sa propre gravité et sa pression. Le rayon de fluide est une sortie pour un état choisi. La source de la modification gravitationnelle est variée de manière cohérente. Le calcul isole quantitativement l'effet de la masse sombre, détecte le centre adiabatique singulier et construit trois intérieurs réguliers avec gradients.

Pour une extension RAR publiable comme réalisation physique, les prochaines exigences sont précises : fixer la charge/masse par une hypothèse de formation testable, obtenir un raccord extérieur et une transition de phase, vérifier la stabilité à masse fixée, puis comparer des galaxies avec paramètres de théorie communs et géométrie baryonique adaptée. Le lien 5D doit également dériver les opérateurs de (1) et leurs coefficients ; choisir K, a₀ et Z ici ne suffit pas. Le rayon compact R n'est ni le rayon de halo S rK, ni la longueur de gradients ell rK, et il n'est pas prédit par cette étude.

Cette note constitue un calcul conditionnel et reproductible avec une limitation analytique explicite. Elle ne revendique ni une origine DDF établie de la RAR, ni une nouveauté bibliographique démontrée, ni une validation par les observations.
