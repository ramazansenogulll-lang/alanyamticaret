# -*- coding: utf-8 -*-
"""Alanyam Ticaret statik site derleyici.  Çalıştır:  python _tools/build.py
Çıktı proje köküne yazılır (klasör/index.html => temiz URL)."""
import html
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(__file__))
import art  # noqa: E402
from content import (BRAND, BRAND_COLORS, BRAND_NAME, DEFAULT_PRODUCT, GAS, KEYS, LANGS, NAME, P, PRODUCTS,  # noqa: E402
                     REDIRECTS, REVIEWS, SITE, SLUG, SODAS, TEL_FIX, TEL_GSM, TEL_WA, UI, WA_NUM, WATERS, intl)
from articles import ARTICLES, DATE  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
VER = "20261124c"
I = art.ICONS
e = html.escape
OUT = []  # sitemap kayıtları: (url, alternates|None)


def strip(s):
    import re
    return re.sub(r'<[^>]+>', '', s)


def tel(n):
    return 'tel:' + intl(n)


def wa_link(lang, text_tr):
    from urllib.parse import quote
    return f'https://wa.me/{WA_NUM}?text=' + quote(text_tr)


WA_HELLO = 'Merhaba Alanyam Ticaret, sipariş vermek istiyorum.'

# ---------------- fotoğraflar (hero hariç; _tools/gorseller.py üretir) ----------------
PHOTOS = {
    'alanyam-ticaret-ipragaz-tup-su-bayii-alanya': ((1086, 1448), {
        'tr': 'Alanyam Ticaret İpragaz tüp ve su bayii dükkânı, Alanya',
        'en': 'Alanyam Ticaret İpragaz gas and water shop in Alanya',
        'ru': 'Магазин газа İpragaz и воды Alanyam Ticaret в Аланье'}),
    'ipragaz-alanya-tup-bayi-vitrin': ((1222, 1287), {
        'tr': 'İpragaz Alanya tüp bayi vitrini ve sipariş telefonları',
        'en': 'İpragaz dealer shop window with order phone numbers, Alanya',
        'ru': 'Витрина дилера İpragaz с телефонами для заказа, Аланья'}),
    'alanya-su-bayii-aysu-madran-hayat-damacana': ((1268, 1240), {
        'tr': 'Aysu, Madran ve Hayat damacana ve şişe sular, Alanya su bayii',
        'en': 'Aysu, Madran and Hayat water jugs and bottles at the Alanya water shop',
        'ru': 'Бутыли и бутылки воды Aysu, Madran и Hayat в магазине в Аланье'}),
    'alanya-damacana-su-bayii-ic-mekan': ((1222, 1287), {
        'tr': 'Alanya damacana su bayii iç mekânı, raflarda 19 litre damacanalar',
        'en': 'Inside the Alanya water shop: 19-litre jugs on the shelves',
        'ru': 'Магазин воды в Аланье: бутыли 19 л на полках'}),
    'alanya-tup-ve-su-siparisi-mutfak': ((1448, 1086), {
        'tr': 'Alanya’da evinde damacana su ve tüp kullanan gülümseyen kadın',
        'en': 'Smiling woman in an Alanya kitchen with a water jug dispenser and a gas cylinder',
        'ru': 'Улыбающаяся женщина на кухне в Аланье с кулером для воды и газовым баллоном'}),
}
GALLERY = ['alanyam-ticaret-ipragaz-tup-su-bayii-alanya', 'ipragaz-alanya-tup-bayi-vitrin',
           'alanya-su-bayii-aysu-madran-hayat-damacana', 'alanya-damacana-su-bayii-ic-mekan']
HERO_PHOTO = {'home': 'alanya-tup-ve-su-siparisi-mutfak'}
PAGE_PHOTO = {'home': 'alanyam-ticaret-ipragaz-tup-su-bayii-alanya', 'gas': 'ipragaz-alanya-tup-bayi-vitrin',
              'water': 'alanya-su-bayii-aysu-madran-hayat-damacana', 'aysu': 'alanya-damacana-su-bayii-ic-mekan',
              'madran': 'alanya-damacana-su-bayii-ic-mekan', 'hayat': 'alanya-damacana-su-bayii-ic-mekan',
              'kizilay': 'alanya-su-bayii-aysu-madran-hayat-damacana', 'beypazari': 'alanya-su-bayii-aysu-madran-hayat-damacana',
              'contact': 'alanyam-ticaret-ipragaz-tup-su-bayii-alanya'}
OG_IMG = '/assets/img/alanya-tup-ve-su-siparisi-mutfak-1200.webp'


def photo(name, lang, sizes, cls='photo', eager=False):
    (w0, h0), alts = PHOTOS[name]
    ws = [w for w in (480, 800, 1200) if w <= w0]
    av = ', '.join(f'/assets/img/{name}-{w}.avif {w}w' for w in ws)
    wb = ', '.join(f'/assets/img/{name}-{w}.webp {w}w' for w in ws)
    d = ws[-1] if ws[-1] <= 800 else 800
    h = round(h0 * d / w0)
    load = 'eager' if eager else 'lazy'
    return (f'<figure class="{cls}"><picture><source type="image/avif" srcset="{av}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{wb}" sizes="{sizes}">'
            f'<img src="/assets/img/{name}-{d}.webp" width="{d}" height="{h}" alt="{e(alts[lang])}" loading="{load}" decoding="async"></picture></figure>')


def gallery(lang, first=None):
    h = {'tr': ('Bizden görüntüler', 'Alanya’daki <span class="hl">tüp ve su bayimiz</span>'),
         'en': ('Photos', 'Our gas and water shop <span class="hl">in Alanya</span>'),
         'ru': ('Фото', 'Наш магазин газа и воды <span class="hl">в Аланье</span>')}[lang]
    names = [n for n in GALLERY if n != first]  # sayfada zaten olan fotoğraf tekrar gösterilmez
    figs = ''.join(photo(n, lang, '(max-width:520px) 100vw, (max-width:1000px) 50vw, 280px', 'photo g-item') for n in names)
    return f'<section class="sec"><div class="wrap">{sec_head(h[0], h[1], center=True)}<div class="gallery g{len(names)}">{figs}</div></div></section>'


