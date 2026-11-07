// Estilo «blanco y negro» para reels-explicativos: paleta, fondos, pie técnico, subtítulos y rótulos.
// Medido sobre @dannystuart (De9ji2QhO6J, la skill Anatomy) y @peter.visuals (DdttI7oyswS), 2026-10-30. El canon
// está en blanco-y-negro.md, al lado. Sin imports: el run le pasa GlobalFonts de @napi-rs/canvas y la voz de "#voz".
//
//   import { GlobalFonts } from "@napi-rs/canvas";
//   import { v } from "#voz";
//   import * as bn from "../../../estilos/blanco-y-negro/estilo.mjs";
//   bn.registrar(GlobalFonts);                       // una vez, en mundo.js (el render dibuja en hilos aparte)
//   ...al final del dibuja(g, t) de cada plano:
//   bn.subtitulos(g, t, v, "papel", { contorno: { 1: "literalmente cualquier cosa" } });
//
// Con este estilo el guion lleva "subtitulos": "no": los subtítulos los dibuja cada plano con la tinta de su fondo.
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const AQUI = dirname(fileURLToPath(import.meta.url));

// Colores medidos en los cuadros de las referencias. Fuera de esto no entra color, salvo que el color sea el tema.
export const TEMAS = {
  papel: { fondo: "#F5F3EF", tinta: "#161616", suave: "#8C8A86", grilla: "22,22,22", relleno: "#FFFFFF" },
  grafito: { fondo: "#444444", tinta: "#F2F1ED", suave: "#A6A5A2", grilla: "242,241,237", relleno: "#3A3A3A" },
  negro: { fondo: "#0A0A0A", tinta: "#FFFFFF", suave: "#7C7C7C", grilla: "255,255,255", relleno: "#161616" },
};
const tema = (n) => TEMAS[n] || (() => { throw new Error(`Tema «${n}»: usá papel, grafito o negro.`); })();

export const LETRA = { titulo: "BN Titulo", rotulo: "BN Rotulo", mono: "BN Mono" };

export function registrar(GlobalFonts) {
  GlobalFonts.registerFromPath(join(AQUI, "letra", "InterDisplay-ExtraBold.ttf"), LETRA.titulo);
  GlobalFonts.registerFromPath(join(AQUI, "letra", "InterDisplay-Bold.ttf"), LETRA.rotulo);
  GlobalFonts.registerFromPath(join(AQUI, "letra", "JetBrainsMono-Regular.ttf"), LETRA.mono);
}

