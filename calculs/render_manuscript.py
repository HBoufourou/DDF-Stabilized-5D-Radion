"""Typeset the authoritative manuscript JSON with ReportLab and mathtext."""
from pathlib import Path
import io, json, re, html, hashlib, sys, os
os.environ['MPLCONFIGDIR']=str(Path(__file__).resolve().parents[1]/'article'/'qa'/'mplcache')
import matplotlib
matplotlib.use('Agg')
from matplotlib import mathtext, font_manager
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, KeepTogether
from PIL import Image as PILImage

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE
ARTICLE=ROOT/'article'
ARTICLE.mkdir(exist_ok=True)
TMP=ARTICLE/'qa'
TMP.mkdir(exist_ok=True)
DATA=json.loads((ARTICLE/'manuscript.json').read_text(encoding='utf-8'))

for name,family,weight in [('Body','DejaVu Serif','normal'),('BodyBold','DejaVu Serif','bold'),
                            ('Heading','DejaVu Sans','normal'),('HeadingBold','DejaVu Sans','bold')]:
    pdfmetrics.registerFont(TTFont(name,font_manager.findfont(FontProperties(family=family,weight=weight))))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='Body',boldItalic='BodyBold')
pdfmetrics.registerFontFamily('Heading',normal='Heading',bold='HeadingBold',italic='Heading',boldItalic='HeadingBold')

INK=colors.HexColor('#17232E'); ACCENT=colors.HexColor('#214B66'); LIGHT=colors.HexColor('#EDF2F5')
styles={
    'body':ParagraphStyle('body',fontName='Body',fontSize=9.6,leading=14,alignment=TA_JUSTIFY,spaceAfter=7,textColor=INK),
    'abstract':ParagraphStyle('abstract',fontName='Body',fontSize=9.2,leading=13.3,alignment=TA_JUSTIFY,spaceAfter=9,textColor=INK),
    'title':ParagraphStyle('title',fontName='BodyBold',fontSize=20,leading=25,spaceAfter=16,textColor=INK),
    'section':ParagraphStyle('section',fontName='HeadingBold',fontSize=11.5,leading=16,spaceBefore=17,spaceAfter=8,keepWithNext=True,textColor=ACCENT),
    'caption':ParagraphStyle('caption',fontName='Body',fontSize=8.3,leading=11.5,spaceBefore=6,spaceAfter=12,textColor=INK),
    'cell':ParagraphStyle('cell',fontName='Heading',fontSize=8,leading=11,alignment=TA_CENTER,textColor=INK),
    'ref':ParagraphStyle('ref',fontName='Body',fontSize=8.1,leading=10,spaceAfter=4,textColor=INK),
    'meta':ParagraphStyle('meta',fontName='Heading',fontSize=9,leading=13,spaceAfter=7,textColor=ACCENT),
}
sup={c:t for c,t in zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾','0123456789+-=()')}
sup.update({'ᴬ':'A','ᴸ':'L','ᵀ':'T'})
sub={c:t for c,t in zip('₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎','0123456789+-=()')}
sub.update({'ᵣ':'r','ₘ':'m','ₙ':'n','ₛ':'s','ₜ':'t','ₐ':'a'})
def para(text,style='body'):
    text=text.replace('—','-').replace('–','-').replace('‑','-').replace('𝒟','D').replace('ℋ','H')
    text=html.escape(text)
    text=''.join('<super>'+sup[c]+'</super>' if c in sup else '<sub>'+sub[c]+'</sub>' if c in sub else c for c in text)
    return Paragraph(text,styles[style])

eq_audit=[]
def equation(block):
    latex=block['latex'].replace('\\Box_4','\\partial_\\mu\\partial^\\mu')
    latex=re.sub(r'\\frac\s*([0-9])\s*([0-9])',r'\\frac{\1}{\2}',latex)
    latex=re.sub(r'\\sqrt\s+([A-Za-z])',r'\\sqrt{\1}',latex)
    latex=re.sub(r'\\frac\s*([0-9])\s*\{',r'\\frac{\1}{',latex)
    latex=latex.replace('\\mathcal D','\\mathcal{D}')
    filename=TMP/('eq-'+str(block['number'])+'.png')
    mathtext.math_to_image('$'+latex+'$',filename,prop=FontProperties(size=12),dpi=320,format='png',color='#17232E')
    with PILImage.open(filename) as im: width,height=im.size
    scale=min(72/320,450/width)
    w,h=width*scale,height*scale
    eq_audit.append({'number':block['number'],'width_pt':w,'height_pt':h,'font_scale':scale/(72/320)})
    img=Image(str(filename),width=w,height=h)
    table=Table([[img,para('('+block['number']+')','cell')]],colWidths=[458,32],hAlign='CENTER')
    table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE'),('ALIGN',(0,0),(0,0),'CENTER'),
                               ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
                               ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
    return table

def scientific_figure():
    figdir=ARTICLE/'figures'; figdir.mkdir(exist_ok=True)
    x=np.linspace(.12,5,400);T=np.tanh(x/2);C=np.cosh(x/2)**2
    ref=json.loads((ROOT/'resultats'/'spectre_5d.json').read_text(encoding='utf-8'))[:6]
    e=np.array([r['epsilon'] for r in ref]);a=np.array([r['scalar_modes'][0]['alpha_scalar_conditional_archive_norm'] for r in ref])
    fig,axs=plt.subplots(1,2,figsize=(7.2,2.65),layout='constrained')
    axs[0].plot(x,4*x*T/C,label=r'$\kappa(x)$',color='#214B66',lw=1.8)
    axs[0].plot(x,(1+T*T+2*T/x)/C,label=r'$c_\alpha(x)$',color='#A55728',lw=1.8)
    axs[0].set(xlabel=r'$x=\mu L$',ylabel='Dimensionless coefficient',title='(a) Analytic coefficients')
    ee=np.linspace(0,.9,200)
    axs[1].plot(ee,(1+.98342023983853*ee*ee)/3,'--',color='#A55728',label=r'$O(\epsilon^2)$ series')
    axs[1].plot(e,a,'o-',color='#214B66',lw=1.2,ms=4,label=r'Coupled solution, $x=2$')
    axs[1].axhline(1/3,lw=.6,color='gray')
    axs[1].set(xlabel=r'$\epsilon$',ylabel=r'$\alpha_r$',title='(b) Radion coupling')
    for ax in axs:
        ax.spines[['top','right']].set_visible(False)
        ax.grid(alpha=.16);ax.legend(fontsize=7,frameon=False);ax.tick_params(labelsize=8)
        ax.title.set_fontsize(9);ax.xaxis.label.set_fontsize(9);ax.yaxis.label.set_fontsize(9)
    fig.savefig(figdir/'weak_coupling.png',dpi=300)
    fig.savefig(figdir/'weak_coupling.svg')
    plt.close(fig)
    return str(figdir/'weak_coupling.png')

figpath=scientific_figure()
story=[para('DDF  /  EFFECTIVE FIVE-DIMENSIONAL MODEL','meta'),Spacer(1,6),para(DATA['title'],'title'),
       para(DATA['author'],'meta'),para(DATA['date'],'meta'),Spacer(1,8),para('Abstract','section'),para(DATA['abstract'],'abstract')]
for section in DATA['sections']:
    story.append(para(section['title'],'section'))
    for block in section['blocks']:
        if block['type']=='paragraph':story.append(para(block['text']))
        elif block['type']=='equation':story.append(equation(block))
        elif block['type']=='table':
            rows=[[para(str(t),'cell') for t in block['headers']]]+[[para(str(t),'cell') for t in row] for row in block['rows']]
            table=Table(rows,colWidths=[490/len(rows[0])]*len(rows[0]),repeatRows=1,hAlign='CENTER')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),LIGHT),('LINEBELOW',(0,0),(-1,0),.6,ACCENT),
                ('LINEBELOW',(0,-1),(-1,-1),.5,ACCENT),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
                ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F8FAFB')]),('VALIGN',(0,0),(-1,-1),'MIDDLE')]))
            story.append(KeepTogether([Spacer(1,5),table,para(block['caption'],'caption')]))
    if section['title'].startswith('8.'):
        story.append(KeepTogether([Image(figpath,width=490,height=180.35),para('Figure 1. (a) Closed leading coefficients for positive x. (b) The coupled x = 2 radion amplitude and its truncated small-backreaction expansion. Connecting lines guide the eye; the asymptotic series is not exact at finite ε.','caption')]))