def reviews(lang):
    """Yalnız gerçek müşteri yorumları (content.REVIEWS). Liste boşsa bölüm çıkmaz."""
    if not REVIEWS:
        return ''
    h = {'tr': ('Müşteri yorumları', 'Müşterilerimiz <span class="hl">ne diyor?</span>'),
         'en': ('Reviews', 'What our <span class="hl">customers say</span>'),
         'ru': ('Отзывы', 'Что говорят <span class="hl">наши клиенты</span>')}[lang]
    note = {'tr': 'Yorumlar Türkçe orijinal hâliyle gösterilmektedir.', 'en': 'Reviews are shown in their original Turkish.', 'ru': 'Отзывы приведены на языке оригинала (турецкий).'}[lang]
    cards = ''
    for r in REVIEWS:
        stars = '★' * int(r.get('puan', 5)) + '☆' * (5 - int(r.get('puan', 5)))
        src = f' · {e(r["kaynak"])}' if r.get('kaynak') else ''
        cards += f'<figure class="card review"><div class="stars" aria-label="{r.get("puan", 5)}/5">{stars}</div><blockquote>{e(r["metin"])}</blockquote><figcaption><b>{e(r["ad"])}</b>{src}</figcaption></figure>'
    extra = '' if lang == 'tr' else f'<p class="note" style="text-align:center">{note}</p>'
    return f'<section class="sec"><div class="wrap">{sec_head(h[0], h[1], center=True)}<div class="grid g3">{cards}</div>{extra}</div></section>'


# ---------------- parçalar ----------------
def head(lang, title, desc, path, alts=None, schema=None, og_type='website'):
    url = SITE + path
    links = ''
    if alts:
        for l, p in alts.items():
            links += f'\n<link rel="alternate" hreflang="{l}" href="{SITE}{p}">'
        links += f'\n<link rel="alternate" hreflang="x-default" href="{SITE}{alts.get("tr", path)}">'
    sch = ''
    for s in (schema or []):
        sch += '\n<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False, separators=(',', ':')) + '</script>'
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">{links}
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="geo.region" content="TR-07"><meta name="geo.placename" content="Alanya">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}"><meta property="og:locale" content="{UI[lang]['locale']}">
<meta property="og:image" content="{SITE}{OG_IMG}"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#063246">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&amp;display=swap">
<link rel="stylesheet" href="/assets/site.css?v={VER}">{sch}
</head>
<body>
<a class="skip" href="#icerik">{UI[lang]['skip']}</a>
'''


def lang_switch(lang, alts):
    out = []
    for l in LANGS:
        href = (alts or {}).get(l, SLUG[l]['home'])
        cur = ' aria-current="true"' if l == lang else ''
        out.append(f'<a href="{href}" hreflang="{l}" lang="{l}"{cur}>{UI[l]["short"]}</a>')
    return '<nav class="lang" aria-label="Language">' + ''.join(out) + '</nav>'


def header(lang, active, alts):
    u = UI[lang]
    s = SLUG[lang]

    def a(k, label):
        cur = ' aria-current="page"' if active == k else ''
        return f'<a href="{s[k]}"{cur}>{label}</a>'
    blog = f'<a href="/blog/"{" aria-current=\"page\"" if active == "blog" else ""}>Rehber</a>' if lang == 'tr' else ''
    return f'''<div class="topbar"><div class="wrap">
  <div class="tb-left"><a class="tb-main" href="{tel(TEL_GSM)}">☎ {TEL_GSM}</a><a href="{tel(TEL_FIX)}">{TEL_FIX}</a><span>🕑 {u['open']} · {u['city']}</span></div>
  {lang_switch(lang, alts)}
</div></div>
<header class="hdr"><div class="wrap">
  <a class="brand" href="{s['home']}">{art.logo()}<span><b>{NAME}</b><small>{u['tagline']}</small></span></a>
  <button class="burger" aria-label="{u['menu']}" aria-expanded="false"><span></span><span></span><span></span></button>
  <nav class="nav" aria-label="{u['menu']}">
    {a('home', u['nav_home'])}
    {a('gas', u['nav_gas'])}
    <div class="sub"><button aria-expanded="false">{u['nav_water']}</button><div class="menu">
      {a('water', u['nav_all_water'])}{a('aysu', 'Aysu')}{a('madran', 'Madran')}{a('hayat', 'Hayat Su')}{a('kizilay', 'Kızılay Soda')}{a('beypazari', 'Beypazarı Soda')}
    </div></div>
    {blog}
    {a('contact', u['nav_contact'])}
    <a class="btn btn-call btn-sm hdr-call" href="{tel(TEL_GSM)}">{I['phone']} {u['call']}</a>
  </nav>
</div></header>
<main id="icerik">
'''


def hero(lang, pg, crumbs, art_svg, bg=None):
    u = UI[lang]
    chips = ''.join(f'<li>{e(c)}</li>' for c in pg['chips'])
    cr = ''
    if crumbs:
        cr = '<nav class="crumbs" aria-label="breadcrumb">' + '<span>›</span>'.join(
            f'<a href="{h}">{e(t)}</a>' if h else f'<b>{e(t)}</b>' for t, h in crumbs) + '</nav>'
    b1, b2 = pg['badge']
    if bg:
        (w0, h0), alts = PHOTOS[bg]
        ws = [w for w in (800, 1200, 1600) if w <= w0] or [w0]
        av = ', '.join(f'/assets/img/{bg}-{w}.avif {w}w' for w in ws)
        wb = ', '.join(f'/assets/img/{bg}-{w}.webp {w}w' for w in ws)
        return f'''<section class="hero hero-photo"><picture class="hero-bg"><source type="image/avif" srcset="{av}" sizes="100vw"><source type="image/webp" srcset="{wb}" sizes="100vw"><img src="/assets/img/{bg}-1200.webp" width="1448" height="1086" alt="{e(alts[lang])}" fetchpriority="high" decoding="async"></picture><div class="wrap">
  <div class="hero-text">
    {cr}
    <span class="eyebrow"><i></i>{e(pg['eyebrow'])}</span>
    <h1>{pg['h1']}</h1>
    <p class="lead">{e(pg['lead'])}</p>
    <div class="actions">
      <a class="btn btn-call btn-lg" href="{tel(TEL_GSM)}">{I['phone']} {TEL_GSM}</a>
      <a class="btn btn-wa btn-lg" href="#siparis">{I['wa']} {u['wa_order']}</a>
    </div>
    <ul class="chips">{chips}</ul>
  </div>
