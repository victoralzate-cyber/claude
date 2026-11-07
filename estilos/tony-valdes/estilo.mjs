// Estilo «Tony Valdes» para reels-explicativos: el formato de los carruseles de @tonyvaldesloans llevado a video.
// Medido sobre «Guía para empezar a invertir en bienes raíces» (PDF de 10 láminas, 2026-11-07). El canon está en
// tony-valdes.md, al lado. Sin imports del kit: el mundo le pasa GlobalFonts de @napi-rs/canvas.
//
//   import { GlobalFonts, loadImage } from "@napi-rs/canvas";
//   import * as tv from "../../../estilos/tony-valdes/estilo.mjs";
//   tv.registrar(GlobalFonts);                      // una vez, en mundo.js
//   tv.fondo(g); tv.cabecera(g, { avatar });        // en cada plano, primero
//   tv.etiqueta(g, "La idea clave", 96, 420, u);
//   tv.titulo(g, ["Un ingreso se gasta.", "El", { it: "patrimonio" }, "se queda."], 96, 520, { t, desde });
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const AQUI = dirname(fileURLToPath(import.meta.url));
const BN = join(AQUI, "..", "blanco-y-negro", "letra");

// Estructura medida en las láminas; colores de la paleta de marca (brandbook Tony Valdes Loans): el naranja de los
// carruseles pasa a amarillo Jasmine y los oscuros a azul Cetacean.
export const C = {
  fondo: "#EFEEEF",        // papel gris
  grilla: "#DDDEE8",       // cuadrícula fina, apenas azulada
  tinta: "#03002E",        // Cetacean Blue: titulares y texto fuerte
  texto: "#2C2B45",        // cuerpo
  suave: "#7D7C92",        // pie, notas
  amarillo: "#F4E478",     // Jasmine: íconos, subrayado de la cursiva, fila del total
  oro: "#B07908",          // Philippine Gold: flechas, «Sigue →», barra de avance (amarillo que se lee sobre claro)
  azul: "#083FB0",         // Cobalt Blue: montos negativos, tilde de verificado
  celeste: "#7888F4",      // Cornflower Blue: acentos suaves
  tarjeta: "#FFFFFF",
  oscura: "#03002E",       // placa del llamado a la acción y encabezado de tablas
  resalta: "#F4E478",
  verificado: "#083FB0",
};

export const LETRA = { titular: "TV Titular", titular2: "TV Titular Bold", serif: "TV Serif", cuerpo: "TV Cuerpo" };

export function registrar(GlobalFonts) {
  GlobalFonts.registerFromPath(join(BN, "InterDisplay-ExtraBold.ttf"), LETRA.titular);
  GlobalFonts.registerFromPath(join(BN, "InterDisplay-Bold.ttf"), LETRA.titular2);
  GlobalFonts.registerFromPath(join(AQUI, "letra", "InstrumentSerif-Italic.ttf"), LETRA.serif);
  GlobalFonts.registerFromPath(join(AQUI, "letra", "Inter.ttf"), LETRA.cuerpo);
}

export const W = 1080, H = 1920, M = 84; // lienzo y margen lateral
const tramo = (t, a, b) => Math.max(0, Math.min(1, (t - a) / (b - a)));
export const salir = (u) => 1 - Math.pow(1 - u, 3);
export const entra = (t, a, dur = 0.45) => salir(tramo(t, a, a + dur));

function limpio(g) { g.setTransform(1, 0, 0, 1, 0, 0); g.globalAlpha = 1; g.filter = "none"; g.letterSpacing = "0px"; }
function redondo(g, x, y, w, h, r) { g.beginPath(); g.roundRect(x, y, w, h, r); }

// Papel con la cuadrícula fina de las láminas. `corre` desplaza la grilla (paneo lento entre ideas).
export function fondo(g, { paso = 64, corre = 0 } = {}) {
  g.save(); limpio(g);
  g.fillStyle = C.fondo; g.fillRect(0, 0, W, H);
  g.strokeStyle = C.grilla; g.lineWidth = 1.5;
  const o = ((corre % paso) + paso) % paso;
  g.beginPath();
  for (let x = -o; x < W; x += paso) { g.moveTo(x, 0); g.lineTo(x, H); }
  for (let y = -o; y < H; y += paso) { g.moveTo(0, y); g.lineTo(W, y); }
  g.stroke();
  g.restore();
}

