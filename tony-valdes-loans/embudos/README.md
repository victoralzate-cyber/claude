# Embudos de Tony Valdes Loans (tonyvaldesloansinfo.com)

Los embudos usan la misma línea gráfica que la web principal (Cetacean Blue, Philippine Gold, Jasmine, Montserrat y la casita del logo). Cada embudo tiene su **propio estilo**, varias páginas para enganchar al lead y está en **ES / EN / PT**.

Tres reglas que cumplen todos:
1. **Sin menú.** El header solo lleva el logo, el selector de idioma y el teléfono, para que el lead no se salga del embudo.
2. **Un solo público, una sola promesa y una sola acción por página.**
3. **Cumplimiento legal en todas las páginas:** NMLS de Tony (#1593970) y de Loan Factory (#320841), sello Equal Housing, consentimiento TCPA en los formularios y nota de "resultados pueden variar". Sin tasas, sin pagos mensuales y sin promesas de rentabilidad.

## Plan general

| # | Embudo | Reemplaza a | Gancho | Estilo | Páginas |
|---|---|---|---|---|---|
| 1 | **Primeros Compradores** ✅ | /primeros-compradores | Test "¿Qué tan cerca estás de tu primera casa?" | "Puerta" (crema, arcos, llaves) | Test → Resultado → Guía → Cita confirmada |
| 1b | **Webinar Primeros Compradores** ✅ | — (nuevo) | Masterclass gratis en vivo "Tu primera casa en USA" | "Escenario" (variante en vivo del estilo Puerta) | Registro → Lugar reservado → Sala (en vivo / repetición) → conecta con el test |
| 2 | **Masterclass Inversionistas** (en vivo y luego grabada) | /inversion-inmobiliaria, /como-invertir-en-usa, /Investors-Webinar | Masterclass "Invierte en USA" | "Escenario" (oscuro, reflector, cuenta regresiva) | Registro → Confirmación → Sala / Repetición → Aplicación → Gracias |
| 3 | **Inversionistas Extranjeros** | /inversion-inmobiliaria-para-extranjeros | Guía "Cómo invertir en USA sin vivir aquí" | "Global" (mapa, pasaporte, rutas) | Guía → Precalificación → Cita |
| 4 | **Agentes Aliados** | /agentes-inmobiliarios, /real-estate-agents | Entrenamiento "Cómo duplicar tus cierres" | "Alianza" (claro, banda dorada) | Registro → Entrenamiento → Aplicación → Bienvenida |
| 5 | *(opcional)* **Refinanciamiento / Equity** | — | "¿Cuánto equity tienes?" | Ejecutivo claro | Calculadora → Resultado → Cita |

## Embudo 1 · Primeros Compradores (`primeros-compradores/`)

**Recorrido del lead:**
1. **Test** (`/primeros-compradores`): hero con foto real de clientes, test de 8 preguntas (una a la vez, con barra de llaves), calculadora de renta y formulario con TCPA para ver el resultado. Debajo: qué va a descubrir, fotos de clientes reales, mensaje de Tony y un CTA final.
2. **Resultado** (`/primeros-compradores-resultado`): saludo con su nombre, puntaje de 0 a 10 con medidor animado, nivel (Listo / Casi listo / Empezando), plan por áreas (ingresos, crédito, ahorro y documentos) con consejos según sus respuestas, "el costo de esperar" con su renta real, mensaje de Tony, **calendario incrustado** y botón a la guía.
3. **Guía** (`/primeros-compradores-guia`): guía estilo revista en 6 capítulos. Incluye una lista de documentos interactiva (empleado o independiente, se guarda en el dispositivo), programas, el camino en 6 pasos, mitos que se voltean al tocarlos e historias reales. Se puede guardar en PDF. **Sirve también como enlace para los emails de seguimiento.**
4. **Cita confirmada** (`/primeros-compradores-cita`): confirmación con qué tener a la mano, qué pasa en la llamada, invitar al co-comprador por WhatsApp, guardar el número y leer la guía.

**Archivos:**
- `ghl/1-test.html`, `ghl/2-resultado.html`, `ghl/3-guia.html`, `ghl/4-cita.html`: para pegar en GHL.
- `revisar/…`: las mismas páginas para abrirlas en el navegador, con todas las fotos incluidas. El recorrido completo funciona: el test redirige al resultado.
- `src/…`: fuente en español. Las traducciones y textos dinámicos están en `i18n.py`.

### Cómo montarlo en GHL

1. En el embudo **Primeros compradores**, deja 4 pasos con estas rutas (path):

   | Paso | Ruta | Archivo | Título SEO |
   |---|---|---|---|
   | 1 | `primeros-compradores` | `ghl/1-test.html` | ¿Estás listo para tu primera casa? Test gratis \| Tony Valdes Loans |
   | 2 | `primeros-compradores-resultado` | `ghl/2-resultado.html` | Tu resultado y tu plan \| Tony Valdes Loans |
   | 3 | `primeros-compradores-guia` | `ghl/3-guia.html` | Guía del Primer Comprador 2026 \| Tony Valdes Loans |
   | 4 | `primeros-compradores-cita` | `ghl/4-cita.html` | ¡Tu cita está confirmada! \| Tony Valdes Loans |

2. En cada paso: página en blanco, una sección y una fila a todo lo ancho, un elemento **Code** y pega el archivo completo. La página se estira a todo el ancho sola.
3. **Descripción SEO del paso 1:** "Responde 8 preguntas en 60 segundos y recibe tu plan personalizado para comprar tu primera casa en EE. UU. Sin costo y sin afectar tu crédito. Tony Valdes, NMLS #1593970." Imagen social: `seo/og-tony-valdes-loans.jpg`.
4. **Calendario → página 4:** en la configuración del calendario, en *Confirmation page*, pon como redirección `https://tonyvaldesloansinfo.com/primeros-compradores-cita`. El embudo usa su propio calendario clonado, **Calendario Primeros Compradores** (`https://api.leadconnectorhq.com/widget/booking/ThrthngO5Or3QFqeWH0j`), para no afectar el calendario de la web principal.
5. Si cambias las rutas, ajusta `NEXT_URL`, `TEST_URL` y `GUIDE_URL` al inicio del `<script>` de cada página.

### Datos que llegan al workflow (mismo webhook de siempre)

Los de siempre: `nombre`, `first_name`, `last_name`, `telefono`, `email`, `objetivo` ("Comprar mi primera casa"), `idioma`, `consentimiento_tcpa`, `consentimiento_fecha`, `origen` (= `funnel-primeros-compradores`) y `pagina`.

Nuevos:

| Campo | Ejemplo |
|---|---|
| `plazo` | 0-3 meses · 3-6 meses · 6-12 meses · Explorando |
| `tipo_ingreso` | Empleado W-2 · Independiente 1099 / negocio · Ambos · Sin ingresos fijos |
| `tiempo_ingresos` | 2+ años · 1-2 años · Menos de 1 año |
| `credito` | Muy bueno (700+) · Bueno (640-699) · Regular (580-639) · Bajo o no sabe |
| `pagos` | Siempre a tiempo · Algún atraso este año · Cuentas en cobranza |
| `ahorro` | Ahorros para entrada y cierre · Algo, pero poco · Todavía no |
| `documentos` | Todo al día · Declara, pero desordenado · Sin taxes recientes |
| `renta_mensual` | 2200 |
| `test_preparacion` | 7/10 |
| `nivel` | Listo · Casi listo · Empezando |

**Seguimiento sugerido en el workflow:**
- Etiqueta `funnel-primeros-compradores` y otra con el `nivel`.
- **Listo** (y plazo de 0 a 6 meses): llamada o SMS de Tony el mismo día. Es un lead caliente.
- **Casi listo:** SMS y email con el enlace a la guía. Recordatorio para agendar en los días 1, 3 y 7.
- **Empezando:** secuencia educativa de crédito y ahorro de 30 días. Ofrecer la llamada cada semana.
- Enlace a la guía personalizada: `https://tonyvaldesloansinfo.com/primeros-compradores-guia?n={{contact.first_name}}`.

### Fotos

Todas las fotos van **incluidas dentro de cada archivo**, igual que en las otras páginas: no hace falta subir nada a la Biblioteca de Medios y se ven aunque abras el archivo solo. Las fotos de clientes están en `assets/clientes/`. **Confirma que cada cliente que aparece autorizó el uso de su foto.**

## Embudo 1b · Webinar Primeros Compradores (`webinar-primeros-compradores/`)

Para la gente que llega por anuncios de la masterclass. Usa el mismo diseño y **se conecta con el embudo de Primeros Compradores**: desde la confirmación y desde la sala se manda al test (`/primeros-compradores`), y de ahí al resultado y a la cita.

**Recorrido:**
1. **Registro** (`/primeros-compradores-webinar`): hero oscuro tipo escenario con la fecha, cuenta regresiva, qué van a aprender, para quién es, clientes reales, Tony y un formulario con TCPA. Incluye la pregunta opcional "¿Qué te gustaría preguntarle a Tony?".
2. **Lugar reservado** (`/primeros-compradores-webinar-confirmado`): "¡María, tu lugar está reservado!" con 3 pasos: agregar al calendario (Google o Apple/Outlook, se genera solo con la fecha), activar avisos por WhatsApp y hacer el test de 60 segundos. Además, invitar a un amigo y la cuenta regresiva.
3. **Sala** (`/primeros-compradores-webinar-sala`): **cambia sola según la fecha**.
   - **Antes:** cuenta regresiva y botones de calendario.
   - **En vivo:** desde 10 minutos antes hasta 30 minutos después, aparece el botón "Entrar al Zoom ahora".
   - **Después:** la repetición queda anclada.

   Debajo, siempre: hacer el test, agendar la revisión y WhatsApp. Para revisarla en cualquier estado: `?modo=antes`, `?modo=vivo` o `?modo=repeticion`.

### Datos del webinar (un solo lugar)

En `webinar-primeros-compradores/i18n.py` → `EVENT`:
- `start`: fecha y hora con zona horaria. Ejemplo: `2026-11-05T19:00:00-05:00`. Usa `-04:00` en horario de verano del Este y `-05:00` en invierno.
- `minutes`: duración.
- `zoom`: enlace de Zoom. Si está vacío, la sala dice que el enlace llegó por correo y WhatsApp.
- `replay`: enlace de la repetición (YouTube, Vimeo o .mp4). Si está vacío, dice "muy pronto".
- `whatsapp_group`: enlace del grupo. Si está vacío, se usa el WhatsApp de Tony.

Después de cambiar algo: `python3 embudos/_tools/build.py embudos/webinar-primeros-compradores` y vuelve a pegar las 3 páginas. La fecha se muestra en el idioma del visitante y en hora del Este.

### Datos que llegan al workflow

Los de siempre, más:
- `origen` = `webinar-primeros-compradores`
- `objetivo` = `Webinar: primeros compradores`
- `webinar` (nombre)
- `webinar_fecha` (fecha ISO)
- `pregunta` (lo que quiere preguntarle a Tony)

**Secuencia sugerida:**
- Confirmación inmediata con el enlace de la sala.
- Recordatorios: 24 horas antes, 1 hora antes, 10 minutos antes y "¡estamos en vivo!".
- Después del evento: la repetición a quien no asistió y el test a todos.

Enlace de la sala para los mensajes: `https://tonyvaldesloansinfo.com/primeros-compradores-webinar-sala`.

## Landing Inversionistas y Empresarios (`inversionistas-empresarios-landing/`)

Página independiente para anuncios dirigidos a inversionistas y dueños de negocio. Tiene **estilo "Capital"**: azul profundo con retícula tipo plano, marcos con esquinas doradas y dos colores de camino (dorado para inversionista, cobalto para empresario).

- **Hero:** "Financiamiento inteligente para hacer crecer tu capital", con dos botones de camino (**Soy inversionista** / **Soy empresario**), Tony con el sello "Ex-Vicepresidente de Banca Comercial · JP Morgan Chase · Bank of America" y una franja de cifras.
- **Perfiles:** dos tarjetas, inversionista y empresario. Los botones abren la pestaña correcta de programas y marcan el perfil en el formulario.
- **Programas en pestañas:**
  - Inversionistas: Fix & Flip/Bridge, DSCR, construcción, Multifamily 5+, HELOC/HELOAN y Foreign National.
  - Empresarios: Bank Statement, P&L, 1099, Asset-Based, propiedad comercial y Cash-Out/HELOC.
- **"Haz tus números":** calculadora DSCR y una comparación de "lo que muestran tus taxes" contra "lo que muestran tus depósitos".
- Casos reales con fotos de obra, el porqué de Tony, el proceso en 4 pasos y FAQ.
- **Formulario:** perfil, objetivo, deal opcional y TCPA. Llega con `origen = landing-inversionistas-empresarios`, más `perfil` y `deal`.
- **Montaje:** página en GHL con la ruta `inversionistas-empresarios` y el archivo `ghl/landing.html`.

## Embudo Diagnóstico de Financiamiento (`inversionistas-empresarios-embudo/`)

1. **Diagnóstico** (`/diagnostico-financiamiento`): test que **cambia según el perfil**.
   - **Inversionista:** objetivo, experiencia y capital.
   - **Empresario:** objetivo, años del negocio y cómo reflejan sus taxes.
   - **Ambos:** combina las dos.
   - **Todos:** crédito, plazo y formulario con TCPA.
2. **Plan** (`/diagnostico-financiamiento-plan`): "Luis, este es tu plan de financiamiento", con:
   - La **recomendación principal y una alternativa**, cada una con qué documentos preparar.
   - Notas según sus respuestas: crédito, poca experiencia, poco capital, menos de 2 años de negocio.
   - El sello **🔥 Prioridad alta** si ya tiene un deal o quiere avanzar en 30 días.
   - El calendario incrustado con botones de respaldo y casos reales.
3. **Cita confirmada** (`/diagnostico-financiamiento-cita`): qué tener a la mano (para inversionista y para empresario), qué pasa en la llamada y Tony.

**Campos nuevos en el workflow:** `perfil`, `objetivo` (empieza con "Inversión:" o "Empresario:"), `experiencia`, `capital`, `anos_negocio`, `taxes`, `credito`, `plazo` y `origen = funnel-inversionistas-empresarios`.

**Calendario:** usa el calendario principal de Tony. Para que después de agendar lleve a la página 3, clona el calendario y pon la redirección a `/diagnostico-financiamiento-cita`. Luego cambia la URL del calendario en `src/2-plan.html` y regenera.

## Masterclass Inversionistas y Empresarios (`webinar-inversionistas-empresarios/`)

Embudo de la masterclass en vivo **"Inversionistas y Empresarios: cómo identificar oportunidades y financiarlas estratégicamente"**, del jueves 5 de noviembre a las 7:30 p.m. (hora de Atlanta / Miami). Usa el estilo "Capital" y los mismos 3 temas de las piezas de anuncio: estado actual del mercado, oportunidades de inversión en bienes raíces y estrategias + financiamiento inteligente.

| Paso | Ruta | Archivo |
|---|---|---|
| 1 · Registro | `masterclass-inversionistas` | `ghl/1-registro.html` |
| 2 · Lugar reservado | `masterclass-inversionistas-confirmado` | `ghl/2-confirmado.html` |
| 3 · Sala (antes / en vivo / repetición) | `masterclass-inversionistas-sala` | `ghl/3-sala.html` |

- El formulario pregunta el perfil (Inversionista / Empresario / Ambos) y una pregunta opcional para Tony.
- Llega con `origen = webinar-inversionistas-empresarios`, `perfil`, `webinar`, `webinar_fecha` y `pregunta`.
- La confirmación y la sala mandan al **diagnóstico de financiamiento** (`/diagnostico-financiamiento`) y al calendario de Tony.
- La fecha, el Zoom, la repetición y el grupo de WhatsApp se cambian en `EVENT`, dentro de `webinar-inversionistas-empresarios/i18n.py`.

## Fotos de stock

Las fotos de ambiente salen de Unsplash, que permite uso comercial gratis y sin atribución. Están en `assets/stock/`, con los créditos en `assets/stock/CREDITOS.md`:
- Skyline de Atlanta de noche y de Miami.
- Casas modernas iluminadas.
- Obra en construcción, rascacielos y una reunión de negocios.

Van incluidas dentro de cada archivo, como fondos bajo una capa azul de la marca y en las tarjetas de perfil.

## SEO de la masterclass y la landing de inversionistas

Imágenes para redes (1200×630) en `seo/`. Se regeneran con `python3 seo/build_og_embudos.py`.
- `og-masterclass-inversionistas.jpg`: los 3 pasos de la masterclass.
- `og-landing-inversionistas-empresarios.jpg`: la landing.

En GHL van en el paso → **Settings → SEO Meta Data**: título, descripción, palabras clave y **Social Image**. El favicon es `seo/favicon-512.png`, en la configuración del embudo.

| Página | Título | Descripción |
|---|---|---|
| Masterclass · Registro | Masterclass Gratis: Inversionistas y Empresarios \| Tony Valdes | Clase gratis en vivo por Zoom con Tony Valdes: estado del mercado, oportunidades en bienes raíces y financiamiento inteligente. Jueves 5 de nov., 7:30 p.m. |
| Masterclass · Lugar reservado | ¡Tu lugar está reservado! \| Masterclass Tony Valdes | Completa 3 pasos para no perderte la masterclass para inversionistas y empresarios. |
| Masterclass · Sala | Sala de la Masterclass \| Tony Valdes Loans | Entra a la masterclass en vivo o mira la repetición. |
| Landing | Financiamiento para Inversionistas y Empresarios \| Tony Valdes | Fix & Flip, DSCR, multifamily y programas para dueños de negocio: Bank Statement, P&L y propiedad comercial. Análisis gratis con Tony Valdes, NMLS #1593970. |

**Palabras clave de la masterclass:** masterclass inversión inmobiliaria, inversionistas bienes raíces, empresarios, financiamiento para inversionistas, préstamos DSCR, Fix and Flip, Bank Statement, invertir en Atlanta, invertir en Miami, Tony Valdes.

**Palabras clave de la landing:** financiamiento para inversionistas, préstamos para empresarios, préstamo DSCR, Fix and Flip, Bank Statement loan, préstamos para self-employed, propiedad comercial, multifamily, Tony Valdes Loans.

## Cómo regenerar

```bash
python3 embudos/_tools/build.py embudos/primeros-compradores
python3 embudos/_tools/build.py embudos/webinar-primeros-compradores
python3 embudos/_tools/build.py embudos/inversionistas-empresarios-landing
python3 embudos/_tools/build.py embudos/inversionistas-empresarios-embudo
python3 embudos/_tools/build.py embudos/webinar-inversionistas-empresarios
```

El script:
- Une la base compartida (`_shared/`) con el tema y la fuente de cada página.
- Etiqueta los textos y aplica las traducciones de `i18n.py` y de `_tools/memoria.json`, y avisa si falta alguna.
- Incluye las fotos de Tony.
- Genera `revisar/` y `ghl/`.
