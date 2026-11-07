#!/usr/bin/env python3
"""Pasa una figura de Anatomy (página HTML) a una secuencia PNG con fondo transparente para un plano del estilo
blanco y negro.

El reloj de la página es nuestro: `performance.now`, `Date.now` y `requestAnimationFrame` se reemplazan antes de que
cargue, y cada cuadro avanza exactamente 1/fps de segundo, así que la animación sale igual en cada corrida aunque la
máquina vaya lenta. (`page.clock` de Playwright 1.58 rechaza los milisegundos con este driver.) La tarjeta y el fondo
de la página se vuelven transparentes: el plano pone su papel o su grafito. Usá la página clara de Anatomy (`--light`)
para el papel y la oscura para el grafito.

Uso:
    python3 capturar_anatomy.py <pagina.html> <carpeta_salida> --segundos 4 [--fps 30] [--ancho 1000]
        [--selector .iso-figure] [--antes 0.5] [--accion 'js antes de grabar'] [--color]

`--selector .iso-plate` graba la tarjeta entera, con «Fig 1», el título y la lectura en vivo.

Después, en el mundo del video: precargá los PNG con `loadImage` (como VIRAL en el reel de los cien dólares) y en el
plano dibujá el cuadro `Math.floor((t - inicio) * fps)`.
"""
import argparse
from pathlib import Path

from playwright.sync_api import sync_playwright

RELOJ = """
(() => {
  let t = 0, cola = [], id = 0;
  const base = 1.7e12;
  performance.now = () => t;
  Date.now = () => base + t;
  window.requestAnimationFrame = (cb) => { cola.push([++id, cb]); return id; };
  window.cancelAnimationFrame = (n) => { cola = cola.filter(([k]) => k !== n); };
  // Avanza ms en pasos de 1/60 s, corriendo los requestAnimationFrame de cada paso.
  window.__avanzar = (ms) => {
    const fin = t + ms;
    while (t < fin - 1e-6) {
      t = Math.min(fin, t + 1000 / 60);
      const ahora = cola; cola = [];
      for (const [, cb] of ahora) cb(t);
    }
  };
})();
"""

TRANSPARENTE = (
    "html,body,.iso,.iso *{background:transparent !important}"
    ".iso-plate,.iso-figure{box-shadow:none !important;border-color:transparent !important}"
)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pagina")
    ap.add_argument("salida")
    ap.add_argument("--segundos", type=float, required=True)
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--ancho", type=int, default=1000, help="ancho de la ventana en px CSS; la escala es 2x")
    ap.add_argument("--selector", default=".iso-figure")
    ap.add_argument("--antes", type=float, default=0.5, help="segundos de animación que corren antes del primer cuadro")
    ap.add_argument("--accion", default="", help="JS que se evalúa antes de grabar (abrir el despiece, apretar algo)")
    ap.add_argument("--color", action="store_true", help="conservar el color de los shaders (la lámpara, el fuego); por defecto sale en grises")
    a = ap.parse_args()

    out = Path(a.salida)
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        nav = p.chromium.launch(args=["--use-gl=angle", "--enable-webgl", "--ignore-gpu-blocklist"])
        pag = nav.new_page(viewport={"width": a.ancho, "height": int(a.ancho * 1.25)}, device_scale_factor=2)
        pag.add_init_script(RELOJ)
        pag.goto(Path(a.pagina).resolve().as_uri())
        gris = "" if a.color else f"{a.selector}{{filter:grayscale(1)}}"
        pag.add_style_tag(content=TRANSPARENTE + gris)
        pag.evaluate(f"__avanzar({a.antes * 1000})")
        if a.accion:
            pag.evaluate(a.accion)
        caja = pag.locator(a.selector).first
        caja.scroll_into_view_if_needed()
        n = round(a.segundos * a.fps)
        for i in range(n):
            caja.screenshot(path=str(out / f"{i:04d}.png"), omit_background=True, animations="allow")
            pag.evaluate(f"__avanzar({1000 / a.fps})")
        nav.close()
    print(f"{n} cuadros a {a.fps} fps en {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
