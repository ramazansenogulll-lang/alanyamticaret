# -*- coding: utf-8 -*-
"""Alanyam Ticaret — tüm metinler (TR / EN / RU).
Teyitli bilgiler (eski siteden): telefonlar, 7/24, Alanya, 1983'ten bugüne, özel günler için şişe su,
Aysu (Dedegöl Dağı etekleri), Madran (Aydın Bozdoğan). İpragaz: 1961'den beri LPG, 1999'dan beri SHV Energy.
Hayat: Danone markası. Doğrulanmamış iddia (pH, teslim dakikası, fiyat, sigorta) YAZILMAZ.
"""

SITE = 'https://alanyamticaret.com.tr'
NAME = 'Alanyam Ticaret'
GAS = 'İpragaz'            # kullanıcı "İbragaz" yazdı; firma adı İpragaz. Değişirse yalnız burayı düzelt.
TEL_GSM = '0551 072 49 77'
TEL_FIX = '0242 514 59 96'
TEL_WA = '0553 265 39 43'
WA_NUM = '905532653943'


def intl(n):
    d = ''.join(c for c in n if c.isdigit())
    return '+90' + d[1:]


LANGS = ['tr', 'en', 'ru']
KEYS = ['home', 'gas', 'water', 'aysu', 'madran', 'hayat', 'kizilay', 'beypazari', 'contact']
SODAS = ['kizilay', 'beypazari']
WATERS = ['aysu', 'madran', 'hayat']

SLUG = {
    'tr': {'home': '/', 'gas': '/ipragaz/', 'water': '/su/', 'aysu': '/aysu/', 'madran': '/madran/', 'hayat': '/hayat-su/', 'kizilay': '/kizilay-soda/', 'beypazari': '/beypazari-soda/', 'contact': '/iletisim/'},
    'en': {'home': '/en/', 'gas': '/en/ipragaz/', 'water': '/en/water/', 'aysu': '/en/aysu/', 'madran': '/en/madran/', 'hayat': '/en/hayat-su/', 'kizilay': '/en/kizilay-soda/', 'beypazari': '/en/beypazari-soda/', 'contact': '/en/contact/'},
    'ru': {'home': '/ru/', 'gas': '/ru/ipragaz/', 'water': '/ru/voda/', 'aysu': '/ru/aysu/', 'madran': '/ru/madran/', 'hayat': '/ru/hayat-su/', 'kizilay': '/ru/kizilay-soda/', 'beypazari': '/ru/beypazari-soda/', 'contact': '/ru/kontakty/'},
}

# Eski WordPress adresleri -> yeni adres
REDIRECTS = {'/kongaz/': '/ipragaz/', '/about/': '/', '/why-us/': '/', '/index.php/iletisim/': '/iletisim/', '/contact/': '/iletisim/'}

# Sipariş formu ürünleri: değer (mesaja Türkçe gider) + dillere göre etiket
PRODUCTS = [
    ('gas_home', f'{GAS} mutfak tüpü (ev)', {'en': f'{GAS} kitchen gas cylinder (home)', 'ru': f'Газовый баллон {GAS} для кухни (дом)'}),
    ('gas_biz', f'{GAS} işyeri tüpü', {'en': f'{GAS} gas cylinder for business', 'ru': f'Газовый баллон {GAS} для бизнеса'}),
    ('aysu', 'Aysu 19 L damacana', {'en': 'Aysu 19 L water jug', 'ru': 'Aysu, бутыль 19 л'}),
    ('madran', 'Madran 19 L damacana', {'en': 'Madran 19 L water jug', 'ru': 'Madran, бутыль 19 л'}),
    ('hayat', 'Hayat 19 L damacana', {'en': 'Hayat 19 L water jug', 'ru': 'Hayat, бутыль 19 л'}),
    ('b15', 'Aysu pet su 1,5 L', {'en': 'Aysu bottled water 1.5 L', 'ru': 'Aysu, бутылка 1,5 л'}),
    ('b05', 'Aysu pet su 0,5 L', {'en': 'Aysu bottled water 0.5 L', 'ru': 'Aysu, бутылка 0,5 л'}),
    ('cup', 'Aysu bardak su', {'en': 'Aysu cup water', 'ru': 'Aysu, вода в стаканчиках'}),
    ('kizilay', 'Kızılay soda (maden suyu)', {'en': 'Kızılay mineral water (soda)', 'ru': 'Минеральная вода Kızılay (сода)'}),
    ('beypazari', 'Beypazarı soda (maden suyu)', {'en': 'Beypazarı mineral water (soda)', 'ru': 'Минеральная вода Beypazarı (сода)'}),
]
DEFAULT_PRODUCT = {'home': 'gas_home', 'gas': 'gas_home', 'water': 'aysu', 'aysu': 'aysu', 'madran': 'madran', 'hayat': 'hayat', 'kizilay': 'kizilay', 'beypazari': 'beypazari', 'contact': 'gas_home'}

BRAND_COLORS = {'aysu': ('#0a84b8', '#0a6a8a'), 'madran': ('#3a8fc4', '#1f6996'), 'hayat': ('#2f6fd6', '#1d4fa3'), 'kizilay': ('#4a9fd0', '#1f6a96'), 'beypazari': ('#1c7cc0', '#13588a')}
BRAND_NAME = {'aysu': 'Aysu', 'madran': 'Madran', 'hayat': 'Hayat', 'kizilay': 'Kızılay', 'beypazari': 'Beypazarı'}

