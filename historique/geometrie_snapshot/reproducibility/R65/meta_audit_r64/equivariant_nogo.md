# R64 — Obstruction uniforme de parité–Hodge pour les tubes de Tyurin

**Voie B :** proposition rationnelle conditionnelle pour O3/O7 **et** O5/O9  
**Date :** 4 septembre 2026  
**Certificat exact :** `meta_audit_r64/r64_equivariant_nogo_audit.py`

## 1. Verdict

Le stop-test de R62 n'est pas propre au scan diagonal de Cox, ni au réseau
\(U(2)\), ni à la seule projection O3/O7. Sous les hypothèses précises du
§3, il devient l'énoncé uniforme suivant.

> **Proposition conditionnelle (obstruction de parité–Hodge).** Soit une dégénérescence
> projective de Tyurin à deux composantes \(Y_1\cup_S Y_2\), munie d'une
> involution holomorphe globale \(\sigma\) au-dessus du paramètre \(t\).
> Posons \(s=\epsilon_{\Omega_3}\in\{+1,-1\}\), avec \(s=-1\) pour O3/O7 et
> \(s=+1\) pour O5/O9, et \(\eta=+1\) si les composantes sont préservées,
> \(\eta=-1\) si elles sont échangées. Soit une classe propre active non
> nulle dans \(Q_{\mathbb Q}=H^2(S,\mathbb Q)/L_{\mathbb Q}\), et soit
> \(C\in L_{\mathbb Q}^{\perp}\) son représentant orthogonal. Si la tube map
> équivariante possède le signe de plomberie déclaré et si le tube fermé
> survit comme vecteur de \(C_4\), alors
> \[
> C^2<0.
> \]
> Il n'existe donc aucune telle classe de carré \(C^2\geq0\), dans aucune
> des quatre combinaisons O3/O7–O5/O9 et préservation–échange.

La conclusion exclut seulement le mécanisme fermé, à charge propre unique,
qui demande une classe active \(C^2\geq0\) pour produire la tour
multi-enroulée. Elle ne démontre ni l'absence d'une tour KK métrique, ni
l'absence de secteurs ouverts ou relatifs, ni l'instabilité d'une
configuration brane–image.

## 2. La formule uniforme des signes

Dans le modèle local \(uv=t\), sur une fibre lisse,

\[
\Omega_3=\Omega_S\wedge d\log u.
\]

Le cercle de plomberie, ou de façon équivalente \(d\log u\), a le signe
\(\eta\). Par conséquent

\[
\epsilon_{\Omega_S}=s\eta.
\]

Pour l'orientifold standard de type IIB, les vecteurs fermés issus de
\(C_4\) appartiennent à \(H^3_{-s}\) : ils sont pairs en O3/O7 et impairs en
O5/O9. Comme

\[
\epsilon_{\operatorname{Tub}(C)}=\eta\epsilon_C,
\]

la survie du tube impose

\[
\eta\epsilon_C=-s,
\qquad\text{donc}\qquad
\boxed{\epsilon_C=-s\eta=-\epsilon_{\Omega_S}}.
\]

La classe de base et la forme holomorphe de la K3 ont toujours des signes
opposés. La table complète est :

| Projection | \(s\) | Action sur les branches \(\eta\) | \(\epsilon_{\Omega_S}=s\eta\) | Parité \(C_4=-s\) | \(\epsilon_C=-s\eta\) |
|---|---:|---:|---:|---:|---:|
| O3/O7 | \(-1\) | préservées \(+1\) | \(-1\) | \(+1\) | \(+1\) |
| O3/O7 | \(-1\) | échangées \(-1\) | \(+1\) | \(+1\) | \(-1\) |
| O5/O9 | \(+1\) | préservées \(+1\) | \(+1\) | \(-1\) | \(-1\) |
| O5/O9 | \(+1\) | échangées \(-1\) | \(-1\) | \(-1\) | \(+1\) |

Cette table corrige la formulation exclusivement O3/O7 de la première
version de R64.

## 3. Hypothèses exactes

Soit

\[
\pi:\mathcal Y\longrightarrow\Delta,
\qquad \mathcal Y_0=Y_1\cup_S Y_2,
\]

