"""Finite-element spectrum for the newly specified quadratic-brane extension.

Run: python quadratic_fem.py [--output PATH]
Dependencies: numpy, scipy. No archived or published solver is imported.
Adapted transparently from the P1 method in DDF-Stabilized-5D-Radion/fem_verify.py.
Single physical interval, M5^3=L=1, V=Lambda5+x^2*sigma^2/2,
U_i=tau_i+lambda_hat*(sigma-v_i)^2 (same lambda at both ends).
At fixed x,epsilon the background is held fixed by reconstructing tau_i,v_i.
Only the endpoint spectral weights change as lambda_hat changes.
The inf entry means the limiting stiff boundary-value problem, not finite U.
Canonical norm is computed as the positive elementwise energy integral,
N=4.5*integral[p(g')^2+Qg^2], avoiding cancellation in assembled g^T K g.
No experimental verdict. The first three scalar modes only are calculated.
"""
import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh


def background(x,epsilon,tol=2e-12):
    q=math.sqrt(12)*epsilon
    def rhs(t,z):
        A,a,s,v=z
        return [a,-v*v/3,v,x*x*s-4*a*v]
    def shoot(vc):
        return solve_ivp(rhs,(0,.5),(0,0,0,vc),method='DOP853',
                         rtol=tol,atol=tol*.01,dense_output=True)
    def residual(vc):
        sol=shoot(vc)
        return sol.y[3,-1]-q if sol.success else 1e100
    vc=brentq(residual,q/math.cosh(x/2)*.01,q,xtol=2e-15)
    sol=shoot(vc)
    if not sol.success or abs(sol.y[3,-1]/q-1)>1e-9:
        raise RuntimeError('Background solve did not satisfy the requested source.')
    shift=sol.y[0,-1]
    def bg(t):
        t=np.asarray(t)
        z=sol.sol(np.abs(t))
        return z[0]-shift,np.sign(t)*z[1],np.sign(t)*z[2],z[3]
    A,a,s,v=bg(.5)
    W=x*x*s/v-4*a
    volume=2*quad(lambda t:float(np.exp(2*bg(t)[0])),0,.5,epsabs=1e-13,epsrel=1e-13)[0]
    constraint=[]
    for t in np.linspace(0,.5,201):
        AA,aa,ss,vv=bg(t)
        constraint.append(6*aa*aa-vv*vv/2+x*x*ss*ss/2+vc*vc/2)
    meta={'x':x,'epsilon':epsilon,'q':q,'Lambda5':vc*vc/2,'volume_I':volume,
          'A_center':float(bg(0)[0]),'sigma_boundary':float(s),'W_right':float(W),
          'U_total_each_boundary':float(3*a),'background_tolerance':tol,
          'constraint_max_abs':float(max(map(abs,constraint))),
          'source_relative_residual':float(v/q-1)}
    def at(y):
        shape=np.shape(y)
        AA,aa,ss,vv=(item.reshape(shape) for item in bg((np.asarray(y)-.5).ravel()))
        return np.exp(-2*AA)/vv**2,np.exp(-4*AA)/vv**2,2*np.exp(-2*AA)/3
    return at,meta


def assemble(n,at,end_weight):
    gx,gw=np.polynomial.legendre.leggauss(8)
    t=(gx+1)/2;weights=gw/2;h=1/n
    p,w,Q=at((np.arange(n)[:,None]+t[None,:])*h)
    shape=np.stack([1-t,t]);derivative=np.sum(p*weights,axis=1)/h
    rows=[];cols=[];kvals=[];hvals=[]
    for i in range(2):
        for j in range(2):
            basis=shape[i]*shape[j]
            rows.append(np.arange(n)+i);cols.append(np.arange(n)+j)
            kvals.append((2*i-1)*(2*j-1)*derivative+h*np.sum(Q*basis*weights,axis=1))
            hvals.append(h*np.sum(w*basis*weights,axis=1))
    rows=np.concatenate(rows);cols=np.concatenate(cols)
    K=coo_matrix((np.concatenate(kvals),(rows,cols)),shape=(n+1,n+1)).tocsr()
    H=coo_matrix((np.concatenate(hvals),(rows,cols)),shape=(n+1,n+1)).tocsr()
    H=H+coo_matrix(([end_weight,end_weight],([0,n],[0,n])),shape=H.shape).tocsr()
    return K,H


