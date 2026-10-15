  // ===== Núcleo de embudos: idiomas (ES / EN / PT), animaciones y utilidades =====
  var I18N=__I18N__;
  var ORIG={};
  document.querySelectorAll('[data-i18n]').forEach(function(el){ORIG[el.getAttribute('data-i18n')]=el.innerHTML});
  document.querySelectorAll('[data-i18n-alt]').forEach(function(el){ORIG['alt:'+el.getAttribute('data-i18n-alt')]=el.getAttribute('alt')});
  document.querySelectorAll('[data-i18n-aria]').forEach(function(el){ORIG['aria:'+el.getAttribute('data-i18n-aria')]=el.getAttribute('aria-label')});
  var LANG='es';
  function T(k){return (I18N[LANG]&&I18N[LANG][k])||I18N.es[k]||''}
  function pick(k,orig){return LANG==='es'?orig:((I18N[LANG]&&I18N[LANG][k])||orig)}
  function setLang(l){
    if(!I18N[l]) l='es'; LANG=l;
    document.querySelectorAll('[data-i18n]').forEach(function(el){var k=el.getAttribute('data-i18n');el.innerHTML=pick(k,ORIG[k])});
    document.querySelectorAll('[data-i18n-alt]').forEach(function(el){var k=el.getAttribute('data-i18n-alt');el.setAttribute('alt',pick(k,ORIG['alt:'+k]))});
    document.querySelectorAll('[data-i18n-aria]').forEach(function(el){var k=el.getAttribute('data-i18n-aria');el.setAttribute('aria-label',pick(k,ORIG['aria:'+k]))});
    var root=document.getElementById('tvl')||document.documentElement; root.setAttribute('lang',l);
    if(!document.getElementById('tvl')){document.title=T('_title');var md=document.querySelector('meta[name="description"]');if(md)md.setAttribute('content',T('_desc'))}
    var y=document.getElementById('year'); if(y) y.textContent=new Date().getFullYear();
    document.querySelectorAll('.lang-switch button').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-lang')===l?'true':'false')});
    document.querySelectorAll('.err').forEach(function(e){e.textContent=''});
    document.querySelectorAll('.field.invalid').forEach(function(f){f.classList.remove('invalid')});
    if(window.tvlRecalc) window.tvlRecalc();
    try{localStorage.setItem('tvl-lang',l)}catch(e){}
  }
  document.querySelectorAll('.lang-switch button').forEach(function(b){b.addEventListener('click',function(){setLang(b.getAttribute('data-lang'))})});
  var QS=new URLSearchParams(location.search);
  function startLang(){
    var s='es';
    try{var q=QS.get('lang');var saved=localStorage.getItem('tvl-lang');s=(q&&I18N[q])?q:(saved&&I18N[saved]?saved:'es')}catch(e){}
    setLang(s);
  }
  function money(v){return '$'+Math.round(v).toLocaleString('en-US')}
  function esc(s){return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  var y=document.getElementById('year'); if(y) y.textContent=new Date().getFullYear();
  var els=document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(entries){entries.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target)}})},{threshold:.12});
    els.forEach(function(el,i){el.style.transitionDelay=(i%4)*80+'ms';io.observe(el)});
  } else { els.forEach(function(el){el.classList.add('in')}) }
