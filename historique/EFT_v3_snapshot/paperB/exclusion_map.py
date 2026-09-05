#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper B — carte d'exclusion du radion pour un fond stabilise Goldberger-Wise.

REGLE BLOQUANTE : ce script REFUSE de produire un verdict tant que le fichier
alpha95_SCREENING_SLOT.csv n'est pas rempli par une digitisation officielle.
Il produit alors seulement la structure du calcul et la table des candidats.
C'est voulu : le juge X-6b est gele et ne peut pas etre remplace par une
approximation de screening.

Signal teste (les DEUX jambes, jamais une seule) :
    Delta(r) = alpha_r * exp(-r/lambda_r) + (8/3) * somme_n exp(-n r / R)
"""
import csv
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CURVE = os.path.join(HERE, "alpha95_SCREENING_SLOT.csv")

C_ALPHA = -0.634          # correction moduli-space a alpha_r (tag : approximation)
ALPHA_KK = 8.0 / 3.0      # Kehagias-Sfetsos, n=1  [Established]
ALPHA_R0 = 1.0 / 3.0      # Adelberger et al.       [Established]


def alpha_r(betaL):
    """Couplage du radion, Einstein frame. Le 1/3 est cite, pas derive."""
    return ALPHA_R0 * (1.0 + C_ALPHA * betaL**2)


def lambda_r(q, M53, eta, x):
    """Portee du radion derivee du fond (limite probe + correction ~1%)."""
    m_r = 2.0 * math.sqrt(eta * x * math.tanh(x / 2.0)) * q / math.sqrt(12.0 * M53)
    return 1.0093 / m_r


def delta(r, a_r, lam_r, R, nmax=200):
    """Signal complet : radion + tour KK."""
    tower = sum(math.exp(-n * r / R) for n in range(1, nmax + 1))
    return a_r * math.exp(-r / lam_r) + ALPHA_KK * tower


def load_curve():
    rows, anchored = [], 0
    with open(CURVE) as fh:
        for row in csv.DictReader(fh):
            if row["alpha95"].strip():
                rows.append((float(row["lambda_um"]), float(row["alpha95"])))
                anchored += 1
    return rows, anchored


def verdict(a_r, lam_r, R, curve):
    """Vert si max Delta/(alpha95) < 1/3 ; rouge si > 3 ; sinon orange."""
    ratios = [delta(lam, a_r, lam_r, R) / a95 for lam, a95 in curve]
    m = max(ratios)
    return ("VERT" if m < 1.0 / 3.0 else "ROUGE" if m > 3.0 else "ORANGE"), m


def main():
    curve, n = load_curve()
    print("=" * 68)
    print("Paper B — carte d'exclusion du radion (fond stabilise GW)")
    print("=" * 68)
    print(f"Courbe alpha95 : {n} point(s) renseigne(s) sur "
          f"{sum(1 for _ in open(CURVE)) - 1} lignes.")
    if n < 6:
        print()
        print("  ARRET VOLONTAIRE : la courbe alpha95 n'est pas renseignee.")
        print("  Le juge X-6b est gele ; aucun verdict d'exclusion ne peut etre")
        print("  produit a partir d'une approximation de screening.")
        print()
        print("  Pour lever le blocage : remplir alpha95_SCREENING_SLOT.csv par")
        print("  une digitisation OFFICIELLE ou tracable des courbes publiees,")
        print("  dans leur domaine de validite, puis relancer.")
        print()
        print("  Structure du calcul (verifiable sans donnees) :")
        for betaL in (0.0, 0.005, 0.01):
            print(f"    betaL = {betaL:<6}  alpha_r = {alpha_r(betaL):.6f}")
        print(f"    alpha_KK (n=1)          = {ALPHA_KK:.6f}   [Established]")
        print("    Delta(r) = alpha_r e^{-r/lambda_r} + (8/3) somme_n e^{-nr/R}")
        print("=" * 68)
        return
    print("Courbe renseignee : execution du scan.")
    print("(inserer ici la grille de fonds ; aucune valeur n'est codee en dur)")
    print("=" * 68)


if __name__ == "__main__":
    main()