UI = {
    'tr': {
        'locale': 'tr_TR', 'lang_name': 'Türkçe', 'short': 'TR',
        'skip': 'İçeriğe geç', 'menu': 'Menü', 'tagline': 'Tüp ve Su Bayii · Alanya',
        'nav_home': 'Ana Sayfa', 'nav_gas': f'{GAS} Tüp', 'nav_water': 'Su', 'nav_all_water': 'Tüm sular', 'nav_contact': 'İletişim',
        'call': 'Hemen Ara', 'wa': 'WhatsApp', 'wa_order': "WhatsApp'tan Sipariş", 'open': '7/24 açık', 'city': 'Alanya / Antalya',
        'more': 'Detaylı bilgi →', 'order_btn': 'Sipariş ver',
        'gsm': 'Cep · Sipariş', 'fixed': 'Sabit hat', 'wa_l': 'WhatsApp',
        'steps_k': 'Nasıl çalışır?', 'steps_h': '3 adımda sipariş',
        'steps': [('Arayın ya da yazın', f'{TEL_GSM} numarasını arayın veya WhatsApp’tan mesaj atın.'),
                  ('Ürünü ve adresi söyleyin', 'Tüp mü su mu, kaç adet, hangi adres; hepsi bu kadar.'),
                  ('Kapınıza getirelim', 'Siparişiniz Alanya’daki evinize ya da işyerinize teslim edilir.')],
        'why_k': 'Neden Alanyam Ticaret?', 'why_h': 'Alanya’da güvenilir tüp ve su bayii',
        'why': [('clock', '7/24 hizmet', 'Gece gündüz, hafta sonu ve bayramlarda sipariş alıyoruz.'),
                ('truck', 'Kapıya teslim', 'Ev ve işyerinize, Alanya genelinde teslimat.'),
                ('shield', 'Kurumsal markalar', f'{GAS} tüp; Aysu, Madran, Hayat su ve Kızılay, Beypazarı soda.'),
                ('home', '1983’ten bugüne', 'Alanya’da yıllardır tüp ve su ihtiyacına çözüm.')],
        'brands_k': 'Markalarımız', 'brands_h': 'Tüp ve su markalarımız', 'brands_sub': {'gas': 'Tüp gaz', 'aysu': 'Damacana, pet, bardak', 'madran': 'Damacana su', 'hayat': 'Damacana su', 'kizilay': 'Maden suyu (soda)', 'beypazari': 'Maden suyu (soda)'},
        'order_k': 'WhatsApp sipariş', 'order_h': 'Formu doldurun, WhatsApp’tan gönderin',
        'order_p': 'Ürünü ve adresinizi yazın; mesajınız hazır olarak WhatsApp’ta açılır, siz yalnızca “Gönder”e basarsınız.',
        'order_ticks': ['Kayıt ya da üyelik yok', 'Mesaj doğrudan bayiye gider', 'Gece de sipariş verebilirsiniz'],
        'f_product': 'Ürün', 'f_qty': 'Adet', 'f_name': 'Adınız (isteğe bağlı)', 'f_addr': 'Teslimat adresi', 'f_addr_ph': 'Mahalle, sokak, bina no, daire',
        'f_note': 'Not (isteğe bağlı)', 'f_note_ph': 'Örn: kapı kodu, boş tüp/damacana var', 'f_send': 'WhatsApp ile gönder',
        'f_small': f'WhatsApp açılmazsa {TEL_GSM} numarasını arayın.',
        'faq_k': 'Sık sorulan sorular', 'faq_h': 'Merak edilenler',
        'cta_h': 'Tüpünüz ya da suyunuz mu bitti?', 'cta_p': 'Bir telefon uzağınızdayız. 7/24 arayın, kapınıza getirelim.',
        'f_about': 'Alanya’da İpragaz tüp ve damacana su bayii. 7/24 sipariş, kapıya teslim.'.replace('İpragaz', GAS),
        'f_pages': 'Sayfalar', 'f_contact': 'İletişim', 'f_lang': 'Dil', 'rights': 'Tüm hakları saklıdır.',
        'crumb_home': 'Ana Sayfa', 'sizes': 'Seçenekler', 'other_waters': 'Diğer sular', 'ask': 'Telefonda sorun',
    },
    'en': {
        'locale': 'en_US', 'lang_name': 'English', 'short': 'EN',
        'skip': 'Skip to content', 'menu': 'Menu', 'tagline': 'Gas & Water Dealer · Alanya',
        'nav_home': 'Home', 'nav_gas': f'{GAS} Gas', 'nav_water': 'Water', 'nav_all_water': 'All water brands', 'nav_contact': 'Contact',
        'call': 'Call now', 'wa': 'WhatsApp', 'wa_order': 'Order on WhatsApp', 'open': 'Open 24/7', 'city': 'Alanya / Antalya',
        'more': 'Learn more →', 'order_btn': 'Order now',
        'gsm': 'Mobile · Orders', 'fixed': 'Landline', 'wa_l': 'WhatsApp',
        'steps_k': 'How it works', 'steps_h': 'Order in 3 steps',
        'steps': [('Call or message', f'Call {TEL_GSM} or send us a WhatsApp message.'),
                  ('Tell us what and where', 'Gas or water, how many, and your address. That’s it.'),
                  ('We deliver to your door', 'Your order is delivered to your home or business in Alanya.')],
        'why_k': 'Why Alanyam Ticaret?', 'why_h': 'A trusted gas and water dealer in Alanya',
        'why': [('clock', '24/7 service', 'We take orders day and night, on weekends and holidays.'),
                ('truck', 'Door delivery', 'Delivered to homes and businesses across Alanya.'),
                ('shield', 'Trusted brands', f'{GAS} gas; Aysu, Madran, Hayat water; Kızılay and Beypazarı soda.'),
                ('home', 'Since 1983', 'Serving Alanya’s gas and water needs for decades.')],
        'brands_k': 'Our brands', 'brands_h': 'Gas and water brands we deliver', 'brands_sub': {'gas': 'Bottled gas (LPG)', 'aysu': 'Jugs, bottles, cups', 'madran': 'Water jug', 'hayat': 'Water jug', 'kizilay': 'Mineral water (soda)', 'beypazari': 'Mineral water (soda)'},
        'order_k': 'WhatsApp order', 'order_h': 'Fill in the form, send it on WhatsApp',
        'order_p': 'Choose the product and enter your address. Your message opens ready in WhatsApp, written in Turkish for the dealer — you just tap “Send”.',
        'order_ticks': ['No sign-up needed', 'Message goes straight to the dealer', 'Order even at night'],
        'f_product': 'Product', 'f_qty': 'Qty', 'f_name': 'Your name (optional)', 'f_addr': 'Delivery address', 'f_addr_ph': 'Neighbourhood, street, building, flat',
        'f_note': 'Note (optional)', 'f_note_ph': 'E.g. door code, empty cylinder/jug to return', 'f_send': 'Send via WhatsApp',
        'f_small': f'If WhatsApp doesn’t open, call {TEL_GSM}.',
        'faq_k': 'FAQ', 'faq_h': 'Frequently asked questions',
        'cta_h': 'Out of gas or water?', 'cta_p': 'We’re just a call away. Call 24/7 and we’ll bring it to your door.',
        'f_about': f'{GAS} gas cylinder and water jug dealer in Alanya. Orders 24/7, delivered to your door.',
        'f_pages': 'Pages', 'f_contact': 'Contact', 'f_lang': 'Language', 'rights': 'All rights reserved.',
        'crumb_home': 'Home', 'sizes': 'Options', 'other_waters': 'Other water brands', 'ask': 'Ask by phone',
    },
    'ru': {
        'locale': 'ru_RU', 'lang_name': 'Русский', 'short': 'RU',
        'skip': 'Перейти к содержанию', 'menu': 'Меню', 'tagline': 'Газ и вода · Аланья',
        'nav_home': 'Главная', 'nav_gas': f'Газ {GAS}', 'nav_water': 'Вода', 'nav_all_water': 'Вся вода', 'nav_contact': 'Контакты',
        'call': 'Позвонить', 'wa': 'WhatsApp', 'wa_order': 'Заказ в WhatsApp', 'open': 'Круглосуточно', 'city': 'Аланья / Анталья',
        'more': 'Подробнее →', 'order_btn': 'Заказать',
        'gsm': 'Мобильный · Заказы', 'fixed': 'Городской', 'wa_l': 'WhatsApp',
        'steps_k': 'Как заказать', 'steps_h': 'Заказ за 3 шага',
        'steps': [('Позвоните или напишите', f'Позвоните по номеру {TEL_GSM} или напишите в WhatsApp.'),
                  ('Укажите товар и адрес', 'Газ или вода, сколько штук и ваш адрес — этого достаточно.'),
                  ('Доставим к двери', 'Заказ привезём домой или в офис в Аланье.')],
        'why_k': 'Почему Alanyam Ticaret?', 'why_h': 'Надёжный поставщик газа и воды в Аланье',
        'why': [('clock', 'Круглосуточно', 'Принимаем заказы днём и ночью, в выходные и праздники.'),
                ('truck', 'Доставка до двери', 'Привозим в квартиры, дома и офисы по всей Аланье.'),
                ('shield', 'Надёжные бренды', f'Газ {GAS}; вода Aysu, Madran, Hayat; минеральная вода Kızılay и Beypazarı.'),
                ('home', 'С 1983 года', 'Много лет обеспечиваем Аланью газом и водой.')],
        'brands_k': 'Наши бренды', 'brands_h': 'Газ и вода, которые мы привозим', 'brands_sub': {'gas': 'Баллонный газ', 'aysu': 'Бутыли, бутылки, стаканчики', 'madran': 'Бутыль 19 л', 'hayat': 'Бутыль 19 л', 'kizilay': 'Минеральная вода', 'beypazari': 'Минеральная вода'},
        'order_k': 'Заказ в WhatsApp', 'order_h': 'Заполните форму и отправьте в WhatsApp',
        'order_p': 'Выберите товар и укажите адрес. Сообщение откроется в WhatsApp уже готовым — на турецком языке, чтобы продавцу было понятно. Вам останется нажать «Отправить».',
        'order_ticks': ['Без регистрации', 'Сообщение сразу уходит продавцу', 'Можно заказать и ночью'],
        'f_product': 'Товар', 'f_qty': 'Кол-во', 'f_name': 'Ваше имя (необязательно)', 'f_addr': 'Адрес доставки', 'f_addr_ph': 'Район (махалле), улица, дом, квартира',
        'f_note': 'Комментарий (необязательно)', 'f_note_ph': 'Напр.: код двери, есть пустой баллон/бутыль', 'f_send': 'Отправить в WhatsApp',
        'f_small': f'Если WhatsApp не открывается, позвоните: {TEL_GSM}.',
        'faq_k': 'Вопросы и ответы', 'faq_h': 'Частые вопросы',
        'cta_h': 'Закончился газ или вода?', 'cta_p': 'Мы на связи круглосуточно. Позвоните — и мы привезём заказ к вашей двери.',
        'f_about': f'Газовые баллоны {GAS} и питьевая вода в бутылях 19 л в Аланье. Круглосуточно, с доставкой до двери.',
        'f_pages': 'Страницы', 'f_contact': 'Контакты', 'f_lang': 'Язык', 'rights': 'Все права защищены.',
        'crumb_home': 'Главная', 'sizes': 'Варианты', 'other_waters': 'Другая вода', 'ask': 'Уточните по телефону',
    },
}

