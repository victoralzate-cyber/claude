# Estilo «blanco y negro»

Usalo cuando el usuario pida láminas técnicas en grises, tipografía en contorno y movimiento sin rebote.

En una frase: láminas técnicas en grises sobre papel y grafito que se alternan en cada corte, la frase arriba en una grotesca negrísima que se arma palabra por palabra con lo clave en contorno, y todo frenando sin rebote.

## Qué se mantiene de la skill

El método del kit, una escena por idea, la aprobación del guion y de la voz, el idioma y el cierre elegidos por el usuario, la música autorizada si corresponde, el master a −14 LUFS, la portada y la entrega siguen como dice [SKILL.md](../SKILL.md).

## Qué cambia con este estilo

Estas reglas reemplazan, sólo en este estilo, a las de la skill sobre el lenguaje visual del kit (luz, volumen, partículas, cámara 3D en perspectiva), el gancho «hecho de luz», el rebote de lo que entra y los subtítulos del kit con el recuadro azul. Lo que la skill pide de fondo sigue valiendo con otros materiales: un gancho simple con una sola cosa grande que cambia en cada parte de la frase, una lista que se apila en orden, lo que se muestra va grande.

### Paleta

| Tema | Fondo | Tinta | Para qué |
|---|---|---|---|
| `papel` | `#F5F3EF` (blanco cálido, nunca blanco puro) | `#161616` | la escena base |
| `grafito` | `#444444` (nunca negro) | `#F2F1ED` | la escena que sigue: los temas se alternan en casi cada corte |
| `negro` | `#0A0A0A` | `#FFFFFF` | sólo la placa que cita una frase de ejemplo, como mucho dos por reel |

Cero color. Las caras de los sólidos van en grises (`CARAS` de `estilo.mjs`: arriba la más clara, la derecha la más oscura) y una sola pieza por escena, la que hay que mirar, va en tinta plena (`lit`). El color entra sólo si es el tema (los tres canales de una pantalla, un semáforo) y entonces es una pieza, no el fondo. En el reel de Danny los nueve cortes alternan papel y grafito; en el de Peter el negro corta dos veces el blanco para citar «but there's one more thing» y «but this is where most people mess up».

### Letra y subtítulos

- **Subtítulos:** la frase se arma arriba, centrada, en Inter Display ExtraBold con la interletra apretada, palabra por palabra al decirse (entra desenfocada, se aclara y sube 10 px en 0,14 s). Lo ya dicho queda en tinta plena, no en gris. **Lo clave de la frase va en contorno** (trazo de tinta, sin relleno): «literalmente cualquier cosa.», «pieza por pieza.», «una hora.». Hasta 4 renglones; si no entra, se parte en bloques parejos. Es la misma mecánica de los subtítulos del kit con la tinta del estilo: el recuadro azul sería el único color de la pantalla.
- **Cómo:** en `guion.json`, `"subtitulos": "no"` y en cada frase un `"contorno"` con las palabras seguidas que van huecas (sin él, va la `clave`). Van en el guion que se muestra para el OK: si se cambian después de la aprobación, revisá de nuevo el guion con el usuario. Cada plano llama a `bn.subtitulos(g, t, v, "<tema>", { contorno })` al final de su `dibuja`, con el tema de su fondo, y el mundo arma el mapa una vez: `Object.fromEntries(guion.frases.map((f, i) => [i + 1, f.contorno]).filter(([, c]) => c))`.
- **Frases cortas:** como en las referencias, de 10 palabras como mucho; la de 13 de la prueba ya pidió dos bloques.
- **Rótulos técnicos:** JetBrains Mono en mayúsculas con interletra abierta y en el gris del tema: el pie de lámina (`bn.pie`: «FIG. 01 · TOCADISCOS» y a la derecha un dato real, «84 PIEZAS», «4 MM DE RECORRIDO»), contadores, listas de piezas, callouts.
- **Rótulo que se revela:** el nombre de un nodo o de una pieza llega tapado por un bloque de tinta que se encoge hacia la derecha y deja las letras, con un cursor fino mientras escribe (`bn.revelar`, unos 0,25 s, con `clic`).
- **Palabras sueltas (placa negra):** en la placa que cita una frase, las palabras aparecen de a una en distintos lugares y las de impacto más grandes y más negras («una cosa más», «la mayoría»), como en Peter.

### Escenas

Una escena por idea, como en la skill, armada con este vocabulario (todo en isométrica de lámina, cámara ortográfica):

- **Lámina técnica:** el objeto del que se habla, en isométrica, sobre el piso de grilla punteada (`bn.fondo(g, tema, { textura: "piso" })`), con callouts numerados y el pie. Si el objeto es el protagonista y vale el detalle, es una figura de Anatomy es una integración opcional y no se incluye en este paquete. Usala sólo si está instalada, el usuario la eligió y una figura detallada mejora la explicación. El estilo funciona también con los prismas y cilindros del módulo incluido.

Para capturar una página local creada con esa integración, está incluido [capturar_anatomy.py](blanco-y-negro/capturar_anatomy.py). Necesita Python 3, Playwright para Python y Chromium, que sólo se instalan si se usa esta opción. El script captura cuadros con fondo transparente; consultá su ayuda y verificá primero la figura. No reemplaza la aprobación de voz ni autoriza generaciones pagas.


## Herramientas

[`blanco-y-negro/estilo.mjs`](blanco-y-negro/estilo.mjs) no importa nada: el mundo le pasa `GlobalFonts` y la voz.

```js
import { GlobalFonts } from "@napi-rs/canvas";
import { v } from "#voz";
import * as bn from "../../../estilos/blanco-y-negro/estilo.mjs"; // desde proyectos/<nombre>/video/mundo.js
bn.registrar(GlobalFonts); // en mundo.js, una vez (el render dibuja en hilos aparte)
// en cada plano:
bn.fondo(g, "papel", { textura: "piso" });        // "piso" | "puntos" | null
bn.prisma(g, "papel", { x, y, z, w, d, h }, vista, { lit });
bn.pie(g, "papel", "Fig. 01 · Tocadiscos", "84 piezas");
bn.revelar(g, "papel", "Gancho", 540, 1000, u);
bn.subtitulos(g, t, v, "papel", { contorno });   // al final del dibuja
```

`bn.TEMAS`, `bn.CARAS` y `bn.SUBS` tienen los valores medidos; `bn.iso(x, y, z, vista)` proyecta a la pantalla. La letra está en `blanco-y-negro/letra/` (Inter Display, JetBrains Mono, ambas OFL).

## Antes de mostrarlo

Además de la revisión de la skill, mirá la hoja de cuadros de tu proyecto y respondé:

- ¿Hay un solo color fuera de papel, grafito, negro y grises? Sacalo.
- ¿Dos escenas seguidas con el mismo fondo, sin una razón? Alternalas.
- ¿Algo rebota, brilla o tiene partículas? Eso es del otro lenguaje del kit.
- ¿La frase de arriba tiene su parte en contorno y se lee en el teléfono?
- ¿Hay un segundo entero en que no cambia nada?