def solve(n,at,weight,I):
    K,H=assemble(n,at,weight)
    eig,vec=eigsh(K,M=H,k=3,sigma=0.,which='LM',tol=2e-13,v0=np.linspace(1,2,n+1))
    order=np.argsort(eig)
    modes=[]
    for j in order:
        mass2=float(eig[j]);u=vec[:,j]
        if mass2<=0:raise RuntimeError('Nonpositive eigenvalue in the positive problem.')
        Ku=K@u;Hu=H@u
        Hnorm=float(u@Hu)
        # For a nearly constant light mode, assembled u^T K u subtracts large
        # neighboring stiffness contributions. Integrate the nonnegative terms
        # first, cell by cell, to preserve the O(epsilon^2) coupling correction.
        gx,gw=np.polynomial.legendre.leggauss(8)
        t=(gx+1)/2;qw=gw/2;h=1/n
        p,w,Q=at((np.arange(n)[:,None]+t[None,:])*h)
        uq=u[:-1,None]*(1-t)[None,:]+u[1:,None]*t[None,:]
        up=(u[1:]-u[:-1])/h
        positive_density=(p*up[:,None]**2+Q*uq**2)*qw[None,:]*h
        energy=math.fsum(float(term) for term in positive_density.ravel())
        assembled_energy=float(u@Ku)
        N=4.5*energy
        alpha=float(I*u[0]**2/N)
        residual=float(np.linalg.norm(Ku-mass2*Hu)/(np.linalg.norm(Ku)+np.linalg.norm(mass2*Hu)))
        norm_error=energy/(mass2*Hnorm)-1
        if abs(norm_error)>2e-5:raise RuntimeError('Canonical-norm identity failed.')
        modes.append({'mL':math.sqrt(mass2),'m2L2':mass2,'alpha':alpha,
                      'canonical_N':N,'canonical_Z':2*N,'SL_norm_D':Hnorm,
                      'energy_H':energy,'norm_identity_relative_residual':norm_error,
                      'assembled_energy_relative_difference':assembled_energy/energy-1,
                      'canonical_normalization_method':'positive elementwise integral; assembled energy retained only as a cancellation diagnostic',
                      'matrix_relative_residual':residual,
                      'parity':'even' if abs(u[0]-u[-1])<abs(u[0]+u[-1]) else 'odd'})
    return {'elements':n,'modes':modes}


def weak(x,lamb):
    C=math.cosh(x/2)**2;T=math.tanh(x/2);d=x*T+2*lamb
    kappa=8*x/math.sinh(x) if math.isinf(lamb) else 4*d/(1+d*math.sinh(x)/(2*x))
    def v1(t):return math.sqrt(12)*math.cosh(x*t)/math.sqrt(C)
    def b(t):return 8*t*math.cosh(x*t)**2/C-kappa*math.sinh(2*x*t)/(2*x)
    def f2(t):return (4*t*t+2*t*math.sinh(2*x*t)/x)/C-kappa*(math.cosh(2*x*t)-1)/(4*x*x)
    avgf=2*quad(f2,0,.5,epsabs=1e-13,epsrel=1e-13)[0]
    avgs=2*quad(lambda t:(3*b(t)/v1(t))**2,0,.5,epsabs=1e-13,epsrel=1e-13)[0]
    return {'kappa':kappa,'c_alpha':2*(f2(.5)-avgf)-avgs/6}


