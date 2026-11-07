# Estilo «Tony Valdes»

Es el estilo por defecto de los reels de Tony Valdes Loans (ver `preferencias.md`). Lleva a video el formato de sus
carruseles: «Guía para empezar a invertir en bienes raíces» (10 láminas, noviembre 2026).

En una frase: papel gris con cuadrícula fina, cabecera con avatar y @tonyvaldesloans, una pastilla «→ TEMA», un
titular negrísimo con una palabra en cursiva serif subrayada a mano en terracota, y debajo tarjetas blancas con íconos
naranjas (números, checks, cruces), cuentas con el total en amarillo y un cierre en placa café oscura.

## Qué se mantiene de la skill

Todo el método: una escena por idea, aprobación del guion y de la voz, gastos avisados, revisión, sonido, master y
entrega como dice [SKILL.md](../SKILL.md).

## Qué cambia

Reemplaza el lenguaje visual del kit (luz, volumen, partículas, cámara 3D, subtítulos con recuadro). Se mantiene el
fondo: lo que dice la voz se ve, grande, y cada idea nueva trae una lámina o una pieza nueva.

### Paleta (`tv.C`)

| Uso | Color |
|---|---|
| Fondo / cuadrícula | `#EFEEEF` / `#E2DCDC` |
| Tinta de titulares / cuerpo | `#1E1715` / `#3A3230` |
| Íconos y flechas | naranja `#E8763A` |
| Subrayado de la cursiva, «Sigue →» | terracota `#C96F56` |
| Montos negativos | `#A24E36` |
| Placa de cierre y encabezado de tabla | café `#2F211C` |
| Fila del total | amarillo `#FFF3B8` |

Fuera de esto no entra color, salvo ilustraciones (casas, monedas) en tonos cálidos.

### Letra

- Titular: Inter Display ExtraBold, interletra apretada. Una o dos palabras clave en **Instrument Serif Italic**,
  un poco más grande, con el subrayado terracota que se dibuja después de que aparece la palabra.
- Cuerpo: Inter Regular, con **negritas** en Inter Display Bold.
- Pastilla: Inter Display Bold en mayúsculas, flecha naranja.

### Estructura de cada escena (lámina)

1. Cabecera fija: avatar + `@tonyvaldesloans` con tilde azul; a la derecha la serie («De ingresos / a patrimonio»).
2. Pastilla `→ TEMA` que entra deslizándose.
3. Titular que se arma palabra por palabra con la voz (`tiempos` sacados de `v.t(...)`).
4. El contenido de la idea: lista de tarjetas (`tv.item` con "num", "check" o "x"), cuenta (`tv.cuenta`), párrafo, o
   una ilustración dibujada con el kit dentro de una tarjeta.
5. Pie fijo: «03/08» y «Sigue →», con una barra de avance terracota.
6. Cierre: `tv.placa` con «¿Listo para dar el siguiente paso?» y el llamado a la acción.

Cada elemento entra cuando la voz lo nombra. Entre láminas: la nueva entra empujando desde la derecha (0,35 s) y la
cuadrícula se desliza despacio todo el tiempo. Nada rebota salvo el ícono naranja, que crece con un leve sobrepaso.

Subtítulos: `"subtitulos": "no"` en `guion.json`; la lámina ya muestra la idea. En escenas sin texto propio, usá
`tv.subtitulo(g, t, v)`: la frase abajo, palabra por palabra, con la clave en cursiva terracota.

## Herramientas

[`tony-valdes/estilo.mjs`](tony-valdes/estilo.mjs):

```js
import { GlobalFonts, loadImage } from "@napi-rs/canvas";
import * as tv from "../../../estilos/tony-valdes/estilo.mjs";
tv.registrar(GlobalFonts);                         // en mundo.js, una vez
tv.fondo(g, { corre: t * 12 });
tv.cabecera(g, { avatar });                       // avatar = await loadImage("estilos/tony-valdes/avatar.jpg")
tv.etiqueta(g, "Antes de invertir", tv.M, 400, tv.entra(t, t0));
const h = tv.titulo(g, ["Revisa tus", { it: "números" }], tv.M, 490, { t, tiempos });
tv.item(g, "check", 0, "Reservas", "para varios meses de hipoteca", tv.M, y, { u: tv.entra(t, t1) });
tv.cuenta(g, [{ txt: "Renta", monto: "$2,200", t0 }, /* … */ { txt: "Flujo de caja", monto: "$144", t0 }], tv.M, y, { t });
tv.placa(g, "¿Listo para dar el siguiente paso?", "Escríbeme a **@tonyvaldesloans**…", tv.M, y, { u });
tv.pie(g, { izq: "03/08", avance: t / v.duracion });
```

Si falta `estilos/tony-valdes/avatar.jpg`, la cabecera muestra un círculo café con «TV».

## Antes de mostrarlo

- ¿Cada lámina tiene una sola palabra (o dos seguidas) en cursiva subrayada?
- ¿Algún color fuera de la paleta?
- ¿Las cifras son reales y tienen fuente, o dicen «ejemplo con números inventados»?
- ¿El cierre lleva el aviso de que es contenido informativo, no asesoría financiera?