</div></section>
'''
    return f'''<section class="hero"><div class="wrap">
  <div class="hero-text">
    {cr}
    <span class="eyebrow"><i></i>{e(pg['eyebrow'])}</span>
    <h1>{pg['h1']}</h1>
    <p class="lead">{e(pg['lead'])}</p>
    <div class="actions">
      <a class="btn btn-call btn-lg" href="{tel(TEL_GSM)}">{I['phone']} {TEL_GSM}</a>
      <a class="btn btn-wa btn-lg" href="#siparis">{I['wa']} {u['wa_order']}</a>
    </div>
    <ul class="chips">{chips}</ul>
  </div>
  <div class="hero-art">{art_svg}<div class="hero-badge"><span><b>{e(b1)}</b>{e(b2)}</span></div></div>
</div>
<svg class="wave" viewBox="0 0 1440 80" preserveAspectRatio="none" aria-hidden="true"><path d="M0 40c240-40 480-40 720 0s480 40 720 0v40H0z" fill="#fff"/></svg>
</section>
'''


def product_cards(lang, keys, extra=None):
    u = UI[lang]
    s = SLUG[lang]
    cards = []
    for k in keys:
        if k == 'gas':
            pic = art.cylinder(GAS)
            name = u['nav_gas']
            pg = P[lang]['gas']
            txt = strip(pg['lead'])
            sizes = ''
            tag = '7/24'
        elif k in SODAS:
            t, c = BRAND_COLORS[k]
            pic = art.soda(BRAND_NAME[k], t, c)
            name = BRAND_NAME[k] + (' Soda' if lang != 'ru' else '')
            txt = BRAND[k][lang].split('. ')[0] + '.'
            sizes = ''
            tag = 'Soda'
        else:
            t, c = BRAND_COLORS[k]
            pic = art.jug(BRAND_NAME[k], t, c)
            name = 'Hayat Su' if k == 'hayat' else BRAND_NAME[k]
            txt = BRAND[k][lang].split('. ')[0] + '.'
            sizes = '<div class="sizes">' + ''.join(f'<span>{szl(x, lang)}</span>' for x in BRAND[k]['sizes']) + '</div>'
            tag = '19 L' if lang != 'ru' else '19 л'
        cards.append(f'''<a class="card prod" href="{s[k]}"><span class="tag">{tag}</span><div class="pic">{pic}</div><div class="bd"><h3>{e(name)}</h3><p>{e(txt)}</p>{sizes}<span class="more">{u['more']}</span></div></a>''')
    if extra:
        ic, h, p = extra
        cards.append(f'''<a class="card" href="#siparis"><div class="ic">{I[ic]}</div><h3>{e(h)}</h3><p>{e(p)}</p><span class="more" style="display:inline-flex;margin-top:12px;font-weight:800">{u['order_btn']} →</span></a>''')
    n = len(cards)
    g = 'g3' if n % 3 == 0 else 'g4'
    return f'<div class="grid {g}">' + ''.join(cards) + '</div>'


def szl(x, lang):
    if x == 'Bardak':
        return {'tr': 'Bardak su', 'en': 'Cup water', 'ru': 'Стаканчики'}[lang]
    if lang == 'en':
        return x.replace(',', '.')
    if lang == 'ru':
        return x.replace('L', 'л').replace('ml', 'мл')
    return x


def icon_cards(items, cols='g3'):
    return f'<div class="grid {cols}">' + ''.join(
        f'<div class="card"><div class="ic">{I[ic]}</div><h3>{e(h)}</h3><p>{e(p)}</p></div>' for ic, h, p in items) + '</div>'


def sec_head(k, h, p=None, center=False):
    pp = f'<p>{e(p)}</p>' if p else ''
    return f'<div class="head{" c" if center else ""}"><span class="kicker">{e(k)}</span><h2>{h}</h2>{pp}</div>'


def steps(lang):
    u = UI[lang]
    items = ''.join(f'<div class="card step"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in u['steps'])
    return f'<section class="sec sec-alt"><div class="wrap">{sec_head(u["steps_k"], e(u["steps_h"]), center=True)}<div class="grid g3 steps">{items}</div></div></section>'


def why(lang):
    u = UI[lang]
    return f'<section class="sec"><div class="wrap">{sec_head(u["why_k"], e(u["why_h"]), center=True)}{icon_cards(u["why"], "g4")}</div></section>'


def brands_strip(lang, exclude=None):
    u = UI[lang]
    s = SLUG[lang]
    tiles = []
    for k in ['gas', 'aysu', 'madran', 'hayat', 'kizilay', 'beypazari']:
        if k == exclude:
            continue
        if k == 'gas':
            ic, nm = art.cylinder(GAS), GAS
        elif k in SODAS:
            t, c = BRAND_COLORS[k]
            ic, nm = art.soda(BRAND_NAME[k], t, c), BRAND_NAME[k]
        else:
            t, c = BRAND_COLORS[k]
            ic, nm = art.jug(BRAND_NAME[k], t, c), ('Hayat Su' if k == 'hayat' else BRAND_NAME[k])
        tiles.append(f'<a class="brand-tile" href="{s[k]}">{ic}<span>{e(nm)}<small>{e(u["brands_sub"][k])}</small></span></a>')
    cols = 3 if len(tiles) > 4 else len(tiles)
    return f'<section class="sec sec-alt"><div class="wrap">{sec_head(u["brands_k"], e(u["brands_h"]), center=True)}<div class="brands" style="--cols:{cols}">' + ''.join(tiles) + '</div></div></section>'


def order(lang, default):
    u = UI[lang]
    opts = ''
    for key, val, labels in PRODUCTS:
        lab = val if lang == 'tr' else labels[lang]
        sel = ' selected' if key == default else ''
        opts += f'<option value="{e(val)}"{sel}>{e(lab)}</option>'
    ticks = ''.join(f'<li>{e(t)}</li>' for t in u['order_ticks'])
    return f'''<section class="sec sec-sand" id="siparis"><div class="wrap order">
  <div class="order-side">
    <span class="kicker">{e(u['order_k'])}</span><h2>{e(u['order_h'])}</h2>
    <p class="lead" style="font-size:1.04rem">{e(u['order_p'])}</p>
    <ul class="ticks">{ticks}</ul>
    <a class="btn btn-call" href="{tel(TEL_GSM)}">{I['phone']} {TEL_GSM}</a>
  </div>
  <form class="order-box" id="siparis-form" data-wa="{WA_NUM}" autocomplete="on">
    <div class="row2">
      <label class="fld"><span>{u['f_product']}</span><select name="urun">{opts}</select></label>
      <label class="fld"><span>{u['f_qty']}</span><input name="adet" type="number" min="1" max="99" value="1" inputmode="numeric"></label>
    </div>
    <label class="fld"><span>{u['f_name']}</span><input name="ad" type="text" autocomplete="name"></label>
    <label class="fld"><span>{u['f_addr']}</span><textarea name="adres" rows="2" required placeholder="{e(u['f_addr_ph'])}" autocomplete="street-address"></textarea></label>
    <label class="fld"><span>{u['f_note']}</span><input name="not" type="text" placeholder="{e(u['f_note_ph'])}"></label>
    <button class="btn btn-wa btn-lg" type="submit">{I['wa']} {u['f_send']}</button>
    <p class="note">{e(u['f_small'])}</p>
  </form>