# ---------- Marka metinleri ----------
BRAND = {
    'aysu': {
        'tr': 'Aysu, doğallığını Dedegöl Dağı eteklerindeki kaynağından alan bir doğal kaynak suyudur. Alanyam Ticaret’te Aysu’nun 19 litre damacanası, 1,5 ve 0,5 litre pet şişeleri ve bardak suyu bulunur.',
        'en': 'Aysu is a natural spring water sourced from the foothills of Mount Dedegöl. At Alanyam Ticaret you can order Aysu in 19-litre jugs, 1.5 and 0.5-litre PET bottles and cup water.',
        'ru': 'Aysu — природная родниковая вода из источника у подножия горы Дедегёль. В Alanyam Ticaret можно заказать Aysu в бутылях 19 л, в бутылках 1,5 и 0,5 л, а также воду в стаканчиках.',
        'sizes': ['19 L', '1,5 L', '0,5 L', 'Bardak'],
    },
    'madran': {
        'tr': 'Madran, Aydın’ın Bozdoğan ilçesindeki Madran Dağı yöresinin kaynaklarından gelen bir sudur. Alanyam Ticaret’te Madran’ın 19 litre damacanası ile 1,5 litre ve 0,5 litre şişeleri bulunur.',
        'en': 'Madran water comes from springs in the Madran Mountain area of Bozdoğan, Aydın. At Alanyam Ticaret you can order Madran in 19-litre jugs as well as 1.5-litre and 0.5-litre bottles.',
        'ru': 'Вода Madran поступает из источников в районе горы Мадран (Боздоган, провинция Айдын). В Alanyam Ticaret можно заказать Madran в бутылях 19 л, а также в бутылках 1,5 л и 0,5 л.',
        'sizes': ['19 L', '1,5 L', '0,5 L'],
    },
    'hayat': {
        'tr': 'Hayat, Danone’nin Türkiye’deki su markalarından biridir. Alanyam Ticaret, Hayat Su 19 litre damacanayı Alanya’da evinize ve işyerinize getirir; şişe seçenekleri için telefonda bilgi alabilirsiniz.',
        'en': 'Hayat is one of Danone’s water brands in Türkiye. Alanyam Ticaret delivers Hayat 19-litre jugs to homes and businesses in Alanya; ask us by phone about bottle sizes.',
        'ru': 'Hayat — один из брендов воды компании Danone в Турции. Alanyam Ticaret доставляет бутыли Hayat 19 л в квартиры, дома и офисы Аланьи; о бутылках меньшего объёма спрашивайте по телефону.',
        'sizes': ['19 L'],
    },
}

BRAND['kizilay'] = {
    'tr': 'Kızılay Maden Suyu’nun hikâyesi, Atatürk’ün 1926’da Afyonkarahisar Gazlıgöl’deki kaynağı Türk Kızılay’a bağışlamasıyla başlar. Alanyam Ticaret, Kızılay maden suyunu (soda) Alanya’da kapınıza getirir; çeşit ve koli seçenekleri için telefonda bilgi alabilirsiniz.',
    'en': 'The story of Kızılay mineral water began in 1926, when Atatürk donated the Gazlıgöl spring in Afyonkarahisar to the Turkish Red Crescent (Kızılay). Alanyam Ticaret delivers Kızılay mineral water (soda) in Alanya; ask us by phone about varieties and cases.',
    'ru': 'История минеральной воды Kızılay началась в 1926 году, когда Ататюрк передал источник Газлыгёль в Афьонкарахисаре Турецкому Красному Полумесяцу (Kızılay). Alanyam Ticaret доставляет минеральную воду Kızılay (соду) по Аланье; о видах и упаковках спрашивайте по телефону.',
    'sizes': ['200 ml'],
}
BRAND['beypazari'] = {
    'tr': 'Beypazarı maden suyu, adını aldığı Ankara’nın Beypazarı ilçesinden gelen bir doğal mineralli sudur. Alanyam Ticaret, Beypazarı sodayı Alanya’da kapınıza getirir; çeşit ve koli seçenekleri için telefonda bilgi alabilirsiniz.',
    'en': 'Beypazarı is a natural mineral water from the Beypazarı district of Ankara, which gives it its name. Alanyam Ticaret delivers Beypazarı soda in Alanya; ask us by phone about varieties and cases.',
    'ru': 'Beypazarı — природная минеральная вода из района Бейпазары (Анкара), давшего ей название. Alanyam Ticaret доставляет соду Beypazarı по Аланье; о видах и упаковках спрашивайте по телефону.',
    'sizes': [],
}

# ---------- Sayfalar ----------
P = {'tr': {}, 'en': {}, 'ru': {}}

