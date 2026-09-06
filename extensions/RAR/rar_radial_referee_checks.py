"""Independent stdlib derivatives and variational checks of stored radial BVPs."""
from pathlib import Path
from bisect import bisect_right
import json
import math

ROOT = Path(__file__).resolve().parent

def h_of(b, c):
    lo, hi = 0., max(1., b * (1 + c*c))
    def flux(h):
        return h / (1+c*c) + 2*c*c*h**3/9
    for _ in range(90):
        mid = (lo+hi)/2
        if flux(mid) < b: lo = mid
        else: hi = mid
    return (lo+hi)/2

def F(b, c):
    h = h_of(b,c)
    return h*h*c*(-1/(1+c*c)**2+h*h/9)

def derivative(b, c):
    h = h_of(b,c)
    q = -1/(1+c*c)**2 + h*h/9
    ml = 1/(1+c*c)+2*c*c*h*h/3
    hc = (2*c*h/(1+c*c)**2-4*c*h**3/9)/ml
    return h*h*(q+4*c*c/(1+c*c)**3)+(2*h*c*q+2*h**3*c/9)*hc

def interp(xs, ys, x):
    i = max(0,min(len(xs)-2,bisect_right(xs,x)-1))
    t = (x-xs[i])/(xs[i+1]-xs[i])
    return ys[i]*(1-t)+ys[i+1]*t

def main():
    data = json.loads((ROOT/'rar_radial_bvp.json').read_text())
    checks=[]
    for b in [.01,.1,1.,3.,4.]:
        for c in [0.,.01,.2,1.,4.,8.]:
            step = 2e-5 * max(1.,abs(c))
            fd=(F(b,c-2*step)-8*F(b,c-step)+8*F(b,c+step)-F(b,c+2*step))/(12*step)
            analytic=derivative(b,c)
            checks.append(dict(b=b,chi=c,analytic=analytic,five_point=fd,
                error_scaled_by_max_1_derivative=abs(fd-analytic)/max(1.,abs(analytic))))
    trials=[]
    for row in data['cases']:
        if row.get('A')!=10 or 'profiles' not in row:continue
        xs=row['profiles']['s'];cs=row['profiles']['chi'];ell=row['ell_over_rb']
        for a in [.25,.35,.45,.6]:
            n=4096;ds=a/n;total=0.
            for i in range(n+1):
                s=i*ds;chi=interp(xs,cs,s)
                b=(1+row['f'])*row['A']*s/(1+s*s)**1.5
                term=derivative(b,chi)/ell**2*math.sin(math.pi*s/a)**2
                total+=term*(1 if i in (0,n) else 2 if i%2==0 else 4)
            potential=total*ds/3/(a/2)
            trials.append(dict(A=row['A'],ell_over_rb=ell,support_radius=a,
                kinetic=math.pi**2/a**2,potential_average=potential,
                rayleigh_quotient=math.pi**2/a**2+potential,
                note='Trial u=sin(pi*s/a) on [0,a], zero beyond. Stored chi linearly interpolated; not a certified continuum error bound.'))
    out=dict(max_derivative_check_error=max(c['error_scaled_by_max_1_derivative'] for c in checks),
             derivative_checks=checks,compact_support_trials=trials)
    (ROOT/'rar_radial_referee_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(max_derivative_check_error=out['max_derivative_check_error'],
                         compact_support_trials=trials),indent=2))

if __name__=='__main__':main()
