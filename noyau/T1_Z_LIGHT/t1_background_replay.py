"""Independent standard-library replay of the null boundary-domain test.

Integrates fixed-action backgrounds, selects the length at the scalar Robin
event, and evaluates the full Israel tensor instead of its null-degenerate
scalar projections. All test units are abstract. This is not a radius fit.
"""
from pathlib import Path
import hashlib
import json
import math
import platform


def rk4(state, step, rhs):
    k1 = rhs(state)
    k2 = rhs(tuple(x + step*k/2 for x,k in zip(state,k1)))
    k3 = rhs(tuple(x + step*k/2 for x,k in zip(state,k2)))
    k4 = rhs(tuple(x + step*k for x,k in zip(state,k3)))
    return tuple(x + step*(a+2*b+2*c+d)/6 for x,a,b,c,d in zip(state,k1,k2,k3,k4))


def background(lam, v, subdivisions, mu=1., grav=1.):
    vacuum = lam*lam*v*v/2
    def rhs(z):
        A, H, sigma, q, integral = z
        return H, -q*q/(3*grav), q, mu*mu*sigma-4*H*q, math.exp(2*A)
    def event(z):
        return z[3] + 2*lam*(z[2]-v)
    state = (0., 0., 0., math.sqrt(2*vacuum), 0.)
    distance = 0.
    step = 1/(mu*subdivisions)
    while True:
        trial = rk4(state,step,rhs)
        if event(trial) >= 0:
            lo,hi=0.,step
            for _ in range(44):
                mid=(lo+hi)/2
                if event(rk4(state,mid,rhs)) < 0:lo=mid
                else:hi=mid
            frac=(lo+hi)/2
            state=rk4(state,frac,rhs)
            distance+=frac
            break
        state=trial
        distance+=step
        if distance>100/mu:raise ArithmeticError('Robin event not found')
    A,H,sigma,q,J=state
    qprime=mu*mu*sigma-4*H*q
    return dict(mu=mu,lambda_brane=lam,v=v,M5_cubed=grav,Lambda5=vacuum,
                tau_compatible=3*grav*H-q*q/(4*lam),L=2*distance,
                A_endpoint=A,H_right=H,sigma_right=sigma,q_endpoint=q,
                qprime_right=qprime,I=2*J,D0=-qprime/q-2*lam,DL=qprime/q+2*lam,
                scalar_event_residual=event(state),
                Einstein_constraint=6*grav*H*H-q*q/2+vacuum+mu*mu*sigma*sigma/2)


def rank(matrix, tolerance=1e-11):
    rows=[list(r) for r in matrix]
    rows=[[v/max(abs(x) for x in r) for v in r] if any(r) else r for r in rows]
    rank_=0
    for col in range(len(rows[0])):
        pivot=max(range(rank_,len(rows)),key=lambda i:abs(rows[i][col]),default=rank_)
        if rank_==len(rows) or abs(rows[pivot][col])<tolerance:continue
        rows[rank_],rows[pivot]=rows[pivot],rows[rank_]
        value=rows[rank_][col]
        rows[rank_]=[x/value for x in rows[rank_]]
        for i in range(len(rows)):
            if i!=rank_:
                value=rows[i][col]
                rows[i]=[x-value*y for x,y in zip(rows[i],rows[rank_])]
        rank_+=1
    return rank_


def boundary_matrix(data, D0=None, DL=None):
    q=data['q_endpoint'];a2=math.exp(2*data['A_endpoint']);I=data['I']
    D0=data['D0'] if D0 is None else D0
    DL=data['DL'] if DL is None else DL
    # Unknowns (c1,C,theta0,thetaL), theta_i=zeta_i+edge_normal_i.
    return [[0.,0.,q*D0,0.], [0.,0.,0.,q*DL],
            [0.,-1.,a2,0.], [-2*I,-1.,0.,a2]]


def israel_X1(data, side, omega=1., spatial_axis=3):
    """Linearize K_mn-K gamma_mn+U gamma_mn/B directly, in straight gauge.

    g_mn=a2(1+2F qwave)eta_mn, g_my=b partial_m qwave,
    F=-1,G=s=E=0; amplitudes qwave stripped. No scalar projection.
    """
    eta_diag=(-1.,1.,1.,1.)
    normal=-1 if side==0 else 1
    A=data['A_endpoint'];a2=math.exp(2*A)
    H=(-1 if side==0 else 1)*data['H_right']
    I=0. if side==0 else data['I']
    b=-2*I/a2
    p=[-omega,0.,0.,0.];p[spatial_axis]=omega
    F=-1.
    dgamma=[[2*a2*F*eta_diag[m] if m==n else 0. for n in range(4)] for m in range(4)]
    dgamma_y=[[2*H*x for x in row] for row in dgamma]
    # D_m N_n = -b p_m p_n for plane wave exp(i p.x).
    dK=[[normal*(dgamma_y[m][n]+2*b*p[m]*p[n])/2 for n in range(4)] for m in range(4)]
    trace_variation=sum(eta_diag[m]*dK[m][m]/a2 for m in range(4))-8*normal*H*F
    # U/B=3 normal H; delta U=0. Baseline K=4 normal H.
    tensor=[[dK[m][n]-normal*H*dgamma[m][n]-trace_variation*(a2*eta_diag[m] if m==n else 0.) for n in range(4)] for m in range(4)]
    trace=sum(eta_diag[m]*tensor[m][m] for m in range(4))
    double_projection=sum(eta_diag[m]*eta_diag[n]*p[m]*p[n]*tensor[m][n] for m in range(4) for n in range(4))
    expected=[[normal*b*p[m]*p[n] for n in range(4)] for m in range(4)]
    return dict(chi=b,tensor=tensor,tensor_max_abs=max(abs(x) for row in tensor for x in row),
                scalar_trace=trace,scalar_double_projection=double_projection,
                direct_vs_chi_formula_max_abs=max(abs(tensor[m][n]-expected[m][n]) for m in range(4) for n in range(4)))


