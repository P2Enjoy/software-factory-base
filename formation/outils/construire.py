#!/usr/bin/env python3
# @spec formation/SPECIFICATION.md#edition | formation/SPECIFICATION.md#slides
"""Éditer les HTML autonomes, les figures SVG et les notes à partir des sources."""
import base64
import html
import json
import re
import textwrap
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "exports"
FIG = ROOT / "illustrations"
OUT.mkdir(exist_ok=True)
FIG.mkdir(exist_ok=True)
PROGRAMME = json.loads((ROOT / "programme.json").read_text(encoding="utf-8"))
SLIDES = json.loads((ROOT / "slides.json").read_text(encoding="utf-8"))
FIGURES = json.loads((ROOT / "illustrations.json").read_text(encoding="utf-8"))
FIG_BY_ID = {f["id"]: f for f in FIGURES}
CSS = (ROOT / "styles.css").read_text(encoding="utf-8")
MD = MarkdownIt("commonmark", {"html": False}).enable("table")


def put(path, value):
    path.write_text(value, encoding="utf-8")


def esc(value):
    return html.escape(str(value), quote=True)


def slug(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def doc_id(path):
    return "doc-" + slug(str(path.relative_to(ROOT).with_suffix("")))


def svg_text(text, x, y, size=24, width=22, color="#0D0D0D", weight=400):
    lines = textwrap.wrap(text, width=width, break_long_words=False)
    spans = "".join(f'<tspan x="{x}" dy="{0 if i == 0 else size * 1.25}">{esc(line)}</tspan>' for i, line in enumerate(lines))
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}">{spans}</text>'