une dégénérescence semistable projective de Calabi–Yau trois-dimensionnels,
localement \(uv=t\) le long de la K3 projective \(S\). On suppose :

1. \(\sigma:\mathcal Y\to\mathcal Y\) est une involution holomorphe globale
   et \(\pi\circ\sigma=\pi\) ; en particulier, elle fixe le paramètre \(t\),
   et non seulement la fibre centrale ;
2. elle préserve séparément \(Y_1,Y_2\), ou les échange ;
3. \(s=\epsilon_{\Omega_3}\) est le signe standard : \(-1\) pour O3/O7,
   \(+1\) pour O5/O9 ;
4. \(L\subset\operatorname{NS}(S)\) est le réseau prolongeable engendré par
   les images des restrictions depuis les composantes ; il est non dégénéré,
   \(\sigma\)-stable et contient une classe ample ;
5. la charge considérée est une classe non nulle du quotient actif
   \(Q_{\mathbb Q}=H^2(S,\mathbb Q)/L_{\mathbb Q}\), propre pour
   \(\sigma^*\), identifiée à son représentant orthogonal rationnel
   \(C\in L_{\mathbb Q}^{\perp}\) ;
6. la tube map de Clemens est supposée équivariante et possède le signe local
   \(\epsilon_{\operatorname{Tub}(C)}=\eta\epsilon_C\) ;
7. on conserve exactement le secteur vectoriel fermé de \(C_4\), de parité
   \(-s\).

L'identification \(Q_{\mathbb Q}\simeq L_{\mathbb Q}^{\perp}\) utilise la
non-dégénérescence de \(L\). Elle n'est en général pas une identification
intégrale : pour \(L=U(2)\), les cosets discriminants doivent encore être
traités dans une construction intégrale de la tube map.

L'hypothèse « \(L\) contient une ample » est essentielle lorsque
\(\epsilon_{\Omega_S}=-1\). Elle ne doit pas être supprimée en particulier
dans la ligne O5/O9 à branches échangées. Dans les lignes
\(\epsilon_{\Omega_S}=+1\), l'argument est même plus fort et n'a pas besoin
de l'orthogonalité à \(L\), mais la proposition garde une formulation commune.

## 4. Preuve par le 3-plan positif

Choisissons \(h_0\in L\) ample. La classe

\[
h=h_0+\sigma^*h_0
\]

est ample, \(\sigma\)-invariante et appartient encore à \(L\). Dans
\(H^2(S,\mathbb R)\), de signature \((3,19)\), le sous-espace

\[
P=\langle\operatorname{Re}\Omega_S,
          \operatorname{Im}\Omega_S,h\rangle
\]

est un 3-plan positif.

La relation de parité démontrée au §2 est
\(\epsilon_C=-\epsilon_{\Omega_S}\). Il y a deux cas, indépendamment du type
O3/O7 ou O5/O9.

### 4.1 \(\epsilon_{\Omega_S}=+1\) et \(\epsilon_C=-1\)

L'invariance de l'intersection donne

\[
C\cdot\Omega_S
=(\sigma^*C)\cdot(\sigma^*\Omega_S)
=-C\cdot\Omega_S=0,
\]

et, puisque \(h\) est invariant,

\[
C\cdot h=-C\cdot h=0.
\]

Ainsi \(C\perp P\). L'orthogonal d'un 3-plan positif dans le réseau K3 est
négatif défini, donc \(C\ne0\Rightarrow C^2<0\).

### 4.2 \(\epsilon_{\Omega_S}=-1\) et \(\epsilon_C=+1\)

Le même calcul donne \(C\cdot\Omega_S=0\). L'activité et \(h\in L\)
donnent en outre \(C\cdot h=0\). Donc, à nouveau, \(C\perp P\) et

\[
C\ne0\quad\Longrightarrow\quad C^2<0.
\]

La preuve est donc une application uniforme de la signature K3 après le
calcul non trivial des parités du tube. Elle ne requiert aucune action
diagonale, torique ou de Cox, et ne requiert pas \(L=U(2)\).

## 5. Branche échangée et cas \(\sigma|_S=\mathrm{id}\)

L'échange \(Y_1\leftrightarrow Y_2\) n'implique pas automatiquement une
involution non triviale sur la couture. Il faut traiter séparément la
possibilité \(\sigma|_S=\mathrm{id}\).

