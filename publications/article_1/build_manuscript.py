"""Generate manuscript sources and compile the delivered PDF with a local TeX engine.

Use --engine to name a local pdfLaTeX or Tectonic executable. Tectonic can
download public TeX resources on first use; document compilation stays local.
Scientific text comes from manuscript.json.
"""
from pathlib import Path
import argparse,hashlib,importlib.util,json,math,os,re,shutil,subprocess,unicodedata

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--source',type=Path,default=HERE/'manuscript.json')
parser.add_argument('--output-dir',type=Path,default=HERE)
parser.add_argument('--engine',default='pdflatex')
args=parser.parse_args()
OUT=args.output_dir.resolve();OUT.mkdir(parents=True,exist_ok=True)
TMP=REPO/'work/article_1_render';TMP.mkdir(parents=True,exist_ok=True)
os.environ.setdefault('MPLCONFIGDIR',str(TMP/'mplcache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pypdf import PdfReader

paper=json.loads(args.source.read_text(encoding='utf-8'))
spec=importlib.util.spec_from_file_location('coefficient',REPO/'noyau/stabilisation/weak_coupling_quadratic.py')
coef=importlib.util.module_from_spec(spec);spec.loader.exec_module(coef)
figdir=OUT/'figures';figdir.mkdir(exist_ok=True)
xs=np.linspace(.2,5,320)
fig,axs=plt.subplots(1,2,figsize=(7.2,2.7),layout='constrained')
for stiffness,color,label in [(0,'#375e7b','affine comparison'),(1,'#bc742d',r'$\widehat\lambda=1$'),(20,'#477f66',r'$\widehat\lambda=20$'),(math.inf,'#71618b','rigid limit')]:
    vals=np.array([coef.coefficients(float(x),stiffness) for x in xs])
    for i in range(2):axs[i].plot(xs,vals[:,i],label=label,color=color,lw=1.5,ls='--' if math.isinf(stiffness) else '-')
axs[0].set(xlabel=r'$x=\mu L$',ylabel=r'$\kappa$',title='(a) Leading mass coefficient')
axs[1].set(xlabel=r'$x=\mu L$',ylabel=r'$c_\alpha$',title='(b) Leading residue coefficient')
for ax in axs:
    ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.16)
    ax.tick_params(labelsize=8);ax.legend(fontsize=7,frameon=False);ax.title.set_fontsize(9)
fig.savefig(figdir/'finite_stiffness.png',dpi=300)
fig.savefig(figdir/'finite_stiffness.svg');plt.close(fig)
caption='Leading coefficients at fixed dimensionless boundary stiffness. Increasing stiffness raises the mass coefficient and lowers the positive residue coefficient. Dashed curves refer to the limiting rigid boundary problem.'

greek=dict(zip('αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΥΦΨΩ',
              ['alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa','lambda','mu','nu','xi','pi','rho','sigma','tau','upsilon','phi','chi','psi','omega','Gamma','Delta','Theta','Lambda','Xi','Pi','Sigma','Upsilon','Phi','Psi','Omega']))
sup=dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾','0123456789+-=()'));sup.update({'ᴬ':'A','ᴸ':'L','ᵀ':'T','ᵞ':'y','ʸ':'y'})
sub=dict(zip('₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎','0123456789+-=()'));sub.update({'ᵣ':'r','ₘ':'m','ₙ':'n','ₛ':'s','ₜ':'t','ₐ':'a','ᵢ':'i','ᵦ':r'\beta'})
symbols={'′':r'{}^{\prime}','″':r'{}^{\prime\prime}','→':r'\to','↔':r'\leftrightarrow','≤':r'\leq','≥':r'\geq','≠':r'\ne','∞':r'\infty','∫':r'\int','∂':r'\partial','√':r'\sqrt{\vphantom{x}}','δ':r'\delta','∑':r'\sum','≈':r'\simeq','×':r'\times','∈':r'\in','ℒ':r'\mathcal{L}','Ω':r'\Omega','𝒟':r'\mathcal{D}','ℋ':r'\mathcal{H}','χ':r'\chi','⟨':r'\langle','⟩':r'\rangle','□':r'\Box','⋅':r'\cdot','−':'-','∝':r'\propto'}
symbols.update({'·':r'\cdot','∧':r'\wedge','ℓ':r'\ell','⁵':r'{}^5'})
escape={'&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','\\':r'\textbackslash{}','^':r'\textasciicircum{}'}
inline_math=json.loads((HERE/'inline_math.json').read_text(encoding='utf-8'))
inline_pattern=re.compile(r'(?<![A-Za-z])(?:'+'|'.join(re.escape(k) for k in sorted(inline_math,key=len,reverse=True))+r')(?![A-Za-z])')
def textext(text):
    text=text.replace('—','-').replace('–','-').replace('‑','-').replace('\u00a0',' ')
    out=[];i=0
    while i<len(text):
        inline=inline_pattern.match(text,i)
        if inline:
            out.append(r'\ensuremath{'+inline_math[inline.group()]+'}')
            i=inline.end();continue
        c=text[i]
        if i+1<len(text) and text[i+1] in ('\u0302','\u0304'):
            base='\\'+greek[c] if c in greek else c
            out.append(r'\ensuremath{'+('\\hat{' if text[i+1]=='\u0302' else '\\bar{')+base+'}}');i+=2;continue
        if c in sup or c in sub:
            mapping=sup if c in sup else sub;run=[]
            while i<len(text) and text[i] in mapping:run.append(mapping[text[i]]);i+=1
            # Source tables also use a superscript minus followed by ASCII digits.
            if mapping is sup and run==['-']:
                while i<len(text) and text[i] in '0123456789':run.append(text[i]);i+=1
            out.append(r'\ensuremath{{}'+('^' if mapping is sup else '_')+'{'+''.join(run)+'}}');continue
        if c in greek:out.append(r'\ensuremath{'+'\\'+greek[c]+'}')
        elif c in symbols:out.append(r'\ensuremath{'+symbols[c]+'}')
        elif c in escape:out.append(escape[c])
        elif ord(c)>127:
            # pdfLaTeX's UTF-8 text encoding supports accented Latin names.
            if 'LATIN' in unicodedata.name(c,'') or c in '’‘“”':out.append(c.replace('’',"'").replace('‘',"'").replace('“','``').replace('”',"''"))
            else:raise ValueError(f'Unmapped text character {c!r} U+{ord(c):04X}')
        else:out.append(c)
        i+=1
    converted=''.join(out)
    def citation(m):
        ids=[]
        for token in m.group(1).split(','):
            if '-' in token:
                a,b=map(int,token.split('-'));ids.extend(range(a,b+1))
            else:ids.append(int(token))
        return r'\cite{'+','.join('ref'+str(n) for n in ids)+'}'
    return re.sub(r'\[(\d+(?:[-,]\d+)*)\]',citation,converted)

tex=[r'\documentclass[11pt,a4paper]{article}',r'\usepackage[T1]{fontenc}',r'\usepackage[utf8]{inputenc}',r'\usepackage{lmodern}',r'\usepackage[margin=24mm]{geometry}',r'\usepackage{amsmath,amssymb,graphicx,booktabs,array,microtype,hyperref}',r'\hypersetup{colorlinks=true,linkcolor=black,citecolor=blue,urlcolor=blue}',r'\setlength{\emergencystretch}{2em}',r'\title{'+textext(paper['title'])+'}',r'\author{'+textext(paper['author'])+'}',r'\date{7 September 2026}',r'\begin{document}',r'\maketitle',r'\begin{abstract}',textext(paper['abstract']),r'\end{abstract}']
md=['# '+paper['title'],'',paper['author'],'',paper['date'],'','## Abstract','',paper['abstract'],'']
equations=[]
for section in paper['sections']:
    tex.append(r'\section*{'+textext(section['title'])+'}')
    md+=['## '+section['title'],'']
    for block in section['blocks']:
        kind=block['type']
        if kind=='paragraph':tex += [textext(block['text']),''];md += [block['text'],'']
        elif kind=='equation':
            equations.append(block['number'])
            eq=block['latex']
            tex += [r'\begin{equation}',eq+r'\tag{'+block['number']+'}',r'\end{equation}']
            md += ['$$',block['latex']+r'\tag{'+block['number']+'}','$$','']
        elif kind=='table':
            n=len(block['headers'])
            tex += [r'\begin{table}[htbp]',r'\centering\small',r'\begin{tabular}{'+'c'*n+'}',r'\toprule',' & '.join(textext(str(x)) for x in block['headers'])+r'\\',r'\midrule']
            tex += [' & '.join(textext(str(x)) for x in row)+r'\\' for row in block['rows']]
            tablecaption=re.sub(r'^Table \d+\.\s*','',block['caption'])
            tex += [r'\bottomrule',r'\end{tabular}',r'\caption{'+textext(tablecaption)+'}',r'\end{table}']
            md += ['| '+' | '.join(block['headers'])+' |','| '+' | '.join(['---']*n)+' |']
            md += ['| '+' | '.join(map(str,row))+' |' for row in block['rows']]+['',block['caption'],'']
    if section['title'].startswith('5.'):
        tex += [r'\begin{figure}[htbp]',r'\centering\includegraphics[width=\linewidth]{figures/finite_stiffness.png}',r'\caption{'+textext(caption)+'}',r'\end{figure}']
        md += ['![Finite-stiffness coefficients](figures/finite_stiffness.png)','',caption,'']
tex += [r'\begin{thebibliography}{99}'];md += ['## References','']
for number,ref in enumerate(paper['references'],1):
    body=textext(ref['text'])
    # Active DOI links use literal URLs in href, preserving identifier punctuation.
    match=re.search(r'DOI: ([^ ]+)',ref['text'])
    if match:
        doi=match.group(1).rstrip('.')
        body=body.replace(textext(doi),r'\href{https://doi.org/'+doi+'}{'+textext(doi)+'}',1)
    elif ref.get('url'):body+=' '+r'\url{'+ref['url']+'}'
    tex += [r'\bibitem{ref'+str(number)+'} '+body]
    md += ['['+str(number)+'] '+ref['text'],'']
tex += [r'\end{thebibliography}',r'\end{document}']
(OUT/'manuscript.tex').write_text('\n'.join(tex)+'\n',encoding='utf-8',newline='\n')
(OUT/'manuscript.md').write_text('\n'.join(md)+'\n',encoding='utf-8',newline='\n')
engine=shutil.which(args.engine) or (str(Path(args.engine).resolve()) if Path(args.engine).is_file() else None)
if not engine:raise RuntimeError('A local pdfLaTeX or Tectonic engine is required. Sources were generated but no PDF was compiled.')
engine=str(Path(engine).resolve())
env=os.environ.copy();env['PATH']=str(Path(engine).parent)+os.pathsep+env.get('PATH','')
env['TEXMFVAR']=str(TMP/'texmf-var');env['TEXMFCONFIG']=str(TMP/'texmf-config')
tectonic='tectonic' in Path(engine).name.lower()
env['TECTONIC_CACHE_DIR']=str(TMP/'tectonic_cache')
passes=1 if tectonic else 3
for attempt in range(passes):
    command=([engine,'-X','compile','--keep-logs','--keep-intermediates','--untrusted','manuscript.tex'] if tectonic else [engine,'-interaction=nonstopmode','-halt-on-error','-file-line-error','-no-shell-escape','manuscript.tex'])
    result=subprocess.run(command,cwd=OUT,env=env,capture_output=True,text=True,errors='replace')
    (TMP/f'compile-pass-{attempt+1}.txt').write_text(result.stdout+result.stderr,encoding='utf-8')
    if result.returncode:raise RuntimeError('TeX compilation failed: '+(result.stdout+result.stderr)[-3500:])
log=(OUT/'manuscript.log').read_text(encoding='utf-8',errors='replace')
issues=re.findall(r'(?:Overfull \\[hv]box[^\n]*|LaTeX Warning:[^\n]*|Package hyperref Warning:[^\n]*|Missing character:[^\n]*)',log)
reader=PdfReader(OUT/'manuscript.pdf')
report=dict(engine='Tectonic (XeTeX)' if tectonic else 'pdfLaTeX',engine_version=subprocess.run([engine,'--version'],capture_output=True,text=True).stdout.splitlines()[0],passes='automatic convergence reruns' if tectonic else 3,pages=len(reader.pages),equations=len(equations),references=len(paper['references']),warnings=issues,source_sha256=hashlib.sha256(args.source.read_bytes()).hexdigest(),pdf_sha256=hashlib.sha256((OUT/'manuscript.pdf').read_bytes()).hexdigest(),visual_review_required=True)
(TMP/'render_report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
