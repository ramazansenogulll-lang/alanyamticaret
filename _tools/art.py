# -*- coding: utf-8 -*-
"""Sitede kullanılan çizimler (stok fotoğraf yerine). Gerçek fotoğraflar gelince değiştirilecek."""

_n = [0]


def _id(p):
    _n[0] += 1
    return f"{p}{_n[0]}"


def cylinder(label="İpragaz", body1="#1d6f93", body2="#6fc3e0", w=None):
    g = _id("cy")
    wa = f' width="{w}"' if w else ''
    return f'''<svg viewBox="0 0 200 300"{wa} role="img" aria-label="{label} tüp"><defs><linearGradient id="{g}" x1="0" x2="1"><stop offset="0" stop-color="{body1}"/><stop offset=".42" stop-color="{body2}"/><stop offset="1" stop-color="{body1}"/></linearGradient></defs>
<path d="M62 50V26a12 12 0 0 1 12-12h52a12 12 0 0 1 12 12v24" fill="none" stroke="#5f6f78" stroke-width="10" stroke-linecap="round"/>
<rect x="86" y="38" width="28" height="22" rx="4" fill="#9aa8af"/><rect x="92" y="30" width="16" height="10" rx="2" fill="#0b84a8"/>
<path d="M40 96c0-26 22-38 60-38s60 12 60 38v152c0 14-9 22-22 22H62c-13 0-22-8-22-22z" fill="url(#{g})"/>
<rect x="40" y="146" width="120" height="44" fill="#fff" opacity=".93"/>
<text x="100" y="175" text-anchor="middle" font-family="Manrope,Arial,sans-serif" font-weight="800" font-size="19" fill="#0f2530">{label}</text>
<rect x="58" y="84" width="9" height="160" rx="4.5" fill="#fff" opacity=".28"/>
<rect x="50" y="266" width="100" height="24" rx="5" fill="#33434b"/></svg>'''


def jug(label="Su", tint="#0a84b8", cap="#0a6a8a", w=None):
    g = _id("jg")
    wa = f' width="{w}"' if w else ''
    return f'''<svg viewBox="0 0 200 300"{wa} role="img" aria-label="{label} 19 L damacana"><defs><linearGradient id="{g}" x1="0" x2="1"><stop offset="0" stop-color="{tint}" stop-opacity=".55"/><stop offset=".45" stop-color="#dff4fc" stop-opacity=".9"/><stop offset="1" stop-color="{tint}" stop-opacity=".6"/></linearGradient></defs>
<rect x="80" y="8" width="40" height="22" rx="6" fill="{cap}"/>
<path d="M86 30h28v20c0 8 6 12 14 17l22 13c14 8 18 18 18 32v148c0 18-10 28-28 28H60c-18 0-28-10-28-28V112c0-14 4-24 18-32l22-13c8-5 14-9 14-17z" fill="url(#{g})" stroke="{tint}" stroke-opacity=".45" stroke-width="3"/>
<path d="M40 140h120M40 236h120" stroke="{tint}" stroke-opacity=".35" stroke-width="3"/>
<rect x="44" y="156" width="112" height="64" rx="10" fill="#fff" opacity=".95"/>
<text x="100" y="186" text-anchor="middle" font-family="Manrope,Arial,sans-serif" font-weight="800" font-size="21" fill="{cap}">{label}</text>
<text x="100" y="208" text-anchor="middle" font-family="Manrope,Arial,sans-serif" font-weight="700" font-size="13" fill="#557080">19 L</text>
<rect x="52" y="96" width="9" height="150" rx="4.5" fill="#fff" opacity=".5"/></svg>'''


