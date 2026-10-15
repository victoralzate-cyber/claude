"""Genera la imagen para redes (Open Graph) y el favicon de Tony Valdes Loans.
Uso: python3 seo/build_images.py <carpeta-con-montserrat-ttf>"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); A = os.path.join(HERE, '..', 'assets'); F = sys.argv[1]
BLUE=(3,0,46); GOLD=(176,121,8); JAS=(244,228,120)
def font(w, s): return ImageFont.truetype(os.path.join(F, f'm{w}.ttf'), s)
def grad(w, h):
    g = Image.new('RGB', (w, h)); d = ImageDraw.Draw(g)
    for x in range(w):
        t = x / max(1, w-1)
        c = tuple(int(GOLD[i] + (JAS[i]-GOLD[i]) * t) for i in range(3)); d.line([(x,0),(x,h)], fill=c)
    return g
def gold_text(img, xy, text, f):
    d = ImageDraw.Draw(img); bb = d.textbbox((0,0), text, font=f); w, h = bb[2]-bb[0], bb[3]-bb[1]
    m = Image.new('L', (w, h+20), 0); ImageDraw.Draw(m).text((-bb[0], -bb[1]), text, font=f, fill=255)
    img.paste(grad(w, h+20), xy, m)

# ---- Open Graph 1200x630 ----
W, H = 1200, 630
og = Image.new('RGB', (W, H), BLUE)
glow = Image.new('RGB', (W, H), BLUE); ImageDraw.Draw(glow).ellipse((620, -120, 1320, 580), fill=(30, 24, 120))
og = Image.blend(og, glow.filter(ImageFilter.GaussianBlur(120)), 0.9)
d = ImageDraw.Draw(og)
# casa de marca como marca de agua
wm = Image.new('RGBA', (W, H), (0,0,0,0)); dw = ImageDraw.Draw(wm); c = (244,228,120,22); s = 5.2; ox, oy = 690, 40
for pts in ([(6,44),(50,4),(94,44)], [(33,64),(33,40),(50,23),(67,40),(67,64)], [(19,50),(19,75),(81,75),(81,50)], [(78,10),(78,30)]):
    dw.line([(ox+x*s, oy+y*s) for x,y in pts], fill=c, width=34, joint='curve')
og.paste(wm, (0,0), wm)
# foto de Tony
ph = Image.open(os.path.join(A, 'tony-senalando-frente.webp')).convert('RGBA')
ph = ph.crop((0, 0, ph.width, int(ph.height*0.62))); ph.thumbnail((560, 600))
ring = Image.new('RGBA', (W, H), (0,0,0,0)); ImageDraw.Draw(ring).ellipse((735, 70, 1175, 510), outline=(176,121,8,160), width=3)
og.paste(ring, (0,0), ring)
og.paste(ph, (W - ph.width - 10, H - ph.height - 8), ph)
# logo + textos
lg = Image.open(os.path.join(A, 'logo-tony-valdes-loans.png')).convert('RGBA'); lg.thumbnail((190, 130))
og.paste(lg, (64, 48), lg)
d.text((64, 214), 'Préstamos Inteligentes.', font=font(900, 54), fill=(255,255,255))
gold_text(og, (64, 282), '¡Sí Es Posible!', font(900, 62))
d.text((66, 378), 'Compra de vivienda · Inversión · Self-employed', font=font(600, 24), fill=(217,215,238))
d.text((66, 414), 'Más de 25 años en banca y finanzas', font=font(600, 24), fill=(217,215,238))
d.rounded_rectangle((64, 470, 396, 514), radius=22, outline=(244,228,120), width=2)
d.text((84, 480), 'Español · English · Português', font=font(800, 18), fill=JAS)
d.text((66, 548), 'Tony Valdes · NMLS #1593970 · Loan Factory NMLS #320841', font=font(500, 16), fill=(160,157,196))
og.paste(grad(W, 8), (0, H-8))
og.save(os.path.join(HERE, 'og-tony-valdes-loans.jpg'), quality=90)

# ---- Favicon: la casita del logo sobre azul ----
lg = Image.open(os.path.join(A, 'logo-tony-valdes-loans.png')).convert('RGBA')
a = lg.getchannel('A'); rows = [y for y in range(lg.height) if a.crop((0,y,lg.width,y+1)).getbbox()]
# la casa termina donde empieza el primer hueco vertical grande (antes del texto)
cut = next(y for y in range(rows[0], lg.height) if not a.crop((int(lg.width*.3), y, int(lg.width*.7), y+1)).getbbox())
house = lg.crop((int(lg.width*.28), 0, int(lg.width*.72), cut)); house = house.crop(house.getchannel('A').getbbox())
for size in (512, 180, 32):
    ic = Image.new('RGBA', (size, size), (0,0,0,0)); m = Image.new('L', (size, size), 0)
    ImageDraw.Draw(m).rounded_rectangle((0,0,size-1,size-1), radius=int(size*.22), fill=255)
    bg = Image.new('RGBA', (size, size), BLUE+(255,)); ic.paste(bg, (0,0), m)
    h2 = house.copy(); h2.thumbnail((int(size*.72), int(size*.72)), Image.LANCZOS)
    ic.paste(h2, ((size-h2.width)//2, (size-h2.height)//2), h2)
    ic.save(os.path.join(HERE, f'favicon-{size}.png'))
print('ok')