</div></section>
'''


def faq_block(lang, faq, k=None, h=None):
    u = UI[lang]
    items = ''.join(f'<details><summary>{e(q)}</summary><div><p>{e(a)}</p></div></details>' for q, a in faq)
    return f'<section class="sec"><div class="wrap">{sec_head(k or u["faq_k"], e(h or u["faq_h"]), center=True)}<div class="faq">{items}</div></div></section>'


def cta(lang):
    u = UI[lang]
    return f'''<section class="sec" style="padding-top:20px"><div class="wrap"><div class="cta">
  <div><h2>{e(u['cta_h'])}</h2><p>{e(u['cta_p'])}</p>
  <div class="actions" style="margin-bottom:0"><a class="btn btn-call btn-lg" href="{tel(TEL_GSM)}">{I['phone']} {u['call']}</a><a class="btn btn-wa btn-lg" href="{wa_link(lang, WA_HELLO)}" target="_blank" rel="noopener">{I['wa']} {u['wa']}</a></div></div>
  <div class="phones">
    <a href="{tel(TEL_GSM)}"><span>{TEL_GSM}</span><small>{u['gsm']}</small></a>
    <a href="{tel(TEL_FIX)}"><span>{TEL_FIX}</span><small>{u['fixed']}</small></a>
    <a href="{wa_link(lang, WA_HELLO)}" target="_blank" rel="noopener"><span>{TEL_WA}</span><small>{u['wa_l']}</small></a>
  </div>
</div></div></section>
'''


def footer(lang, alts):
    u = UI[lang]
    s = SLUG[lang]
    blog = '<li><a href="/blog/">Rehber</a></li>' if lang == 'tr' else ''
    langs = ''.join(f'<li><a href="{(alts or {}).get(l, SLUG[l]["home"])}" hreflang="{l}">{UI[l]["lang_name"]}</a></li>' for l in LANGS)
    return f'''</main>
<footer class="ftr"><div class="wrap">
  <div class="cols">
    <div><a class="brand" href="{s['home']}">{art.logo()}<span><b>{NAME}</b><small>{u['tagline']}</small></span></a><p style="margin-top:14px">{e(u['f_about'])}</p></div>
    <div><h4>{u['f_pages']}</h4><ul><li><a href="{s['home']}">{u['nav_home']}</a></li><li><a href="{s['gas']}">{u['nav_gas']}</a></li><li><a href="{s['water']}">{u['nav_water']}</a></li><li><a href="{s['aysu']}">Aysu</a></li><li><a href="{s['madran']}">Madran</a></li><li><a href="{s['hayat']}">Hayat Su</a></li><li><a href="{s['kizilay']}">Kızılay Soda</a></li><li><a href="{s['beypazari']}">Beypazarı Soda</a></li>{blog}<li><a href="{s['contact']}">{u['nav_contact']}</a></li></ul></div>
    <div><h4>{u['f_contact']}</h4><ul><li><a href="{tel(TEL_GSM)}">{TEL_GSM}</a> · {u['gsm']}</li><li><a href="{tel(TEL_FIX)}">{TEL_FIX}</a> · {u['fixed']}</li><li><a href="{wa_link(lang, WA_HELLO)}" target="_blank" rel="noopener">{TEL_WA}</a> · WhatsApp</li><li>{u['open']}</li><li>{u['city']}</li></ul></div>
    <div><h4>{u['f_lang']}</h4><ul>{langs}</ul></div>
  </div>
  <div class="copy"><span>© 2026 {NAME}. {u['rights']}</span><span>{u['city']}</span></div>