def bottle(tint="#0a84b8", w=None, label="1,5 L"):
    g = _id("bt")
    wa = f' width="{w}"' if w else ''
    return f'''<svg viewBox="0 0 80 200"{wa} role="img" aria-label="{label} şişe su"><defs><linearGradient id="{g}" x1="0" x2="1"><stop offset="0" stop-color="{tint}" stop-opacity=".45"/><stop offset=".5" stop-color="#eaf8fd"/><stop offset="1" stop-color="{tint}" stop-opacity=".5"/></linearGradient></defs>
<rect x="30" y="4" width="20" height="14" rx="3" fill="{tint}"/>
<path d="M32 18h16v14c0 6 14 12 14 30v120c0 9-6 14-14 14H32c-8 0-14-5-14-14V62c0-18 14-24 14-30z" fill="url(#{g})" stroke="{tint}" stroke-opacity=".4" stroke-width="2"/>
<rect x="18" y="92" width="44" height="34" fill="#fff" opacity=".93"/><text x="40" y="114" text-anchor="middle" font-family="Manrope,Arial,sans-serif" font-weight="800" font-size="11" fill="#0f2530">{label}</text></svg>'''


def soda(label="Soda", tint="#1c7cc0", cap="#13588a", w=None):
    g = _id("sd")
    wa = f' width="{w}"' if w else ''
    return f'''<svg viewBox="0 0 80 200"{wa} role="img" aria-label="{label} maden suyu"><defs><linearGradient id="{g}" x1="0" x2="1"><stop offset="0" stop-color="{tint}" stop-opacity=".55"/><stop offset=".5" stop-color="#eef9fd"/><stop offset="1" stop-color="{tint}" stop-opacity=".6"/></linearGradient></defs>
<rect x="30" y="10" width="20" height="10" rx="2" fill="#9aa8af"/>
<path d="M32 20h16v26c0 10 16 16 16 34v96c0 9-6 14-14 14H30c-8 0-14-5-14-14V80c0-18 16-24 16-34z" fill="url(#{g})" stroke="{tint}" stroke-opacity=".5" stroke-width="2"/>
<circle cx="30" cy="150" r="2.5" fill="#fff" opacity=".8"/><circle cx="44" cy="166" r="2" fill="#fff" opacity=".8"/><circle cx="38" cy="132" r="1.8" fill="#fff" opacity=".8"/>
<rect x="16" y="96" width="48" height="30" fill="#fff" opacity=".95"/><text x="40" y="115" text-anchor="middle" font-family="Manrope,Arial,sans-serif" font-weight="800" font-size="10" fill="{cap}">{label}</text></svg>'''


def cup(label="Aysu", tint="#0a84b8", w=None):
    g = _id("cp")
    wa = f' width="{w}"' if w else ''
    return f'''<svg viewBox="0 0 120 140"{wa} role="img" aria-label="{label} bardak su"><defs><linearGradient id="{g}" x1="0" x2="1"><stop offset="0" stop-color="{tint}" stop-opacity=".4"/><stop offset=".5" stop-color="#eef9fd"/><stop offset="1" stop-color="{tint}" stop-opacity=".45"/></linearGradient></defs>
<path d="M22 30h76l-8 96c-1 6-5 9-11 9H41c-6 0-10-3-11-9z" fill="url(#{g})" stroke="{tint}" stroke-opacity=".5" stroke-width="2"/>
<rect x="16" y="20" width="88" height="12" rx="4" fill="#dfe9ee" stroke="{tint}" stroke-opacity=".5"/>
<text x="60" y="30" text-anchor="middle" font-family="Manrope,Arial,sans-serif" font-weight="800" font-size="10" fill="{tint}">{label}</text>
<path d="M30 70c20 8 40-8 60 0" stroke="#fff" stroke-width="3" fill="none" opacity=".7"/></svg>'''


def _inner(svg, x, y, w, h):
    """Bir svg'yi sahne içine yerleştir."""
    s = svg.replace('<svg ', f'<svg x="{x}" y="{y}" width="{w}" height="{h}" ', 1)
    return s


