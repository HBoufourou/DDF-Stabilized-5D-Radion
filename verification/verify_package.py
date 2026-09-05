"""Verify packaging integrity and consistency of archived numerical checks.
This is not a physical validation, an eigenvalue solver or an exclusion test.
Standard-library Python only. Numerical recalculation is separate.
"""
from pathlib import Path
import hashlib
import json
import math
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
errors=[]
def check(condition,message):
    if not condition:
        errors.append(message)

def contained(rel):
    p=(ROOT/rel).resolve()
    check(p.is_relative_to(ROOT),'Path outside package: '+str(rel))
    return p

manifest=json.loads((ROOT/'MANIFEST.json').read_text(encoding='utf-8'))
for item in manifest['files']:
    p=contained(item['path'])
    if not p.is_file():
        errors.append('Missing file: '+item['path'])
        continue
    data=p.read_bytes()
    check(hashlib.sha256(data).hexdigest()==item['sha256'],'Hash mismatch: '+item['path'])
    check(len(data)==item['bytes'],'Size mismatch: '+item['path'])

claims=json.loads((ROOT/'registre_revendications.json').read_text(encoding='utf-8'))['claims']
check(len({c['id'] for c in claims})==len(claims),'Duplicate claim ids')
for claim in claims:
    check(contained(claim['evidence']).is_file(),'Missing evidence: '+claim['id'])

rows=json.loads((ROOT/'resultats/spectre_5d.json').read_text(encoding='utf-8'))
check(len(rows)==7,'Reference data must have six parameter points and one refined repeat')
for row in rows:
    check(math.isfinite(row['epsilon']),'Nonfinite epsilon')
    check(abs(row['background_constraint_max_residual'])<1e-8,'Archived background residual too large')
    check(len(row['scalar_modes'])==3,'Expected three archived scalar modes')
    for s in row['scalar_modes']:
        check(math.isfinite(s['mL']) and s['mL']>0,'Invalid recorded positive scalar root')
        check(abs(s['energy_identity_relative_residual'])<1e-8,'Archived energy residual too large')
        check(abs(s['boundary_residual'])<1e-8,'Archived boundary residual too large')
        check(s['alpha_scalar_conditional_archive_norm']>0,'Invalid scalar amplitude')
        expected=math.pi*8.2/s['mL']
        check(abs(s['lambda_um_if_L_equals_pi_times_8p2_um']-expected)<1e-9,'Range conversion mismatch')
    check(len(row['tensor_modes'])>=1,'Missing archived tensor mode')

if len(rows)==7:
    a,b=rows[3],rows[6]
    check(a['epsilon']==b['epsilon']==.53,'Refined point mismatch')
    for ma,mb in zip(a['scalar_modes'],b['scalar_modes']):
        check(abs(ma['mL']-mb['mL'])<1e-8,'Archived tolerance check inconsistent')

for name in ['README.md','ETAT_SCIENTIFIQUE.md','DEVELOPPEMENT.md','CORRECTIONS_APPLIQUEES.md',
             'noyau/EFT_MODELE_ET_RESULTATS.md','noyau/GEOMETRIE.md']:
    p=ROOT/name
    text=p.read_text(encoding='utf-8')
    check(not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',text),'Control character in '+name)
    for dest in re.findall(r'\]\(([^)]+)\)',text):
        if dest.startswith(('http:','https:','#')):
            continue
        check((p.parent/dest).resolve().exists(),'Broken local link '+name+': '+dest)

report={
 'status':'PASS' if not errors else 'FAIL',
 'meaning':'Package integrity and archived numerical consistency only; no physical or experimental validation.',
 'manifest_file_count':len(manifest['files']),
 'claim_count':len(claims),
 'recorded_parameter_rows':len(rows),
 'errors':errors}
(ROOT/'verification/RESULTAT_VERIFICATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
sys.exit(bool(errors))