# ===== TÜRKÇE =====
P['tr']['home'] = dict(
    title='Alanya Tüp ve Su Bayii | İpragaz Tüp, Damacana Su 7/24 | Alanyam Ticaret',
    desc=f'Alanya’da İpragaz tüp, Aysu, Madran, Hayat damacana su ve Kızılay, Beypazarı soda siparişi. 7/24 kapınıza teslim. Telefon/WhatsApp: {TEL_GSM}',
    crumb='Ana Sayfa', eyebrow='Alanya · 7/24 tüp ve su',
    h1='Alanya’da tüp ve damacana su <span>kapınıza kadar</span>',
    lead='Alanyam Ticaret olarak İpragaz tüp, Aysu, Madran ve Hayat damacana su, Aysu pet ve bardak su ile Kızılay ve Beypazarı soda siparişlerinizi gece gündüz evinize ve işyerinize getiriyoruz.',
    chips=['7/24 sipariş', 'Ev ve işyerine teslim', 'WhatsApp’tan sipariş'], badge=('7/24', 'Gece gündüz sipariş'), art='mix',
    prod_k='Ürünlerimiz', prod_h='Tüp ve su, <span class="hl">tek numaradan</span>',
    prod_p='Mutfak tüpünüz ya da damacana suyunuz bittiğinde aramanız yeterli. Ürünü seçin, adresinizi söyleyin, kapınıza getirelim.',
    info_k='Hakkımızda', info_h='Alanya’nın tüp ve su bayii',
    info_p=['Alanyam Ticaret, Alanya’da ev ve işyerlerine tüp gaz ve damacana su dağıtan yerel bir bayidir. 1983’ten bugüne Alanya’da hizmet veriyoruz.',
            'Tüpte İpragaz; suda Aysu, Madran ve Hayat; sodada Kızılay ve Beypazarı ile çalışıyoruz. Düğün, toplantı ve davetler için Aysu pet ve bardak su siparişi de alıyoruz.'],
    info_ticks=['İpragaz tüp bayisi', 'Aysu, Madran ve Hayat 19 L damacana', 'Aysu pet su (0,5 L, 1,5 L) ve bardak su', 'Kızılay ve Beypazarı soda', 'Özel günler için toplu su siparişi'],
    faq=[('Alanya’da gece tüp siparişi verebilir miyim?', f'Evet. Alanyam Ticaret 7/24 sipariş alır. Gece de {TEL_GSM} numarasını arayabilir ya da WhatsApp’tan yazabilirsiniz.'),
         ('WhatsApp’tan nasıl sipariş veririm?', f'Sayfadaki sipariş formunda ürünü, adedi ve adresinizi yazıp “WhatsApp ile gönder”e basın. Mesaj hazır olarak {TEL_WA} numarasına açılır; siz yalnızca gönderirsiniz.'),
         ('Hangi su ve soda markalarını getiriyorsunuz?', 'Aysu, Madran ve Hayat 19 litre damacana; Aysu pet su (0,5 ve 1,5 litre) ve bardak su; Kızılay ve Beypazarı soda getiriyoruz.'),
         ('Alanya’nın hangi bölgelerine teslimat yapıyorsunuz?', 'Alanya genelinde ev ve işyerlerine teslimat yapıyoruz. Bulunduğunuz mahalleyi sipariş sırasında söylemeniz yeterli; teslim süresini telefonda netleştiririz.'),
         ('Güncel fiyatları nereden öğrenebilirim?', 'Tüp ve su fiyatları dönemsel olarak değiştiği için güncel fiyatı telefonda ya da WhatsApp’tan sorabilirsiniz.')],
)
P['tr']['gas'] = dict(
    title='Alanya İpragaz Tüp Bayi | 7/24 Tüp Siparişi | Alanyam Ticaret',
    desc=f'Alanya’da İpragaz tüp siparişi: ev ve işyeri tüpleri 7/24 kapınıza. Telefon veya WhatsApp ile hemen sipariş verin: {TEL_GSM}',
    crumb='İpragaz Tüp', eyebrow='Alanya · İpragaz tüp bayi',
    h1='Alanya İpragaz tüp, <span>7/24 kapınızda</span>',
    lead='Tüpünüz yemeğin ortasında mı bitti? Alanyam Ticaret, Alanya’da İpragaz tüp siparişinizi gece gündüz adresinize getirir. Arayın ya da WhatsApp’tan yazın.',
    chips=['İpragaz tüp', 'Ev ve işyeri', 'Gece de sipariş'], badge=('7/24', 'Tüp siparişi'), art='cyl',
    prod_k='Tüp siparişi', prod_h='Eviniz ve işyeriniz için <span class="hl">İpragaz tüp</span>',
    prod_p='Hangi tüpe ihtiyacınız olduğunu bilmiyorsanız sorun yok; telefonda kullanım yerinizi söyleyin, uygun tüpü birlikte belirleyelim.',
    cards=[('home', 'Ev tipi mutfak tüpü', 'Evlerde ocak ve fırın için kullanılan mutfak tüpü. Bittiğinde arayın, dolusunu getirelim.'),
           ('flame', 'İşyeri tüpleri', 'Restoran, kafe, otel ve işyerleri için tüp. İhtiyacınıza uygun tüpü telefonda birlikte seçelim.'),
           ('truck', '7/24 kapıya teslim', 'Alanya genelinde ev ve işyerinize gece gündüz teslimat.')],
    info_k='Marka', info_h='İpragaz hakkında',
    info_p=['İpragaz, Türkiye’de 1961’den bu yana LPG dağıtımı yapan ve 1999’dan beri SHV Energy grubunun parçası olan köklü bir şirkettir.',
            'Alanyam Ticaret, Alanya’da İpragaz tüplerini ev ve işyerlerine ulaştırır. Tüp siparişinizi telefonla ya da WhatsApp’tan 7/24 verebilirsiniz.'],
    info_ticks=['Alanya İpragaz tüp siparişi', 'Ev ve işyeri tüpleri', 'Gece, hafta sonu ve bayramda teslimat'],
    safety_h='Tüp güvenliği için 6 basit kural',
    safety=['Tüpü dik tutun; güneşten, sobadan ve ısı kaynaklarından uzak, havalanan bir yerde kullanın.',
            'Kaçak kontrolünü sabunlu suyla yapın; kabarcık çıkıyorsa vanayı kapatın. Kontrol için asla ateş kullanmayın.',
            'Hortum ve kelepçeleri düzenli kontrol edin; çatlamış ya da sertleşmiş hortumu değiştirin.',
            'Ocağı kullanmadığınızda ve evden çıkarken tüp vanasını kapatın.',
            'Gaz kokusu alırsanız elektrik düğmelerine dokunmayın, vanayı kapatın, kapı ve pencereleri açın.',
            'Acil durumda 112’yi arayın.'],
    faq=[('Alanya’da İpragaz tüp siparişi nasıl verilir?', f'{TEL_GSM} numarasını arayın ya da sayfadaki formla WhatsApp’tan sipariş verin. Adresinizi ve tüp türünü söylemeniz yeterli.'),
         ('Gece tüp getiriyor musunuz?', 'Evet, 7/24 sipariş alıyoruz; gece, hafta sonu ve bayramlarda da arayabilirsiniz.'),
         ('Boş tüpümü ne yapacağım?', 'Tüp değişimi ve depozito koşullarını sipariş sırasında telefonda öğrenebilirsiniz. Teslimatta boş tüpünüzü hazır bulundurmanız işi hızlandırır.'),
         ('Gaz kokusu alırsam ne yapmalıyım?', 'Elektrik düğmelerine dokunmadan tüp vanasını kapatın, ortamı havalandırın ve gerekirse 112’yi arayın. Tüp ya da bağlantıyla ilgili sorularınız için bizi arayabilirsiniz.')],
)
P['tr']['water'] = dict(
    title='Alanya Su ve Soda Siparişi | Aysu, Madran, Hayat, Kızılay, Beypazarı | Alanyam Ticaret',
    desc=f'Alanya’da Aysu, Madran, Hayat damacana su; Aysu pet ve bardak su; Kızılay ve Beypazarı soda siparişi. 7/24 kapınıza teslim. WhatsApp: {TEL_WA}',
    crumb='Su', eyebrow='Alanya · damacana su',
    h1='Alanya su ve soda: <span>Aysu, Madran, Hayat, Kızılay, Beypazarı</span>',
    lead='Damak tadınıza uygun suyu seçin, kapınıza getirelim. Alanyam Ticaret, Alanya’da 19 litre damacana, Aysu pet ve bardak su ile Kızılay ve Beypazarı soda siparişlerinizi 7/24 teslim eder.',
    chips=['19 L damacana', 'Aysu pet ve bardak su', 'Kızılay ve Beypazarı soda'], badge=('5', 'marka'), art='jugs',
    prod_k='Su markalarımız', prod_h='Hangi suyu <span class="hl">tercih edersiniz?</span>',
    prod_p='Her markanın kendi sayfasında seçenekleri ve sipariş bilgisini bulabilirsiniz.',
    extra_card=('party', 'Aysu pet ve bardak su', 'Aysu 0,5 L ve 1,5 L pet su ile bardak su; düğün, toplantı ve davetler için toplu sipariş.'),
    info_k='Pratik bilgi', info_h='Damacana su nasıl saklanır?',
    info_p=['Damacana suyun tadını ve tazeliğini korumak için birkaç basit kurala dikkat etmek yeterli.'],
    info_ticks=['Damacanayı doğrudan güneş almayan, serin ve temiz bir yerde saklayın.', 'Açtığınız damacanayı kısa sürede tüketin.',
                'Pompa ya da sebili düzenli olarak temizleyin.', 'Damacanayı kimyasal ve kokulu ürünlerin yanında tutmayın.'],
    faq=[('Alanya’da hangi damacana su markalarını getiriyorsunuz?', 'Aysu, Madran ve Hayat Su 19 litre damacana getiriyoruz. Aysu ve Madran’ın 1,5 ve 0,5 litre şişeleri de var.'),
         ('Damacana su siparişi nasıl verilir?', f'{TEL_GSM} numarasını arayın ya da sayfadaki formla WhatsApp’tan sipariş verin. Marka, adet ve adres yeterli.'),
         ('Toplu su siparişi alıyor musunuz?', 'Evet; düğün, toplantı ve davetler için şişe su siparişi alıyoruz. Miktarı önceden telefonda bildirmeniz yeterli.'),
         ('Boş damacana ne olacak?', 'Boş damacana ve depozito koşullarını sipariş sırasında telefonda öğrenebilirsiniz.')],
)


