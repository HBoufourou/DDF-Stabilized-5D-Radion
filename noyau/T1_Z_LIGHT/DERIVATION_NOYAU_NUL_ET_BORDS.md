# Rejeu analytique du noyau nul et des jonctions complètes

Date : 6 septembre 2026. Calcul indépendant pour l'action actuelle, sur un intervalle physique, avec coefficient d'Einstein \(B/2=M_5^3/2\). Ce texte calcule le domaine des solutions. Il ne reprend pas comme preuve les verdicts historiques, et ne calcule pas à lui seul les deux routes présymplectiques.

## 1. Hypothèses et ce que « nul » signifie

Le fond est \(ds^2=e^{2A(y)}\eta_{\mu\nu}dx^\mu dx^\nu+dy^2\), \(\sigma=\sigma_0(y)\), sur \([0,L]\). La signature est \((-++++)\). Poser \(a=A'\), \(q=\sigma_0'\), \(B=M_5^3>0\), et \(V=\Lambda_5+\mu^2\sigma_0^2/2\). Les identités du fond sont

\[
a'=-q^2/(3B),\qquad 6Ba^2=q^2/2-V,\qquad q'=V_\sigma-4aq.
\]

On suppose un fond lisse, \(q\ne0\) partout, des branes contenant seulement les potentiels isotropes \(U_i\), et des fluctuations autour du vide matériel. Les cinétiques de brane et les contraintes de bord imposées artificiellement en plus de l'action sont absentes.

On étudie \(\varphi(x)=e^{ip\cdot x}\), avec \(p^2=0\) mais \(p_\mu\ne0\). Aucun inverse de \(p^2\) n'est utilisé. Ce secteur contient le graviton sans masse : l'expression « tout Z-light est vide » serait fausse.

## 2. Complétude dans une vraie base nulle

La paramétrisation \(F,G,s,\widehat E,B_5\) présentée plus bas ne suffit pas, à elle seule, à démontrer la complétude : dans une base nulle on peut former d'autres tenseurs avec le vecteur nul conjugué. Voici leur élimination directe.

On peut choisir des coordonnées gaussiennes normales dans le bulk, en laissant momentanément les branes se déplacer : \(h_{55}=h_{5\mu}=0\). Les équations différentielles des paramètres de difféomorphisme donnant cette jauge sont régulières sur un intervalle fini. Elles ne fixent pas les déplacements \(Z_i(x)\) des branes. Écrire \(g_{\mu\nu}=e^{2A}(\eta_{\mu\nu}+h_{\mu\nu}\varphi)\).

Choisir \(p_\mu=(k,0,0,0)\), \(k\ne0\), dans les coordonnées \((+,-,1,2)\), avec \(\eta_{+-}=-1\), \(\eta_{ab}=\delta_{ab}\). Définir \(t=(h_{11}+h_{22})/2\). Le Ricci 4D linéaire est calculé sans projection :

\[
R^{(4,1)}_{\mu\nu}=\frac12\left[p^2h_{\mu\nu}+p_\mu p_\nu h-p_\mu p^\rho h_{\rho\nu}-p_\nu p^\rho h_{\rho\mu}\right].
\]

En particulier,

\[
R_{--}^{(4,1)}=R_{-a}^{(4,1)}=R_{ab}^{(4,1)}=0,\quad
R_{+-}^{(4,1)}=k^2h_{--}/2,\quad R_{+a}^{(4,1)}=k^2h_{-a}/2,\quad R_{++}^{(4,1)}=k^2t.
\]

Les équations radiales d'Einstein, obtenues depuis la métrique gaussienne normale, sont

\[
\frac B2\left(\partial^\nu h'_{\mu\nu}-\partial_\mu h'\right)=q\partial_\mu s,
\]
\[
h''_{\mu\nu}+4a h'_{\mu\nu}+a\eta_{\mu\nu}h'
-2e^{-2A}R^{(4,1)}_{\mu\nu}
=-\frac{4V_\sigma s}{3B}\eta_{\mu\nu}.
\]

