"""Re-solve the documented models in a fresh workspace; never overwrite references."""
from pathlib import Path
import argparse,concurrent.futures,datetime,hashlib,json,math,os,shutil,subprocess,sys,time,uuid
ROOT=Path(__file__).resolve().parents[1]


def compare(reference,actual,rtol,atol,path='$'):
    failures=[];count=0
    if isinstance(reference,bool) or reference is None:
        if actual!=reference:failures.append(path+': state changed')
    elif isinstance(reference,(int,float)) and not isinstance(reference,bool):
        count=1
        if not isinstance(actual,(int,float)) or not math.isfinite(float(actual)) or not math.isclose(float(reference),float(actual),rel_tol=rtol,abs_tol=atol):
            failures.append(f'{path}: reference={reference!r}, calculated={actual!r}')
    elif isinstance(reference,dict):
        if not isinstance(actual,dict) or set(reference)!=set(actual):return 0,[path+': object keys differ']
        for k,v in reference.items():
            n,f=compare(v,actual[k],rtol,atol,path+'.'+k);count+=n;failures+=f
    elif isinstance(reference,list):
        if not isinstance(actual,list) or len(reference)!=len(actual):return 0,[path+': list length differs']
        for i,(a,b) in enumerate(zip(reference,actual)):
            n,f=compare(a,b,rtol,atol,path+f'[{i}]');count+=n;failures+=f
    elif isinstance(reference,str):
        if reference!=actual:failures.append(path+': descriptive/input string changed')
    else:failures.append(path+': unsupported value')
    return count,failures


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--profile',choices=['article1','extensions','all'],default='article1')
    ap.add_argument('--destination',type=Path)
    ap.add_argument('--workers',type=int,default=2)
    args=ap.parse_args()
    if args.workers not in (1,2,3,4):ap.error('workers must be 1..4')
    config=json.loads((ROOT/'verification/reproduction_config.json').read_text(encoding='utf-8'))
    jobs=[j for j in config['jobs'] if args.profile=='all' or j['profile']==args.profile]
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    dest=(args.destination or ROOT/'work'/('reproduction-'+stamp+'-'+uuid.uuid4().hex[:8])).resolve()
    if dest==ROOT.resolve() or ROOT.resolve().is_relative_to(dest):raise ValueError('Destination must not be the repository or one of its ancestors.')
    if dest.exists():raise FileExistsError('Choose a new destination; previous runs are never overwritten.')
    dest.mkdir(parents=True)
    workspace=dest/'calculated';workspace.mkdir()
    for folder in ['noyau','matiere','extensions']:
        shutil.copytree(ROOT/folder,workspace/folder,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    # Remove only the expected newly copied output files, never directories.
    # This ensures a failed script cannot pass by retaining its reference copy.
    for job in jobs:
        copied=(workspace/job['result']).resolve()
        assert copied.is_relative_to(workspace.resolve()) and copied.is_file()
        copied.unlink()
    env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',PYTHONIOENCODING='utf-8',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
    def run(job):
        start=time.monotonic();log=dest/(job['id']+'.log')
        code=None;error=None;n=0;fail=[]
        with log.open('w',encoding='utf-8') as f:
            try:
                p=subprocess.run([sys.executable,str(workspace/job['script'])],cwd=workspace,env=env,stdout=f,stderr=subprocess.STDOUT,timeout=job.get('timeout_seconds',600))
                code=p.returncode
                if code==0:
                    reference=json.loads((ROOT/job['result']).read_text(encoding='utf-8'))
                    actual=json.loads((workspace/job['result']).read_text(encoding='utf-8'))
                    n,fail=compare(reference,actual,job['rtol'],job['atol'])
            except (subprocess.TimeoutExpired,OSError,ValueError) as exc:error=str(exc)
        out=dict(id=job['id'],script=job['script'],result=job['result'],return_code=code,error=error,
                 numeric_values_compared=n,rtol=job['rtol'],atol=job['atol'],differences=fail,
                 status='PASS' if code==0 and error is None and not fail else 'FAIL',seconds=round(time.monotonic()-start,3),
                 reference_sha256=hashlib.sha256((ROOT/job['result']).read_bytes()).hexdigest(),
                 script_sha256=hashlib.sha256((ROOT/job['script']).read_bytes()).hexdigest())
        print(json.dumps({k:out[k] for k in ['id','status','numeric_values_compared','seconds','error']},ensure_ascii=False),flush=True)
        return out
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:rows=list(pool.map(run,jobs))
    result=dict(profile=args.profile,status='PASS' if all(r['status']=='PASS' for r in rows) else 'FAIL',
        utc=stamp,python=sys.version.split()[0],jobs=rows,reference_files_overwritten=False,
        meaning='Re-executed numerical reproduction of specified models. No experimental or publication validation.')
    (dest/'REPRODUCTION_REPORT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'report':str(dest/'REPRODUCTION_REPORT.json')},ensure_ascii=False),flush=True)
    if result['status']!='PASS':sys.exit(1)


if __name__=='__main__':main()
