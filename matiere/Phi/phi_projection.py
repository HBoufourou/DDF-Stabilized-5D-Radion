"""Probe Phi: independent cosine-Galerkin projection and weak nonlinear closure.

Python standard library + NumPy only. All benchmark lengths are L=M5^3=1.
No cosmological abundance, portal or observational fit is inferred.
Reads optional input_data/phi_spectrum.json solely to compare verified linear
spectral benchmarks. The background and all new results are computed locally.
"""
from pathlib import Path
import json, math
import numpy as np


def rk4_step(z,h,x=2.):
    def rhs(u):
        A,a,s,v=u
        return np.array([a,-v*v/3,s*0+v,x*x*s-4*a*v])
    k1=rhs(z);k2=rhs(z+h*k1/2);k3=rhs(z+h*k2/2);k4=rhs(z+h*k3)
    return z+h*(k1+2*k2+2*k3+k4)/6


def background(n=4096):
    # Shooting is needed only at low resolution; final vc is corrected at n.
    q=math.sqrt(12)*.3
    def integrate(vc,steps,keep=False):
        z=np.array([0.,0.,0.,vc]);arr=[z.copy()] if keep else None
        for _ in range(steps):
            z=rk4_step(z,.5/steps)
            if keep:arr.append(z.copy())
        return np.array(arr) if keep else z
    lo,hi=.01*q/math.cosh(1),q
    for _ in range(48):
        mid=(lo+hi)/2
        if integrate(mid,512)[3]>q:hi=mid
        else:lo=mid
    vc=(lo+hi)/2
    for _ in range(3):
        r=integrate(vc,n)[3]-q
        derivative=(integrate(vc*(1+1e-6),n)[3]-integrate(vc*(1-1e-6),n)[3])/(2e-6*vc)
        vc-=r/derivative
    arr=integrate(vc,n,True);tt=np.linspace(0,.5,n+1)
    # Hermite interpolation of A and A' retains RK4 accuracy.
    def at(y):
        t=np.abs(np.asarray(y)-.5);j=np.minimum((t*2*n).astype(int),n-1)
        h=.5/n;u=(t-tt[j])/h
        A=((2*u**3-3*u*u+1)*arr[j,0]+(u**3-2*u*u+u)*h*arr[j,1]
           +(-2*u**3+3*u*u)*arr[j+1,0]+(u**3-u*u)*h*arr[j+1,1])-arr[-1,0]
        return A
    constraint=6*arr[:,1]**2-arr[:,3]**2/2+2*arr[:,2]**2+vc*vc/2
    return at,{'half_steps':n,'central_derivative':vc,'Lambda5':vc*vc/2,
       'A_center':-float(arr[-1,0]),'source_relative_residual':float(arr[-1,3]/q-1),
       'constraint_max_abs':float(np.max(np.abs(constraint)))}


