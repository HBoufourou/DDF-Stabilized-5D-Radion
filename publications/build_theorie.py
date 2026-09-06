from pathlib import Path
import re, html, json, sys
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
from matplotlib import font_manager
from matplotlib.font_manager import FontProperties
pdfmetrics.registerFont(TTFont('DDFBody',font_manager.findfont(FontProperties(family='DejaVu Sans'))))
pdfmetrics.registerFont(TTFont('DDFBold',font_manager.findfont(FontProperties(family='DejaVu Sans',weight='bold'))))
pdfmetrics.registerFontFamily('DDFBody',normal='DDFBody',bold='DDFBold',italic='DDFBody',boldItalic='DDFBold')
width=459.28
ink=colors.HexColor('#17384b');muted=colors.HexColor('#526675')
styles={
 'body':ParagraphStyle('body',fontName='DDFBody',fontSize=9.2,leading=13.6,spaceAfter=7,textColor='#172934'),
 'title':ParagraphStyle('title',fontName='DDFBold',fontSize=22,leading=27,spaceAfter=15,textColor=ink),
 'h2':ParagraphStyle('h2',fontName='DDFBold',fontSize=12.6,leading=17,spaceBefore=13,spaceAfter=8,keepWithNext=True,textColor=ink),
 'h3':ParagraphStyle('h3',fontName='DDFBold',fontSize=10.5,leading=15,spaceBefore=10,spaceAfter=5,keepWithNext=True,textColor=ink),
 'code':ParagraphStyle('code',fontName='DDFBody',fontSize=8.45,leading=13.3,spaceAfter=0,textColor='#12374a'),
 'cell':ParagraphStyle('cell',fontName='DDFBody',fontSize=8.2,leading=12,spaceAfter=0,textColor='#172934'),
 'ref':ParagraphStyle('ref',fontName='DDFBody',fontSize=8.3,leading=12.2,spaceAfter=5,textColor=muted),
}

def markup(text):
    # Keep formula glyphs; normalize dash characters for reliable rendering.
    text=text.replace('—','-').replace('–','-').replace('‑','-')
    text=html.escape(text)
    text=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',text)
    def link(m):
        label,target=m.groups()
        return f'<link href="{target}" color="#1b617a">{label}</link>' if target.startswith('https://') else label
    return re.sub(r'\[([^]]+)\]\(([^)]+)\)',link,text)

def para(text,kind='body'):return Paragraph(markup(text),styles[kind])

def story_from_md(path):
    lines=path.read_text(encoding='utf-8').splitlines();story=[];i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        if line.startswith('```'):
            items=[];i+=1
            while i<len(lines) and not lines[i].startswith('```'):
                items.append([para(lines[i].strip() or ' ','code')]);i+=1
            box=Table(items,colWidths=[width-18],hAlign='LEFT')
            box.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#eef4f6')),
                ('BOX',(0,0),(-1,-1),.5,colors.HexColor('#cfdee5')),
                ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
                ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
            introductory=story.pop() if story and isinstance(story[-1],Paragraph) else Spacer(1,0)
            block=[introductory,box,Spacer(1,9)]
            if story and isinstance(story[-1],Paragraph) and getattr(story[-1].style,'keepWithNext',False):
                block.insert(0,story.pop())
            story.append(KeepTogether(block));i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                raw=lines[i].strip().strip('|').split('|')
                if not all(re.fullmatch(r'\s*:?-+:?\s*',c) for c in raw):
                    rows.append([para(c.strip(),'cell') for c in raw])
                i+=1
            n=len(rows[0]);table=Table(rows,colWidths=[width/n]*n,repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e4edf2')),
               ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f6f9fa')]),
               ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),
               ('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),
               ('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,0),.5,colors.HexColor('#adbfca'))]))
            introductory=story.pop() if story and isinstance(story[-1],Paragraph) else Spacer(1,0)
            block=[introductory,table,Spacer(1,10)]
            if story and isinstance(story[-1],Paragraph) and getattr(story[-1].style,'keepWithNext',False):
                block.insert(0,story.pop())
            story.append(KeepTogether(block));continue
        if line.startswith('# '):story.append(para(line[2:],'title'));i+=1;continue
        if line.startswith('## '):story.append(para(line[3:],'h2'));i+=1;continue
        if line.startswith('### '):story.append(para(line[4:],'h3'));i+=1;continue
        if line.startswith('- '):story.append(para('• '+line[2:],'ref'));i+=1;continue
        paragraph=[line];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','```','|','- ')):
            paragraph.append(lines[i].strip());i+=1
        story.append(para(' '.join(paragraph)))
    return story

def footer(canvas,doc):
    canvas.saveState();w,h=doc.pagesize
    canvas.setFont('DDFBody',7.2);canvas.setFillColor(muted)
    canvas.drawString(68,27,'DDF - modèle effectif canonique | 6 septembre 2026')
    canvas.drawRightString(w-68,27,str(doc.page))
    canvas.setStrokeColor(colors.HexColor('#c6d6df'));canvas.line(68,41,w-68,41)
    canvas.restoreState()

def main():
    source=ROOT/'THEORIE_DDF.md';target=source.with_suffix('.pdf')
    doc=SimpleDocTemplate(str(target),pagesize=(595.28,841.89),rightMargin=68,leftMargin=68,
                         topMargin=55,bottomMargin=57,title='DDF : un intervalle stabilisé et un secteur scalaire sombre contrôlé',author='Hicham Boufourou')
    doc.build(story_from_md(source),onFirstPage=footer,onLaterPages=footer)
    reader=PdfReader(target);texts=[p.extract_text() or '' for p in reader.pages]
    assert all(len(t)>180 for t in texts),'Unexpected empty page.'
    assert not any('\ufffd' in t or '\x00' in t for t in texts),'Text replacement/control character.'
    report=dict(pages=len(reader.pages),characters_per_page=[len(t) for t in texts],
                file=str(target),text_checks='PASS')
    (ROOT/'work/theorie_render').mkdir(parents=True,exist_ok=True)
    (ROOT/'work/theorie_render/pdf_text_check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
