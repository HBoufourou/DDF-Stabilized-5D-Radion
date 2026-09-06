"""Solve length AND signed 4D curvature with all brane couplings fixed.

Single physical interval, M5^3 R/2. Canonical sigma, symmetric quadratic
branes, maximally symmetric slices R4=12 h. h can be negative (AdS).
Classical background calculation; no curved fluctuation stability claim.
Standard library only, with variational equations and RK4 refinement.
"""
from pathlib import Path
import json
import math


def solve_at_curvature(h, v=.3, steps=2000, mu=1., lam=.5, M5=1., Lambda=None):
    if Lambda is None: Lambda=v*v/8
    q0sq=2*Lambda-12*M5*h
    if q0sq<=0: raise ValueError('Nonpositive central scalar slope squared.')
    q0=math.sqrt(q0sq)
    if q0>=2*lam*v: raise ValueError('Outside the local event branch.')
    a=2*lam/mu;B=math.sqrt(2)*lam*v/math.sqrt(Lambda)
    Lflat=2/mu*math.log((B+math.sqrt(B*B+a*a-1))/(1+a))
    dt=Lflat/(2*steps)

    def rhs(z):
        A,w,s,q,I,J,G=z[:7]
        Ah,wh,sh,qh,Ih,Jh,Gh=z[7:]
        expm=math.exp(-2*A);expp=1/expm
        return [w,-q*q/(3*M5)-h*expm,q,mu*mu*s-4*w*q,expp,expm,q*q,
                wh,-2*q*qh/(3*M5)-expm+2*h*expm*Ah,qh,
                mu*mu*sh-4*wh*q-4*w*qh,2*expp*Ah,-2*expm*Ah,2*q*qh]

    def step(z,d):
        k1=rhs(z);k2=rhs([u+d*k/2 for u,k in zip(z,k1)])
        k3=rhs([u+d*k/2 for u,k in zip(z,k2)])
        k4=rhs([u+d*k for u,k in zip(z,k3)])
        return [u+d*(a+2*b+2*c+e)/6 for u,a,b,c,e in zip(z,k1,k2,k3,k4)]

    def event(z):return z[3]+2*lam*z[2]-2*lam*v
    z=[0.,0.,0.,q0,0.,0.,0.,0.,0.,0.,-6*M5/q0,0.,0.,0.]
    t=0.;cres=0.;profile=[]
    for k in range(4*steps):
        if k%max(1,steps//100)==0:profile.append([t,*z[:4]])
        zn=step(z,dt)
        if event(zn)>=0:
            lo,hi=0.,dt
            for _ in range(45):
                mid=(lo+hi)/2
                if event(step(z,mid))>=0:hi=mid
                else:lo=mid
            d=(lo+hi)/2;z=step(z,d);t+=d
            break
        z=zn;t+=dt
        A,w,s,q=z[:4]
        cres=max(cres,abs(6*M5*(w*w-h*math.exp(-2*A))-q*q/2+mu*mu*s*s/2+Lambda))
    else:raise RuntimeError('No event found in the declared finite integration range.')
    A,w,s,q,I,J,G=z[:7];dz=rhs(z)
    th=-(z[10]+2*lam*z[9])/(dz[3]+2*lam*q)
    total=[zh+zd*th for zh,zd in zip(z[7:],dz[:7])]
    tau=3*M5*w-lam*(s-v)**2
    tauh=3*M5*total[1]-2*lam*(s-v)*total[2]
    hbrane=h*math.exp(-2*A)
    hbder=math.exp(-2*A)*(1-2*h*total[0])
    M4sq=2*M5*I*math.exp(-2*A)
    profile.append([t,*z[:4]])
    return dict(inputs=dict(mu=mu,lambda_brane=lam,v=v,M5_cubed=M5,Lambda5=Lambda),
        h_center=h,h_brane=hbrane,L=2*t,R_conventional=2*t/math.pi,
        tau_required=tau,M4_squared=M4sq,A_boundary_center_units=A,
        scalar_slope_center=q0,scalar_slope_boundary=q,
        derivatives=dict(dL_dh_center=2*th,dtau_dh_center=tauh,
            dh_brane_dh_center=hbder,dL_dtau=2*th/tauh),
        scalar_boundary_residual=event(z),constraint_max_absolute=cres,
        integrated_sum_rule_residual=6*M5*w+2*G+6*M5*h*J,
        steps_per_flat_half_interval=steps,profile_center_to_boundary=profile)


def solve_fixed_tension(tau_target,v,steps=2000,seed_h=0.):
    h=seed_h;history=[]
    for _ in range(12):
        row=solve_at_curvature(h,v,steps)
        residual=row['tau_required']-tau_target
        history.append(dict(h_center=h,tension_residual=residual))
        if abs(residual)<2e-14*max(v*v,1e-4):break
        h-=residual/row['derivatives']['dtau_dh_center']
    else:raise RuntimeError('Fixed-tension Newton iteration did not converge.')
    row['fixed_tau_input']=tau_target;row['tension_residual']=residual
    row['newton_history']=history
    return row


def main():
    reference=[];detunings=[]
    for v in (.02,.3,1.2):
        flat=solve_at_curvature(0.,v,4000)
        # Exact first-order response to an equal shift of both brane constants.
        deriv=flat['derivatives'];linear_hb_per_tau=deriv['dh_brane_dh_center']/deriv['dtau_dh_center']
        identity=linear_hb_per_tau/(2/(3*flat['M4_squared']))-1
        flat['linear_curvature_response_identity_relative_error']=identity
        assert abs(identity)<2e-9
        reference.append(flat)
        for relative in (-1e-4,-1e-5,1e-5,1e-4):
            delta=relative*v*v
            target=flat['tau_required']+delta
            coarse=solve_fixed_tension(target,v,2000)
            fine=solve_fixed_tension(target,v,4000,coarse['h_center'])
            fine['delta_tau_each']=delta
            fine['fractional_length_change']=fine['L']/flat['L']-1
            fine['linear_response_h_brane']=2*delta/(3*flat['M4_squared'])
            fine['relative_error_to_linear_h_brane']=fine['h_brane']/fine['linear_response_h_brane']-1
            fine['relative_error_to_linear_length_change']=(fine['L']-flat['L'])/(deriv['dL_dtau']*delta)-1
            fine['refinement']=dict(relative_L_change=fine['L']/coarse['L']-1,
                relative_h_brane_change=fine['h_brane']/coarse['h_brane']-1)
            assert abs(fine['constraint_max_absolute'])<1e-9
            assert abs(fine['integrated_sum_rule_residual'])<1e-10
            assert fine['h_brane']*delta>0
            detunings.append(fine)
            print(json.dumps({k:fine[k] for k in ('inputs','fixed_tau_input','L','h_brane','fractional_length_change','relative_error_to_linear_h_brane','refinement')}),flush=True)
    # One independent bracketed inversion uses no variational derivatives.
    chosen=next(r for r in detunings if r['inputs']['v']==.3 and r['delta_tau_each']>0)
    lo=0.;hi=chosen['h_center']*2
    flo=solve_at_curvature(lo,.3,2000)['tau_required']-chosen['fixed_tau_input']
    for _ in range(32):
        mid=(lo+hi)/2
        fm=solve_at_curvature(mid,.3,2000)['tau_required']-chosen['fixed_tau_input']
        if flo*fm<=0:hi=mid
        else:lo=mid;flo=fm
    bracketed=(lo+hi)/2
    result=dict(scope=__doc__,flat_reference=reference,fixed_tension_solutions=detunings,
        bracketed_crosscheck=dict(v=.3,tau_target=chosen['fixed_tau_input'],
            curvature_center_bisection=bracketed,curvature_center_newton=chosen['h_center'],
            relative_difference=bracketed/chosen['h_center']-1),
        limitations=['Local branch around the compatible Minkowski solution; no global uniqueness theorem for curved slices.',
            'Curved scalar/tensor fluctuations and possible AdS boundary conditions are not solved.',
            'All couplings and tension detunings are abstract inputs; neither observed dark energy nor a micrometric R is predicted.'])
    assert abs(result['bracketed_crosscheck']['relative_difference'])<1e-6
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':main()