class Galerkin:
    def __init__(self,at,n=40,nq=640):
        t,ww=np.polynomial.legendre.leggauss(nq)
        self.y=(t+1)/2;self.qw=ww/2;A=at(self.y)
        self.w=np.exp(2*A);self.p=np.exp(4*A);self.n=n
        k=np.arange(n)*math.pi
        self.X=np.cos(self.y[:,None]*k[None,:])*math.sqrt(2)
        self.X[:,0]=1
        self.dX=-np.sin(self.y[:,None]*k[None,:])*k[None,:]*math.sqrt(2)
        self.M=self.X.T@((self.qw*self.w)[:,None]*self.X)
        self.P=self.X.T@((self.qw*self.p)[:,None]*self.X)
        self.T=self.dX.T@((self.qw*self.p)[:,None]*self.dX)
        self.I=float(np.dot(self.qw,self.w));self.J=float(np.dot(self.qw,self.p))
        self.A=A;self.Amax=float(at(np.array([.5]))[0])

    def solve(self,mu):
        K=self.T+mu*mu*self.P
        values=[];vectors=[]
        # Exact reflection separates even and odd blocks, avoiding parity roundoff.
        for parity in [0,1]:
            ix=np.arange(parity,self.n,2);M=self.M[np.ix_(ix,ix)]
            KK=K[np.ix_(ix,ix)];C=np.linalg.cholesky(M)
            H=np.linalg.solve(C,np.linalg.solve(C,KK).T).T
            ev,uv=np.linalg.eigh((H+H.T)/2)
            vv=np.linalg.solve(C.T,uv)
            for j in range(len(ix)):
                v=np.zeros(self.n);v[ix]=vv[:,j]
                if v[0]+math.sqrt(2)*sum(v[1:])<0:v=-v
                values.append(ev[j]);vectors.append(v)
        order=np.argsort(values);ev=np.array(values)[order];v=np.array(vectors)[order].T
        if mu==0:
            assert abs(ev[0])<1e-9
            ev[0]=0.;v[:,0]=0.;v[0,0]=1/math.sqrt(self.I)
        psi=self.X@v
        coeff=psi.T@(self.qw*self.w)/math.sqrt(self.I)
        coeff[1::2]=0. # exact reflection identity
        quartic=psi.T@(self.qw*self.p*psi[:,0]**3)
        quartic[1::2]=0.
        normfrac=float(np.sum(coeff[1:]**2))
        total=mu*mu*self.J/self.I
        energyfrac=float(np.dot(ev[1:],coeff[1:]**2)/total) if mu else None
        # Continuum spectral bound uses max A, not a computed Galerkin eigenvalue.
        # Here A_min=0 and reflection excludes odd modes from the constant profile.
        variance=float(mu**4*np.dot(self.qw*self.w,(self.w-self.J/self.I)**2)/self.I)
        lower_even_eigenvalue=mu*mu+4*math.pi**2*math.exp(-2*self.Amax)
        if lower_even_eigenvalue>total and mu>0:
            norm_bound=variance/(lower_even_eigenvalue-total)**2
            energy_bound=lower_even_eigenvalue*norm_bound/total
            assert normfrac<norm_bound and energyfrac<energy_bound
        else:norm_bound=0. if mu==0 else None;energy_bound=None
        mixing=np.array([2*mu*mu*np.dot(self.qw,self.A*self.X[:,j])/(j*math.pi)**2
                        if j else 0. for j in range(self.n)])
        residual=K@v-self.M@v*ev[None,:]
        gram=v.T@self.M@v
        ratios=quartic/quartic[0]
        gaps=ev[1:]-ev[0]
        rotation_sum=float(np.sum((ratios[1:]/gaps)**2))
        static_sextic=float(np.sum(quartic[1:]**2/ev[1:]))
        data={'basis_modes':self.n,'quadrature_points':len(self.y),'mPhiL':mu,
          'masses_mL':np.sqrt(np.maximum(ev[:8],0)).tolist(),
          'coefficients_of_normalized_constant_first8':coeff[:8].tolist(),
          'homogeneous_KK_canonical_norm_fraction':normfrac,
          'homogeneous_KK_initial_energy_fraction_at_rest':energyfrac,
          'constant_profile_spectral_variance_m4L4':variance,
          'analytic_lower_first_even_excited_m2L2':lower_even_eigenvalue,
          'continuum_variance_KK_norm_upper_bound':norm_bound,
          'continuum_variance_KK_energy_upper_bound':energy_bound,
          'projection_parseval_abs_residual':float(abs(np.dot(coeff,coeff)-1)),
          'projection_energy_abs_residual':float(abs(np.dot(ev,coeff*coeff)-total)),
          'linear_equation_max_abs_residual_first8':float(np.max(np.abs(residual[:,:8]))),
          'orthonormality_max_abs_residual':float(np.max(np.abs(gram-np.eye(self.n)))),
          'lambda_n000_L_first8':quartic[:8].tolist(),
          'quartic_ratios_first8':ratios[:8].tolist(),
          'weak_warp_constant_projection_c2':float(mixing[2]),
          'rotation_admixture_sum_divided_by_eta2':rotation_sum,
          'static_tree_sextic_sum_lambda_squared_over_mn2':static_sextic}
        return data,{'ev':ev,'v':v,'psi':psi,'K':K,'quartic':quartic,'coeff':coeff}

    def nonlinear_rotation(self,mu,eta,linear):
        # Phi=F exp(-i omega t) u(y), integral w u^2=1.
        # eta=g4 F^2 L^2, g4=g5 lambda0000 from the zero-density eigenmode.
        ix=np.arange(0,self.n,2);M=self.M[np.ix_(ix,ix)]
        K=linear['K'][np.ix_(ix,ix)];X=self.X[:,ix]
        q0=linear['quartic'][0];h=eta/q0
        c=linear['v'][ix,0].copy();nu=linear['ev'][0]+eta
        for iteration in range(20):
            profile=X@c
            source=X.T@(self.qw*self.p*profile**3)
            r=K@c+h*source-nu*M@c
            norm=float(c@M@c)
            R=np.r_[r,norm-1]
            if max(abs(R))<2e-12:break
            J=K-nu*M+3*h*(X.T@((self.qw*self.p*profile**2)[:,None]*X))
            bordered=np.zeros((len(ix)+1,len(ix)+1))
            bordered[:-1,:-1]=J;bordered[:-1,-1]=-M@c
            bordered[-1,:-1]=2*c@M
            delta=np.linalg.solve(bordered,-R)
            c+=delta[:-1];nu+=delta[-1]
        assert max(abs(R))<5e-10
        coeff=np.zeros(self.n);coeff[ix]=c
        overlaps=linear['v'].T@self.M@coeff
        gaps=linear['ev'][1:]-linear['ev'][0]
        prediction=-eta*(linear['quartic'][1:]/q0)/gaps
        admixture=float(np.dot(overlaps[1:],overlaps[1:]))
        norm=float(coeff@self.M@coeff)
        energy=float(coeff@linear['K']@coeff+h/2*np.dot(self.qw*self.p,profile**4))
        undressed_energy=float(linear['ev'][0]+eta/2)
        Vmat=self.X.T@((self.qw*self.p*profile**2)[:,None]*self.X)
        Hminus=linear['K']-nu*self.M+h*Vmat
        Hplus=Hminus+2*h*Vmat
        C=np.linalg.cholesky(self.M)
        def eigenvalues(H):
            HH=np.linalg.solve(C,np.linalg.solve(C,H).T).T
            return np.linalg.eigvalsh((HH+HH.T)/2)
        minus=eigenvalues(Hminus);plus=eigenvalues(Hplus)
        assert minus[0]>-1e-8 and minus[1]>0 and plus[0]>0
        assert min(profile)>0
        return {'eta_g4_F2_L2':eta,'omega2L2':nu,'norm':norm,
          'maximum_nonlinear_projected_residual':float(max(abs(R))),
          'newton_iterations':iteration,
          'free_mode_amplitudes_first8':overlaps[:8].tolist(),
          'excited_free_mode_norm_fraction':admixture,
          'first_order_predicted_excited_norm_fraction':float(np.dot(prediction,prediction)),
          'a2_first_order':float(prediction[1]),
          'a2_relative_first_order_error':float(overlaps[2]/prediction[1]-1),
          'energy_per_F2':energy,'undressed_energy_per_F2':undressed_energy,
          'energy_difference_dressed_minus_undressed':energy-undressed_energy,
          'minimum_nodeless_profile_sample':float(min(profile)),
          'rotating_phase_Hminus_first4_eigenvalues':minus[:4].tolist(),
          'rotating_amplitude_Hplus_first4_eigenvalues':plus[:4].tolist(),
          'eta_over_first_even_gap':float(eta/(linear['ev'][2]-linear['ev'][0])),
          'eta_over_m0_squared':float(eta/linear['ev'][0]) if mu else None}