</div></footer>
<div class="dock"><a class="btn btn-call" href="{tel(TEL_GSM)}">{I['phone']} {u['call']}</a><a class="btn btn-wa" href="#siparis">{I['wa']} {u['wa']}</a></div>
<script src="/assets/site.js?v={VER}" defer></script>
</body>
</html>
'''


# ---------------- şema ----------------
def org_schema(lang):
    return {
        '@context': 'https://schema.org', '@type': 'Store', '@id': SITE + '/#isletme', 'name': NAME,
        'description': UI[lang]['f_about'], 'url': SITE + '/', 'telephone': intl(TEL_GSM),
        'image': [SITE + f'/assets/img/{n}-800.webp' for n in GALLERY], 'logo': SITE + '/favicon.svg', 'priceRange': '₺',
        'address': {'@type': 'PostalAddress', 'addressLocality': 'Alanya', 'addressRegion': 'Antalya', 'addressCountry': 'TR'},
        'geo': {'@type': 'GeoCoordinates', 'latitude': 36.5444, 'longitude': 31.9954},
        'areaServed': {'@type': 'City', 'name': 'Alanya', 'sameAs': 'https://www.wikidata.org/wiki/Q212017'},
        'openingHoursSpecification': {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'opens': '00:00', 'closes': '23:59'},
        'contactPoint': [{'@type': 'ContactPoint', 'telephone': intl(TEL_GSM), 'contactType': 'sales', 'availableLanguage': ['tr']},
                         {'@type': 'ContactPoint', 'telephone': intl(TEL_FIX), 'contactType': 'customer service'},
                         {'@type': 'ContactPoint', 'telephone': intl(TEL_WA), 'contactType': 'sales', 'contactOption': 'WhatsApp'}],
        'brand': [{'@type': 'Brand', 'name': n} for n in [GAS, 'Aysu', 'Madran', 'Hayat', 'Kızılay', 'Beypazarı']],
        'foundingDate': '1983', 'knowsLanguage': ['tr'],
    }


def faq_schema(faq):
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq]}


def crumb_schema(crumbs):
    items = []
    for i, (t, h) in enumerate(crumbs, 1):
        d = {'@type': 'ListItem', 'position': i, 'name': t}
        if h:
            d['item'] = SITE + h
        items.append(d)
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items}


# ---------------- sayfa tipleri ----------------
def write(path, content):
    fs = os.path.join(ROOT, path.strip('/').replace('/', os.sep), 'index.html') if path.endswith('/') else os.path.join(ROOT, path.strip('/'))
    os.makedirs(os.path.dirname(fs), exist_ok=True)
    with open(fs, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)


def page(lang, key):
    pg = P[lang][key]
    u = UI[lang]
    s = SLUG[lang]
    alts = {l: SLUG[l][key] for l in LANGS}
    path = s[key]
    crumbs = [] if key == 'home' else ([(u['crumb_home'], s['home'])] + ([(u['nav_water'], s['water'])] if key in WATERS + SODAS else []) + [(pg['crumb'], None)])
    # sahne
    if pg['art'] == 'cyl':
        sv = art.scene('cyl', {'gas': GAS})
    elif pg['art'] == 'jug':
        sv = art.scene('jug', {'brand': BRAND_NAME.get(key, 'Aysu')})
    elif pg['art'] == 'jugs':
        sv = art.scene('jugs')
    elif pg['art'] == 'soda':
        sv = art.scene('soda', {'brand': BRAND_NAME[key], 'colors': BRAND_COLORS[key]})
    else:
        sv = art.scene('mix', {'gas': GAS, 'brand': 'Aysu'})
    out = [head(lang, pg['title'], pg['desc'], path, alts,
                [org_schema(lang), faq_schema(pg['faq'])] + ([crumb_schema([(t, h or path) for t, h in crumbs])] if crumbs else [])),
           header(lang, key, alts), hero(lang, pg, crumbs, sv, HERO_PHOTO.get(key))]

    # Ürün bölümü
    if key == 'home':
        out.append(f'<section class="sec"><div class="wrap">{sec_head(pg["prod_k"], pg["prod_h"], pg["prod_p"])}{product_cards(lang, ["gas", "aysu", "madran", "hayat", "kizilay", "beypazari"])}</div></section>')
    elif key == 'gas' or key in SODAS:
        out.append(f'<section class="sec"><div class="wrap">{sec_head(pg["prod_k"], pg["prod_h"], pg["prod_p"])}{icon_cards(pg["cards"])}</div></section>')
    elif key == 'water':
        out.append(f'<section class="sec"><div class="wrap">{sec_head(pg["prod_k"], pg["prod_h"], pg["prod_p"])}{product_cards(lang, ["aysu", "madran", "hayat", "kizilay", "beypazari"], pg["extra_card"])}</div></section>')
    elif key in WATERS:
        t, c = BRAND_COLORS[key]
        sizes = BRAND[key]['sizes']
        cards = []
        for i, sz in enumerate(sizes):
            lb = szl(sz, lang)
            pic = art.jug(BRAND_NAME[key], t, c) if i == 0 else art.cup(BRAND_NAME[key], t) if sz == 'Bardak' else art.bottle(t, label=lb)
            nm = {'tr': ['19 L damacana', '1,5 L pet şişe', '0,5 L pet şişe', 'Bardak su'], 'en': ['19 L jug', '1.5 L PET bottle', '0.5 L PET bottle', 'Cup water'], 'ru': ['Бутыль 19 л', 'Бутылка 1,5 л', 'Бутылка 0,5 л', 'Вода в стаканчиках']}[lang][i]
            dd = {'tr': ['Ev ve işyeri için standart damacana. Pompa ya da sebille kullanılır.', 'Günlük kullanım, sofra ve dışarıda tüketim için.', 'Toplantı, davet ve özel günler için pratik boy.', 'Düğün, toplantı, ofis ve davetler için kapaklı bardak su.'],
                  'en': ['The standard jug for homes and offices, used with a pump or dispenser.', 'For everyday use, the table and on the go.', 'Handy size for meetings, events and special occasions.', 'Sealed cup water for weddings, meetings, offices and events.'],
                  'ru': ['Стандартная бутыль для дома и офиса — с помпой или кулером.', 'Для каждого дня, к столу и в дорогу.', 'Удобный объём для встреч, мероприятий и праздников.', 'Вода в запечатанных стаканчиках для свадеб, встреч, офисов и праздников.']}[lang][i]
            cards.append(f'<a class="card prod" href="#siparis"><div class="pic">{pic}</div><div class="bd"><h3>{BRAND_NAME[key]} · {e(nm)}</h3><p>{e(dd)}</p><span class="more">{u["order_btn"]} →</span></div></a>')
        if len(sizes) == 1:
            cards.append(f'<div class="card"><div class="ic">{I["chat"]}</div><h3>{e({"tr": "Şişe seçenekleri", "en": "Bottle sizes", "ru": "Бутылки меньшего объёма"}[lang])}</h3><p>{e(u["ask"])}: {TEL_GSM}</p></div>')
            cards.append(f'<div class="card"><div class="ic">{I["truck"]}</div><h3>{e(u["why"][1][1])}</h3><p>{e(u["why"][1][2])}</p></div>')
        gcls = 'g4' if len(cards) == 4 else 'g3'
        out.append(f'<section class="sec"><div class="wrap">{sec_head(pg["prod_k"], pg["prod_h"], pg["prod_p"])}<div class="grid {gcls}">{"".join(cards)}</div></div></section>')
    elif key == 'contact':
        cc = [('phone', TEL_GSM, u['gsm'], tel(TEL_GSM)), ('phone', TEL_FIX, u['fixed'], tel(TEL_FIX)), ('wa', TEL_WA, 'WhatsApp', wa_link(lang, WA_HELLO)),
              ('clock', u['open'], {'tr': 'Gece, hafta sonu, bayram', 'en': 'Nights, weekends, holidays', 'ru': 'Ночью, в выходные и праздники'}[lang], None),
              ('map', u['city'], {'tr': 'Alanya geneline teslimat', 'en': 'Delivery across Alanya', 'ru': 'Доставка по всей Аланье'}[lang], None),
              ('chat', u['wa_order'], {'tr': 'Formla hazır mesaj', 'en': 'Ready-made message form', 'ru': 'Готовое сообщение через форму'}[lang], '#siparis')]
        cards = ''.join((f'<a class="card" href="{h}"' + (' target="_blank" rel="noopener"' if h and h.startswith('https') else '') + '>' if h else '<div class="card">')
                        + f'<div class="ic">{I[ic]}</div><h3>{e(t)}</h3><p>{e(sub)}</p>' + ('</a>' if h else '</div>') for ic, t, sub, h in cc)
        out.append(f'<section class="sec"><div class="wrap">{sec_head(u["f_contact"], e(pg["crumb"]))}<div class="grid g3">{cards}</div></div></section>')

    if key != 'contact':
        out.append(steps(lang))

    # Bilgi bölümü (yanında sayfaya ait fotoğraf)
    ph = PAGE_PHOTO[key]
    if 'info_h' in pg:
        ps = ''.join(f'<p>{e(x)}</p>' for x in pg['info_p'])
        ticks = f'<ul class="ticks">' + ''.join(f'<li>{e(x)}</li>' for x in pg['info_ticks']) + '</ul>'
        btn = f'<a class="btn btn-wa" href="#siparis">{I["wa"]} {u["wa_order"]}</a>'
        if 'safety' in pg:
            left = f'<span class="kicker">{e(pg["info_k"])}</span><h2>{e(pg["info_h"])}</h2>{ps}{ticks}{photo(ph, lang, "(max-width:860px) 100vw, 560px")}'
            right = f'<div class="warn"><h3>⚠ {e(pg["safety_h"])}</h3><ul class="ticks">' + ''.join(f'<li>{e(x)}</li>' for x in pg['safety']) + '</ul></div>'
        else:
            left = f'<span class="kicker">{e(pg["info_k"])}</span><h2>{e(pg["info_h"])}</h2>{ps}{ticks}{btn}'
            right = photo(ph, lang, '(max-width:860px) 100vw, 560px')
        out.append(f'<section class="sec sec-alt"><div class="wrap split"><div>{left}</div>{right}</div></section>')
    elif key == 'contact':
        sh = {'tr': ('Dükkânımız', 'Alanya’daki dükkânımız', 'Tüp ve su siparişlerimizi Alanya’daki dükkânımızdan hazırlıyoruz. Siparişinizi telefonla ya da WhatsApp’tan verin, kapınıza getirelim.'),
              'en': ('Our shop', 'Our shop in Alanya', 'We prepare gas and water orders at our shop in Alanya. Order by phone or WhatsApp and we’ll bring it to your door.'),
              'ru': ('Наш магазин', 'Наш магазин в Аланье', 'Заказы газа и воды мы собираем в нашем магазине в Аланье. Закажите по телефону или в WhatsApp — привезём к двери.')}[lang]
        out.append(f'<section class="sec sec-alt"><div class="wrap split"><div><span class="kicker">{e(sh[0])}</span><h2>{e(sh[1])}</h2><p>{e(sh[2])}</p><a class="btn btn-wa" href="#siparis">{I["wa"]} {u["wa_order"]}</a></div>{photo(ph, lang, "(max-width:860px) 100vw, 560px")}</div></section>')

    if key in ('home', 'contact'):
        out.append(why(lang))
    out.append(order(lang, DEFAULT_PRODUCT[key]))
    if key in WATERS + SODAS:
        out.append(brands_strip(lang, exclude=key))
    elif key in ('home', 'gas', 'water'):
        out.append(brands_strip(lang, exclude=key if key == 'gas' else None))
    if lang == 'tr' and key != 'contact':
        out.append(blog_teaser(key))
    out.append(reviews(lang))
    out.append(gallery(lang, first=ph))
    out.append(faq_block(lang, pg['faq']))
    out.append(cta(lang))
    out.append(footer(lang, alts))
    write(path, ''.join(out))
    OUT.append((path, alts))


# ---------------- blog ----------------
def art_card(a):
    sv = {'cyl': art.cylinder(GAS), 'jug': art.jug('Su'), 'jugs': art.jug('Su', '#3a8fc4', '#1f6996')}[a['art']]
    return f'''<a class="card prod" href="/blog/{a['slug']}/"><span class="tag">{e(a['cat'])}</span><div class="pic">{sv}</div><div class="bd"><h3>{e(strip(a['h1']))}</h3><p>{e(a['desc'])}</p><span class="more">Devamını oku →</span></div></a>'''


def blog_teaser(key):
    pick = {'gas': ['alanya-tup-siparisi', 'tup-gaz-guvenligi', 'su-ph-degeri-nedir'],
            'water': ['su-ph-degeri-nedir', 'aysu-madran-hayat-hangi-su', 'kaynak-suyu-ile-icme-suyu-farki']}.get(
        key, ['su-ph-degeri-nedir', 'alanya-su-siparisi', 'alanya-tup-siparisi'] if key == 'home' else ['aysu-madran-hayat-hangi-su', 'su-ph-degeri-nedir', 'sebil-ve-damacana-pompasi-temizligi'])
    arts = [a for s in pick for a in ARTICLES if a['slug'] == s]
    return f'<section class="sec"><div class="wrap">{sec_head("Rehber", "Su ve tüp hakkında <span class=\"hl\">bilmeniz gerekenler</span>", "Su kalitesi, pH değeri, tüp güvenliği ve Alanya’da sipariş üzerine kısa rehberler.")}<div class="grid g3">' + ''.join(art_card(a) for a in arts) + '</div><p style="margin-top:22px"><a class="btn btn-ghost" href="/blog/">Tüm rehber yazıları →</a></p></div></section>'


def blog_index():
    lang = 'tr'
    pg = dict(eyebrow='Rehber · Alanya', h1='Su ve tüp <span>rehberi</span>',
              lead='Su kalitesi ve pH değeri, kaynak suyu ile içme suyu farkı, tüp gaz güvenliği ve Alanya’da su ve tüp siparişi üzerine sade, kaynaklı yazılar.',
              chips=['Su kalitesi', 'pH değeri', 'Tüp güvenliği', 'Alanya sipariş'], badge=(str(len(ARTICLES)), 'rehber yazısı'))
    crumbs = [('Ana Sayfa', '/'), ('Rehber', None)]
    path = '/blog/'
    title = 'Su ve Tüp Rehberi: pH Değeri, Su Kalitesi, Tüp Güvenliği | Alanyam Ticaret'
    desc = 'Suyun pH değeri, kaynak suyu ile içme suyu farkı, Aysu–Madran–Hayat karşılaştırması, tüp gaz güvenliği ve Alanya su/tüp siparişi rehberleri.'
    items = {'@context': 'https://schema.org', '@type': 'ItemList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i, 'url': f'{SITE}/blog/{a["slug"]}/', 'name': strip(a['h1'])} for i, a in enumerate(ARTICLES, 1)]}
    out = [head(lang, title, desc, path, None, [org_schema(lang), crumb_schema([('Ana Sayfa', '/'), ('Rehber', path)]), items]),
           header(lang, 'blog', None), hero(lang, pg, crumbs, art.scene('mix', {'gas': GAS, 'brand': 'Aysu'})),
           f'<section class="sec"><div class="wrap">{sec_head("Tüm yazılar", "Rehber yazıları")}<div class="grid g3">' + ''.join(art_card(a) for a in ARTICLES) + '</div></div></section>',
           steps(lang), order(lang, 'aysu'), gallery(lang), cta(lang), footer(lang, None)]
    write(path, ''.join(out))
    OUT.append((path, None))


def article(a):
    lang = 'tr'
    path = f'/blog/{a["slug"]}/'
    crumbs = [('Ana Sayfa', '/'), ('Rehber', '/blog/'), (a['cat'], None)]
    pg = dict(eyebrow=f'Rehber · {a["cat"]}', h1=a['h1'].replace('?', '<span>?</span>', 1) if False else a['h1'], lead=a['desc'],
              chips=['Kısa cevap', 'Kaynaklı bilgi', 'Alanya'], badge=('📖', '24 Kasım 2026'))
    sv = art.scene({'cyl': 'cyl', 'jug': 'jug', 'jugs': 'jugs'}[a['art']], {'gas': GAS, 'brand': 'Aysu'})
    toc = ''.join(f'<li><a href="#b{i}">{e(h)}</a></li>' for i, (h, _) in enumerate(a['body'], 1))
    body = ''.join(f'<h2 id="b{i}">{e(h)}</h2>{b}' for i, (h, b) in enumerate(a['body'], 1))
    src = ''
    if a['sources']:
        src = '<h2>Kaynaklar</h2><ol class="src">' + ''.join(f'<li><a href="{u}" rel="nofollow noopener" target="_blank">{e(t)}</a></li>' for t, u in a['sources']) + '</ol>'
    rel_s = SLUG['tr']
    rel_names = {'water': 'Alanya damacana su', 'aysu': 'Aysu su siparişi', 'madran': 'Madran su siparişi', 'hayat': 'Hayat su siparişi', 'gas': f'{GAS} tüp siparişi', 'contact': 'İletişim', 'home': 'Ana sayfa'}
    rel = ''.join(f'<li><a href="{rel_s[k]}">{rel_names[k]}</a></li>' for k in a['related'])
    schema_art = {'@context': 'https://schema.org', '@type': 'Article', 'headline': strip(a['h1']), 'description': a['desc'],
                  'datePublished': DATE, 'dateModified': DATE, 'inLanguage': 'tr', 'mainEntityOfPage': SITE + path,
                  'author': {'@type': 'Organization', 'name': NAME, 'url': SITE + '/'},
                  'publisher': {'@type': 'Organization', 'name': NAME, 'logo': {'@type': 'ImageObject', 'url': SITE + '/favicon.svg'}},
                  'about': [{'@type': 'Place', 'name': 'Alanya'}]}
    if a['sources']:
        schema_art['citation'] = [u for _, u in a['sources']]
    out = [head(lang, a['title'], a['desc'], path, None, [org_schema(lang), schema_art, faq_schema(a['faq']), crumb_schema([(t, h or path) for t, h in crumbs])], og_type='article'),
           header(lang, 'blog', None), hero(lang, pg, crumbs, sv),
           f'''<section class="sec" style="padding-top:40px"><div class="wrap art-wrap">
  <article class="art-body">
    <div class="answer"><b>Kısa cevap</b><p>{e(a['answer'])}</p></div>
    {body}
    {src}
    <p class="meta">Yayın: 24 Kasım 2026 · Hazırlayan: {NAME}, Alanya</p>
  </article>
  <aside class="art-side">
    <div class="panel"><h3>Bu yazıda</h3><ol class="toc">{toc}</ol></div>
    <div class="panel"><h3>Sipariş</h3><p>Alanya’da 7/24 tüp ve su siparişi.</p><a class="btn btn-call" href="{tel(TEL_GSM)}" style="width:100%">{I['phone']} {TEL_GSM}</a><a class="btn btn-wa" href="#siparis" style="width:100%;margin-top:8px">{I['wa']} WhatsApp</a><ul class="ticks" style="margin-top:14px">{rel}</ul></div>
  </aside>