const tramo = (t, a, b) => Math.max(0, Math.min(1, (t - a) / (b - a)));
const salir = (u) => 1 - Math.pow(1 - u, 3);
const sinTilde = (s) => String(s).toLowerCase().normalize("NFKD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]/g, "");

// El fondo plano del tema y, si se pide, su textura:
//   "piso"   la grilla isométrica punteada de Anatomy, sólo en la mitad de abajo y apagándose hacia arriba;
//   "puntos" la matriz de puntos de @peter.visuals, más marcada en el centro.
export function fondo(g, nombre, { textura = null, piso = 1100 } = {}) {
  const T = tema(nombre);
  g.save();
  g.setTransform(1, 0, 0, 1, 0, 0);
  g.globalAlpha = 1; g.filter = "none"; g.globalCompositeOperation = "source-over";
  g.fillStyle = T.fondo; g.fillRect(0, 0, 1080, 1920);
  if (textura === "piso") {
    const paso = 96, dx = Math.cos(Math.PI / 6), dy = Math.sin(Math.PI / 6);
    g.lineWidth = 1.6;
    for (const s of [1, -1]) {
      for (let c = -2000; c < 3000; c += paso) {
        // recta y = piso + s·(x − c)·tan30, en tramos de 18 px con 10 de hueco
        for (let x = 0; x < 1080; x += 28) {
          const y0 = piso + s * (x - c) * (dy / dx), y1 = piso + s * (x + 18 - c) * (dy / dx);
          if (y0 < piso - 40 || y0 > 1920) continue;
          const a = 0.16 * tramo(y0, piso - 40, piso + 360);
          if (a <= 0.004) continue;
          g.strokeStyle = `rgba(${T.grilla},${a})`;
          g.beginPath(); g.moveTo(x, y0); g.lineTo(x + 18, y1); g.stroke();
        }
      }
    }
  } else if (textura === "puntos") {
    for (let y = 24; y < 1920; y += 48) for (let x = 24; x < 1080; x += 48) {
      const d = Math.hypot((x - 540) / 540, (y - 900) / 1100), a = 0.22 * Math.max(0, 1 - d);
      if (a <= 0.01) continue;
      g.fillStyle = `rgba(${T.grilla},${a})`;
      g.beginPath(); g.arc(x, y, 2.2, 0, Math.PI * 2); g.fill();
    }
  }
  g.restore();
}

// El pie de lámina técnica: una regla fina y, debajo, «FIG. 01 · TOCADISCOS» a la izquierda y un dato a la derecha.
export function pie(g, nombre, izq, der = "", { y = 1500, al = 1 } = {}) {
  const T = tema(nombre);
  g.save();
  g.setTransform(1, 0, 0, 1, 0, 0);
  g.globalAlpha = al;
  g.strokeStyle = T.suave; g.lineWidth = 1.5;
  g.beginPath(); g.moveTo(96, y); g.lineTo(984, y); g.stroke();
  g.font = `400 27px "${LETRA.mono}"`;
  g.letterSpacing = "3px";
  g.textBaseline = "top";
  g.fillStyle = T.suave;
  g.textAlign = "left"; g.fillText(String(izq).toUpperCase(), 96, y + 22);
  g.textAlign = "right"; g.fillText(String(der).toUpperCase(), 984, y + 22);
  g.restore();
}

// Subtítulos del estilo: la frase se arma arriba, centrada, palabra por palabra (desenfoque que se aclara y sube 10
// px); las dichas quedan en tinta, no en gris; lo clave va en contorno (trazo de tinta sobre el color del fondo).
// Una frase larga sigue en un bloque nuevo cuando no entra en `lineas` renglones.
//   contorno: { <n de frase>: "palabras seguidas de esa frase" }; sin entrada, la «clave» de guion.json.
export const SUBS = { tam: 82, linea: 88, ancho: 860, arriba: 232, lineas: 4, anticipo: 0.08, entra: 0.14 };

const bloquesCache = new WeakMap();
function bloquesDe(g, v, contorno) {
  if (bloquesCache.has(v.palabras)) return bloquesCache.get(v.palabras);
  const S = SUBS, bs = [];
  g.save();
  g.font = `800 ${S.tam}px "${LETRA.titulo}"`;
  g.letterSpacing = "-2px";
  const hueco = g.measureText(" ").width;
  for (const f of v.frases) {
    const ps = v.palabras.filter((w) => w.frase === f.n);
    const marca = new Set();
    const pedido = contorno?.[f.n];
    if (pedido) {
      const ks = String(pedido).split(/\s+/).map(sinTilde).filter(Boolean);
      for (let i = 0; i + ks.length <= ps.length; i++) if (ks.every((k, j) => sinTilde(ps[i + j].texto) === k)) { ks.forEach((_, j) => marca.add(i + j)); break; }
      if (!marca.size) throw new Error(`Contorno «${pedido}» no está en la frase ${f.n}: «${f.texto}».`);
    } else ps.forEach((w, i) => w.clave && marca.add(i));
    // renglones de la frase entera; si son más de `lineas`, se reparten parejo en bloques (5 → 3 + 2, nunca 4 + 1)
    const lin = [[]];
    let usado = 0;
    ps.forEach((w, i) => {
      const ancho = g.measureText(w.texto).width;
      if (usado && usado + hueco + ancho > S.ancho) { lin.push([]); usado = 0; }
      lin[lin.length - 1].push({ ...w, ancho, contorno: marca.has(i) });
      usado += (usado ? hueco : 0) + ancho;
    });
    const nb = Math.ceil(lin.length / S.lineas);
    for (let k = 0, desde = 0; k < nb; k++) {
      const cuantas = Math.ceil((lin.length - desde) / (nb - k)), ls = lin.slice(desde, desde + cuantas);
      bs.push({ frase: f.n, lineas: ls, palabras: ls.flat() });
      desde += cuantas;
    }
  }
  bs.forEach((b, i) => {
    b.lineas.forEach((l, j) => {
      const total = l.reduce((s, p, k) => s + p.ancho + (k ? hueco : 0), 0);
      let x = 540 - total / 2;
      for (const p of l) { p.x = x; p.y = S.arriba + j * S.linea; x += p.ancho + hueco; }
    });
    // del anticipo de su primera palabra hasta el de la primera del bloque siguiente (o 0,9 s después de la última)
    b.inicio = b.palabras[0].inicio - S.anticipo;
    const sig = bs[i + 1], ult = b.palabras[b.palabras.length - 1];
    b.fin = sig ? Math.min(sig.palabras[0].inicio - S.anticipo, ult.fin + 0.9) : v.duracion;
  });
  g.restore();
  bloquesCache.set(v.palabras, bs);
  return bs;
}

export function subtitulos(g, t, v, nombre, { contorno = null, al = 1 } = {}) {
  const T = tema(nombre), S = SUBS;
  const b = bloquesDe(g, v, contorno).find((x) => t >= x.inicio && t < x.fin);
  if (!b) return;
  g.save();
  g.setTransform(1, 0, 0, 1, 0, 0);
  g.globalCompositeOperation = "source-over";
  g.font = `800 ${S.tam}px "${LETRA.titulo}"`;
  g.letterSpacing = "-2px";
  g.textBaseline = "middle"; g.textAlign = "left";
  g.lineJoin = "round";
  for (const p of b.palabras) {
    const u = salir(tramo(t, p.inicio - S.anticipo, p.inicio - S.anticipo + S.entra));
    if (u <= 0) continue;
    g.globalAlpha = al * u;
    g.filter = u < 1 ? `blur(${(9 * (1 - u)).toFixed(2)}px)` : "none";
    const y = p.y + S.linea / 2 + 10 * (1 - u);
    if (p.contorno) {
      g.fillStyle = T.fondo; g.fillText(p.texto, p.x, y);
      g.strokeStyle = T.tinta; g.lineWidth = 3; g.strokeText(p.texto, p.x, y);
    } else {
      g.fillStyle = T.tinta; g.fillText(p.texto, p.x, y);
    }
  }
  g.restore();
}

// Rótulo que se revela con un bloque de tinta (los nodos de @peter.visuals): el bloque llega a cubrir la palabra y se
// encoge hacia la derecha dejando las letras, con un cursor fino al final mientras se escribe.
//   u: avance 0→1 (dale unos 0,25 s); x, y: centro del rótulo.
export function revelar(g, nombre, texto, x, y, u, { tam = 64, peso = 700 } = {}) {
  if (u <= 0) return;
  const T = tema(nombre);
  g.save();
  g.setTransform(1, 0, 0, 1, 0, 0);
  g.font = `${peso} ${tam}px "${peso >= 800 ? LETRA.titulo : LETRA.rotulo}"`;
  g.letterSpacing = "-1px";
  g.textBaseline = "middle"; g.textAlign = "left";
  const w = g.measureText(texto).width, x0 = x - w / 2, alto = tam * 1.05;
  const cubre = tramo(u, 0, 0.3), destapa = salir(tramo(u, 0.3, 1));
  const letras = Math.round(texto.length * destapa);
  g.fillStyle = T.tinta;
  g.fillText(texto.slice(0, letras), x0, y);
  const izq = x0 + w * destapa, der = x0 + w * cubre;
  if (der > izq) g.fillRect(izq, y - alto / 2, der - izq, alto);
  if (destapa > 0 && u < 1) g.fillRect(x0 + w + 6, y - alto / 2, 4, alto); // el cursor, mientras escribe
  g.restore();
}

// Isométrica de lámina técnica, como Anatomy: x e y en el piso, z hacia arriba, ejes a 30°. `vista` corre y escala el
// dibujo entero (la cámara de este estilo: ortográfica, se acerca o se corre, nunca rota en perspectiva).
export function iso(x, y, z, vista = {}) {
  const { cx = 540, cy = 1050, esc = 1 } = vista, c = Math.cos(Math.PI / 6), s = Math.sin(Math.PI / 6);
  return [cx + (x - y) * c * esc, cy + ((x + y) * s - z) * esc];
}

// Tonos de las caras por tema: arriba la más clara, la izquierda media, la derecha la más oscura (luz de arriba a la
// izquierda, como en Anatomy). `lit` es la única pieza que el espectador tiene que mirar: va en tinta plena, con sus
// tres caras todavía distintas y el contorno del color del fondo para que no se aplane.
export const CARAS = {
  papel: { arriba: "#FFFFFF", izq: "#E9E7E2", der: "#D2D0CB", lit: ["#3C3C3C", "#262626", "#161616"] },
  grafito: { arriba: "#5A5A5A", izq: "#4C4C4C", der: "#3A3A3A", lit: ["#FFFFFF", "#E6E5E1", "#CCCBC7"] },
  negro: { arriba: "#2A2A2A", izq: "#1E1E1E", der: "#141414", lit: ["#FFFFFF", "#E6E6E6", "#CCCCCC"] },
};

// Un prisma (caja) con sus tres caras visibles y el contorno en tinta. {x, y, z} es la esquina de abajo más lejana.
export function prisma(g, nombre, { x = 0, y = 0, z = 0, w, d, h }, vista = {}, { lit = false, trazo = 2.2 } = {}) {
  const T = tema(nombre), C = CARAS[nombre], P = (a, b, c) => iso(a, b, c, vista);
  const [arriba, izq, der] = lit ? C.lit : [C.arriba, C.izq, C.der];
  const cara = (pts, fill) => {
    g.beginPath(); pts.forEach(([px, py], i) => (i ? g.lineTo(px, py) : g.moveTo(px, py))); g.closePath();
    g.fillStyle = fill; g.fill(); g.stroke();
  };
  g.save();
  g.strokeStyle = lit ? T.fondo : T.tinta; g.lineWidth = trazo; g.lineJoin = "round";
  cara([P(x, y + d, z), P(x + w, y + d, z), P(x + w, y + d, z + h), P(x, y + d, z + h)], izq);
  cara([P(x + w, y, z), P(x + w, y + d, z), P(x + w, y + d, z + h), P(x + w, y, z + h)], der);
  cara([P(x, y, z + h), P(x + w, y, z + h), P(x + w, y + d, z + h), P(x, y + d, z + h)], arriba);
  g.restore();
}
