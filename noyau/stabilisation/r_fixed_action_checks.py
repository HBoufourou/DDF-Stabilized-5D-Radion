"""Fixed-action quadratic stabilization: standard-library reproducible checks.

All stationary-point test vectors are in arbitrary common energy units, not
physical radius benchmarks. No micrometric radius is fitted or predicted.
The scalar boundary-value problem is exact on a flat interval. Its use as a
gravitational radion potential is leading order in backreaction.
"""
import json
import math
from pathlib import Path


def scalar_data(length,mu,lam,v):
    u=mu*length/2
    a=2*lam/mu
    den=1+a*math.tanh(u)
    q=2*lam*v/den
    H=math.cosh(u)+a*math.sinh(u)
    K=math.sinh(u)+a*math.cosh(u)
    energy=2*lam*v*v/den
    d1=-2*lam*lam*v*v/(H*H)
    d2=-mu*d1*K/H
    return {'u':u,'a':a,'H':H,'K':K,'q':q,'sigma_boundary':q*math.tanh(u)/mu,
            'energy':energy,'dE_dL':d1,'d2E_dL2':d2}


def closed_length(mu,lam,v,Lambda5):
    if not (mu>0 and lam>0 and v>0 and 0<Lambda5<2*lam*lam*v*v):
        raise ValueError('No finite positive Minkowski stationary length in the stated domain.')
    a=2*lam/mu
    B=math.sqrt(2)*lam*v/math.sqrt(Lambda5)
    return 2/mu*math.log((B+math.sqrt(B*B+a*a-1))/(1+a))


def bisection(fun,lo,hi,n=100):
    flo=fun(lo);fhi=fun(hi)
    if flo*fhi>0:raise ValueError('Root is not bracketed.')
    for _ in range(n):
        mid=(lo+hi)/2;fm=fun(mid)
        if flo*fm<=0:hi=mid;fhi=fm
        else:lo=mid;flo=fm
    return (lo+hi)/2


def simpson(fun,length,n=12000):
    h=length/n
    return h/3*(fun(0)+fun(length)+4*math.fsum(fun(i*h) for i in range(1,n,2))
                +2*math.fsum(fun(i*h) for i in range(2,n,2)))