</div></section>''',
           order(lang, DEFAULT_PRODUCT['gas'] if a['art'] == 'cyl' else 'aysu'),
           faq_block(lang, a['faq']),
           f'<section class="sec sec-alt"><div class="wrap">{sec_head("Rehber", "Diğer yazılar")}<div class="grid g3">' + ''.join(art_card(x) for x in ARTICLES if x['slug'] != a['slug'])[:0] + ''.join(art_card(x) for x in [y for y in ARTICLES if y['slug'] != a['slug']][:3]) + '</div></div></section>',
           cta(lang), footer(lang, None)]
    write(path, ''.join(out))
    OUT.append((path, None))


# ---------------- yardımcı dosyalar ----------------
def redirects():
    for old, new in REDIRECTS.items():
        write(old, f'''<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>{NAME}</title><link rel="canonical" href="{SITE}{new}"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0;url={new}"><script>location.replace("{new}")</script></head><body><a href="{new}">{SITE}{new}</a></body></html>''')


def notfound():
    lang = 'tr'
    out = [head(lang, 'Sayfa bulunamadı | Alanyam Ticaret', 'Aradığınız sayfa bulunamadı.', '/404.html'),
           header(lang, None, None),
           f'''<section class="hero"><div class="wrap"><div class="hero-text"><span class="eyebrow"><i></i>404</span><h1>Sayfa <span>bulunamadı</span></h1><p class="lead">Aradığınız sayfa taşınmış olabilir. Sipariş için bizi arayabilirsiniz.</p><div class="actions"><a class="btn btn-call btn-lg" href="{tel(TEL_GSM)}">{I['phone']} {TEL_GSM}</a><a class="btn btn-ghost btn-lg" href="/">Ana sayfa</a></div></div><div class="hero-art">{art.scene('mix', {'gas': GAS, 'brand': 'Aysu'})}</div></div></section>''',
           footer(lang, None)]
    with open(os.path.join(ROOT, '404.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(''.join(out).replace('<meta name="robots" content="index,follow,max-image-preview:large">', '<meta name="robots" content="noindex">'))


def sitemap():
    x = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for path, alts in OUT:
        x.append(f'<url><loc>{SITE}{path}</loc><lastmod>{DATE}</lastmod>')
        if alts:
            for l, p in alts.items():
                x.append(f'<xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{p}"/>')
            x.append(f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{alts["tr"]}"/>')
        x.append('</url>')
    x.append('</urlset>')
    with open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(x))
    with open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')


def llms():
    lines = [f'# {NAME} — Alanya tüp ve su bayii', '',
             f'> {NAME}, Alanya (Antalya) merkezli tüp gaz ve damacana su bayisidir. {GAS} tüp ile Aysu, Madran ve Hayat 19 L damacana su; Aysu ve Madran için 1,5 L ve 0,5 L şişe su. 7/24 sipariş, ev ve işyerine kapıya teslim. 1983’ten bugüne Alanya’da.', '',
             '## İletişim',
             f'- Cep / sipariş: {TEL_GSM}', f'- Sabit hat: {TEL_FIX}', f'- WhatsApp: {TEL_WA} (sitedeki form siparişi Türkçe mesaj olarak hazırlar)',
             '- Çalışma: 7/24 (gece, hafta sonu, bayram)', '- Hizmet bölgesi: Alanya geneli', '- Diller: site Türkçe, İngilizce ve Rusça', '',
             '## Sayfalar']
    for k in KEYS:
        lines.append(f'- [{strip(P["tr"][k]["h1"])}]({SITE}{SLUG["tr"][k]}) — EN: {SITE}{SLUG["en"][k]} · RU: {SITE}{SLUG["ru"][k]}')
    lines += ['', '## Rehber']
    for a in ARTICLES:
        lines.append(f'- [{strip(a["h1"])}]({SITE}/blog/{a["slug"]}/): {a["answer"]}')
    with open(os.path.join(ROOT, 'llms.txt'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


def favicon():
    with open(os.path.join(ROOT, 'favicon.svg'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(art.logo().replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'))


def clean():
    # Önceki çıktıyı temizle (kaynak klasörlerine dokunma)
    keep = {'_tools', 'assets', '.git', '.gitignore', 'CNAME', '_kaynak', 'img', '.nojekyll'}
    for n in os.listdir(ROOT):
        if n in keep:
            continue
        p = os.path.join(ROOT, n)
        if os.path.isdir(p):
            shutil.rmtree(p)
        elif n.endswith(('.html', '.xml', '.txt', '.svg')):
            os.remove(p)


if __name__ == '__main__':
    clean()
    for lg in LANGS:
        for k in KEYS:
            page(lg, k)
    blog_index()
    for a_ in ARTICLES:
        article(a_)
    redirects()
    notfound()
    sitemap()
    llms()
    favicon()
    print(f'{len(OUT)} sayfa yazıldı -> {ROOT}')
