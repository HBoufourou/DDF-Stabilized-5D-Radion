"""Independent radion comparison: Legendre Ritz-Galerkin with endpoint weights.

Standard library + NumPy. One physical interval, M5^3=L=1 for the spectrum.
R0=3 micrometres is a configurable INPUT, never a predicted radius.
Affine boundary potentials and reconstructed quadratic potentials are distinct
families; at fixed (x,epsilon), their background is identical by construction.
No archived script is imported or executed. Optional input_data JSON files
contain independently audited reference numbers for comparison.
"""
import argparse,cmath,json,math
from pathlib import Path
import numpy as np


def rhs(z,mu):
    A,a,s,q=z
    return np.array([a,-q*q/3,q,mu*mu*s-4*a*q])


def step(z,h,mu):
    a=rhs(z,mu);b=rhs(z+h*a/2,mu);c=rhs(z+h*b/2,mu);d=rhs(z+h*c,mu)
    return z+h*(a+2*b+2*c+d)/6


def make_background(epsilon,x=2.,n=4096):
    qb=math.sqrt(12)*epsilon
    def integrate(vc,steps,keep=False):
        z=np.array([0.,0.,0.,vc]);zz=[z.copy()] if keep else None
        for _ in range(steps):
            z=step(z,.5/steps,x)
            if max(abs(z))>1e6:return None
            if keep:zz.append(z.copy())
        return np.array(zz) if keep else z
    lo,hi=.01*qb/math.cosh(x/2),qb
    for _ in range(44):
        mid=(lo+hi)/2;z=integrate(mid,512)
        if z is None or z[3]>qb:hi=mid
        else:lo=mid
    vc=(lo+hi)/2
    for _ in range(3):
        residual=integrate(vc,n)[3]-qb
        deriv=(integrate(vc*(1+1e-6),n)[3]-integrate(vc*(1-1e-6),n)[3])/(2e-6*vc)
        vc-=residual/deriv
    zz=integrate(vc,n,True);tt=np.linspace(0,.5,n+1);hh=.5/n
    dz=np.array([rhs(z,x) for z in zz]);shift=zz[-1,0]
    def at(y):
        y=np.asarray(y);t=np.abs(y-.5);j=np.minimum((t/hh).astype(int),n-1)
        u=(t-tt[j])/hh
        z=((2*u**3-3*u*u+1)[...,None]*zz[j]+(u**3-2*u*u+u)[...,None]*hh*dz[j]
          +(-2*u**3+3*u*u)[...,None]*zz[j+1]+(u**3-u*u)[...,None]*hh*dz[j+1])
        A=z[...,0]-shift;a=z[...,1]*np.sign(y-.5);s=z[...,2]*np.sign(y-.5);q=z[...,3]
        return A,a,s,q
    lam5=vc*vc/2
    constraint=6*zz[:,1]**2-zz[:,3]**2/2+x*x*zz[:,2]**2/2+lam5
    W=x*x*zz[-1,2]/zz[-1,3]-4*zz[-1,1]
    meta={'x':x,'epsilon':epsilon,'half_steps':n,'Lambda5':lam5,
       'A_center':-shift,'sigma_boundary':float(zz[-1,2]),'q_boundary':qb,
       'W_right':float(W),'U_each_boundary':float(3*zz[-1,1]),
       'constraint_max_abs':float(max(abs(constraint))),
       'source_relative_residual':float(zz[-1,3]/qb-1)}
    assert W>0 and meta['U_each_boundary']<0
    return at,meta


