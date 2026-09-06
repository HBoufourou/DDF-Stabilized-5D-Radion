"""Read-only integrity and recorded-result checks for the canonical DDF folder.

No equations are re-solved here. Integrity is not scientific validation.
"""
from pathlib import Path, PurePosixPath
import ast, hashlib, json, re, zipfile, csv, math

ROOT=Path(__file__).resolve().parents[1]

def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def contained(relative):
    q=PurePosixPath(relative)
    assert not q.is_absolute() and '..' not in q.parts and ':' not in relative
    path=(ROOT/relative).resolve()
    assert path.is_relative_to(ROOT.resolve())
    return path

def active_files():
    return [p for p in ROOT.rglob('*') if p.is_file() and
            not any(x in p.relative_to(ROOT).parts for x in ('work','__pycache__','.git')) and p.suffix!='.pyc']

def markdown_targets(text):
    text=re.sub(r'```[\s\S]*?```','',text)
    text=re.sub(r'`[^`]*`','',text)
    text=re.sub(r'\\\([\s\S]*?\\\)','',text)
    text=re.sub(r'\\\[[\s\S]*?\\\]','',text)
    text=re.sub(r'\$\$[\s\S]*?\$\$','',text)
    return re.findall(r'(?<!\\)\]\(([^)]+)\)',text)

def validate_article():
    folder=ROOT/'publications/article_1'
    paper=read(folder/'manuscript.json')
    blocks=[b for s in paper['sections'] for b in s['blocks']]
    eqs=[b for b in blocks if b['type']=='equation']
    ids=[b['number'] for b in eqs]
    assert len(ids)==len(set(ids))==36
    tex=(folder/'manuscript.tex').read_text(encoding='utf-8')
    md=(folder/'manuscript.md').read_text(encoding='utf-8')
    assert re.findall(r'\\tag\{([^}]+)\}',tex)==ids
    assert re.findall(r'\\tag\{([^}]+)\}',md)==ids
    for b in blocks:
        if b['type']=='paragraph':assert b['text'] in md,'Generated article text has drifted.'
        if b['type']=='equation':assert b['latex'] in tex and b['latex'] in md
    assert len(paper['references'])==20
    assert len(re.findall(r'@article\{',(folder/'references.bib').read_text(encoding='utf-8')))==20
    tables=[b for b in blocks if b['type']=='table'];assert len(tables)==4
    coeff=read(ROOT/'noyau/stabilisation/weak_coupling_quadratic.json')
    expected=[]
    for r in coeff['rows']:
        if r['x']==2 and r['lambda_hat'] in (0.,1.,20.,'infinity'):
            expected.append(['rigid' if r['lambda_hat']=='infinity' else str(int(r['lambda_hat'])),f"{r['kappa']:.9f}",f"{r['c_alpha']:.9f}"])
    assert tables[1]['rows']==expected
    data=read(ROOT/'noyau/stabilisation/radion_comparison.json')
    expected=[]
    for r in data['cases']:
        m=r['runs'][-1]['modes'][0]
        expected.append([f"{r['epsilon']:.2f}",'rigid' if r['lambda_hat'] is None else str(int(r['lambda_hat'])),f"{m['mL']:.6f}",f"{m['alpha']:.6f}",f"{math.pi*3/m['mL']:.4f}"])
    assert tables[2]['rows']==expected
    curve=read(ROOT/'noyau/courbure/courbure_action_fixe.json')
    flat=next(r for r in curve['flat_reference'] if r['inputs']['v']==.3)
    assert abs(float(tables[3]['rows'][1][1])-flat['L'])<5e-12
    for sign,i in [(-1,0),(1,2)]:
        row=next(r for r in curve['fixed_tension_solutions'] if r['inputs']['v']==.3 and math.isclose(r['delta_tau_each'],sign*9e-6,rel_tol=1e-10))
        assert abs(float(tables[3]['rows'][i][1])-row['L'])<5e-12
        val=tables[3]['rows'][i][2].replace('×10⁻6','e-6')
        assert math.isclose(float(val),row['h_brane'],rel_tol=5e-10)
    return dict(equations=len(ids),tables=len(tables),references=len(paper['references']))

