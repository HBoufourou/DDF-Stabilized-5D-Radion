"""Independent article-1 mathematical checks, using only the standard library.

No repository solver is imported. The residue is integrated from f2' rather
than the printed f2, with composite eight-point Gauss quadrature. Backgrounds
are re-solved in z=mu*t, s=sigma/v variables. Curvature derivatives use symmetric
finite differences of the background event, not variational equations.
"""
import json
import math
from pathlib import Path


NODES=(.1834346424956498,.5255324099163290,.7966664774136267,.9602898564975363)
WEIGHTS=(.3626837833783620,.3137066458778873,.2223810344533745,.1012285362903763)


def gauss_integrate(fun,left,right,panels=64):
    half=(right-left)/(2*panels)
    terms=[]
    for panel in range(panels):
        mid=left+(2*panel+1)*half
        for node,weight in zip(NODES,WEIGHTS):
            terms.append(half*weight*(fun(mid-node*half)+fun(mid+node*half)))
    return math.fsum(terms)


def closed(x,stiffness):
    S=math.sinh(x);H=math.cosh(x);C=(1+H)/2
    d=x*math.tanh(x/2)+2*stiffness
    kinf=8*x/S
    k=kinf if math.isinf(stiffness) else 8*x/(S+2*x/d)
    cinf=4*(H-S/x)/(S*S)
    c0=(1+math.tanh(x/2)**2+2*math.tanh(x/2)/x)/C
    if math.isinf(stiffness):c=cinf
    else:
        b=d*S/(2*x)
        c=cinf+4*C*(S/x-1)/(S*S)*(1+2*b)/(1+b)**2
    return k,c,c0,cinf


def profile_check(x,stiffness,panels):
    k,c,c0,cinf=closed(x,stiffness)
    C=math.cosh(x/2)**2
    def profiles(t):
        cc=math.cosh(x*t)
        b=cc*cc*(8*t/C-k*math.tanh(x*t)/x)
        a2p=-(2*t+math.sinh(2*x*t)/x)/C
        fp=b-2*a2p
        v1sq=12*cc*cc/C
        return fp,b*b/v1sq
    metric=4*gauss_integrate(lambda t:t*profiles(t)[0],0,.5,panels)
    kinetic=3*gauss_integrate(lambda t:profiles(t)[1],0,.5,panels)
    return {'kappa':k,'closed_c':c,'profile_c':metric-kinetic,'affine_upper':c0,
            'rigid_lower':cinf,'absolute_difference':abs(metric-kinetic-c)}


def flat_length(mu,lam,v,Lambda):
    a=2*lam/mu
    zeta=math.sqrt(2)*lam*v/math.sqrt(Lambda)
    return 2*math.log((zeta+math.sqrt(zeta*zeta+a*a-1))/(1+a))/mu


def background(mu,lam,v,B,Lambda,h=0.,resolution=3000):
    # Dimensionless coordinate z=mu*t and s=sigma/v.
    alpha=2*lam/mu;beta=v*v/B;hhat=h/(mu*mu)
    sc=math.sqrt(2*Lambda-12*B*h)/(mu*v)
    if not 0<sc<alpha:raise ValueError('Outside the central-slope event domain')
    zflat=mu*flat_length(mu,lam,v,Lambda)/2
    step=zflat/resolution
    def rhs(state):
        s,p,A,a,I=state
        return [p,s-4*a*p,a,-beta*p*p/3-hhat*math.exp(-2*A),math.exp(2*A)]
    def advance(state,delta):
        a=rhs(state)
        b=rhs([u+delta*w/2 for u,w in zip(state,a)])
        c=rhs([u+delta*w/2 for u,w in zip(state,b)])
        d=rhs([u+delta*w for u,w in zip(state,c)])
        return [u+delta*(w+2*x+2*y+z)/6 for u,w,x,y,z in zip(state,a,b,c,d)]
    def event(state):return state[1]+alpha*state[0]-alpha
    state=[0.,sc,0.,0.,0.];z=0.
    for _ in range(3*resolution):
        nxt=advance(state,step)
        if event(nxt)>=0:
            lo,hi=0.,step
            for _ in range(48):
                mid=(lo+hi)/2
                if event(advance(state,mid))<0:lo=mid
                else:hi=mid
            delta=(lo+hi)/2
            state=advance(state,delta);z+=delta
            break
        state=nxt;z+=step
    else:raise RuntimeError('No boundary event found')
    s,p,A,a,I=state
    sigma=v*s;q=mu*v*p;Aprime=mu*a
    length=2*z/mu
    M4sq=2*B*I*math.exp(-2*A)/mu
    return {'L':length,'L_flat':2*zflat/mu,'tau':3*B*Aprime-lam*(sigma-v)**2,
            'h_brane':h*math.exp(-2*A),'M4_squared':M4sq,'sigma_boundary':sigma,
            'W_boundary':(mu*mu*sigma-4*Aprime*q)/q,
            'scalar_boundary_residual':mu*v*event(state),
            'Einstein_constraint_residual':6*B*(Aprime*Aprime-h*math.exp(-2*A))-q*q/2+mu*mu*sigma*sigma/2+Lambda,
            'central_slope':mu*v*sc}


