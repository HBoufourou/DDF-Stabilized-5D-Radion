"""Conditional radial gradient-sector benchmark, not a full superfluid halo.

Solves chi and the gravitational acceleration for a prescribed Plummer source.
The SF density, its formation and its outer transition are NOT solved. The EFT
is assumed valid throughout the finite computational domain. Outer chi is an
explicit boundary input. No parameters are fitted to galaxy data.
Requires numpy and scipy. Natural units. All parameters are dimensionless.
"""
from pathlib import Path
import json
import math
import numpy as np
from scipy.integrate import solve_bvp, simpson
from scipy.optimize import brentq
from scipy.linalg import eigh_tridiagonal

ROOT=Path(__file__).resolve().parent

def baryonic_h(s,A):
    return A*s/(1+s*s)**1.5

def acceleration(b,chi):
    """Unique positive root of c*h^3+d*h=b; stable at chi=0."""
    chi=np.asarray(chi);b=np.asarray(b)
    c=2*chi*chi/9
    d=1/(1+chi*chi)
    z=np.sqrt(3*c/d)
    # sinh(asinh(w)/3)/w -> 1/3 as w->0.
    w=1.5*(b/d)*z
    ratio=np.ones_like(w)/3
    mask=np.abs(w)>1e-7
    ratio[mask]=np.sinh(np.arcsinh(w[mask])/3)/w[mask]
    return 3*b/d*ratio

def adiabatic_h(b):
    b=np.asarray(b)
    flat=b.ravel()
    result=np.array([0. if u==0 else u if u>=3 else
        brentq(lambda h:h*h-2*h*h*h/9-u,0,3,xtol=1e-14) for u in flat])
    return result.reshape(b.shape)

def radial_jacobian(sol,A,ell,outer,f,n=2400):
    # Linearization with the prescribed enclosed mass held fixed. It detects
    # unstable stationary branches in this reduced radial problem, not ghosts.
    ds=outer/n
    s=np.arange(1,n)*ds
    cc=sol.sol(s)[0]
    hh=acceleration((1+f)*baryonic_h(s,A),cc)
    Q=-1/(1+cc*cc)**2+hh*hh/9
    muL=1/(1+cc*cc)+2*cc*cc*hh*hh/3
    hchi=(2*cc*hh/(1+cc*cc)**2-4*cc*hh**3/9)/muL
    fixed_h=hh*hh*(Q+4*cc*cc/(1+cc*cc)**3)
    partial_h=2*hh*cc*Q+2*hh**3*cc/9
    potential=(fixed_h+partial_h*hchi)/(ell*ell)
    eigen=eigh_tridiagonal(2/ds**2+potential,np.full(n-2,-1/ds**2),
                          select='i',select_range=(0,2),eigvals_only=True)
    return dict(intervals=n,eigenvalues=eigen.tolist(),
                scope='Reduced static radial Jacobian after eliminating acceleration at fixed prescribed enclosed mass; Dirichlet perturbations at outer boundary.',
                lowest_positive=bool(eigen[0]>0))

def reduced_energy(sol,A,ell,outer,f):
    estimates=[]
    for n in (16384,32768):
        s=np.linspace(0,outer,n+1)
        cc,cp=sol.sol(s)
        hh=acceleration((1+f)*baryonic_h(s,A),cc)
        W=-hh**2/(1+cc**2)-cc**2*hh**4/3
        estimates.append(float(simpson(s*s*(ell*ell*cp*cp+W),x=s)))
    return dict(energy=estimates[-1],quadrature_intervals=[16384,32768],
                quadrature_absolute_change=abs(estimates[-1]-estimates[-2]),
                scope='Dimensionless reduced static functional; compare only identical source, ell and boundary data.')

