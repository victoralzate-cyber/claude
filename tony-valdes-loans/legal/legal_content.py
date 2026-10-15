# Contenido de las páginas legales de Tony Valdes Loans (ES / EN / PT).
# build_legal.py genera las páginas HTML a partir de este archivo.

EFFECTIVE = {"es": "Vigente desde: 15 de octubre de 2026",
             "en": "Effective date: October 15, 2026",
             "pt": "Vigente desde: 15 de outubro de 2026"}

CONTACT = {
 "es": "<p><strong>Tony Valdes Loans</strong><br>Tony Valdes, Mortgage Loan Officer, NMLS #1593970<br>Loan Factory, Inc., NMLS #320841<br>Teléfono: <a href=\"tel:+17708656771\">(770) 865-6771</a> · WhatsApp: <a href=\"https://wa.me/17708653002\">(770) 865-3002</a><br>Email: <a href=\"mailto:info@tonyvaldesloans.com\">info@tonyvaldesloans.com</a></p>",
 "en": "<p><strong>Tony Valdes Loans</strong><br>Tony Valdes, Mortgage Loan Officer, NMLS #1593970<br>Loan Factory, Inc., NMLS #320841<br>Phone: <a href=\"tel:+17708656771\">(770) 865-6771</a> · WhatsApp: <a href=\"https://wa.me/17708653002\">(770) 865-3002</a><br>Email: <a href=\"mailto:info@tonyvaldesloans.com\">info@tonyvaldesloans.com</a></p>",
 "pt": "<p><strong>Tony Valdes Loans</strong><br>Tony Valdes, Mortgage Loan Officer, NMLS #1593970<br>Loan Factory, Inc., NMLS #320841<br>Telefone: <a href=\"tel:+17708656771\">(770) 865-6771</a> · WhatsApp: <a href=\"https://wa.me/17708653002\">(770) 865-3002</a><br>E-mail: <a href=\"mailto:info@tonyvaldesloans.com\">info@tonyvaldesloans.com</a></p>",
}

