# -*- coding: utf-8 -*-
"""Kaynak fotoğrafları (_kaynak/) AVIF + WebP boylarına çevirir -> assets/img/.
Çalıştır: python -X utf8 _tools/gorseller.py"""
import os
from PIL import Image, ImageOps

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC = os.path.join(ROOT, '_kaynak')
OUT = os.path.join(ROOT, 'assets', 'img')

# kaynak dosya -> yayın adı (SEO uyumlu)
PHOTOS = {
    'dukkan.png': 'alanyam-ticaret-ipragaz-tup-su-bayii-alanya',
    'vitrin.png': 'ipragaz-alanya-tup-bayi-vitrin',
    'su-bayii.png': 'alanya-su-bayii-aysu-madran-hayat-damacana',
    'ic-mekan.png': 'alanya-damacana-su-bayii-ic-mekan',
    'hero.png': 'alanya-tup-ve-su-siparisi-mutfak',
}
WIDTHS = [480, 800, 1200]


def main():
    os.makedirs(OUT, exist_ok=True)
    info = {}
    for src, name in PHOTOS.items():
        im = ImageOps.exif_transpose(Image.open(os.path.join(SRC, src))).convert('RGB')
        w0, h0 = im.size
        info[name] = (w0, h0)
        for w in WIDTHS:
            if w > w0:
                continue
            r = im.resize((w, round(h0 * w / w0)), Image.LANCZOS)
            r.save(os.path.join(OUT, f'{name}-{w}.avif'), quality=55, speed=6)
            r.save(os.path.join(OUT, f'{name}-{w}.webp'), quality=78, method=6)
        print(name, w0, h0)
    return info


if __name__ == '__main__':
    main()
