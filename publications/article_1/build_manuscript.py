"""Render one structured manuscript to Markdown, LaTeX and PDF.

Run from an installed Python environment with requirements-article.txt.
Outputs default to this script's directory; scratch files stay under work/.
"""
from pathlib import Path
import argparse,json,re,html,os,math,importlib.util

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,default=HERE)
ap.add_argument('--source',type=Path,default=HERE/'manuscript.json')
args=ap.parse_args();OUT=args.output_dir.resolve();OUT.mkdir(parents=True,exist_ok=True)
TMP=REPO/'work/article_1_render';TMP.mkdir(parents=True,exist_ok=True)
os.environ.setdefault('MPLCONFIGDIR',str(TMP/'mplcache'))
import matplotlib
matplotlib.use('Agg')
from matplotlib import mathtext,font_manager
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as PILImage
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Image,Table,TableStyle,KeepTogether
from pypdf import PdfReader

DATA=json.loads(args.source.read_text(encoding='utf-8'))
for name,family,weight in [('Body','DejaVu Serif','normal'),('BodyBold','DejaVu Serif','bold'),('Heading','DejaVu Sans','normal'),('HeadingBold','DejaVu Sans','bold')]:
    pdfmetrics.registerFont(TTFont(name,font_manager.findfont(FontProperties(family=family,weight=weight))))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='Body',boldItalic='BodyBold')
INK=colors.HexColor('#17232e');ACCENT=colors.HexColor('#214b66')
styles={
 'body':ParagraphStyle('body',fontName='Body',fontSize=9.3,leading=13.3,spaceAfter=7,textColor=INK),
 'abstract':ParagraphStyle('abstract',fontName='Body',fontSize=9.2,leading=13.2,spaceAfter=9,textColor=INK),
 'title':ParagraphStyle('title',fontName='BodyBold',fontSize=19,leading=24,spaceAfter=15,textColor=INK),
 'section':ParagraphStyle('section',fontName='HeadingBold',fontSize=11.5,leading=16,spaceBefore=15,spaceAfter=8,keepWithNext=True,textColor=ACCENT),
 'caption':ParagraphStyle('caption',fontName='Body',fontSize=8.3,leading=11.5,spaceBefore=6,spaceAfter=10,textColor=INK),
 'cell':ParagraphStyle('cell',fontName='Heading',fontSize=8,leading=11,alignment=1,textColor=INK),
 'ref':ParagraphStyle('ref',fontName='Body',fontSize=8.0,leading=10.6,spaceAfter=5,textColor=INK),
 'meta':ParagraphStyle('meta',fontName='Heading',fontSize=8.7,leading=12.5,spaceAfter=7,textColor=ACCENT)}