def main():
    profiles=[]
    for x in (.05,.5,2.,3.,6.,12.):
        for stiff in (0.,.1,1.,20.,math.inf):
            low=profile_check(x,stiff,16);high=profile_check(x,stiff,32)
            assert high['absolute_difference']<2e-11
            assert 0<high['rigid_lower']<=high['closed_c']+1e-13<=high['affine_upper']+2e-13
            profiles.append({'x':x,'stiffness':'rigid' if math.isinf(stiff) else stiff,
                **high,'quadrature_refinement':high['profile_c']-low['profile_c']})

    false_bound_examples=[{'x':x,'rigid_c':closed(x,math.inf)[1],
        'finite_stiffness_20_c':closed(x,20.)[1]} for x in (3.,6.,12.)]
    assert all(r['rigid_c']<1/3 and r['finite_stiffness_20_c']<1/3 for r in false_bound_examples)

    ratio_bounds=[]
    for x in (.05,.5,2.,3.,6.,12.):
        lower=math.pi**2/(2*x)*(1/math.tanh(x)-1/x)
        upper=math.pi**2/(2*x)*(1/math.tanh(x)+1/x)
        values=[]
        for stiff in (0.,.1,1.,20.,math.inf):
            k,c,_,_=closed(x,stiff)
            observed=math.pi**2*c/k
            # K_affine grows as pi^2/x^2, so use a relative endpoint tolerance.
            assert lower-2e-12*max(1.,abs(lower))<=observed<=upper+2e-12*max(1.,abs(upper))
            values.append(observed)
        assert all(a>b for a,b in zip(values,values[1:]))
        assert math.isclose(values[0],upper,rel_tol=2e-12,abs_tol=1e-10)
        assert math.isclose(values[-1],lower,rel_tol=2e-12,abs_tol=1e-10)
        assert math.isclose(upper-lower,math.pi**2/x**2,rel_tol=2e-12)
        ratio_bounds.append({'x':x,'K_affine':upper,'K_rigid':lower,
            'pi_squared_c_over_kappa_at_stiffness_0_point1_1_20_rigid':values,
            'affine_identity_absolute_difference':abs(values[0]-upper),
            'rigid_identity_absolute_difference':abs(values[-1]-lower)})

    events=[]
    for mu,lam,v,B,ratio in ((1.,.5,.3,1.,.25),(.4,.1,.1,2.,.6),
                             (1.3,2.,.7,1.,.1),(.7,.8,1.1,3.,.8),
                             (1.,.5,1.2,1.,.25)):
        Lambda=ratio*2*lam*lam*v*v
        lo=background(mu,lam,v,B,Lambda,resolution=1500)
        hi=background(mu,lam,v,B,Lambda,resolution=3000)
        assert 0<hi['L']<hi['L_flat']
        assert hi['W_boundary']+2*lam>0
        assert abs(hi['L']/lo['L']-1)<1e-9
        u=mu*hi['L_flat']/2
        slope_flat=2*lam*v/(math.cosh(u)+(2*lam/mu)*math.sinh(u))
        assert abs(slope_flat/math.sqrt(2*Lambda)-1)<1e-14
        events.append({'inputs':dict(mu=mu,lam=lam,v=v,B=B,Lambda=Lambda),
                       **hi,'relative_refinement':hi['L']/lo['L']-1,
                       'flat_stationary_central_slope':slope_flat})

    responses=[]
    for v in (.02,.3,1.2):
        Lambda=v*v/8
        flat=background(1.,.5,v,1.,Lambda,resolution=3000)
        expected=2/(3*flat['M4_squared'])
        checks=[]
        for fraction in (1e-3,1e-4,1e-5):
            step=Lambda*fraction
            minus=background(1.,.5,v,1.,Lambda,-step,3000)
            plus=background(1.,.5,v,1.,Lambda,step,3000)
            observed=(plus['h_brane']-minus['h_brane'])/(plus['tau']-minus['tau'])
            checks.append({'h_center_step':step,'observed_dhb_dtau':observed,
                           'relative_difference':observed/expected-1})
        assert abs(checks[-1]['relative_difference'])<2e-7
        responses.append({'v':v,'flat':flat,'expected_dhb_dtau':expected,'symmetric_differences':checks})

    result={'scope':'Independent analytic-formula/profile quadrature and background-event numerical checks. No complete spectral replay or bibliographic novelty audit.',
            'profile_comparisons':profiles,'counterexamples_to_review_calpha_gt_one_third':false_bound_examples,
            'fixed_action_length_cases':events,'curvature_response_cases':responses,
            'leading_observable_ratio_coefficient_bounds':ratio_bounds,
            'maximum_profile_formula_absolute_difference':max(r['absolute_difference'] for r in profiles),
            'maximum_background_length_refinement':max(abs(r['relative_refinement']) for r in events),
            'maximum_finest_response_relative_difference':max(abs(r['symmetric_differences'][-1]['relative_difference']) for r in responses),
            'checks_passed':True}
    out=Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k.startswith('maximum_') or k=='checks_passed'},indent=2))


if __name__=='__main__':main()
