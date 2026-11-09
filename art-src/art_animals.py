from h import *
ART=[]
def add(id,name,w,h,inner,vb="0 0 100 100",cat="Animals",colors=20):
    ART.append(dict(id=id,cat=cat,name=name,w=w,h=h,svg=wrap(vb,inner),colors=colors))

# ---------- Cat ----------
s=['<rect width="100" height="100" fill="#bfe3e0"/>', snow(8,16,0,100,0,100,1.8,'#e6f5f3'),
   '<ellipse cx="50" cy="104" rx="36" ry="22" fill="#f5a142"/>',
   '<polygon points="20,44 24,10 48,28" fill="#f5a142"/><polygon points="80,44 76,10 52,28" fill="#f5a142"/>',
   '<polygon points="27,36 29,19 40,28" fill="#f48fb1"/><polygon points="73,36 71,19 60,28" fill="#f48fb1"/>',
   '<ellipse cx="50" cy="56" rx="31" ry="27" fill="#f5a142"/>',
   '<polygon points="50,29 46.5,41 53.5,41" fill="#d9791a"/><polygon points="40,32 38,42 45,41" fill="#d9791a"/><polygon points="60,32 62,42 55,41" fill="#d9791a"/>',
   '<ellipse cx="41" cy="68" rx="11" ry="9" fill="#fff3e0"/><ellipse cx="59" cy="68" rx="11" ry="9" fill="#fff3e0"/>',
   '<ellipse cx="37" cy="53" rx="6.4" ry="7" fill="#9ccc65"/><ellipse cx="63" cy="53" rx="6.4" ry="7" fill="#9ccc65"/>',
   '<ellipse cx="37" cy="53" rx="2.2" ry="5" fill="#212121"/><ellipse cx="63" cy="53" rx="2.2" ry="5" fill="#212121"/>',
   '<circle cx="35.2" cy="50.6" r="1.4" fill="#fff"/><circle cx="61.2" cy="50.6" r="1.4" fill="#fff"/>',
   '<polygon points="46,62 54,62 50,67" fill="#f06292"/>',
   '<path d="M50 67 Q 50 74 43 73 M50 67 Q 50 74 57 73" stroke="#6d4c41" stroke-width="2.2" fill="none"/>',
   '<path d="M34 66 L10 60 M34 70 L10 72 M66 66 L90 60 M66 70 L90 72" stroke="#ffffff" stroke-width="2.4"/>',
   '<rect x="24" y="82" width="52" height="7" rx="3" fill="#e53935"/><circle cx="50" cy="93" r="5" fill="#ffd54f"/><rect x="48.6" y="91" width="2.8" height="5" fill="#f9a825"/>']
add('ani-cat','Tabby Cat',40,40,"".join(s),colors=18)

# ---------- Owl ----------
s=['<rect width="100" height="100" fill="#273469"/>',
   '<circle cx="78" cy="22" r="13" fill="#fff3b0"/><circle cx="73" cy="18" r="3.4" fill="#f0e08c"/><circle cx="83" cy="27" r="2.6" fill="#f0e08c"/>',
   f'<polygon points="{star(14,16,5,2.2)}" fill="#fff3b0"/><polygon points="{star(34,10,3.6,1.6)}" fill="#fff3b0"/><polygon points="{star(20,40,3.6,1.6)}" fill="#fff3b0"/>',
   '<rect x="-2" y="78" width="104" height="8" rx="3" fill="#6d4c41"/><rect x="-2" y="78" width="104" height="3" fill="#8a6a58"/>',
   '<polygon points="30,34 28,16 44,29" fill="#6d4c41"/><polygon points="70,34 72,16 56,29" fill="#6d4c41"/>',
   '<ellipse cx="50" cy="56" rx="25" ry="28" fill="#8d6e63"/>',
   '<ellipse cx="27" cy="62" rx="9" ry="19" fill="#6d4c41" transform="rotate(8 27 62)"/><ellipse cx="73" cy="62" rx="9" ry="19" fill="#6d4c41" transform="rotate(-8 73 62)"/>',
   '<ellipse cx="50" cy="67" rx="14" ry="18" fill="#d7b899"/>',
   '<path d="M42 58 q3 4 6 0 M52 58 q3 4 6 0 M42 67 q3 4 6 0 M52 67 q3 4 6 0 M46 76 q4 4 8 0" stroke="#a98467" stroke-width="2.2" fill="none"/>',
   '<circle cx="40" cy="44" r="12" fill="#efe3d1"/><circle cx="60" cy="44" r="12" fill="#efe3d1"/>',
   '<circle cx="40" cy="44" r="7.6" fill="#ffca28"/><circle cx="60" cy="44" r="7.6" fill="#ffca28"/>',
   '<circle cx="40" cy="44" r="3.8" fill="#111"/><circle cx="60" cy="44" r="3.8" fill="#111"/>',
   '<circle cx="38.6" cy="42.4" r="1.4" fill="#fff"/><circle cx="58.6" cy="42.4" r="1.4" fill="#fff"/>',
   '<polygon points="46.5,49 53.5,49 50,58" fill="#ff9800"/>',
   '<polygon points="38,80 42,80 40,86" fill="#ff9800"/><polygon points="43,80 47,80 45,86" fill="#ff9800"/>',
   '<polygon points="53,80 57,80 55,86" fill="#ff9800"/><polygon points="58,80 62,80 60,86" fill="#ff9800"/>',
   '<ellipse cx="20" cy="76" rx="6" ry="3" fill="#2e7d32" transform="rotate(-25 20 76)"/><ellipse cx="82" cy="76" rx="6" ry="3" fill="#43a047" transform="rotate(25 82 76)"/>']
