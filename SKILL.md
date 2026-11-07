---
name: reels-explicativos
description: "Creá reels explicativos de 30 a 60 segundos con voz, animaciones dibujadas en código, subtítulos y efectos. Incluye el motor, las guías, dos ejemplos completos y un estilo opcional en blanco y negro."
---

# Reels explicativos

Una idea entra —por ejemplo, por qué el cielo es azul— y sale un reel vertical en el que una voz cuenta algo sorprendente mientras la imagen muestra lo que dice, con luz, volumen y movimiento. El dibujo y el render se ejecutan en la computadora con Node, canvas y ffmpeg. La voz usa la cuenta de ElevenLabs del usuario.

Esta edición funciona como una carpeta de proyecto independiente. Todas las rutas de abajo parten de la carpeta que contiene este archivo y `package.json`. Abrí la carpeta completa en Claude Code o Codex; no copies únicamente este archivo. No requiere las carpetas, scripts ni cuentas de ningún otro workspace.

## Antes de empezar

1. Leé [AGENTS.md](AGENTS.md), [METODO.md](METODO.md) entero y las guías [guion](guia/guion.md), [dibujo](guia/dibujar.md) y [sonido](guia/sonido.md).
2. Mirá [las muestras del kit](guia/muestras.jpg), los videos de `ejemplo/`, sus `plan.md` y `notas.md`. Son referencias de nivel y construcción, no plantillas para copiar de tema en tema.
3. Ejecutá `node motor/doctor.mjs`. Si faltan dependencias, instalá con `npm ci`. Se necesitan Node 20 o superior, ffmpeg y ffprobe.
4. La primera vez, preguntá en un solo mensaje el idioma, la audiencia, la voz elegida, el cierre y si quiere efectos o música. Guardá las preferencias del usuario en `preferencias.md`.
5. Para la clave de ElevenLabs, usá `node motor/clave.mjs`: se pega en una página local, nunca en el chat. Elegí una voz accesible en la cuenta del usuario y escribí su ID en `guion.json`, en `voz.id`.

## Flujo y aprobaciones

- Creá cada video con `node motor/nuevo.mjs "<idea>"`. Trabajá en su carpeta dentro de `proyectos/`. El resultado se entrega en `salida/`.
- Primero investigá los datos y sus fuentes, escribí el guion y pensá la imagen de cada frase. Si el usuario entregó un texto literal, respetalo.
- Mostrá el guion completo, las palabras y la duración estimada antes de generar la voz. Registrá el texto aprobado y la autorización en `notas.md`. Una corrección no es un OK. Si ya existe una delegación explícita que autoriza completar el guion, registrala y respetá sus límites.
- Antes de una llamada paga, avisá qué se manda y el costo estimado. Respetá el presupuesto autorizado y las reglas de gasto del usuario. Registrá el consumo y el resultado en `notas.md`.
- Generá la voz con `node motor/voz.mjs <proyecto>`. Elegí la voz en `guion.json` con `"voz": { "id": "ID_DE_TU_VOZ" }`. El modelo y los ajustes pueden configurarse en ese mismo objeto; consultá `--ayuda`. No reutilices una voz privada de los ejemplos.
- Escuchá la toma entera y contrastala con el texto. No cortes palabras, no acortes pausas ni cambies la velocidad para hacer encajar escenas. Si algo falla, corregí sólo dentro de la autorización vigente.
- Mostrá la voz para su validación antes de generar imágenes o videos pagos. El dibujo local del kit no requiere otro proveedor. Las imágenes externas son opcionales y llevan su aprobación y su presupuesto.
- Usá los tiempos reales de `voz/tiempos.json` para planear. Nunca inventes tiempos o pegues frases de distintas tomas sin autorización.
- Una pieza aprobada se conserva. Los cambios posteriores van en otra carpeta de proyecto. Crear un video no autoriza publicarlo ni enviarlo a terceros.

## Lenguaje visual

