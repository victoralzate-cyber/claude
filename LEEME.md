# Reels explicativos

## Uso rápido

1. Conservá esta carpeta completa y abrila como proyecto local en Claude Code o Codex.
2. Escribí: **«Leé SKILL.md y configurame este kit»**.
3. El asistente comprueba Node 20+, ffmpeg y ffprobe, e instala las dependencias con `npm ci`.
4. Configurá tu propia clave de ElevenLabs en la página local que abre el asistente. No pegues claves en el chat. Elegí una voz disponible en tu cuenta.
5. Pedí una idea o un video. Primero revisás el guion y después la voz. El MP4 final, la portada y el caption quedan en `salida/`.

No es un archivo para cargar en un chat web: el asistente necesita acceso a esta carpeta y a una terminal local.

## Contenido

- `SKILL.md` y `AGENTS.md`: instrucciones del asistente.
- `METODO.md` y `guia/`: proceso, escritura, animación y sonido.
- `motor/`, `letra/`, `sonidos/`: herramientas y recursos.
- `ejemplo/`: dos proyectos completos y sus videos de referencia, recomprimidos en 720 × 1280 a 30 fps.
- `estilos/`: variante opcional en blanco y negro.
- `package.json` y `package-lock.json`: instalación reproducible de las dependencias.

El dibujo y el render son locales. La voz se factura en tu cuenta de ElevenLabs; cualquier generación externa adicional se acuerda antes. El paquete no contiene claves, cuentas personales ni dependencias ya instaladas. La instalación y los renders pueden ocupar más espacio que la descarga.

Los avisos de licencia de las fuentes se conservan junto a los archivos tipográficos. Anatomy es una integración opcional externa: no se incluye ni se necesita para el estilo base o el módulo en blanco y negro.