- En O3/O7, \(s=-1\) et \(\eta=-1\), donc
  \(\epsilon_{\Omega_S}=+1\), ce qui est compatible avec l'identité. Mais le
  tube \(C_4\) exige \(\epsilon_C=-1\). L'espace anti-invariant de
  \(\sigma|_S=\mathrm{id}\) est nul : la seule classe admissible est
  \(C=0\).
- En O5/O9, \(s=+1\) et \(\eta=-1\), donc
  \(\epsilon_{\Omega_S}=-1\). Cela est incompatible avec
  \(\sigma|_S=\mathrm{id}\), qui fixe nécessairement \(\Omega_S\). Cette
  sous-branche n'existe pas sous les hypothèses standard.

Ainsi le cas identité n'est ni oublié ni assimilé à tort à une involution de
Nikulin. Si \(\sigma|_S\) est une involution symplectique non triviale,
son réseau anti-invariant est \(E_8(-2)\), donc négatif défini ; c'est une
description plus précise de l'un des quatre cas, non un ingrédient nécessaire
à la preuve.

## 6. Application conditionnelle à la couture R63

Pour une double couverture lisse très générale de
\(\mathbb P^1\times\mathbb P^1\) ramifiée en bidegré \((4,4)\), on a

\[
\operatorname{NS}(S)=L=U(2)
\]

Toute classe de parité opposée à
\(\Omega_S\) est de type \((1,1)\), donc appartient à
\(\operatorname{NS}(S)=L\). L'activité impose simultanément
\(C\in L^\perp\). Comme \(L\) est non dégénéré,

\[
L\cap L^\perp=0,
\qquad\boxed{C=0}.
\]

Ainsi, **si** la sous-famille de coutures produite par R63 domine la famille
\((4,4)\) pertinente — porte A3 encore ouverte — et si une involution
globale réalise la ligne considérée, le secteur propre actif requis est nul.
Ce corollaire conditionnel est plus fort que la proposition de signature.

Le calcul exact déjà certifié reste valable :

\[
O(U(2),\mathbb Z)=\{\pm I,\pm S\},
\]

les seules classes isotropes primitives de \(U(2)\) sont les deux rulings
avec leurs opposées, et \(L\cap L^\perp=0\). Ces faits illustrent
l'application, mais ne fondent pas la proposition générale.

## 7. Ce qui est prouvé et ce qui ne l'est pas

| Énoncé | Statut R64 |
|---|---|
| Formule \(\epsilon_C=-\epsilon_{\Omega_S}\) | dérivée rationnellement sous l'hypothèse d'une tube map équivariante avec le signe local |
| No-go \(C^2\geq0\) | prouvé pour le représentant orthogonal rationnel d'une classe active propre, sous les hypothèses du §3 |
| Tube map équivariante et saturations intégrales | ouvertes |
| O3/O7, branches préservées ou échangées | couvert |
| O5/O9, branches préservées ou échangées | couvert |
| Couture R63 si A3 établit \(\operatorname{NS}=L=U(2)\) | secteur requis nul conditionnellement |
| Relèvement global d'une involution candidate | hypothèse, non construit par cette proposition |
| Action qui envoie \(t\) sur \(-t\), \(\bar t\) ou une autre base | non couverte |
| Paire brane–image non réduite à une charge propre | non couverte |
| Existence et stabilité de D3/BPS multi-enroulées | non démontrées |
| Cycles relatifs, chaînes à bord et secteurs ouverts | non couverts |
| Tour KK métrique ou gravitationnelle | non exclue |
| Projections non géométriques ou anti-holomorphes | non couvertes |
| Dégénérescences à plus de deux composantes | non couvertes |

Il serait donc incorrect d'écrire « l'orientifold interdit toute tour ».
L'énoncé permis est : **sous l'hypothèse de tube équivariante, le secteur
vectoriel fermé de \(C_4\) ne contient aucune classe active propre dont le
représentant orthogonal rationnel a un carré non négatif pouvant alimenter ce
mécanisme de tube multi-enroulé.**

## 8. Contre-exemples qui rendent les hypothèses nécessaires

1. **Sans “active”.** Les rulings \(h_1,h_2\in U(2)=L\) sont invariants et
   isotropes. Ils ne sont pas dans \(L^\perp\).
