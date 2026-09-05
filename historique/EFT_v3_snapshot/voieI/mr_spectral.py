#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Voie I — masse spectrale du radion sur le fond couple backreacte (nouveau modele, branche forte).
Reproduit la table de VOIE_I_SPECTRAL.md. Numerique declare, pas un certificat.

Pipeline :
  1. fond couple Z2-symetrique par tir (A''=-s'^2/3, s''=mu^2 s-4A's', s'(0)=s'(1)=q, s(1/2)=0, A'(1/2)=0)
  2. equation master certifiee  Q''+(4A'-2A''/A')Q'+[m^2 e^{-2A}-V_Q]Q=0
  3. BC a parametre spectral  (m^2+nu_i)Q' = nu_i W_i Q
  4. point singulier regulier y=1/2 : tir BILATERAL + serie de Frobenius exacte (u^9, symetrie forcee)
Controles : F(m^2->0) ~ 0 (zero-mode spurieux du master, exclu physiquement par T1) ; accord moduli a petit betaL.
"""
import numpy as np, sympy as sp, warnings, sys
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve, brentq
warnings.filterwarnings("ignore")
x = 2.0; mu = x; NORD = 9
def rhs_bg(y, w):
    A, Ap, s, sp_ = w; return [Ap, -sp_**2/3.0, sp_, mu**2*s - 4*Ap*sp_]
def shoot_bg(p, q):
    s0, Lam = p; arg = (q**2/2 - mu**2*s0**2/2 - Lam)/6.0
    if arg < 0: return [1e3, 1e3]
    sol = solve_ivp(rhs_bg, [0, 0.5], [0.0, np.sqrt(arg), s0, q], rtol=1e-12, atol=1e-14)
    A, Ap, s, sp_ = sol.y[:, -1]; return [s, Ap]
def background(betaL):
    q = betaL*np.sqrt(12.0); eta0 = 1/np.cosh(x/2)**2
    p = fsolve(shoot_bg, [-(q/mu)*np.tanh(x/2), 0.999*eta0*q**2/2], args=(q,), xtol=1e-14); s0, Lam = p
    arg = (q**2/2 - mu**2*s0**2/2 - Lam)/6.0
    return solve_ivp(rhs_bg, [0, 1.0], [0.0, np.sqrt(arg), s0, q], rtol=1e-12, atol=1e-14, dense_output=True), q, Lam
u = sp.symbols('u'); A1, s0s, s1s = sp.symbols('A1 s0 s1')
def D(e): return sp.expand(sp.diff(e, A1)*(-s1s**2/3) + sp.diff(e, s0s)*s1s + sp.diff(e, s1s)*(mu**2*s0s - 4*A1*s1s))
Ak = [sp.Symbol('A00'), A1, -s1s**2/3]; sk = [s0s, s1s, mu**2*s0s - 4*A1*s1s]
for k in range(3, NORD+3): Ak.append(D(Ak[-1])); sk.append(D(sk[-1]))
def frob_series(bg):
    A0, Ap0, s0v, sp0 = bg.sol(0.5)
    sub = {sp.Symbol('A00'): A0, A1: 0.0, s0s: 0.0, s1s: sp0}       # symetrie exacte forcee
    Akn = [float(Ak[k].subs(sub)) for k in range(NORD+3)]; skn = [float(sk[k].subs(sub)) for k in range(NORD+3)]
    for k in range(NORD+3):
        if k % 2 == 1: Akn[k] = 0.0
        if k % 2 == 0: skn[k] = 0.0
    Af = sum(Akn[k]*u**k/sp.factorial(k) for k in range(NORD+3)); sf = sum(skn[k]*u**k/sp.factorial(k) for k in range(NORD+3))
    Ap = sp.diff(Af, u); App = sp.diff(Af, u, 2); spf = sp.diff(sf, u)
    Pt = sp.expand(sp.series(4*Ap - 2*App/Ap + 2/u, u, 0, NORD+1).removeO())
    R0 = sp.expand(sp.series(-(mu**2 + 4*App + 2*mu**2*sf*spf/(3*Ap)), u, 0, NORD+1).removeO())
    R1 = sp.expand(sp.series(sp.exp(-2*Af), u, 0, NORD+1).removeO())
    return ([float(Pt.coeff(u, j)) for j in range(NORD+1)], [float(R0.coeff(u, j)) for j in range(NORD+1)],
            [float(R1.coeff(u, j)) for j in range(NORD+1)])
def bridge(pj, r0, r1, m2):
    r = [r0[j] + m2*r1[j] for j in range(NORD+1)]
    def rec(c0, c3):
        c = [0.0]*(NORD+1); c[0] = c0
        for N in range(0, NORD):
            if N == 2: c[3] = c3; continue
            S = sum((N-j)*c[N-j]*pj[j] for j in range(0, N+1)) + sum(c[N-1-j]*r[j] for j in range(0, N))
            c[N+1] = -S/((N+1)*(N-2.0))
        return np.array(c)
    return rec(1.0, 0.0), rec(0.0, 1.0)
def ev(c, d): return sum(c[k]*d**k for k in range(len(c))), sum(k*c[k]*d**(k-1) for k in range(1, len(c)))
def rhs_master(y, w, m2, bg):
    Q, Qp = w; A, Ap, s, sp_ = bg.sol(y); App = -sp_**2/3.0
    return [Qp, -(4*Ap - 2*App/Ap)*Qp - (m2*np.exp(-2*A) - (mu**2 + 4*App + 2*mu**2*s*sp_/(3*Ap)))*Q]
def bcdata(bg, y):
    A, Ap, s, sp_ = bg.sol(y); spp = mu**2*s - 4*Ap*sp_; return spp/sp_, np.exp(2*A)*sp_*spp/(3*Ap)
def F(m2, bg, fro, d=0.02):
    E, O = bridge(*fro, m2); W0, nu0 = bcdata(bg, 0.0); WL, nuL = bcdata(bg, 1.0)
    sL = solve_ivp(rhs_master, [0, 0.5-d], [m2+nu0, nu0*W0], args=(m2, bg), rtol=1e-12, atol=1e-15); QLm, QpLm = sL.y[:, -1]
    sR = solve_ivp(rhs_master, [1.0, 0.5+d], [m2+nuL, nuL*WL], args=(m2, bg), rtol=1e-12, atol=1e-15); QRp, QpRp = sR.y[:, -1]
    Em, Epm = ev(E, -d); Om, Opm = ev(O, -d); Ep, Epp = ev(E, d); Op, Opp = ev(O, d)
    cL = np.linalg.solve([[Em, Om], [Epm, Opm]], [QLm, QpLm]); cR = np.linalg.solve([[Ep, Op], [Epp, Opp]], [QRp, QpRp])
    return (cL[0]*cR[1] - cL[1]*cR[0])/(np.hypot(*cL)*np.hypot(*cR) + 1e-300)
def main(betas=(0.05, 0.10, 0.143, 0.30, 0.53, 0.70, 0.90), Rstar_um=8.2):
    print("betaL   F(1e-9)    m1L     m1/mKK   moduli   ecart    m2L    m3L   lambda_r@R*   verdict")
    for betaL in betas:
        bg, q, Lam = background(betaL); fro = frob_series(bg); F0 = F(1e-9, bg, fro)
        grid = np.concatenate([np.linspace(1e-4, 0.05, 30), np.linspace(0.05, 2.0, 60), np.linspace(2.0, 60, 90)])
        vals = np.array([F(m, bg, fro) for m in grid]); roots = []
        for i in range(len(grid)-1):
            if np.sign(vals[i]) != np.sign(vals[i+1]):
                try: roots.append(brentq(lambda m: F(m, bg, fro), grid[i], grid[i+1], xtol=1e-13))
                except Exception: pass
        ms = [np.sqrt(r) for r in roots[:3]] + [np.nan]*3
        moduli = 2*np.sqrt((2*Lam/q**2)*x*np.tanh(x/2))*betaL
        lam = np.pi*Rstar_um/ms[0]; v = "VERT" if lam <= 38.6 else ("ORANGE" if lam <= 70 else "ROUGE")
        print(f"{betaL:5.3f}  {F0:+.1e}  {ms[0]:6.4f}  {ms[0]/np.pi:6.4f}  {moduli:6.4f}  {100*(ms[0]/moduli-1):+5.1f}%  {ms[1]:5.3f}  {ms[2]:5.3f}  {lam:6.1f} um   {v}")
if __name__ == "__main__":
    main()