def convergence(runs):
    rows=[]
    for j in range(3):
        row={'mode':j+1}
        for key in ('mL','alpha'):
            v=[r['modes'][j][key] for r in runs]
            coarse_delta=v[-3]-v[-2];fine_delta=v[-2]-v[-1]
            order=math.log2(abs(coarse_delta/fine_delta)) if fine_delta and coarse_delta else None
            extrap=(4*v[-1]-v[-2])/3
            floating_floor=128*np.finfo(float).eps*max(map(abs,v))
            verified=bool(order is not None and 1.5<order<2.5 and abs(fine_delta)>floating_floor)
            row[key+'_order_last_three']=order
            row[key+'_richardson_candidate']=extrap
            row[key+'_second_order_resolved']=verified
            row[key+'_estimate_method']='Richardson' if verified else 'finest grid; order-two extrapolation not validated'
            row[key+'_selected_estimate']=extrap if verified else v[-1]
            row[key+'_finest_vs_richardson_relative']=v[-1]/extrap-1
        rows.append(row)
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    args=parser.parse_args()
    data={'action':'M5^3 R/2 on one physical interval; quadratic U=tau+lambda(sigma-v)^2',
          'units':'M5^3=L=1; lambda_hat=lambda L; x=mu L; epsilon=qL/sqrt(12M5^3)',
          'scope':'First three scalar modes, no tensor/Phi/exclusion calculation; fixed background with reconstructed brane minima and tensions.',
          'method':'P1 full-interval FEM, 8-point Gauss quadrature, generalized eigenproblem including endpoint spectral weights.',
          'cases':[]}
    bg_cache={}
    for eps,lamb in ((.3,0.),(.3,1.),(.3,20.),(.3,float('inf')),(.01,1.),(.005,1.)):
        if eps not in bg_cache:bg_cache[eps]=background(2.,eps)
        at,meta=bg_cache[eps]
        B=meta['W_right']+2*lamb
        if B<=0:raise RuntimeError('Outside the strictly positive boundary-sign domain.')
        weight=0. if math.isinf(lamb) else 1/(meta['q']**2*B)
        runs=[solve(n,at,weight,meta['volume_I']) for n in (256,512,1024)]
        conv=convergence(runs);coeff=weak(2.,lamb)
        m=conv[0]['mL_selected_estimate'];alpha=conv[0]['alpha_selected_estimate']
        row={'lambda_hat':'infinity' if math.isinf(lamb) else lamb,'background':meta,
             'each_endpoint_D_weight':weight,'boundary_sign_quantity_B':None if math.isinf(lamb) else B,
             'runs':runs,'convergence':conv,'weak_coefficients':coeff,
             'asymptotic_comparison':{'kappa_from_finite_epsilon':m*m/eps**2,
                'mass_estimate_method':conv[0]['mL_estimate_method'],
                'coupling_estimate_method':conv[0]['alpha_estimate_method'],
                'kappa_finite_epsilon_relative_difference':m*m/(eps**2*coeff['kappa'])-1,
                'c_alpha_from_finite_epsilon':(3*alpha-1)/eps**2,
                'c_alpha_finite_epsilon_relative_difference':((3*alpha-1)/eps**2)/coeff['c_alpha']-1},
             'radion_range_um_if_R_equals_3um':math.pi*3/m}
        if lamb>0 and not math.isinf(lamb):
            row['quadratic_parameters']={'v_left':-meta['sigma_boundary']-meta['q']/(2*lamb),
                'v_right':meta['sigma_boundary']+meta['q']/(2*lamb),
                'tau_each':meta['U_total_each_boundary']-meta['q']**2/(4*lamb)}
        data['cases'].append(row)
        print(json.dumps({'epsilon':eps,'lambda_hat':row['lambda_hat'],'mrL':m,'alpha':alpha,
                          'range_at_R3um':row['radion_range_um_if_R_equals_3um'],
                          'asymptotic_comparison':row['asymptotic_comparison']}),flush=True)
    small=[r for r in data['cases'] if r['background']['epsilon']<.1]
    moderate=[r for r in data['cases'] if r['background']['epsilon']==.3]
    monotone=all(moderate[i+1]['runs'][-1]['modes'][j]['mL']>
                 moderate[i]['runs'][-1]['modes'][j]['mL']
                 for i in range(len(moderate)-1) for j in range(3))
    if not monotone:raise RuntimeError('Scalar mass monotonicity under increased brane stiffness failed at epsilon=0.3.')
    data['mass_positivity_and_moderate_epsilon_monotonicity_passed']=True
    data['small_epsilon_error_reduction']={
        k:abs(small[0]['asymptotic_comparison'][k]/small[1]['asymptotic_comparison'][k])
        for k in ('kappa_finite_epsilon_relative_difference','c_alpha_finite_epsilon_relative_difference')}
    data['small_epsilon_error_reduction_note']='Diagnostic ratio only; when mesh order is not resolved the finest-grid result is used, and no Richardson convergence or asymptotic remainder bound is claimed.'
    args.output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'saved':str(args.output),'small_epsilon_error_reduction':data['small_epsilon_error_reduction']}),flush=True)


if __name__=='__main__':main()