// Arriba: avatar + @usuario (con tilde azul) a la izquierda y la serie a la derecha, en dos renglones.
export function cabecera(g, { avatar = null, usuario = "@tonyvaldesloans", serie = ["De ingresos", "a patrimonio"], y = 150, verificado = true } = {}) {
  g.save(); limpio(g);
  const r = 34, cx = M + r;
  g.save(); g.beginPath(); g.arc(cx, y, r, 0, Math.PI * 2); g.clip();
  if (avatar) {
    const s = Math.max((2 * r) / avatar.width, (2 * r) / avatar.height);
    g.drawImage(avatar, cx - (avatar.width * s) / 2, y - (avatar.height * s) / 2, avatar.width * s, avatar.height * s);
  } else { g.fillStyle = C.oscura; g.fill(); g.fillStyle = "#fff"; g.font = `700 30px "${LETRA.titular2}"`; g.textAlign = "center"; g.textBaseline = "middle"; g.fillText("TV", cx, y + 1); }
  g.restore();
  g.font = `500 31px "${LETRA.cuerpo}"`; g.fillStyle = C.texto; g.textBaseline = "middle"; g.textAlign = "left";
  g.fillText(usuario, cx + r + 20, y);
  if (verificado) {
    const vx = cx + r + 20 + g.measureText(usuario).width + 22;
    g.fillStyle = C.verificado; g.beginPath(); g.arc(vx, y, 13, 0, Math.PI * 2); g.fill();
    g.strokeStyle = "#fff"; g.lineWidth = 3.5; g.lineCap = "round"; g.lineJoin = "round";
    g.beginPath(); g.moveTo(vx - 6, y); g.lineTo(vx - 1.5, y + 5); g.lineTo(vx + 6.5, y - 5); g.stroke();
  }
  g.textAlign = "right"; g.font = `400 27px "${LETRA.cuerpo}"`; g.fillStyle = C.texto;
  serie.forEach((s, i) => g.fillText(s, W - M, y - 16 + i * 32));
  g.restore();
}

// Abajo: «03/10» a la izquierda y «Sigue →» a la derecha. En video, `avance` 0→1 dibuja además una barra fina.
export function pie(g, { izq = "", der = "Sigue →", avance = null, y = 1800 } = {}) {
  g.save(); limpio(g);
  g.font = `400 27px "${LETRA.cuerpo}"`; g.textBaseline = "middle";
  g.fillStyle = C.suave; g.textAlign = "left"; g.fillText(izq, M, y);
  g.fillStyle = C.oro; g.textAlign = "right"; g.fillText(der, W - M, y);
  if (avance != null) {
    g.fillStyle = "rgba(3,0,46,0.08)"; redondo(g, M, y + 40, W - 2 * M, 5, 3); g.fill();
    g.fillStyle = C.oro; redondo(g, M, y + 40, (W - 2 * M) * Math.max(0, Math.min(1, avance)), 5, 3); g.fill();
  }
  g.restore();
}

// La pastilla «→ LA IDEA CLAVE»: borde de tinta, fondo claro, flecha dorada. Entra con u (0→1) desde la izquierda.
export function etiqueta(g, texto, x, y, u = 1) {
  if (u <= 0) return 0;
  g.save(); limpio(g);
  g.font = `700 29px "${LETRA.titular2}"`; g.letterSpacing = "0.5px";
  const t = String(texto).toUpperCase(), w = g.measureText(t).width + 100, h = 60;
  g.globalAlpha = u; g.translate(-24 * (1 - u), 0);
  g.fillStyle = "#F7F6F6"; redondo(g, x, y, w, h, 10); g.fill();
  g.strokeStyle = C.tinta; g.lineWidth = 2.5; g.stroke();
  flecha(g, x + 34, y + h / 2, 22, C.oro);
  g.fillStyle = C.tinta; g.textBaseline = "middle"; g.textAlign = "left"; g.fillText(t, x + 60, y + h / 2 + 1);
  g.restore();
  return w;
}

export function flecha(g, x, y, l, color) {
  g.save(); g.strokeStyle = color; g.lineWidth = 4; g.lineCap = "round"; g.lineJoin = "round";
  g.beginPath(); g.moveTo(x - l / 2, y); g.lineTo(x + l / 2, y); g.moveTo(x + l / 2 - 8, y - 8); g.lineTo(x + l / 2, y); g.lineTo(x + l / 2 - 8, y + 8); g.stroke();
  g.restore();
}

