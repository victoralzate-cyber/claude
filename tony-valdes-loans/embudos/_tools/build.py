"""Construye las páginas de un embudo.

Uso:  python3 embudos/_tools/build.py embudos/primeros-compradores

Por cada página de src/ genera:
  revisar/<pagina>.html  -> HTML completo con imágenes incluidas (para revisar en el navegador)
  ghl/<pagina>.html      -> versión encapsulada bajo #tvl para pegar en un elemento Code de GHL
Las traducciones salen de <embudo>/i18n.py (lista T y diccionario META) y de _tools/memoria.json.
"""
import base64, importlib.util, io, json, os, re, subprocess, sys, tempfile
from PIL import Image

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)                      # embudos/
ASSETS = os.path.join(os.path.dirname(ROOT), 'assets')
SHARED = os.path.join(ROOT, '_shared')
fdir = os.path.abspath(sys.argv[1])

spec = importlib.util.spec_from_file_location('cfg', os.path.join(fdir, 'i18n.py'))
cfg = importlib.util.module_from_spec(spec); spec.loader.exec_module(cfg)
mem = json.load(open(os.path.join(TOOLS, 'memoria.json'), encoding='utf-8'))
TM = {'en': dict(mem['en']), 'pt': dict(mem['pt'])}
for es, en, pt in cfg.T:
    TM['en'][es] = en; TM['pt'][es] = pt
for same in getattr(cfg, 'SAME', []):
    TM['en'][same] = same; TM['pt'][same] = same
COMMON_META = {l: {k: v for k, v in mem['meta'][l].items() if k.startswith('_err_')} for l in ('es', 'en', 'pt')}

def read(p): return open(p, encoding='utf-8').read()
_cache = {}
def data_uri(name, h):
    key = (name, h)
    if key not in _cache:
        im = Image.open(os.path.join(ASSETS, name))
        if im.height > h: im = im.resize((round(im.width * h / im.height), h), Image.LANCZOS)
        buf = io.BytesIO()
        if name.endswith('.png'): im.save(buf, 'PNG', optimize=True); mt = 'image/png'
        else: im.save(buf, 'WEBP', quality=80); mt = 'image/webp'
        _cache[key] = f'data:{mt};base64,' + base64.b64encode(buf.getvalue()).decode()
    return _cache[key]

os.makedirs(os.path.join(fdir, 'revisar'), exist_ok=True)
os.makedirs(os.path.join(fdir, 'ghl'), exist_ok=True)
total_missing = 0
all_missing = {}
for page in cfg.PAGES:
    name = page['src']
    h = read(os.path.join(fdir, 'src', name))
    h = h.replace('/*FUNNEL_CSS*/', read(os.path.join(SHARED, 'funnel.css')))
    tema = os.path.join(fdir, 'src', 'tema.css')
    h = h.replace('/*THEME_CSS*/', read(tema) if os.path.exists(tema) else '')
    h = h.replace('<!--HEADER-->', read(os.path.join(SHARED, 'header.html')))
    h = h.replace('<!--FOOTER-->', read(os.path.join(SHARED, 'footer.html')).replace('{{WA}}', cfg.WA_TEXT))
    h = h.replace('/*CORE_JS*/', read(os.path.join(SHARED, 'core.js')))
    with tempfile.TemporaryDirectory() as td:
        a, b, d = (os.path.join(td, x) for x in ('a.html', 'b.html', 'es.json'))
        open(a, 'w', encoding='utf-8').write(h)
        subprocess.run([sys.executable, '-I', os.path.join(TOOLS, 'i18n_tag.py'), a, b, d], check=True, stdout=subprocess.DEVNULL)
        h = read(b); es = json.load(open(d, encoding='utf-8'))
    # El sello Equal Housing siempre en inglés
    h = re.sub(r'<span data-i18n="t\d+">EQUAL HOUSING</span>\s*<br/>\s*(?:<span data-i18n="t\d+">OPPORTUNITY</span>)?', 'EQUAL HOUSING<br/>OPPORTUNITY', h)
    h = re.sub(r'(class="ehl"[^>]*?) data-i18n-aria="t\d+"', r'\1', h)
    h = re.sub(r' data-i18n-aria="t\d+"(?=[^>]*class="ehl")', '', h)
    d = {'es': {}, 'en': {}, 'pt': {}}
    missing = []
    for k, v in es.items():
        if v in ('EQUAL HOUSING', 'OPPORTUNITY', 'Equal Housing Opportunity'): continue
        e, p = TM['en'].get(v), TM['pt'].get(v)
        if e: d['en'][k] = e
        if p: d['pt'][k] = p
        if (not e or not p) and re.search(r'[a-záéíóúñ]{3,}', re.sub(r'<[^>]+>', '', v), re.I):
            missing.append((k, v))
    for l in ('es', 'en', 'pt'):
        d[l].update(COMMON_META[l]); d[l].update(cfg.META[l])
        d[l]['_title'] = page['title'][l]; d[l]['_desc'] = page['desc'][l]
    h = h.replace('__I18N__', json.dumps(d, ensure_ascii=False))
    h = re.sub(r'<title>.*?</title>', '<title>' + page['title']['es'] + '</title>', h, count=1, flags=re.S)
    h = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + page['desc']['es'].replace('"', '&quot;'), h, count=1)
    h = re.sub(r'\{\{A\}\}/([\w\-/]+\.(?:png|webp))(?:\?h=(\d+))?',
               lambda m: data_uri(m.group(1), int(m.group(2) or (400 if m.group(1).endswith('.png') else 1300))), h)
    out_rev = os.path.join(fdir, 'revisar', name)
    open(out_rev, 'w', encoding='utf-8').write(h)
    subprocess.run([sys.executable, '-I', os.path.join(TOOLS, 'ghl_scope.py'), out_rev, os.path.join(fdir, 'ghl', name),
                    page['label']], check=True, stdout=subprocess.DEVNULL)
    print(f"{name}: {round(len(h)/1024)} KB | textos {len(es)} | sin traducir {len(missing)}")
    for k, v in missing: print('   ', k, '=', v[:140])
    total_missing += len(missing)
    all_missing.update({v: '' for k, v in missing})
print('TOTAL sin traducir:', total_missing)
if all_missing: json.dump(list(all_missing), open(os.path.join(fdir, '.faltan.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
