// Formato cinético «Del negocio al activo»: tipografía enorme que golpea con la voz, fondos que cambian de color en
// cada idea (azul noche, amarillo Jasmine, papel), dibujos de línea dorada que se transforman y cámara con empujes.
import * as k from "#kit";
import { v } from "#voz";
import { GlobalFonts, loadImage } from "@napi-rs/canvas";
import * as tn from "../../../estilos/tony-valdes-noche/estilo.mjs" /* copiar a video/mundo.js del proyecto */;

export const tv = tn.tv;
export { tn };
tn.registrar(GlobalFonts);
export const logo = await tn.cargarLogo(loadImage);
export const C = { navy: "#03002E", navy2: "#0B0F4A", amarillo: "#F4E478", oro: "#B07908", papel: "#EFEEEF", blanco: "#FFFFFF" };
export const W = 1080, H = 1920;
export const F = { bold: tv.LETRA.titular, serif: tv.LETRA.serif, cuerpo: tv.LETRA.cuerpo, mono: tn.MONO };
const tramo = k.tramo;
export const salir = (u) => 1 - Math.pow(1 - u, 3);
export const rebote = (u) => (u <= 0 ? 0 : u >= 1 ? 1 : 1 + 2.2 * Math.pow(u - 1, 3) + 1.2 * Math.pow(u - 1, 2));

// Fondo de color plano con textura: «navy» con resplandor y grano, «amarillo» con rayas diagonales suaves, «papel»
// con cuadrícula.
export function fondo(g, tipo, t) {
  g.save(); g.setTransform(1, 0, 0, 1, 0, 0);
  if (tipo === "navy") { tn.fondo(g, t); }
  else if (tipo === "amarillo") {
    g.fillStyle = C.amarillo; g.fillRect(0, 0, W, H);
    g.strokeStyle = "rgba(176,121,8,0.12)"; g.lineWidth = 26; const o = (t * 60) % 120;
    for (let x = -H; x < W + H; x += 120) { g.beginPath(); g.moveTo(x + o, 0); g.lineTo(x + o - H * 0.6, H); g.stroke(); }
  } else { tv.fondo(g, { corre: t * 20 }); }
  g.restore();
}

// Palabra que GOLPEA: entra grande y borrosa, se encoge con rebote a su sitio. align: "left" | "center".
export function golpe(g, txt, x, y, { t, t0, tam = 160, font = "bold", color = C.blanco, align = "left", dur = 0.22, contorno = null, salida = null } = {}) {
  if (t < t0 - 0.05) return 0;
  const u = tramo(t, t0 - 0.05, t0 - 0.05 + dur), s = 1 + 0.9 * (1 - rebote(u));
  const out = salida ? tramo(t, salida, salida + 0.15) : 0;
  if (out >= 1) return 0;
  g.save(); g.globalAlpha = Math.min(1, u * 2.5) * (1 - out);
  g.font = font === "serif" ? `400 ${tam * 1.1}px "${F.serif}"` : `800 ${tam}px "${F.bold}"`;
  g.letterSpacing = font === "serif" ? "0px" : `${-tam * 0.04}px`;
  const w = g.measureText(txt).width, ax = align === "center" ? x : x + w / 2;
  g.translate(ax, y); g.scale(s, s); g.translate(-ax, -y);
  if (u < 1) g.filter = `blur(${(10 * (1 - u)).toFixed(1)}px)`;
  g.textAlign = align; g.textBaseline = "alphabetic";
  if (contorno) { g.lineWidth = tam * 0.04; g.strokeStyle = contorno; g.strokeText(txt, x, y); }
  if (color === "oro") { const gr = g.createLinearGradient(x - (align === "center" ? w / 2 : 0), y - tam, x + w, y); gr.addColorStop(0, "#B07908"); gr.addColorStop(0.45, "#F4E478"); gr.addColorStop(0.7, "#FFF1A8"); gr.addColorStop(1, "#C9961E"); g.fillStyle = gr; }
  else g.fillStyle = color;
  if (color !== "hueco") g.fillText(txt, x, y);
  g.restore();
  return w;
}

// Sacudida de cámara breve en cada golpe fuerte.
export function sacudida(g, t, golpes, amp = 14) {
  let dx = 0, dy = 0;
  for (const t0 of golpes) { const e = Math.exp(-Math.pow((t - t0 - 0.06) / 0.09, 2)); dx += Math.sin(t * 90) * amp * e; dy += Math.cos(t * 77) * amp * e; }
  g.translate(dx, dy);
}

// Destello de corte (pantalla completa) y barrido de color (para pasar de un fondo a otro).
export function destello(g, t, t0, color = "255,255,255") {
  const e = Math.exp(-Math.pow((t - t0) / 0.06, 2)); if (e < 0.02) return;
  g.save(); g.setTransform(1, 0, 0, 1, 0, 0); g.fillStyle = `rgba(${color},${0.6 * e})`; g.fillRect(0, 0, W, H); g.restore();
}

// Pie fijo y discreto: usuario + barra de avance.
export function firma(g, t, claro = false) {
  g.save(); g.setTransform(1, 0, 0, 1, 0, 0);
  const lw = 40, lh = (logo.height / logo.width) * lw; g.drawImage(logo, 84, 1748 - lh / 2, lw, lh);
  g.font = `600 26px "${F.cuerpo}"`; g.fillStyle = claro ? C.navy : C.blanco; g.textBaseline = "middle"; g.fillText("@tonyvaldesloans", 136, 1749);
  g.fillStyle = claro ? "rgba(3,0,46,0.15)" : "rgba(255,255,255,0.18)"; g.fillRect(84, 1790, 912, 4);
  g.fillStyle = claro ? C.navy : C.amarillo; g.fillRect(84, 1790, 912 * Math.min(1, t / v.duracion), 4);
  g.restore();
}

// Dibujos de línea dorada (usan el trazo del estilo nocturno: se dibujan con u 0→1).
export const trazo = tn.trazo;
export const rect = (x, y, w, h) => [[x, y], [x + w, y], [x + w, y + h], [x, y + h], [x, y]];