def stationary_case(a,B,mu=1.,v=.02,M5cubed=1.):
    lam=a*mu/2
    Lambda5=2*lam*lam*v*v/(B*B)
    L=closed_length(mu,lam,v,Lambda5)
    r=scalar_data(L,mu,lam,v)
    tau_sum=-Lambda5*L-r['energy']
    def VJ(length):return Lambda5*length+tau_sum+scalar_data(length,mu,lam,v)['energy']
    def VE(length):return (L/length)**2*VJ(length)
    def stationary_J(length):return Lambda5+scalar_data(length,mu,lam,v)['dE_dL']
    hi=max(L,1.)
    while stationary_J(hi)<0:hi*=2
    Lnum=bisection(stationary_J,1e-10,hi)
    h=max(.1,L)*1e-3
    numerical_second=(-VE(L+2*h)+16*VE(L+h)-30*VE(L)+16*VE(L-h)-VE(L-2*h))/(12*h*h)
    q=r['q']
    def profile(y):return q*math.sinh(mu*(y-L/2))/(mu*math.cosh(mu*L/2))
    def gradient(y):return q*math.cosh(mu*(y-L/2))/math.cosh(mu*L/2)
    direct_energy=simpson(lambda y:.5*(gradient(y)**2+mu*mu*profile(y)**2),L)
    direct_energy+=lam*(profile(0)+v)**2+lam*(profile(L)-v)**2
    epsilon=q*L/math.sqrt(12*M5cubed)
    x=mu*L;lambda_hat=lam*L;T=math.tanh(x/2);C=math.cosh(x/2)**2
    d=x*T+2*lambda_hat
    kappa=4*d/(1+d*math.sinh(x)/(2*x))
    M4squared=M5cubed*L
    mass2=2*L*L*r['d2E_dL2']/(3*M4squared)
    equivalent_mass2=kappa*epsilon*epsilon/(L*L)
    sensitivity={'mu':-1+a*math.sinh(r['u'])/(r['u']*r['K']),
                 'lambda':math.cosh(r['u'])/(r['u']*r['K']),
                 'v':B/(r['u']*r['K']),
                 'Lambda5':-B/(2*r['u']*r['K'])}
    numerical_sensitivity={}
    base={'mu':mu,'lam':lam,'v':v,'Lambda5':Lambda5}
    names={'mu':'mu','lambda':'lam','v':'v','Lambda5':'Lambda5'}
    dh=1e-5
    for name,argument in names.items():
        plus=dict(base);minus=dict(base)
        plus[argument]*=math.exp(dh);minus[argument]*=math.exp(-dh)
        numerical_sensitivity[name]=(math.log(closed_length(**plus))-math.log(closed_length(**minus)))/(2*dh)
    # A second Einstein-frame stationary point separates the Minkowski minimum
    # from the asymptotic V_E -> 0+ decompactification region.
    def F(length):
        z=scalar_data(length,mu,lam,v)
        return length*(Lambda5+z['dE_dL'])-2*VJ(length)
    lo=L*1.001;hi=L*2
    while F(hi)>0:hi*=1.5
    barrier=bisection(F,lo,hi)
    errors={'closed_vs_root_relative':Lnum/L-1,
            'integrated_vs_closed_energy_relative':direct_energy/r['energy']-1,
            'stationarity_residual_over_Lambda5':stationary_J(L)/Lambda5,
            'Minkowski_energy_residual':VJ(L),
            'scalar_right_BC_residual':gradient(L)-2*lam*(v-profile(L)),
            'Einstein_hessian_relative_difference':numerical_second/r['d2E_dL2']-1,
            'radion_mass_vs_spectral_kappa_relative':mass2/equivalent_mass2-1,
            'sensitivity_max_abs':max(abs(sensitivity[k]-numerical_sensitivity[k]) for k in sensitivity)}
    if max(abs(errors[k]) for k in errors if k!='sensitivity_max_abs')>2e-6:
        raise ArithmeticError(errors)
    if errors['sensitivity_max_abs']>2e-5:raise ArithmeticError(errors)
    return {'dimensionless_test_vector':{'a':a,'B':B},'fixed_action_parameters':base|{'tau_sum':tau_sum,'M5cubed':M5cubed},
            'derived_length_in_test_units':L,'x':x,'lambda_hat':lambda_hat,'epsilon':epsilon,
            'scalar':r,'mass_squared_leading_backreaction':mass2,'kappa':kappa,
            'Einstein_decompactification_barrier':{'length':barrier,'height':VE(barrier)},
            'logarithmic_sensitivities':sensitivity,'numerical_sensitivities':numerical_sensitivity,'checks':errors}


def identifiability_case(L,with_casimir=False):
    # Same mu,lambda,v,rho for different stationary L: counterterms differ.
    mu=1.;lam=.5;v=.02;rho=1e-10
    s=scalar_data(L,mu,lam,v)
    cas_C=1e-8 if with_casimir else 0.
    # Artificial unitless loop test coefficient, not physical field content.
    C0=cas_C/L**4;C1=-4*cas_C/L**5;C2=20*cas_C/L**6
    N=s['energy']+C0;Np=s['dE_dL']+C1;Npp=s['d2E_dL2']+C2
    Lambda5=2*rho/L-Np
    tau_sum=-rho+L*Np-N
    VJ=Lambda5*L+tau_sum+N
    VJp=Lambda5+Np
    hessian=Npp-2*rho/L**2
    errors={'value_vs_rho_abs':abs(VJ-rho),'Einstein_stationarity_abs':abs(VJp-2*VJ/L)}
    if max(errors.values())>1e-15:raise ArithmeticError(errors)
    if hessian<=0:raise ArithmeticError('This test vector is not stable.')
    return {'chosen_length_test_units':L,'same_inputs':{'mu':mu,'lambda':lam,'v':v,'rho':rho,'casimir_C_test':cas_C},
            'different_local_parameters':{'Lambda5':Lambda5,'tau_sum':tau_sum},
            'positive_Einstein_hessian':hessian,'checks':errors,
            'interpretation':'Same vacuum density, different stationary lengths; this is an identifiability counterexample, not a prediction.'}