def validate_t1():
    """Validate recorded evidence and its hashes, without replacing the replay."""
    folder=ROOT/'noyau/T1_Z_LIGHT'
    report=read(ROOT/'verification/T1_REPLAY_EXECUTED.json')
    names=['null_boundary_checks','covariant_adm_current','adm_component_referee',
           't1_background_replay','t1_integrated_norms']
    assert report['verdict']=='GREEN' and report['checks_passed']
    assert report['full_DDF_closed'] is False and report['experimental_validation'] is False
    assert [j['id'] for j in report['jobs']]==names
    for job in report['jobs']:
        assert job['status']=='PASS' and job['return_code']==0 and not job['differences']
        for extension,key in [('py','script_sha256'),('json','reference_sha256')]:
            assert hashlib.sha256((folder/(job['id']+'.'+extension)).read_bytes()).hexdigest()==job[key]
    exact=read(folder/'null_boundary_checks.json')
    assert len(exact['checks'])==29 and all(v=='PASS' for v in exact['checks'].values())
    covariance=read(folder/'covariant_adm_current.json')
    assert covariance['random_component_checks']==100
    assert covariance['maximum_current_divergence_residual']<1e-10
    adm=read(folder/'adm_component_referee.json')
    assert adm['checks_passed'] and adm['random_component_comparisons']==128
    assert adm['maximum_absolute_difference']<1e-10
    backgrounds=read(folder/'t1_background_replay.json')
    assert backgrounds['checks_passed'] and len(backgrounds['cases'])==9
    assert backgrounds['X1_verdict']=='EXCLUDED_BY_FULL_ISRAEL_BOUNDARY_CONDITION'
    integrated=read(folder/'t1_integrated_norms.json')
    assert integrated['checks_passed'] and integrated['background_cases']==3
    for name,digest in integrated['source_sha256'].items():
        assert '/' not in name and '\\' not in name
        assert hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest
    for name,data in [('t1_background_replay',backgrounds),('t1_integrated_norms',integrated)]:
        assert hashlib.sha256((folder/(name+'.py')).read_bytes()).hexdigest()==data['script_sha256']
    history=read(ROOT/'audits/T1_sources/SOURCES.json')
    for source in history['sources']:
        data=(ROOT/'audits/T1_sources'/source['filename']).read_bytes()
        assert len(data)==source['bytes'] and hashlib.sha256(data).hexdigest()==source['sha256']
    return dict(verdict='GREEN_IN_DECLARED_DOMAIN',executed_programs=5,
                exact_checks=29,backgrounds=9,integrated_backgrounds=3,full_DDF_closed=False)

