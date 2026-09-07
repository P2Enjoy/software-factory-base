#!/usr/bin/env python3
# @spec formation/SPECIFICATION.md#verification
"""Vérifier liens, correspondances, exports et manifeste sans déclarer de preuve métier."""
import argparse
import ast
import hashlib
import json
import re
import subprocess
import unicodedata
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
OUT = ROOT / 'exports'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--archive-only',action='store_true')
args = parser.parse_args()
report = {'checks':[]}


def check(name, condition, details=None):
    report['checks'].append({'name':name,'ok':bool(condition),'details':details})


def slug(text):
    text=unicodedata.normalize('NFKD',text).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',text).strip('-')


def archive_check():
    with ZipFile(OUT/'formation-complete.zip') as archive:
        names=archive.namelist()
        check('ZIP sans erreur CRC',archive.testzip() is None)
        check('ZIP sans sortie de dossier',all(not n.startswith('/') and '..' not in Path(n).parts for n in names))
        check('ZIP sans environnement ni base',all(not {'.git','node_modules','__pycache__','.venv'}.intersection(Path(n).parts) and not n.endswith(('.sqlite3','.pyc')) for n in names))
        inventory=json.loads(archive.read('formation/exports/inventaire.json'))['files']
        check('inventaire exact du ZIP',set(names)==set(inventory)|{'formation/exports/inventaire.json'})
        for name, item in inventory.items():
            data=archive.read(name)
            check('intégrité ZIP '+name,len(data)==item['bytes'] and hashlib.sha256(data).hexdigest()==item['sha256'])
            current=REPO/name
            check('ZIP à jour '+name,current.is_file() and hashlib.sha256(current.read_bytes()).hexdigest()==item['sha256'])
        for name in ['formation/atelier/commun/BACKLOG.md','formation/atelier/commun/DAT.md','formation/SPECIFICATION.md','formation/exports/slides.pptx','formation/exports/cours.pdf']:
            check('ressource critique empaquetée '+name,name in names)
        return len(names)


if args.archive_only:
    report['archive_files']=archive_check()
