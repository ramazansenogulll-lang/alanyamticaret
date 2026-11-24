// Alanyam Ticaret — menü ve WhatsApp sipariş formu
(function () {
  var b = document.querySelector('.burger'), n = document.querySelector('.nav');
  if (b && n) b.addEventListener('click', function () {
    var o = n.classList.toggle('open'); b.setAttribute('aria-expanded', o ? 'true' : 'false');
  });
  document.querySelectorAll('.nav .sub>button').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var s = btn.parentNode, o = s.classList.toggle('on'); btn.setAttribute('aria-expanded', o ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (e) {
    document.querySelectorAll('.nav .sub.on').forEach(function (s) { if (!s.contains(e.target)) s.classList.remove('on'); });
  });

  // Sipariş formu: mesaj her dilde Türkçe hazırlanır (bayi Türkçe okur).
  var f = document.getElementById('siparis-form');
  if (!f) return;
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var v = function (k) { var el = f.elements[k]; return el ? String(el.value || '').trim() : ''; };
    var urun = v('urun'), adet = v('adet') || '1', ad = v('ad'), adres = v('adres'), not_ = v('not');
    if (!adres) { f.elements['adres'].focus(); f.elements['adres'].setAttribute('aria-invalid', 'true'); return; }
    var lines = ['Merhaba Alanyam Ticaret, sipariş vermek istiyorum.', '', 'Ürün: ' + urun, 'Adet: ' + adet];
    if (ad) lines.push('İsim: ' + ad);
    lines.push('Adres: ' + adres);
    if (not_) lines.push('Not: ' + not_);
    var dil = document.documentElement.lang;
    if (dil === 'ru') lines.push('', '(Müşteri Rusça konuşuyor / Клиент говорит по-русски)');
    if (dil === 'en') lines.push('', '(Müşteri İngilizce konuşuyor / Customer speaks English)');
    var url = 'https://wa.me/' + f.getAttribute('data-wa') + '?text=' + encodeURIComponent(lines.join('\n'));
    if (window.dataLayer) window.dataLayer.push({ event: 'whatsapp_siparis', urun: urun });
    window.open(url, '_blank', 'noopener');
  });
})();
