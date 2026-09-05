# R65 — Préenregistrement du pilote spectral

**Gelé avant calcul :** 5 septembre 2026  
**Configuration exécutable :** `R65_CONFIG.json`

## 1. Question unique

Le pipeline reconnaît-il un paquet de valeurs propres effectivement
unidimensionnel et le distingue-t-il de deux faux positifs : un mode de
Cheeger/tunneling créé par un étranglement, et une contamination par des
excitations transverses ?

R65 ne teste pas la métrique Ricci-plate de DDF, ne calcule pas le spectre
spin-2 et ne produit aucune longueur physique. Toutes les longueurs de ce
pilote sont sans dimension. La valeur historique de 8,2 micromètres n'est ni
une entrée, ni une cible, ni un filtre de sélection.

## 2. Paramètres gelés

On utilise cinq valeurs consécutives

\[
|t|=10^{-1},10^{-2},10^{-3},10^{-4},10^{-5},
\qquad
L(|t|)=6\bigl(1-\log_{10}|t|\bigr),
\]

soit \(L=12,18,24,30,36\). Cette relation sert seulement à ordonner cinq
longueurs pilotes ; elle n'est pas revendiquée comme relation métrique DDF.

Pour chaque modèle, 30 valeurs propres positives sont calculées. La
classification utilise les dix premières, dans leur ordre spectral naturel,
sans retirer ni réassigner un niveau après le calcul. Pour le cercle, elle
utilise les dix premiers **niveaux distincts** et conserve explicitement la
multiplicité deux des modes longitudinaux.

## 3. Contrôles positifs

1. rectangle \([0,L]\times[0,1]\), Neumann–Neumann ;
2. rectangle \([0,L]\times[0,1]\), Dirichlet longitudinal et Neumann
   transverse ;
3. tore rectangle de circonférences \(L\) et 1, avec doublets longitudinaux
   enregistrés à l'avance.

Les spectres continus séparables constituent la vérité analytique. Les deux
discrétisations numériques sont : volumes finis/différences secondes à
mailles centrées, et éléments finis \(P_1\) à matrice de masse cohérente.
Les résolutions sont 12, 24 et 48 cellules par unité transverse.

## 4. Contrôles négatifs

### 4.1 Haltère de Cheeger/tunneling

Sur \([-2,2]\), on étudie

\[
-A(x)^{-1}\frac{d}{dx}\!\left(A(x)\frac{du}{dx}\right),
\]

avec conditions naturelles de Neumann. Les deux caps ont \(A=1\), le col
central a \(A=|t|\), et deux transitions linéaires relient ces régions. Les
résolutions sont 200, 400 et 800. Un petit premier niveau isolé et une énergie
de gradient concentrée dans la région enregistrée \(|x|<0.75\), transitions
comprises, doivent être identifiés comme tunneling, pas comme début d'une
tour KK.

### 4.2 Faux paquet transverse

On reprend le rectangle de Neumann avec largeur transverse \(L/3\). Le
premier mode transverse arrive alors au niveau longitudinal \(n=3\). Même si
les premières valeurs semblent régulières, la présence explicite de labels
transverses parmi les dix premiers doit forcer le rejet.

## 5. Diagnostics fixés avant calcul

- extrapolation de Richardson des dix premiers niveaux sur trois maillages ;
- désaccord entre les deux discrétisations ;
- résidu algébrique relatif
  \(\|Ku-\lambda Mu\|_2/(\|Ku\|_2+|\lambda|\|Mu\|_2)\) ;
- ajustement \(\lambda_n=a(n+\delta)^2+c\), avec \(n=1,\ldots,10\) fixé ;
- ajustement concurrent avec exposant libre \(p\in[0.5,4]\) ;
- dimension de comptage effective tirée de
  \(N(\lambda)\propto\lambda^{d_{\rm eff}/2}\) ;
- longueur de contrôle \(L_{\rm eff}=\pi/\sqrt a\) pour l'intervalle et
  \(L_{\rm eff}=2\pi/\sqrt a\) pour le cercle ;
- labels et multiplicités ;
- ratio du premier seuil transverse au dixième niveau longitudinal ;
- pour l'haltère, \(\lambda_2/\lambda_1\) et fraction d'énergie de gradient
  dans le col.

## 6. Seuils binaires

Un contrôle KK est accepté seulement si, pour les cinq paramètres :

1. variation de Richardson et désaccord des méthodes inférieurs à 5 % ;
2. résidu algébrique inférieur à 10 % ;
3. résidu quadratique inférieur à 10 % et \(1.8\le p\le2.2\) ;
4. \(0.8\le d_{\rm eff}\le1.2\) ;
5. erreur sur la longueur analytique inférieure à 5 % ;
6. gap transverse \(\lambda_{T,1}/\lambda_{L,10}\ge1.25\) ;
7. aucun mode transverse parmi les dix premiers ;
8. multiplicité conforme au type intervalle ou cercle annoncé.

L'haltère est correctement rejeté si au moins trois paramètres donnent
simultanément \(\lambda_2/\lambda_1\ge20\) et une fraction d'énergie du col
au moins égale à 60 %, sans passer le paquet quadratique complet. Le contrôle
transverse est correctement rejeté si au moins trois paramètres violent le
gap et contiennent un mode transverse parmi les dix premiers.

## 7. Porte globale

~~~text
GO_PIPELINE = les trois contrôles positifs sont reconnus avec leur topologie
              et les deux contrôles négatifs sont rejetés pour la raison gelée.
STOP_PIPELINE = toute autre issue.
~~~

Un GO valide uniquement la méthode et autorise R66. Il ne prouve ni une
direction longue dans DDF, ni une tour gravitonique, ni une échelle
micrométrique.

