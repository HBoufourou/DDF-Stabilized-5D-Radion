"""Reflection-symmetric Einstein-scalar interval, M5^3=L=1.

Action and canonical norms: see article/manuscript.tex. No division by A'.
The background family reconstructs Lambda5 and brane tensions at each (x, eps).
It does not keep every Lagrangian parameter fixed while changing L.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq


def background(x, eps, tol=2e-10):
    if x <= 0 or eps <= 0:
        raise ValueError('This chart requires x > 0 and eps > 0.')
    q = math.sqrt(12) * eps
    def rhs(t, z):
        A, a, sigma, v = z
        return a, -v*v/3, v, x*x*sigma-4*a*v
    def integrate(vc):
        return solve_ivp(rhs, (0, .5), (0, 0, 0, vc), method='DOP853',
                         rtol=tol, atol=tol*.01, dense_output=True)
    # Blow-up on the positive branch brackets a slope larger than q.
    def residual(vc):
        sol = integrate(vc)
        return sol.y[3, -1]-q if sol.success else 1e100
    lo = q / math.cosh(x/2) * .01
    vc = brentq(residual, lo, q, xtol=tol*.001)
    sol = integrate(vc)
    if not sol.success or abs(sol.y[3,-1]/q-1) > 100*tol:
        raise RuntimeError('Background shooting failed.')
    shift = sol.y[0, -1]
    def bg(t):
        z = sol.sol(np.abs(t))
        return z[0]-shift, np.sign(t)*z[1], np.sign(t)*z[2], z[3]
    return bg, {'x':x, 'epsilon':eps, 'q':q, 'Lambda5':vc*vc/2}


def mode(m2, parity, bg, x, tol=2e-10, tensor=False):
    def rhs(t, z):
        A, a, sigma, v = bg(t)
        if tensor:
            return z[1], -4*a*z[1]-m2*np.exp(-2*A)*z[0]
        W = x*x*sigma/v-4*a
        return z[1], -(2*a-2*W)*z[1]-(-4*v*v/3-4*a*W+m2*np.exp(-2*A))*z[0]
    sol = solve_ivp(rhs, (0,.5), (1,0) if parity=='even' else (0,1),
                    method='DOP853', rtol=tol, atol=tol*.01, dense_output=True)
    if not sol.success:
        raise RuntimeError('Mode integration failed.')
    A,a,sigma,v = bg(.5)
    f, fp = sol.y[:,-1]
    W = x*x*sigma/v-4*a
    residual = fp if tensor else W*(fp+2*a*f)-m2*np.exp(-2*A)*f
    return float(residual), sol


def lowest_roots(bg, x, tol=2e-10, tensor=False, count=3, m2max=100):
    found = []
    grid = np.unique(np.r_[np.geomspace(1e-9,.2,18), np.linspace(.2,m2max,240)])
    for parity in ['even', 'odd']:
        prev = grid[0]
        fprev = mode(prev,parity,bg,x,tol,tensor)[0]
        for curr in grid[1:]:
            fcurr = mode(curr,parity,bg,x,tol,tensor)[0]
            if fprev*fcurr < 0:
                root = brentq(lambda z:mode(z,parity,bg,x,tol,tensor)[0],
                              prev,curr,xtol=tol*.01)
                found.append((root,parity))
                if sum(p==parity for _,p in found) >= (count+1)//2:
                    break
            prev,fprev = curr,fcurr
    found.sort()
    if len(found)<count:
        raise RuntimeError('Insufficient roots; increase m2max or grid density.')
    return found[:count]


def evaluate(x, eps, tol=2e-10, count=3):
    bg, data = background(x,eps,tol)
    I = 2*quad(lambda t:math.exp(2*bg(t)[0]),0,.5,epsabs=tol)[0]
    A,a,sigma,v = bg(.5)
    data.update(tolerance=tol, I_over_L=I, A_center=float(bg(0)[0]),
                sigma_endpoint=float(sigma), W_right=float(x*x*sigma/v-4*a),
                U_endpoint=float(3*a), T_endpoint=float(3*a+v*sigma))
    ham = [6*bg(t)[1]**2-bg(t)[3]**2/2+x*x*bg(t)[2]**2/2+data['Lambda5']
           for t in np.linspace(0,.5,201)]
    data['constraint_residual'] = float(max(map(abs,ham)))
    for tensor in [False, True]:
        modes=[]
        for m2,parity in lowest_roots(bg,x,tol,tensor,count):
            res,sol = mode(m2,parity,bg,x,tol,tensor)
            fb,fpb = sol.y[:,-1]
            def density(t):
                A,a,sigma,v = bg(t)
                f,fp = sol.sol(t)
                return math.exp(2*A)*(f*f if tensor else 3*f*f+4.5*(fp+2*a*f)**2/v**2)
            N = 2*quad(density,0,.5,epsabs=tol,epsrel=tol)[0]
            entry={'mL':math.sqrt(m2),'parity':parity,'alpha':float((4/3 if tensor else 1)*I*fb*fb/N),
                   'boundary_residual':res}
            if not tensor:
                def wdensity(t):
                    A,a,sigma,v = bg(t)
                    f=sol.sol(t)[0]
                    return f*f/v**2
                W=x*x*sigma/v-4*a
                H=2*quad(wdensity,0,.5,epsabs=tol,epsrel=tol)[0]+2*fb*fb/(v*v*W)
                entry['norm_identity_relative_residual']=float(N/(4.5*m2*H)-1)
            modes.append(entry)
        data['tensor_modes' if tensor else 'scalar_modes']=modes
    return data
