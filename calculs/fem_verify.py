"""P1 finite-element cross-check with the scalar endpoint spectral weights.

Run from an installed copy: python calculs/fem_verify.py [--extended]
The optional --repo PATH permits running this file before it is copied into a
repository. Results are written to resultats/fem_verification_recalcule.json by default.
Dependencies are declared in calculs/requirements.txt.

This is an independent spectral discretization, not an independent derivation
of the 5D theory. Only the background coefficient function is shared with the
shooting calculation. See audits/ARTICLE1_REFEREE.md for the analytical audit.
"""
from pathlib import Path
import argparse, json, importlib.util
import numpy as np
from scipy.integrate import quad
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh


def load_model(repo):
    spec=importlib.util.spec_from_file_location('interval_background',repo/'calculs'/'model.py')
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def coefficients(model,x,epsilon):
    bg,parameters=model.background(x,epsilon,2e-12)
    def at(y):
        y=np.asarray(y)
        A,aprime,sigma,v=(item.reshape(y.shape) for item in bg((y-.5).ravel()))
        return np.exp(-2*A)/v**2,np.exp(-4*A)/v**2,2*np.exp(-2*A)/3
    A,a,sigma,v=bg(.5)
    W=x*x*sigma/v-4*a
    endpoint_weight=float(np.exp(-4*A)/v**2/W)
    if not endpoint_weight>0:
        raise ValueError('This positive-definite verification requires W_left<0<W_right.')
    volume=2*quad(lambda t:float(np.exp(2*bg(t)[0])),0,.5,epsabs=1e-13,epsrel=1e-13)[0]
    return at,endpoint_weight,volume


def assemble(N,at,endpoint_weight):
    """K=integral(p u'v'+r uv), H=integral(w uv)+endpoint weights."""
    gx,gw=np.polynomial.legendre.leggauss(8)
    t=(gx+1)/2;wg=gw/2;h=1/N
    p,w,r=at((np.arange(N)[:,None]+t[None,:])*h)
    basis=np.stack([1-t,t]);ip=np.sum(p*wg,axis=1)/h
    rows=[];cols=[];kd=[];md=[]
    for i in range(2):
        for j in range(2):
            factor=basis[i]*basis[j]
            derivative_sign=(2*i-1)*(2*j-1)
            rows.append(np.arange(N)+i);cols.append(np.arange(N)+j)
            kd.append(derivative_sign*ip+h*np.sum(r*factor*wg,axis=1))
            md.append(h*np.sum(w*factor*wg,axis=1))
    rows=np.concatenate(rows);cols=np.concatenate(cols)
    K=coo_matrix((np.concatenate(kd),(rows,cols)),shape=(N+1,N+1)).tocsr()
    H=coo_matrix((np.concatenate(md),(rows,cols)),shape=(N+1,N+1)).tocsr()
    boundary=coo_matrix(([endpoint_weight,endpoint_weight],([0,N],[0,N])),shape=H.shape).tocsr()
    return K,H+boundary


def solve(N,at,endpoint_weight,volume):
    K,H=assemble(N,at,endpoint_weight)
    vals,vecs=eigsh(K,M=H,k=3,sigma=0,which='LM',tol=2e-13,v0=np.linspace(1,2,N+1))
    ix=np.argsort(vals);vals=vals[ix];vecs=vecs[:,ix]
    modes=[]
    for k in range(3):
        lam=vals[k];u=vecs[:,k]
        Hnorm=float(u@(H@u));Knorm=float(u@(K@u))
        physical_norm=4.5*lam*Hnorm
        alpha=volume*u[0]**2/physical_norm
        res=K@u-lam*(H@u)
        denominator=np.linalg.norm(K@u)+np.linalg.norm(lam*H@u)
        modes.append({'mL':float(np.sqrt(lam)),'alpha':float(alpha),'N':float(physical_norm),
                      'H_norm':Hnorm,'K_vs_lambdaH_relative_error':float(Knorm/(lam*Hnorm)-1),
                      'matrix_relative_residual':float(np.linalg.norm(res)/denominator),
                      'parity':'even' if abs(u[0]-u[-1])<abs(u[0]+u[-1]) else 'odd'})
    return {'elements':N,'scalar_modes':modes}


