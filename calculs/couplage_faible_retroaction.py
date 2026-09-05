"""Evaluate the independently derived weak-backreaction integrals.
See 03_derivation_couplage_radion.md. L=M5^3=1, mu=2, epsilon=q/sqrt(12).
No fit to the spectral table or experimental data is used.
"""
import math

C = math.cosh(1)**2
kappa = 8*math.tanh(1)/C
def f2(t):
    return (4*t*t+t*math.sinh(4*t))/C-kappa*(math.cosh(4*t)-1)/16
def b(t):
    return 8*t*math.cosh(2*t)**2/C-kappa*math.sinh(4*t)/4
def v1(t):
    return math.sqrt(12)*math.cosh(2*t)/math.cosh(1)
def simpson(fun,n):
    h=.5/n
    return h/3*(fun(0)+fun(.5)
                +4*math.fsum(fun(i*h) for i in range(1,n,2))
                +2*math.fsum(fun(i*h) for i in range(2,n,2)))

def evaluate(n):
    avg_f2=2*simpson(f2,n)
    avg_s1sq=2*simpson(lambda t:(3*b(t)/v1(t))**2,n)
    c_alpha=2*(f2(.5)-avg_f2)-avg_s1sq/6
    return {'kappa':kappa,'f2_boundary':f2(.5),'mean_f2':avg_f2,
            'mean_s1_squared':avg_s1sq,'c_alpha':c_alpha}

coarse,fine=evaluate(10000),evaluate(20000)
error=abs(coarse['c_alpha']-fine['c_alpha'])
if error>1e-10:
    raise RuntimeError('Integral refinement did not converge to the requested threshold')
fine['refinement_absolute_difference']=error
print(fine)
