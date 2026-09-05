# Test des trois voies pour le micron — 05/09/2026 (exploratoire, nouveau modele, pas un certificat)

## Voie III — deplacer le micron vers lambda_r, constitution v1 intacte (betaL <= 0.143)
lambda_r >= 4.4 L a betaL = 0.143 ; ancre experimentale : alpha95 = 1 a 38.6 um (Lee 2020), plus lache en deca.

| R* (um) | L (um) | lambda_r min (um) | radion vs ancre | tour KK a 38.6 um |
|---|---|---|---|---|
| 0.056 | 0.2 | 1 | VERT (ancre) | 1.2e-299 |
| 0.23 | 0.7 | 3 | VERT (ancre) | 3.5e-73 |
| 0.5 | 1.6 | 7 | VERT (ancre) | 7.9e-34 |
| 1.0 | 3.1 | 14 | VERT (ancre) | 4.6e-17 |
| 2.0 | 6.3 | 28 | VERT (ancre) | 1.1e-08 |
| 2.8 | 8.8 | 39 | ORANGE | 2.7e-06 |
| 4.0 | 12.6 | 55 | ORANGE | 1.7e-04 |
| 8.2 | 25.8 | 113 | ROUGE | 2.4e-02 |

=> sur la seule jambe radion, a l'ancre, R* <= 2.8 um passe DANS la constitution v1. La carte gelee donnait vert <= 0.056 um :
   ecart x50 en R*, du a (i) la contrainte de linearite < 1% (betaL bien plus petit), (ii) la marge x3, (iii) la courbe de screening.
   A RESOUDRE par la digitisation + relance de la carte. [Candidate]

## Voie II — ecrantage du radion (v1 intacte, R* = 8.2 um => lambda_r >= 115 um)
Il faut alpha_r < alpha95(115 um) << 1 : suppression du couplage d'un facteur >~ 10 (valeur exacte : digitisation).
Nouveau secteur (cameleon/symmetron ou couplage supprime) ; les memes balances de torsion contraignent les cameleons.
Aucun test mecanique possible sans specifier le secteur. [Open, nouveau modele, gates propres]

## Voie I — stabilisation forte (nouveau modele R9), fond couple resolu numeriquement
Voir table ci-dessus dans le log : betaL 0.53-0.90 => fond existe, sigma0' > 0, T2 = +2.4..+3.6 aux deux branes (marge croissante),
backreaction 5-11 %, m_r/m_KK = 0.22-0.31 (formule moduli-space), lambda_r = 26-37 um a R* = 8.2 um => VERT a l'ancre.

EFT : sigma0/M5^{3/2} ~ q/(m_sigma M5^{3/2}) = sqrt(12) betaL/x  (L=1, M5^3=1)
   betaL = 0.143 : sigma0/M5^(3/2) ~ 0.25
   betaL = 0.390 : sigma0/M5^(3/2) ~ 0.68
   betaL = 0.530 : sigma0/M5^(3/2) ~ 0.92
   betaL = 0.700 : sigma0/M5^(3/2) ~ 1.21
   betaL = 0.900 : sigma0/M5^(3/2) ~ 1.56
=> a betaL ~ 0.5-0.9 le scalaire atteint 0.9-1.6 M5^{3/2} : PORTE EFT a argumenter explicitement (backreaction exacte a la
   DeWolfe-Freedman-Gubser-Karch), pas un kill. Le 'plafond structurel' pi/8 de v1 n'est pas une limite physique : le fond existe au-dela.

## Classement
1. VOIE I  — la seule qui garde R* = 8.2 um LUI-MEME. Existe, carte OK, T2 vert, backreaction moderee. Gates : m_r spectral reel,
             EFT a sigma0 ~ M5^{3/2}, digitisation. Nouveau modele R9.
2. VOIE III — certaine, sans physique nouvelle ; et elle garde peut-etre deja R* ~ 1-3 um dans v1 (a confirmer).
3. VOIE II  — la plus faible : secteur nouveau + suppression x10+ + contraintes propres.
