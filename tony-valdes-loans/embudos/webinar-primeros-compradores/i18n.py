# Embudo Webinar Primeros Compradores · configuración y traducciones (es, en, pt)

# ===== DATOS DEL WEBINAR: cambia aquí y regenera (afecta las 3 páginas) =====
EVENT = {
    'start': '2026-11-05T19:00:00-05:00',  # fecha y hora de inicio con zona horaria (-05:00 = hora del Este en invierno)
    'tz': 'America/New_York',              # zona horaria en la que se muestra la hora
    'minutes': 60,                          # duración
    'zoom': '',                             # enlace de Zoom (vacío = "te llegó por correo y WhatsApp")
    'replay': '',                           # enlace de la repetición: YouTube, Vimeo o .mp4 (vacío = "muy pronto")
    'whatsapp_group': '',                   # enlace del grupo de WhatsApp (vacío = WhatsApp de Tony)
}

WA_TEXT = 'Hola%20Tony%2C%20me%20interesa%20la%20masterclass%20de%20primeros%20compradores'

def L(es, en, pt): return {'es': es, 'en': en, 'pt': pt}

PAGES = [
    {'src': '1-registro.html', 'label': 'WEBINAR PRIMEROS COMPRADORES · PASO 1 REGISTRO',
     'title': L('Masterclass gratis: tu primera casa en USA | Tony Valdes Loans',
                'Free masterclass: your first home in the USA | Tony Valdes Loans',
                'Masterclass grátis: sua primeira casa nos EUA | Tony Valdes Loans'),
     'desc': L('Clase gratis en vivo con Tony Valdes: cuánto necesitas de verdad para comprar, programas de ayuda para la entrada y opciones si eres independiente o tu crédito no es perfecto. NMLS #1593970.',
               'Free live class with Tony Valdes: how much you really need to buy, down payment assistance programs and options if you are self-employed or your credit is not perfect. NMLS #1593970.',
               'Aula grátis ao vivo com Tony Valdes: quanto você realmente precisa para comprar, programas de ajuda para a entrada e opções se você é autônomo ou seu crédito não é perfeito. NMLS #1593970.')},
    {'src': '2-confirmado.html', 'label': 'WEBINAR PRIMEROS COMPRADORES · PASO 2 LUGAR RESERVADO',
     'title': L('¡Tu lugar está reservado! | Tony Valdes Loans', 'Your spot is reserved! | Tony Valdes Loans', 'Sua vaga está reservada! | Tony Valdes Loans'),
     'desc': L('Completa 3 pasos para no perderte la masterclass.', 'Complete 3 steps so you do not miss the masterclass.', 'Complete 3 passos para não perder a masterclass.')},
    {'src': '3-sala.html', 'label': 'WEBINAR PRIMEROS COMPRADORES · PASO 3 SALA',
     'title': L('Sala de la masterclass | Tony Valdes Loans', 'Masterclass room | Tony Valdes Loans', 'Sala da masterclass | Tony Valdes Loans'),
     'desc': L('Entra a la masterclass en vivo o mira la repetición.', 'Join the live masterclass or watch the replay.', 'Entre na masterclass ao vivo ou assista à reprise.')},
]

_M = [
    ('_tz', '(hora del Este)', '(Eastern Time)', '(horário do Leste dos EUA)'),
    ('_ev_title', 'Masterclass: Tu primera casa en USA · Tony Valdes', 'Masterclass: Your first home in the USA · Tony Valdes', 'Masterclass: Sua primeira casa nos EUA · Tony Valdes'),
    ('_ev_details', 'Clase gratis en vivo con Tony Valdes. Entra aquí:', 'Free live class with Tony Valdes. Join here:', 'Aula grátis ao vivo com Tony Valdes. Entre aqui:'),
    ('_k_title', '¡Tu lugar está reservado!', 'Your spot is reserved!', 'Sua vaga está reservada!'),
    ('_k_title_n', '¡{n}, tu lugar está reservado!', '{n}, your spot is reserved!', '{n}, sua vaga está reservada!'),
    ('_wa_avisos', 'Hola Tony, me inscribí a la masterclass de primeros compradores ({d}). Quiero recibir los avisos por aquí.',
     'Hi Tony, I signed up for the first-time buyer masterclass ({d}). I would like to get the reminders here.',
     'Olá Tony, me inscrevi na masterclass de primeiros compradores ({d}). Quero receber os avisos por aqui.'),
    ('_share_w', 'Me inscribí a una clase gratis con Tony Valdes sobre cómo comprar tu primera casa en USA ({d}). ¡Inscríbete conmigo!',
     'I signed up for a free class with Tony Valdes on how to buy your first home in the USA ({d}). Sign up with me!',
     'Me inscrevi em uma aula grátis com Tony Valdes sobre como comprar sua primeira casa nos EUA ({d}). Inscreva-se comigo!'),
    ('_live_nozoom', 'El enlace de Zoom te llegó por correo y WhatsApp. Si no lo encuentras, pídelo aquí y te lo enviamos al instante.',
     'The Zoom link was sent to your email and WhatsApp. If you cannot find it, ask here and we will send it right away.',
     'O link do Zoom foi enviado para seu e-mail e WhatsApp. Se não encontrar, peça aqui e enviamos na hora.'),
    ('_wa_link', 'Hola Tony, estoy listo para la masterclass. ¿Me envías el enlace de Zoom?', 'Hi Tony, I am ready for the masterclass. Can you send me the Zoom link?', 'Olá Tony, estou pronto para a masterclass. Pode me enviar o link do Zoom?'),
    ('_wa_ask', 'Hola Tony, vi la masterclass de primeros compradores y tengo una pregunta:', 'Hi Tony, I watched the first-time buyer masterclass and I have a question:', 'Olá Tony, assisti à masterclass de primeiros compradores e tenho uma pergunta:'),
]
META = {'es': {k: e for k, e, n, p in _M}, 'en': {k: n for k, e, n, p in _M}, 'pt': {k: p for k, e, n, p in _M}}

