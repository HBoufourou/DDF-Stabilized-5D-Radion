# R64 — Rapport arbitral intégré final

**Date :** 4 septembre 2026  
**Rôle :** seconde lecture hostile, mathématique et éditoriale  
**Corpus principal :** `R64_REPORT.md`, `R64_CLAIM_LEDGER.csv`,
`R64_DATA_MANIFEST.json`, `R64_ERRATA_R62_R63.md`,
`R64_ARTICLE1_DECISION.md`, `meta_audit_r64/equivariant_nogo.md` et
`meta_audit_r64/no_go_novelty_comparison.md`.

## 1. Verdict binaire

```text
NOYAU_PARITE_HODGE_RATIONNEL_CONDITIONNEL = PASS
TABLE_DES_QUATRE_SIGNES                  = PASS
PREUVE_DU_TROIS_PLAN                     = PASS
THEOREME_INTEGRAL_DE_TUBE                = NOT_YET_ESTABLISHED
REALISATION_ORIENTIFOLD_GLOBALE           = NOT_ESTABLISHED
COROLLAIRE_R63_EFFECTIF_NS_U2             = CONDITIONAL_ON_GENERICITY
NOUVEAUTE_PHYSIQUE_LARGE                  = FAIL
ARTICLE_AUTONOME_DE_NO_GO                 = FAIL
PROPOSITION_DANS_UN_ARTICLE_ETROIT        = PASS_WITH_LIMITS
SOUMISSION_IMMEDIATE                      = HOLD
```

Le dossier passe uniquement comme **énoncé rationnel conditionnel et borné** :
si l'on dispose d'une involution holomorphe globale au-dessus de l'identité de
la base, de la projection standard indiquée, et d'une tube map équivariante,
alors la classe active propre qui alimente un vecteur fermé de \(C_4\) est de
carré strictement négatif. Le calcul de Hodge qui produit cette conclusion est
correct.

Ce verdict ne valide ni un théorème intégral de cycles proches, ni l'existence
d'un quotient O3/O7 ou O5/O9 global du modèle R63, ni une obstruction à toute
tour, ni une nouveauté physique générale. Il ne rend pas l'Article 1 prêt à
soumettre.

## 2. Recalcul des quatre parités

Avec

\[
s=\epsilon_{\Omega_3},\qquad
\eta=\begin{cases}+1&\text{branches préservées},\\-1&\text{branches échangées},\end{cases}
\]

le modèle \(uv=t\), avec \(t\) fixé, donne

\[
\epsilon_{\Omega_S}=s\eta.
\]

La réversion du cercle de plomberie sous l'échange des branches donne, pour
une classe propre \(C\),

\[
\epsilon_{\operatorname{Tub}(C)}=\eta\epsilon_C.
\]

Dans les conventions standard utilisées par le dossier, les vecteurs de
\(C_4\) proviennent de \(H^3_+\) en O3/O7 et de \(H^3_-\) en O5/O9 ; leur
parité est donc \(-s\). La condition de survie est

\[
\eta\epsilon_C=-s,
\qquad
\epsilon_C=-s\eta=-\epsilon_{\Omega_S}.
\]

Le recalcul donne exactement :

| Projection | Branches | \(s\) | \(\eta\) | \(\epsilon_{\Omega_S}\) | \(\epsilon_C\) |
|---|---|---:|---:|---:|---:|
| O3/O7 | préservées | \(-1\) | \(+1\) | \(-1\) | \(+1\) |
| O3/O7 | échangées | \(-1\) | \(-1\) | \(+1\) | \(-1\) |
| O5/O9 | préservées | \(+1\) | \(+1\) | \(+1\) | \(-1\) |
| O5/O9 | échangées | \(+1\) | \(-1\) | \(-1\) | \(+1\) |

Il n'y a pas d'erreur de signe dans les trois documents. En revanche,
« quatre cas couverts » signifie seulement que les quatre **implications
formelles de signe** sont traitées. Cela ne démontre l'existence globale
d'aucun de ces quatre cas. En particulier, branches échangées,
\(\sigma|_S=\mathrm{id}\) est compatible avec la ligne O3/O7, où le secteur
anti-invariant requis est nul, mais incompatible avec la ligne O5/O9, où
\(\Omega_S\) devrait être anti-invariante.

