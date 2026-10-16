  // ===== Evento: una sola fecha para las 3 páginas (se cambia en i18n.py → EVENT) =====
  var EV=__EVENT__;
  var START=new Date(EV.start), END=new Date(START.getTime()+(EV.minutes||60)*60000);
  var LOC={es:'es-US',en:'en-US',pt:'pt-BR'};
  var URLS={registro:'/primeros-compradores-webinar',confirmado:'/primeros-compradores-webinar-confirmado',sala:'/primeros-compradores-webinar-sala',test:'/primeros-compradores'};
  if(location.protocol==='file:'){URLS={registro:'1-registro.html',confirmado:'2-confirmado.html',sala:'3-sala.html',test:'../../primeros-compradores/revisar/1-test.html'}}
  function abs(u){return location.protocol==='file:'?u:location.origin+u}
  function cap(s){return s.charAt(0).toUpperCase()+s.slice(1)}
  function evDate(){try{return cap(new Intl.DateTimeFormat(LOC[LANG],{weekday:'long',day:'numeric',month:'long',timeZone:EV.tz}).format(START))}catch(e){return START.toDateString()}}
  function evTime(){try{return new Intl.DateTimeFormat(LOC[LANG],{hour:'numeric',minute:'2-digit',timeZone:EV.tz}).format(START)+' '+T('_tz')}catch(e){return ''}}
  function fillEvent(){
    document.querySelectorAll('[data-ev="date"]').forEach(function(e){e.textContent=evDate()});
    document.querySelectorAll('[data-ev="time"]').forEach(function(e){e.textContent=evTime()});
  }
  // Estado del evento: antes / en vivo (abre 10 min antes, cierra 30 min después) / repetición
  function evMode(){
    var f=QS.get('modo'); if(f==='antes'||f==='vivo'||f==='repeticion') return f;
    var now=Date.now();
    if(now<START.getTime()-10*60000) return 'antes';
    if(now<END.getTime()+30*60000) return 'vivo';
    return 'repeticion';
  }
  function pad(n){return (n<10?'0':'')+n}
  function startCountdowns(){
    var cds=document.querySelectorAll('.cd');
    if(!cds.length) return;
    function tick(){
      var ms=Math.max(0,START.getTime()-Date.now()), s=Math.floor(ms/1000);
      var v={d:Math.floor(s/86400),h:Math.floor(s%86400/3600),m:Math.floor(s%3600/60),s:s%60};
      cds.forEach(function(cd){
        for(var k in v){var el=cd.querySelector('[data-cd="'+k+'"]'); if(el) el.textContent=pad(v[k])}
        cd.classList.toggle('done',ms===0);
      });
    }
    tick(); setInterval(tick,1000);
  }
  // Agregar al calendario
  function gfmt(d){return d.toISOString().replace(/[-:]/g,'').replace(/\.\d{3}/,'')}
  function calDetails(){return T('_ev_details')+' '+abs(URLS.sala)}
  function gcalUrl(){
    return 'https://calendar.google.com/calendar/render?action=TEMPLATE&text='+encodeURIComponent(T('_ev_title'))+
      '&dates='+gfmt(START)+'/'+gfmt(END)+'&details='+encodeURIComponent(calDetails())+'&location='+encodeURIComponent(abs(URLS.sala));
  }
  function downloadIcs(){
    var ics=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Tony Valdes Loans//Webinar//ES','BEGIN:VEVENT',
      'UID:webinar-'+gfmt(START)+'@tonyvaldesloans.com','DTSTAMP:'+gfmt(new Date()),'DTSTART:'+gfmt(START),'DTEND:'+gfmt(END),
      'SUMMARY:'+T('_ev_title'),'DESCRIPTION:'+calDetails(),'URL:'+abs(URLS.sala),
      'BEGIN:VALARM','TRIGGER:-PT30M','ACTION:DISPLAY','DESCRIPTION:'+T('_ev_title'),'END:VALARM','END:VEVENT','END:VCALENDAR'].join('\r\n');
    var a=document.createElement('a');
    a.href=URL.createObjectURL(new Blob([ics],{type:'text/calendar'}));
    a.download='webinar-tony-valdes.ics'; document.body.appendChild(a); a.click(); a.remove();
  }
  function bindCalendar(){
    document.querySelectorAll('[data-cal="google"]').forEach(function(a){a.href=gcalUrl()});
    document.querySelectorAll('[data-cal="ics"]').forEach(function(b){b.onclick=function(e){e.preventDefault();downloadIcs()}});
  }
