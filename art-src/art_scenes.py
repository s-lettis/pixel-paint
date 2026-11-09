from h import *
ART=[]
def add(id,name,w,h,inner,vb="0 0 100 100",cat="Scenes",colors=20):
    ART.append(dict(id=id,cat=cat,name=name,w=w,h=h,svg=wrap(vb,inner),colors=colors))

# ---------- Sunset ----------
sky=['#2d1b69','#4b2a85','#7a3590','#b04292','#e85a7a','#ff8a5c','#ffc062']
s=[]
for i,c in enumerate(sky): s.append(f'<rect y="{i*8}" width="100" height="{8.4}" fill="{c}"/>')
s+=['<circle cx="50" cy="44" r="14" fill="#fff1a8"/>',
    '<polygon points="0,54 16,38 28,48 46,30 62,48 78,36 100,50 100,56 0,56" fill="#6a3a8a"/>',
    '<polygon points="0,58 22,44 42,56 64,42 100,58 100,60 0,60" fill="#442a6c"/>',
    '<rect y="54" width="100" height="16" fill="#8a3f88"/>',
    '<rect y="58" width="100" height="4" fill="#b85a86"/><rect y="62" width="100" height="4" fill="#e0725e"/><rect y="66" width="100" height="4" fill="#f5a05c"/>',
    '<rect x="44" y="56" width="12" height="3" fill="#fff1a8"/><rect x="46" y="60" width="8" height="3" fill="#fff1a8"/><rect x="47" y="64" width="6" height="3" fill="#ffe08a"/>',
    '<polygon points="0,60 0,36 4,44 6,36 10,46 12,40 16,52 20,60" fill="#1d1236"/>',
    '<polygon points="82,60 86,44 88,50 90,38 94,52 96,46 100,60" fill="#1d1236"/>',
    '<path d="M62 18 l4 -3 l4 3 M74 24 l3 -2 l3 2" stroke="#2a1a4a" stroke-width="1.8" fill="none"/>']
add('sc-sunset','Mountain Sunset',50,35,"".join(s),vb="0 0 100 70",colors=22)

# ---------- Hot air balloon ----------
s=['<rect width="100" height="100" fill="#8fd3f4"/><rect y="60" width="100" height="40" fill="#b9e6f9"/>',
   '<ellipse cx="20" cy="22" rx="14" ry="6" fill="#fff"/><ellipse cx="30" cy="18" rx="9" ry="5" fill="#fff"/>',
   '<ellipse cx="84" cy="46" rx="14" ry="5" fill="#fff"/><ellipse cx="76" cy="42" rx="8" ry="4" fill="#fff"/>',
   '<ellipse cx="22" cy="108" rx="50" ry="26" fill="#66bb6a"/><ellipse cx="80" cy="110" rx="46" ry="24" fill="#43a047"/>',
   '<path d="M50 6 C 22 6, 16 40, 36 62 L 64 62 C 84 40, 78 6, 50 6 Z" fill="#e53935"/>',
   '<clipPath id="bl"><path d="M50 6 C 22 6, 16 40, 36 62 L 64 62 C 84 40, 78 6, 50 6 Z"/></clipPath>',
   '<g clip-path="url(#bl)"><rect x="26" y="0" width="12" height="70" fill="#ffc107"/><rect x="50" y="0" width="12" height="70" fill="#ffc107"/>'
   '<rect x="38" y="0" width="12" height="70" fill="#1e88e5"/><rect x="62" y="0" width="12" height="70" fill="#1e88e5"/>'
   '<rect x="0" y="24" width="100" height="5" fill="#fff"/></g>',
   '<ellipse cx="38" cy="22" rx="3" ry="6" fill="#fff" opacity=".55" transform="rotate(20 38 22)"/>',
   '<path d="M36 62 L44 76 M64 62 L56 76 M50 62 L50 76" stroke="#5d4037" stroke-width="1.8"/>',
   '<rect x="42" y="76" width="16" height="12" fill="#8d6e63"/><rect x="42" y="76" width="16" height="3" fill="#6d4c41"/>',
   '<path d="M42 82 L58 82 M42 85 L58 85" stroke="#6d4c41" stroke-width="1.4"/>',
   '<path d="M10 56 l3 -2 l3 2 M26 62 l3 -2 l3 2" stroke="#37474f" stroke-width="1.6" fill="none"/>']
add('sc-balloon','Hot Air Balloon',40,40,"".join(s),colors=16)
