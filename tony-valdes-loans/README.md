# Tony Valdes Loans — Página de Inicio

Página principal de **tonyvaldesloans.com**, construida según el brandbook oficial de la marca. Es un solo archivo (`index.html`, con HTML, CSS y JS incluidos) más la carpeta `assets/`, y está pensada para pegarse en un bloque de **Código personalizado** de GoHighLevel.

## Idiomas: Español, English y Português

La página es trilingüe. El selector **ES · EN · PT** del header cambia todo el contenido al instante, sin recargar: textos, botones, formulario, mensajes de error, textos alternativos de las imágenes y avisos legales.
- **Español** es el idioma por defecto.
- El idioma elegido se recuerda en el navegador del visitante para su próxima visita.
- **Links directos por idioma**, útiles para anuncios y campañas: agrega `?lang=en` o `?lang=pt` a la URL. Ejemplo: `tonyvaldesloans.com/?lang=pt`.
- Los nombres propios de programas (FHA, VA, DSCR, Fix & Flip, etc.) y el sello Equal Housing Opportunity se mantienen igual en los tres idiomas.
- Las traducciones viven en el objeto `I18N` dentro del `<script>`. Cada texto tiene una clave `data-i18n="tNNN"`.

## Identidad aplicada (brandbook)

| Elemento | Valor |
|---|---|
| Cetacean Blue (principal) | `#03002E` |
| Philippine Gold | `#B07908` |
| Jasmine | `#F4E478` (solo sobre fondos oscuros o en degradados) |
| Cobalt Blue (secundario) | `#083FB0` (estados de foco en formularios) |
| Tipografía | Montserrat |
| Slogan | Préstamos Inteligentes. ¡Sí Es Posible! |

## Secciones

1. Barra superior de contacto y header con menú (se reduce al hacer scroll; en celular es un menú lateral)
2. Hero con foto de Tony, slogan, CTA de asesoría, WhatsApp y estadísticas
3. Selector de 3 caminos: Comprar casa / Invertir / Soy Realtor
4. "Cada mes que pagas renta…" y beneficios de comprar
5. Sobre Tony (más de 25 años, ex-VP de banca comercial, licencias)
6. Casos reales (Familia W., Stephannie, Oscar, Duncan Dr, Forest Park, deal rescatado)
7. Programas tradicionales y no tradicionales
8. Las 5 estrategias de inversión
9. Sección para Realtors
10. Proceso de compra en 6 pasos y consejos de crédito
11. Preguntas frecuentes
12. Formulario de captura con consentimiento TCPA
13. Footer legal con NMLS #1593970, Loan Factory NMLS #320841, Equal Housing y NMLS Consumer Access
14. Botón flotante de WhatsApp

## Contacto configurado

- Teléfono principal: (770) 865-6771 (`tel:+17708656771`)
- WhatsApp: (770) 865-3002 (`https://wa.me/17708653002`)
- Email: info@tonyvaldesloans.com
- Instagram: @tonyvaldesloans

## Versión para pegar en GHL (recomendada)

`ghl-pegar-en-ghl.html` está lista para pegarse completa en un elemento **Code** de GHL:
- Las imágenes van incrustadas, así que no hace falta subirlas a la Biblioteca de Medios.
- Todo el CSS está encapsulado bajo `#tvl`, para que los estilos de GHL no alteren la página y la página no altere el resto del sitio.
- No lleva etiquetas `<html>`, `<head>` ni `<body>`. Título y descripción SEO se configuran en los Settings de la página en GHL.

Se genera a partir de `index-con-imagenes.html`. Si se edita la página, hay que regenerarla.

## Versión con imágenes incluidas

`index-con-imagenes.html` es la misma página, con el logo y las fotos incrustados dentro del archivo (base64, unos 400 KB). Se ve completa al abrirla sola, sin la carpeta `assets/`. Es la ideal para revisar o compartir la página. Para GHL se recomienda la versión con imágenes subidas a la Biblioteca de Medios, porque carga más rápido.

## Cómo subirla a GHL

1. **Imágenes:** sube los archivos de `assets/` a la Biblioteca de Medios de GHL. Luego busca en `index.html` cada `assets/…` y reemplázalo por la URL pública que te da GHL:
   - `assets/logo-tony-valdes-loans.png`
   - `assets/tony-senalando-frente.webp` (hero)
   - `assets/tony-apoyado.webp` (Sobre Tony)
   - `assets/tony-sentado.webp` (Contacto)
   - `assets/tony-senalando-lado.webp` y `assets/tony-traje-completo.webp` (reservadas para las páginas de Inversionistas y Realtors)
2. **Código:** pega el contenido del archivo en un elemento de **Custom Code**. Si GHL separa los campos, el contenido de `<style>` va en CSS y el de `<script>` va en JS.

## Links configurados

| Elemento | Destino |
|---|---|
| Botones "Agenda tu asesoría" | https://api.leadconnectorhq.com/widget/bookings/calendario-tony-valdes-loans |
| Términos y Condiciones | `/terminos` (página en GHL con ese slug) |
| Política de Privacidad | `/privacidad` (página en GHL con ese slug) |
| Instagram | https://www.instagram.com/tonyvaldesloans/ |
| Facebook | https://www.facebook.com/tonyvaldesloanss/ |
| YouTube | https://www.youtube.com/@TonyValdesLoans |

## Páginas legales (`legal/`)

Términos y Privacidad en ES/EN/PT, con el mismo diseño de la marca. El idioma se comparte con la página principal (se guarda como `tvl-lang`). Incluyen el lenguaje que pide el registro A2P 10DLC para SMS: frecuencia de mensajes, STOP/HELP, tarifas, y que los datos de móvil no se comparten con terceros para marketing.
- `legal/ghl-terminos.html` y `legal/ghl-privacidad.html`: para pegar en GHL en páginas con los slugs `terminos` y `privacidad`.
- `legal/terminos.html` y `legal/privacidad.html`: para revisarlas en el navegador.
- El contenido se edita en `legal/legal_content.py`. Para regenerar: `python3 legal/build_legal.py`.
- Antes de publicar, deben revisarlas compliance de Loan Factory o un abogado.


El formulario está conectado al workflow **"Lead Web – Tony Valdes Loans"** (disparador Inbound Webhook, constante `GHL_WEBHOOK` en el `<script>`). Envía en formato form-urlencoded: `nombre`, `first_name`, `last_name`, `telefono` (E.164), `email`, `objetivo` (siempre en español), `idioma` (es/en/pt), `consentimiento_tcpa`, `consentimiento_fecha`, `origen` y `pagina`.

## Notas de compliance

- No se usan promesas de tasas ("garantizo los rates más bajos"), y los casos no mencionan tasas ni pagos mensuales de préstamos de vivienda. Esos datos son "triggering terms" de la Reg. Z y obligarían a publicar el APR y los términos completos.
- Los casos aparecen con nombre de pila o inicial. **Hay que confirmar que cada cliente o agente autorizó su testimonio** antes de publicar.
- Antes de salir en vivo, revisa el texto legal del footer con el departamento de compliance de Loan Factory.