def solve_case(A,ell,outer=20.,f=0.,bc='adiabatic',tol=1e-5,previous=None,seed_adiabatic=False):
    b_out=(1+f)*float(baryonic_h(outer,A))
    h_out=float(adiabatic_h(b_out))
    chi_out=math.sqrt(max(0,3/h_out-1)) if bc=='adiabatic' else 0.
    # Increasing eta smoothly from zero follows a positive branch from the
    # forced outer solution; this is not a proof of uniqueness or stability.
    mesh=np.unique(np.r_[0.,np.geomspace(1e-5,1,100),np.linspace(1,outer,260)])
    eta=1/(ell*ell)
    history=[]
    if previous is None:
        yy=np.vstack([np.full_like(mesh,max(chi_out,1.)),np.zeros_like(mesh)])
        stages=np.r_[0.,np.geomspace(1e-8,eta,38)]
        if seed_adiabatic:
            he=adiabatic_h((1+f)*baryonic_h(np.sqrt(mesh**2+.02**2),A))
            cs=np.sqrt(np.maximum(0,3/he-1))
            yy=np.vstack([cs,np.gradient(cs,mesh)])
            yy[1,0]=0.
            stages=[eta]
    else:
        mesh=previous.x
        yy=previous.y
        prev_eta=previous.get('continuation_eta',eta)
        stages=np.geomspace(prev_eta,eta,12) if eta!=prev_eta else [eta]
    final=None
    for e in stages:
        def rhs(s,y):
            cc=y[0]
            h=acceleration((1+f)*baryonic_h(s,A),cc)
            return np.vstack([y[1],e*h*h*cc*(-1/(1+cc*cc)**2+h*h/9)])
        def boundary(ya,yb):return np.array([ya[1],yb[0]-chi_out])
        sol=solve_bvp(rhs,boundary,mesh,yy,S=np.array([[0.,0.],[0.,-2.]]),
                      tol=tol,bc_tol=tol*.1,max_nodes=16000)
        history.append(dict(eta=float(e),success=bool(sol.success),nodes=len(sol.x),
                            max_rms_residual=float(max(sol.rms_residuals))))
        if not sol.success:
            return None,dict(A=A,ell_over_rb=ell,outer_over_rb=outer,f=f,bc=bc,
                             status='SOLVER_DID_NOT_CONVERGE',history=history,
                             note='Numerical failure is not nonexistence of solutions.')
        mesh,yy=sol.x,sol.y
        sol['continuation_eta']=float(e)
        final=sol
    grid=np.unique(np.r_[0.,np.geomspace(1e-4,outer,700)])
    cc,cp=final.sol(grid)
    b=baryonic_h(grid,A);total=(1+f)*b
    h=acceleration(total,cc)
    had=adiabatic_h(total)
    algebra=h/(1+cc*cc)+2*cc*cc*h**3/9-total
    muT=1/(1+cc*cc)+2*cc*cc*h*h/9
    muL=1/(1+cc*cc)+2*cc*cc*h*h/3
    interior=(grid>=.05)&(grid<=10)
    rel=(h[interior]/had[interior]-1)
    report=dict(A=A,ell_over_rb=ell,outer_over_rb=outer,f=f,bc=bc,
        initial_seed='regularized_adiabatic' if seed_adiabatic else 'continuation_from_outer_forced_branch',
        chi_outer=chi_out,chi_center=float(cc[0]),
        status='CONVERGED_CONDITIONAL_BOUNDARY_PROBLEM',history=history,
        chi_min=float(min(cc)),chi_max=float(max(cc)),
        algebraic_flux_max_absolute_residual=float(max(abs(algebra))),
        fixed_chi_mu_transverse_min=float(min(muT)),
        fixed_chi_mu_longitudinal_min=float(min(muL)),
        max_fractional_departure_from_adiabatic_on_0p05_to_10=float(max(abs(rel))),
        median_fractional_departure_from_adiabatic_on_0p05_to_10=float(np.median(abs(rel))),
        reduced_radial_jacobian=radial_jacobian(final,A,ell,outer,f),
        reduced_static_energy=reduced_energy(final,A,ell,outer,f),
        profiles=dict(s=grid.tolist(),chi=cc.tolist(),chi_prime=cp.tolist(),
                      h=h.tolist(),h_baryonic=b.tolist(),h_adiabatic=had.tolist()))
    assert min(cc)>-1e-6,'This continuation did not remain on a positive branch.'
    assert max(abs(algebra))<1e-8 and min(muT)>0 and min(muL)>0
    return final,report

def main():
    cases=[];solutions={}
    for A in (1.,10.,100.):
        prev=None
        for ell in (1.,.3,.1,.03):
            sol,row=solve_case(A,ell,previous=prev)
            cases.append(row)
            if sol is not None:prev=sol;solutions[(A,ell)]=sol
            print(json.dumps({k:v for k,v in row.items() if k not in ('profiles','history')}),flush=True)
    alternatives=[]
    for A in (1.,10.,100.):
        for ell in (1.,.3,.1,.03):
            sol,row=solve_case(A,ell,seed_adiabatic=True)
            alternatives.append(row)
            if sol is not None and row['reduced_radial_jacobian']['lowest_positive']:
                solutions[(A,ell)]=sol
            print(json.dumps({'alternative_seed':True,**{k:v for k,v in row.items() if k not in ('profiles','history')}}),flush=True)
    refinements=[]
    for checked_ell in (.1,.03):
        if (10.,checked_ell) not in solutions:continue
        sol,row=solve_case(10.,checked_ell,tol=2e-7,previous=solutions[(10.,checked_ell)])
        ref=next(r for r in alternatives if r['A']==10 and r['ell_over_rb']==checked_ell)
        if sol is not None:
            p=np.array(row['profiles']['h']);q=np.array(ref['profiles']['h'])
            row['h_change_relative_max_against_tol_1e5']=float(np.max(np.abs(p[1:]/q[1:]-1)))
        if sol is not None:
            row['jacobian_grid_refinement']=radial_jacobian(sol,10.,checked_ell,20.,0.,n=4800)
        refinements.append(row)
    for outer,f in ((40.,0.),(20.,.3),(20.,1.)):
        sol,row=solve_case(10.,.1,outer=outer,f=f,seed_adiabatic=True)
        refinements.append(row)
    data=dict(scope=__doc__,definitions={'s':'r/r_b','h':'g/a0','A':'G M_b/(a0 r_b^2)',
       'ell_over_rb':'Z/(sqrt(2) M_Pl a0 r_b)','f':'Extra prescribed Plummer mass divided by baryonic mass',
       'equation':'h/(1+chi^2)+2chi^2 h^3/9=(1+f) A s/(1+s^2)^1.5',
       'boundary':'chi_prime(0)=0; chi(outer) fixed to the local adiabatic value'},
       cases=cases,alternative_seed_cases=alternatives,refinements_and_source_variations=refinements,
       limitations=['No self-consistent condensate density or phase boundary.',
                    'Static radial reduced-energy Hessian is tested at fixed source; no full time-dependent, angular, condensate or relativistic stability result.',
                    'Positive branch continuation, not all solutions or global uniqueness.',
                    'a0, Z, baryonic source and boundary are prescribed, not derived from 5D.',
                    'No SPARC fit, no R prediction, no direct observational exclusion.'])
    target=ROOT/'rar_radial_bvp.json';target.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'saved':str(target),'converged':sum(r['status'].startswith('CONVERGED') for r in cases),
                      'total':len(cases)}))

if __name__=='__main__':main()