def _brand_tr(k):
    n = BRAND_NAME[k]
    return dict(
        title=f'Alanya {n} Damacana Su Siparişi | 7/24 Teslim | Alanyam Ticaret',
        desc=f'Alanya’da {n} 19 L damacana su siparişi' + (' ile 0,5 L ve 1,5 L şişe su' if k != 'hayat' else '') + '. Kapınıza 7/24 teslim; arayın ya da WhatsApp’tan sipariş verin.',
        crumb=n, eyebrow=f'Alanya · {n} su',
        h1=f'Alanya {n} damacana su, <span>kapınıza</span>',
        lead=f'{n} suyunu Alanya’da evinize ve işyerinize getiriyoruz. ' + ('19 litre damacana ya da şişe su; siz seçin, biz teslim edelim.' if k != 'hayat' else '19 litre damacanayı 7/24 sipariş verebilirsiniz.'),
        chips=[f'{n} 19 L damacana', '7/24 sipariş', 'Kapıya teslim'], badge=('19 L', 'damacana'), art='jug',
        prod_k='Seçenekler', prod_h=f'{n} <span class="hl">su seçenekleri</span>',
        prod_p='Kaç adet istediğinizi söyleyin; ev ve işyeri siparişlerini aynı gün içinde planlıyoruz.' if False else 'Kaç adet istediğinizi söyleyin, siparişinizi adresinize getirelim.',
        info_k='Marka', info_h=f'{n} hakkında', info_p=[BRAND[k]['tr']],
        info_ticks=[f'Alanya {n} damacana siparişi', '7/24 telefon ve WhatsApp', 'Ev ve işyerine teslim'],
        faq=[(f'Alanya’da {n} damacana su siparişi nasıl verilir?', f'{TEL_GSM} numarasını arayın ya da sayfadaki formdan WhatsApp’la sipariş verin. Adet ve adres yeterli.'),
             (f'{n} damacana kaç litre?', f'{n} damacana 19 litredir. ' + ('1,5 ve 0,5 litre şişe seçenekleri de var.' if k != 'hayat' else 'Şişe seçenekleri için telefonda bilgi alabilirsiniz.')),
             (f'{n} suyu gece de getiriyor musunuz?', 'Evet, 7/24 sipariş alıyoruz.'),
             ('Başka marka su da var mı?', 'Evet; Aysu, Madran ve Hayat Su getiriyoruz. Diğer markaların sayfalarına aşağıdan ulaşabilirsiniz.')],
    )


for _k in ['aysu', 'madran', 'hayat']:
    P['tr'][_k] = _brand_tr(_k)

P['tr']['contact'] = dict(
    title='İletişim ve Sipariş | Alanyam Ticaret – Alanya Tüp ve Su',
    desc=f'Alanyam Ticaret iletişim: {TEL_GSM}, {TEL_FIX}, WhatsApp {TEL_WA}. Alanya’da 7/24 tüp ve su siparişi.',
    crumb='İletişim', eyebrow='Alanya · 7/24 iletişim',
    h1='Bize ulaşın, <span>siparişiniz yola çıksın</span>',
    lead='Tüp ve su siparişleriniz, soru ve önerileriniz için 7/24 arayabilir ya da WhatsApp’tan yazabilirsiniz.',
    chips=['7/24 açık', '3 iletişim hattı', 'WhatsApp sipariş'], badge=('7/24', 'açığız'), art='mix',
    faq=[('Hangi numaradan sipariş verebilirim?', f'Sipariş için {TEL_GSM} veya sabit hattımız {TEL_FIX} numarasını arayabilir, {TEL_WA} numarasına WhatsApp’tan yazabilirsiniz.'),
         ('Çalışma saatleriniz nedir?', 'Alanyam Ticaret 7/24 hizmet verir; gece, hafta sonu ve bayramlarda da sipariş alırız.'),
         ('Nerede hizmet veriyorsunuz?', 'Alanya genelinde ev ve işyerlerine tüp ve su teslimatı yapıyoruz.')],
)

# ===== ENGLISH =====
P['en']['home'] = dict(
    title='Gas & Water Delivery in Alanya 24/7 | İpragaz, Water Jugs | Alanyam Ticaret',
    desc=f'Order İpragaz gas cylinders and Aysu, Madran, Hayat water jugs in Alanya. Delivered to your door 24/7. Call or WhatsApp: {TEL_GSM}',
    crumb='Home', eyebrow='Alanya · gas & water 24/7',
    h1='Gas cylinders and drinking water in Alanya, <span>delivered to your door</span>',
    lead='Alanyam Ticaret delivers İpragaz gas cylinders, Aysu, Madran and Hayat 19-litre water jugs, Aysu bottled and cup water, and Kızılay and Beypazarı mineral water to homes and businesses in Alanya, day and night.',
    chips=['Orders 24/7', 'Homes & businesses', 'Order on WhatsApp'], badge=('24/7', 'Day & night orders'), art='mix',
    prod_k='Our products', prod_h='Gas and water, <span class="hl">one number</span>',
    prod_p='When your kitchen gas or drinking water runs out, just call. Choose the product, give us your address, and we’ll bring it to your door.',
    info_k='About us', info_h='Alanya’s gas and water dealer',
    info_p=['Alanyam Ticaret is a local dealer delivering bottled gas and drinking water to homes and businesses in Alanya. We have been serving Alanya since 1983.',
            'For gas we work with İpragaz; for water with Aysu, Madran and Hayat. We also take bulk bottled-water orders for weddings, meetings and special events.'],
    info_ticks=['İpragaz gas cylinder dealer', 'Aysu, Madran and Hayat 19 L jugs', 'Aysu bottled (0.5 L, 1.5 L) and cup water', 'Kızılay and Beypazarı mineral water', 'Bulk water for events'],
    faq=[('Can I order a gas cylinder at night in Alanya?', f'Yes. Alanyam Ticaret takes orders 24/7. Call {TEL_GSM} or send a WhatsApp message any time.'),
         ('How do I order on WhatsApp?', f'Fill in the order form on this page and tap “Send via WhatsApp”. The message opens ready (in Turkish) to {TEL_WA}; you just send it.'),
         ('Do you speak English?', 'The easiest way is to order with the WhatsApp form: it writes your order in Turkish for the dealer, so there is no language barrier.'),
         ('Which water brands do you deliver?', 'Aysu, Madran and Hayat 19-litre jugs, plus 0.5 and 1.5-litre bottled water.'),
         ('How much does it cost?', 'Gas and water prices change from time to time, so please ask for the current price by phone or WhatsApp.')],
)
P['en']['gas'] = dict(
    title='İpragaz Gas Cylinder Delivery in Alanya 24/7 | Alanyam Ticaret',
    desc=f'Order an İpragaz gas cylinder in Alanya: home and business cylinders delivered 24/7. Call or WhatsApp: {TEL_GSM}',
    crumb='İpragaz Gas', eyebrow='Alanya · İpragaz dealer',
    h1='İpragaz gas cylinders in Alanya, <span>24/7 to your door</span>',
    lead='Gas ran out in the middle of cooking? Alanyam Ticaret delivers your İpragaz gas cylinder anywhere in Alanya, day or night. Call us or send a WhatsApp message.',
    chips=['İpragaz cylinders', 'Homes & businesses', 'Night orders'], badge=('24/7', 'Gas orders'), art='cyl',
    prod_k='Gas orders', prod_h='<span class="hl">İpragaz</span> for your home and business',
    prod_p='Not sure which cylinder you need? Tell us where you use it and we’ll help you choose.',
    cards=[('home', 'Kitchen gas cylinder', 'The standard household cylinder for hobs and ovens. Call when it runs out and we’ll bring a full one.'),
           ('flame', 'Cylinders for businesses', 'For restaurants, cafés, hotels and shops. We’ll pick the right cylinder with you by phone.'),
           ('truck', '24/7 door delivery', 'Delivery to homes and businesses across Alanya, day and night.')],
    info_k='Brand', info_h='About İpragaz',
    info_p=['İpragaz has been distributing LPG in Türkiye since 1961 and has been part of the SHV Energy group since 1999.',
            'Alanyam Ticaret delivers İpragaz cylinders to homes and businesses in Alanya. You can order by phone or WhatsApp 24/7.'],
    info_ticks=['İpragaz gas delivery in Alanya', 'Home and business cylinders', 'Nights, weekends and holidays'],
    safety_h='6 simple gas cylinder safety rules',
    safety=['Keep the cylinder upright, in a ventilated place away from sun, heaters and other heat sources.',
            'Check for leaks with soapy water; if bubbles appear, close the valve. Never use a flame to check.',
            'Inspect the hose and clamps regularly; replace a cracked or hardened hose.',
            'Close the cylinder valve when the cooker is not in use and when you leave home.',
            'If you smell gas, don’t touch light switches; close the valve and open doors and windows.',
            'In an emergency, call 112.'],
    faq=[('How do I order an İpragaz cylinder in Alanya?', f'Call {TEL_GSM} or use the WhatsApp form on this page. Just tell us your address and which cylinder you need.'),
         ('Do you deliver gas at night?', 'Yes, we take orders 24/7, including nights, weekends and holidays.'),
         ('What about my empty cylinder?', 'Ask about cylinder exchange and deposit terms when you order. Having your empty cylinder ready speeds up delivery.'),
         ('What should I do if I smell gas?', 'Don’t touch electrical switches; close the cylinder valve, ventilate the room and call 112 if needed.')],
)
P['en']['water'] = dict(
    title='Water & Soda Delivery in Alanya | Aysu, Madran, Hayat, Kızılay, Beypazarı | Alanyam Ticaret',
    desc=f'Order Aysu, Madran and Hayat 19 L water jugs and 0.5 L / 1.5 L bottled water in Alanya. Delivered 24/7. WhatsApp: {TEL_WA}',
    crumb='Water', eyebrow='Alanya · drinking water',
    h1='Water and soda in Alanya: <span>Aysu, Madran, Hayat, Kızılay, Beypazarı</span>',
    lead='Choose the water you like and we’ll bring it to your door. Alanyam Ticaret delivers 19-litre jugs and bottled water across Alanya, 24/7.',
    chips=['19 L jugs', 'Aysu bottles & cups', 'Kızılay & Beypazarı soda'], badge=('5', 'brands'), art='jugs',
    prod_k='Our water brands', prod_h='Which water <span class="hl">do you prefer?</span>',
    prod_p='Each brand has its own page with sizes and ordering details.',
    extra_card=('party', 'Aysu bottles & cup water', 'Aysu 0.5 L and 1.5 L PET bottles and cup water; bulk orders for weddings, meetings and parties.'),
    info_k='Good to know', info_h='How to store a water jug',
    info_p=['A few simple habits keep your water fresh and tasting good.'],
    info_ticks=['Store the jug in a cool, clean place out of direct sunlight.', 'Finish an opened jug within a short time.',
                'Clean your pump or water dispenser regularly.', 'Keep jugs away from chemicals and strong-smelling products.'],
    faq=[('Which water brands do you deliver in Alanya?', 'Aysu, Madran and Hayat 19-litre jugs. Aysu and Madran also come in 1.5 and 0.5-litre bottles.'),
         ('How do I order water?', f'Call {TEL_GSM} or use the WhatsApp form on this page: brand, quantity and address are enough.'),
         ('Do you take bulk orders?', 'Yes, we take bottled-water orders for weddings, meetings and events. Just let us know the quantity in advance.'),
         ('What about empty jugs?', 'Ask about empty-jug and deposit terms when you order.')],
)


