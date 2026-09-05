"""Reproduce the x=1,3 checks supplementing the x=2 reference scan."""
import json
from pathlib import Path
from model import evaluate

if __name__=='__main__':
    results=[]
    for x,eps in [(1.,.05),(1.,.4),(3.,.05),(3.,.4)]:
        r=evaluate(x,eps,count=3)
        results.append(r)
        print(json.dumps(r),flush=True)
    out=Path(__file__).resolve().parents[1]/'resultats'/'extension_x_recalcule.json'
    out.write_text(json.dumps(results,indent=2),encoding='utf-8')
