// Estilo «Tony Valdes · noche»: el carrusel nocturno de @tonyvaldesloans («Estrategia de adquisición», 2026-11)
// llevado a video. Azul muy oscuro con resplandor, cuadrícula tenue, rótulo en mono con punto dorado, logo dorado
// arriba a la derecha, titular blanco con la cursiva en degradado dorado, paneles oscuros con dibujos de línea dorados,
// filas numeradas con check y el pie con avance «01 / 05». Reusa la letra y el titular del estilo claro.
//
//   import * as tn from "../../../estilos/tony-valdes-noche/estilo.mjs";
//   tn.registrar(GlobalFonts);  const logo = await tn.cargarLogo(loadImage);
//   tn.fondo(g, t); tn.rotulo(g, "Objetivo 1", u); tn.logo(g, logo);
//   tn.titulo(g, ["Propiedad para", { it: "operar" }, "tu negocio."], y, { t, desde });
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as tv from "../tony-valdes/estilo.mjs";

const AQUI = dirname(fileURLToPath(import.meta.url));
export { tv };
export const W = 1080, H = 1920, M = 84;

export const C = {
  fondo0: "#02012A", fondo1: "#07094D",
  resplandor: "48,64,210",
  grilla: "rgba(130,140,255,0.055)",
  blanco: "#FFFFFF",
  texto: "#AEB3D6",          // párrafos
  rotulo: "#C9CCEA",
  panel: "rgba(12,14,74,0.82)", borde: "rgba(150,160,255,0.16)",
  oro: "#F4E478", oroOscuro: "#B07908",
  azul: "#7888F4",
};
export const MONO = "TVN Mono";

export function registrar(GlobalFonts) {
  tv.registrar(GlobalFonts);
  GlobalFonts.registerFromPath(join(AQUI, "..", "blanco-y-negro", "letra", "JetBrainsMono-Regular.ttf"), MONO);
}
export const cargarLogo = (loadImage) => loadImage(join(AQUI, "..", "tony-valdes", "logo.png"));

const tramo = (t, a, b) => Math.max(0, Math.min(1, (t - a) / (b - a)));
export const salir = (u) => 1 - Math.pow(1 - u, 3);
export const entra = (t, a, d = 0.45) => salir(tramo(t, a, a + d));
const limpio = (g) => { g.setTransform(1, 0, 0, 1, 0, 0); g.globalAlpha = 1; g.filter = "none"; g.letterSpacing = "0px"; g.shadowColor = "transparent"; };
export function oro(g, x0, y0, x1, y1) {
  const gr = g.createLinearGradient(x0, y0, x1, y1);
  gr.addColorStop(0, "#B07908"); gr.addColorStop(0.45, "#F4E478"); gr.addColorStop(0.7, "#FFF1A8"); gr.addColorStop(1, "#C9961E");
  return gr;
}

// Fondo: degradado azul noche, resplandor azul abajo (respira despacio) y cuadrícula tenue.
export function fondo(g, t = 0, { corre = 0 } = {}) {
  g.save(); limpio(g);
  const bg = g.createLinearGradient(0, 0, 0, H); bg.addColorStop(0, C.fondo0); bg.addColorStop(0.6, "#040340"); bg.addColorStop(1, C.fondo1);
  g.fillStyle = bg; g.fillRect(0, 0, W, H);
  const r = 0.26 + 0.04 * Math.sin(t * 0.8);
  const gl = g.createRadialGradient(540, 1500, 50, 540, 1500, 1100); gl.addColorStop(0, `rgba(${C.resplandor},${r})`); gl.addColorStop(1, `rgba(${C.resplandor},0)`);
  g.fillStyle = gl; g.fillRect(0, 0, W, H);
  const gl2 = g.createRadialGradient(900, 300, 20, 900, 300, 700); gl2.addColorStop(0, "rgba(48,64,210,0.12)"); gl2.addColorStop(1, "rgba(48,64,210,0)");
  g.fillStyle = gl2; g.fillRect(0, 0, W, H);
  g.strokeStyle = C.grilla; g.lineWidth = 1.5; g.beginPath();
  const p = 72, o = ((t * 6 + corre) % p + p) % p;
  for (let x = -o; x < W; x += p) { g.moveTo(x, 0); g.lineTo(x, H); }
  for (let y = -o; y < H; y += p) { g.moveTo(0, y); g.lineTo(W, y); }
  g.stroke();
  g.restore();
}

// Rótulo de sección: punto dorado + mayúsculas en mono con interletra abierta.
export function rotulo(g, texto, u = 1, { x = M, y = 300 } = {}) {
  if (u <= 0) return;
  g.save(); limpio(g); g.globalAlpha = u; g.translate(-20 * (1 - u), 0);
  g.fillStyle = C.oro; g.beginPath(); g.arc(x + 7, y, 7, 0, 7); g.fill();
  g.font = `400 30px "${MONO}"`; g.letterSpacing = "5px"; g.fillStyle = C.rotulo; g.textBaseline = "middle"; g.textAlign = "left";
  g.fillText(String(texto).toUpperCase(), x + 30, y + 1);
  g.restore();
}