add('ani-owl','Night Owl',48,48,"".join(s),colors=20)

# ---------- Fox ----------
half=('<polygon points="18,48 22,8 48,28" fill="#e8711a"/><polygon points="25,38 27,19 38,29" fill="#2f2220"/>'
      '<polygon points="16,50 50,26 50,92 28,76" fill="#ee7d20"/>'
      '<polygon points="16,50 38,60 50,66 50,92 28,76" fill="#fff4e6"/>'
      '<ellipse cx="36" cy="52" rx="4.2" ry="3.4" fill="#2b2b2b" transform="rotate(14 36 52)"/><circle cx="34.6" cy="50.8" r="1.2" fill="#fff"/>'
      '<circle cx="24" cy="62" r="1.2" fill="#c9885a"/><circle cx="28" cy="66" r="1.2" fill="#c9885a"/>')
s=['<rect width="100" height="100" fill="#d5ecd4"/>',
   '<ellipse cx="14" cy="88" rx="12" ry="6" fill="#f9a825"/><ellipse cx="88" cy="90" rx="12" ry="6" fill="#e65100"/>',
   half, f'<g transform="translate(100 0) scale(-1 1)">{half}</g>',
   '<polygon points="42,70 58,70 50,92" fill="#fff4e6"/>',
   '<ellipse cx="50" cy="88" rx="6" ry="4.6" fill="#2b2b2b"/><ellipse cx="48" cy="86.6" rx="1.8" ry="1" fill="#6d6d6d"/>']
add('ani-fox','Fox',40,40,"".join(s),colors=14)

# ---------- Penguin ----------
s=['<rect width="100" height="100" fill="#bde4f7"/>', snow(9,24,0,100,0,100,1.7),
   '<polygon points="0,100 0,70 22,56 40,76 50,100" fill="#9fd3ee"/><polygon points="60,100 74,62 100,50 100,100" fill="#9fd3ee"/>',
   '<ellipse cx="50" cy="104" rx="70" ry="16" fill="#f3f9ff"/>',
   '<ellipse cx="50" cy="56" rx="25" ry="34" fill="#263238"/>',
   '<ellipse cx="27" cy="62" rx="6.4" ry="17" fill="#1b252a" transform="rotate(14 27 62)"/><ellipse cx="73" cy="62" rx="6.4" ry="17" fill="#1b252a" transform="rotate(-14 73 62)"/>',
   '<ellipse cx="50" cy="64" rx="16" ry="25" fill="#ffffff"/>',
   '<circle cx="41" cy="34" r="6" fill="#fff"/><circle cx="59" cy="34" r="6" fill="#fff"/>',
   '<circle cx="42" cy="35" r="2.8" fill="#111"/><circle cx="58" cy="35" r="2.8" fill="#111"/>',
   '<polygon points="44,41 56,41 50,50" fill="#ff9800"/>',
   '<circle cx="36" cy="43" r="3" fill="#f8a5b8"/><circle cx="64" cy="43" r="3" fill="#f8a5b8"/>',
   '<rect x="27" y="52" width="46" height="8" rx="3" fill="#e53935"/><rect x="34" y="52" width="4" height="8" fill="#fff"/><rect x="46" y="52" width="4" height="8" fill="#fff"/><rect x="58" y="52" width="4" height="8" fill="#fff"/>',
   '<polygon points="60,58 70,58 72,76 63,76" fill="#c62828"/>',
   '<ellipse cx="39" cy="92" rx="9" ry="3.6" fill="#ff9800"/><ellipse cx="61" cy="92" rx="9" ry="3.6" fill="#ff9800"/>']
add('ani-penguin','Penguin',40,40,"".join(s),colors=16)