def spectrum(at,meta,lam,n=32,nq=384):
    t,qw=np.polynomial.legendre.leggauss(nq);y=(t+1)/2;qw=qw/2
    X=np.polynomial.legendre.legvander(t,n-1)*np.sqrt(2*np.arange(n)+1)
    dX=np.empty_like(X)
    for j in range(n):
        c=np.zeros(j+1);c[j]=1
        dX[:,j]=2*math.sqrt(2*j+1)*np.polynomial.legendre.legval(t,np.polynomial.legendre.legder(c))
    A,a,s,q=at(y);p=np.exp(-2*A)/q**2;w=np.exp(-4*A)/q**2;Q=2*np.exp(-2*A)/3
    K=dX.T@((qw*p)[:,None]*dX)+X.T@((qw*Q)[:,None]*X)
    D=X.T@((qw*w)[:,None]*X)
    ends=np.vstack([(-1.)**np.arange(n),np.ones(n)])*np.sqrt(2*np.arange(n)+1)
    B=meta['W_right']+2*lam if lam is not None else math.inf
    border=1/(meta['q_boundary']**2*B)
    D+=border*(ends.T@ends)
    ev=[];vec=[]
    for parity in [0,1]:
        ix=np.arange(parity,n,2);C=np.linalg.cholesky(D[np.ix_(ix,ix)])
        KK=K[np.ix_(ix,ix)];HH=np.linalg.solve(C,np.linalg.solve(C,KK).T).T
        e,v=np.linalg.eigh((HH+HH.T)/2);v=np.linalg.solve(C.T,v)
        for j in range(len(ix)):
            u=np.zeros(n);u[ix]=v[:,j]
            if ends[0]@u<0:u=-u
            ev.append(e[j]);vec.append(u)
    order=np.argsort(ev)
    # Refine the tiny eigenvalue by a stable Schur complement in the even block.
    # Constant mode coefficient is fixed to 1; its derivative stiffness vanishes
    # identically. This avoids loss of relative accuracy for epsilon -> 0.
    j0=order[0];mu2=float(ev[j0]);ix=np.arange(2,n,2)
    for _ in range(6):
        E=K[np.ix_(ix,ix)]-mu2*D[np.ix_(ix,ix)]
        r=K[ix,0]-mu2*D[ix,0]
        u=np.zeros(n);u[0]=1.;u[ix]=-np.linalg.solve(E,r)
        schur=K[0,0]-mu2*D[0,0]+(K[0,ix]-mu2*D[0,ix])@u[ix]
        mu2+=schur/(u@D@u)
    E=K[np.ix_(ix,ix)]-mu2*D[np.ix_(ix,ix)]
    u=np.zeros(n);u[0]=1.;u[ix]=-np.linalg.solve(E,K[ix,0]-mu2*D[ix,0])
    u/=math.sqrt(u@D@u)
    if ends[0]@u<0:u=-u
    ev[j0]=mu2;vec[j0]=u
    I=float(qw@np.exp(2*A));modes=[]
    for j in order[:3]:
        m2=float(ev[j]);u=vec[j];g=X@u;gp=dX@u
        energy=float(np.dot(qw,p*gp*gp+Q*g*g))
        normSL=float(np.dot(qw,w*g*g)+border*np.dot(ends@u,ends@u))
        N=4.5*energy;alpha=I*(ends[0]@u)**2/N
        residual=K@u-m2*D@u
        # Monotonicity theorem, derivative with respect to lambda_hat at fixed background.
        derivative=2*m2*np.dot(ends@u,ends@u)/(meta['q_boundary']**2*B*B*normSL) if lam is not None else None
        modes.append({'mL':math.sqrt(m2),'m2L2':m2,'alpha':float(alpha),
           'canonical_N':N,'spectral_D':normSL,'positive_energy_K':energy,
           'energy_identity_relative_residual':energy/(m2*normSL)-1,
           'eigen_equation_relative_residual':float(np.linalg.norm(residual)/(np.linalg.norm(K@u)+np.linalg.norm(m2*D@u))),
           'dm2_dlambda_hat_fixed_background':float(derivative) if derivative is not None else None,
           'g_left':float(ends[0]@u),'g_right':float(ends[1]@u)})
        assert m2>0 and N>0
    ix=np.arange(1,n,2)
    KT=dX.T@((qw*np.exp(4*A))[:,None]*dX)
    DT=X.T@((qw*np.exp(2*A))[:,None]*X)
    CT=np.linalg.cholesky(DT[np.ix_(ix,ix)])
    HH=np.linalg.solve(CT,np.linalg.solve(CT,KT[np.ix_(ix,ix)]).T).T
    tensor_mass=math.sqrt(float(np.linalg.eigvalsh((HH+HH.T)/2)[0]))
    return {'basis_modes':n,'quadrature_points':nq,'volume_I':I,'boundary_positive_B':B if lam is not None else None,
            'first_tensor_mass_mL':tensor_mass,
            'each_spectral_boundary_weight':border,'modes':modes}