def casimir_scaling():
    # zeta(5) from an elementary convergent sum with rigorous integral-tail bound.
    n=20000
    zeta5=math.fsum(1/k**5 for k in range(1,n+1))
    zeta_tail_bound=1/(4*n**4)
    Cscalar=-3*zeta5/(128*math.pi**2) # one real massless NN/DD scalar, physical interval
    M4_eV=2.435e27
    eps=.3;x=2.;lh=1.
    T=math.tanh(x/2);d=x*T+2*lh
    kappa=4*d/(1+d*math.sinh(x)/(2*x))
    rows=[]
    for inverseL in (.001,.01,.1):
        # Positive-C magnitude used only to display the Casimir curvature scale;
        # the real-boson coefficient above is negative and by itself unstable.
        mC=math.sqrt(40*abs(Cscalar)/3)*inverseL**2/M4_eV
        mTree=math.sqrt(kappa)*eps*inverseL
        fractional_shift=4*abs(Cscalar)*inverseL**2/(kappa*eps**2*M4_eV**2)
        rows.append({'inverse_interval_eV_test':inverseL,'absolute_Casimir_only_mass_scale_eV':mC,
                     'tree_radion_mass_eV_leading':mTree,'Casimir_to_tree_mass_scale_ratio':mC/mTree,
                     'fixed_tree_local_parameters_linearized_abs_deltaL_over_L':fractional_shift})
    return {'massless_real_interval_scalar_C':Cscalar,'bosonic_sign':'negative for identical NN/DD boundary conditions',
            'coefficient_definition':'V_C^J=C/L^4; interval, not a circle; no arbitrary sign flip.',
            'zeta5_sum_tail_upper_bound':zeta_tail_bound,'M4_reference_eV':M4_eV,
            'fixed_tree_test_shape':{'epsilon':eps,'x':x,'lambda_hat':lh,'kappa':kappa},
            'scale_tests_not_radius_predictions':rows,
            'assumptions':'Leading weak backreaction, massless-loop scaling, a small number of weakly coupled fields, no huge spectral enhancements. The complete DDF determinant is not computed here.'}