Les composantes \((-5)\) et \((a5)\) donnent \(h'_{--}=h'_{-a}=0\). Les combinaisons \((+-)+(11+22)/2\) et \((+a)\) donnent alors

\[
[e^{4A}(h_{+-}+t)']'=k^2e^{2A}h_{--},\qquad
(e^{4A}h'_{+a})'=k^2e^{2A}h_{-a}.
\]

Le déplacement d'une brane apporte à Israel une Hessienne \(\partial_\mu\partial_\nu Z_i\). Dans cette base, elle possède seulement une composante \((++)\). La source \(U_i\) est isotrope. Les jonctions des deux combinaisons précédentes imposent donc

\[
(h_{+-}+t)'_i=0,\qquad h'_{+a,i}=0.
\]

L'intégration sur tout l'intervalle donne \(k^2I_Lh_{--}=k^2I_Lh_{-a}=0\), où \(I_L=\int_0^Le^{2A}dy>0\). Ainsi \(h_{--}=h_{-a}=0\). Les deux autres combinaisons sont constantes en \(y\) et s'enlèvent par les difféomorphismes tangentiels résiduels indépendants de \(y\), de paramètres \(\xi_-\) et \(\xi_a\). Ceci requiert \(k\ne0\), jamais \(p^2\ne0\).

Il reste

\[
h_{ab}=2F\delta_{ab}+h^{\rm TT}_{ab},\quad h_{+-}=-2F,\quad h_{++}\ \text{longitudinal},
\]

où \(h^{\rm TT}_{ab}\) est une matrice symétrique 2×2 de trace nulle : exactement les deux polarisations du graviton. Elles satisfont \((e^{4A}h^{{\rm TT}\prime}_{ab})'=0\) et \(h^{{\rm TT}\prime}_{ab}|_i=0\), donc elles sont constantes en \(y\). Leur cinétique vient de \(B I_L>0\). Elles ne peuvent annuler la jonction \((++)\) du candidat scalaire : ce sont des polarisations distinctes.

Ce raisonnement inclut et élimine les composantes absentes de la paramétrisation scalaire habituelle. Les degrés de liberté nuls restants se répartissent donc en deux polarisations gravitationnelles et le bloc scalaire/longitudinal traité ci-dessous.

## 3. Bloc scalaire/longitudinal régulier

Retourner à une jauge générale pour ce bloc :

\[
g_{\mu\nu}=e^{2A}\big[(1+2F\varphi)\eta_{\mu\nu}+2\widehat E\partial_\mu\partial_\nu\varphi\big],\quad
g_{\mu5}=B_5\partial_\mu\varphi,\quad g_{55}=1+2G\varphi,\quad
\sigma=\sigma_0+s\varphi.
\]

\(B_5\) est un champ de décalage, distinct du coefficient constant \(B=M_5^3\). Poser \(\chi=B_5-e^{2A}\widehat E'\).

Avec la convention \(\delta_\xi g=\mathcal L_\xi g\), \(\xi^5=\zeta\varphi\), \(\xi_\mu=\lambda\partial_\mu\varphi\),

\[
\delta F=a\zeta,\quad\delta G=\zeta',\quad\delta s=q\zeta,\quad
\delta\widehat E=e^{-2A}\lambda,\quad
\delta B_5=\zeta+\lambda'-2a\lambda,\quad \delta\chi=\zeta.
\]

La composante \((\mu5)\), dont \(p_\mu\) est non nul, impose

\[
C_1:=3B(F'-aG)+qs=0.
\]

La composante \((55)\) impose

\[
12Ba(F'-aG)=q(s'-qG)-V_\sigma s.
\]

Éliminer \(F'-aG\) entre ces deux égalités, puis utiliser \(V_\sigma-4aq=q'\), donne

\[
q(s'-qG)-q's=0.
\]

Puisque \(q\ne0\), définir \(z=s/q\). On obtient \(G=z'\). La contrainte devient \(F'=az'+a'z=(az)'\), donc

\[
F=az-c_1,\qquad G=z',\qquad s=qz.
\]

Les équations de trace et du scalaire sont alors satisfaites exactement par les équations du fond. La composante \(\partial_\mu\partial_\nu\varphi\), qui n'est pas nulle sur le cône de lumière, donne

\[
\chi'+2a\chi=2F+G.
\]

Une intégration fournit la solution générale

\[
\boxed{\chi=z-(2c_1I+C)e^{-2A}},\qquad I(y)=\int_0^ye^{2A(u)}du.
\]

\(\widehat E\) reste un choix tangentiel de jauge. \(c_1,C\) sont les deux constantes à tester par les jonctions. Cette complétude vient de deux équations indépendantes et d'une intégration du premier ordre, et non d'une vérification d'un ansatz particulier. Les identités différentielles et les composants nuls sont vérifiés exactement dans `null_boundary_checks.py`.

## 4. Jonctions et complétion par les positions de bord

### 4.1. Hessienne explicite des potentiels quadratiques

Pour éviter de confondre le facteur de chaîne avec \(a=A'\), noter \(\Omega_i=e^{A_i}\). En jauge de branes fixes, prendre le chemin de variation \(\gamma_{\mu\nu}=\Omega_i^2(\eta_{\mu\nu}+\varepsilon h_{\mu\nu})\), \(\sigma=\sigma_i+\varepsilon\delta\sigma_i\), avec \(h=\eta^{\mu\nu}h_{\mu\nu}\). L'expansion directe du déterminant donne

\[
\sqrt{-\gamma}=\Omega_i^4\left[1+\frac{\varepsilon h}{2}
+\varepsilon^2\left(\frac{h^2}{8}-\frac{h_{\mu\nu}h^{\mu\nu}}4\right)\right]+O(\varepsilon^3).
\]

Le coefficient de \(\varepsilon^2\) dans la densité \(-\sqrt{-\gamma}U_i(\sigma)\) est donc

\[
\boxed{-\Omega_i^4\left[\frac12U_i''(\delta\sigma_i)^2
+\frac12hU_i'\delta\sigma_i
+U_i\left(\frac{h^2}{8}-\frac{h_{\mu\nu}h^{\mu\nu}}4\right)\right].}
\]

Les \(U_i,U_i',U_i''\) sont évalués sur le fond ; \(U_i\) est la valeur **totale** du potentiel et non sa seule constante \(\tau_i\). Ce coefficient est la moitié de la seconde variation le long du chemin déclaré. Pour \(h_{\mu\nu}=2F_i\eta_{\mu\nu}\varphi\), \(\delta\sigma_i=s_i\varphi\), on trouve \(h=8F_i\varphi\), \(h_{\mu\nu}h^{\mu\nu}=16F_i^2\varphi^2\), puis

\[
\mathcal L^{(2)}_{U_i}
=-e^{4A_i}\left[\lambda_i s_i^2+4F_iU_i's_i+4U_iF_i^2\right]\varphi^2,
\qquad U_i''=2\lambda_i.
\]

Le contrôle élémentaire \(\sqrt{-\det[(1+2\varepsilon F\varphi)\eta]}=(1+2\varepsilon F\varphi)^2\) confirme les coefficients 4 des termes métriques. Pour X₁, \(F=-1,s=0\), ce morceau vaut exactement \(-4e^{4A_i}U_i\varphi^2\). La raideur intervient dans l'Hessienne par \(U_i''\) et dans la condition scalaire linéarisée, mais aucun terme \(\lambda_i s_i^2\) ne subsiste sur ce candidat. Dans cette jauge, cette densité ne contient aucune dérivée tangentielle de \(F\) ou \(s\) et ne fournit donc pas une cinétique autonome de X₁. Son signe isolé ne décide pas le signe d'une norme.

La Hessienne complète est celle d'Einstein–Hilbert, du scalaire, de GHY avec coefficient \(B\), et de ces deux densités de bord. Sur un fond satisfaisant les jonctions, ses conditions naturelles sont exactement les **jonctions originales complètes différentiées**, testées par des variations tensorielles indépendantes. Le calcul des jonctions ci-dessous est ainsi le test du domaine de cette Hessienne complète ; il ne remplace pas celle-ci par la seule restriction \(F,s\).

Sur le cône nul, un résidu \(\mathcal J_{\mu\nu}\propto p_\mu p_\nu\) échappe aux variations métriques réduites de structures \(\eta_{\mu\nu}\) et \(p_\mu p_\nu\). La variation conjuguée \(\delta\gamma^{\mu\nu}\propto n^\mu n^\nu\), où \(p\cdot n\ne0\), donne au contraire une contraction proportionnelle à \((p\cdot n)^2\ne0\). L'omettre avant de varier fait perdre une équation naturelle de la forme quadratique ; cela ne démontre pas que cette équation est satisfaite.

Avec des embeddings mobiles, le pullback de \(\gamma\) contient lui-même des dérivées des positions de bord. Leurs contributions, ainsi que celles de GHY et du bulk, doivent être conservées ensemble ; la formule en jauge fixe ci-dessus n'autorise pas à les ignorer. La complétion qui suit et le calcul compagnon `PRESYMPLECTIQUE_ADM_ET_BORDS.md` appliquent cette distinction.

### 4.2. Positions de bord et jonctions complètes

Écrire l'embedding perturbé d'une brane \(X_i^A=(x^\mu+X_i^\mu(x),y_i+Z_i(x))\). La transformation \(\delta_\xi X_i^A=-\xi^A|_i\) compense le changement de coordonnées du bulk. Les combinaisons \(s_i+q_iZ_i\) et \(\chi_i+Z_i\) sont invariantes sous les déplacements normaux.

Les déplacements tangentiels \(X_i^\mu\) complètent de la même manière les métriques induites :

\[
\delta\gamma_{\mu\nu}^{\rm pullback}/e^{2A_i}
=h_{\mu\nu,i}+2a_iZ_i\eta_{\mu\nu}
+2\partial_{(\mu}X_{i\nu)}.
\]

La notation « transverse/longitudinal » pour \(X_i^\mu\) ne doit pas utiliser un projecteur \(1/p^2\). Elle se définit ici par les composantes dans la base \((p,n,e_1,e_2)\), ou simplement par le vecteur \(X_i^\mu\) complet. Les reparamétrisations tangentielles des branes sont aussi des redondances. Aucun nouveau terme cinétique n'a été ajouté à l'action par cette complétion.

La géométrie donne, pour la composante anisotrope de la courbure extrinsèque,

\[
\delta K^{\rm TF}_{\mu\nu}\big|_{\partial\partial\varphi}
=-\eta_i(\chi_i+Z_i)\partial_\mu\partial_\nu\varphi.
\]

Le stress de brane est isotrope, même si \(U_i''\ne0\). Israel impose donc **une condition à chacun des deux bords** :

\[
\boxed{\chi_i+Z_i=0.}
\]

La trace, après emploi de \(U_i=3\eta_iBa_i\) et \(U_i'=-\eta_iq_i\), est

\[
3B(F'-aG+a'Z_i)+q(s+qZ_i)
=C_1+(3Ba'+q^2)Z_i=C_1=0.
\]

Enfin \(n\cdot\partial\sigma=-U_i'\), évaluée sur la brane déplacée, donne

\[
s'_i-q_iG_i+\eta_iU_i''s_i
+(q'_i+\eta_iU_i''q_i)Z_i=0.
\]

Sur le noyau de bulk, poser \(\theta_i=z_i+Z_i\). Pour les potentiels actuels \(U_i=\tau_i+\lambda_i(\sigma-v_i)^2\),

\[
\boxed{q_iD_i\theta_i=0,\quad D_i=W_i+2\eta_i\lambda_i,\quad W_i=q'_i/q_i.}
\]

Le lieu de dégénérescence est \(D_i=0\), et non \(q'_i=0\) pris isolément. La constante nue \(\tau_i\) et les valeurs \(v_i\) interviennent par les jonctions du fond ; aucun signe de tension n'est ignoré.

## 5. Résolution du domaine et quotient

Pour \(D_0D_L\ne0\), la jonction scalaire impose \(\theta_0=\theta_L=0\). Les deux jonctions sans trace deviennent

\[
C=0,\qquad 2c_1I_L+C=0.
\]

Comme \(I_L>0\), \(c_1=C=0\). Le noyau restant est

\[
F=az,\quad G=z',\quad s=qz,\quad\chi=z,\quad Z_i=-z_i,
\]

avec le champ tangentiel \(\widehat E\) et les reparamétrisations tangentielles correspondantes. Il s'agit exactement d'un difféomorphisme du fond, accompagné de la transformation de ses embeddings. Le quotient de jauge normal et tangentiel annule ce bloc. En jauge de branes fixes, \(Z_i=0\), on a \(z_i=0\) et le même résultat par les seules transformations préservant les bords.

Le déterminant du système de bord sur \((c_1,C,\theta_0,\theta_L)\) vaut

\[
-\frac{2I_Lq_0q_LD_0D_L}{e^{2A_0}e^{2A_L}},
\]

qui rend le domaine non dégénéré explicite. Si un \(D_i\) s'annule, ce raisonnement ne donne pas un verdict par continuité : le rang diminue réellement. La limite infiniment raide doit aussi être déclarée comme telle ; sa condition est \(s_i+q_iZ_i=0\), donc \(\theta_i=0\), et elle donne la même exclusion sous \(q_i\ne0\).

## 6. Le candidat X₁, explicitement

Le candidat historique correspond à \(c_1=1,C=0,z=0\), avec \(F=-1,G=s=0\) et \(\chi=-2Ie^{-2A}\). Il satisfait le bulk. En branes fixes,

\[
\chi_0=0,\qquad \chi_L=-2I_Le^{-2A_L}\ne0.
\]

Le résidu tensoriel droit est donc

\[
\delta K^{\rm TF}_{\mu\nu,L}
=2\eta_LI_Le^{-2A_L}\partial_\mu\partial_\nu\varphi\ne0.
\]

Il ne disparaît pas parce que sa trace et sa double divergence sont nulles. Si l'on déplace la brane droite pour annuler ce résidu, la condition scalaire donne \(q_LD_LZ_L\ne0\) dans le domaine générique. Les bords quadratiques n'autorisent donc pas une réparation par déplacement de brane.

Une contribution « TT » proportionnelle à \(p_\mu p_\nu\varphi\) est déjà contenue dans \(\widehat E\). La compter une deuxième fois ne crée pas une nouvelle constante libre permettant de satisfaire les deux jonctions. Les véritables polarisations transverses \(h^{\rm TT}_{ab}\), traitées en section 2, ne portent pas cette structure.

Une forme quadratique évaluée sur X₁ hors domaine peut être calculée comme diagnostic, mais elle ne devient pas une norme d'état physique. Le calcul compagnon `PRESYMPLECTIQUE_ADM_ET_BORDS.md`, complété par `t1_integrated_norms.py` et sa sortie, reproduit le nombre \(N[X_1]=-3B I_L\) par les deux routes déclarées pour l'action actuelle. La reproduction de ce nombre ne certifie pas un ancien journal absent et ne rend pas X₁ admissible : le résidu d'Israel reste non nul.

## 7. Pourquoi la jauge de l'article n'est pas une hypothèse salvatrice

Le système spectral de l'article est écrit avec \(\widehat E=B_5=0\), d'où \(G=-2F\) par la composante \(\partial_\mu\partial_\nu\) du bulk. Sur le domaine complet de branes fixes, on peut choisir \(\xi^5=-\chi\), puis une transformation tangentielle annulant \(\widehat E\). Cette transformation normale préserve les bords précisément parce que \(\chi_i=0\). Le passage à la jauge de l'article est donc justifié après la vérification du domaine.

Pour X₁, \(-\chi_L=2I_Le^{-2A_L}\ne0\) : la transformation nécessaire ne préserve pas la brane droite. On ne peut pas invoquer \(G=-2F\) comme motif initial pour rejeter X₁. Le motif indépendant est la jonction d'Israel complète, et la jauge spectrale devient ensuite régulière sur les configurations admissibles.

## 8. Domaine principal du modèle actuel

Sur la branche plate symétrique actuelle, au centre \(A'=\sigma_0=0\) et \(q_c=\sqrt{2\Lambda_5}>0\). À droite du centre, tant que la solution reste lisse, \(a'<0\), \(a<0\), \(\sigma_0>0\), \(q>0\), et

\[
q'=\mu^2\sigma_0-4aq>0.
\]

La réflexion donne \(W_0=-W_L<0\). Avec \(\lambda_i>0\),

\[
\eta_iW_i+2\lambda_i>0
\]

aux deux bords. La branche principale entre donc dans le domaine non dégénéré du présent calcul et dans le domaine positif de l'identité spectrale massive. Les exemples \(D_i=0\) sont des changements de domaine à étudier séparément, et non des limites silencieuses des valeurs génériques.

Le champ sombre \(\Phi\), s'il est inclus dans la troncature courante autour de \(\Phi=0\), est découplé à l'ordre linéaire. Pour \(m_\Phi^2>0\), son problème nul satisfait \(-(e^{4A}u')'+m_\Phi^2e^{4A}u=0\), avec Neumann aux deux bords. L'intégration positive impose \(u=0\). Si l'on change de modèle en posant \(m_\Phi=0\), le mode constant complexe existe avec une cinétique positive ; il faut alors le compter.

## 9. Verdict limité de ce calcul

**X₁ est exclu par les jonctions complètes. Le quotient du bloc scalaire/longitudinal sur le cône nul est trivial dans le domaine déclaré. Le cône nul complet conserve deux polarisations du graviton sans masse à cinétique positive.**

Ce résultat ferme la question du domaine qui manque au seul problème scalaire massif. Pour imprimer un verdict T1 rassemblant les demandes de l'audit, il faut joindre les calculs présymplectiques covariant et ADM sur cet espace admissible et avec les mêmes embeddings. Le présent calcul ne justifie pas un verdict sur les branes avec cinétiques ajoutées, les fonds courbes, les points \(q=0\) ou \(D_i=0\), les configurations statiques \(p_\mu=0\), ni la viabilité complète de DDF.

Les fichiers historiques contiennent une rétraction de RED suivie d'une revendication de fermeture générique. Cela corrige la chronologie du dossier, mais ne remplace pas le rejeu effectué ici sur les potentiels quadratiques actuels.

Contrôle exécuté : `null_boundary_checks.py` donne 29 vérifications exactes réussies, dont 28 identités nulles en arithmétique rationnelle et le rang générique quatre du système de bord. Il utilise seulement la bibliothèque standard Python. Les trois premiers contrôles vérifient l'arithmétique interne ; les autres vérifient les composants du Ricci nul, les identités de bulk, les jonctions complétées et le déterminant. La preuve d'intégration et de quotient reste le raisonnement explicite ci-dessus, et n'est pas remplacée par le nombre de contrôles.
