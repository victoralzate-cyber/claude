# Prompt para crear el workflow de la Masterclass con la IA de GHL

**Dónde:** Automation → Workflows → **+ Create Workflow** → **Build with AI** (o el ícono ✨ "AI Builder"). Pega el prompt completo.

**Antes de usarlo:**
1. Crea los campos personalizados: **Origen, Idioma, Perfil, Pregunta para Tony, Webinar**. La IA no crea campos.
2. Ten a mano el enlace de Zoom. Si todavía no lo tienes, deja el texto `[ENLACE ZOOM]` y lo cambias después.

---

## Prompt 1 · Workflow "Masterclass Inversionistas – Nov 5"

```
Crea un workflow llamado "Masterclass Inversionistas – Nov 5" para Tony Valdes Loans. Zona horaria de todas las esperas: America/New_York. No permitir re-entrada (allow re-entry desactivado).

TRIGGER: Contact Tag added = "masterclass-inv-nov5".

ACCIONES EN ORDEN:

1) Enviar SMS inmediato:
"¡Hola {{contact.first_name}}! 🎉 Tu lugar en la Masterclass para Inversionistas y Empresarios de Tony Valdes está reservado. 📅 Jueves 5 de noviembre · 7:30 p.m. (Atlanta/Miami). Guarda tu sala: https://tonyvaldesloansinfo.com/masterclass-inversionistas-sala — Tony Valdes Loans. Responde STOP para cancelar."

2) Enviar email inmediato.
Asunto: "{{contact.first_name}}, tu lugar en la Masterclass está confirmado ✅"
Cuerpo: saluda por nombre; confirma la Masterclass gratuita "Inversionistas y Empresarios: cómo identificar oportunidades y financiarlas estratégicamente", jueves 5 de noviembre a las 7:30 p.m. hora de Atlanta/Miami, en vivo por Zoom. Lista los 3 temas: estado actual del mercado; oportunidades de inversión en bienes raíces; estrategias + financiamiento inteligente (DSCR, Bank Statement, equity). Botón "Ir a mi sala" a https://tonyvaldesloansinfo.com/masterclass-inversionistas-sala. Segundo botón "Hacer mi diagnóstico de 60 segundos" a https://tonyvaldesloansinfo.com/diagnostico-financiamiento. Firma: Tony Valdes, Mortgage Loan Officer, NMLS #1593970, Loan Factory NMLS #320841. Pie: "Contenido educativo. No constituye asesoría fiscal o financiera."

3) Notificación interna (email) al usuario asignado / a Tony:
"Nuevo registro Masterclass Inv/Emp: {{contact.name}} · {{contact.phone}} · {{contact.email}}. Perfil: {{contact.perfil}}. Pregunta: {{contact.pregunta_para_tony}}."

4) Esperar hasta el 4 de noviembre de 2026 a las 7:30 PM.
Luego enviar SMS: "{{contact.first_name}}, ¡mañana es la Masterclass! 🔥 Jueves 7:30 p.m. (Atlanta/Miami) con Tony Valdes. Trae tus preguntas y, si tienes un deal en mente, tráelo. Tu sala: https://tonyvaldesloansinfo.com/masterclass-inversionistas-sala"
Y enviar email con asunto "Mañana: Masterclass para Inversionistas y Empresarios", recordatorio corto con fecha, hora y botón a la sala.

5) Esperar hasta el 5 de noviembre de 2026 a las 6:30 PM.
Enviar SMS: "⏰ {{contact.first_name}}, en 1 hora empezamos la Masterclass con Tony Valdes (7:30 p.m.). Ten listo papel y tus preguntas. Sala: https://tonyvaldesloansinfo.com/masterclass-inversionistas-sala"

6) Esperar hasta el 5 de noviembre de 2026 a las 7:28 PM.
Enviar SMS: "🔴 ¡Estamos EN VIVO! Entra ahora: [ENLACE ZOOM] — Tony Valdes Loans"
Enviar email con asunto "🔴 Estamos en vivo: entra ahora" y un botón grande "Entrar a Zoom" a [ENLACE ZOOM].

7) Esperar hasta el 6 de noviembre de 2026 a las 10:00 AM.
Enviar SMS: "{{contact.first_name}}, gracias por registrarte a la Masterclass 🙌 ¿No pudiste verla completa? Aquí está la repetición: https://tonyvaldesloansinfo.com/masterclass-inversionistas-sala — Y si quieres revisar tu caso con Tony, haz tu diagnóstico gratis: https://tonyvaldesloansinfo.com/diagnostico-financiamiento"
Enviar email con asunto "La repetición de la Masterclass + tu siguiente paso": botón a la repetición (sala), resumen de los 3 temas y botón "Agendar mi análisis con Tony" a https://api.leadconnectorhq.com/widget/bookings/calendario-tony-valdes-loans.

8) Esperar hasta el 8 de noviembre de 2026 a las 11:00 AM.
Enviar SMS: "{{contact.first_name}}, soy Tony 👋 ¿Qué te pareció la Masterclass? Si tienes un deal o un negocio que quieras revisar, agenda 15 minutos conmigo: https://api.leadconnectorhq.com/widget/bookings/calendario-tony-valdes-loans"

9) Esperar hasta el 11 de noviembre de 2026 a las 11:00 AM.
Enviar email con asunto "¿Seguimos con tu plan de inversión?": cuenta el caso real Duncan Drive (compra de $235,000 + remodelación de $70,000, vendida en $419,999, más de $100K de ganancia; los resultados pueden variar) e invita a agendar con el botón del calendario.

10) Agregar el tag "masterclass-inv-nov5-terminado".

REGLAS:
- Antes de cada espera de los pasos 4, 5 y 6, agrega una condición If/Else: si la fecha y hora actual ya pasó la hora de esa espera, saltar ese recordatorio y continuar con el siguiente.
- Respetar horario de envío de SMS entre 8:00 AM y 9:00 PM.
- Escribir todo en español latino neutro, cercano y profesional.
```

---

## Prompt 2 (opcional) · Rama en el workflow "Lead Web – Tony Valdes Loans"

Este cambio conviene hacerlo **a mano** sobre el workflow que ya funciona, para no romper el mapeo del webhook. Si prefieres pedírselo a la IA dentro de ese workflow, usa:

```
En este workflow, después de la acción Create/Update Contact, agrega una condición If/Else llamada "¿De dónde viene?". Rama "Masterclass Inversionistas": si el campo personalizado Origen es igual a "webinar-inversionistas-empresarios", agregar el tag "masterclass-inv-nov5" y añadir el contacto al workflow "Masterclass Inversionistas – Nov 5". En la rama None, mantener las acciones actuales.
```

---

## Revisión después de que la IA lo cree

La IA de GHL a veces deja pasos a medias. Revisa:
1. Que el **trigger** sea el tag `masterclass-inv-nov5`.
2. Que las **esperas** sean "until specific date/time" con la fecha y la hora correctas, en **America/New_York**.
3. Que los **enlaces** de los mensajes estén completos y que `[ENLACE ZOOM]` esté reemplazado.
4. Que las **variables** de perfil y pregunta coincidan con el nombre real de tus campos en el selector `{{ }}`.
5. Que el workflow esté en **Publish** (no en Draft) antes del primer registro.