SAME = ['Tony Valdes Loans', 'Tony Valdes', 'Facebook', 'YouTube', 'Instagram @tonyvaldesloans', 'Idioma / Language / Idioma',
        'Tony Valdes, Loan Officer', 'Google Calendar', 'Apple / Outlook']

T = [
("<i></i>Masterclass gratis · En vivo por Zoom","<i></i>Free masterclass · Live on Zoom","<i></i>Masterclass grátis · Ao vivo pelo Zoom"),
('Tu primera casa en USA: <span class="gold-text">cómo comprar aunque creas que no calificas</span>','Your first home in the USA: <span class="gold-text">how to buy even if you think you don\'t qualify</span>','Sua primeira casa nos EUA: <span class="gold-text">como comprar mesmo achando que não se qualifica</span>'),
("En una clase en vivo, Tony te explica paso a paso cómo pasar de pagar renta a tener tus llaves: cuánto necesitas de verdad, los programas de ayuda y qué hacer si eres independiente o tu crédito no es perfecto.","In a live class, Tony explains step by step how to go from paying rent to holding your keys: how much you really need, assistance programs and what to do if you're self-employed or your credit isn't perfect.","Em uma aula ao vivo, Tony explica passo a passo como passar de pagar aluguel a ter suas chaves: quanto você realmente precisa, os programas de ajuda e o que fazer se você é autônomo ou seu crédito não é perfeito."),
("días","days","dias"),("horas","hours","horas"),("min","min","min"),("seg","sec","seg"),
("Reservar mi lugar gratis","Save my free spot","Reservar minha vaga grátis"),
("100% gratis · En español","100% free · In Spanish","100% grátis · Em espanhol"),
("<i>🎙️</i>En vivo con Tony","<i>🎙️</i>Live with Tony","<i>🎙️</i>Ao vivo com Tony"),
("<i>💬</i>Preguntas y respuestas","<i>💬</i>Q&amp;A","<i>💬</i>Perguntas e respostas"),
("En esta clase vas a aprender","In this class you'll learn","Nesta aula você vai aprender"),
("Lo que nadie te explica antes de comprar tu primera casa","What nobody explains before you buy your first home","O que ninguém te explica antes de comprar sua primeira casa"),
("Cuánto necesitas realmente para comprar","How much you really need to buy","Quanto você realmente precisa para comprar"),
("Y por qué muchas veces es menos de lo que imaginas.","And why it's often less than you imagine.","E por que muitas vezes é menos do que você imagina."),
("Los programas de ayuda para la entrada","Down payment assistance programs","Os programas de ajuda para a entrada"),
("Qué son, quién califica y cómo aprovecharlos.","What they are, who qualifies and how to use them.","O que são, quem se qualifica e como aproveitá-los."),
("Cómo comprar si eres independiente o tu crédito no es perfecto","How to buy if you're self-employed or your credit isn't perfect","Como comprar se você é autônomo ou seu crédito não é perfeito"),
("Opciones reales para trabajadores 1099, dueños de negocio y créditos en construcción.","Real options for 1099 workers, business owners and credit still being built.","Opções reais para trabalhadores 1099, donos de negócio e créditos em construção."),
("Los 6 pasos desde la preaprobación hasta las llaves","The 6 steps from pre-approval to keys","Os 6 passos da pré-aprovação até as chaves"),
("Para que sepas qué esperar y no te tomen por sorpresa.","So you know what to expect and nothing catches you off guard.","Para você saber o que esperar e não ser pego de surpresa."),
("Reserva tu lugar gratis","Save your free spot","Reserve sua vaga grátis"),
("Teléfono (WhatsApp)","Phone (WhatsApp)","Telefone (WhatsApp)"),
('¿Qué te gustaría preguntarle a Tony? <span class="opt-lbl">(opcional)</span>','What would you like to ask Tony? <span class="opt-lbl">(optional)</span>','O que você gostaria de perguntar ao Tony? <span class="opt-lbl">(opcional)</span>'),
("Reservar mi lugar","Save my spot","Reservar minha vaga"),
("Te enviaremos el enlace de la clase por correo y WhatsApp.","We'll send you the class link by email and WhatsApp.","Enviaremos o link da aula por e-mail e WhatsApp."),
("¿Esta clase es para ti?","Is this class for you?","Esta aula é para você?"),
("Sí, si te identificas con alguna de estas","Yes, if any of these sound like you","Sim, se você se identifica com alguma destas"),
("Pagas renta y quieres que ese dinero sea para tu propia casa","You pay rent and want that money to go toward your own home","Você paga aluguel e quer que esse dinheiro vá para a sua própria casa"),
("Trabajas por tu cuenta o con 1099 y no sabes si calificas","You're self-employed or a 1099 worker and don't know if you qualify","Você trabalha por conta própria ou com 1099 e não sabe se se qualifica"),
("Crees que necesitas mucho dinero ahorrado para comprar","You think you need a lot of savings to buy","Você acha que precisa de muito dinheiro guardado para comprar"),
("Tu crédito no es perfecto y quieres un plan para mejorarlo","Your credit isn't perfect and you want a plan to improve it","Seu crédito não é perfeito e você quer um plano para melhorá-lo"),
("¡Día de llaves!","Keys day!","Dia das chaves!"),
("Tu instructor","Your instructor","Seu instrutor"),
("<i></i>En vivo por Zoom","<i></i>Live on Zoom","<i></i>Ao vivo pelo Zoom"),
("Tu primera casa empieza con la información correcta","Your first home starts with the right information","Sua primeira casa começa com a informação certa"),
("Una hora con Tony puede ahorrarte meses de dudas y miles de dólares en errores.","One hour with Tony can save you months of doubts and thousands of dollars in mistakes.","Uma hora com o Tony pode poupar meses de dúvidas e milhares de dólares em erros."),
("Quiero mi lugar gratis","I want my free spot","Quero minha vaga grátis"),
("Tony Valdes, tu instructor en la masterclass","Tony Valdes, your masterclass instructor","Tony Valdes, seu instrutor na masterclass"),
("Cuenta regresiva","Countdown","Contagem regressiva"),
("¡Tu lugar está reservado!","Your spot is reserved!","Sua vaga está reservada!"),
("Te enviamos la confirmación por correo y WhatsApp. Completa estos 3 pasos para no perderte la clase y sacarle el máximo provecho.","We sent your confirmation by email and WhatsApp. Complete these 3 steps so you don't miss the class and get the most out of it.","Enviamos a confirmação por e-mail e WhatsApp. Complete estes 3 passos para não perder a aula e aproveitá-la ao máximo."),
("No te pierdas la clase","Don't miss the class","Não perca a aula"),
("3 pasos para llegar listo","3 steps to show up ready","3 passos para chegar pronto"),
("Agrégalo a tu calendario","Add it to your calendar","Adicione ao seu calendário"),
("Así te llega un recordatorio y el enlace de la sala queda guardado.","You'll get a reminder and the room link will be saved.","Assim você recebe um lembrete e o link da sala fica salvo."),
("Activa los avisos por WhatsApp","Turn on WhatsApp reminders","Ative os avisos pelo WhatsApp"),
("Te mandamos el enlace de Zoom y un recordatorio justo antes de empezar.","We'll send you the Zoom link and a reminder right before we start.","Enviamos o link do Zoom e um lembrete pouco antes de começar."),
("Activar avisos","Turn on reminders","Ativar avisos"),
("Haz el test de 60 segundos","Take the 60-second quiz","Faça o teste de 60 segundos"),
("Descubre qué tan cerca estás de tu primera casa y llega a la clase sabiendo qué preguntar.","Find out how close you are to your first home and come to class knowing what to ask.","Descubra quão perto você está da sua primeira casa e chegue à aula sabendo o que perguntar."),
("¿Vas a comprar con alguien más?","Buying with someone else?","Vai comprar com mais alguém?"),
("Invita a tu pareja, a un familiar o a un amigo que también quiera dejar de pagar renta.","Invite your partner, a relative or a friend who also wants to stop paying rent.","Convide seu parceiro, um familiar ou um amigo que também queira parar de pagar aluguel."),
("Nos vemos en la clase","See you in class","Nos vemos na aula"),
("Prepara tus preguntas. En la masterclass las respondo en vivo, y al final te digo exactamente cuál es tu siguiente paso. ¡Sí es posible!","Get your questions ready. I'll answer them live in the masterclass, and at the end I'll tell you exactly what your next step is. Yes, it's possible!","Prepare suas perguntas. Na masterclass eu respondo ao vivo e, no final, digo exatamente qual é o seu próximo passo. Sim, é possível!"),
("Tony Valdes te espera en la masterclass","Tony Valdes is waiting for you at the masterclass","Tony Valdes espera você na masterclass"),
("<i></i>Masterclass gratis · Próximamente","<i></i>Free masterclass · Coming soon","<i></i>Masterclass grátis · Em breve"),
("La sala se abre 10 minutos antes de empezar. Guarda esta página: aquí mismo vas a encontrar el botón para entrar.","The room opens 10 minutes before we start. Save this page: the button to join will appear right here.","A sala abre 10 minutos antes de começar. Salve esta página: o botão para entrar vai aparecer aqui mesmo."),
("Agregar a Google Calendar","Add to Google Calendar","Adicionar ao Google Calendar"),
("<i></i>¡Estamos en vivo!","<i></i>We're live!","<i></i>Estamos ao vivo!"),
("La masterclass está empezando","The masterclass is starting","A masterclass está começando"),
("Entra ahora a la sala de Zoom. Ten a mano papel y tus preguntas: Tony las responde en vivo.","Join the Zoom room now. Have paper and your questions ready: Tony answers them live.","Entre agora na sala do Zoom. Tenha papel e suas perguntas à mão: Tony responde ao vivo."),
("Entrar al Zoom ahora","Join Zoom now","Entrar no Zoom agora"),
("¿No tienes el enlace? Pídelo aquí","Don't have the link? Ask here","Não tem o link? Peça aqui"),
("<i></i>Repetición disponible","<i></i>Replay available","<i></i>Reprise disponível"),
("Mira la masterclass completa","Watch the full masterclass","Assista à masterclass completa"),
("¿Te la perdiste o quieres verla otra vez? Aquí está la grabación. Al final, da tu siguiente paso.","Missed it or want to watch it again? Here's the recording. At the end, take your next step.","Perdeu ou quer assistir de novo? Aqui está a gravação. No final, dê o seu próximo passo."),
("La repetición estará disponible muy pronto","The replay will be available very soon","A reprise estará disponível muito em breve"),
("Te avisamos por WhatsApp y correo en cuanto esté lista.","We'll let you know by WhatsApp and email as soon as it's ready.","Avisamos pelo WhatsApp e e-mail assim que estiver pronta."),
("Después de la clase","After the class","Depois da aula"),
("Tu siguiente paso hacia tus llaves","Your next step toward your keys","Seu próximo passo rumo às suas chaves"),
("Descubre qué tan cerca estás de tu primera casa y recibe tu plan personalizado.","Find out how close you are to your first home and get your personalized plan.","Descubra quão perto você está da sua primeira casa e receba seu plano personalizado."),
("Agenda tu revisión gratis","Book your free review","Agende sua revisão grátis"),
("15 minutos con Tony para revisar tu caso y saber para qué programas podrías calificar.","15 minutes with Tony to review your case and find out which programs you could qualify for.","15 minutos com o Tony para revisar seu caso e saber para quais programas você pode se qualificar."),
("Escríbele a Tony","Message Tony","Escreva para o Tony"),
("¿Te quedó una duda de la clase? Escríbele por WhatsApp y te responde personalmente.","Still have a question from the class? Message him on WhatsApp and he'll answer personally.","Ficou alguma dúvida da aula? Escreva pelo WhatsApp e ele responde pessoalmente."),
("Escribir por WhatsApp","Message on WhatsApp","Escrever pelo WhatsApp"),
("La masterclass es educativa. No es una oferta de préstamo ni un compromiso de prestar.","The masterclass is educational. It is not a loan offer or a commitment to lend.","A masterclass é educativa. Não é uma oferta de empréstimo nem um compromisso de emprestar."),
]

# Reutiliza las traducciones del embudo Primeros Compradores (consentimiento, pie, fotos, cita de Tony…)
import importlib.util as _u, os as _os
_s = _u.spec_from_file_location('_pc', _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'primeros-compradores', 'i18n.py'))
_pc = _u.module_from_spec(_s); _s.loader.exec_module(_pc)
T = list(_pc.T) + T
