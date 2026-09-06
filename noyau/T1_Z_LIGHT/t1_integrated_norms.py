"""Integrate independently contracted covariant and ADM currents on DDF solutions."""
from pathlib import Path
import hashlib, json, math, sys

BASE=Path(__file__).resolve().parent
if (BASE/'symplectic').is_dir():sys.path.insert(0,str(BASE/'symplectic'))
from covariant_adm_current import currents, boundary_covariant_C_Z
from t1_background_replay import rk4


def integrate(case, cells):
    B=case['M5_cubed'];mu=case['mu'];length=case['L']
    def rhs(z):
        A,H,sigma,q,I=z
        return H,-q*q/(3*B),q,mu*mu*sigma-4*H*q,math.exp(2*A)
    state=(case['A_endpoint'],-case['H_right'],-case['sigma_right'],case['q_endpoint'],0.)
    cov_values=[];adm_values=[];tt_cov=[];tt_adm=[];gauge_cov=[];gauge_adm=[]
    endpoints=[]
    for i in range(cells+1):
        A,H,sigma,q,I=state;a=math.exp(A);b=-2*I/(a*a)
        args=dict(a=a,Ap=H,sigp=q,F=-1.,Fp=0.,G=0.,Gp=0.,b=b,bp=-2-2*H*b,s=0.,sp=0.,B=B)
        raw=currents(**args)
        cov_values.append(raw['covariant_bulk_Z']);adm_values.append(raw['canonical_adm_bulk_Z'])
        tt=currents(**(args|dict(F=0.,b=0.,bp=0.,t=1.)))
        tt_cov.append(tt['covariant_bulk_Z']);tt_adm.append(tt['canonical_adm_bulk_Z'])
        # Normal gauge parameter zeta=sin(pi y/L), with both endpoints zero.
        y=i*length/cells;zeta=math.sin(math.pi*i/cells);zetap=math.pi/length*math.cos(math.pi*i/cells)
        zetapp=-(math.pi/length)**2*zeta;Hp=-q*q/(3*B);qp=mu*mu*sigma-4*H*q
        gauge=currents(**(args|dict(F=H*zeta,Fp=Hp*zeta+H*zetap,G=zetap,Gp=zetapp,
                                  b=zeta,bp=zetap,s=q*zeta,sp=qp*zeta+q*zetap)))
        gauge_cov.append(gauge['covariant_bulk_Z']);gauge_adm.append(gauge['canonical_adm_bulk_Z'])
        if i in (0,cells):
            endpoints.append(dict(a=a,b=b,F=-1.,G=0.,B=B))
        if i<cells:state=rk4(state,length/cells,rhs)
    def simpson(values):
        return length/cells/3*(values[0]+values[-1]+4*math.fsum(values[1:-1:2])+2*math.fsum(values[2:-1:2]))
    I=state[4];unit=B*I
    cov_bulk=simpson(cov_values);adm_bulk=simpson(adm_values)
    cov_corner=boundary_covariant_C_Z(**endpoints[1])-boundary_covariant_C_Z(**endpoints[0])
    tilt=lambda e:-3*e['B']*e['a']**2*e['F']*e['b']
    adm_corner=tilt(endpoints[1])-tilt(endpoints[0])
    observed=dict(covariant_bulk_Z=cov_bulk/unit,covariant_corner_Z=cov_corner/unit,
                  ADM_bulk_Z=adm_bulk/unit,ADM_corner_Z=adm_corner/unit,
                  covariant_complete_Z=(cov_bulk+cov_corner)/unit,
                  ADM_complete_Z=(adm_bulk+adm_corner)/unit,
                  covariant_N=(cov_bulk+cov_corner)/(2*unit),ADM_N=(adm_bulk+adm_corner)/(2*unit),
                  TT_plus_covariant_Z=simpson(tt_cov)/unit,TT_plus_ADM_Z=simpson(tt_adm)/unit,
                  endpoint_zero_gauge_covariant_Z=simpson(gauge_cov)/unit,
                  endpoint_zero_gauge_ADM_Z=simpson(gauge_adm)/unit)
    target=dict(covariant_bulk_Z=-2.,covariant_corner_Z=-4.,ADM_bulk_Z=0.,ADM_corner_Z=-6.,
                covariant_complete_Z=-6.,ADM_complete_Z=-6.,covariant_N=-3.,ADM_N=-3.,
                TT_plus_covariant_Z=.5,TT_plus_ADM_Z=.5,
                endpoint_zero_gauge_covariant_Z=0.,endpoint_zero_gauge_ADM_Z=0.)
    errors={key:observed[key]-target[key] for key in target}
    assert max(abs(v) for v in errors.values())<2e-5,(cells,errors)
    return dict(cells=cells,I_integrated=I,I_relative_background_difference=I/case['I']-1,
                observed_in_units_BI=observed,analytic_expected_in_units_BI=target,
                differences=errors,max_absolute_difference=max(abs(v) for v in errors.values()))


def main():
    input_path=BASE/'t1_background_replay.json'
    data=json.loads(input_path.read_text(encoding='utf-8'))
    cases=[]
    for case in data['cases']:
        background=case['background']
        if background['v']!=.3:continue
        runs=[integrate(background,cells) for cells in (64,128,256)]
        assert runs[-1]['max_absolute_difference']<1e-7
        cases.append(dict(lambda_brane=background['lambda_brane'],v=.3,L=background['L'],runs=runs))
    report=dict(scope='Independent component-current contractions integrated on three fixed-action backgrounds at three resolutions. Raw X1 is outside the full boundary domain; its negative evaluated form is not a physical ghost norm.',
                checks_passed=True,background_cases=3,currents=['covariant Theta with GHY C','canonical ADM with tilt'],
                cases=cases,source_sha256={input_path.name:hashlib.sha256(input_path.read_bytes()).hexdigest(),
                    'covariant_adm_current.py':hashlib.sha256(Path(sys.modules['covariant_adm_current'].__file__).read_bytes()).hexdigest(),
                    't1_background_replay.py':hashlib.sha256((BASE/'t1_background_replay.py').read_bytes()).hexdigest()},
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    path=BASE/'t1_integrated_norms.json';path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps({'checks':'PASS','backgrounds':len(cases),'grids_per_background':3,
                      'maximum_finest_grid_difference':max(c['runs'][-1]['max_absolute_difference'] for c in cases),
                      'X1_N_in_units_Mbar_squared':-3,'X1_is_admissible':False}))


if __name__=='__main__':main()