// Titular: grotesca negrísima apretada, con UNA palabra (o dos) en cursiva serif con marcador amarillo a mano.
//   partes: ["Revisa tus", { it: "números" }]   o una cadena.
//   t/desde/paso: cada palabra entra al tiempo `desde + i·paso` (o pasá `tiempos` con un instante por palabra,
//   p. ej. sacado de v.t(...) para que caiga con la voz). Sin t, todo visible. marcaDesde: cuándo se dibuja el
//   marcador (si no, poco después de que aparece su palabra).
// Devuelve la altura usada.
export function titulo(g, partes, x, y, { tam = 104, ancho = W - 2 * M, interlinea = 1.04, t = null, desde = 0, paso = 0.09, tiempos = null, color = C.tinta, alinear = "izq", marcaDesde = null } = {}) {
  g.save(); limpio(g);
  const lista = (Array.isArray(partes) ? partes : [partes]).flatMap((p) =>
    typeof p === "string" ? p.split(/\s+/).filter(Boolean).map((w) => ({ w, it: false })) : String(p.it).split(/\s+/).map((w) => ({ w, it: true })));
  const fuente = (it) => (it ? `400 ${Math.round(tam * 1.12)}px "${LETRA.serif}"` : `800 ${tam}px "${LETRA.titular}"`);
  const esp = (it) => (it ? "0px" : `${-tam * 0.045}px`);
  for (const p of lista) { g.font = fuente(p.it); g.letterSpacing = esp(p.it); p.a = g.measureText(p.w).width; }
  g.font = fuente(false); g.letterSpacing = "0px"; const hueco = tam * 0.24;
  const lineas = [[]]; let usado = 0;
  for (const p of lista) {
    if (usado && usado + hueco + p.a > ancho) { lineas.push([]); usado = 0; }
    lineas.at(-1).push(p); usado += (usado ? hueco : 0) + p.a;
  }
  const alto = tam * interlinea;
  let i = 0;
  lineas.forEach((l, j) => {
    const total = l.reduce((s, p, k) => s + p.a + (k ? hueco : 0), 0);
    let px = alinear === "centro" ? x + (ancho - total) / 2 : x;
    // las cursivas seguidas comparten un solo subrayado: el ancho de la tirada va en su primera palabra
    l.forEach((p, k) => { p.tirada = p.it && !(k && l[k - 1].it) ? l.slice(k).findIndex((q) => !q.it) : 0; });
    l.forEach((p, k) => { if (p.tirada) { const n = p.tirada < 0 ? l.length - k : p.tirada; p.ancho = l.slice(k, k + n).reduce((s, q, j) => s + q.a + (j ? hueco : 0), 0); } });
    const base = y + j * alto + tam * 0.82;
    for (const p of l) {
      const t0 = tiempos ? tiempos[i] : desde + i * paso, u = t == null ? 1 : entra(t, t0, 0.32);
      i++;
      if (u > 0) {
        g.globalAlpha = u; g.filter = u < 1 ? `blur(${(6 * (1 - u)).toFixed(1)}px)` : "none";
        g.font = fuente(p.it); g.letterSpacing = esp(p.it); g.fillStyle = color; g.textBaseline = "alphabetic"; g.textAlign = "left";
        g.fillText(p.w, px, base + 14 * (1 - u));
        g.filter = "none";
        if (p.ancho) subrayar(g, px - 4, base + tam * 0.02, p.ancho + 8, t == null ? 1 : marcaDesde != null ? tramo(t, marcaDesde, marcaDesde + 0.45) : tramo(t, t0 + 0.2, t0 + 0.65), tam);
      }
      px += p.a + hueco;
    }
  });
  g.restore();
  return lineas.length * alto;
}

// El marcador amarillo bajo la cursiva: un trazo grueso, apenas ondulado, que se dibuja de izquierda a derecha.
export function subrayar(g, x, y, w, u = 1, tam = 100) {
  if (u <= 0) return;
  g.save(); g.globalAlpha = 1; g.globalCompositeOperation = "multiply"; g.strokeStyle = C.amarillo; g.lineWidth = Math.max(8, tam * 0.16); g.lineCap = "round";
  g.beginPath();
  const n = 24, fin = Math.max(1, Math.round(n * salir(u)));
  for (let k = 0; k <= fin; k++) { const s = k / n, xx = x + w * s, yy = y + Math.sin(s * Math.PI * 1.3) * tam * 0.035 - s * tam * 0.02; k ? g.lineTo(xx, yy) : g.moveTo(xx, yy); }
  g.stroke(); g.restore();
}

