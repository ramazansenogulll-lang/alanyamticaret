# -*- coding: utf-8 -*-
"""Rehber (blog) makaleleri — Türkçe. SEO + GEO: başta kısa cevap, net H2'ler, kaynak, SSS.
Kural: marka bazında doğrulanmamış pH / mineral rakamı YAZMA; sağlık iddiası yok."""
from content import TEL_GSM, TEL_WA, GAS

DATE = '2026-11-24'

SRC_YON = ('İnsani Tüketim Amaçlı Sular Hakkında Yönetmelik (Resmî Gazete, 17.02.2005, sayı 25730)',
           'https://www.lexpera.com.tr/mevzuat/yonetmelikler/insani-tuketim-amacli-sular-hakkinda-yonetmelik')
SRC_TUBITAK = ('TÜBİTAK Bilim ve Teknik – Su posteri (içme sularına ait bazı parametreler)',
               'https://bilimteknik.tubitak.gov.tr/sites/default/files/posterler/57x82_suposteri_haziran_2019.pdf')
SRC_WHO = ('Dünya Sağlık Örgütü – Guidelines for drinking-water quality', 'https://www.who.int/publications/i/item/9789240045064')

ARTICLES = [
    dict(
        slug='su-ph-degeri-nedir', cat='Su kalitesi', art='jug', related=['water', 'aysu', 'madran'],
        title='Suyun pH Değeri Nedir? İçme Suyunda pH Kaç Olmalı? | Alanyam Ticaret',
        desc='İçme suyunun pH değeri nedir, kaç olmalı, damacana etiketinde nasıl okunur? Türkiye’deki 6,5–9,5 sınırı ve alkali su hakkında sade rehber.',
        h1='Suyun pH değeri nedir, içme suyunda kaç olmalı?',
        answer='pH, suyun asidik ya da bazik olduğunu gösteren 0–14 arası bir ölçüdür; 7 nötrdür. Türkiye’de içme ve kaynak suları için kabul edilen pH aralığı 6,5–9,5’tir. Bu aralıktaki sular içmeye uygundur; pH’ın birkaç onda bir yüksek ya da düşük olması tek başına “daha sağlıklı su” anlamına gelmez.',
        body=[
            ('pH ne demek?', '''<p>pH, sudaki hidrojen iyonu yoğunluğunu gösteren bir ölçektir. Ölçek <strong>0 ile 14</strong> arasındadır:</p>
<ul><li><strong>7’nin altı</strong> asidik (örneğin limon suyu yaklaşık 2–3),</li><li><strong>7</strong> nötr (saf su),</li><li><strong>7’nin üstü</strong> bazik ya da alkali (örneğin karbonatlı su, sabunlu su).</li></ul>
<p>Ölçek logaritmiktir: pH 6 olan bir su, pH 7 olan sudan 10 kat daha asidiktir. Bu yüzden etiketlerde 7,2 ile 7,8 gibi küçük görünen farklar bile kimyasal olarak anlamlıdır; ama sağlık açısından ikisi de normal içme suyudur.</p>'''),
            ('İçme suyunda pH kaç olmalı?', '''<p>Türkiye’de şişe, damacana ve şebeke sularını düzenleyen <em>İnsani Tüketim Amaçlı Sular Hakkında Yönetmelik</em>, içme ve kaynak suları için pH değerini <strong>6,5 ile 9,5 arasında</strong> tanımlar. Avrupa Birliği’ndeki içme suyu düzenlemesi de aynı aralığı kullanır.</p>
<p>Dünya Sağlık Örgütü (DSÖ) pH için sağlığa dayalı bir sınır koymaz; pH’ı daha çok suyun tadını, borulardaki korozyonu ve dezenfeksiyonun etkinliğini etkileyen bir işletme parametresi olarak ele alır.</p>
<div class="callout"><b>Kısaca:</b> Etiketindeki pH 6,5–9,5 arasında olan ve ruhsatlı bir tesiste dolan su içmeye uygundur.</div>'''),
            ('Damacana etiketinde pH nasıl okunur?', '''<p>Damacana ve şişe su etiketlerinde genellikle bir <strong>analiz tablosu</strong> bulunur. Bu tabloda şunları görürsünüz:</p>
<ul><li><strong>pH</strong> – suyun asit/baz dengesi,</li><li><strong>Kalsiyum (Ca), Magnezyum (Mg)</strong> – suyun sertliğini ve tadını etkiler,</li><li><strong>Sodyum (Na)</strong> – tuz kısıtlaması olanların dikkat ettiği değer,</li><li><strong>Bikarbonat, sülfat, klorür, nitrat</strong> gibi diğer parametreler,</li><li>Kaynağın adı ve yeri, dolum tesisi, analiz tarihi ve ruhsat bilgisi.</li></ul>
<p>Markaların pH değerleri kaynaktan kaynağa değişir ve aynı marka farklı tesislerde farklı değer verebilir. En doğru bilgi, elinizdeki damacananın kendi etiketidir.</p>'''),
            ('Alkali su daha mı sağlıklı?', '''<p>“Yüksek pH’lı su vücudu alkali yapar” gibi iddialar sık duyulur. Vücudumuz kanın pH’ını kendi mekanizmalarıyla dar bir aralıkta tutar; içtiğimiz suyun pH’ı bunu değiştirmez. Alkali suyun hastalıklara iyi geldiğine dair güçlü bilimsel kanıt yoktur.</p>
<p>Su seçerken pH’tan çok <strong>tadı beğenmeniz, düzenli ve yeterli su içmeniz</strong> ve suyun güvenilir bir tesisten gelmesi önemlidir.</p>'''),
            ('pH dışında su kalitesini ne belirler?', '''<ul><li><strong>Kaynağın korunması:</strong> Kaynak suyunun bulunduğu havzanın kirlenmeye karşı korunması.</li><li><strong>Dolum hijyeni:</strong> Damacananın yıkanması, kapak ve dolum hattının temizliği.</li><li><strong>Saklama:</strong> Güneş ve ısı, plastik ambalajlı suyun tadını bozabilir.</li><li><strong>Tüketim süresi:</strong> Açılan damacananın kısa sürede bitirilmesi.</li></ul>
<p>Saklama ve sebil temizliği için <a href="/blog/sebil-ve-damacana-pompasi-temizligi/">sebil ve damacana pompası temizliği rehberimize</a> bakabilirsiniz.</p>'''),
        ],
        faq=[('İçme suyunun pH değeri kaç olmalı?', 'Türkiye’deki yönetmeliğe göre içme ve kaynak suları için pH 6,5 ile 9,5 arasında olmalıdır.'),
             ('pH 8 olan su sağlıklı mı?', 'pH 8, kabul edilen 6,5–9,5 aralığındadır; içmeye uygundur. Yüksek pH tek başına suyu daha sağlıklı yapmaz.'),
             ('Damacana suyun pH değerini nereden öğrenirim?', 'Damacananın etiketindeki analiz tablosunda pH değeri yazar. En doğru bilgi elinizdeki ürünün etiketidir.'),
             ('Alkali su içmek gerekli mi?', 'Hayır. Vücut kan pH’ını kendisi dengeler; alkali suyun hastalıklara iyi geldiğine dair güçlü kanıt yoktur.')],
        sources=[SRC_YON, SRC_TUBITAK, SRC_WHO],
    ),
    dict(
        slug='kaynak-suyu-ile-icme-suyu-farki', cat='Su kalitesi', art='jugs', related=['water', 'hayat', 'aysu'],
        title='Kaynak Suyu ile İçme Suyu Farkı Nedir? Etikette Neye Bakılır? | Alanyam Ticaret',
        desc='Doğal kaynak suyu, içme suyu ve doğal mineralli su arasındaki fark nedir? Damacana alırken etikette kontrol edilecek 6 bilgi.',
        h1='Kaynak suyu ile içme suyu arasındaki fark nedir?',
        answer='Kaynak suyu, yer altında doğal olarak oluşan ve kaynağından çıkan sudur; kural olarak özelliklerini değiştiren arıtma işlemi uygulanmadan doldurulur. İçme suyu ise farklı kaynaklardan alınıp gerektiğinde arıtılarak içilebilir hâle getirilen sudur. İkisi de yönetmelikteki kalite sınırlarını sağlamak zorundadır; fark, suyun nereden geldiği ve hangi işlemlerden geçtiğidir.',
        body=[
            ('Üç ana su türü', '''<ul><li><strong>Doğal kaynak suyu:</strong> Jeolojik olarak korunmuş bir yeraltı kaynağından gelir. Etikette kaynağın adı ve yeri yazar. Damacana sularının çoğu bu gruptadır.</li>
<li><strong>İçme suyu:</strong> Kaynak, kuyu veya yüzey suyundan alınıp gerekiyorsa arıtılır. Kalite sınırları aynıdır; arıtma yöntemi etikette belirtilebilir.</li>
<li><strong>Doğal mineralli su:</strong> Mineral içeriği yüksek, ayrı bir yönetmelikle düzenlenen sudur (soda/maden suyu). Günlük damacana suyu bu gruba girmez.</li></ul>'''),
            ('Etikette kontrol edilecek 6 bilgi', '''<ol><li><strong>Su türü:</strong> “Doğal kaynak suyu” mu “içme suyu” mu?</li><li><strong>Kaynağın adı ve yeri</strong></li><li><strong>Dolum tesisi ve ruhsat/izin bilgisi</strong></li><li><strong>Analiz tablosu:</strong> pH, kalsiyum, magnezyum, sodyum vb.</li><li><strong>Dolum ve son tüketim tarihi</strong></li><li><strong>Kapak ve mühür:</strong> Damacana kapağı sağlam ve mühürlü olmalı.</li></ol>
<p>pH değerinin ne anlama geldiğini <a href="/blog/su-ph-degeri-nedir/">suyun pH değeri rehberimizde</a> anlattık.</p>'''),
            ('Hangisi daha iyi?', '''<p>Ruhsatlı bir tesiste dolan ve yönetmelik sınırlarını sağlayan her su içmeye uygundur. Seçimde en belirleyici unsur genellikle <strong>tat</strong>tır: mineral dengesi farklı olduğu için her kaynağın suyu biraz farklı içilir. Alanyam Ticaret’te Aysu, Madran ve Hayat Su arasından deneyip size en uygun tadı seçebilirsiniz.</p>'''),
        ],
        faq=[('Damacana su kaynak suyu mudur?', 'Çoğu damacana su doğal kaynak suyudur; bunu etiketteki “doğal kaynak suyu” ibaresinden ve kaynak adından anlayabilirsiniz.'),
             ('İçme suyu kaynak suyundan kötü müdür?', 'Hayır. İçme suyu da aynı kalite sınırlarını sağlamak zorundadır; fark kaynağı ve uygulanan işlemlerdir.'),
             ('Etikette en önemli bilgi hangisi?', 'Su türü, kaynak adı, dolum tesisi/ruhsat bilgisi ve son tüketim tarihi birlikte kontrol edilmelidir.')],
        sources=[SRC_YON, SRC_TUBITAK],
    ),
    dict(
        slug='aysu-madran-hayat-hangi-su', cat='Markalar', art='jugs', related=['aysu', 'madran', 'hayat'],
        title='Aysu, Madran, Hayat: Alanya’da Hangi Damacana Suyu Seçmeli? | Alanyam Ticaret',
        desc='Alanya’da sipariş verebileceğiniz Aysu, Madran ve Hayat damacana sularını tanıyın: kaynakları, seçenekleri ve seçim ipuçları.',
        h1='Aysu, Madran ve Hayat: Alanya’da hangi damacana suyu seçmeli?',
        answer='Alanyam Ticaret’ten Alanya’da Aysu, Madran ve Hayat 19 litre damacana sipariş edebilirsiniz. Üçü de içmeye uygun ambalajlı sulardır; aralarındaki fark kaynak bölgesi, mineral dengesi ve buna bağlı tattır. En iyi yöntem, her birini birer kez deneyip ailenizin beğendiği tadı seçmektir.',
        body=[
            ('Aysu', f'''<p>Aysu, doğallığını <strong>Dedegöl Dağı eteklerindeki</strong> kaynağından alan bir doğal kaynak suyudur. Alanyam Ticaret’te 19 litre damacana ile 1,5 ve 0,5 litre şişe seçenekleri bulunur. <a href="/aysu/">Alanya Aysu su siparişi →</a></p>'''),
            ('Madran', '''<p>Madran, <strong>Aydın’ın Bozdoğan ilçesindeki Madran Dağı</strong> yöresinin kaynaklarından gelir. 19 litre damacana ile 1,5 ve 0,5 litre şişe seçenekleri vardır. <a href="/madran/">Alanya Madran su siparişi →</a></p>'''),
            ('Hayat', '''<p>Hayat, <strong>Danone</strong>’nin Türkiye’deki su markalarından biridir. Alanyam Ticaret, Hayat Su 19 litre damacanayı Alanya’da kapınıza getirir. <a href="/hayat-su/">Alanya Hayat su siparişi →</a></p>'''),
            ('Seçerken nelere bakmalı?', '''<ul><li><strong>Tat:</strong> Mineral dengesi farklı suların tadı da farklıdır; deneyerek seçin.</li><li><strong>Etiket:</strong> pH ve mineral değerlerini etiketteki analiz tablosundan okuyun (<a href="/blog/su-ph-degeri-nedir/">pH rehberi</a>).</li><li><strong>Tüketim hızı:</strong> Kalabalık hanelerde ya da işyerinde birden fazla damacana sipariş etmek pratiktir.</li><li><strong>Şişe ihtiyacı:</strong> Dışarıda kullanım ya da davetler için 0,5 ve 1,5 litre şişeler uygundur.</li></ul>'''),
        ],
        faq=[('Alanya’da hangi damacana suları sipariş edilebilir?', 'Alanyam Ticaret’ten Aysu, Madran ve Hayat 19 litre damacana sipariş edebilirsiniz.'),
             ('Hangi su daha iyi?', 'Üçü de içmeye uygun ambalajlı sulardır. Fark çoğunlukla tattadır; denemeniz en doğrusudur.'),
             ('Markaların pH değerleri nedir?', 'pH değeri kaynak ve parti bazında değişebilir; en doğru bilgi damacananın etiketindedir.')],
        sources=[],
    ),
    dict(
        slug='alanya-su-siparisi', cat='Alanya', art='jug', related=['water', 'contact', 'aysu'],
        title='Alanya Su Siparişi: Damacana Su Nasıl Sipariş Edilir? | Alanyam Ticaret',
        desc=f'Alanya’da damacana su siparişi nasıl verilir? Telefon ve WhatsApp ile 7/24 sipariş, marka seçimi ve teslimat. Hemen arayın: {TEL_GSM}',
        h1='Alanya su siparişi: damacana su nasıl sipariş edilir?',
        answer=f'Alanya’da damacana su siparişi için Alanyam Ticaret’i {TEL_GSM} numarasından arayabilir ya da WhatsApp’tan ({TEL_WA}) yazabilirsiniz. Marka (Aysu, Madran, Hayat), adet ve adresinizi söylemeniz yeterlidir; siparişler 7/24 alınır ve kapınıza teslim edilir.',
        body=[
            ('Adım adım su siparişi', f'''<ol><li><strong>Markayı seçin:</strong> Aysu, Madran ya da Hayat.</li><li><strong>Adedi belirleyin:</strong> Ev için genellikle 1–2, işyeri için ihtiyaca göre.</li><li><strong>Bize ulaşın:</strong> {TEL_GSM} numarasını arayın ya da sitedeki formdan WhatsApp’la gönderin.</li><li><strong>Adresinizi verin:</strong> Mahalle, sokak, bina ve daire numarası.</li><li><strong>Teslim alın:</strong> Boş damacananız varsa hazır bulundurun.</li></ol>'''),
            ('WhatsApp’tan sipariş', '''<p>Sitemizdeki her sayfada bir sipariş formu var. Ürünü, adedi ve adresi yazıp “WhatsApp ile gönder”e bastığınızda mesaj hazır olarak açılır. Alanya’da yaşayan yabancı müşterilerimiz için form İngilizce ve Rusça sayfalarda da var; mesaj bayiye Türkçe ulaşır.</p>'''),
            ('Alanya’nın neresine teslimat var?', '''<p>Alanya genelinde ev ve işyerlerine teslimat yapıyoruz. Bulunduğunuz mahalleyi sipariş sırasında söylemeniz yeterli; teslim süresini telefonda netleştiririz.</p>'''),
            ('Toplu ve özel gün siparişleri', '''<p>Düğün, nişan, toplantı ve davetler için 0,5 ve 1,5 litre şişe su siparişi alıyoruz. Miktarı önceden bildirmeniz, siparişin zamanında hazırlanmasını kolaylaştırır.</p>'''),
        ],
        faq=[('Alanya’da gece su siparişi verilir mi?', 'Evet, Alanyam Ticaret 7/24 sipariş alır.'),
             ('Hangi markalar var?', 'Aysu, Madran ve Hayat 19 litre damacana; Aysu ve Madran’ın şişe seçenekleri de var.'),
             ('Fiyatı nasıl öğrenirim?', 'Güncel fiyatı telefonda ya da WhatsApp’tan sorabilirsiniz.')],
        sources=[],
    ),
    dict(
        slug='alanya-tup-siparisi', cat='Alanya', art='cyl', related=['gas', 'contact', 'home'],
        title=f'Alanya Tüp Siparişi: Gece Tüp Bitince Ne Yapmalı? | Alanyam Ticaret',
        desc=f'Alanya’da tüp siparişi nasıl verilir? {GAS} tüp 7/24 kapınıza; boş tüp, güvenli takma ve kaçak kontrolü. Hemen arayın: {TEL_GSM}',
        h1='Alanya tüp siparişi: tüp gece bitince ne yapmalı?',
        answer=f'Alanya’da tüp siparişi için Alanyam Ticaret’i {TEL_GSM} numarasından 7/24 arayabilir ya da WhatsApp’tan yazabilirsiniz. Adresinizi ve tüpün ev mi işyeri mi için olduğunu söylemeniz yeterli; {GAS} tüpünüz kapınıza getirilir.',
        body=[
            ('Tüp bittiğinde ilk yapılacaklar', '''<ol><li>Ocağın düğmelerini ve tüp vanasını kapatın.</li><li>Bizi arayın ya da WhatsApp’tan yazın; adresinizi ve tüp türünü söyleyin.</li><li>Boş tüpü kapı önüne ya da kolay ulaşılacak bir yere hazırlayın.</li></ol>'''),
            ('Tüp nasıl güvenle takılır?', '''<ul><li>Regülatörü takmadan önce contanın yerinde ve sağlam olduğundan emin olun.</li><li>Regülatörü yerine oturtup kilitleyin, ardından vanayı açın.</li><li>Bağlantıları <strong>sabunlu suyla</strong> kontrol edin; kabarcık varsa vanayı kapatıp bağlantıyı yeniden yapın. Kontrol için asla çakmak ya da kibrit kullanmayın.</li><li>Emin değilseniz bizi arayın.</li></ul>
<p>Daha fazlası için <a href="/blog/tup-gaz-guvenligi/">tüp gaz güvenliği rehberimize</a> bakın.</p>'''),
            ('Ev ve işyeri tüpleri', f'''<p>Evlerde ocak ve fırın için mutfak tüpü kullanılır. Restoran, kafe ve oteller ise kullanım yoğunluğuna göre farklı tüplere ihtiyaç duyabilir. Hangisinin size uygun olduğunu telefonda birlikte belirleriz. <a href="/ipragaz/">Alanya {GAS} tüp siparişi →</a></p>'''),
        ],
        faq=[('Alanya’da gece tüp siparişi verilir mi?', 'Evet, Alanyam Ticaret 7/24 tüp siparişi alır.'),
             ('Hangi marka tüp getiriyorsunuz?', f'{GAS} tüp getiriyoruz.'),
             ('Boş tüp alınıyor mu?', 'Tüp değişimi ve depozito koşullarını sipariş sırasında telefonda öğrenebilirsiniz.')],
        sources=[],
    ),
    dict(
        slug='tup-gaz-guvenligi', cat='Güvenlik', art='cyl', related=['gas', 'home', 'contact'],
        title='Tüp Gaz Güvenliği: Kaçak Kontrolü, Hortum ve Regülatör | Alanyam Ticaret',
        desc='Evde tüp gaz güvenliği: sabunlu suyla kaçak kontrolü, hortum ve regülatör bakımı, gaz kokusu alınca yapılacaklar. Kısa ve uygulanabilir rehber.',
        h1='Tüp gaz güvenliği: kaçak kontrolü, hortum ve regülatör',
        answer='Tüp gazı güvenle kullanmak için tüpü dik ve havalanan bir yerde tutun, bağlantıları sabunlu suyla kontrol edin, hortumu düzenli değiştirin ve kullanmadığınızda vanayı kapatın. Gaz kokusu alırsanız elektrik düğmelerine dokunmadan vanayı kapatın, ortamı havalandırın ve gerekirse 112’yi arayın.',
        body=[
            ('Tüpün yeri', '''<ul><li>Tüp her zaman <strong>dik</strong> durmalı.</li><li>Güneş, soba, kalorifer ve ocağın hemen yanı gibi ısı kaynaklarından uzak olmalı.</li><li>Havalanan bir yerde kullanılmalı; LPG havadan ağır olduğu için zemine çöker, bodrum ve kapalı dolaplar uygun değildir.</li></ul>'''),
            ('Kaçak kontrolü nasıl yapılır?', '''<ol><li>Bir kaba sabunlu su hazırlayın.</li><li>Vana açıkken bağlantı noktalarına fırça ya da süngerle sürün.</li><li>Kabarcık oluşuyorsa gaz kaçıyordur: vanayı kapatın, bağlantıyı yeniden yapın, sorun sürerse yardım isteyin.</li></ol>
<div class="callout"><b>Asla:</b> Kaçak kontrolü için çakmak, kibrit ya da ateş kullanmayın.</div>'''),
            ('Hortum ve regülatör', '''<ul><li>Hortumu düzenli kontrol edin; çatlak, sertleşme ya da ezilme varsa değiştirin.</li><li>Hortum uçlarında kelepçe kullanın ve sıkılığını kontrol edin.</li><li>Regülatörün contası bozulmuşsa kullanmayın.</li></ul>'''),
            ('Gaz kokusu alırsanız', '''<ol><li>Elektrik düğmelerine, prizlere ve zillere dokunmayın.</li><li>Tüp vanasını kapatın.</li><li>Kapı ve pencereleri açarak ortamı havalandırın.</li><li>Ortamı terk edin ve gerekirse <strong>112</strong>’yi arayın.</li></ol>'''),
        ],
        faq=[('Tüpte gaz kaçağı nasıl anlaşılır?', 'Gaz kokusu alınması ve bağlantılara sürülen sabunlu suda kabarcık oluşması kaçak işaretidir.'),
             ('Tüp yatık kullanılır mı?', 'Hayır, tüp her zaman dik kullanılmalıdır.'),
             ('Gaz kokusunda ilk ne yapılmalı?', 'Elektrik düğmelerine dokunmadan vanayı kapatın, havalandırın, gerekirse 112’yi arayın.')],
        sources=[],
    ),
    dict(
        slug='sebil-ve-damacana-pompasi-temizligi', cat='Su kalitesi', art='jug', related=['water', 'aysu', 'hayat'],
        title='Sebil ve Damacana Pompası Nasıl Temizlenir? | Alanyam Ticaret',
        desc='Sebil ve damacana pompası temizliği adım adım: ne sıklıkla, hangi malzemeyle? Damacana suyun tadını koruyan saklama ipuçları.',
        h1='Sebil ve damacana pompası nasıl temizlenir?',
        answer='Sebil ve damacana pompası, suyun tadını ve hijyenini korumak için düzenli temizlenmelidir. Genel öneri, pompayı ve sebilin su haznesini her damacana değişiminde durulamak ve birkaç haftada bir sıcak suyla, gıdaya uygun bir temizleyiciyle temizleyip iyice durulamaktır. Cihazınızın kullanım kılavuzundaki talimatlar önceliklidir.',
        body=[
            ('Damacana pompası temizliği', '''<ol><li>Pompayı damacanadan çıkarın, mümkünse parçalarına ayırın.</li><li>Ilık suda, gıdaya uygun bir deterjanla yıkayın.</li><li>Hortumun içinden bol su geçirerek durulayın.</li><li>Kurumaya bırakıp yeni damacanaya takın.</li></ol>'''),
            ('Sebil temizliği', '''<ol><li>Sebilin fişini çekin, damacanayı çıkarın.</li><li>Haznedeki suyu musluklardan boşaltın.</li><li>Kullanım kılavuzunda önerilen temizleyiciyle hazneyi temizleyin.</li><li>Bol suyla birkaç kez durulayın, muslukları da silin.</li></ol>'''),
            ('Damacana nasıl saklanır?', '''<ul><li>Doğrudan güneş almayan, serin ve temiz bir yerde saklayın.</li><li>Kimyasal ve kokulu ürünlerden uzak tutun.</li><li>Açılan damacanayı kısa sürede tüketin.</li><li>Kapağı ve mührü sağlam olmayan damacanayı kullanmayın.</li></ul>
<p>Su kalitesini etikette nasıl okuyacağınızı <a href="/blog/kaynak-suyu-ile-icme-suyu-farki/">kaynak suyu ve içme suyu farkı</a> yazımızda anlattık.</p>'''),
        ],
        faq=[('Sebil ne sıklıkla temizlenmeli?', 'Cihaz kılavuzu önceliklidir; genel olarak birkaç haftada bir ayrıntılı temizlik önerilir.'),
             ('Damacana güneşte kalırsa ne olur?', 'Güneş ve ısı plastik ambalajlı suyun tadını bozabilir; damacanayı gölgede saklayın.'),
             ('Pompayı neyle temizlemeliyim?', 'Ilık su ve gıdaya uygun bir deterjanla yıkayıp bol suyla durulayın.')],
        sources=[],
    ),
]