else:
    md=MarkdownIt('commonmark',{'html':False}).enable('table')
    prog=json.loads((ROOT/'programme.json').read_text(encoding='utf-8'))
    slides=json.loads((ROOT/'slides.json').read_text(encoding='utf-8'))
    figures=json.loads((ROOT/'illustrations.json').read_text(encoding='utf-8'))
    check('quinze modules dans l’ordre', [m['id'] for m in prog['modules']]==list(range(1,16)))
    check('42 heures hors pauses',len(prog['modules'])*prog['module_minutes']+prog['evaluation_minutes']==2520)
    exercises=(ROOT/'EXERCICES.md').read_text(encoding='utf-8')
    answers=(ROOT/'CORRIGES.md').read_text(encoding='utf-8')
    expected_ex=[f'E{i:02d}' for i in range(1,31)]
    check('30 exercices ordonnés',re.findall(r'^## (E\d\d)\b',exercises,re.M)==expected_ex)
    check('30 corrigés ordonnés',re.findall(r'^## (E\d\d)\b',answers,re.M)==expected_ex)
    check('association des exercices',sum([m['exercises'] for m in prog['modules']],[])==expected_ex)
    quiz=[]
    for m in prog['modules']:
        content=(ROOT/'cours'/m['file']).read_text(encoding='utf-8')
        quiz.extend(re.findall(r'Q\d+\.\d+',content))
        check(f'M{m["id"]} : objectif, exercices et figure', 'Objectif :' in content and all(e in content for e in m['exercises']) and m['figure']+'.svg' in content)
    expected_quiz={f'Q{i}.{j}' for i in range(1,16) for j in range(1,4)}
    check('45 quiz dans les chapitres',set(quiz)==expected_quiz and len(quiz)==45)
    check('45 réponses de quiz',set(re.findall(r'\| (Q\d+\.\d+) \|',answers))==expected_quiz)
    check('80 slides et notes complètes',len(slides)==80 and all(all(s.get('notes',{}).get(k,'').strip() for k in ['intention','explication','question','attendu','transition','minutage']) for s in slides))
    check('progression des slides',[s['module'] for s in slides]==[0,0]+[i for i in range(1,16) for _ in range(5)]+[16,16,16])
    check('15 figures',len(figures)==15 and len(list((ROOT/'illustrations').glob('*.svg')))==15)
    source_files=[p for p in ROOT.rglob('*.md') if 'exports' not in p.relative_to(ROOT).parts and 'node_modules' not in p.parts]
    links=0
    for file in source_files:
        content=file.read_text(encoding='utf-8')
        for token in md.parse(content):
            for child in token.children or []:
                if child.type not in ('link_open','image'):
                    continue
                link=child.attrGet('href') if child.type=='link_open' else child.attrGet('src')
                parts=urlsplit(link)
                if parts.scheme or parts.netloc:
                    continue
                target=(file.parent/unquote(parts.path)).resolve() if parts.path else file
                links+=1
                check('lien '+str(file.relative_to(ROOT))+' → '+link,target.exists())
                if target.is_file() and target.suffix=='.md' and parts.fragment:
                    tokens=md.parse(target.read_text(encoding='utf-8'))
                    anchors={slug(tokens[i+1].content) for i,t in enumerate(tokens) if t.type=='heading_open'}
                    check('ancre '+link,slug(unquote(parts.fragment)) in anchors)
    report['local_links']=links
    for file in ROOT.rglob('*.py'):
        if 'node_modules' in file.parts:continue
        try:ast.parse(file.read_text(encoding='utf-8'));valid=True
        except SyntaxError:valid=False
        check('syntaxe Python '+str(file.relative_to(ROOT)),valid)
    for file in [ROOT/'lecteur-slides.js',*list((ROOT/'outils').glob('*.cjs'))]:
        result=subprocess.run(['node','--check',str(file)],capture_output=True,text=True)
        check('syntaxe JS '+file.name,result.returncode==0,result.stderr or None)
    for name in ['cours','cahier-exercices','corriges','guide-animation','slides']:
        result=subprocess.run(['pdfinfo',str(OUT/(name+'.pdf'))],capture_output=True,text=True)
        match=re.search(r'^Pages:\s+(\d+)',result.stdout,re.M)
        count=int(match[1]) if match else 0
        check('PDF '+name,result.returncode==0 and count>0,{'pages':count})
        if name=='slides':check('80 pages de slides PDF',count==80)
        # Chaque page doit contenir du texte, pas seulement un fond ou un pied de page.
        text=subprocess.run(['pdftotext',str(OUT/(name+'.pdf')),'-'],capture_output=True,text=True)
        pages=[p for p in text.stdout.split('\f') if p.strip()]
        check('pages PDF non vides '+name,len(pages)==count and all(len(p.strip())>50 for p in pages))
    ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
    with ZipFile(OUT/'slides.pptx') as pptx:
        names=pptx.namelist()
        check('PowerPoint 80 slides',len([n for n in names if re.fullmatch(r'ppt/slides/slide\d+\.xml',n)])==80)
        check('PowerPoint 80 notes',len([n for n in names if re.fullmatch(r'ppt/notesSlides/notesSlide\d+\.xml',n)])==80)
        for index,s in enumerate(slides,1):
            xml=ET.fromstring(pptx.read(f'ppt/slides/slide{index}.xml'))
            texts=[e.text or '' for e in xml.findall('.//a:t',ns)]
            joined='\n'.join(texts)
            check(f'S{index} titre éditable',s['title'] in joined)
            check(f'S{index} texte et conclusion',all(p in joined for p in s.get('points',[])) and s['takeaway'] in joined and all(line in joined for line in s.get('case','').splitlines()))
            notes=ET.fromstring(pptx.read(f'ppt/notesSlides/notesSlide{index}.xml'))
            note_text='\n'.join(e.text or '' for e in notes.findall('.//a:t',ns))
            check(f'S{index} notes conservées',all(value in note_text for value in s['notes'].values()))
            if s.get('figure'):
                alt=' '.join(e.attrib.get('descr','') for e in xml.findall('.//p:cNvPr',ns))
                f=next(f for f in figures if f['id']==s['figure'])
                check(f'S{index} alternative du schéma',all(label in alt and detail in alt for label,detail in f['nodes']))
    for name in ['controle-rendu','controle-atelier']:
        data=json.loads((OUT/(name+'.json')).read_text(encoding='utf-8'))
        check('rapport '+name+' sans échec',bool(data.get('checks')) and all(c['ok'] for c in data['checks']) and not data.get('error') and not data.get('cleanup_error'))
        check('rapport '+name+' lié aux sources courantes',bool(data.get('sources')) and all((ROOT/n).is_file() and hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==digest for n,digest in data.get('sources',{}).items()))
    report['counts']={'modules':15,'exercises':30,'quiz':45,'figures':15,'slides':80,'minutes':2520}

failures=[c for c in report['checks'] if not c['ok']]
report['failed']=len(failures)
if not args.archive_only:
    (OUT/'controle-edition.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'checks':len(report['checks']),'failed':failures,**({'archive_files':report['archive_files']} if args.archive_only else report['counts'])},ensure_ascii=False,indent=2))
raise SystemExit(1 if failures else 0)
