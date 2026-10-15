import re, sys
src, out = sys.argv[1], sys.argv[2]
label = sys.argv[3] if len(sys.argv) > 3 else 'PÁGINA'
html = open(src, encoding='utf-8').read()

css = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
body = re.search(r'<body>(.*?)</body>', html, re.S).group(1)
fonts = '\n'.join(re.findall(r'<link[^>]+>', html))
P = '#tvl'

def scope_sel(sel):
    sel = sel.strip()
    if sel in (':root', 'body', 'html', 'html,body'): return P
    if sel.startswith(':root'): return P + sel[5:]
    if sel.startswith('html'): return P + sel[4:]
    if sel.startswith('body'): return P + sel[4:]
    if sel.startswith('::') or sel.startswith(':focus'): return P + ' ' + sel
    if sel == '*': return P + ' *'
    return P + ' ' + sel

def scope_rules(block):
    res, i = [], 0
    while i < len(block):
        j = block.find('{', i)
        if j < 0: res.append(block[i:]); break
        head = block[i:j].strip()
        # find matching brace
        depth, k = 0, j
        while k < len(block):
            if block[k] == '{': depth += 1
            elif block[k] == '}':
                depth -= 1
                if depth == 0: break
            k += 1
        inner = block[j+1:k]
        lead = head.split('*/')[-1] if '*/' in head else head
        comment = head[:len(head)-len(lead)]
        lead = lead.strip()
        if lead.startswith('@keyframes'):
            res.append(f'{comment}{lead}{{{inner}}}')
        elif lead.startswith('@media'):
            res.append(f'{comment}{lead}{{{scope_rules(inner)}}}')
        else:
            sels = ','.join(scope_sel(s) for s in lead.split(','))
            res.append(f'{comment}{sels}{{{inner}}}')
        i = k + 1
    return '\n'.join(res)

scoped = scope_rules(css)
# wrapper-level fixes: clip instead of hidden (keeps sticky header working), reset GHL inherited styles
scoped = scoped.replace(f'{P}{{margin:0;overflow-x:hidden;', f'{P}{{margin:0;overflow-x:clip;')
scoped = scoped.replace(f'{P}{{scroll-behavior:smooth}}', 'html{scroll-behavior:smooth}')
scoped += f'\n/* Full-bleed: ocupa todo el ancho de la pantalla aunque la fila de GHL tenga ancho máximo */\nhtml,body{{overflow-x:clip}}\n{P}{{width:100vw!important;max-width:100vw!important;position:relative;left:50%;right:50%;margin-left:-50vw!important;margin-right:-50vw!important;text-align:left;letter-spacing:normal;font-size:16px}}\n{P} h1,{P} h2,{P} h3,{P} h4{{font-family:var(--font);text-transform:none;color:inherit;letter-spacing:normal;font-style:normal}}\n{P} p,{P} li,{P} blockquote{{color:inherit}}\n{P} img{{border:0;box-shadow:none;border-radius:0;background:none;padding:0;margin:0}}\n{P} svg{{overflow:visible}}\n{P} p,{P} li,{P} a,{P} span,{P} label{{font-family:var(--font)}}\n{P} ul{{margin-top:0}}'

out_html = f'''<!-- ===== TONY VALDES LOANS · {label} · Pegar completo en un elemento "Code" de GHL ===== -->
{fonts}
<style>
{scoped}
</style>
<div id="tvl" lang="es">
{body.strip()}
</div>
'''
open(out, 'w', encoding='utf-8').write(out_html)
print('ok', round(len(out_html)/1024), 'KB')