def _brand_en(k):
    n = BRAND_NAME[k]
    return dict(
        title=f'{n} Water Jug Delivery in Alanya 24/7 | Alanyam Ticaret',
        desc=f'Order {n} 19 L water jugs' + (' and 0.5 L / 1.5 L bottles' if k != 'hayat' else '') + ' in Alanya. Delivered to your door 24/7. Call or WhatsApp.',
        crumb=n, eyebrow=f'Alanya · {n} water',
        h1=f'{n} water in Alanya, <span>delivered to your door</span>',
        lead=f'We deliver {n} water to homes and businesses in Alanya. ' + ('Jugs or bottles — you choose, we deliver.' if k != 'hayat' else 'Order 19-litre jugs 24/7.'),
        chips=[f'{n} 19 L jug', 'Orders 24/7', 'Door delivery'], badge=('19 L', 'jug'), art='jug',
        prod_k='Options', prod_h=f'{n} <span class="hl">water options</span>',
        prod_p='Tell us how many you need and we’ll bring them to your address.',
        info_k='Brand', info_h=f'About {n}', info_p=[BRAND[k]['en']],
        info_ticks=[f'{n} water delivery in Alanya', '24/7 phone and WhatsApp', 'Homes and businesses'],
        faq=[(f'How do I order {n} water in Alanya?', f'Call {TEL_GSM} or use the WhatsApp form on this page. Quantity and address are enough.'),
             (f'How big is a {n} jug?', f'A {n} jug holds 19 litres. ' + ('1.5 and 0.5-litre bottles are also available.' if k != 'hayat' else 'Ask us by phone about bottle sizes.')),
             (f'Do you deliver {n} at night?', 'Yes, we take orders 24/7.'),
             ('Do you have other brands?', 'Yes — Aysu, Madran and Hayat. You’ll find the other brands below.')],
    )


for _k in ['aysu', 'madran', 'hayat']:
    P['en'][_k] = _brand_en(_k)

P['en']['contact'] = dict(
    title='Contact & Orders | Alanyam Ticaret – Gas and Water in Alanya',
    desc=f'Contact Alanyam Ticaret: {TEL_GSM}, {TEL_FIX}, WhatsApp {TEL_WA}. Gas and water delivery in Alanya 24/7.',
    crumb='Contact', eyebrow='Alanya · contact 24/7',
    h1='Get in touch, <span>we’ll be on our way</span>',
    lead='Call or WhatsApp us 24/7 for gas and water orders, questions or feedback.',
    chips=['Open 24/7', '3 phone lines', 'WhatsApp orders'], badge=('24/7', 'open'), art='mix',
    faq=[('Which number should I call?', f'Call {TEL_GSM} or our landline {TEL_FIX}, or message {TEL_WA} on WhatsApp.'),
         ('What are your hours?', 'Alanyam Ticaret is open 24/7, including nights, weekends and holidays.'),
         ('Where do you deliver?', 'We deliver gas and water to homes and businesses across Alanya.')],
)

