"""Closed finite-stiffness radion coupling checked against profile quadrature.

Python standard library only. No finite-backreaction spectrum is fitted.
The source action and limiting affine family are described in the companion note.
"""
from pathlib import Path
import argparse,json,math


def coefficients(x, stiffness):
    if x <= 0 or stiffness < 0:
        raise ValueError('Require x>0 and stiffness>=0.')
    C=math.cosh(x/2)**2; S=math.sinh(x); T=math.tanh(x/2)
    if math.isinf(stiffness):
        k=8*x/S
    else:
        d=x*T+2*stiffness
        k=4*d/(1+d*S/(2*x))
    c=(1+S/x)/C-C*k*k*(S/x-1)/(16*x*x)
    return k,c


def quadrature(x, stiffness, panels):
    if panels%2:raise ValueError('Simpson panels must be even.')
    k,_=coefficients(x,stiffness)
    C=math.cosh(x/2)**2
    def profiles(t):
        b=8*t*math.cosh(x*t)**2/C-k*math.sinh(2*x*t)/(2*x)
        v1=math.sqrt(12/C)*math.cosh(x*t)
        f2=(4*t*t+2*t*math.sinh(2*x*t)/x)/C-k*(math.cosh(2*x*t)-1)/(4*x*x)
        s1=-3*b/v1
        return f2,s1*s1
    step=1/panels
    sums=[[],[]]
    for j in range(panels+1):
        weight=1 if j in (0,panels) else 4 if j%2 else 2
        f,s=profiles(-.5+j*step)
        sums[0].append(weight*f);sums[1].append(weight*s)
    fmean,s2mean=[step*math.fsum(s)/3 for s in sums]
    fboundary=profiles(.5)[0]
    cquad=2*(fboundary-fmean)-s2mean/6
    bboundary=4*math.cosh(x/2)**2/C-k*math.sinh(x)/(2*x)
    # This bboundary is the unsimplified bulk solution at t=1/2.
    residual=bboundary if math.isinf(stiffness) else (x*math.tanh(x/2)+2*stiffness)*bboundary-k
    return dict(c_alpha=cquad,metric_term=2*(fboundary-fmean),scalar_kinetic_term=s2mean/6,
                boundary_residual=residual)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    args=ap.parse_args()
    rows=[]
    for x in (.25,.5,1.,2.,3.,4.,6.):
        for stiffness in (0.,.1,1.,20.,math.inf):
            k,c=coefficients(x,stiffness)
            q1=quadrature(x,stiffness,2048);q2=quadrature(x,stiffness,4096)
            C=math.cosh(x/2)**2;T=math.tanh(x/2);S=math.sinh(x)
            c0=(1+T*T+2*T/x)/C
            cinf=4*(math.cosh(x)-S/x)/(S*S)
            row=dict(x=x,lambda_hat='infinity' if math.isinf(stiffness) else stiffness,kappa=k,
                c_alpha=c,profile_quadrature=q2,quadrature_refinement=q2['c_alpha']-q1['c_alpha'],
                quadrature_minus_closed=q2['c_alpha']-c,affine_upper=c0,rigid_lower=cinf,
                bounds_hold=cinf-1e-12<=c<=c0+1e-12)
            assert abs(row['quadrature_minus_closed'])<2e-10
            assert abs(row['quadrature_refinement'])<2e-9
            assert abs(q2['boundary_residual'])<2e-12
            assert row['bounds_hold'] and cinf>0
            rows.append(row)
    data=dict(scope='Leading epsilon^2 at fixed x and equal lambda_hat; rebuilt boundary parameters keep the background fixed. No all-orders coupling monotonicity claim.',
        formula='c=(1+sinh(x)/x)/cosh(x/2)^2-cosh(x/2)^2*kappa^2*(sinh(x)/x-1)/(16*x^2)',
        rigorous_bounds='0<c_rigid<=c(x,lambda_hat)<=c_affine for x>0 and lambda_hat>=0; proof in companion note.',
        rows=rows,checks_passed=True,
        max_abs_quadrature_difference=max(abs(r['quadrature_minus_closed']) for r in rows),
        max_abs_refinement=max(abs(r['quadrature_refinement']) for r in rows))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in data.items() if k!='rows'},indent=2))


if __name__=='__main__':main()
