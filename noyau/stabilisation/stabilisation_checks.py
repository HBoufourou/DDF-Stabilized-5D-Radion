"""Independent small checks of the NEW stated model; no archived solver imported.
Standard library only. L=M5^3=1. These are not an experimental exclusion.
"""
import json
import math
from pathlib import Path


def rk4_bg(epsilon, a0, delta, n=16000, mu=2.0):
    q = math.sqrt(12)*epsilon
    z = [0., -a0, -(4*a0*q/(mu*mu)+delta), q]
    initial = list(z)
    lam5 = q*q/2 - mu*mu*z[2]*z[2]/2 - 6*a0*a0
    h = 1/n
    minv = q
    max_constraint = 0.
    def rhs(z):
        A,a,s,v=z
        return [a,-v*v/3,v,mu*mu*s-4*a*v]
    for i in range(n):
        try:
            k1=rhs(z)
            k2=rhs([u+h*k/2 for u,k in zip(z,k1)])
            k3=rhs([u+h*k/2 for u,k in zip(z,k2)])
            k4=rhs([u+h*k for u,k in zip(z,k3)])
            z=[u+h*(a+2*b+2*c+d)/6 for u,a,b,c,d in zip(z,k1,k2,k3,k4)]
            if not all(math.isfinite(u) and abs(u)<1e80 for u in z):
                raise OverflowError
            A,a,s,v=z
            minv=min(minv,v)
            max_constraint=max(max_constraint,abs(6*a*a-v*v/2+mu*mu*s*s/2+lam5))
        except OverflowError:
            return {'epsilon':epsilon,'a0':a0,'delta':delta,'finite_to_L':False,
                    'integration_break_y':(i+1)*h,'status':'This IVP becomes singular numerically; not a global non-existence theorem.'}
    A,a,s,v=z
    return {'epsilon':epsilon,'a0':a0,'delta':delta,'finite_to_L':True,'steps':n,
            'initial':initial,'endpoint':z,'Lambda5':lam5,'q_left':q,'q_right':v,
            'q_right_over_left':v/q,'W_left':mu*mu*initial[2]/q+4*a0,
            'W_right':mu*mu*s/v-4*a,'U_left':3*a0,'U_right':3*a,
            'min_sigma_prime':minv,'max_constraint_abs':max_constraint}


def simpson(fun,n=20000):
    h=.5/n
    return 2*h/3*(fun(0)+fun(.5)+4*math.fsum(fun(i*h) for i in range(1,n,2))
                  +2*math.fsum(fun(i*h) for i in range(2,n,2)))


def weak_quadratic(x,lambda_hat):
    C=math.cosh(x/2)**2
    d=x*math.tanh(x/2)+2*lambda_hat
    kappa=8*x/math.sinh(x) if math.isinf(lambda_hat) else 4*d/(1+d*math.sinh(x)/(2*x))
    def v1(t): return math.sqrt(12)*math.cosh(x*t)/math.sqrt(C)
    def b(t): return 8*t*math.cosh(x*t)**2/C-kappa*math.sinh(2*x*t)/(2*x)
    def f2(t): return (4*t*t+2*t*math.sinh(2*x*t)/x)/C-kappa*(math.cosh(2*x*t)-1)/(4*x*x)
    c=2*(f2(.5)-simpson(f2))-simpson(lambda t:(3*b(t)/v1(t))**2)/6
    return {'x':x,'lambda_hat':'infinity' if math.isinf(lambda_hat) else lambda_hat,'kappa':kappa,'c_alpha':c,
            'boundary_order_epsilon2_residual':b(.5) if math.isinf(lambda_hat) else d*b(.5)-kappa,
            'mrL_leading_at_epsilon_0p3':math.sqrt(kappa)*.3,
            'alpha_leading_at_epsilon_0p3':(1+c*.3**2)/3,
            'status':'Asymptotic at fixed x,lambda_hat; not a finite-epsilon spectral calculation.'}


def symmetric_background(epsilon=.3, mu=2., n=4000):
    q=math.sqrt(12)*epsilon
    def integrate(vc):
        z=[0.,0.,0.,vc]
        h=.5/n
        def rhs(v):
            A,a,s,u=v
            return [a,-u*u/3,u,mu*mu*s-4*a*u]
        for i in range(n):
            k1=rhs(z); k2=rhs([u+h*k/2 for u,k in zip(z,k1)])
            k3=rhs([u+h*k/2 for u,k in zip(z,k2)])
            k4=rhs([u+h*k for u,k in zip(z,k3)])
            z=[u+h*(a+2*b+2*c+d)/6 for u,a,b,c,d in zip(z,k1,k2,k3,k4)]
        return z
    lo,hi=.01*q,q
    for _ in range(48):
        vc=(lo+hi)/2
        z=integrate(vc)
        if z[3]>q: hi=vc
        else: lo=vc
    A,a,s,v=integrate((lo+hi)/2)
    return {'epsilon':epsilon,'x':mu,'q':q,'sigma_center_prime':(lo+hi)/2,
            'A_center_in_brane_units':-A,'e2A_center':math.exp(-2*A),
            'sigma_boundary_over_M5_3half':s,'A_prime_right':a,'U_right':3*a,
            'W_right':mu*mu*s/v-4*a,'Lambda5':((lo+hi)/2)**2/2,
            'endpoint_derivative_error':v-q,'steps_half_interval':n}


if __name__=='__main__':
    out={'monotone_stated_points':[rk4_bg(.3,a,.2) for a in (.02,.1,.2)],
         'refinement_check':rk4_bg(.3,.02,.2,8000),
         'symmetric_epsilon_0p3':symmetric_background(),
         'quadratic_weak_coefficients':[weak_quadratic(2.,s) for s in (0.,1.,20.,float('inf'))]}
    target=Path(__file__).with_name('stabilisation_checks.json')
    target.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))