def references(repo,x,epsilon):
    files=['spectre_5d.json','extension_x.json']
    candidates=[]
    for file in files:
        path=repo/'resultats'/file
        if not path.exists():continue
        entries=json.loads(path.read_text(encoding='utf-8-sig'))
        for entry in entries:
            if abs(entry.get('x',2)-x)<1e-12 and abs(entry['epsilon']-epsilon)<1e-12:
                candidates.append((entry.get('tolerance',1),file,entry))
    if not candidates:
        raise ValueError(f'No recorded shooting reference for x={x}, epsilon={epsilon}.')
    _,filename,entry=min(candidates,key=lambda item:item[0])
    return filename,entry


def compare(runs,reference):
    rows=[]
    for k,ref in enumerate(reference['scalar_modes'][:3]):
        refa=ref.get('alpha',ref.get('alpha_scalar_conditional_archive_norm'))
        ms=[row['scalar_modes'][k]['mL'] for row in runs]
        al=[row['scalar_modes'][k]['alpha'] for row in runs]
        def order(values):
            return float(np.log2(abs((values[-3]-values[-2])/(values[-2]-values[-1]))))
        extrap_m=(4*ms[-1]-ms[-2])/3
        extrap_a=(4*al[-1]-al[-2])/3
        row={'mode':k,'mass_convergence_order_last_three':order(ms),'alpha_convergence_order_last_three':order(al),
             'raw_finest_mass_relative_error_vs_shooting':float(ms[-1]/ref['mL']-1),
             'raw_finest_alpha_relative_error_vs_shooting':float(al[-1]/refa-1),
             'richardson_mass':float(extrap_m),'richardson_alpha':float(extrap_a),
             'richardson_mass_relative_error_vs_shooting':float(extrap_m/ref['mL']-1),
             'richardson_alpha_relative_error_vs_shooting':float(extrap_a/refa-1)}
        # Conservative acceptance thresholds, not error bars on the physics.
        row['finite_element_crosscheck_passed']=bool(
            abs(row['raw_finest_mass_relative_error_vs_shooting'])<2e-5 and
            abs(row['raw_finest_alpha_relative_error_vs_shooting'])<2e-4 and
            abs(row['richardson_mass_relative_error_vs_shooting'])<2e-6 and
            abs(row['richardson_alpha_relative_error_vs_shooting'])<2e-6)
        rows.append(row)
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--extended',action='store_true')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();repo=args.repo.resolve();model=load_model(repo)
    cases=[(2.,.53)]+([(1.,.05),(1.,.4),(3.,.05),(3.,.4)] if args.extended else [])
    all_data=[]
    for x,epsilon in cases:
        at,end,volume=coefficients(model,x,epsilon)
        runs=[]
        for N in [64,128,256,512,1024,2048]:
            row=solve(N,at,end,volume);runs.append(row)
            print(json.dumps({'x':x,'epsilon':epsilon,**row}),flush=True)
        filename,ref=references(repo,x,epsilon)
        comparisons=compare(runs,ref)
        data={'x':x,'epsilon':epsilon,'I':volume,'each_endpoint_H_weight':end,
              'method':'P1 full-interval FEM; 8 point Gauss per cell; generalized SPD eigenproblem with endpoint spectral weights',
              'background':'Shared solve_ivp background at tolerance 2e-12; spectrum computed without shooting',
              'reference_file':filename,'reference_tolerance':ref.get('tolerance'),
              'runs':runs,'comparison':comparisons}
        all_data.append(data)
        print(json.dumps({'x':x,'epsilon':epsilon,'comparison':comparisons}),flush=True)
    output=args.output or repo/'resultats'/'fem_verification_recalcule.json'
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(all_data,indent=2),encoding='utf8')
    if not all(row['finite_element_crosscheck_passed'] for data in all_data for row in data['comparison']):
        raise RuntimeError('At least one FEM cross-check exceeds its declared numerical tolerance; inspect output.')

if __name__=='__main__':main()