sup={c:t for c,t in zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾','0123456789+-=()')};sup.update({'ᴬ':'A','ᴸ':'L','ᵀ':'T'})
sub={c:t for c,t in zip('₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎','0123456789+-=()')};sub.update({'ᵣ':'r','ₘ':'m','ₙ':'n','ₛ':'s','ₜ':'t','ₐ':'a','ᵢ':'i'})
def para(text,style='body'):
    text=text.replace('—','-').replace('–','-').replace('‑','-').replace('𝒟','D').replace('ℋ','H')
    text=html.escape(text)
    text=''.join('<super>'+sup[c]+'</super>' if c in sup else '<sub>'+sub[c]+'</sub>' if c in sub else c for c in text)
    return Paragraph(text,styles[style])

equation_audit=[]
def eq(block):
    latex=block['latex'].replace(r'\Box_4',r'\partial_\mu\partial^\mu')
    latex=re.sub(r'\\frac\s*([0-9])\s*([0-9])',r'\\frac{\1}{\2}',latex)
    latex=re.sub(r'\\cal\s+([A-Za-z])',r'\\mathcal{\1}',latex)
    latex=re.sub(r'\\le\b',r'\\leq',latex)
    latex=re.sub(r'\\ge\b',r'\\geq',latex)
    f=TMP/('eq-'+block['number']+'.png')
    mathtext.math_to_image('$'+latex+'$',f,prop=FontProperties(size=11.6),dpi=320,format='png',color='#17232e')
    with PILImage.open(f) as im:w,h=im.size
    scale=min(72/320,455/w)
    equation_audit.append(dict(number=block['number'],font_scale=scale/(72/320),width_pt=w*scale,height_pt=h*scale))
    t=Table([[Image(str(f),width=w*scale,height=h*scale),para('('+block['number']+')','cell')]],colWidths=[458,32],hAlign='CENTER')
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE'),('ALIGN',(0,0),(0,0),'CENTER'),
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
    return t

figdir=OUT/'figures';figdir.mkdir(exist_ok=True)
module_path=REPO/'noyau/stabilisation/weak_coupling_quadratic.py'
spec=importlib.util.spec_from_file_location('ddf_weak',module_path);coef=importlib.util.module_from_spec(spec);spec.loader.exec_module(coef)
xs=np.linspace(.2,5,320)
fig,axs=plt.subplots(1,2,figsize=(7.2,2.7),layout='constrained')
for stiff,color,label in [(0,'#375e7b','affine'),(1,'#bc742d',r'$\widehat\lambda=1$'),(20,'#477f66',r'$\widehat\lambda=20$'),(math.inf,'#71618b','rigid')]:
    values=np.array([coef.coefficients(float(x),stiff) for x in xs])
    for j in range(2):axs[j].plot(xs,values[:,j],label=label,color=color,lw=1.5,ls='--' if math.isinf(stiff) else '-')
axs[0].set(xlabel=r'$x=\mu L$',ylabel=r'$\kappa$',title='(a) Leading mass coefficient')
axs[1].set(xlabel=r'$x=\mu L$',ylabel=r'$c_\alpha$',title='(b) Leading residue coefficient')
for ax in axs:
    ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.16);ax.tick_params(labelsize=8)
    ax.legend(fontsize=7,frameon=False);ax.title.set_fontsize(9)
fig.savefig(figdir/'finite_stiffness.png',dpi=300);fig.savefig(figdir/'finite_stiffness.svg');plt.close(fig)
figcaption='Figure 1. Analytic leading coefficients at fixed dimensionless boundary stiffness. Increasing stiffness raises the mass coefficient and lowers the positive residue coefficient. The dashed rigid curves are limiting boundary problems; no dimensional radius enters.'

# Export readable text and editable TeX from exactly the same blocks.
md=['# '+DATA['title'],'',DATA['author'],'',DATA['date'],'','## Abstract','',DATA['abstract'],'']
def textext(text):
    escapes={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}'}
    text=''.join(escapes.get(c,c) for c in text)
    text=text.replace('—','-').replace('–','-').replace('‑','-')
    def citations(m):
        nums=[]
        for piece in m.group(1).split(','):
            if '-' in piece:
                a,b=map(int,piece.split('-'));nums.extend(range(a,b+1))
            else:nums.append(int(piece))
        return r'\cite{'+','.join('ref'+str(n) for n in nums)+'}'
    return re.sub(r'\[(\d+(?:[-,]\d+)*)\]',citations,text)
