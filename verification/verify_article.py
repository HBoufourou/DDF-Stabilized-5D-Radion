"""Check manuscript tables against recorded results and verify independent checks.

This validates transcription and numerical consistency, not physical reality.
The algebra and spectral equations are documented separately.
"""
from pathlib import Path
import json, math

ROOT=Path(__file__).resolve().parents[1]
def read(name):return json.loads((ROOT/name).read_text(encoding='utf-8'))
article=read('article/manuscript.json')
tables=[b for s in article['sections'] for b in s['blocks'] if b['type']=='table']
assert len(tables)==4
equations=[b for s in article['sections'] for b in s['blocks'] if b['type']=='equation']
assert len(equations)==40
tex=(ROOT/'article/manuscript.tex').read_text(encoding='utf-8')
assert all(e['latex'] in tex for e in equations), 'LaTeX and structured equations differ'
assert len(article['references'])==12
for row in tables[0]['rows']:
    x,k,c,r=map(float,row);T=math.tanh(x/2);C=math.cosh(x/2)**2
    expected_k=4*x*T/C;expected_c=(1+T*T+2*T/x)/C
    assert abs(k-expected_k)<5.1e-9 and abs(c-expected_c)<5.1e-9
    assert abs(r-expected_c/expected_k)<5.1e-9
ref=read('resultats/spectre_5d.json')[:6]
for row,r in zip(tables[1]['rows'],ref):
    e,m,a,lr,lt,at=map(float,row)
    assert e==r['epsilon']
    s=r['scalar_modes'][0];t=r['tensor_modes'][0]
    assert abs(m-s['mL'])<5.1e-7
    assert abs(a-s['alpha_scalar_conditional_archive_norm'])<5.1e-7
    assert abs(lr-math.pi*8.2/s['mL'])<5.1e-4
    assert abs(lt-math.pi*8.2/t['mL'])<5.1e-4
    assert abs(at-t['alpha_tensor'])<5.1e-7
ext=read('resultats/extension_x.json')
for row,r in zip(tables[2]['rows'],ext):
    x,e,m,a=map(float,row)
    assert (x,e)==(r['x'],r['epsilon'])
    assert abs(m-r['scalar_modes'][0]['mL'])<5.1e-10
    assert abs(a-r['scalar_modes'][0]['alpha'])<5.1e-10
fem=read('resultats/fem_verification.json')
assert len(fem)==5 and all(c['finite_element_crosscheck_passed'] for r in fem for c in r['comparison'])
for row in tables[3]['rows']:
    n,m,a=map(float,row)
    r=next(v for v in fem[0]['runs'] if v['elements']==n)['scalar_modes'][0]
    assert abs(m-r['mL'])<5.1e-12 and abs(a-r['alpha'])<5.1e-12
for c in fem[0]['comparison']:
    assert abs(c['mass_convergence_order_last_three']-2)<.001
    assert abs(c['alpha_convergence_order_last_three']-2)<.001
for r in ext:
    assert abs(r['constraint_residual'])<1.6e-10
    assert all(abs(s['norm_identity_relative_residual'])<3.2e-10 for s in r['scalar_modes'])
print(json.dumps({'status':'PASS','tables':4,'equations':40,'references':12,'fem_points':5,
 'scope':'Manuscript transcription, recorded spectral checks, and main-benchmark convergence.'},indent=2))
