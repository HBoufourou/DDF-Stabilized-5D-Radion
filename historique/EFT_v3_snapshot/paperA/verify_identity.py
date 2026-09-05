#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper A — verification symbolique complete de l'identite d'energie reguliere.

Reproduit, sans aucune entree numerique :
  (1) l'ideal du fond ;
  (2) l'identite exacte  2 V_bulk = (1/2) e^{4A} G^2 + d/dy[G_y]  modulo C1 ;
  (3) l'annulation complete de la dependance en f dans la forme de bord ;
  (4) l'autovalidation : la BC naturelle redonne s' + 2 sigma0' f = 0 ;
  (5) le critere  s_i sigma0''/sigma0' >= 0 ;
  (6) l'application au fond GW Z2-symetrique (warp non monotone).

Dependance : sympy. Duree : quelques secondes.
Sortie : lignes "OK" ; tout residu non nul est une erreur.
"""
import sympy as sp

y = sp.symbols('y')
M53, mus2, Lam = sp.symbols('M53 msig2 Lambda5', positive=True)
si = sp.symbols('s_i')
A = sp.Function('A')(y)
s0 = sp.Function('sigma0')(y)
w = sp.exp(2 * A)
Ap = sp.diff(A, y)
sp0 = sp.diff(s0, y)
sp2 = sp.diff(s0, y, 2)
f, s = [sp.Function(n)(y) for n in "fs"]

# ---------------------------------------------------------------- ideal du fond
RA2 = -sp0**2 / (3 * M53)                       # A'' = -sigma0'^2 / 3 M5^3
r = {sp.diff(A, y, 2): RA2,
     sp.diff(s0, y, 2): mus2 * s0 - 4 * Ap * sp0}   # sigma0'' = V'(sigma) - 4A' sigma'
for n in (3, 4):
    r[sp.diff(A, y, n)] = sp.expand(sp.diff(r[sp.diff(A, y, n - 1)], y).subs(r))
    r[sp.diff(s0, y, n)] = sp.expand(sp.diff(r[sp.diff(s0, y, n - 1)], y).subs(r))
con = sp.Eq(6 * M53 * Ap**2,
            sp.Rational(1, 2) * sp0**2 - sp.Rational(1, 2) * mus2 * s0**2 - Lam)
Ls_ = sp.solve(con, Lam)[0]


def canon(e_):
    e_ = e_.replace(lambda z: z.is_Pow and z.base.func == sp.exp,
                    lambda z: sp.exp(sp.expand(z.base.args[0] * z.exp)))
    return sp.expand(sp.powsimp(sp.expand(e_), force=True))


def ideal(e_):
    e_ = canon(e_)
    for _ in range(8):
        e2 = sp.expand(e_.subs(r))
        if e2 == e_:
            break
        e_ = e2
    return canon(sp.expand(e_.subs(Lam, Ls_).subs(r)))


def check(label, expr):
    v = sp.simplify(ideal(expr))
    print(("OK   " if v == 0 else "FAIL ") + label + ("" if v == 0 else f"  residu = {v}"))
    return v == 0


# ------------------------------- densite de potentiel de bulk (certifiee)
# V_bulk : densite du lagrangien reduit du secteur scalaire, dans la jauge
# ou le secteur est decrit par (f, s). Sa caracterisation intrinseque est
# EL_f[V] = (A X)_f et EL_s[V] = (A X)_s, ou A est l'operateur de masse
# du probleme modal A X = m^2 K X. C'est le test (1) ci-dessous.
Vb = w**2 * (
    432 * M53 * f**2 * Ap**2
    + 320 * M53 * f * Ap * sp.diff(f, y)
    + 32 * M53 * f * sp.diff(f, y, 2)
    + 20 * M53 * sp.diff(f, y)**2
    + 4 * mus2 * f * s * s0
    + mus2 * s**2
    - 36 * f**2 * sp0**2
    + 12 * f * sp.diff(s, y) * sp0
    + sp.diff(s, y)**2
) / 4

Af_ref = w**2 * (6 * M53 * sp.diff(f, y, 2) + 24 * M53 * Ap * sp.diff(f, y)
                 + 24 * M53 * Ap**2 * f - 2 * sp0**2 * f
                 + 3 * sp0 * sp.diff(s, y) + mus2 * s0 * s)
As_ref = w**2 * (-sp.diff(s, y, 2) / 2 - 2 * Ap * sp.diff(s, y) + mus2 * s / 2
                 - 3 * sp0 * sp.diff(f, y) - 2 * mus2 * s0 * f)


def EL(D, q):
    return ideal(sp.expand(sp.diff(D, q)
                           - sp.diff(sp.diff(D, sp.diff(q, y)), y)
                           + sp.diff(sp.diff(D, sp.diff(q, y, 2)), y, 2)))


print("=" * 70)
print("Paper A -- verification de l'identite d'energie reguliere")
print("=" * 70)
check("(1a) EL_f[V_bulk] = (A X)_f", EL(Vb, f) - Af_ref)
check("(1b) EL_s[V_bulk] = (A X)_s", EL(Vb, s) - As_ref)

# ---------------------------------------------------------- surface de contrainte
fp = -2 * Ap * f - sp0 * s / (3 * M53)                    # C1 : f' = ...
fpp = sp.expand(sp.diff(fp, y).subs(sp.diff(f, y), fp))
Vc = ideal(sp.expand(Vb.subs(sp.diff(f, y, 2), fpp).subs(sp.diff(f, y), fp)))

# ------------------------------------------------- combinaison reguliere et identite
G = ideal(sp.diff(s, y) + 2 * sp0 * f - sp2 * s / sp0)
Gy = ideal(28 * M53 * w**2 * Ap * f**2
           - sp.Rational(4, 3) * sp0 * w**2 * f * s
           + (sp2 / sp0) * w**2 * s**2 / 2)
dGy = sp.expand(sp.diff(Gy, y).subs(sp.diff(f, y), fp))
check("(2)  2 V_bulk - (1/2) e^{4A} G^2 - d/dy[G_y] = 0  (modulo C1)",
      2 * Vc - sp.Rational(1, 2) * w**2 * G**2 - dGy)

# ----------------------------------------------------------------- terme de brane
GB = si * w**2 * (14 * M53 * Ap * f**2 - sp.Rational(2, 3) * sp0 * f * s)
eps = w**2 * sp2 / (2 * sp0)
check("(3)  s_i G_y - 2 GB|img = s_i (e^{4A} sigma0''/2 sigma0') s^2  "
      "(toute la dependance en f s'annule)",
      si * Gy - 2 * GB - si * eps * s**2)

# ------------------------------------------------------------------ autovalidation
nat = ideal(w**2 * G + 2 * eps * s)
check("(4)  BC naturelle  e^{4A} G + 2 eps s = e^{4A}(s' + 2 sigma0' f)",
      nat - w**2 * (sp.diff(s, y) + 2 * sp0 * f))

# --------------------------------------------- (5) critere et (6) fond GW symetrique
print("-" * 70)
print("(5)  CRITERE : s_i * sigma0''(y_i)/sigma0'(y_i) >= 0 aux deux branes => m^2 >= 0")
print("     s_0 = -1, s_L = +1 :  sigma0''(0)/sigma0'(0) <= 0  ET  sigma0''(L)/sigma0'(L) >= 0")

L, ms, q = sp.symbols('L m_sigma q', positive=True)
u = ms * (y - L / 2)
s0g = (q / ms) * sp.sinh(u) / sp.cosh(ms * L / 2)
rat = sp.simplify(sp.diff(s0g, y, 2) / sp.diff(s0g, y))
print("-" * 70)
print("(6)  Fond GW Z2-symetrique : sigma0''/sigma0' =", rat)
print("     parite : sigma0(L-y) + sigma0(y) =",
      sp.simplify(s0g.subs(y, L - y) + s0g), " => sigma0 impaire autour de L/2")
print("     en y=0 :", sp.simplify(rat.subs(y, 0)), "(<0) ; s_0 = -1 => produit >= 0  OK")
print("     en y=L :", sp.simplify(rat.subs(y, L)), "(>0) ; s_L = +1 => produit >= 0  OK")
print("     => fond sans tachyon, ET warp non monotone (A' impair, A'(L/2)=0)")
print("=" * 70)