# ===== РУССКИЙ =====
P['ru']['home'] = dict(
    title='Доставка газа и воды в Аланье 24/7 | İpragaz, вода 19 л | Alanyam Ticaret',
    desc=f'Газовые баллоны İpragaz и вода Aysu, Madran, Hayat в бутылях 19 л с доставкой по Аланье круглосуточно. Звоните или пишите в WhatsApp: {TEL_GSM}',
    crumb='Главная', eyebrow='Аланья · газ и вода 24/7',
    h1='Газ и питьевая вода в Аланье <span>с доставкой до двери</span>',
    lead='Alanyam Ticaret привозит газовые баллоны İpragaz, воду Aysu, Madran и Hayat в бутылях 19 л, воду Aysu в бутылках и стаканчиках, а также минеральную воду Kızılay и Beypazarı — в квартиры, дома и офисы Аланьи, днём и ночью.',
    chips=['Заказ 24/7', 'Дома и офисы', 'Заказ в WhatsApp'], badge=('24/7', 'Заказы днём и ночью'), art='mix',
    prod_k='Наши товары', prod_h='Газ и вода <span class="hl">по одному номеру</span>',
    prod_p='Закончился газ на кухне или питьевая вода? Просто позвоните: выберите товар, назовите адрес — и мы привезём заказ к вашей двери.',
    info_k='О нас', info_h='Газ и вода в Аланье',
    info_p=['Alanyam Ticaret — местный поставщик баллонного газа и питьевой воды для домов и офисов в Аланье. Мы работаем в Аланье с 1983 года.',
            'Газ — İpragaz, вода — Aysu, Madran и Hayat. Также принимаем оптовые заказы воды в бутылках на свадьбы, встречи и праздники.'],
    info_ticks=['Газовые баллоны İpragaz', 'Вода Aysu, Madran и Hayat, бутыли 19 л', 'Aysu в бутылках (0,5 и 1,5 л) и стаканчиках', 'Минеральная вода Kızılay и Beypazarı', 'Оптовые заказы на мероприятия'],
    faq=[('Можно ли заказать газовый баллон ночью?', f'Да. Alanyam Ticaret принимает заказы круглосуточно. Звоните по номеру {TEL_GSM} или пишите в WhatsApp в любое время.'),
         ('Как заказать через WhatsApp?', f'Заполните форму заказа на этой странице и нажмите «Отправить в WhatsApp». Сообщение откроется готовым (на турецком) для номера {TEL_WA} — вам останется его отправить.'),
         ('Вы говорите по-русски?', 'Проще всего заказать через форму WhatsApp: она сама составит заказ на турецком языке для продавца, поэтому языковой барьер не помешает.'),
         ('Какую воду вы привозите?', 'Aysu, Madran и Hayat в бутылях 19 л, а также воду в бутылках 0,5 л и 1,5 л.'),
         ('Сколько это стоит?', 'Цены на газ и воду периодически меняются, поэтому актуальную цену уточняйте по телефону или в WhatsApp.')],
)
P['ru']['gas'] = dict(
    title='Газовые баллоны İpragaz в Аланье 24/7 | Доставка | Alanyam Ticaret',
    desc=f'Заказ газового баллона İpragaz в Аланье: баллоны для дома и бизнеса с доставкой круглосуточно. Звоните или пишите в WhatsApp: {TEL_GSM}',
    crumb='Газ İpragaz', eyebrow='Аланья · баллоны İpragaz',
    h1='Газовые баллоны İpragaz в Аланье <span>круглосуточно</span>',
    lead='Газ закончился посреди готовки? Alanyam Ticaret привезёт баллон İpragaz по вашему адресу в Аланье днём и ночью. Позвоните или напишите в WhatsApp.',
    chips=['Баллоны İpragaz', 'Дом и бизнес', 'Заказ ночью'], badge=('24/7', 'Заказ газа'), art='cyl',
    prod_k='Заказ газа', prod_h='<span class="hl">İpragaz</span> для дома и бизнеса',
    prod_p='Не знаете, какой баллон нужен? Расскажите по телефону, где вы его используете, — поможем выбрать.',
    cards=[('home', 'Кухонный баллон', 'Обычный бытовой баллон для плиты и духовки. Закончился — звоните, привезём полный.'),
           ('flame', 'Баллоны для бизнеса', 'Для ресторанов, кафе, отелей и магазинов. Подберём подходящий баллон по телефону.'),
           ('truck', 'Доставка 24/7', 'Привозим в дома и офисы по всей Аланье днём и ночью.')],
    info_k='Бренд', info_h='О компании İpragaz',
    info_p=['İpragaz занимается поставками сжиженного газа (LPG) в Турции с 1961 года, а с 1999 года входит в группу SHV Energy.',
            'Alanyam Ticaret доставляет баллоны İpragaz в дома и офисы Аланьи. Заказать можно по телефону или в WhatsApp круглосуточно.'],
    info_ticks=['Доставка газа İpragaz по Аланье', 'Баллоны для дома и бизнеса', 'Ночью, в выходные и праздники'],
    safety_h='6 простых правил безопасности',
    safety=['Держите баллон вертикально, в проветриваемом месте, вдали от солнца, обогревателей и источников тепла.',
            'Проверяйте утечку мыльной водой: если появились пузыри, закройте вентиль. Никогда не проверяйте огнём.',
            'Регулярно осматривайте шланг и хомуты; треснувший или затвердевший шланг замените.',
            'Закрывайте вентиль баллона, когда плитой не пользуетесь и когда уходите из дома.',
            'Почувствовали запах газа — не трогайте выключатели, закройте вентиль, откройте окна и двери.',
            'В экстренной ситуации звоните 112.'],
    faq=[('Как заказать баллон İpragaz в Аланье?', f'Позвоните по номеру {TEL_GSM} или воспользуйтесь формой WhatsApp на этой странице. Назовите адрес и нужный баллон.'),
         ('Вы привозите газ ночью?', 'Да, мы принимаем заказы круглосуточно, в том числе ночью, в выходные и праздники.'),
         ('Что делать с пустым баллоном?', 'Условия обмена и залога уточните при заказе. Если пустой баллон будет готов к приезду курьера, доставка пройдёт быстрее.'),
         ('Что делать, если пахнет газом?', 'Не трогайте электрические выключатели, закройте вентиль баллона, проветрите помещение и при необходимости звоните 112.')],
)
P['ru']['water'] = dict(
    title='Доставка воды и соды в Аланье | Aysu, Madran, Hayat, Kızılay, Beypazarı | Alanyam Ticaret',
    desc=f'Вода Aysu, Madran и Hayat в бутылях 19 л и в бутылках 0,5 / 1,5 л с доставкой по Аланье 24/7. WhatsApp: {TEL_WA}',
    crumb='Вода', eyebrow='Аланья · питьевая вода',
    h1='Вода и сода в Аланье: <span>Aysu, Madran, Hayat, Kızılay, Beypazarı</span>',
    lead='Выберите воду по вкусу — мы привезём её к двери. Alanyam Ticaret доставляет бутыли 19 л и воду в бутылках по всей Аланье круглосуточно.',
    chips=['Бутыли 19 л', 'Aysu в бутылках и стаканчиках', 'Сода Kızılay и Beypazarı'], badge=('5', 'брендов'), art='jugs',
    prod_k='Наша вода', prod_h='Какую воду <span class="hl">вы предпочитаете?</span>',
    prod_p='На странице каждого бренда — варианты объёма и информация о заказе.',
    extra_card=('party', 'Aysu в бутылках и стаканчиках', 'Бутылки Aysu 0,5 и 1,5 л и вода в стаканчиках; оптом на свадьбы, встречи и праздники.'),
    info_k='Полезно знать', info_h='Как хранить бутыль с водой',
    info_p=['Несколько простых правил помогут сохранить свежесть и вкус воды.'],
    info_ticks=['Храните бутыль в прохладном чистом месте, без прямого солнца.', 'Открытую бутыль старайтесь выпить в короткий срок.',
                'Регулярно мойте помпу или кулер.', 'Не храните бутыли рядом с химией и пахучими веществами.'],
    faq=[('Какую воду вы привозите в Аланье?', 'Aysu, Madran и Hayat в бутылях 19 л. Aysu и Madran есть также в бутылках 1,5 л и 0,5 л.'),
         ('Как заказать воду?', f'Позвоните по номеру {TEL_GSM} или воспользуйтесь формой WhatsApp на этой странице: бренд, количество и адрес.'),
         ('Принимаете оптовые заказы?', 'Да, принимаем заказы воды в бутылках на свадьбы, встречи и мероприятия. Сообщите количество заранее.'),
         ('Что с пустыми бутылями?', 'Условия возврата пустых бутылей и залога уточните при заказе.')],
)


def _brand_ru(k):
    n = BRAND_NAME[k]
    return dict(
        title=f'Вода {n} в Аланье, бутыль 19 л | Доставка 24/7 | Alanyam Ticaret',
        desc=f'Вода {n} в бутылях 19 л' + (' и бутылках 0,5 / 1,5 л' if k != 'hayat' else '') + ' с доставкой по Аланье круглосуточно. Звоните или пишите в WhatsApp.',
        crumb=n, eyebrow=f'Аланья · вода {n}',
        h1=f'Вода {n} в Аланье <span>с доставкой до двери</span>',
        lead=f'Привозим воду {n} в квартиры, дома и офисы Аланьи. ' + ('Бутыли или бутылки — выбирайте, а мы доставим.' if k != 'hayat' else 'Бутыли 19 л можно заказать круглосуточно.'),
        chips=[f'{n}, бутыль 19 л', 'Заказ 24/7', 'Доставка до двери'], badge=('19 л', 'бутыль'), art='jug',
        prod_k='Варианты', prod_h=f'Вода {n}: <span class="hl">варианты</span>',
        prod_p='Скажите, сколько нужно, — и мы привезём заказ по вашему адресу.',
        info_k='Бренд', info_h=f'О воде {n}', info_p=[BRAND[k]['ru']],
        info_ticks=[f'Доставка воды {n} по Аланье', 'Телефон и WhatsApp 24/7', 'Дома и офисы'],
        faq=[(f'Как заказать воду {n} в Аланье?', f'Позвоните по номеру {TEL_GSM} или воспользуйтесь формой WhatsApp на этой странице. Достаточно количества и адреса.'),
             (f'Какой объём бутыли {n}?', f'Бутыль {n} — 19 литров. ' + ('Также есть бутылки 1,5 л и 0,5 л.' if k != 'hayat' else 'О бутылках меньшего объёма спрашивайте по телефону.')),
             (f'Привозите {n} ночью?', 'Да, мы принимаем заказы круглосуточно.'),
             ('Есть другие бренды?', 'Да — Aysu, Madran и Hayat. Другие бренды смотрите ниже.')],
    )


for _k in ['aysu', 'madran', 'hayat']:
    P['ru'][_k] = _brand_ru(_k)