PAGES = {
"privacidad": {
 "title": {"es": "Política de Privacidad", "en": "Privacy Policy", "pt": "Política de Privacidade"},
 "intro": {
  "es": "En Tony Valdes Loans respetamos tu privacidad. Esta política explica qué información recopilamos cuando visitas nuestro sitio web o te comunicas con nosotros, cómo la usamos y qué opciones tienes.",
  "en": "At Tony Valdes Loans we respect your privacy. This policy explains what information we collect when you visit our website or contact us, how we use it, and the choices you have.",
  "pt": "Na Tony Valdes Loans respeitamos sua privacidade. Esta política explica quais informações coletamos quando você visita nosso site ou entra em contato conosco, como as usamos e quais opções você tem."},
 "sections": [
  {"h": {"es": "1. Información que recopilamos", "en": "1. Information we collect", "pt": "1. Informações que coletamos"},
   "b": {
    "es": "<p>Recopilamos la información que tú nos das voluntariamente al llenar un formulario, agendar una cita o escribirnos:</p><ul><li>Nombre, teléfono y correo electrónico.</li><li>Tu objetivo (por ejemplo, comprar casa, invertir o refinanciar) y tu idioma preferido.</li><li>La fecha y la página desde donde diste tu consentimiento para ser contactado.</li></ul><p>Si decides avanzar con un préstamo, durante el proceso de solicitud podemos pedirte información financiera adicional (ingresos, empleo, crédito, activos). Esa información se maneja de acuerdo con la ley Gramm-Leach-Bliley (GLBA) y la política de privacidad de Loan Factory, Inc.</p><p>También recopilamos de forma automática datos técnicos básicos, como el tipo de navegador, el dispositivo, las páginas visitadas y la dirección IP, mediante cookies y tecnologías similares.</p>",
    "en": "<p>We collect the information you voluntarily provide when you fill out a form, book an appointment or message us:</p><ul><li>Name, phone number and email address.</li><li>Your goal (for example, buying a home, investing or refinancing) and your preferred language.</li><li>The date and page where you gave your consent to be contacted.</li></ul><p>If you decide to move forward with a loan, during the application process we may request additional financial information (income, employment, credit, assets). That information is handled in accordance with the Gramm-Leach-Bliley Act (GLBA) and the privacy policy of Loan Factory, Inc.</p><p>We also automatically collect basic technical data, such as browser type, device, pages visited and IP address, through cookies and similar technologies.</p>",
    "pt": "<p>Coletamos as informações que você nos fornece voluntariamente ao preencher um formulário, agendar um horário ou nos enviar uma mensagem:</p><ul><li>Nome, telefone e e-mail.</li><li>Seu objetivo (por exemplo, comprar casa, investir ou refinanciar) e seu idioma preferido.</li><li>A data e a página em que você deu seu consentimento para ser contatado.</li></ul><p>Se você decidir seguir com um empréstimo, durante o processo de solicitação podemos pedir informações financeiras adicionais (renda, emprego, crédito, ativos). Essas informações são tratadas de acordo com a lei Gramm-Leach-Bliley (GLBA) e a política de privacidade da Loan Factory, Inc.</p><p>Também coletamos automaticamente dados técnicos básicos, como tipo de navegador, dispositivo, páginas visitadas e endereço IP, por meio de cookies e tecnologias semelhantes.</p>"}},
  {"h": {"es": "2. Cómo usamos tu información", "en": "2. How we use your information", "pt": "2. Como usamos suas informações"},
   "b": {
    "es": "<ul><li>Responder a tus preguntas y contactarte sobre las opciones de financiamiento que solicitaste.</li><li>Agendar y confirmar asesorías.</li><li>Enviarte información educativa, recordatorios y novedades del mercado, si lo autorizaste.</li><li>Mejorar nuestro sitio web y nuestros servicios.</li><li>Cumplir con obligaciones legales y regulatorias.</li></ul>",
    "en": "<ul><li>Respond to your questions and contact you about the financing options you requested.</li><li>Schedule and confirm consultations.</li><li>Send you educational information, reminders and market updates, if you authorized it.</li><li>Improve our website and services.</li><li>Comply with legal and regulatory obligations.</li></ul>",
    "pt": "<ul><li>Responder às suas perguntas e entrar em contato sobre as opções de financiamento que você solicitou.</li><li>Agendar e confirmar consultorias.</li><li>Enviar informações educativas, lembretes e novidades do mercado, se você autorizou.</li><li>Melhorar nosso site e nossos serviços.</li><li>Cumprir obrigações legais e regulatórias.</li></ul>"}},
  {"h": {"es": "3. Mensajes de texto (SMS) y WhatsApp", "en": "3. Text messages (SMS) and WhatsApp", "pt": "3. Mensagens de texto (SMS) e WhatsApp"},
   "b": {
    "es": "<p>Si nos das tu consentimiento, podemos enviarte mensajes de texto o de WhatsApp relacionados con tu consulta, tus citas y tu proceso de préstamo. La frecuencia de los mensajes varía. Pueden aplicar tarifas de mensajes y datos de tu operador.</p><p>Puedes cancelar en cualquier momento respondiendo <strong>STOP</strong>. Para recibir ayuda, responde <strong>HELP</strong> o escríbenos a info@tonyvaldesloans.com.</p><p><strong>No compartimos, vendemos ni alquilamos tu número de teléfono móvil ni tu consentimiento para recibir mensajes de texto con terceros o afiliados para sus fines de marketing.</strong> Los datos de suscripción a SMS y el consentimiento no se comparten con ningún tercero, salvo con los proveedores que nos ayudan a enviar los mensajes.</p>",
    "en": "<p>If you give us your consent, we may send you text or WhatsApp messages related to your inquiry, your appointments and your loan process. Message frequency varies. Message and data rates from your carrier may apply.</p><p>You can opt out at any time by replying <strong>STOP</strong>. For help, reply <strong>HELP</strong> or email us at info@tonyvaldesloans.com.</p><p><strong>We do not share, sell or rent your mobile phone number or your text messaging consent with third parties or affiliates for their marketing purposes.</strong> SMS opt-in data and consent are not shared with any third parties, except the providers that help us deliver the messages.</p>",
    "pt": "<p>Se você nos der seu consentimento, podemos enviar mensagens de texto ou de WhatsApp relacionadas à sua consulta, seus agendamentos e seu processo de empréstimo. A frequência das mensagens varia. Podem ser cobradas tarifas de mensagens e dados pela sua operadora.</p><p>Você pode cancelar a qualquer momento respondendo <strong>STOP</strong>. Para ajuda, responda <strong>HELP</strong> ou escreva para info@tonyvaldesloans.com.</p><p><strong>Não compartilhamos, vendemos nem alugamos seu número de celular nem seu consentimento para receber mensagens de texto com terceiros ou afiliados para fins de marketing deles.</strong> Os dados de inscrição em SMS e o consentimento não são compartilhados com terceiros, exceto com os provedores que nos ajudam a enviar as mensagens.</p>"}},
  {"h": {"es": "4. Con quién compartimos tu información", "en": "4. Who we share your information with", "pt": "4. Com quem compartilhamos suas informações"},
   "b": {
    "es": "<p><strong>No vendemos tu información personal.</strong> Solo la compartimos cuando es necesario para atenderte:</p><ul><li>Con Loan Factory, Inc. y los prestamistas, procesadores, tasadores y compañías de título que participan en tu préstamo, si decides solicitarlo.</li><li>Con proveedores de tecnología que nos ayudan a operar (por ejemplo, nuestro CRM, el calendario, el email y las plataformas de mensajería), que solo pueden usarla para prestarnos ese servicio.</li><li>Cuando la ley, una autoridad o un proceso legal lo exijan.</li></ul>",
    "en": "<p><strong>We do not sell your personal information.</strong> We only share it when needed to serve you:</p><ul><li>With Loan Factory, Inc. and the lenders, processors, appraisers and title companies involved in your loan, if you choose to apply.</li><li>With technology providers that help us operate (for example, our CRM, calendar, email and messaging platforms), who may only use it to provide that service to us.</li><li>When required by law, a regulator or legal process.</li></ul>",
    "pt": "<p><strong>Não vendemos suas informações pessoais.</strong> Só as compartilhamos quando necessário para atendê-lo:</p><ul><li>Com a Loan Factory, Inc. e os credores, processadores, avaliadores e empresas de título envolvidos no seu empréstimo, se você decidir solicitá-lo.</li><li>Com provedores de tecnologia que nos ajudam a operar (por exemplo, nosso CRM, agenda, e-mail e plataformas de mensagens), que só podem usá-las para nos prestar esse serviço.</li><li>Quando exigido por lei, por uma autoridade ou por um processo legal.</li></ul>"}},
  {"h": {"es": "5. Cookies", "en": "5. Cookies", "pt": "5. Cookies"},
   "b": {
    "es": "<p>Usamos cookies para que el sitio funcione correctamente, recordar tu idioma preferido y entender cómo se usa el sitio. Puedes bloquear o borrar las cookies desde la configuración de tu navegador; algunas funciones podrían dejar de funcionar.</p>",
    "en": "<p>We use cookies to make the site work properly, remember your preferred language and understand how the site is used. You can block or delete cookies in your browser settings; some features may stop working.</p>",
    "pt": "<p>Usamos cookies para que o site funcione corretamente, lembrar seu idioma preferido e entender como o site é usado. Você pode bloquear ou apagar os cookies nas configurações do seu navegador; alguns recursos podem deixar de funcionar.</p>"}},
  {"h": {"es": "6. Seguridad", "en": "6. Security", "pt": "6. Segurança"},
   "b": {
    "es": "<p>Aplicamos medidas administrativas, técnicas y físicas razonables para proteger tu información. Ningún sistema es 100% seguro, por lo que no podemos garantizar una seguridad absoluta. Nunca te pediremos datos bancarios ni tu número de Seguro Social por mensaje de texto o redes sociales.</p>",
    "en": "<p>We apply reasonable administrative, technical and physical safeguards to protect your information. No system is 100% secure, so we cannot guarantee absolute security. We will never ask for your bank details or Social Security number by text message or social media.</p>",
    "pt": "<p>Aplicamos medidas administrativas, técnicas e físicas razoáveis para proteger suas informações. Nenhum sistema é 100% seguro, por isso não podemos garantir segurança absoluta. Nunca pediremos seus dados bancários ou seu número de Seguro Social por mensagem de texto ou redes sociais.</p>"}},
  {"h": {"es": "7. Tus opciones y derechos", "en": "7. Your choices and rights", "pt": "7. Suas opções e direitos"},
   "b": {
    "es": "<ul><li>Dejar de recibir mensajes de texto respondiendo STOP, o emails usando el enlace para cancelar la suscripción.</li><li>Pedirnos acceso, corrección o eliminación de tu información, escribiendo a info@tonyvaldesloans.com. Algunos registros deben conservarse por obligación legal.</li><li>Según el estado donde vivas, puedes tener derechos adicionales sobre tus datos personales.</li></ul>",
    "en": "<ul><li>Stop receiving text messages by replying STOP, or emails by using the unsubscribe link.</li><li>Request access to, correction of or deletion of your information by emailing info@tonyvaldesloans.com. Some records must be kept by law.</li><li>Depending on the state where you live, you may have additional rights over your personal data.</li></ul>",
    "pt": "<ul><li>Deixar de receber mensagens de texto respondendo STOP, ou e-mails usando o link de cancelamento.</li><li>Pedir acesso, correção ou exclusão das suas informações escrevendo para info@tonyvaldesloans.com. Alguns registros devem ser mantidos por obrigação legal.</li><li>Dependendo do estado onde você mora, você pode ter direitos adicionais sobre seus dados pessoais.</li></ul>"}},
  {"h": {"es": "8. Menores de edad", "en": "8. Children", "pt": "8. Menores de idade"},
   "b": {
    "es": "<p>Nuestro sitio está dirigido a personas mayores de 18 años. No recopilamos a sabiendas información de menores de 13 años.</p>",
    "en": "<p>Our site is intended for people 18 and older. We do not knowingly collect information from children under 13.</p>",
    "pt": "<p>Nosso site é destinado a maiores de 18 anos. Não coletamos intencionalmente informações de menores de 13 anos.</p>"}},
  {"h": {"es": "9. Cambios a esta política", "en": "9. Changes to this policy", "pt": "9. Alterações desta política"},
   "b": {
    "es": "<p>Podemos actualizar esta política. Publicaremos la versión vigente en esta página con su fecha de actualización.</p>",
    "en": "<p>We may update this policy. We will post the current version on this page with its updated date.</p>",
    "pt": "<p>Podemos atualizar esta política. Publicaremos a versão vigente nesta página com a data de atualização.</p>"}},
  {"h": {"es": "10. Contacto", "en": "10. Contact", "pt": "10. Contato"}, "b": "CONTACT"},
 ]},

"terminos": {
 "title": {"es": "Términos y Condiciones", "en": "Terms and Conditions", "pt": "Termos e Condições"},
 "intro": {
  "es": "Al usar el sitio web de Tony Valdes Loans aceptas estos Términos y Condiciones. Si no estás de acuerdo, por favor no uses el sitio.",
  "en": "By using the Tony Valdes Loans website you agree to these Terms and Conditions. If you do not agree, please do not use the site.",
  "pt": "Ao usar o site da Tony Valdes Loans você aceita estes Termos e Condições. Se não concordar, por favor não use o site."},
 "sections": [
  {"h": {"es": "1. Quiénes somos", "en": "1. Who we are", "pt": "1. Quem somos"},
   "b": {
    "es": "<p>Tony Valdes es Mortgage Loan Officer con licencia, NMLS #1593970, y opera con Loan Factory, Inc., NMLS #320841. Puedes verificar las licencias en <a href=\"https://www.nmlsconsumeraccess.org/\" target=\"_blank\" rel=\"noopener\">NMLS Consumer Access</a>. Los servicios hipotecarios solo se ofrecen en los estados donde existe licencia vigente.</p>",
    "en": "<p>Tony Valdes is a licensed Mortgage Loan Officer, NMLS #1593970, operating with Loan Factory, Inc., NMLS #320841. You can verify licenses at <a href=\"https://www.nmlsconsumeraccess.org/\" target=\"_blank\" rel=\"noopener\">NMLS Consumer Access</a>. Mortgage services are only offered in states where a current license is held.</p>",
    "pt": "<p>Tony Valdes é Mortgage Loan Officer licenciado, NMLS #1593970, e atua com a Loan Factory, Inc., NMLS #320841. Você pode verificar as licenças em <a href=\"https://www.nmlsconsumeraccess.org/\" target=\"_blank\" rel=\"noopener\">NMLS Consumer Access</a>. Os serviços hipotecários só são oferecidos nos estados onde há licença vigente.</p>"}},
  {"h": {"es": "2. No es una oferta de préstamo", "en": "2. Not an offer to lend", "pt": "2. Não é uma oferta de empréstimo"},
   "b": {
    "es": "<p>La información de este sitio es general y educativa. No constituye una oferta de préstamo, una aprobación ni un compromiso de prestar. Todos los préstamos están sujetos a la aprobación de crédito, verificación de ingresos y activos, tasación y suscripción (underwriting). Los programas, tasas, términos y condiciones pueden cambiar sin previo aviso y no están disponibles en todos los estados.</p>",
    "en": "<p>The information on this site is general and educational. It is not an offer to lend, an approval or a commitment to lend. All loans are subject to credit approval, income and asset verification, appraisal and underwriting. Programs, rates, terms and conditions are subject to change without notice and are not available in all states.</p>",
    "pt": "<p>As informações deste site são gerais e educativas. Não constituem uma oferta de empréstimo, uma aprovação nem um compromisso de emprestar. Todos os empréstimos estão sujeitos à aprovação de crédito, comprovação de renda e ativos, avaliação e análise (underwriting). Programas, taxas, termos e condições podem mudar sem aviso prévio e não estão disponíveis em todos os estados.</p>"}},
  {"h": {"es": "3. Casos y resultados", "en": "3. Cases and results", "pt": "3. Casos e resultados"},
   "b": {
    "es": "<p>Los casos presentados son ejemplos reales de clientes y se muestran con fines ilustrativos. Los resultados individuales pueden variar según la calificación de cada cliente, la propiedad y las condiciones del mercado. No garantizamos resultados específicos.</p>",
    "en": "<p>The cases shown are real client examples presented for illustrative purposes. Individual results may vary depending on each client's qualifications, the property and market conditions. We do not guarantee specific results.</p>",
    "pt": "<p>Os casos apresentados são exemplos reais de clientes, mostrados para fins ilustrativos. Os resultados individuais podem variar conforme a qualificação de cada cliente, o imóvel e as condições de mercado. Não garantimos resultados específicos.</p>"}},
  {"h": {"es": "4. No es asesoría legal ni fiscal", "en": "4. Not legal or tax advice", "pt": "4. Não é assessoria jurídica ou fiscal"},
   "b": {
    "es": "<p>Nada de lo publicado en este sitio constituye asesoría legal, fiscal ni contable. Consulta con tu abogado o contador antes de tomar decisiones.</p>",
    "en": "<p>Nothing published on this site constitutes legal, tax or accounting advice. Consult your attorney or accountant before making decisions.</p>",
    "pt": "<p>Nada do que é publicado neste site constitui assessoria jurídica, fiscal ou contábil. Consulte seu advogado ou contador antes de tomar decisões.</p>"}},
  {"h": {"es": "5. Consentimiento para comunicaciones", "en": "5. Consent to communications", "pt": "5. Consentimento para comunicações"},
   "b": {
    "es": "<p>Al enviar un formulario en este sitio y marcar la casilla de consentimiento, autorizas a Tony Valdes Loans a contactarte por llamada, mensaje de texto (SMS), WhatsApp o correo electrónico al número y correo que proporcionaste, incluso mediante sistemas automatizados, en relación con tu consulta y servicios de financiamiento. El consentimiento no es condición para recibir servicios.</p><p><strong>Programa de mensajes de texto:</strong> la frecuencia de los mensajes varía. Pueden aplicar tarifas de mensajes y datos. Responde <strong>STOP</strong> para cancelar o <strong>HELP</strong> para recibir ayuda. Los operadores móviles no son responsables de mensajes retrasados o no entregados. Consulta nuestra <a href=\"/privacidad\">Política de Privacidad</a>.</p>",
    "en": "<p>By submitting a form on this site and checking the consent box, you authorize Tony Valdes Loans to contact you by phone call, text message (SMS), WhatsApp or email at the number and email you provided, including through automated systems, regarding your inquiry and financing services. Consent is not a condition of receiving services.</p><p><strong>Text messaging program:</strong> message frequency varies. Message and data rates may apply. Reply <strong>STOP</strong> to opt out or <strong>HELP</strong> for help. Carriers are not liable for delayed or undelivered messages. See our <a href=\"/privacidad\">Privacy Policy</a>.</p>",
    "pt": "<p>Ao enviar um formulário neste site e marcar a caixa de consentimento, você autoriza a Tony Valdes Loans a contatá-lo por ligação, mensagem de texto (SMS), WhatsApp ou e-mail no número e e-mail informados, inclusive por sistemas automatizados, em relação à sua consulta e aos serviços de financiamento. O consentimento não é condição para receber os serviços.</p><p><strong>Programa de mensagens de texto:</strong> a frequência das mensagens varia. Podem ser cobradas tarifas de mensagens e dados. Responda <strong>STOP</strong> para cancelar ou <strong>HELP</strong> para ajuda. As operadoras não são responsáveis por mensagens atrasadas ou não entregues. Consulte nossa <a href=\"/privacidad\">Política de Privacidade</a>.</p>"}},
  {"h": {"es": "6. Uso del sitio", "en": "6. Use of the site", "pt": "6. Uso do site"},
   "b": {
    "es": "<p>Te comprometes a usar el sitio de forma legal y a proporcionar información verdadera y actualizada. No puedes intentar dañar el sitio, acceder sin autorización a sus sistemas ni usarlo para enviar información falsa o de otra persona.</p>",
    "en": "<p>You agree to use the site lawfully and to provide true and current information. You may not attempt to damage the site, access its systems without authorization, or use it to submit false information or someone else's information.</p>",
    "pt": "<p>Você se compromete a usar o site de forma legal e a fornecer informações verdadeiras e atualizadas. Você não pode tentar danificar o site, acessar seus sistemas sem autorização nem usá-lo para enviar informações falsas ou de outra pessoa.</p>"}},
  {"h": {"es": "7. Propiedad intelectual", "en": "7. Intellectual property", "pt": "7. Propriedade intelectual"},
   "b": {
    "es": "<p>El logo, la marca Tony Valdes Loans, las fotografías, los textos y el diseño de este sitio son propiedad de Tony Valdes Loans o se usan con autorización. No pueden copiarse ni usarse sin permiso por escrito.</p>",
    "en": "<p>The logo, the Tony Valdes Loans brand, photographs, text and design of this site are owned by Tony Valdes Loans or used with permission. They may not be copied or used without written permission.</p>",
    "pt": "<p>O logotipo, a marca Tony Valdes Loans, as fotografias, os textos e o design deste site são de propriedade da Tony Valdes Loans ou usados com autorização. Não podem ser copiados nem usados sem permissão por escrito.</p>"}},
  {"h": {"es": "8. Enlaces a terceros", "en": "8. Third-party links", "pt": "8. Links de terceiros"},
   "b": {
    "es": "<p>El sitio puede incluir enlaces a sitios de terceros (por ejemplo, redes sociales, WhatsApp o NMLS). No controlamos ni somos responsables de su contenido ni de sus prácticas de privacidad.</p>",
    "en": "<p>The site may include links to third-party sites (for example, social media, WhatsApp or NMLS). We do not control and are not responsible for their content or privacy practices.</p>",
    "pt": "<p>O site pode incluir links para sites de terceiros (por exemplo, redes sociais, WhatsApp ou NMLS). Não controlamos nem somos responsáveis pelo conteúdo ou pelas práticas de privacidade deles.</p>"}},
  {"h": {"es": "9. Limitación de responsabilidad", "en": "9. Limitation of liability", "pt": "9. Limitação de responsabilidade"},
   "b": {
    "es": "<p>El sitio se ofrece \"tal cual\". En la medida permitida por la ley, Tony Valdes Loans no será responsable por daños derivados del uso o la imposibilidad de usar el sitio, ni por decisiones tomadas únicamente con base en su contenido.</p>",
    "en": "<p>The site is provided \"as is.\" To the extent permitted by law, Tony Valdes Loans will not be liable for damages arising from the use of or inability to use the site, or for decisions made solely based on its content.</p>",
    "pt": "<p>O site é oferecido \"como está\". Na medida permitida pela lei, a Tony Valdes Loans não será responsável por danos decorrentes do uso ou da impossibilidade de usar o site, nem por decisões tomadas apenas com base em seu conteúdo.</p>"}},
  {"h": {"es": "10. Ley aplicable", "en": "10. Governing law", "pt": "10. Lei aplicável"},
   "b": {
    "es": "<p>Estos términos se rigen por las leyes del Estado de Georgia y las leyes federales aplicables de los Estados Unidos.</p>",
    "en": "<p>These terms are governed by the laws of the State of Georgia and applicable federal laws of the United States.</p>",
    "pt": "<p>Estes termos são regidos pelas leis do Estado da Geórgia e pelas leis federais aplicáveis dos Estados Unidos.</p>"}},
  {"h": {"es": "11. Igualdad de oportunidades", "en": "11. Equal opportunity", "pt": "11. Igualdade de oportunidades"},
   "b": {
    "es": "<p>Somos un prestamista que ofrece igualdad de oportunidades de vivienda (Equal Housing Opportunity). No discriminamos por raza, color, religión, origen nacional, sexo, estado civil, edad, discapacidad, situación familiar ni por recibir ingresos de asistencia pública.</p>",
    "en": "<p>We are an Equal Housing Opportunity lender. We do not discriminate on the basis of race, color, religion, national origin, sex, marital status, age, disability, familial status or receipt of public assistance income.</p>",
    "pt": "<p>Somos um credor que oferece igualdade de oportunidades de moradia (Equal Housing Opportunity). Não discriminamos por raça, cor, religião, origem nacional, sexo, estado civil, idade, deficiência, situação familiar nem por receber renda de assistência pública.</p>"}},
  {"h": {"es": "12. Cambios y contacto", "en": "12. Changes and contact", "pt": "12. Alterações e contato"}, "b": "CONTACT",
   "pre": {"es": "<p>Podemos actualizar estos términos en cualquier momento. La versión vigente estará siempre publicada en esta página.</p>",
           "en": "<p>We may update these terms at any time. The current version will always be posted on this page.</p>",
           "pt": "<p>Podemos atualizar estes termos a qualquer momento. A versão vigente estará sempre publicada nesta página.</p>"}},
 ]},
}

UI = {
 "back": {"es": "← Volver al inicio", "en": "← Back to home", "pt": "← Voltar ao início"},
 "other": {"privacidad": {"es": "Ver Términos y Condiciones", "en": "See Terms and Conditions", "pt": "Ver Termos e Condições"},
           "terminos": {"es": "Ver Política de Privacidad", "en": "See Privacy Policy", "pt": "Ver Política de Privacidade"}},
 "rights": {"es": "Todos los derechos reservados.", "en": "All rights reserved.", "pt": "Todos os direitos reservados."},
}