def scene(kind, labels=None):
    """Hero çizimi: güneş, Kızıl Kule silueti, deniz ve ürünler."""
    labels = labels or {}
    items = ''
    if kind == 'cyl':
        items = _inner(cylinder(labels.get('gas', 'İpragaz')), 175, 95, 210, 315)
    elif kind == 'jug':
        b = labels.get('brand', 'Su')
        items = _inner(jug(b), 150, 95, 210, 315) + _inner(bottle(label='1,5 L'), 345, 230, 76, 190) + _inner(bottle(label='0,5 L'), 95, 280, 56, 140)
    elif kind == 'jugs':
        items = (_inner(jug('Aysu', '#0a84b8', '#0a6a8a'), 60, 130, 170, 255) + _inner(jug('Madran', '#3a8fc4', '#1f6996'), 300, 130, 170, 255)
                 + _inner(jug('Hayat', '#2f6fd6', '#1d4fa3'), 175, 90, 190, 285))
    elif kind == 'soda':
        b = labels.get('brand', 'Soda')
        t, c = labels.get('colors', ('#1c7cc0', '#13588a'))
        items = (_inner(soda(b, t, c), 120, 170, 100, 250) + _inner(soda(b, t, c), 215, 120, 120, 300)
                 + _inner(soda(b, t, c), 330, 170, 100, 250))
    else:  # mix
        items = (_inner(cylinder(labels.get('gas', 'İpragaz')), 70, 110, 190, 290) + _inner(jug(labels.get('brand', 'Aysu')), 250, 105, 200, 300)
                 + _inner(bottle(label='1,5 L'), 425, 260, 64, 160))
    return f'''<svg class="art" viewBox="0 0 520 460" aria-hidden="true">
<circle cx="390" cy="96" r="70" fill="#dff3fa"/><circle cx="390" cy="96" r="46" fill="#bfe6f3"/>
<g fill="#8fc3d6" opacity=".55"><path d="M40 300V196l10-8h70l10 8v104z"/><path d="M36 196h102v-14h-10v8h-12v-8h-12v8h-12v-8h-12v8h-12v-8h-12v8h-10z"/><rect x="74" y="230" width="20" height="30" rx="10" fill="#5d9cb5"/></g>
<path d="M0 330c60-18 120-18 180 0s120 18 180 0 120-18 160-8v138H0z" fill="#bfe6f3"/>
<path d="M0 360c60-14 130-14 190 2s120 14 180-2 110-10 150-2v102H0z" fill="#8fd2ea"/>
{items}
</svg>'''


def logo():
    return '''<svg viewBox="0 0 48 48" aria-hidden="true"><defs><linearGradient id="lg1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b84a8"/><stop offset="1" stop-color="#063246"/></linearGradient></defs><rect width="48" height="48" rx="14" fill="url(#lg1)"/><path d="M17 12c4 6 8 9 8 15a8 8 0 0 1-16 0c0-6 4-9 8-15z" fill="#fff"/><path d="M33 16c1 4 6 6 6 12a6.5 6.5 0 0 1-13 0c0-3 1.5-5 3.5-6.5-.2 2 .6 3.6 2 4 .4-3-.4-6.6 1.5-9.5z" fill="#7fd3ee"/></svg>'''


ICONS = {
    'phone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
    'wa': '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4a.5.5 0 0 0 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4 5.1 5.1 0 0 0 3.2.7 2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>',
    'clock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    'truck': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="17.5" r="2"/><circle cx="17" cy="17.5" r="2"/></svg>',
    'shield': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
    'home': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/></svg>',
    'drop': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" aria-hidden="true"><path d="M12 3c3.5 5 6 8 6 11.5a6 6 0 0 1-12 0C6 11 8.5 8 12 3z"/></svg>',
    'flame': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" aria-hidden="true"><path d="M12 3c1 4 6 6 6 11a6 6 0 0 1-12 0c0-3 1.5-5 3.5-6.5 0 2 .8 3.5 2.3 4 .4-3.5-.8-6.5.2-8.5z"/></svg>',
    'map': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
    'chat': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/></svg>',
    'party': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20l5-14 9 9z"/><path d="M14 4v2M19 9h2M17 6l1.5-1.5"/></svg>',
}
