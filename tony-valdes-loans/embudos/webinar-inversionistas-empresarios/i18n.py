# Embudo Masterclass Inversionistas y Empresarios · configuración y traducciones (es, en, pt)
import importlib.util as _u, os as _os

# ===== DATOS DEL WEBINAR: cambia aquí y regenera (afecta las 3 páginas) =====
EVENT = {
    'start': '2026-11-05T19:30:00-05:00',  # jueves 5 de noviembre, 7:30 p.m. hora de Atlanta / Miami (-05:00 en invierno, -04:00 en verano)
    'tz': 'America/New_York',
    'minutes': 75,
    'zoom': '',             # enlace de Zoom (vacío = "te llegó por correo y WhatsApp")
    'replay': '',           # repetición: YouTube, Vimeo o .mp4 (vacío = "muy pronto")
    'whatsapp_group': '',   # grupo de WhatsApp (vacío = WhatsApp de Tony)
}

WA_TEXT = 'Hola%20Tony%2C%20me%20interesa%20la%20masterclass%20para%20inversionistas%20y%20empresarios'

def L(es, en, pt): return {'es': es, 'en': en, 'pt': pt}

PAGES = [
    {'src': '1-registro.html', 'label': 'MASTERCLASS INVERSIONISTAS Y EMPRESARIOS · PASO 1 REGISTRO',
     'title': L('Masterclass Gratis: Inversionistas y Empresarios | Tony Valdes',
                'Free masterclass: Investors and Business Owners | Tony Valdes Loans',
                'Masterclass grátis: Investidores e Empresários | Tony Valdes Loans'),
     'desc': L('Clase gratis en vivo por Zoom con Tony Valdes: estado del mercado, oportunidades en bienes raíces y financiamiento inteligente. Jueves 5 de nov., 7:30 p.m.',
               'Free live class with Tony Valdes: current market conditions, real estate investment opportunities and smart financing strategies. Thursday, November 5, 7:30 p.m. (Atlanta / Miami).',
               'Aula grátis ao vivo com Tony Valdes: situação atual do mercado, oportunidades de investimento imobiliário e estratégias de financiamento inteligente. Quinta-feira, 5 de novembro, 19h30 (Atlanta / Miami).')},
    {'src': '2-confirmado.html', 'label': 'MASTERCLASS INVERSIONISTAS Y EMPRESARIOS · PASO 2 LUGAR RESERVADO',
     'title': L('¡Tu lugar está reservado! | Tony Valdes Loans', 'Your spot is reserved! | Tony Valdes Loans', 'Sua vaga está reservada! | Tony Valdes Loans'),
     'desc': L('Completa 3 pasos para no perderte la masterclass.', 'Complete 3 steps so you do not miss the masterclass.', 'Complete 3 passos para não perder a masterclass.')},
    {'src': '3-sala.html', 'label': 'MASTERCLASS INVERSIONISTAS Y EMPRESARIOS · PASO 3 SALA',
     'title': L('Sala de la masterclass | Tony Valdes Loans', 'Masterclass room | Tony Valdes Loans', 'Sala da masterclass | Tony Valdes Loans'),
     'desc': L('Entra a la masterclass en vivo o mira la repetición.', 'Join the live masterclass or watch the replay.', 'Entre na masterclass ao vivo ou assista à reprise.')},
]

_M = [
    ('_tz', '(hora de Atlanta / Miami)', '(Atlanta / Miami time)', '(horário de Atlanta / Miami)'),
    ('_ev_title', 'Masterclass Inversionistas y Empresarios · Tony Valdes', 'Masterclass for Investors and Business Owners · Tony Valdes', 'Masterclass Investidores e Empresários · Tony Valdes'),
    ('_ev_details', 'Clase gratis en vivo con Tony Valdes: cómo identificar oportunidades y financiarlas estratégicamente. Entra aquí:',
     'Free live class with Tony Valdes: how to spot opportunities and finance them strategically. Join here:',
     'Aula grátis ao vivo com Tony Valdes: como identificar oportunidades e financiá-las estrategicamente. Entre aqui:'),
    ('_k_title', '¡Tu lugar está reservado!', 'Your spot is reserved!', 'Sua vaga está reservada!'),
    ('_k_title_n', '¡{n}, tu lugar está reservado!', '{n}, your spot is reserved!', '{n}, sua vaga está reservada!'),
    ('_wa_avisos', 'Hola Tony, me inscribí a la masterclass para inversionistas y empresarios ({d}). Quiero recibir los avisos por aquí.',
     'Hi Tony, I signed up for the masterclass for investors and business owners ({d}). I would like to get the reminders here.',
     'Olá Tony, me inscrevi na masterclass para investidores e empresários ({d}). Quero receber os avisos por aqui.'),
    ('_share_w', 'Me inscribí a una masterclass gratis con Tony Valdes para inversionistas y empresarios: cómo identificar oportunidades y financiarlas ({d}). ¡Inscríbete conmigo!',
     'I signed up for a free masterclass with Tony Valdes for investors and business owners: how to spot opportunities and finance them ({d}). Sign up with me!',
     'Me inscrevi em uma masterclass grátis com Tony Valdes para investidores e empresários: como identificar oportunidades e financiá-las ({d}). Inscreva-se comigo!'),
    ('_live_nozoom', 'El enlace de Zoom te llegó por correo y WhatsApp. Si no lo encuentras, pídelo aquí y te lo enviamos al instante.',
     'The Zoom link was sent to your email and WhatsApp. If you cannot find it, ask here and we will send it right away.',
     'O link do Zoom foi enviado para seu e-mail e WhatsApp. Se não encontrar, peça aqui e enviamos na hora.'),
    ('_wa_link', 'Hola Tony, estoy listo para la masterclass de inversionistas y empresarios. ¿Me envías el enlace de Zoom?',
     'Hi Tony, I am ready for the investors and business owners masterclass. Can you send me the Zoom link?',
     'Olá Tony, estou pronto para a masterclass de investidores e empresários. Pode me enviar o link do Zoom?'),
    ('_wa_ask', 'Hola Tony, vi la masterclass para inversionistas y empresarios y quiero analizar mi caso:',
     'Hi Tony, I watched the masterclass for investors and business owners and I would like to review my case:',
     'Olá Tony, assisti à masterclass para investidores e empresários e quero analisar meu caso:'),
]
META = {'es': {k: e for k, e, n, p in _M}, 'en': {k: n for k, e, n, p in _M}, 'pt': {k: p for k, e, n, p in _M}}