def figure_svg(f):
    description = f['subtitle'] + " " + "; ".join(": ".join(n) for n in f['nodes']) + ". " + f['footer']
    body = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="460" viewBox="0 0 1200 460" role="img" aria-labelledby="title desc"><title id="title">{esc(f["title"])}</title><desc id="desc">{esc(description)}</desc>',
            '<rect width="1200" height="460" rx="14" fill="#F7F8FA"/><g font-family="Arial, sans-serif">',
            svg_text(f['subtitle'], 32, 44, 24, 85, "#4B5563")]
    kind = f['kind']
    if kind == "flow":
        boxes = [(32 + i * 295, 146, 251, 160) for i in range(4)]
        for i in range(3):
            x = boxes[i][0] + boxes[i][2]
            body.append(f'<path d="M{x+5} 226 H{x+34} m-9 -8 9 8 -9 8" fill="none" stroke="#23468C" stroke-width="3"/>')
    elif kind == "grid":
        boxes = [(32 + (i % 2) * 582, 106 + (i // 2) * 133, 552, 116) for i in range(4)]
    elif kind == "split":
        boxes = [(32, 132, 552, 186), (616, 132, 552, 186)]
    elif kind == "rights":
        boxes = [(32 + i * 390, 138, 356, 184) for i in range(3)]
    elif kind == "roles":
        boxes = [(400, 83, 400, 96)] + [(32 + i * 390, 238, 356, 111) for i in range(3)]
        body.append('<path d="M600 179 V210 H210 V238 M600 210 V238 M600 210 H990 V238" fill="none" stroke="#23468C" stroke-width="3"/>')
    else:
        raise ValueError(f"Type de figure inconnu : {kind}")
    for i, ((title, detail), (x, y, w, h)) in enumerate(zip(f['nodes'], boxes)):
        body.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="white" stroke="#23468C" stroke-width="2"/>')
        body.append(f'<rect x="{x+18}" y="{y+18}" width="5" height="{h-36}" rx="2" fill="#D9CF4A"/>')
        body.append(svg_text(title, x+37, y+37, 25, int((w-58)/14), "#23468C", 700))
        title_lines = len(textwrap.wrap(title, width=int((w-58)/14), break_long_words=False))
        body.append(svg_text(detail, x+37, y+38+title_lines*31, 21, int((w-58)/11)))
    body += ['<path d="M32 391 H1168" stroke="#D9CF4A" stroke-width="4"/>', svg_text(f['footer'], 32, 423, 21, 101), '</g></svg>']
    return "\n".join(body)


for fig in FIGURES:
    put(FIG / (fig['id'] + '.svg'), figure_svg(fig))

guide = '# Illustrations et équivalents textuels\n\nQuinze schémas vectoriels originaux, palette P2Enjoy, sans ressource distante.\nLes relations sont explicitées ci-dessous et dans les descriptions accessibles\ndes SVG. Les versions PNG exportées servent au PowerPoint.\n\n'
for fig in FIGURES:
    guide += f'## {fig["title"]}\n\n![{fig["title"]}](illustrations/{fig["id"]}.svg)\n\n{fig["subtitle"]}\n\n'
    guide += '\n'.join(f'- {a} : {b}.' for a, b in fig['nodes']) + '\n\n' + fig['footer'] + '\n\n'
put(ROOT / 'ILLUSTRATIONS.md', guide)

notes = '# Notes par diapositive\n\n80 diapositives. Les durées se rattachent aux phases du module, sans s’ajouter\nau programme de 42 heures. Les deux ouvertures sont comprises dans M1.\n\n'
for i, s in enumerate(SLIDES, 1):
    notes += f'## S{i:02d} — {s["title"]}\n\n'
    for key, label in [('minutage','Minutage'),('intention','Intention'),('explication','Explication / démonstration'),('question','Question'),('attendu','Réponse attendue'),('transition','Transition')]:
        notes += f'**{label}.** {s["notes"][key]}\n\n'
put(OUT / 'notes-slides.md', notes)


def render_document(path, included):
    source = path.read_text(encoding='utf-8')
    tokens = MD.parse(source)
    prefix = doc_id(path)
    seen = {}
    for index, token in enumerate(tokens):
        if token.type == 'heading_open':
            heading = slug(tokens[index + 1].content)
            occurrence = seen.get(heading, 0)
            seen[heading] = occurrence + 1
            token.attrSet('id', prefix + '--' + heading + (f'-{occurrence}' if occurrence else ''))
        for child in token.children or []:
            if child.type == 'image':
                local = (path.parent / unquote(child.attrGet('src'))).resolve()
                if not local.is_file():
                    raise FileNotFoundError(local)
                mime = 'image/svg+xml' if local.suffix == '.svg' else 'image/png'
                child.attrSet('src', f'data:{mime};base64,' + base64.b64encode(local.read_bytes()).decode())
            if child.type == 'link_open':
                link = child.attrGet('href')
                parts = urlsplit(link)
                if parts.scheme or parts.netloc:
                    continue
                local = (path.parent / unquote(parts.path)).resolve() if parts.path else path
                if local in included:
                    target = '#' + doc_id(local)
                    if parts.fragment:
                        target += '--' + slug(unquote(parts.fragment))
                else:
                    import os
                    target = os.path.relpath(local, OUT).replace('\\', '/')
                    if parts.fragment:
                        target += '#' + parts.fragment
                child.attrSet('href', target)
    title = next((t.content for i, t in enumerate(tokens) if i and tokens[i-1].type == 'heading_open'), path.stem)
    return title, f'<article id="{prefix}">{MD.renderer.render(tokens, MD.options, {})}</article>'


def book(filename, title, files, subtitle):
    paths = [(ROOT / f).resolve() for f in files]
    sections = [render_document(path, set(paths)) for path in paths]
    toc = '<nav aria-label="Sommaire"><h2>Sommaire</h2><ul>' + ''.join(f'<li><a href="#{doc_id(path)}">{esc(section[0])}</a></li>' for path, section in zip(paths, sections)) + '</ul></nav>'
    content = f'<section class="cover"><p class="eyebrow">P2Enjoy · Formation au codage agentique</p><h1>{esc(title)}</h1><div class="rule"></div><p>{esc(subtitle)}</p><p class="print-help">Document autonome hors ligne. Les liens externes des sources nécessitent une connexion.</p></section>'
    put(OUT / filename, '<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(title)+'</title><style>'+CSS+'</style></head><body><a class="skip" href="#contenu">Aller au contenu</a><main class="book" id="contenu">'+content+toc+''.join(s[1] for s in sections)+'</main></body></html>')


chapters = ['cours/' + m['file'] for m in PROGRAMME['modules']]
book('cours.html', PROGRAMME['title'], ['SYLLABUS.md','INSTALLATION.md'] + chapters + ['EXERCICES.md','EVALUATION.md','CORRIGES.md','CORRIGE_FINAL.md','FICHES.md','GLOSSAIRE.md','SOURCES.md'], 'Le cours complet : quinze chapitres, trente exercices, leurs corrigés, les quiz et l’évaluation finale.')
book('cahier-exercices.html', 'Cahier des exercices', ['INSTALLATION.md','EXERCICES.md','EVALUATION.md','FICHES.md'], 'Consignes, indices, critères et fiches à remplir. Les corrigés sont dans un volume séparé.')
book('corriges.html', 'Corrigés et raisonnements', ['CORRIGES.md','CORRIGE_FINAL.md'], 'À consulter après votre première production. Une solution écrite ne remplace pas vos propres preuves.')
book('guide-animation.html', 'Animer la formation', ['ANIMATION.md','exports/notes-slides.md'], 'Déroulé premium sur six journées et notes des quatre-vingts diapositives.')

slide_html = []
for i, s in enumerate(SLIDES, 1):
    eyebrow = 'Parcours' if s['module'] == 0 else ('Évaluation finale' if s['module'] == 16 else f'Module {s["module"]:02d} / 15')
    content = f'<p class="eyebrow">{eyebrow}</p><h1 class="{"statement" if s["type"] == "hero" else ""}">{esc(s["title"])}</h1>'
    if 'lead' in s:
        content += f'<p class="lead">{esc(s["lead"])}</p>'
    if 'points' in s:
        content += '<ul>' + ''.join('<li>'+esc(p)+'</li>' for p in s['points']) + '</ul>'
    if 'case' in s:
        content += '<pre class="case">'+esc(s['case'])+'</pre>'
    if 'figure' in s:
        source_svg = (FIG/(s['figure']+'.svg')).read_text(encoding='utf-8')
        cropped_svg = source_svg.replace('height="460" viewBox="0 0 1200 460"', 'height="300" viewBox="0 80 1200 300"', 1)
        data = base64.b64encode(cropped_svg.encode()).decode()
        f = next(f for f in FIGURES if f['id'] == s['figure'])
        content += f'<img class="figure" src="data:image/svg+xml;base64,{data}" alt="{esc(f["subtitle"]+" "+" ; ".join(": ".join(n) for n in f["nodes"]))}">'
    if 'figure' not in s and 'visual' in s and s['visual'] in FIG_BY_ID:
        source_svg = (FIG / (s['visual'] + '.svg')).read_text(encoding='utf-8')
        mini_svg = source_svg.replace('height="460" viewBox="0 0 1200 460"', 'height="220" viewBox="0 120 1200 220"', 1)
        data = base64.b64encode(mini_svg.encode()).decode()
        fig = FIG_BY_ID[s['visual']]
        content += f'<img class="visual-ornament" src="data:image/svg+xml;base64,{data}" alt="{esc(fig["subtitle"]+" "+" ; ".join(": ".join(n) for n in fig["nodes"]))}">'
    content += f'<p class="takeaway">{esc(s["takeaway"])}</p><footer><span>P2Enjoy · Les bases, la méthode, puis l’usine</span><span>{i:02d} / {len(SLIDES)}</span></footer>'
    content += '<template><h2>Notes S'+str(i)+'</h2>' + ''.join(f'<p><strong>{esc(k.capitalize())}.</strong> {esc(v)}</p>' for k, v in s['notes'].items())+'</template>'
    slide_html.append(f'<section class="slide {s["type"]}{" active" if i==1 else ""}" aria-label="Diapositive {i}" aria-hidden="{"false" if i==1 else "true"}">{content}</section>')
script = (ROOT/'lecteur-slides.js').read_text(encoding='utf-8')
put(OUT/'slides.html', '<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Coder avec un agent — 80 diapositives</title><style>'+CSS+'\n@media print{@page{size:1280px 720px;margin:0}}</style></head><body class="deck"><div class="deck-toolbar"><button id="previous">Précédent</button><button id="next">Suivant</button><button id="toggle-notes" aria-expanded="false" aria-controls="notes">Notes</button><span id="position" role="status" aria-live="polite"></span><a href="cours.html">Lire le cours</a></div><main class="deck-stage">'+''.join(slide_html)+'</main><aside class="notes" id="notes" hidden></aside><script>'+script+'</script></body></html>')
print(json.dumps({'chapitres':len(chapters),'slides':len(SLIDES),'figures':len(FIGURES),'html':5}, ensure_ascii=False))
