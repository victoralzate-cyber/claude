# Investy360 — Sitio web

Sitio de presentación y captura de leads para Investy360, construido como un único archivo autocontenido (`index.html`: HTML + CSS + JS embebidos), sin frameworks ni pasos de build, pensado para incrustarse dentro de **GoHighLevel (GHL)** mediante un bloque de código personalizado.

## Cómo usarlo en GHL

1. Abre `index.html`.
2. Copia **todo el contenido del `<body>`** (o el archivo completo, si el bloque de GHL lo permite) dentro de un elemento de "Código personalizado / Custom Code" en el constructor de páginas de GHL.
3. Si GHL separa HTML/CSS/JS en campos distintos, mueve el contenido de `<style>` al campo de CSS y el contenido de `<script>` al campo de JS, dejando el HTML del `<body>` en el campo principal.
4. La fuente Montserrat se carga desde Google Fonts vía `<link>` en el `<head>`; si tu bloque de GHL no permite editar el `<head>`, puedes omitir esas líneas — el sitio cae automáticamente a `system-ui`/sans-serif como respaldo.

## Placeholders pendientes de reemplazar

Busca estos textos en `index.html` y reemplázalos antes de publicar:

| Placeholder | Dónde aparece | Qué poner |
|---|---|---|
| `CALENDAR_LINK_AQUI` | Header, Hero, sección "Sesión 1:1 con Tony Valdes", Footer | Link de agendar de GHL (calendario) |
| `TERMINOS_URL_AQUI` | Checkbox del formulario, Footer | URL de Términos y Condiciones |
| `PRIVACIDAD_URL_AQUI` | Checkbox del formulario, Footer | URL de Política de Privacidad |
| `TU_LINK_INSTAGRAM_AQUI` / `TU_LINK_FACEBOOK_AQUI` / `TU_LINK_LINKEDIN_AQUI` / `TU_LINK_YOUTUBE_AQUI` | Footer (redes sociales) | Links reales de redes sociales |
| `[PENDIENTE: precio]` | Sección Membresía | Precio real de la membresía, cuando esté definido |
| `// TODO: conectar a GHL` | `<script>`, dentro del submit del formulario (`#leadForm`) | Descomentar el bloque `fetch(...)` y reemplazar la URL por el webhook/endpoint real de GHL |

## Formulario de captura

- Campos: nombre, teléfono, correo.
- El checkbox de aceptación de Términos y Condiciones / Política de Privacidad es obligatorio: el envío queda bloqueado (con mensaje de error visible) si no está marcado.
- La validación ocurre en el cliente (JS). El punto exacto de envío a GHL está marcado con el comentario `// TODO: conectar a GHL` dentro del `<script>` — ahí mismo se arma el objeto `payload` con `nombre`, `telefono`, `email` y `terminosAceptados` listo para enviarse por `fetch` a un webhook de GHL.

## Accesibilidad

- Foco de teclado visible en todos los elementos interactivos (`:focus-visible`).
- Skip link al contenido principal.
- Contraste verificado: el dorado (`#D4AC57` / `#9E732A`) se usa como texto solo sobre fondos oscuros (contraste >9:1) o en botones con fondo dorado y texto negro; sobre fondos claros el cuerpo de texto usa un tono casi negro (`#17160F`) para cumplir AA, reservando el dorado oscuro para títulos grandes/acentos.
- Respeta `prefers-reduced-motion`: desactiva animaciones y scroll suave para quien lo prefiera.

## Qué falta a propósito (fuera de alcance de esta fase)

- Marketplace funcional real (solo vista previa/"Próximamente").
- Precios de membresía y cualquier cifra de rendimiento/retorno.
- Integración de pagos (la sección de Membresía deja el CTA "Únete ahora" listo para conectarse después).
- Fotografía real: se usaron bloques de color, iconografía lineal y un monograma tipográfico en vez de fotos de stock.