def _load(name):
    s = _u.spec_from_file_location('_' + name.replace('-', '_'), _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', name, 'i18n.py'))
    m = _u.module_from_spec(s); s.loader.exec_module(m); return m

_web = _load('webinar-primeros-compradores')
_emb = _load('inversionistas-empresarios-embudo')
SAME = list(dict.fromkeys(list(_web.SAME) + list(_emb.SAME)))
T = list(_emb.T) + list(_web.T)[len(_load('primeros-compradores').T):] + [
('Inversionistas y <span class="gold-text">Empresarios</span><small>Cómo identificar oportunidades y financiarlas estratégicamente</small>','Investors and <span class="gold-text">Business Owners</span><small>How to spot opportunities and finance them strategically</small>','Investidores e <span class="gold-text">Empresários</span><small>Como identificar oportunidades e financiá-las estrategicamente</small>'),
('Una clase en vivo con Tony Valdes sobre el estado actual del mercado, dónde están las oportunidades en bienes raíces y cómo financiarlas de forma inteligente, aunque tus ingresos no sean "tradicionales".','A live class with Tony Valdes on current market conditions, where the real estate opportunities are and how to finance them smartly, even if your income isn\'t "traditional".','Uma aula ao vivo com Tony Valdes sobre a situação atual do mercado, onde estão as oportunidades no mercado imobiliário e como financiá-las de forma inteligente, mesmo que sua renda não seja "tradicional".'),
("Reserva tu lugar ahora","Save your spot now","Reserve sua vaga agora"),
("🎙️ En vivo con Tony","🎙️ Live with Tony","🎙️ Ao vivo com Tony"),
("En esta masterclass vas a aprender","In this masterclass you'll learn","Nesta masterclass você vai aprender"),
("Lo que necesitas saber antes de tu próximo movimiento","What you need to know before your next move","O que você precisa saber antes do seu próximo movimento"),
("Estado actual del mercado","Current state of the market","Situação atual do mercado"),
("Qué está pasando hoy y cómo leerlo como inversionista.","What's happening today and how to read it as an investor.","O que está acontecendo hoje e como interpretar como investidor."),
("Oportunidades de inversión en bienes raíces","Real estate investment opportunities","Oportunidades de investimento imobiliário"),
("Fix &amp; Flip, rentas, multifamily y construcción: dónde están los números.","Fix &amp; Flip, rentals, multifamily and construction: where the numbers are.","Fix &amp; Flip, aluguéis, multifamily e construção: onde estão os números."),
("Estrategias + financiamiento inteligente","Strategies + smart financing","Estratégias + financiamento inteligente"),
("DSCR, Bank Statement, equity y más: cómo estructurar cada deal.","DSCR, Bank Statement, equity and more: how to structure every deal.","DSCR, Bank Statement, equity e mais: como estruturar cada negócio."),
("Preguntas y respuestas en vivo","Live Q&amp;A","Perguntas e respostas ao vivo"),
("Trae tu caso: Tony responde al final de la clase.","Bring your case: Tony answers at the end of the class.","Traga seu caso: Tony responde no final da aula."),
("¿Para quién es?","Who is it for?","Para quem é?"),
("Para quien quiere que su dinero trabaje","For anyone who wants their money to work","Para quem quer que seu dinheiro trabalhe"),
("Ya inviertes y quieres escalar tu portafolio","You already invest and want to scale your portfolio","Você já investe e quer escalar seu portfólio"),
("Quieres hacer tu primer Fix &amp; Flip o tu primera renta","You want to do your first Fix &amp; Flip or first rental","Você quer fazer seu primeiro Fix &amp; Flip ou seu primeiro aluguel"),
("Buscas financiamiento que califique con la renta","You're looking for financing that qualifies with the rent","Você busca financiamento que se qualifique com o aluguel"),
("Tienes un negocio y quieres invertir sus ganancias","You own a business and want to invest its profits","Você tem um negócio e quer investir os lucros"),
("Tus taxes muestran poco, pero tu negocio sí genera","Your tax returns show little, but your business does make money","Sua declaração mostra pouco, mas seu negócio gera dinheiro"),
("Quieres comprar el local de tu negocio o liberar capital","You want to buy your business's location or free up capital","Você quer comprar o ponto do seu negócio ou liberar capital"),
("Fui Vicepresidente de Banca Comercial y trabajé con más de 150 clientes de alto perfil. En esta clase te comparto cómo piensan los grandes inversionistas para encontrar y financiar sus oportunidades.","I was a Commercial Banking Vice President and worked with more than 150 high-profile clients. In this class I share how big investors think when they find and finance their opportunities.","Fui Vice-Presidente de Banco Comercial e trabalhei com mais de 150 clientes de alto perfil. Nesta aula compartilho como os grandes investidores pensam para encontrar e financiar suas oportunidades."),
("Tony Valdes<span>Mortgage Loan Officer · NMLS #1593970 · 25+ años en banca y finanzas</span>","Tony Valdes<span>Mortgage Loan Officer · NMLS #1593970 · 25+ years in banking and finance</span>","Tony Valdes<span>Mortgage Loan Officer · NMLS #1593970 · 25+ anos em bancos e finanças</span>"),
("¿Vas a dejar pasar esta masterclass?","Are you going to miss this masterclass?","Você vai deixar passar esta masterclass?"),
("Una hora con Tony puede cambiar la forma en que inviertes y haces crecer tu negocio.","One hour with Tony can change the way you invest and grow your business.","Uma hora com o Tony pode mudar a forma como você investe e faz seu negócio crescer."),
("Contenido educativo. No constituye asesoría fiscal o financiera.","Educational content. It does not constitute tax or financial advice.","Conteúdo educativo. Não constitui assessoria fiscal ou financeira."),
("Tony Valdes, instructor de la masterclass","Tony Valdes, masterclass instructor","Tony Valdes, instrutor da masterclass"),
("Paso 1","Step 1","Passo 1"),("Paso 2","Step 2","Passo 2"),("Paso 3","Step 3","Passo 3"),
("Haz tu diagnóstico de 60 segundos","Take your 60-second assessment","Faça seu diagnóstico de 60 segundos"),
("Descubre qué financiamiento te conviene y llega a la clase sabiendo qué preguntar.","Find out which financing fits you and come to class knowing what to ask.","Descubra qual financiamento combina com você e chegue à aula sabendo o que perguntar."),
("¿Tienes un socio o un colega inversionista?","Have a partner or fellow investor?","Tem um sócio ou colega investidor?"),
("Invita a tu socio, a otro empresario o a un amigo que también quiera invertir con estrategia.","Invite your partner, another business owner or a friend who also wants to invest strategically.","Convide seu sócio, outro empresário ou um amigo que também queira investir com estratégia."),
("Prepara tus preguntas y, si tienes un deal en mente, tráelo. En la masterclass respondo en vivo y al final te digo cuál es tu siguiente paso. ¡Sí es posible!","Get your questions ready and, if you have a deal in mind, bring it. I answer live in the masterclass and at the end I'll tell you your next step. Yes, it's possible!","Prepare suas perguntas e, se tiver um negócio em mente, traga. Na masterclass respondo ao vivo e no final digo qual é o seu próximo passo. Sim, é possível!"),
('Inversionistas y <span class="gold-text">Empresarios</span>: cómo identificar oportunidades y financiarlas estratégicamente','Investors and <span class="gold-text">Business Owners</span>: how to spot opportunities and finance them strategically','Investidores e <span class="gold-text">Empresários</span>: como identificar oportunidades e financiá-las estrategicamente'),
("Convierte lo que aprendiste en tu próximo deal","Turn what you learned into your next deal","Transforme o que você aprendeu no seu próximo negócio"),
("Haz tu diagnóstico de financiamiento","Take your financing assessment","Faça seu diagnóstico de financiamento"),
("En 60 segundos descubre qué programas podrían encajar con tu deal o tu negocio.","In 60 seconds, find out which programs could fit your deal or business.","Em 60 segundos descubra quais programas podem combinar com seu investimento ou seu negócio."),
("15 minutos con Tony para revisar los números de tu deal o la situación de tu negocio.","15 minutes with Tony to review your deal's numbers or your business situation.","15 minutos com o Tony para revisar os números do seu investimento ou a situação do seu negócio."),
("Contenido educativo. No constituye asesoría fiscal o financiera, ni es una oferta de préstamo o un compromiso de prestar.","Educational content. It does not constitute tax or financial advice, nor is it a loan offer or a commitment to lend.","Conteúdo educativo. Não constitui assessoria fiscal ou financeira, nem é uma oferta de empréstimo ou um compromisso de emprestar."),
]