## 3. Tube homologique, cohomologie et réseau actif

Le dossier emploie alternativement une classe \(C\in H_2(S,\mathbb Z)\), sa
duale de Poincaré dans \(H^2(S,\mathbb Z)\), un élément du quotient actif et un
élément de \(L^\perp\). Ces objets ont le même espace vectoriel rationnel
pertinent, mais pas la même structure intégrale.

Le gradin actif naturel est

\[
Q=H^2(S,\mathbb Z)/L,
\]

tandis que le réseau orthogonal est

\[
K=L^\perp\subset H^2(S,\mathbb Z).
\]

Si \(L\) est non dégénéré, la projection orthogonale donne

\[
Q_{\mathbb Q}\simeq K_{\mathbb Q}.
\]

Elle ne donne généralement pas \(Q=K\) sur \(\mathbb Z\). Dans l'application
\(L=U(2)\) primitive, \(L\oplus K\) est d'indice quatre dans le réseau K3 ;
le quotient \(Q\) est le sur-réseau correspondant, équivalent à \(K^\vee\),
et non le sous-réseau \(K\) lui-même. Le passage rationnel du rapport est donc
la bonne réparation : un élément propre intégral de \(Q\) possède un
représentant orthogonal rationnel propre ; après multiplication par un
dénominateur, ni sa parité ni le signe de son carré ne changent.

Mais cette réparation ne remplace pas une preuve intégrale de la tube map. Un
énoncé intégral doit expliciter :

1. la classe homologique \(c\in H_2(S,\mathbb Z)\) et sa duale de Poincaré ;
2. le quotient par les classes prolongeables et les éventuels noyaux/torsions ;
3. le morphisme de tube vers \(H_3(Y_t,\mathbb Z)/\mathrm{tors}\) ;
4. l'identité équivariante
   \(\sigma_*\operatorname{Tub}(c)=\eta\operatorname{Tub}(\sigma_*c)\) ;
5. la dualité de Poincaré équivariante qui transporte cette valeur propre au
   \(H^3\) sur lequel \(C_4\) est développé ;
6. les saturations et cosets de discriminant.

Le script `r64_equivariant_nogo_audit.py` vérifie l'arithmétique des signes ;
il ne prouve aucun de ces six points. `R64_ARTICLE1_DECISION.md`, porte A6,
reconnaît correctement que cette fermeture est seulement partielle. Cette
réserve doit remonter dans le statut des claims C07, C09 et C23.

## 4. Existence de la classe ample invariante

Sur ce point, la version de `R64_REPORT.md` est correcte et plus précise que
la simple hypothèse de `equivariant_nogo.md`. Si \(\mathcal H\) est relativement
ample sur la famille projective et si \(\sigma\) est une involution globale au-
dessus de la base, alors

\[
h=c_1\!\left((\mathcal H\otimes\sigma^*\mathcal H)|_S\right)
\]

est intégrale, ample et \(\sigma\)-invariante. Elle appartient à \(L\), car le
fibré se restreint depuis les composantes, y compris lorsqu'elles sont
échangées. De même, la globalité de \(\sigma\) rend \(L\) stable.

Il faut conserver cette construction dans tout énoncé final. Si l'on part au
contraire d'un réseau abstrait \(L\), « \(L\) contient une ample » et
« \(L\) est \(\sigma\)-stable » doivent rester des hypothèses. Les supprimer
rend l'énoncé faux, comme le témoin \(L_0=\mathbb Zh_1\subset U(2)\) le montre.

## 5. Vérification du trois-plan positif

Le cœur de la preuve est valide. Sur une K3 projective,

\[
P=\langle\operatorname{Re}\Omega_S,
          \operatorname{Im}\Omega_S,h\rangle
\]

est positif défini de dimension trois. La parité opposée de \(C\) et
\(\Omega_S\) force \(C\perp\Omega_S\). Si \(C\) est anti-invariant,
l'invariance de \(h\) force \(C\perp h\). Si \(C\) est invariant, l'activité
\(C\in L^\perp_{\mathbb Q}\) et \(h\in L\) force encore \(C\perp h\). Donc
\(C\in P^\perp\), lequel est négatif défini dans la signature \((3,19)\), et