story.append(para('References','section'))
for i,ref in enumerate(DATA['references'],1):story.append(para('['+str(i)+'] '+ref['text'],'ref'))

def page(canvas,doc):
    canvas.saveState();canvas.setFont('Heading',7.1);canvas.setFillColor(ACCENT)
    canvas.drawString(52,814,'BOUFOUROU  |  RADION STABILITY AND BRANE COUPLINGS')
    canvas.setStrokeColor(colors.HexColor('#CDD9E0'));canvas.setLineWidth(.45);canvas.line(52,804,543,804)
    canvas.drawString(52,27,'Research draft  -  5 September 2026')
    canvas.drawRightString(543,27,str(doc.page));canvas.restoreState()

doc=SimpleDocTemplate(str(ARTICLE/'manuscript.pdf'),pagesize=(595.28,841.89),
     leftMargin=52,rightMargin=52,topMargin=54,bottomMargin=46,
     title=DATA['title'],author=DATA['author'],subject='Classical five-dimensional scalar-gravity model; research draft')
doc.build(story,onFirstPage=page,onLaterPages=page)
(TMP/'equation_layout.json').write_text(json.dumps(eq_audit,indent=2),encoding='utf-8')
print(json.dumps({'output':str(ARTICLE/'manuscript.pdf'),'equations':len(eq_audit),
                  'minimum_equation_font_scale':min(e['font_scale'] for e in eq_audit)},indent=2))