// Logo dorado arriba a la derecha.
export function logo(g, img, { x = W - M, y = 236, w = 170, al = 1 } = {}) {
  const h = (img.height / img.width) * w;
  g.save(); limpio(g); g.globalAlpha = al; g.drawImage(img, x - w, y, w, h); g.restore();
}

// Titular blanco, con la cursiva en degradado dorado y sin marcador.
export const titulo = (g, partes, y, o = {}) => tv.titulo(g, partes, M, y, { color: C.blanco, colorIt: "oro", marca: false, tam: 104, ...o });
export const parrafo = (g, texto, y, o = {}) => tv.parrafo(g, texto, M, y, { tam: 38, color: C.texto, fuerte: C.blanco, ...o });

// Panel oscuro con borde fino y cuadrícula interior; u lo hace subir y aparecer.
export function panel(g, x, y, w, h, { u = 1, r = 30, grilla = true } = {}) {
  if (u <= 0) return 0;
  const dy = 40 * (1 - salir(u));
  g.save(); limpio(g); g.globalAlpha = u;
  g.shadowColor = "rgba(0,0,20,0.5)"; g.shadowBlur = 40; g.shadowOffsetY = 14;
  g.fillStyle = C.panel; g.beginPath(); g.roundRect(x, y + dy, w, h, r); g.fill(); g.shadowColor = "transparent";
  g.strokeStyle = C.borde; g.lineWidth = 2; g.stroke();
  if (grilla) {
    g.save(); g.clip(); g.strokeStyle = "rgba(130,140,255,0.06)"; g.lineWidth = 1.2; g.beginPath();
    for (let xx = x + 36; xx < x + w; xx += 48) { g.moveTo(xx, y + dy); g.lineTo(xx, y + dy + h); }
    for (let yy = y + dy + 36; yy < y + dy + h; yy += 48) { g.moveTo(x, yy); g.lineTo(x + w, yy); }
    g.stroke(); g.restore();
  }
  g.restore();
  return dy;
}

// Fila numerada: «01  El tipo de préstamo  ✓». check: 0→1 hace aparecer el check (amarillo o azul).
export function fila(g, n, texto, y, { u = 1, check = 0, azul = false, x = M, w = W - 2 * M } = {}) {
  if (u <= 0) return;
  const h = 96;
  panel(g, x, y, w, h, { u, r: 20, grilla: false });
  const dy = 40 * (1 - salir(u));
  g.save(); limpio(g); g.globalAlpha = u;
  g.font = `400 28px "${MONO}"`; g.fillStyle = azul ? C.azul : C.oro; g.textBaseline = "middle"; g.textAlign = "left";
  g.fillText(String(n).padStart(2, "0"), x + 30, y + dy + h / 2 + 1);
  g.font = `700 40px "${tv.LETRA.titular2}"`; g.fillStyle = C.blanco; g.fillText(texto, x + 96, y + dy + h / 2 + 2);
  if (check > 0) {
    const s = salir(check), cx = x + w - 52, cy = y + dy + h / 2;
    g.save(); g.translate(cx, cy); g.scale(0.6 + 0.4 * s, 0.6 + 0.4 * s);
    g.fillStyle = azul ? C.azul : C.oro; g.beginPath(); g.arc(0, 0, 22, 0, 7); g.fill();
    g.strokeStyle = "#03002E"; g.lineWidth = 5; g.lineCap = "round"; g.lineJoin = "round";
    g.beginPath(); g.moveTo(-9, 0); g.lineTo(-2, 8); g.lineTo(10, -8); g.stroke(); g.restore();
  }
  g.restore();
}

// Pie: logo pequeño + usuario + guiones de avance + «01 / 05» en mono.
export function pie(g, img, n, total, { y = 1750, avance = null } = {}) {
  g.save(); limpio(g);
  const lw = 44, lh = (img.height / img.width) * lw; g.drawImage(img, M, y - lh / 2, lw, lh);
  g.font = `600 28px "${tv.LETRA.cuerpo}"`; g.fillStyle = C.blanco; g.textBaseline = "middle"; g.textAlign = "left";
  g.fillText("tonyvaldesloans", M + 58, y + 1);
  const x0 = M + 300, dw = 42, gap = 12;
  for (let i = 0; i < total; i++) {
    g.fillStyle = i === n - 1 ? C.oro : "rgba(174,179,214,0.25)";
    g.fillRect(x0 + i * (dw + gap), y - 2, dw, 4);
  }
  if (avance != null) { g.fillStyle = "rgba(244,228,120,0.5)"; g.fillRect(x0, y + 10, (total * (dw + gap) - gap) * Math.max(0, Math.min(1, avance)), 2); }
  g.font = `400 28px "${MONO}"`; g.letterSpacing = "3px"; g.fillStyle = C.rotulo; g.textAlign = "right";
  g.fillText(`${String(n).padStart(2, "0")} / ${String(total).padStart(2, "0")}`, W - M, y + 1);
  g.restore();
}