P['ru']['contact'] = dict(
    title='Контакты и заказ | Alanyam Ticaret – газ и вода в Аланье',
    desc=f'Контакты Alanyam Ticaret: {TEL_GSM}, {TEL_FIX}, WhatsApp {TEL_WA}. Доставка газа и воды по Аланье 24/7.',
    crumb='Контакты', eyebrow='Аланья · на связи 24/7',
    h1='Свяжитесь с нами — <span>заказ уже в пути</span>',
    lead='Звоните или пишите в WhatsApp круглосуточно: заказы газа и воды, вопросы и пожелания.',
    chips=['Круглосуточно', '3 номера', 'Заказ в WhatsApp'], badge=('24/7', 'на связи'), art='mix',
    faq=[('По какому номеру звонить?', f'Звоните по номеру {TEL_GSM} или на городской {TEL_FIX}, пишите в WhatsApp: {TEL_WA}.'),
         ('Какой у вас график работы?', 'Alanyam Ticaret работает круглосуточно, включая ночь, выходные и праздники.'),
         ('Куда вы доставляете?', 'Доставляем газ и воду в дома и офисы по всей Аланье.')],
)



def _soda(lang, k):
    n = BRAND_NAME[k]
    T = {
        'tr': dict(
            title=f'Alanya {n} Soda (Maden Suyu) Siparişi | 7/24 | Alanyam Ticaret',
            desc=f'Alanya’da {n} maden suyu (soda) siparişi. Ev, işyeri ve restoranlara 7/24 kapıya teslim; telefon veya WhatsApp ile sipariş verin.',
            crumb=f'{n} Soda', eyebrow=f'Alanya · {n} soda',
            h1=f'Alanya {n} soda, <span>kapınıza</span>',
            lead=f'{n} maden suyunu Alanya’da evinize, işyerinize ve restoranınıza getiriyoruz. Su ya da tüp siparişinizle birlikte de isteyebilirsiniz.',
            chips=[f'{n} maden suyu', '7/24 sipariş', 'Su ve tüple birlikte'], badge=('Soda', 'maden suyu'),
            prod_k='Sipariş', prod_h=f'{n} <span class="hl">soda siparişi</span>',
            prod_p='Kaç adet ya da koli istediğinizi söyleyin, siparişinizi adresinize getirelim.',
            cards=[('drop', f'{n} soda', f'{n} maden suyunu tek tek ya da toplu sipariş edebilirsiniz; çeşitleri telefonda sorun.'),
                   ('party', 'İşyeri ve davetler', 'Restoran, kafe, ofis ve davetler için toplu soda siparişi; miktarı telefonda bildirin.'),
                   ('truck', '7/24 kapıya teslim', 'Alanya genelinde ev ve işyerinize gece gündüz teslimat.')],
            info_k='Marka', info_h=f'{n} hakkında', info_p=[BRAND[k]['tr']],
            info_ticks=[f'Alanya {n} soda siparişi', 'Su ve tüp siparişiyle birlikte', '7/24 telefon ve WhatsApp'],
            faq=[(f'Alanya’da {n} soda siparişi nasıl verilir?', f'{TEL_GSM} numarasını arayın ya da sayfadaki formdan WhatsApp’la sipariş verin. Adet ve adres yeterli.'),
                 ('Soda ile maden suyu aynı şey mi?', 'Evet. Günlük dilde “soda” denilen ürün doğal mineralli sudur, yani maden suyudur.'),
                 ('Su siparişimle birlikte soda isteyebilir miyim?', 'Evet; damacana su, pet su ya da tüp siparişinizin yanına soda da ekleyebilirsiniz.'),
                 (f'{n} sodayı gece de getiriyor musunuz?', 'Evet, 7/24 sipariş alıyoruz.')]),
        'en': dict(
            title=f'{n} Mineral Water (Soda) Delivery in Alanya 24/7 | Alanyam Ticaret',
            desc=f'Order {n} mineral water (soda) in Alanya. Delivered 24/7 to homes, offices and restaurants; order by phone or WhatsApp.',
            crumb=f'{n} Soda', eyebrow=f'Alanya · {n} soda',
            h1=f'{n} mineral water in Alanya, <span>to your door</span>',
            lead=f'We deliver {n} mineral water to homes, offices and restaurants in Alanya. Add it to your water or gas order.',
            chips=[f'{n} mineral water', 'Orders 24/7', 'With water & gas'], badge=('Soda', 'mineral water'),
            prod_k='Ordering', prod_h=f'Order <span class="hl">{n} soda</span>',
            prod_p='Tell us how many bottles or cases you need and we’ll bring them to your address.',
            cards=[('drop', f'{n} soda', f'Order {n} mineral water by the bottle or in bulk; ask us about varieties by phone.'),
                   ('party', 'Businesses & events', 'Bulk soda for restaurants, cafés, offices and events; tell us the quantity by phone.'),
                   ('truck', '24/7 door delivery', 'Delivery to homes and businesses across Alanya, day and night.')],
            info_k='Brand', info_h=f'About {n}', info_p=[BRAND[k]['en']],
            info_ticks=[f'{n} soda delivery in Alanya', 'Together with water and gas', '24/7 phone and WhatsApp'],
            faq=[(f'How do I order {n} soda in Alanya?', f'Call {TEL_GSM} or use the WhatsApp form on this page. Quantity and address are enough.'),
                 ('Is “soda” the same as mineral water?', 'Yes. In Türkiye, “soda” usually means natural sparkling mineral water.'),
                 ('Can I add soda to my water order?', 'Yes, add soda to your jug, bottled water or gas order.'),
                 (f'Do you deliver {n} at night?', 'Yes, we take orders 24/7.')]),
        'ru': dict(
            title=f'Минеральная вода {n} (сода) в Аланье 24/7 | Alanyam Ticaret',
            desc=f'Минеральная вода {n} (сода) с доставкой по Аланье круглосуточно — в дома, офисы и рестораны. Заказ по телефону или в WhatsApp.',
            crumb=f'{n}', eyebrow=f'Аланья · сода {n}',
            h1=f'Минеральная вода {n} в Аланье <span>с доставкой</span>',
            lead=f'Привозим минеральную воду {n} в дома, офисы и рестораны Аланьи. Можно добавить к заказу воды или газа.',
            chips=[f'Минеральная вода {n}', 'Заказ 24/7', 'Вместе с водой и газом'], badge=('Soda', 'минеральная вода'),
            prod_k='Заказ', prod_h=f'Заказать <span class="hl">{n}</span>',
            prod_p='Скажите, сколько бутылок или упаковок нужно, — и мы привезём заказ по вашему адресу.',
            cards=[('drop', f'Сода {n}', f'Минеральную воду {n} можно заказать поштучно или оптом; о видах спрашивайте по телефону.'),
                   ('party', 'Бизнес и мероприятия', 'Оптом для ресторанов, кафе, офисов и праздников — количество уточните по телефону.'),
                   ('truck', 'Доставка 24/7', 'Привозим в дома и офисы по всей Аланье днём и ночью.')],
            info_k='Бренд', info_h=f'О воде {n}', info_p=[BRAND[k]['ru']],
            info_ticks=[f'Доставка {n} по Аланье', 'Вместе с водой и газом', 'Телефон и WhatsApp 24/7'],
            faq=[(f'Как заказать {n} в Аланье?', f'Позвоните по номеру {TEL_GSM} или воспользуйтесь формой WhatsApp на этой странице. Достаточно количества и адреса.'),
                 ('«Сода» — это минеральная вода?', 'Да. В Турции «содой» обычно называют природную газированную минеральную воду.'),
                 ('Можно добавить соду к заказу воды?', 'Да, соду можно добавить к заказу бутылей, бутылок воды или газа.'),
                 (f'Привозите {n} ночью?', 'Да, мы принимаем заказы круглосуточно.')]),
    }[lang]
    T['art'] = 'soda'
    return T


for _l in LANGS:
    for _k in SODAS:
        P[_l][_k] = _soda(_l, _k)

# İpragaz adı ileride değişirse metinlerde de değişsin
if GAS != 'İpragaz':
    for _l in P:
        for _p in P[_l].values():
            for _f, _v in list(_p.items()):
                if isinstance(_v, str):
                    _p[_f] = _v.replace('İpragaz', GAS)

# ---------- Müşteri yorumları ----------
# YALNIZ gerçek yorumlar (Google İşletme Profili vb.). Uydurma yorum EKLENMEZ.
# Örnek: {'ad': 'Ayşe K.', 'puan': 5, 'metin': '...', 'kaynak': 'Google'}
REVIEWS = []
