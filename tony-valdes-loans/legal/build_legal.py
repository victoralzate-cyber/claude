"""Genera las páginas legales (Términos y Privacidad) en ES/EN/PT.

Uso (desde tony-valdes-loans/):  python3 legal/build_legal.py
Salida por página:
  legal/<slug>.html       página completa para revisar en el navegador
  legal/ghl-<slug>.html   fragmento para pegar en un elemento "Code" de GHL
"""
import base64, io, os, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from legal_content import PAGES, EFFECTIVE, CONTACT, UI

LANGS = ("es", "en", "pt")


def logo_uri():
    im = Image.open(os.path.join(HERE, "..", "assets", "logo-tony-valdes-loans.png"))
    im.thumbnail((360, 360))
    buf = io.BytesIO(); im.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


CSS = """
#tvll{--blue:#03002E;--blue-2:#0A0745;--gold:#B07908;--jasmine:#F4E478;--gold-grad:linear-gradient(90deg,#B07908 0%,#D9B23F 50%,#F4E478 100%);--ink:#03002E;--ink-soft:#3D3B5C;--paper:#F7F6F1;--font:"Montserrat",system-ui,-apple-system,"Segoe UI",sans-serif;
  width:100vw!important;max-width:100vw!important;position:relative;left:50%;right:50%;margin-left:-50vw!important;margin-right:-50vw!important;
  font-family:var(--font);color:var(--ink);background:var(--paper);line-height:1.7;font-size:16px;text-align:left;-webkit-font-smoothing:antialiased}
html,body{overflow-x:clip}
#tvll *,#tvll *::before,#tvll *::after{box-sizing:border-box}
#tvll h1,#tvll h2,#tvll p,#tvll li,#tvll a,#tvll strong{font-family:var(--font);text-transform:none;letter-spacing:normal}
#tvll img{border:0;box-shadow:none;max-width:100%}
#tvll .lg-top{background:var(--blue);border-bottom:1px solid rgba(244,228,120,.18)}
#tvll .lg-wrap{max-width:880px;margin:0 auto;padding:0 20px}
#tvll .lg-top .lg-wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-top:14px;padding-bottom:14px;flex-wrap:wrap}
#tvll .lg-logo img{height:56px;width:auto;display:block}
#tvll .lg-tools{display:flex;align-items:center;gap:16px;flex-wrap:wrap}
#tvll .lg-back{color:#E9E7F7;text-decoration:none;font-weight:700;font-size:.88rem}
#tvll .lg-back:hover{color:var(--jasmine)}
#tvll .lang-switch{display:inline-flex;border:1px solid rgba(244,228,120,.45);border-radius:999px;padding:3px;gap:2px}
#tvll .lang-switch button{font-family:inherit;font-size:.74rem;font-weight:800;letter-spacing:.06em;color:#E9E7F7;background:transparent;border:0;border-radius:999px;padding:6px 10px;cursor:pointer;line-height:1}
#tvll .lang-switch button[aria-pressed="true"]{background:var(--gold-grad);color:var(--blue)}
#tvll .lg-hero{background:var(--blue);color:#fff;padding:46px 0 54px;position:relative}
#tvll .lg-hero::after{content:"";position:absolute;left:0;right:0;bottom:0;height:5px;background:var(--gold-grad)}
#tvll .lg-hero h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:900;margin:0 0 8px;color:#fff}
#tvll .lg-hero p{margin:0;color:#CFCDE6;font-size:.92rem}
#tvll .lg-card{background:#fff;border-radius:16px;box-shadow:0 18px 50px rgba(3,0,46,.12);padding:40px 44px;margin:-26px auto 0;position:relative;z-index:1}
#tvll .lg-intro{font-size:1.05rem;color:var(--ink-soft);border-left:4px solid var(--gold);padding-left:16px;margin:0 0 28px}
#tvll h2{font-size:1.15rem;font-weight:800;margin:30px 0 10px;color:var(--ink)}
#tvll p{margin:0 0 12px;color:var(--ink-soft)}
#tvll ul{margin:0 0 12px;padding-left:22px}
#tvll li{margin-bottom:6px;color:var(--ink-soft)}
#tvll a{color:#083FB0}
#tvll strong{color:var(--ink)}
#tvll .lg-other{display:inline-block;margin-top:26px;font-weight:800;color:var(--blue);text-decoration:none;border-bottom:2px solid var(--gold)}
#tvll .lg-foot{text-align:center;font-size:.78rem;color:#77749A;padding:30px 20px 40px}
#tvll [data-l]{display:none}
#tvll[data-lang="es"] [data-l="es"],#tvll[data-lang="en"] [data-l="en"],#tvll[data-lang="pt"] [data-l="pt"]{display:block}
#tvll :focus-visible{outline:3px solid var(--jasmine);outline-offset:3px}
@media (max-width:600px){#tvll .lg-card{padding:28px 20px;border-radius:12px}#tvll .lg-logo img{height:44px}}
"""

