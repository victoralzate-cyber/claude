import re, json, sys
from bs4 import BeautifulSoup, NavigableString, Comment
src, out, dump = sys.argv[1:4]
raw = open(src, encoding='utf-8').read()
head, rest = raw.split('<body>', 1)
body_html, tail = rest.rsplit('</body>', 1)
soup = BeautifulSoup(body_html, 'html.parser')

TEXT = {'h1','h2','h3','h4','p','li','span','a','strong','small','summary','button','option','blockquote','label','div','em','b'}
COMPLEX = {'svg','input','select','textarea','img','ul','ol','div','p','h1','h2','h3','h4','li','details','form','button','article','header','blockquote'}
letters = re.compile(r'[A-Za-zÁÉÍÓÚÑáéíóúñü¿¡]{2,}')
es, n = {}, [0]
def key():
    n[0] += 1; return f't{n[0]:03d}'
def skip_zone(el):
    return any(p.name in ('script','style','svg') or (p.has_attr('data-i18n') if hasattr(p,'has_attr') else False) for p in el.parents if p.name)

# keep CRM values in Spanish
for o in soup.find_all('option'):
    if o.get('value') is None: o['value'] = o.get_text()

for el in list(soup.find_all(True)):
    if el.name not in TEXT or skip_zone(el): continue
    own = [c for c in el.children if isinstance(c, NavigableString) and not isinstance(c, Comment) and letters.search(c)]
    if not own: continue
    if el.find(lambda t: t.name in COMPLEX):
        for c in own:
            k = key(); sp = soup.new_tag('span'); sp['data-i18n'] = k
            txt = str(c); lead = txt[:len(txt)-len(txt.lstrip())]; trail = txt[len(txt.rstrip()):]
            sp.string = txt.strip(); es[k] = txt.strip()
            c.replace_with(sp)
            if lead: sp.insert_before(NavigableString(lead))
            if trail: sp.insert_after(NavigableString(trail))
        continue
    k = key(); el['data-i18n'] = k; es[k] = el.decode_contents().strip()

# second pass for wrap cases with no leading whitespace: handled by replace above? ensure none lost
for attr, flag in (('alt','data-i18n-alt'),('aria-label','data-i18n-aria')):
    for el in soup.find_all(attrs={attr: True}):
        if letters.search(el[attr]) and not skip_zone(el):
            k = key(); el[flag] = k; es[k] = el[attr]

open(out, 'w', encoding='utf-8').write(head + '<body>' + str(soup) + '</body>' + tail)
json.dump(es, open(dump, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(es), 'textos')
