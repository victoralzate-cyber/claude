# Estilo «Tony Valdes · noche»

Variante nocturna del estilo de Tony Valdes, medida sobre su carrusel «Estrategia de adquisición» (operar vs. rentar,
noviembre 2026). Mismo método y aprobaciones de [SKILL.md](../SKILL.md); cambia solo lo visual.

- **Fondo:** azul noche (#02012A → #07094D) con resplandor azul abajo que respira y cuadrícula tenue que se desliza.
- **Arriba:** rótulo en mono (JetBrains Mono, mayúsculas, interletra abierta) con punto dorado; logo dorado a la derecha.
- **Titular:** blanco (Inter Display ExtraBold), con la palabra clave en Instrument Serif Italic con degradado dorado
  (#B07908 → #F4E478 → #FFF1A8), sin marcador.
- **Párrafo:** Inter gris azulado #AEB3D6 con **negritas** en blanco.
- **Paneles:** azul oscuro translúcido, borde fino lila, cuadrícula interior; dibujos de línea dorada que se trazan
  (`tn.trazo`) y se encienden con brillo.
- **Filas:** «01 · texto · ✓» con número en mono dorado (o azul #7888F4) y check amarillo.
- **Pie:** logo pequeño, «tonyvaldesloans», guiones de avance (el actual en dorado) y «02 / 06» en mono.
- **Cierre:** palabra del CTA enorme en serif dorada, barra de comentario oscura con «Publicar» dorado y la notificación
  blanca del mensaje directo.

Herramientas: [`tony-valdes-noche/estilo.mjs`](tony-valdes-noche/estilo.mjs) (`fondo`, `rotulo`, `logo`, `titulo`,
`parrafo`, `panel`, `fila`, `pie`, `trazo`, `comentario`, `mensaje`, `aviso`). Ejemplo completo:
`proyectos/2026-11-11-heloc-heloan/`.
