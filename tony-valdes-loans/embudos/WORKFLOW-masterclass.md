# Workflow · Masterclass Inversionistas y Empresarios (jueves 5 de noviembre, 7:30 p.m. ET)

Todos los formularios de la web y de los embudos llegan al **mismo webhook**. El plan:
1. El workflow que ya existe (**Lead Web – Tony Valdes Loans**) crea o actualiza el contacto y lo **reparte según `origen`**.
2. La masterclass tiene **su propio workflow** con confirmación, recordatorios y seguimiento.

---

## Parte 1 · Campos personalizados (una sola vez)

En **Settings → Custom Fields → + Add Field**, tipo *Single line* salvo que se indique otro:

| Nombre | Clave sugerida | Para qué |
|---|---|---|
| Origen | `origen` | De qué página o embudo vino el lead |
| Idioma | `idioma` | es / en / pt, para mandarle los mensajes en su idioma |
| Perfil | `perfil` | Inversionista / Empresario / Ambos |
| Pregunta para Tony | `pregunta_tony` | *Multi line*: lo que quiere preguntar en la clase |
| Webinar | `webinar` | Nombre del webinar |

## Parte 2 · Ajustar el workflow "Lead Web – Tony Valdes Loans"

1. Abre la acción **Create/Update Contact** y mapea los campos nuevos:
   - Origen → `{{inboundWebhookRequest.origen}}`
   - Idioma → `{{inboundWebhookRequest.idioma}}`
   - Perfil → `{{inboundWebhookRequest.perfil}}`
   - Pregunta para Tony → `{{inboundWebhookRequest.pregunta}}`
   - Webinar → `{{inboundWebhookRequest.webinar}}`
2. Debajo agrega **If/Else** y llámalo "¿De dónde viene?". Rama 1:
   - Nombre: **Masterclass Inversionistas**.
   - Condición: *Custom Field → Origen* **is** `webinar-inversionistas-empresarios`.
3. Dentro de esa rama:
   - **Add Contact Tag**: `masterclass-inv-nov5`.
   - **Add to Workflow**: *Masterclass Inversionistas – Nov 5* (lo creas en la Parte 3).
4. En la rama **None** dejas lo que ya tienes: la notificación general a Tony.

> Más adelante agregamos otras ramas en este mismo If/Else, una por cada `origen`: `funnel-primeros-compradores`, `webinar-primeros-compradores`, `funnel-inversionistas-empresarios` y `landing-inversionistas-empresarios`.

## Parte 3 · Workflow "Masterclass Inversionistas – Nov 5"

**Trigger:** *Contact Tag* → Tag added → `masterclass-inv-nov5`.
**Settings del workflow:** activa **Allow re-entry: off**, para que nadie reciba los mensajes dos veces.

### Paso 1 · Confirmación inmediata

**SMS**
```
¡Hola {{contact.first_name}}! 🎉 Tu lugar en la Masterclass para Inversionistas y Empresarios de Tony Valdes está reservado.
📅 Jueves 5 de noviembre · 7:30 p.m. (Atlanta/Miami)
Guarda tu sala: https://tonyvaldesloansinfo.com/masterclass-inversionistas-sala
Tony Valdes Loans. Responde STOP para cancelar.
```

**Email**
- **Asunto:** `{{contact.first_name}}, tu lugar en la Masterclass está confirmado ✅`
- **Cuerpo:**
```
Hola {{contact.first_name}},

¡Ya estás dentro! Te espero en la Masterclass gratuita:

INVERSIONISTAS Y EMPRESARIOS
Cómo identificar oportunidades y financiarlas estratégicamente

📅 Jueves 5 de noviembre · 🕖 7:30 p.m. (hora de Atlanta / Miami) · 💻 En vivo por Zoom

Vamos a ver:
• El estado actual del mercado
• Dónde están las oportunidades de inversión en bienes raíces
• Estrategias + financiamiento inteligente (DSCR, Bank Statement, equity y más)

👉 Esta es tu sala (guárdala): https://tonyvaldesloansinfo.com/masterclass-inversionistas-sala

Mientras tanto, haz tu diagnóstico de financiamiento de 60 segundos y llega con tus preguntas listas:
https://tonyvaldesloansinfo.com/diagnostico-financiamiento

¡Nos vemos en vivo!
Tony Valdes
Mortgage Loan Officer · NMLS #1593970 · Loan Factory NMLS #320841

Contenido educativo. No constituye asesoría fiscal o financiera.
```

### Paso 2 · Aviso interno a Tony

**Internal Notification** (email o SMS a Tony):
```
Nuevo registro Masterclass Inv/Emp: {{contact.name}} · {{contact.phone}}
Perfil: {{contact.perfil}}
Pregunta: {{contact.pregunta_tony}}
```
Aquí usa los nombres de tus campos personalizados tal como los muestre GHL en el selector de variables.

### Paso 3 · Recordatorio 24 horas antes