def exact_backreaction_fixed_action(v,steps,mu=1.,lam=.5,B=2.,M5cubed=1.):
    """Solve for length from fixed couplings, not for couplings at chosen length.

    The flat-slice center constraint fixes sigma'_c=sqrt(2 Lambda5).
    The scalar Robin condition is an event. The required common tension is a
    compatibility condition on the action; it is not used to fit the length.
    """
    Lambda5=2*lam*lam*v*v/(B*B)
    vc=math.sqrt(2*Lambda5)
    flat=closed_length(mu,lam,v,Lambda5)
    h=flat/(2*steps)
    def rhs(z):
        A,a,s,q,I=z
        return [a,-q*q/(3*M5cubed),q,mu*mu*s-4*a*q,math.exp(2*A)]
    def step(z,dt):
        k1=rhs(z)
        k2=rhs([u+dt*k/2 for u,k in zip(z,k1)])
        k3=rhs([u+dt*k/2 for u,k in zip(z,k2)])
        k4=rhs([u+dt*k for u,k in zip(z,k3)])
        return [u+dt*(a+2*b+2*c+d)/6 for u,a,b,c,d in zip(z,k1,k2,k3,k4)]
    def event(z):return z[3]+2*lam*z[2]-2*lam*v
    z=[0.,0.,0.,vc,0.];t=0.;constraint=[]
    for _ in range(steps+2):
        nxt=step(z,h)
        if event(nxt)>=0:
            lo,hi=0.,h
            for _ in range(50):
                mid=(lo+hi)/2
                if event(step(z,mid))>=0:hi=mid
                else:lo=mid
            dt=(lo+hi)/2;z=step(z,dt);t+=dt
            break
        z=nxt;t+=h
        A,a,s,q,I=z
        constraint.append(abs(6*M5cubed*a*a-q*q/2+mu*mu*s*s/2+Lambda5))
    else:raise RuntimeError('Robin event did not occur before the flat-length bound.')
    A,a,s,q,I=z;L=2*t
    tension=3*M5cubed*a-lam*(s-v)**2
    if not L<flat:raise ArithmeticError('Backreaction upper bound failed.')
    return {'fixed_inputs':{'mu':mu,'lambda':lam,'v':v,'Lambda5':Lambda5,'M5cubed':M5cubed},
            'steps_per_flat_half_length':steps,'derived_length':L,'flat_approximation_length':flat,
            'relative_length_shift_vs_flat':L/flat-1,'epsilon_at_solution':q*L/math.sqrt(12*M5cubed),
            'x_at_solution':mu*L,'lambda_hat_at_solution':lam*L,'sigma_boundary':s,
            'sigma_prime_boundary':q,'A_center_in_brane_units':-A,
            'M4_squared':M5cubed*2*math.exp(-2*A)*I,
            'required_tau_each_for_flat_slices':tension,'total_U_each':3*M5cubed*a,
            'scalar_boundary_residual':event(z),'constraint_max_abs':max(constraint,default=0.),
            'interpretation':'The length is an output of fixed mu,lambda,v,Lambda5; flat slices exist only if the independent tension matches the recorded compatibility value.'}


if __name__=='__main__':
    data={'scope':'Fixed-action quadratic scalar energy exact on flat interval; gravitational reduction and masses at leading weak backreaction.',
          'stationary_test_vectors':[stationary_case(a,B) for a in (.2,1.,3.) for B in (1.1,2.,5.)],
          'non_identifiability_at_fixed_vacuum_density':[identifiability_case(L,c) for c in (False,True) for L in (.5,1.,2.,3.)],
          'casimir_scale_checks':casimir_scaling()}
    exact=[]
    for amplitude in (.02,.3,.7,1.2):
        coarse=exact_backreaction_fixed_action(amplitude,4000)
        fine=exact_backreaction_fixed_action(amplitude,8000)
        fine['refinement_relative_length_difference']=coarse['derived_length']/fine['derived_length']-1
        fine['refinement_relative_tension_difference']=coarse['required_tau_each_for_flat_slices']/fine['required_tau_each_for_flat_slices']-1
        if abs(fine['refinement_relative_length_difference'])>1e-9:raise ArithmeticError(fine)
        exact.append(fine)
    data['exact_gravity_fixed_action_length_solutions']=exact
    target=Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'stationary_vectors':len(data['stationary_test_vectors']),
                      'identifiability_counterexamples':len(data['non_identifiability_at_fixed_vacuum_density']),
                      'maximum_hessian_test_relative_error':max(abs(r['checks']['Einstein_hessian_relative_difference']) for r in data['stationary_test_vectors']),
                      'saved':str(target),'casimir_scale_checks':data['casimir_scale_checks']},indent=2))
    print(json.dumps({'exact_fixed_action_lengths':[{'v':r['fixed_inputs']['v'],'L':r['derived_length'],
                         'epsilon':r['epsilon_at_solution'],'shift':r['relative_length_shift_vs_flat'],
                         'mesh_difference':r['refinement_relative_length_difference']} for r in exact]},indent=2))