// Trazo dorado de línea que se dibuja: pts en coordenadas absolutas; u 0→1 cuánto del camino se ve.
export function trazo(g, pts, u, { ancho = 8, cerrado = false } = {}) {
  if (u <= 0) return;
  const p = cerrado ? [...pts, pts[0]] : pts;
  let largo = 0; for (let i = 1; i < p.length; i++) largo += Math.hypot(p[i][0] - p[i - 1][0], p[i][1] - p[i - 1][1]);
  g.save(); g.lineWidth = ancho; g.lineCap = "round"; g.lineJoin = "round";
  const xs = p.map((q) => q[0]), ys = p.map((q) => q[1]);
  g.strokeStyle = oro(g, Math.min(...xs), Math.min(...ys), Math.max(...xs), Math.max(...ys));
  g.shadowColor = "rgba(244,228,120,0.35)"; g.shadowBlur = 14;
  g.setLineDash([largo, largo]); g.lineDashOffset = largo * (1 - Math.min(1, u));
  g.beginPath(); p.forEach(([x, y], i) => (i ? g.lineTo(x, y) : g.moveTo(x, y))); g.stroke();
  g.restore();
}

// Comentario que se escribe (barra oscura con «Publicar» dorado) y la notificación del mensaje directo (tarjeta blanca).
export function comentario(g, img, texto, y, letras, publicado, { x = M, w = W - 2 * M, al = 1 } = {}) {
  if (al <= 0) return;
  g.save(); limpio(g); g.globalAlpha = al;
  g.fillStyle = "rgba(12,14,74,0.9)"; g.beginPath(); g.roundRect(x, y, w, 96, 48); g.fill();
  g.strokeStyle = C.borde; g.lineWidth = 2; g.stroke();
  const lw = 40, lh = (img.height / img.width) * lw; g.drawImage(img, x + 28, y + 48 - lh / 2, lw, lh);
  const tx = texto.slice(0, letras);
  g.font = `700 38px "${tv.LETRA.titular2}"`; g.fillStyle = C.blanco; g.textBaseline = "middle"; g.textAlign = "left";
  g.fillText(tx, x + 92, y + 50);
  if (!publicado) { const cw = g.measureText(tx).width; g.fillRect(x + 96 + cw, y + 28, 3, 44); }
  g.font = `700 32px "${tv.LETRA.titular2}"`; g.fillStyle = publicado ? C.oro : "rgba(244,228,120,0.55)"; g.textAlign = "right"; g.fillText("Publicar", x + w - 36, y + 50);
  g.restore();
}
export function mensaje(g, img, texto, y, u, { x = M, w = W - 2 * M } = {}) {
  if (u <= 0) return;
  const dy = 30 * (1 - salir(u));
  g.save(); limpio(g); g.globalAlpha = u;
  g.shadowColor = "rgba(0,0,30,0.5)"; g.shadowBlur = 30; g.shadowOffsetY = 10;
  g.fillStyle = "#FFFFFF"; g.beginPath(); g.roundRect(x, y + dy, w, 130, 28); g.fill(); g.shadowColor = "transparent";
  g.fillStyle = "#03002E"; g.beginPath(); g.arc(x + 62, y + dy + 65, 36, 0, 7); g.fill();
  const lw = 46, lh = (img.height / img.width) * lw; g.drawImage(img, x + 62 - lw / 2, y + dy + 65 - lh / 2, lw, lh);
  g.textAlign = "left"; g.textBaseline = "middle";
  g.font = `700 28px "${tv.LETRA.titular2}"`; g.fillStyle = "#03002E"; g.fillText("tonyvaldesloans", x + 116, y + dy + 46);
  const nw = g.measureText("tonyvaldesloans").width;
  g.font = `400 26px "${tv.LETRA.cuerpo}"`; g.fillStyle = "#6B6E8F"; g.fillText(" te envió un mensaje · ahora", x + 116 + nw, y + dy + 46);
  g.font = `500 32px "${tv.LETRA.cuerpo}"`; g.fillStyle = "#03002E"; g.fillText(texto, x + 116, y + dy + 90);
  g.fillStyle = "#03002E"; g.beginPath(); g.roundRect(x + w - 82, y + dy + 42, 50, 50, 12); g.fill();
  g.strokeStyle = "#FFFFFF"; g.lineWidth = 3; g.lineJoin = "round"; g.beginPath();
  g.moveTo(x + w - 70, y + dy + 66); g.lineTo(x + w - 44, y + dy + 54); g.lineTo(x + w - 56, y + dy + 82); g.lineTo(x + w - 60, y + dy + 70); g.closePath(); g.stroke();
  g.restore();
}

// Aviso legal pequeño.
export function aviso(g, texto, u = 1, y = 1420) {
  if (u <= 0) return;
  g.save(); limpio(g); g.globalAlpha = u * 0.9; g.font = `400 25px "${tv.LETRA.cuerpo}"`; g.fillStyle = "#8C90B8"; g.textAlign = "center"; g.textBaseline = "middle";
  g.fillText(texto, 540, y); g.restore();
}
