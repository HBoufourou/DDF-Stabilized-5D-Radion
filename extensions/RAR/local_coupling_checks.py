"""Bounded audit, not a dark-matter formation or MOND calculation.

Python 3 standard library only. Writes JSON beside this file (or --output PATH).
Independent finite-difference boundary-value solve versus an infinite-line
Green-function integral for two separated, smooth, compact sources. Also
checks a switched-on local source in time with RK4, and constrained Legendre
transforms of repulsive quartic/sextic interactions. All units are explicit.
"""
from pathlib import Path
import argparse
import json
import math


def simpson(f, a, b, n=4096):
    assert n % 2 == 0
    h = (b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if i % 2 else 2)*f(a+i*h) for i in range(1, n)))


def source(x, center=0., width=.5, charge=1.):
    z = (x-center)/width
    return charge/width*math.cos(math.pi*z/2)**2 if abs(z) < 1 else 0.


def bvp(n, length=12., mass=1., center=2.):
    """(-d_x^2+mass^2)phi=J, phi(-length)=phi(length)=0; Thomas solve."""
    h = 2*length/n
    xs = [-length+i*h for i in range(n+1)]
    off = -1/h**2
    diag = [2/h**2+mass**2]*(n-1)
    rhs = [source(x, center) for x in xs[1:-1]]
    for i in range(1, n-1):
        fac = off/diag[i-1]
        diag[i] -= fac*off
        rhs[i] -= fac*rhs[i-1]
    sol = [0.]*(n-1)
    sol[-1] = rhs[-1]/diag[-1]
    for i in range(n-3, -1, -1):
        sol[i] = (rhs[i]-off*sol[i+1])/diag[i]
    return xs, [0.]+sol+[0.], h


def interaction(n):
    xs, phi, h = bvp(n)
    energy = -h*sum(source(x, -2.)*p for x, p in zip(xs, phi))
    residual = max(abs(-(phi[i+1]-2*phi[i]+phi[i-1])/h**2+phi[i]-source(xs[i], 2.)) for i in range(1, len(xs)-1))
    return {"cells": n, "interaction_energy_per_transverse_area": energy, "max_discrete_residual": residual}


def time_check(n, omega=math.sqrt(2.), j=1., end=100.37):
    """phi''+omega^2 phi=j, zero initial data, plus integrated phi."""
    y = [0., 0., 0.]
    dt = end/n
    def rhs(y): return [y[1], j-omega**2*y[0], y[0]]
    for _ in range(n):
        k1 = rhs(y)
        k2 = rhs([a+dt*b/2 for a,b in zip(y,k1)])
        k3 = rhs([a+dt*b/2 for a,b in zip(y,k2)])
        k4 = rhs([a+dt*b for a,b in zip(y,k3)])
        y = [a+dt*(b+2*c+2*d+e)/6 for a,b,c,d,e in zip(y,k1,k2,k3,k4)]
    exact = j/omega**2*(1-math.sin(omega*end)/(omega*end))
    return {"steps": n, "end_time": end, "omega": omega, "rk4_time_average": y[2]/end, "exact_time_average": exact, "absolute_error": abs(y[2]/end-exact), "static_response": j/omega**2}


