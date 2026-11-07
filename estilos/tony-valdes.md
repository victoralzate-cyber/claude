# Estilo «Tony Valdes»

Es el estilo por defecto de los reels de Tony Valdes Loans (ver `preferencias.md`). Lleva a video el formato de sus
carruseles: «Guía para empezar a invertir en bienes raíces» (10 láminas, noviembre 2026).

En una frase: papel gris con cuadrícula fina, cabecera con avatar y @tonyvaldesloans, una pastilla «→ TEMA», un
titular negrísimo con una palabra en cursiva serif con marcador amarillo, y debajo tarjetas blancas con íconos
amarillos (números, checks, cruces), cuentas con el total en amarillo y un cierre en placa azul oscuro.

## Qué se mantiene de la skill

Todo el método: una escena por idea, aprobación del guion y de la voz, gastos avisados, revisión, sonido, master y
entrega como dice [SKILL.md](../SKILL.md).

## Qué cambia

Reemplaza el lenguaje visual del kit (luz, volumen, partículas, cámara 3D, subtítulos con recuadro). Se mantiene el
fondo: lo que dice la voz se ve, grande, y cada idea nueva trae una lámina o una pieza nueva.

### Paleta (`tv.C`, del brandbook de Tony Valdes Loans)

El formato es el de los carruseles; los colores son los de la marca: el naranja pasa a amarillo y los oscuros a azul.

| Uso | Color |
|---|---|
| Fondo / cuadrícula | `#EFEEEF` / `#DDDEE8` |
| Titulares, placa de cierre, encabezado de tabla | Cetacean Blue `#03002E` |
| Íconos, marcador bajo la cursiva, fila del total, @usuario en la placa | Jasmine `#F4E478` |
| Flechas, «Sigue →», barra de avance | Philippine Gold `#B07908` |
| Montos negativos, tilde de verificado | Cobalt Blue `#083FB0` |
| Acentos suaves | Cornflower Blue `#7888F4` |

Fuera de esto no entra color, salvo ilustraciones (casas, obra) que pueden llevar tonos cálidos.

### Letra

- Titular: Inter Display ExtraBold, interletra apretada. Una o dos palabras clave en **Instrument Serif Italic**,
  un poco más grande, con el marcador amarillo que se dibuja después de que aparece la palabra.
- Cuerpo: Inter Regular, con **negritas** en Inter Display Bold.
- Pastilla: Inter Display Bold en mayúsculas, flecha dorada.

### Estructura de cada escena (lámina)

1. Cabecera fija: avatar + `@tonyvaldesloans` con tilde azul; a la derecha la serie («De ingresos / a patrimonio»).
2. Pastilla `→ TEMA` que entra deslizándose.
3. Titular que se arma palabra por palabra con la voz (`tiempos` sacados de `v.t(...)`).
4. El contenido de la idea: lista de tarjetas (`tv.item` con "num", "check" o "x"), cuenta (`tv.cuenta`), párrafo, o
   una ilustración dibujada con el kit dentro de una tarjeta.
5. Pie fijo: «03/08» y «Sigue →», con una barra de avance dorada.
6. Cierre: `tv.placa` con «¿Listo para dar el siguiente paso?» y el llamado a la acción.

Cada elemento entra cuando la voz lo nombra. Entre láminas: la nueva entra empujando desde la derecha (0,35 s) y la
cuadrícula se desliza despacio todo el tiempo. Nada rebota salvo el ícono amarillo, que crece con un leve sobrepaso.

Subtítulos: `"subtitulos": "no"` en `guion.json`; la lámina ya muestra la idea. En escenas sin texto propio, usá
`tv.subtitulo(g, t, v)`: la frase abajo, palabra por palabra, con la clave en cursiva con marcador amarillo.

## Herramientas

[`tony-valdes/estilo.mjs`](tony-valdes/estilo.mjs):

```js
import { GlobalFonts, loadImage } from "@napi-rs/canvas";
import * as tv from "../../../estilos/tony-valdes/estilo.mjs";
tv.registrar(GlobalFonts);                         // en mundo.js, una vez
tv.fondo(g, { corre: t * 12 });
tv.cabecera(g, { avatar });                       // avatar = await loadImage("estilos/tony-valdes/avatar.png")
tv.etiqueta(g, "Antes de invertir", tv.M, 400, tv.entra(t, t0));
const h = tv.titulo(g, ["Revisa tus", { it: "números" }], tv.M, 490, { t, tiempos });
tv.item(g, "check", 0, "Reservas", "para varios meses de hipoteca", tv.M, y, { u: tv.entra(t, t1) });
tv.cuenta(g, [{ txt: "Renta", monto: "$2,200", t0 }, /* … */ { txt: "Flujo de caja", monto: "$144", t0 }], tv.M, y, { t });
tv.placa(g, "¿Listo para dar el siguiente paso?", "Escríbeme a **@tonyvaldesloans**…", tv.M, y, { u });
tv.pie(g, { izq: "03/08", avance: t / v.duracion });
```

El avatar es `estilos/tony-valdes/avatar.png` (foto de perfil de Instagram). Si falta, la cabecera muestra un círculo azul con «TV».

## Antes de mostrarlo

- ¿Cada lámina tiene una sola palabra (o dos seguidas) en cursiva subrayada?
- ¿Algún color fuera de la paleta?
- ¿Las cifras son reales y tienen fuente, o dicen «ejemplo con números inventados»?
- ¿El cierre lleva el aviso de que es contenido informativo, no asesoría financiera?