tex=[r'\documentclass[11pt,a4paper]{article}',r'\usepackage[margin=23mm]{geometry}',r'\usepackage{fontspec}',r'\setmainfont{DejaVu Serif}',r'\usepackage{amsmath,amssymb,graphicx,booktabs,longtable,hyperref}',r'\hypersetup{colorlinks=true,urlcolor=blue,citecolor=blue}',r'\title{'+textext(DATA['title'])+'}',r'\author{'+textext(DATA['author'])+'}',r'\date{'+textext(DATA['date'])+'}',r'\begin{document}',r'\maketitle',r'\begin{abstract}',textext(DATA['abstract']),r'\end{abstract}']
story=[para('DDF / CLASSICAL FIVE-DIMENSIONAL MODEL','meta'),Spacer(1,5),para(DATA['title'],'title'),para(DATA['author'],'meta'),para(DATA['date'],'meta'),para('Abstract','section'),para(DATA['abstract'],'abstract')]
for sec in DATA['sections']:
    md+=['## '+sec['title'],''];tex+=[r'\section*{'+textext(sec['title'])+'}'];story.append(para(sec['title'],'section'))
    for block in sec['blocks']:
        kind=block['type']
        if kind=='paragraph':
            md+=[block['text'],''];tex+=[textext(block['text']),''];story.append(para(block['text']))
        elif kind=='equation':
            md+=['$$',block['latex']+r'\tag{'+block['number']+'}','$$','']
            tex+=[r'\begin{equation}',block['latex']+r'\tag{'+block['number']+'}',r'\end{equation}']
            preceding=story.pop() if story and isinstance(story[-1],Paragraph) else Spacer(1,0)
            bundle=[preceding,eq(block)]
            if story and isinstance(story[-1],Paragraph) and getattr(story[-1].style,'keepWithNext',False):bundle.insert(0,story.pop())
            story.append(KeepTogether(bundle))
        elif kind=='table':
            md+=['| '+' | '.join(block['headers'])+' |','| '+' | '.join(['---']*len(block['headers']))+' |']
            md+=['| '+' | '.join(map(str,row))+' |' for row in block['rows']]+['',block['caption'],'']
            n=len(block['headers']);tex+=[r'\begin{center}',r'\begin{tabular}{'+'c'*n+'}',r'\toprule',' & '.join(textext(str(c)) for c in block['headers'])+r'\\',r'\midrule']
            tex+=[' & '.join(textext(str(c)) for c in row)+r'\\' for row in block['rows']]+[r'\bottomrule',r'\end{tabular}',r'\end{center}',textext(block['caption']),'']
            rows=[[para(str(c),'cell') for c in row] for row in [block['headers']]+block['rows']]
            t=Table(rows,colWidths=[490/n]*n,hAlign='CENTER')
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8eff3')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f7f9fb')]),('LINEBELOW',(0,0),(-1,0),.5,ACCENT),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
            story.append(KeepTogether([Spacer(1,4),t,para(block['caption'],'caption')]))
    if sec['title'].startswith('5.'):
        md+=['![Finite-stiffness coefficients](figures/finite_stiffness.png)','',figcaption,'']
        tex+=[r'\begin{figure}[ht]',r'\centering\includegraphics[width=\linewidth]{figures/finite_stiffness.png}',r'\caption{'+textext(figcaption)+'}',r'\end{figure}']
        story.append(KeepTogether([Image(str(figdir/'finite_stiffness.png'),width=490,height=183.75),para(figcaption,'caption')]))
md+=['## References',''];tex+=[r'\begin{thebibliography}{99}'];story.append(para('References','section'))
for i,ref in enumerate(DATA['references'],1):
    text=ref['text'];md+=['['+str(i)+'] '+text,''];tex+=[r'\bibitem{ref'+str(i)+'} '+textext(text)]
    story.append(para('['+str(i)+'] '+text,'ref'))
tex+=[r'\end{thebibliography}',r'\end{document}']
(OUT/'manuscript.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
(OUT/'manuscript.tex').write_text('\n'.join(tex)+'\n',encoding='utf-8')
def footer(canvas,doc):
    canvas.saveState();canvas.setFont('Heading',7.0);canvas.setFillColor(ACCENT)
    canvas.drawString(52,815,'BOUFOUROU | BOUNDARY STIFFNESS AND RADION RESIDUES')
    canvas.setStrokeColor(colors.HexColor('#cbd8e1'));canvas.line(52,805,543,805)
    canvas.drawString(52,26,'Research manuscript for review - 6 September 2026');canvas.drawRightString(543,26,str(doc.page));canvas.restoreState()
doc=SimpleDocTemplate(str(OUT/'manuscript.pdf'),pagesize=(595.28,841.89),leftMargin=52,rightMargin=52,topMargin=53,bottomMargin=45,title=DATA['title'],author=DATA['author'])
doc.build(story,onFirstPage=footer,onLaterPages=footer)
reader=PdfReader(OUT/'manuscript.pdf');texts=[p.extract_text() or '' for p in reader.pages]
assert all(len(t)>150 for t in texts)
assert all('\ufffd' not in t and '\x00' not in t for t in texts)
result=dict(pages=len(texts),characters_per_page=list(map(len,texts)),equations=len(equation_audit),minimum_equation_scale=min(r['font_scale'] for r in equation_audit),text_checks='PASS',equation_layout=equation_audit,
 software=dict(numpy=np.__version__,matplotlib=matplotlib.__version__))
(TMP/'render_report.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='equation_layout'},indent=2))