\[
C\ne0\quad\Longrightarrow\quad C^2<0.
\]

La même parité montre aussi que la classe rationnelle propre est de type
\((1,1)\). Il n'y a ici ni recours caché à \(U(2)\), ni besoin de la
classification de Nikulin. L'argument est cependant un corollaire élémentaire
de l'indice de Hodge après admission de la parité du tube ; il ne doit pas
être présenté comme un nouveau théorème abstrait sur les K3.

## 6. Corollaire \(\operatorname{NS}(S)=L=U(2)\)

Le corollaire logique est correct : si

\[
\operatorname{NS}(S)_{\mathbb Q}=L_{\mathbb Q}=U(2)_{\mathbb Q},
\]

la parité opposée à celle de \(\Omega_S\) place \(C\) dans
\(\operatorname{NS}(S)_{\mathbb Q}\), tandis que l'activité le place dans
\(L^\perp_{\mathbb Q}\). La non-dégénérescence de \(U(2)\) donne \(C=0\).

La lacune est l'application non conditionnelle au paquet R63. La porte A3 de
`R64_ARTICLE1_DECISION.md` est `PARTIAL` : la dominance de la sous-famille de
coefficients R63 vers la famille pertinente des branches \((4,4)\), ou au
moins sa non-inclusion dans un lieu de Noether--Lefschetz, n'est pas fermée.
Ainsi, le dossier peut écrire aujourd'hui :

> pour toute couture R63 satisfaisant
> \(\operatorname{NS}(S)=L=U(2)\), le secteur propre actif requis est nul ;

mais non :

> le membre très général de la sous-famille R63 a effectivement
> \(\operatorname{NS}(S)=U(2)\),

avant la fermeture de A3. Sur un lieu de Noether--Lefschetz compatible, le
théorème de négativité reste valable sous ses hypothèses, mais le secteur peut
être non nul.

## 7. Portée physique

La majorité des garde-fous du dossier est correcte : tour KK neutre, secteurs
ouverts/relatifs, paire brane--image, flux, tadpoles, stabilité BPS,
corrections quantiques, relation \(R(t)\), microns et plan de Fano restent
hors conclusion.

Deux formulations doivent toutefois être systématiquement bornées.

- « Le tube survit comme vecteur de \(C_4\) » est d'abord une condition sur
  une classe homologique/cohomologique et sur un mode du champ fermé. Elle ne
  construit pas un état D3 orientifoldé, ne prouve pas sa calibration et ne
  calcule pas son indice.
- « Le mécanisme de Hassfeld et al. est exclu » doit devenir « aucune charge
  propre active du secteur fermé \(C_4\) considéré ne satisfait la condition
  géométrique \(C^2\ge0\) utilisée par ce mécanisme, sous les hypothèses du
  théorème ». Le mécanisme parental \(\mathcal N=2\) et toute autre tour ne
  sont pas exclus.

Pour O5/O9, la table de réduction fermée suffit au calcul de signe, mais pas à
la validation d'un orientifold physique. Lieux fixes, action complète sur la
D3, branes requises et annulation des tadpoles doivent être construits avant
toute revendication de réalisation O5/O9.

## 8. Nouveauté et cohérence éditoriale

Le verdict de `no_go_novelty_comparison.md` est cohérent avec les sources
primaires citées : le message large O3/O7 et les cas O-type A/B rencontrent
des antériorités directes chez Kaufmann--Monnee--Weigand--Wiesner ; les
parités de départ viennent de Grimm--Louis ; le mécanisme parental vient de
Hassfeld--Monnee--Weigand--Wiesner. Le dossier a donc raison de refuser les
expressions « premier no-go », « obstruction quantique générale » et
« article autonome de no-go ».