def main():
    manifest=read(ROOT/'MANIFEST.json')
    seen=set()
    for row in manifest['files']:
        assert row['path'] not in seen;seen.add(row['path'])
        p=contained(row['path']);data=p.read_bytes()
        assert len(data)==row['bytes'],f'Size changed: {row["path"]}'
        assert hashlib.sha256(data).hexdigest()==row['sha256'],f'Hash changed: {row["path"]}'
    actual={p.relative_to(ROOT).as_posix() for p in active_files() if p!=ROOT/'MANIFEST.json'}
    assert actual==seen,dict(unlisted=sorted(actual-seen),missing=sorted(seen-actual))
    claims=read(ROOT/'registre_revendications.json')['claims']
    assert len(set(c['id'] for c in claims))==len(claims)
    assert all(contained(c['evidence']).is_file() for c in claims)
    assert all(contained(e).is_file() for c in claims for e in c.get('additional_evidence',[]))
    model=read(ROOT/'MODELE.json')
    assert model['name']=='DDF-Stabilized-5D-Radion'
    scripts=[p for p in active_files() if p.suffix=='.py' and 'historique' not in p.relative_to(ROOT).parts]
    for p in scripts:ast.parse(p.read_text(encoding='utf-8-sig'),filename=str(p))
    links=0
    for p in [p for p in active_files() if p.suffix=='.md' and 'historique' not in p.relative_to(ROOT).parts]:
        for target in markdown_targets(p.read_text(encoding='utf-8')):
            if target.startswith(('https://','http://','#')):continue
            local=(p.parent/target.split('#')[0]).resolve()
            assert local.is_relative_to(ROOT.resolve()) and local.exists(),(p.name,target)
            links+=1
    # Only the corrected edition is distributed. Old source registers are audit
    # evidence; complete superseded editions and manuscripts stay in local backups.
    assert not (ROOT/'historique').exists(), 'Superseded editions must remain outside the current publication.'
    curved=read(ROOT/'noyau/courbure/courbure_action_fixe.json')
    assert len(curved['fixed_tension_solutions'])==12
    assert max(abs(r['linear_curvature_response_identity_relative_error']) for r in curved['flat_reference'])<1e-9
    assert abs(curved['bracketed_crosscheck']['relative_difference'])<1e-6
    phi=read(ROOT/'matiere/Phi/phi_projection.json')
    halo=read(ROOT/'extensions/RAR/halo_hydrostatic.json')
    chi=read(ROOT/'extensions/RAR/halo_chi_boundary.json')
    assert phi['checks_passed'] and halo['checks_passed']
    assert sum(len(c['charged_stationary_profiles']) for c in phi['cases'])==12
    assert len(halo['cases'])==27 and len(chi['cases'])==3
    assert all(c['boundary_numerically_resolved'] for c in chi['cases'])
    assert all(c['chi_prime_surface']!=0 for c in chi['cases']), 'Do not erase unresolved boundary derivatives.'
    source=read(ROOT/'noyau/relations_spectrales/principles_calculs.json')
    for name,digest in source['source_sha256'].items():
        data=(ROOT/'noyau/relations_spectrales/input_data'/name).read_bytes()
        assert hashlib.sha256(data).hexdigest()==digest
    # Reject non-standard NaN/Infinity in active machine-readable records.
    for p in [p for p in active_files() if p.suffix=='.json' and 'historique' not in p.relative_to(ROOT).parts]:
        json.loads(p.read_text(encoding='utf-8-sig'),parse_constant=lambda c:(_ for _ in ()).throw(ValueError((p,c))))
    coeff=read(ROOT/'noyau/stabilisation/weak_coupling_quadratic.json')
    assert coeff['checks_passed'] and len(coeff['rows'])==35
    spec=read(ROOT/'noyau/stabilisation/radion_comparison.json')
    assert spec['checks_passed'] and len(spec['cases'])==12
    local=read(ROOT/'extensions/RAR/local_coupling_checks.json');assert all(local['validation'].values())
    with (ROOT/'audits/CORRESPONDANCE_ANCIENS_REGISTRES.csv').open(encoding='utf-8-sig',newline='') as f:oldmap=list(csv.DictReader(f))
    old1=read(ROOT/'audits/sources_registres/registre_DDFU.json')
    old1=old1['claims'] if isinstance(old1,dict) and 'claims' in old1 else old1
    assert len(oldmap)==50 and len({r['id_ancien'] for r in oldmap})==50
    active_ids={c['id'] for c in claims}
    for row in oldmap:
        targets=re.findall(r'\b(?:[CFMGRUSA]\d{2})\b',row['ids_actifs_pertinents'])
        assert all(t in active_ids for t in targets)
    before=read(ROOT/'audits/COMPTES_CORRESPONDANCE.json')
    assert len(old1)==18
    with (ROOT/'audits/sources_registres/CLAIMS_V3.csv').open(encoding='utf-8-sig',newline='') as f:old2=list(csv.DictReader(f))
    assert len(old2)==32
    oldids={r['id'] for r in old1}|{r.get('id',r.get('ID')) for r in old2}
    assert oldids=={r['id_ancien'] for r in oldmap}
    report=read(ROOT/'verification/REPRODUCTION_EXECUTEE.json')
    assert report['status']=='PASS' and len(report['jobs'])==9
    for job in report['jobs']:
        assert job['status']=='PASS'
        assert hashlib.sha256((ROOT/job['result']).read_bytes()).hexdigest()==job['reference_sha256']
        assert hashlib.sha256((ROOT/job['script']).read_bytes()).hexdigest()==job['script_sha256']
    article=validate_article()
    t1=validate_t1()
    print(json.dumps(dict(integrity='PASS',recorded_results_consistency='PASS',
       manifest_files=len(seen),active_claims=len(claims),parsed_active_scripts=len(scripts),
       checked_navigation_links=links,superseded_editions_in_current_tree=False,
       old_claims_mapped=len(oldmap),executed_reproductions=len(report['jobs']),T1=t1,article=article,
       scientific_or_experimental_validation=False,repository='DDF-Stabilized-5D-Radion'),indent=2))

if __name__=='__main__':main()