def monotone_trial(eps,a0,delta,steps=4096,x=2.):
    q0=math.sqrt(12)*eps;s0=-(4*a0*q0/(x*x)+delta)
    lam5=q0*q0/2-x*x*s0*s0/2-6*a0*a0
    z=np.array([0.,-a0,s0,q0]);minq=q0;maximum=0.;constraint=0.;completed=True
    for j in range(steps):
        z=step(z,1/steps,x)
        if not np.all(np.isfinite(z)) or max(abs(z))>1e4:
            completed=False;break
        minq=min(minq,float(z[3]));maximum=max(maximum,abs(float(z[0])))
        constraint=max(constraint,abs(6*z[1]**2-z[3]**2/2+x*x*z[2]**2/2+lam5))
    out={'epsilon':eps,'a0':a0,'delta':delta,'steps':steps,'completed_to_L':completed,
         'last_y':(j+1)/steps,'sigma_prime_min_sample':minq,'Lambda5':lam5,
         'U0':3*a0,'W0':-x*x*delta/q0,'constraint_max_abs':constraint}
    if completed:
        WL=x*x*z[2]/z[3]-4*z[1]
        out.update({'UL':float(3*z[1]),'WL':float(WL),'A_boundary':float(z[0]),
           'sigma_boundary':float(z[2]),'q_boundary':float(z[3]),
           'qL_over_q0':float(z[3]/q0),'max_abs_A':maximum,
           'regular_positive_boundary_domain':bool(minq>0 and delta>0 and WL>0)})
    else:out['scope_stop']='Finite numerical threshold before L; not a proof of all-parameter nonexistence.'
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--radius-um',type=float,default=3.)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'));args=ap.parse_args()
    assert args.radius_um>0
    data={'scope':'Three scalar eigenmodes on fixed symmetric backgrounds; R0 is input; no exclusion or absolute-scale prediction.',
      'action':'M5^3 R/2; affine U=T+J sigma versus quadratic U=tau+lambda(sigma-v_i)^2 reconstructed on same background.',
      'radius_input_um':args.radius_um,'L_input_um':math.pi*args.radius_um,'cases':[],
      'background_refinement':[],'monotone_checks':[],'weak_coupling_checks':[]}
    for eps in [.1,.3,.53]:
        at,meta=make_background(eps,n=4096);at2,meta2=make_background(eps,n=8192)
        diff=float(max(abs(at(np.linspace(0,1,1001))[0]-at2(np.linspace(0,1,1001))[0])))
        data['background_refinement'].append({'epsilon':eps,'coarse':meta,'fine':meta2,'max_A_difference':diff})
        group=[]
        for lam in [0.,1.,20.,None]:
            runs=[spectrum(at2,meta2,lam,n,nq) for n,nq in [(20,256),(32,384),(48,512)]]
            r=runs[-1];m=r['modes'][0]
            physical={'range_radion_um':math.pi*args.radius_um/m['mL'],
                      'radion_mass_eV':.1973269804*m['mL']/(math.pi*args.radius_um),
                      'alpha_potential_relative_to_tensor_G':m['alpha'],
                      'range_first_tensor_um':math.pi*args.radius_um/r['first_tensor_mass_mL'],
                      'radion_to_first_tensor_mass_ratio':m['mL']/r['first_tensor_mass_mL']}
            q=meta2['q_boundary'];s=meta2['sigma_boundary'];U=meta2['U_each_boundary']
            if lam==0:
                constants={'family':'affine','J_left':q,'J_right':-q,'T_each':U+q*s,'U_each':U}
            elif lam is None:
                constants={'family':'stiff_limit','scope':'Limiting spectral boundary problem, not a finite quadratic action.','U_each':U}
            else:
                constants={'family':'quadratic','v_right':s+q/(2*lam),'v_left':-s-q/(2*lam),
                           'tau_each':U-q*q/(4*lam),'U_each':U}
            group.append({'epsilon':eps,'x':2.,'lambda_hat':lam,'boundary_constants':constants,
               'background':meta2,'runs':runs,'physical_input_scale_output':physical})
        for i in range(3):
            assert group[i+1]['runs'][-1]['modes'][0]['mL']>group[i]['runs'][-1]['modes'][0]['mL']
        data['cases'].extend(group)
        print(json.dumps({'epsilon':eps,'radions':[{'lambda_hat':c['lambda_hat'],**c['physical_input_scale_output']} for c in group]}),flush=True)
    for eps in [.02,.01,.005]:
        at,meta=make_background(eps,n=4096)
        for lam in [1.,20.]:
            runs=[spectrum(at,meta,lam,n,nq) for n,nq in [(20,256),(32,384),(48,512)]]
            m=runs[-1]['modes'][0]
            data['weak_coupling_checks'].append({'epsilon':eps,'x':2.,'lambda_hat':lam,'runs':runs,
                'kappa_observed':m['m2L2']/eps**2,'c_alpha_observed':(3*m['alpha']-1)/eps**2})
    for eps in [.3,.53]:
        for a0 in [.02,.1,.2]:
            for delta in [.05,.2]:
                coarse=monotone_trial(eps,a0,delta,2048);fine=monotone_trial(eps,a0,delta,4096)
                data['monotone_checks'].append({'coarse':coarse,'fine':fine})
    data['counterexample_a0_zero_delta_finite']={
      'a0':0.,'delta':.2,'sigma0':-.2,'W0_at_eps03':-4*.2/(math.sqrt(12)*.3),
      'interpretation':'Not the reflection center: sigma0 and W0 remain nonzero as a0 tends to zero at fixed delta.'}
    data['R_real_branch_check']={'mu':1.,'lambda':.5,'v':.3,'q':.2,
       'z_mu_v_over_q_minus_mu_over_2lambda':.5,'physical_muL':math.log(3.),
       'printed_archive_branch_imaginary_part':float((2*cmath.log(-math.sqrt(3))).imag),
       'interpretation':'Archive printed 2 log(-sqrt(3)); the real positive branch is log(3), without the imaginary branch contribution.'}
    # Analytic coefficients are POSTPROCESSING checks only, never spectrum inputs.
    data['weak_formula_comparison']=[]
    for lam in [1.,20.]:
        x=2.;C=math.cosh(x/2)**2;S=math.sinh(x);dd=x*math.tanh(x/2)+2*lam
        kap=4*dd/(1+dd*S/(2*x));calpha=(1+S/x)/C-C*kap*kap*(S/x-1)/(16*x*x)
        rows=[c for c in data['weak_coupling_checks'] if c['lambda_hat']==lam]
        ek=[c['kappa_observed']-kap for c in rows];ea=[c['c_alpha_observed']-calpha for c in rows]
        data['weak_formula_comparison'].append({'lambda_hat':lam,'kappa_formula':kap,'c_alpha_formula':calpha,
          'epsilon_list':[c['epsilon'] for c in rows],'kappa_errors':ek,'c_alpha_errors':ea,
          'kappa_error_reduction_when_epsilon_halved':[ek[i]/ek[i+1] for i in range(2)],
          'c_alpha_error_reduction_when_epsilon_halved':[ea[i]/ea[i+1] for i in range(2)]})
    # Old data are optional verification references; this solver is otherwise standalone.
    ref=Path(__file__).resolve().parent/'input_data/quadratic_fem.json'
    comparisons=[]
    if ref.exists():
        old=json.loads(ref.read_text(encoding='utf-8'))
        for new in data['cases']:
            if new['epsilon']!=.3:continue
            tag='infinity' if new['lambda_hat'] is None else new['lambda_hat']
            matching=[c for c in old['cases'] if c['lambda_hat']==tag and c['background']['epsilon']==.3]
            if not matching:continue
            c=matching[0]
            # Old JSON carries a per-observable validated selection in convergence.
            for j in range(3):
                conv=c['convergence'][j]
                if 'mL_selected_estimate' in conv:
                    mass=conv['mL_selected_estimate']
                    alpha=conv['alpha_selected_estimate']
                    if mass is not None and alpha is not None:
                        m=new['runs'][-1]['modes'][j]
                        comparisons.append({'lambda_hat':new['lambda_hat'],'n':j,
                           'relative_mass_difference':m['mL']/mass-1,'relative_alpha_difference':m['alpha']/alpha-1})
    data['reference_comparisons']=comparisons
    affine_ref=Path(__file__).resolve().parent/'input_data/spectre_5d.json'
    if affine_ref.exists():
        old=json.loads(affine_ref.read_text(encoding='utf-8'))
        candidates=[c for c in old if c['epsilon']==.53]
        if candidates:
            old=min(candidates,key=lambda c:c['tolerance'])
            new=next(c for c in data['cases'] if c['epsilon']==.53 and c['lambda_hat']==0)['runs'][-1]
            data['independent_affine_shooting_comparison_eps053']={
              'scalar_relative_mass_differences':[new['modes'][j]['mL']/old['scalar_modes'][j]['mL']-1 for j in range(3)],
              'scalar_relative_alpha_differences':[new['modes'][j]['alpha']/old['scalar_modes'][j]['alpha_scalar_conditional_archive_norm']-1 for j in range(3)],
              'first_tensor_relative_mass_difference':new['first_tensor_mass_mL']/old['tensor_modes'][0]['mL']-1}
    data['checks_passed']=True
    args.output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'saved':str(args.output),'checks_passed':True}),flush=True)


if __name__=='__main__':main()