// Párrafo en Inter con **negritas** dentro. Devuelve la altura.
export function parrafo(g, texto, x, y, { tam = 38, ancho = W - 2 * M, interlinea = 1.42, color = C.texto, fuerte = C.tinta, al = 1 } = {}) {
  g.save(); limpio(g); g.globalAlpha = al;
  const trozos = []; String(texto).split(/(\*\*[^*]+\*\*)/).forEach((s) => {
    const b = s.startsWith("**"); (b ? s.slice(2, -2) : s).split(/(\s+)/).forEach((w) => w && trozos.push({ w, b }));
  });
  const f = (b) => (b ? `700 ${tam}px "${LETRA.titular2}"` : `400 ${tam}px "${LETRA.cuerpo}"`);
  let px = x, py = y + tam;
  for (const p of trozos) {
    g.font = f(p.b); const a = g.measureText(p.w).width;
    if (/^\s+$/.test(p.w)) { if (px > x) px += a; continue; }
    if (px > x && px + a > x + ancho) { px = x; py += tam * interlinea; }
    g.fillStyle = p.b ? fuerte : color; g.textBaseline = "alphabetic"; g.fillText(p.w, px, py); px += a;
  }
  g.restore();
  return py - y + tam * (interlinea - 1);
}

// Tarjeta blanca con sombra suave. u (0→1) la hace subir 40 px y aparecer.
export function tarjeta(g, x, y, w, h, { u = 1, r = 26, color = C.tarjeta } = {}) {
  if (u <= 0) return;
  g.save(); limpio(g); g.globalAlpha = u;
  const dy = 40 * (1 - u);
  g.shadowColor = "rgba(3,0,46,0.10)"; g.shadowBlur = 30; g.shadowOffsetY = 10;
  g.fillStyle = color; redondo(g, x, y + dy, w, h, r); g.fill();
  g.restore();
}

// Ícono amarillo: "num" con un número, "check" o "x". u lo hace crecer con un leve sobrepaso.
export function icono(g, tipo, x, y, { n = 1, tam = 56, u = 1 } = {}) {
  if (u <= 0) return;
  const s = u < 1 ? salir(u) * (1 + 0.12 * Math.sin(u * Math.PI)) : 1;
  g.save(); limpio(g); g.translate(x + tam / 2, y + tam / 2); g.scale(s, s);
  g.fillStyle = C.amarillo; redondo(g, -tam / 2, -tam / 2, tam, tam, tam * 0.24); g.fill();
  g.strokeStyle = C.tinta; g.fillStyle = C.tinta; g.lineWidth = tam * 0.1; g.lineCap = "round"; g.lineJoin = "round";
  if (tipo === "num") { g.font = `700 ${tam * 0.56}px "${LETRA.titular2}"`; g.textAlign = "center"; g.textBaseline = "middle"; g.fillText(String(n), 0, tam * 0.03); }
  else if (tipo === "check") { g.beginPath(); g.moveTo(-tam * 0.22, 0); g.lineTo(-tam * 0.06, tam * 0.16); g.lineTo(tam * 0.24, -tam * 0.16); g.stroke(); }
  else { const k = tam * 0.18; g.beginPath(); g.moveTo(-k, -k); g.lineTo(k, k); g.moveTo(k, -k); g.lineTo(-k, k); g.stroke(); }
  g.restore();
}

// Una fila de lista dentro de su tarjeta: ícono + **título** + texto. Devuelve la altura de la tarjeta.
export function item(g, tipo, n, titular, texto, x, y, { ancho = W - 2 * M, u = 1, tam = 42 } = {}) {
  const pad = 34, ix = x + pad, tx = ix + 56 + 26, tw = ancho - (tx - x) - pad;
  // medir primero (al = 0) para saber la altura
  const h1 = parrafo(g, `**${titular}**`, tx, 0, { tam: tam * 1.08, ancho: tw, al: 0 });
  const h2 = texto ? parrafo(g, texto, tx, 0, { tam: tam * 0.92, ancho: tw, al: 0 }) : 0;
  const h = pad * 2 + h1 + (texto ? 6 + h2 : 0) - tam * 0.3;
  if (u <= 0) return h;
  tarjeta(g, x, y, ancho, h, { u });
  const dy = 40 * (1 - salir(u));
  g.save(); g.globalAlpha = u;
  icono(g, tipo, ix, y + dy + pad - 4, { n, u: tramo(u, 0.3, 1) });
  parrafo(g, `**${titular}**`, tx, y + dy + pad - tam * 0.28, { tam: tam * 1.08, ancho: tw, al: u });
  if (texto) parrafo(g, texto, tx, y + dy + pad - tam * 0.28 + h1 + 6, { tam: tam * 0.92, ancho: tw, al: u });
  g.restore();
  return h;
}

