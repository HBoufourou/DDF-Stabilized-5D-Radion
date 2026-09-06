"""Re-execute the complete documented T1 replay in a new work directory.

GREEN is scoped to the analytic domain in VERDICT_T1.md. Execution failure
returns INCONCLUSIVE, never a fabricated physical RED or GREEN verdict.
"""
from pathlib import Path
import argparse, datetime, hashlib, json, math, os, shutil, subprocess, sys, time, uuid

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
JOBS=['null_boundary_checks','covariant_adm_current','adm_component_referee',
      't1_background_replay','t1_integrated_norms']


def compare(a,b,path='$'):
    if isinstance(a,bool) or a is None:
        return [] if a==b else [path+': state mismatch']
    if isinstance(a,(int,float)):
        return [] if isinstance(b,(int,float)) and math.isfinite(b) and math.isclose(a,b,rel_tol=1e-9,abs_tol=1e-10) else [path+': number mismatch']
    if isinstance(a,dict):
        if not isinstance(b,dict) or set(a)!=set(b):return [path+': keys mismatch']
        return [failure for key in a for failure in compare(a[key],b[key],path+'.'+key)]
    if isinstance(a,list):
        if not isinstance(b,list) or len(a)!=len(b):return [path+': list mismatch']
        return [failure for i,(x,y) in enumerate(zip(a,b)) for failure in compare(x,y,path+f'[{i}]')]
    return [] if a==b else [path+': value mismatch']


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--destination',type=Path);args=parser.parse_args()
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    target=(args.destination or ROOT/'work'/('t1-'+stamp+'-'+uuid.uuid4().hex[:8])).resolve()
    if target==ROOT.resolve() or ROOT.resolve().is_relative_to(target):raise ValueError('Choose a new workspace outside repository ancestors.')
    if target.exists():raise FileExistsError('Destination exists; choose a new path.')
    target.mkdir(parents=True)
    calc=target/'calculated';calc.mkdir()
    for name in JOBS:shutil.copyfile(HERE/(name+'.py'),calc/(name+'.py'))
    # Only scripts are copied. No reference output can mask an execution failure.
    env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',PYTHONIOENCODING='utf-8')
    rows=[]
    for name in JOBS:
        started=time.monotonic();script=HERE/(name+'.py');reference=HERE/(name+'.json')
        error=None;differences=[];code=None
        with (target/(name+'.log')).open('w',encoding='utf-8') as log:
            try:
                result=subprocess.run([sys.executable,str(calc/(name+'.py'))],cwd=calc,stdout=log,stderr=subprocess.STDOUT,env=env,timeout=300)
                code=result.returncode
                if code==0:
                    actual=json.loads((calc/(name+'.json')).read_text(encoding='utf-8'))
                    expected=json.loads(reference.read_text(encoding='utf-8'))
                    differences=compare(expected,actual)
            except (OSError,ValueError,subprocess.TimeoutExpired) as exc:error=str(exc)
        row=dict(id=name,status='PASS' if code==0 and error is None and not differences else 'FAIL',
                 return_code=code,error=error,differences=differences,seconds=round(time.monotonic()-started,3),
                 script_sha256=hashlib.sha256(script.read_bytes()).hexdigest(),
                 reference_sha256=hashlib.sha256(reference.read_bytes()).hexdigest())
        rows.append(row);print(json.dumps({k:row[k] for k in ('id','status','seconds')}),flush=True)
        if row['status']!='PASS':break
    passed=len(rows)==len(JOBS) and all(r['status']=='PASS' for r in rows)
    report=dict(verdict='GREEN' if passed else 'INCONCLUSIVE',checks_passed=passed,
                domain='Linear propagating perturbations of the minimal smooth flat interval, B>0, sigma_prime nonzero, D_i=W_i+eta_i U_i_second nonzero; massive positivity also requires eta_i W_i+U_i_second>0; vacuum matter and the declared boundary gauge quotient.',
                X1='Outside the complete Israel boundary domain; the reproduced negative form is not a physical ghost norm.',
                full_DDF_closed=False,experimental_validation=False,reference_files_overwritten=False,
                python=sys.version.split()[0],utc=stamp,jobs=rows)
    (target/'T1_REPLAY_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'T1':report['verdict'],'report':str(target/'T1_REPLAY_REPORT.json'),'full_DDF_closed':False}),flush=True)
    if not passed:sys.exit(1)


if __name__=='__main__':main()