2. **Sans ample dans \(L\).** Pour \(L_0=\mathbb Zh_1\), on a
   \(h_1\in L_0^\perp\) et \(h_1^2=0\). Le cas
   \(\epsilon_{\Omega_S}=-1\) ne peut donc pas se passer de l'hypothèse
   d'amplitude.
3. **Sans la parité orientifold.** Le réseau actif parental peut contenir un
   facteur hyperbolique et donc des isotropes ; ils se trouvent simplement
   dans le mauvais espace propre pour le vecteur \(C_4\) considéré.
4. **Sans “classe propre”.** Une somme \(h_1+e\), avec \(e\) isotrope dans un
   facteur hyperbolique actif et de signe opposé, peut être isotrope sans
   être propre. La proposition ne décide pas la projection ni la stabilité de
   la paire \(C,\sigma C\).

## 9. Portée pour DDF

R64 ferme une famille précise de réparations : changer seulement les signes
de Cox, choisir une autre classe propre non négative dans le même secteur, ou
passer de O3/O7 à O5/O9 ne sauve pas le mécanisme fermé \(C_4\) sous les
hypothèses déclarées.

Restent réellement ouvertes :

- une tour KK ou gravitationnelle dérivée de la métrique ;
- le mécanisme dans le parent \(\mathcal N=2\) avant projection ;
- un calcul explicite de paire brane–image ou de secteur ouvert/relatif ;
- une action sur la base qui sort de l'hypothèse \(\pi\circ\sigma=\pi\) ;
- un autre mécanisme spectral ne reposant pas sur une classe propre
  \(C^2\geq0\).

R64 n'autorise toujours aucune valeur micrométrique de \(R\), aucune formule
\(m_n=n/R\), et aucune affirmation de stabilité BPS dans le quotient.

## 10. Reproductibilité

Exécuter :

```bash
python3 meta_audit_r64/r64_equivariant_nogo_audit.py
```

La sortie bloquante doit contenir :

```text
UNIFORM_SIGN_IDENTITY: EPSILON_C_EQUALS_MINUS_EPSILON_OMEGA_S
ALL_FOUR_ORIENTIFOLD_BRANCH_CASES: NEGATIVE_OR_ZERO
EXCHANGED_BRANCH_SIGMA_S_IDENTITY: O3O7_ZERO_O5O9_INCOMPATIBLE
GENERAL_C4_ACTIVE_NONNEGATIVE_NOGO: POSITIVE_THREE_PLANE_COROLLARY
BRANE_IMAGE_STABILITY_KK: NOT_COVERED
```

## 11. Sources primaires et positionnement

1. T. W. Grimm, J. Louis, *The effective action of N=1 Calabi–Yau
   orientifolds*, Nucl. Phys. B **699** (2004) 387–426,
   [arXiv:hep-th/0403067](https://arxiv.org/abs/hep-th/0403067). Les tableaux
   des réductions O3/O7 et O5/O9 donnent respectivement les vecteurs de
   \(C_4\) dans \(H^3_+\) et \(H^3_-\).
2. B. van Geemen, A. Sarti, *Nikulin involutions on K3 surfaces*, Math. Z.
   **255** (2007) 731–753,
   [arXiv:math/0602015](https://arxiv.org/abs/math/0602015). Pour une
   involution symplectique non triviale, le réseau anti-invariant est
   \(E_8(-2)\).
3. F. Hassfeld, B. Monnee, T. Weigand, M. Wiesner, *Emergent Strings in Type
   IIB Calabi–Yau Compactifications*,
   [arXiv:2504.01066](https://arxiv.org/abs/2504.01066). Le mécanisme visé
   utilise les tubes au-dessus de classes \(C^2\geq0\) et un argument
   physique de multi-enroulement ; R64 ne transforme pas cet argument de
   stabilité en théorème.

Le noyau algébrique de la preuve est l'indice de Hodge, donc il ne faut pas
présenter R64 comme un nouveau théorème abstrait sur les involutions de K3.
La contribution possible est la formulation uniforme du filtre de parité du
tube et son application certifiée au modèle relatif précis de R63. Une
revendication de nouveauté éditoriale exige encore une comparaison experte
avec la littérature récente sur les obstructions orientifold.