// Cuenta tipo «Renta − todos los gastos = flujo de caja»: filas con monto a la derecha; los negativos en azul cobalto y la
// última (total) resaltada en amarillo. filas: [{ txt, monto, t0 }] con monto como cadena («−$1,350»).
export function cuenta(g, filas, x, y, { ancho = W - 2 * M, alto = 100, t = null, total = true } = {}) {
  const h = filas.length * alto + 24;
  tarjeta(g, x, y, ancho, h, { u: 1 });
  g.save(); limpio(g);
  filas.forEach((f, i) => {
    const u = t == null || f.t0 == null ? 1 : entra(t, f.t0, 0.35);
    if (u <= 0) return;
    const fy = y + 12 + i * alto, ult = total && i === filas.length - 1;
    g.globalAlpha = u;
    if (ult) { g.fillStyle = C.resalta; redondo(g, x + 8, fy, ancho - 16, alto, 16); g.fill(); }
    else if (i) { g.fillStyle = "rgba(3,0,46,0.08)"; g.fillRect(x + 30, fy, ancho - 60, 2); }
    const neg = /^[−-]/.test(f.monto);
    g.textBaseline = "middle";
    g.font = ult ? `700 46px "${LETRA.titular2}"` : `400 42px "${LETRA.cuerpo}"`; g.fillStyle = C.tinta; g.textAlign = "left";
    g.fillText(f.txt, x + 34 + 16 * (1 - u), fy + alto / 2);
    g.font = `700 ${ult ? 48 : 42}px "${LETRA.titular2}"`; g.fillStyle = neg ? C.azul : C.tinta; g.textAlign = "right";
    g.fillText(f.monto, x + ancho - 34, fy + alto / 2);
  });
  g.restore();
  return h;
}

// Placa oscura del cierre: «¿Listo para dar el siguiente paso?» + texto, con @usuario en negrita.
export function placa(g, titular, texto, x, y, { ancho = W - 2 * M, u = 1 } = {}) {
  const pad = 52;
  const h1 = titulo(g, titular, 0, -9999, { tam: 80, ancho: ancho - 2 * pad }), h2 = parrafo(g, texto, 0, -9999, { tam: 42, ancho: ancho - 2 * pad, al: 0 });
  const h = pad * 2 + h1 + 20 + h2;
  if (u <= 0) return h;
  tarjeta(g, x, y, ancho, h, { u, color: C.oscura, r: 30 });
  const dy = 40 * (1 - u);
  g.save(); g.globalAlpha = u;
  titulo(g, titular, x + pad, y + dy + pad, { tam: 80, ancho: ancho - 2 * pad, color: "#fff" });
  parrafo(g, texto, x + pad, y + dy + pad + h1 + 20, { tam: 42, ancho: ancho - 2 * pad, color: "#E6E6F2", fuerte: C.amarillo, al: u });
  g.restore();
  return h;
}

// Subtítulo de la voz (opcional, abajo): la frase que se dice en Inter Bold, palabra por palabra, la palabra clave en
// cursiva con el marcador amarillo. Úsalo sólo en escenas sin texto propio; si la lámina ya dice la frase, no hace falta.
export function subtitulo(g, t, v, { y = 1590, ancho = W - 2 * M, tam = 50 } = {}) {
  const f = v.frases.find((x) => t >= x.inicio - 0.1 && t < x.fin + 0.4);
  if (!f) return;
  const ps = v.palabras.filter((w) => w.frase === f.n);
  const partes = ps.map((w) => (w.clave ? { it: w.texto } : w.texto));
  titulo(g, partes, M, y, { tam, ancho, t, tiempos: ps.map((w) => w.inicio - 0.06), alinear: "centro" });
}