- **Wait** → *Until specific date/time* → **4 de noviembre de 2026, 7:30 p.m.**, zona **America/New_York**.
- **SMS**
```
{{contact.first_name}}, ¡mañana es la Masterclass! 🔥 Jueves 7:30 p.m. (Atlanta/Miami) con Tony Valdes. Trae tus preguntas y, si tienes un deal en mente, tráelo. Tu sala: https://tonyvaldesloansinfo.com/masterclass-inversionistas-sala
```
- **Email**
  - **Asunto:** `Mañana: Masterclass para Inversionistas y Empresarios`
  - **Cuerpo:** recordatorio corto con la fecha, la hora y el enlace de la sala.

### Paso 4 · Recordatorio 1 hora antes

- **Wait** → *Until* **5 de noviembre de 2026, 6:30 p.m.** (America/New_York).
- **SMS**
```
⏰ {{contact.first_name}}, en 1 hora empezamos la Masterclass con Tony Valdes (7:30 p.m.). Ten listo papel y tus preguntas. Sala: https://tonyvaldesloansinfo.com/masterclass-inversionistas-sala
```

### Paso 5 · "Estamos en vivo"

- **Wait** → *Until* **5 de noviembre de 2026, 7:28 p.m.**
- **SMS**
```
🔴 ¡Estamos EN VIVO! Entra ahora: [ENLACE DE ZOOM]
Tony Valdes Loans
```
- **Email**
  - **Asunto:** `🔴 Estamos en vivo: entra ahora`
  - **Cuerpo:** el botón con el enlace de Zoom.

> El SMS y el email de este paso llevan el **enlace directo de Zoom**. Pégalo cuando lo tengas.

### Paso 6 · Repetición y siguiente paso (día siguiente)

- **Wait** → *Until* **6 de noviembre de 2026, 10:00 a.m.**
- **SMS**
```
{{contact.first_name}}, gracias por registrarte a la Masterclass 🙌 ¿No pudiste verla completa? Aquí está la repetición: https://tonyvaldesloansinfo.com/masterclass-inversionistas-sala
Y si quieres revisar tu caso con Tony, haz tu diagnóstico gratis: https://tonyvaldesloansinfo.com/diagnostico-financiamiento
```
- **Email**
  - **Asunto:** `La repetición de la Masterclass + tu siguiente paso`
  - **Cuerpo:** el enlace de la repetición, un resumen de los 3 temas y un botón para agendar el análisis con el calendario de Tony.

### Paso 7 · Seguimiento (8 de noviembre, 11:00 a.m.)

- **Wait** → *Until* **8 de noviembre de 2026, 11:00 a.m.**
- **SMS**
```
{{contact.first_name}}, soy Tony 👋 ¿Qué te pareció la Masterclass? Si tienes un deal o un negocio que quieras revisar, agenda 15 minutos conmigo: https://api.leadconnectorhq.com/widget/bookings/calendario-tony-valdes-loans
```

### Paso 8 · Último empujón (11 de noviembre)

- **Wait** → *Until* **11 de noviembre de 2026, 11:00 a.m.**
- **Email**
  - **Asunto:** `¿Seguimos con tu plan de inversión?`
  - **Cuerpo:** un caso real (Duncan Drive, por ejemplo) y la invitación a agendar.
- Después, **Add Tag** `masterclass-inv-nov5-terminado`.

---

## Detalles importantes

1. **Si alguien se registra tarde:** en GHL, cuando la fecha de un *Wait until* ya pasó, el contacto **sigue de inmediato al próximo paso**. Alguien que se registre el mismo día recibiría seguidos los recordatorios que ya pasaron. Para evitarlo:
   - Antes de cada recordatorio pon un **If/Else**: *Date/Time → Current date/time is before* la hora de ese recordatorio. Si no, salta al siguiente paso.
   - Si tu cuenta no muestra esa condición, avísame y lo resolvemos con un segundo workflow para registros del mismo día.
2. **Si agenda una cita con Tony,** sácalo del seguimiento de venta: en el workflow de citas, **Remove from Workflow** → *Masterclass Inversionistas – Nov 5*, pero solo después del Paso 6.
3. **SMS:**
   - Que cada mensaje empiece o termine con el nombre de la marca.
   - El primero lleva "Responde STOP para cancelar", como pide el registro A2P.
   - No envíes SMS antes de las 8:00 a.m. ni después de las 9:00 p.m., hora del contacto.
4. **Idioma:** los textos de arriba están en español. Para los inscritos en inglés o portugués, pon un **If/Else** por *Idioma* (`en`, `pt`) antes de cada mensaje y duplica el SMS o el email traducido.
5. **Asistencia:** después del evento puedes exportar los asistentes de Zoom y ponerles la etiqueta `asistio-masterclass-nov5`. Así le mandas un mensaje distinto a quien sí asistió ("gracias por estar") y a quien no ("aquí está la repetición").
6. **Prueba:**
   - Regístrate con tu propio número y correo.
   - Revisa que llegue la confirmación y que el contacto tenga la etiqueta y los campos llenos.
   - Saca tu contacto del workflow para no recibir todos los recordatorios.