- Mostrá lo que dice cada frase, a escala grande. Una idea nueva pide una acción nueva, una transformación o una escena nueva. No sostengas el mismo dibujo durante varias ideas.
- El gancho abre desde el cuadro 0 con una cosa reconocible en su momento más espectacular. Nada de pantallas vacías, esquemas quietos o rótulos que sólo anuncian el tema.
- Usá el kit con luz, volumen, texturas, partículas y cámara: `k.mira`, `k.ruta`, `k.proyecta`. El movimiento tiene una causa ligada a la voz.
- Si la voz sigue hablando de la misma cosa, mové la cámara en lugar de cortar. Reservá el corte para un sitio o idea nuevos, en la palabra que los introduce. Terminá la acción antes de cortar.
- Las listas se acumulan en orden y se pueden leer. Los elementos nombrados se ven completos al menos medio segundo. Evitá escenas demasiado breves para entender la acción.
- Los subtítulos del estilo base son los del kit: `"subtitulos": "arriba"`, una palabra clave por frase y espacio libre para leer. No agregues otro sistema encima.
- Para láminas técnicas en grises, tipografía pesada con palabras en contorno y movimiento sin rebote, usá [estilos/blanco-y-negro.md](estilos/blanco-y-negro.md). Su módulo y sus fuentes están incluidos.
- Si una foto o recorte externo mejora la explicación, usá un recurso autorizado y guardá su origen. No hace falta contratar otro motor para producir el estilo base.

## Producción y revisión

Seguí los pasos de [METODO.md](METODO.md): idea, guion, voz, plan, hook, escenas, revisión, sonido y entrega. Las aprobaciones de esta skill se cumplen antes de cada gasto, aunque el método muestre el guion más adelante junto con los hooks.

1. Escribí `plan.md` con una fila por frase: acción, palabra de impacto, cámara y transición.
2. Construí primero la apertura y revisala en movimiento. Usá los ejemplos para entender la estructura de `video/mundo.js` y `video/planos/*.js`.
3. Revisá cada plano con `node motor/ver.mjs <proyecto> frase 5`, `... palabra sodio`, `... corte 2` o un rango `... 24-27 --fps 10`. Abrí la imagen generada.
4. Ejecutá `node motor/revisar.mjs <proyecto>` y mirá sus hojas completas. Arreglá cortes con movimiento a medio hacer, objetos fuera de cuadro, texto tapado, saltos y segundos muertos. Un comando exitoso no sustituye mirar.
5. Si lleva efectos, escribí `sonidos.js` y corré `node motor/sonido.mjs <proyecto>`. Sincronizá cada efecto con la acción y mantené la voz clara. Para música, usá una pista autorizada y un nivel que no tape la narración.
6. Renderizá un video por vez: `nice -n 10 node motor/render.mjs <proyecto> --hilos 4` en macOS/Linux; sin `nice` en Windows. El motor limita también ffmpeg a cuatro hilos. No lances varios renders a la vez.
7. Revisá el video completo con sonido: palabras, sincronía, primer y último cuadro, subtítulos y cortes. No entregues defectos conocidos.
8. El render nativo mezcla a −21 LUFS. Para el master de redes, normalizá una copia final a −14 LUFS integrados y pico verdadero máximo −1,5 dBTP, sin reencodificar la imagen; verificá después los niveles y que siga el audio correcto.
9. Entregá el MP4, la portada y el texto de publicación como archivos individuales. Registrá en `notas.md` las decisiones, costos y verificaciones. No publiques automáticamente.

## Qué incluye esta edición

Motor completo, fuentes, efectos, guías y dos ejemplos con código, voz, tiempos, hojas de revisión y videos en 720 × 1280 a 30 fps. Los videos de ejemplo están recomprimidos para reducir la descarga. Los proyectos nuevos se renderizan con la configuración de calidad del motor. `node_modules` se instala en la computadora del usuario; las claves no se distribuyen.