La seule nouveauté encore envisageable est une synthèse très étroite : formule
uniforme à quatre lignes, preuve de la tube map équivariante dans une famille
de Tyurin et application au paquet relatif R63. L'absence de collision dans
le corpus inspecté ne prouve pas la priorité. Le statut
`POSSIBLY_NEW_SYNTHESIS`/`PLAUSIBLE_NOT_CERTIFIED` est admissible ; le mot
« nouveau » sans ce qualificatif ne l'est pas.

Il n'y a donc pas de contradiction éditoriale fatale entre
`PASS_NARROW`, `ARTICLE_1_READY_FOR_SUBMISSION = NO` et
`STANDALONE_THEOREM_PAPER = NO` : le premier est un seuil interne de
substance conditionnelle, les deux autres sont des verdicts de diffusion.

## 9. Contradictions et suraffirmations à corriger

1. **Tube map :** C07 est marqué `PROVED` alors que les rapports prennent
   l'équivalence intégrale de la tube map comme hypothèse et A6 reste
   `PARTIAL`. Remplacer le statut par
   `PROVED_CONDITIONALLY_RATIONAL; INTEGRAL_EQUIVARIANCE_OPEN`, ou fournir la
   preuve intégrale.
2. **Orthogonal contre quotient :** le théorème de
   `equivariant_nogo.md` porte sur \(C\in L^\perp\) intégral, alors que le
   mécanisme naturel vit dans \(H^2(S)/L\). Harmoniser tous les fichiers sur
   le quotient avec représentant orthogonal rationnel ; ne réserver la
   version intégrale qu'après contrôle des saturations.
3. **Très général :** C12 est `PROVED_VERY_GENERAL`, tandis que A3 reconnaît
   que la généricité de la sous-famille R63 n'est pas démontrée. Remplacer par
   `PROVED_CONDITIONAL_ON_NS_EQUALS_U2` jusqu'à fermeture de A3.
4. **Quatre cas :** `O3O7_AND_O5O9 = COVERED` peut se lire comme une
   réalisation. Remplacer par
   `FOUR_STANDARD_TRUNCATION_SIGN_CASES = COVERED_CONDITIONALLY` et ajouter
   `GLOBAL_ORIENTIFOLD_REALIZATIONS = NOT_CONSTRUCTED`.
5. **Portée physique :** toute phrase sans les qualificatifs « fermé »,
   « propre », « actif », « \(C_4\) », « condition \(C^2\ge0\) » et
   « sous les hypothèses » doit être refusée.
6. **Nouveauté :** conserver `FAIL_BROAD_NOVELTY`; ne promouvoir la synthèse
   à quatre cas au-delà de `POSSIBLY_NEW_SYNTHESIS` qu'après vérification
   experte et recherche ciblée O5/O9.
7. **Reproductibilité :** au moment de cette lecture,
   `python3 r64_substance_gate.py` échoue sur
   `missing report: R64_MANIFEST.sha256`; `R64_AUDIT_OUTPUT.txt` est également
   absent. Après intégration du présent rapport, régénérer le manifeste, puis
   la sortie figée, et rejouer le gate jusqu'à code retour zéro. Les trois
   sous-certificats spécialisés passent déjà.

## 10. Formulation finale admissible

La formulation suivante franchit cette relecture :

> Soit une dégénérescence projective de Tyurin à deux composantes, munie
> d'une involution holomorphe globale au-dessus de l'identité de la base.
> Supposons le réseau prolongeable stable, la tube map équivariante avec le
> signe du cercle de plomberie, et la troncature fermée standard O3/O7 ou
> O5/O9. Via l'identification rationnelle
> \(H^2(S,\mathbb Q)/L_{\mathbb Q}\simeq L^\perp_{\mathbb Q}\), toute classe
> propre active non nulle dont le tube appartient au secteur vectoriel
> survivant de \(C_4\) a carré strictement négatif. Elle ne satisfait donc pas
> la condition \(C^2\ge0\) du mécanisme fermé multi-enroulé considéré.

Ajouter immédiatement : la proposition est classique dans son cœur Hodge,
conditionnelle quant à la tube map et au quotient orientifold, recoupe des
antériorités O3/O7, ne couvre aucune tour KK/ouverte/relative, et n'est pas un
article autonome.

R64_INTEGRATED_REFEREE_VERDICT: PASS_WITH_LIMITS