def main(output=None):
    cases=[]
    for lam in (.1,.5,2.):
        for v in (.1,.3,.5):
            runs=[background(lam,v,n) for n in (1024,2048,4096)]
            data=runs[-1]
            errors={key:max(abs(r[key]-data[key]) for r in runs[:-1]) for key in ('L','I','D0','DL')}
            matrix=boundary_matrix(data)
            tensor_checks=[dict(side=side,omega=om,axis=axis,**israel_X1(data,side,om,axis)) for side in (0,1) for om,axis in ((.7,1),(1.,3),(2.,2))]
            assert rank(matrix)==4
            assert data['I']>0 and data['D0']<0<data['DL']
            assert abs(data['scalar_event_residual'])<1e-12 and abs(data['Einstein_constraint'])<1e-9
            assert max(errors.values())<1e-7
            for t in tensor_checks:
                assert max(abs(t[k]) for k in ('scalar_trace','scalar_double_projection','direct_vs_chi_formula_max_abs'))<1e-11
                assert (t['tensor_max_abs']<1e-12) if t['side']==0 else (t['tensor_max_abs']>1e-5)
            # The same background can be supported by separately reconstructed
            # affine boundary potentials. Complete Israel still excludes X1.
            W=data['qprime_right']/data['q_endpoint']
            assert rank(boundary_matrix(data,-W,W))==4
            # Negative controls: do not extend a nondegenerate proof by continuity.
            degenerate_ranks=[rank(boundary_matrix(data,0.,data['DL'])),rank(boundary_matrix(data,data['D0'],0.)),rank(boundary_matrix(data,0.,0.))]
            assert degenerate_ranks==[3,3,2]
            # Spectral-chart gauge xi5=-chi fails to preserve the right endpoint.
            gauge_endpoint_violation=2*data['I']*math.exp(-2*data['A_endpoint'])
            # Direct scalar junction excludes attempted compensation by an edge.
            edge_rescue_scalar_residual=data['q_endpoint']*data['DL']*gauge_endpoint_violation
            assert gauge_endpoint_violation>0 and edge_rescue_scalar_residual>0
            cases.append(dict(background=data,resolution_steps_per_unit=[1024,2048,4096],max_refinement_absolute=errors,
                              boundary_matrix=matrix,boundary_rank=4,physical_scalar_null_dimension=0,
                              X1_full_Israel_checks=tensor_checks,affine_reconstructed_boundary_rank=4,
                              degenerate_control_ranks=degenerate_ranks,
                              chart_gauge_right_endpoint_violation=gauge_endpoint_violation,
                              edge_rescue_scalar_residual=edge_rescue_scalar_residual,
                              raw_off_domain_norm_N=-3*data['M5_cubed']*data['I'],
                              raw_norm_scope='Formula to compare with independent covariant/ADM calculation; not itself a norm derivation.',
                              tensor_zero_mode_kinetic_Z_unit_polarization=data['M5_cubed']*data['I']/4))
    report=dict(scope='Fixed-action symmetric quadratic flat backgrounds; nonzero null four-momentum. Numerical boundary replay supports, but does not replace, the analytic completeness and symplectic proof.',
                checks_passed=True,X1_verdict='EXCLUDED_BY_FULL_ISRAEL_BOUNDARY_CONDITION',
                scalar_null_domain_verdict='TRIVIAL_AFTER_GAUGE_QUOTIENT_IN_DECLARED_DOMAIN',
                degenerate_endpoints='Not covered; rank-loss controls only, not a ghost verdict.',
                cases=cases,software={'python':platform.python_version()},
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    destination=Path(output) if output else Path(__file__).with_suffix('.json')
    destination.write_text(json.dumps(report,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps({'cases':len(cases),'checks':'PASS','full_tensor_checks':sum(len(c['X1_full_Israel_checks']) for c in cases),'X1':report['X1_verdict'],'output':str(destination)}))


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
    main(args.output)