def legendre(x, a, b):
    """sup_{n>=0} [n X - a n^2 - b n^3], a,b>=0, not both zero."""
    if x <= 0: return 0., 0.
    n = x/(2*a) if b == 0 else 2*x/(2*a+math.sqrt(4*a*a+12*b*x))
    return n, n*x-a*n*n-b*n**3


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_suffix('.json'))
    args = parser.parse_args()
    # Nonoverlapping sources centered at +/-2, width .5, mass 1.
    moment = simpson(lambda z: source(z)*math.exp(z), -.5, .5)
    exact_energy = -.5*math.exp(-4.)*moment**2
    spatial = [interaction(n) for n in (384, 768, 1536, 3072)]
    for row in spatial:
        row['relative_error_vs_infinite_line'] = abs(row['interaction_energy_per_transverse_area']/exact_energy-1)
    for a,b,c in zip(spatial, spatial[1:], spatial[2:]):
        c['observed_order_from_three_meshes'] = math.log(abs((a['interaction_energy_per_transverse_area']-b['interaction_energy_per_transverse_area'])/(b['interaction_energy_per_transverse_area']-c['interaction_energy_per_transverse_area'])),2)
    time = [time_check(n) for n in (4096, 8192, 16384)]
    # Physical eV units, velocity declared as one-dimensional dispersion.
    hbarc = 1.973269804e-5  # eV cm
    rho = .4e9*hbarc**3
    v = 200000/299792458
    zeta = 2.612375348685488
    thresholds = {
        'rho_eV4': rho, 'v_1d_over_c': v,
        'thermal_lambda_threshold_mass_eV': ((2*math.pi)**1.5*rho/(zeta*v**3))**.25,
        'legacy_h_over_mv_threshold_mass_eV': ((2*math.pi)**3*rho/(zeta*v**3))**.25,
        'interpretation': 'Phase-space degeneracy only; no equilibration or formation rate computed.'}
    cases = []
    for tag,a,b in [('quartic',1.,0.),('sextic',0.,1.),('mixed',1.,1.)]:
        for x in (-1., -.01, 0., .01, 1.):
            n,p = legendre(x,a,b)
            # Direct concave maximization by ternary search, independent of root formula.
            lo,hi = 0., 4.
            for _ in range(180):
                n1,n2 = (2*lo+hi)/3,(lo+2*hi)/3
                f1,f2 = n1*x-a*n1*n1-b*n1**3,n2*x-a*n2*n2-b*n2**3
                if f1 < f2: lo = n1
                else: hi = n2
            brute_n = (lo+hi)/2
            brute_p = max(0.,brute_n*x-a*brute_n**2-b*brute_n**3)
            cases.append({'interaction':tag,'X':x,'density':n,'pressure':p,'maximization_error':abs(p-brute_p)})
    # Re-evaluate exactly one archived tangle cell, holding its unproved model
    # assumptions fixed, to isolate the reduced/non-reduced Planck convention.
    a0 = 1.2e-10/(299792458**2)*1.973269804e-7
    kelvon = []
    for label, planck in [('archived_nonreduced',1.22e28),('corrected_reduced',2.435e27)]:
        lam = math.sqrt(a0*planck)
        mass, fs, logv, chi = .3, .03, 10., .3
        line_density = 3*mass*lam*math.sqrt(logv)
        spacing = line_density**-.5
        tau = spacing**2*mass/chi
        kelvon.append({'planck_convention':label,'Lambda_meV':lam*1e3,'spacing_um':spacing*1.973269804e-1,'v_over_c_archived_formula':2/(mass*spacing),'g4_threshold_archived_formula':6*mass**3*lam*math.sqrt(logv)/(fs*rho),'lifetime_seconds_archived_formula':tau*6.582119569e-16,'power_over_rhoH_archived_formula':(2*math.pi*fs*lam/mass)/tau/1.5e-33})
    # Amplitude response of GP gas: delta n(k)=-V(k)/(g+k^2/(4 m n0)).
    # Here m=g=1,n0=1/4 -> response healing length 1. This is not a halo fit.
    density_response = [{'k_times_response_length':k,'response_divided_by_contact_limit':1/(1+k*k)} for k in (0.,.1,1.,10.)]
    results = {
        'scope':'Counterexample and unit audit; neither MOND derivation nor dark-matter viability test.',
        'spatial_setup':{'geometry':'one dimensional, translationally invariant planes; energy per area','mass':1.,'source_centers':[-2.,2.],'source_half_width':.5,'source_integral_each':1.,'dirichlet_endpoints':[-12.,12.],'infinite_line_reference_energy':exact_energy,'infinite_line_force_along_separation':exact_energy},
        'spatial_convergence':spatial,'time_source_response':time,
        'legendre_density_nonnegative':cases,'degeneracy':thresholds,
        'kelvon_convention_only':kelvon,'density_response':density_response,
        'BK_plummer_formal_deep_branch':{'assumption':'Only algebraic slope in gradient-dominated spherical approximation, not a validated central solution.','peak_radius_over_b':1/math.sqrt(2),'samples':[{'r_over_b':r,'dlogrho_dlogr':(1-2*r*r)/(2*(1+r*r))} for r in (.1,.5,1.,2.)]},
        'validation':{'finite_separation_interaction_nonzero':exact_energy<0,'last_spatial_relative_error_below_2e_5':spatial[-1]['relative_error_vs_infinite_line']<2e-5,'time_error_below_1e_8':time[-1]['absolute_error']<1e-8,'constrained_max_error_below_1e_12':max(c['maximization_error'] for c in cases)<1e-12}}
    assert all(results['validation'].values()),results['validation']
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(args.output),'validation':results['validation'],'energy':exact_energy,'last_spatial':spatial[-1],'degeneracy':thresholds,'kelvon':kelvon},indent=2))


if __name__ == '__main__': main()
