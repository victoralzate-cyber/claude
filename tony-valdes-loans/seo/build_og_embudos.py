"""Imágenes para redes (Open Graph 1200x630) de la masterclass y la landing de inversionistas y empresarios.
Uso: python3 seo/build_og_embudos.py"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); A = os.path.join(HERE, '..', 'assets'); F = os.path.join(HERE, 'fonts')
BLUE=(3,0,46); GOLD=(176,121,8); JAS=(244,228,120); WHITE=(255,255,255); SOFT=(217,215,238)
W, H = 1200, 630
def font(w, s): return ImageFont.truetype(os.path.join(F, f'm{w}.ttf'), s)
def grad(w, h):
    g = Image.new('RGB', (w, h)); d = ImageDraw.Draw(g)
    for x in range(w):
        t = x / max(1, w-1); d.line([(x,0),(x,h)], fill=tuple(int(GOLD[i] + (JAS[i]-GOLD[i]) * t) for i in range(3)))
    return g
def gold_text(img, xy, text, f):
    d = ImageDraw.Draw(img); bb = d.textbbox((0,0), text, font=f); w, h = bb[2]-bb[0], bb[3]-bb[1]
    m = Image.new('L', (w, h+24), 0); ImageDraw.Draw(m).text((-bb[0], -bb[1]), text, font=f, fill=255)
    img.paste(grad(w, h+24), xy, m); return w
def background(photo):
    bg = Image.open(os.path.join(A, 'stock', photo)).convert('RGB')
    r = max(W/bg.width, H/bg.height); bg = bg.resize((int(bg.width*r)+1, int(bg.height*r)+1), Image.LANCZOS)
    bg = bg.crop(((bg.width-W)//2, (bg.height-H)//2, (bg.width-W)//2+W, (bg.height-H)//2+H))
    # capa azul: más sólida a la izquierda (texto) y más transparente a la derecha
    ov = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(ov)
    for x in range(W):
        t = x / (W-1); a = int(255*(0.95 - 0.55*t)); d.line([(x,0),(x,H)], fill=BLUE+(a,))
    bg = bg.convert('RGBA'); bg.alpha_composite(ov); return bg
def tony(img, file, box_h, right=24, crop_top=0.0, crop_bottom=1.0):
    ph = Image.open(os.path.join(A, file)).convert('RGBA')
    ph = ph.crop((0, int(ph.height*crop_top), ph.width, int(ph.height*crop_bottom)))
    r = box_h / ph.height; ph = ph.resize((int(ph.width*r), box_h), Image.LANCZOS)
    sh = Image.new('RGBA', ph.size, (0,0,0,0)); sh.putalpha(ph.getchannel('A').point(lambda v: int(v*.55)))
    sh = Image.merge('RGBA', (*Image.new('RGB', ph.size, (0,0,0)).split(), sh.getchannel('A'))).filter(ImageFilter.GaussianBlur(18))
    x = W - ph.width - right; y = H - ph.height
    img.alpha_composite(sh, (x-10, y+6)); img.alpha_composite(ph, (x, y)); return x
def pill(d, xy, text, f, fill, color, pad=(18, 9), outline=None):
    bb = d.textbbox((0,0), text, font=f); w, h = bb[2]-bb[0], bb[3]-bb[1]
    x, y = xy; d.rounded_rectangle((x, y, x+w+pad[0]*2, y+h+pad[1]*2+6), radius=(h+pad[1]*2)//2+3, fill=fill, outline=outline, width=2 if outline else 0)
    d.text((x+pad[0]-bb[0], y+pad[1]-bb[1]+3), text, font=f, fill=color); return x+w+pad[0]*2
def logo(img, xy, w=150):
    lg = Image.open(os.path.join(A, 'logo-tony-valdes-loans.png')).convert('RGBA'); lg.thumbnail((w, w)); img.alpha_composite(lg, xy)
def footer(img, text):
    d = ImageDraw.Draw(img); d.text((60, H-44), text, font=font(500, 15), fill=(170,167,205)); img.paste(grad(W, 8), (0, H-8))

# ---------- 1. Masterclass Inversionistas y Empresarios ----------
img = background('atlanta-noche.webp'); d = ImageDraw.Draw(img)
tony(img, 'tony-senalando-lado.webp', 600, right=-30, crop_bottom=.88)
logo(img, (60, 34), 120)
x = pill(d, (60, 150), 'MASTERCLASS GRATUITA', font(900, 20), JAS, BLUE)
d.ellipse((x+18, 166, x+30, 178), fill=(255,59,48)); d.text((x+38, 158), 'EN VIVO · VÍA ZOOM', font=font(800, 18), fill=WHITE)
d.text((60, 210), 'INVERSIONISTAS', font=font(900, 64), fill=WHITE)
gold_text(img, (60, 282), 'Y EMPRESARIOS', font(900, 64))
d.text((62, 362), 'Cómo identificar oportunidades', font=font(800, 28), fill=WHITE)
d.text((62, 398), 'y financiarlas estratégicamente', font=font(800, 28), fill=WHITE)
box = Image.new('RGBA', (W, H), (0,0,0,0)); ImageDraw.Draw(box).rounded_rectangle((60, 456, 420, 532), radius=14, fill=(255,255,255,28), outline=JAS+(255,), width=2)
img.alpha_composite(box); d = ImageDraw.Draw(img)
d.text((82, 468), 'Jueves 5 de noviembre', font=font(800, 24), fill=JAS)
d.text((82, 500), '7:30 p.m. · Atlanta / Miami', font=font(600, 20), fill=SOFT)
cta = Image.new('RGBA', (250, 56), (0,0,0,0)); m = Image.new('L', (250, 56), 0); ImageDraw.Draw(m).rounded_rectangle((0,0,249,55), radius=28, fill=255)
cta.paste(grad(250, 56), (0,0), m); ImageDraw.Draw(cta).text((125, 29), 'REGÍSTRATE GRATIS', font=font(900, 18), fill=BLUE, anchor='mm')
img.alpha_composite(cta, (446, 466))
footer(img, 'Con Tony Valdes · Ex-VP de Banca Comercial · NMLS #1593970 · Loan Factory NMLS #320841')
img.convert('RGB').save(os.path.join(HERE, 'og-masterclass-inversionistas.jpg'), quality=88)

# ---------- 2. Landing Inversionistas y Empresarios ----------
img = background('casa-moderna-noche.webp'); d = ImageDraw.Draw(img)
tony(img, 'tony-traje-completo.webp', 640, right=70, crop_bottom=.80)
logo(img, (60, 34), 120)
pill(d, (60, 150), 'INVERSIONISTAS Y EMPRESARIOS', font(900, 18), JAS, BLUE)
d.text((60, 206), 'Financiamiento', font=font(900, 60), fill=WHITE)
d.text((60, 272), 'inteligente para', font=font(900, 60), fill=WHITE)
gold_text(img, (60, 338), 'hacer crecer tu capital', font(900, 52))
d.text((64, 420), 'Fix & Flip · DSCR · Multifamily · Construcción', font=font(800, 22), fill=SOFT)
d.text((64, 454), 'Bank Statement · P&L · 1099 · Propiedad comercial', font=font(800, 22), fill=SOFT)
pill(d, (60, 506), 'Ex-Vicepresidente de Banca Comercial', font(800, 18), (255,255,255), BLUE)
footer(img, 'Tony Valdes · NMLS #1593970 · Loan Factory NMLS #320841 · Análisis gratis')
img.convert('RGB').save(os.path.join(HERE, 'og-landing-inversionistas-empresarios.jpg'), quality=88)
print('ok')