JS = """
<script>
(function(){
  var root=document.getElementById('tvll'), L=['es','en','pt'];
  function setLang(l){
    if(L.indexOf(l)<0) l='es';
    root.setAttribute('data-lang',l); root.setAttribute('lang',l);
    root.querySelectorAll('.lang-switch button').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-lang')===l?'true':'false')});
    try{localStorage.setItem('tvl-lang',l)}catch(e){}
  }
  root.querySelectorAll('.lang-switch button').forEach(function(b){b.addEventListener('click',function(){setLang(b.getAttribute('data-lang'))})});
  var start='es';
  try{var q=new URLSearchParams(location.search).get('lang');var s=localStorage.getItem('tvl-lang');start=(q&&L.indexOf(q)>=0)?q:((s&&L.indexOf(s)>=0)?s:'es')}catch(e){}
  setLang(start);
})();
</script>
"""


def spans(d):
    return "".join(f'<span data-l="{l}" lang="{l}">{d[l]}</span>' for l in LANGS)


def build(slug):
    pg = PAGES[slug]
    other = "terminos" if slug == "privacidad" else "privacidad"
    body = []
    for l in LANGS:
        parts = [f'<p class="lg-intro">{pg["intro"][l]}</p>']
        for s in pg["sections"]:
            parts.append(f'<h2>{s["h"][l]}</h2>')
            if "pre" in s:
                parts.append(s["pre"][l])
            parts.append(CONTACT[l] if s["b"] == "CONTACT" else s["b"][l])
        parts.append(f'<a class="lg-other" href="/{other}">{UI["other"][slug][l]}</a>')
        body.append(f'<div data-l="{l}" lang="{l}">' + "\n".join(parts) + "</div>")

    fragment = f"""<!-- ===== TONY VALDES LOANS · {pg['title']['es'].upper()} · Pegar completo en un elemento "Code" de GHL ===== -->
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
<div id="tvll" data-lang="es" lang="es">
  <div class="lg-top"><div class="lg-wrap">
    <a class="lg-logo" href="/"><img src="{logo_uri()}" alt="Tony Valdes Loans"></a>
    <div class="lg-tools">
      <a class="lg-back" href="/">{spans(UI['back'])}</a>
      <div class="lang-switch" role="group" aria-label="Idioma / Language / Idioma"><button type="button" data-lang="es" aria-pressed="true">ES</button><button type="button" data-lang="en" aria-pressed="false">EN</button><button type="button" data-lang="pt" aria-pressed="false">PT</button></div>
    </div>
  </div></div>
  <div class="lg-hero"><div class="lg-wrap"><h1>{spans(pg['title'])}</h1><p>{spans(EFFECTIVE)}</p></div></div>
  <div class="lg-wrap"><div class="lg-card">
{chr(10).join(body)}
  </div></div>
  <div class="lg-foot">© <span class="lg-year">2026</span> Tony Valdes Loans. {spans(UI['rights'])} · NMLS #1593970 · Loan Factory, Inc. NMLS #320841 · Equal Housing Opportunity</div>
</div>
{JS}<script>document.querySelectorAll('#tvll .lg-year').forEach(function(e){{e.textContent=new Date().getFullYear()}})</script>
"""
    with open(os.path.join(HERE, f"ghl-{slug}.html"), "w", encoding="utf-8") as f:
        f.write(fragment)
    full = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{pg['title']['es']} | Tony Valdes Loans</title><style>body{{margin:0;background:#F7F6F1}}</style></head>
<body>
{fragment}
</body></html>
"""
    with open(os.path.join(HERE, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(full)
    print(slug, round(len(fragment) / 1024), "KB")


if __name__ == "__main__":
    for slug in PAGES:
        build(slug)