def main():
    out=Path(__file__).with_suffix('.json')
    at,bg=background(4096);at2,bg2=background(8192)
    data={'scope':'Free probe Phi projection and classical weak nonlinear charged-profile closure; no abundance or portal.',
          'background':bg,'background_refinement':bg2,
          'background_refinement_max_A_difference':float(np.max(np.abs(at(np.linspace(0,1,1001))-at2(np.linspace(0,1,1001))))),
          'basis':'Normalized flat Neumann cosines, independent Ritz-Galerkin; exact even/odd blocks.',
          'cases':[]}
    # Independent basis refinements; quadrature also increases.
    meshes=[Galerkin(at2,24,384),Galerkin(at2,40,640),Galerkin(at2,64,1024)]
    for mu in [0.,.1,1.,3.]:
        runs=[]
        for mesh in meshes:
            d,l=mesh.solve(mu);runs.append(d)
        last=meshes[-1];d,l=last.solve(mu)
        rotations=[last.nonlinear_rotation(mu,eta,l) for eta in [.001,.01,.1,1.]] if mu>0 else []
        rotation_refinement=[]
        if mu>0:
            for mesh in meshes[:-1]:
                _,ll=mesh.solve(mu)
                rr=mesh.nonlinear_rotation(mu,.1,ll)
                rotation_refinement.append({'basis_modes':mesh.n,
                   'excited_free_mode_norm_fraction':rr['excited_free_mode_norm_fraction'],
                   'omega2L2':rr['omega2L2'],
                   'a2':rr['free_mode_amplitudes_first8'][2]})
        assert runs[-1]['projection_parseval_abs_residual']<1e-10
        assert runs[-1]['projection_energy_abs_residual']<1e-9
        assert runs[-1]['orthonormality_max_abs_residual']<1e-10
        data['cases'].append({'mPhiL':mu,'runs':runs,'charged_stationary_profiles':rotations,
                             'charged_profile_eta01_refinement':rotation_refinement})
    mesh=meshes[-1];lo,hi=1.,3.
    for _ in range(45):
        mid=(lo+hi)/2;d,l=mesh.solve(mid)
        if l['ev'][2]-9*l['ev'][0]>0:lo=mid
        else:hi=mid
    mid=(lo+hi)/2;d,l=mesh.solve(mid)
    data['real_misalignment_third_harmonic_resonance']={'mPhiL':mid,
       'm0L':math.sqrt(l['ev'][0]),'m2L':math.sqrt(l['ev'][2]),
       'm2_squared_minus_9_m0_squared':float(l['ev'][2]-9*l['ev'][0]),
       'lambda2000_L':float(l['quartic'][2]),
       'scope':'Linear frequency coincidence only; nonlinear detuning, finite time, expansion and depletion not solved.'}
    # Compare previous independent P1 FEM data without executing its code.
    previous=Path(__file__).resolve().parent/'input_data/phi_spectrum.json'
    if previous.exists():
        prev=json.loads(previous.read_text(encoding='utf-8'))
        comparisons=[]
        for old in prev['cases']:
            new=next(c for c in data['cases'] if c['mPhiL']==old['mPhiL'])['runs'][-1]
            for n in range(4):
                oldmass=old['convergence'][n]['mL']['selected_estimate']
                comparisons.append({'mPhiL':old['mPhiL'],'n':n,
                  'relative_mass_difference':new['masses_mL'][n]/oldmass-1 if oldmass else 0.})
        data['independent_previous_FEM_comparison']=comparisons
        data['comparison_input']='input_data/phi_spectrum.json'
    else:
        data['comparison_input']='Optional input_data/phi_spectrum.json absent; comparison skipped, new calculations unaffected.'
    data['checks_passed']=True
    out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'saved':str(out),'background':bg,
       'projections':[{ 'mPhiL':c['mPhiL'],**{k:c['runs'][-1][k] for k in
       ['homogeneous_KK_canonical_norm_fraction','homogeneous_KK_initial_energy_fraction_at_rest']}} for c in data['cases']],
       'resonance':data['real_misalignment_third_harmonic_resonance']},indent=2))


if __name__=='__main__':main()
