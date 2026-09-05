"""Independent check of the equations (not the action as printed) in DDF v3.

Units L=M5^3=1; consistent action convention M5^3*Ricci/2.
Integrate from the reflection centre. The scalar variable f is regular at A'=0:
f''+(2A'-2W)f'+(4A''-4A'W+m2 exp(-2A))f=0, W=sigma''/sigma'.
Boundary: W*(f'+2A'f)-m2 exp(-2A)*f=0.
These follow from the standard scalar perturbation equations and the DDF C1/BC.
No Frobenius bridge and no division by A'. The archive master is not imported.
Exploratory brane couplings use the archive's norm and are NOT an exclusion.
"""
import json, math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq

OUT = Path(__file__).resolve().parents[1] / "resultats"
OUT.mkdir(parents=True, exist_ok=True)

def background(eps, tol):
    mu=2.; q=math.sqrt(12)*eps
    def rhs(y,z):
        A,a,s,v=z
        return a,-v*v/3,v,mu*mu*s-4*a*v
    def shoot(v):
        sol=solve_ivp(rhs,(.5,1.),(0,0,0,v),rtol=tol,atol=tol*.01,dense_output=True)
        return sol
    def end(v):
        sol=shoot(v)
        return sol.y[3,-1]-q
    vc=brentq(end,q*.01,q,xtol=tol*.01)
    sol=shoot(vc)
    assert sol.success
    shift=sol.y[0,-1]
    def bg(y):
        A,a,s,v=sol.sol(y)
        return A-shift,a,s,v
    return bg, q, vc*vc/2

def mode(m2, parity, bg, tol, tensor=False):
    def rhs(y,z):
        A,a,s,v=bg(y); w=(4*s-4*a*v)/v
        if tensor:
            return z[1],-4*a*z[1]-m2*np.exp(-2*A)*z[0]
        return z[1],-(2*a-2*w)*z[1]-(-4*v*v/3-4*a*w+m2*np.exp(-2*A))*z[0]
    sol=solve_ivp(rhs,(.5,1.),(1.,0.) if parity=='even' else (0.,1.),
                  rtol=tol,atol=tol*.01,dense_output=True)
    A,a,s,v=bg(1.); w=(4*s-4*a*v)/v
    f,fp=sol.y[:,-1]
    res=fp if tensor else w*(fp+2*a*f)-m2*np.exp(-2*A)*f
    return res,sol,rhs

def roots(bg,tol,tensor=False):
    found=[]
    for parity in ('even','odd'):
        grid=np.r_[np.linspace(1e-7,2,40),np.linspace(2.1,32,80)]
        vals=[mode(m,parity,bg,tol,tensor)[0] for m in grid]
        for lo,hi,fl,fh in zip(grid[:-1],grid[1:],vals[:-1],vals[1:]):
            if fl*fh<0:
                root=brentq(lambda m:mode(m,parity,bg,tol,tensor)[0],lo,hi,xtol=tol*.02)
                found.append((root,parity))
    return sorted(found)[:3]

def audit(eps,tol):
    bg,q,Lam=background(eps,tol)
    sroots=roots(bg,tol); troots=roots(bg,tol,True)
    I=2*quad(lambda y:float(np.exp(2*bg(y)[0])),.5,1,epsabs=tol)[0]
    A,a,s,v=bg(1.); W=(4*s-4*a*v)/v
    mode_data=[]
    for m2,parity in sroots:
        res,sol,rhs=mode(m2,parity,bg,tol)
        def integrands(y):
            A,a,s,v=bg(y); w=(4*s-4*a*v)/v
            f,fp=sol.sol(y); fpp=rhs(y,(f,fp))[1]
            fluct=-3*(fp+2*a*f)/v
            fluctp=-3*(fpp+2*(-v*v/3)*f+2*a*fp-w*(fp+2*a*f))/v
            G=fluctp+2*v*f-w*fluct
            return float(np.exp(2*A)*(3*f*f+.5*fluct*fluct)),float(.5*np.exp(4*A)*G*G)
        norm=2*quad(lambda y:integrands(y)[0],.5,1,epsabs=tol)[0]
        bulk=2*quad(lambda y:integrands(y)[1],.5,1,epsabs=tol)[0]
        A,a,s,v=bg(1.); w=(4*s-4*a*v)/v; f,fp=sol.y[:,-1]
        fluct=-3*(fp+2*a*f)/v
        boundary=float(np.exp(4*A)*w*fluct*fluct)
        mode_data.append({'mL':float(np.sqrt(m2)), 'parity':parity,
          'lambda_um_if_L_equals_pi_times_8p2_um':float(np.pi*8.2/np.sqrt(m2)),
          'alpha_scalar_conditional_archive_norm':float(I*f*f/norm),
          'energy_identity_relative_residual':float((bulk+boundary)/(m2*norm)-1),
          'boundary_residual':float(res)})
    tensors=[]
    for m2,parity in troots:
        res,sol,_=mode(m2,parity,bg,tol,True)
        norm=2*quad(lambda y:float(np.exp(2*bg(y)[0])*sol.sol(y)[0]**2),.5,1,epsabs=tol)[0]
        alpha=(4/3)*I*sol.y[0,-1]**2/norm
        tensors.append({'mL':float(np.sqrt(m2)),'parity':parity,'alpha_tensor':float(alpha),
            'range_um_if_L_equals_pi_times_8p2_um':float(np.pi*8.2/np.sqrt(m2))})
    pts=np.linspace(.5,1,300)
    hamilton=[6*bg(y)[1]**2-.5*bg(y)[3]**2+2*bg(y)[2]**2+Lam for y in pts]
    result={'epsilon':eps,'tolerance':tol,'q':q,'Lambda5':Lam,'A_center':float(bg(.5)[0]),
        'sigma_endpoint':float(bg(1)[2]),'W_right':float(W),'I_over_L':float(I),
        'background_constraint_max_residual':float(max(abs(v) for v in hamilton)),
        'scalar_modes':mode_data,'tensor_modes':tensors}
    print(json.dumps(result),flush=True)
    return result

if __name__=='__main__':
    results=[audit(e,2e-10) for e in [.05,.143,.4,.53,.7,.9]]
    results.append(audit(.53,2e-12))
    (OUT/'spectre_5d_recalcule.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
