from h import *
ART=[]
def add(id,name,w,h,inner,vb="0 0 100 100",cat="Christmas",colors=20):
    ART.append(dict(id=id,cat=cat,name=name,w=w,h=h,svg=wrap(vb,inner),colors=colors))

# ---------- Tree ----------
s=['<rect width="100" height="100" fill="#15204f"/>', snow(1,22,0,100,0,72,1.5),
   '<ellipse cx="50" cy="102" rx="72" ry="15" fill="#eef3fb"/><ellipse cx="50" cy="106" rx="60" ry="11" fill="#d9e4f5"/>',
   '<rect x="44" y="78" width="12" height="12" fill="#6d4c41"/>',
   '<polygon points="50,38 12,82 88,82" fill="#1b6e2e"/>',
   '<polygon points="50,24 18,62 82,62" fill="#2e8b3a"/>',
   '<polygon points="50,12 28,44 72,44" fill="#3da34a"/>',
   '<path d="M33 44 Q 50 52 67 44" stroke="#ffd54f" stroke-width="2.8" fill="none"/>',
   '<path d="M26 62 Q 50 72 74 62" stroke="#ffd54f" stroke-width="2.8" fill="none"/>',
   '<path d="M19 80 Q 50 92 81 80" stroke="#ffd54f" stroke-width="2.8" fill="none"/>',
   f'<polygon points="{star(50,12,8,3.6)}" fill="#ffe14d"/>']
for x,y,c in[(44,35,'#e53935'),(57,30,'#42a5f5'),(38,54,'#ffca28'),(60,52,'#f06292'),(50,46,'#e53935'),
             (30,72,'#42a5f5'),(46,70,'#e53935'),(64,74,'#ffca28'),(76,76,'#f06292'),(54,84,'#42a5f5')]:
    s.append(f'<circle cx="{x}" cy="{y}" r="3.5" fill="{c}"/>')
s+=['<rect x="6" y="84" width="20" height="14" fill="#e53935"/><rect x="14" y="84" width="4" height="14" fill="#fff"/>',
    '<rect x="72" y="86" width="22" height="12" fill="#43a047"/><rect x="81" y="86" width="4" height="12" fill="#ffd54f"/>',
    bow(16,83,'#fff','#e0e0e0',.6),bow(83,85,'#ffd54f','#f9a825',.6)]
add('xmas-tree','Christmas Tree',48,48,"".join(s),colors=22)

# ---------- Snowman ----------
s=['<rect width="100" height="100" fill="#243a8f"/>', snow(2,30,0,100,0,70,1.5),
   '<circle cx="82" cy="18" r="9" fill="#fff3b0"/>',
   '<ellipse cx="50" cy="100" rx="70" ry="22" fill="#eef3fb"/>',
   '<circle cx="52" cy="78" r="21" fill="#c3d6ef"/><circle cx="48" cy="74" r="19.5" fill="#fff"/>',
   '<circle cx="52" cy="52" r="15" fill="#c3d6ef"/><circle cx="48.5" cy="49" r="13.5" fill="#fff"/>',
   '<circle cx="52" cy="32" r="11" fill="#c3d6ef"/><circle cx="49" cy="29.5" r="9.8" fill="#fff"/>',
   '<path d="M36 52 L14 38 M20 41 L14 46 M14 38 L16 30" stroke="#6d4c41" stroke-width="2.6" fill="none"/>',
   '<path d="M64 52 L86 38 M80 41 L86 46 M86 38 L84 30" stroke="#6d4c41" stroke-width="2.6" fill="none"/>',
   '<rect x="40" y="10" width="18" height="12" fill="#212121"/><rect x="34" y="20" width="30" height="4" fill="#212121"/>',
   '<rect x="40" y="16" width="18" height="3.6" fill="#e53935"/>',
   '<circle cx="45" cy="29" r="2.4" fill="#212121"/><circle cx="54" cy="29" r="2.4" fill="#212121"/>',
   '<polygon points="49,32 65,35 49,38" fill="#fb8c00"/>',
   '<circle cx="42" cy="36" r="1.6" fill="#212121"/><circle cx="46" cy="38.5" r="1.6" fill="#212121"/><circle cx="52" cy="38.5" r="1.6" fill="#212121"/>',
   '<rect x="37" y="39" width="26" height="6" fill="#e53935"/><polygon points="55,44 63,44 64,60 57,60" fill="#c62828"/>',
   '<rect x="55" y="50" width="8" height="2.5" fill="#fff" opacity=".0"/>',
   '<circle cx="49" cy="55" r="2.4" fill="#212121"/><circle cx="49" cy="64" r="2.4" fill="#212121"/><circle cx="49" cy="73" r="2.4" fill="#212121"/>',
   '<rect x="10" y="88" width="20" height="3" fill="#cfe0f5"/>']
add('xmas-snowman','Snowman',40,40,"".join(s),colors=18)

# ---------- Gingerbread house ----------
s=['<rect width="100" height="100" fill="#bfe3ff"/>',
   '<ellipse cx="82" cy="18" rx="9" ry="9" fill="#fff6c7"/>',
   '<ellipse cx="50" cy="104" rx="76" ry="24" fill="#f4f8ff"/><ellipse cx="50" cy="108" rx="60" ry="16" fill="#dde9f7"/>',
   '<rect x="26" y="50" width="48" height="36" fill="#b06a3b"/>',
   '<rect x="26" y="82" width="48" height="4" fill="#fff"/>',
   '<rect x="62" y="22" width="8" height="18" fill="#8d5a3a"/><rect x="60" y="20" width="12" height="4" fill="#fff"/>',
   '<polygon points="14,54 50,22 86,54" fill="#7a4a2b"/>',
   '<polyline points="14,54 50,22 86,54" stroke="#fff" stroke-width="3.2" fill="none"/>',
   '<polyline points="22,52 78,52" stroke="#fff" stroke-width="3.2" fill="none"/>',
   '<circle cx="36" cy="46" r="3.4" fill="#e53935"/><circle cx="50" cy="36" r="3.4" fill="#ffd54f"/><circle cx="64" cy="46" r="3.4" fill="#43a047"/>',
   '<circle cx="50" cy="47" r="3.4" fill="#42a5f5"/>',
   '<rect x="44" y="64" width="12" height="22" fill="#e53935"/><circle cx="50" cy="64" r="6" fill="#e53935"/>',
   '<circle cx="53.5" cy="76" r="1.5" fill="#ffd54f"/>',
   '<rect x="30" y="58" width="10" height="10" fill="#ffe082" stroke="#fff" stroke-width="1.6"/>',
   '<rect x="60" y="58" width="10" height="10" fill="#ffe082" stroke="#fff" stroke-width="1.6"/>',
   '<polygon points="10,86 18,66 26,86" fill="#2e7d32"/><polygon points="12,74 18,66 24,74" fill="#fff"/>',
   '<polygon points="76,88 84,64 92,88" fill="#388e3c"/><polygon points="79,74 84,64 89,74" fill="#fff"/>',
   '<rect x="17" y="86" width="2.6" height="4" fill="#5d4037"/><rect x="83" y="88" width="2.6" height="4" fill="#5d4037"/>']
add('xmas-gingerbread','Gingerbread House',48,48,"".join(s),colors=20)

# ---------- Stocking ----------
s=['<rect width="100" height="100" fill="#1e5a2e"/>', snow(3,26,0,100,0,100,1.5,'#9ccc65'),
   '<path d="M38 22 L62 22 L62 56 C 62 62, 78 62, 82 72 C 86 82, 74 88, 64 84 L 42 76 C 34 72, 38 62, 38 54 Z" fill="#d32f2f"/>',
   '<clipPath id="sk"><path d="M38 22 L62 22 L62 56 C 62 62, 78 62, 82 72 C 86 82, 74 88, 64 84 L 42 76 C 34 72, 38 62, 38 54 Z"/></clipPath>',
   '<g clip-path="url(#sk)"><path d="M30 34 L70 44 M30 46 L70 56" stroke="#fff" stroke-width="4" fill="none"/>'
   '<ellipse cx="78" cy="78" rx="9" ry="12" fill="#fff"/><ellipse cx="46" cy="72" rx="8" ry="8" fill="#2e7d32"/></g>',
   '<rect x="34" y="14" width="32" height="12" rx="5" fill="#fff"/>',
   '<circle cx="42" cy="20" r="1.8" fill="#e0e0e0"/><circle cx="52" cy="21" r="1.8" fill="#e0e0e0"/><circle cx="60" cy="19" r="1.8" fill="#e0e0e0"/>',
   '<circle cx="36" cy="10" r="4.6" fill="none" stroke="#ffd54f" stroke-width="2.4"/>',
   '<path d="M52 16 L52 6 C 52 -2, 66 -2, 66 6" stroke="#fff" stroke-width="5.4" fill="none"/>'
   '<path d="M52 16 L52 6 C 52 -2, 66 -2, 66 6" stroke="#e53935" stroke-width="5.4" fill="none" stroke-dasharray="3.4 3.4"/>',
   '<ellipse cx="22" cy="82" rx="9" ry="4.6" fill="#43a047" transform="rotate(-30 22 82)"/><ellipse cx="34" cy="88" rx="9" ry="4.6" fill="#66bb6a" transform="rotate(20 34 88)"/>',
   '<circle cx="27" cy="85" r="3.2" fill="#e53935"/><circle cx="22" cy="88" r="3.2" fill="#c62828"/>']
add('xmas-stocking','Stocking',40,40,"".join(s),colors=16)

# ---------- Wreath ----------
rnd=random.Random(5)
greens=['#1b5e20','#2e7d32','#43a047','#66bb6a']
s=['<rect width="100" height="100" fill="#f1e6d2"/><circle cx="50" cy="50" r="46" fill="#e8dcc6"/>',
   '<circle cx="50" cy="50" r="29" fill="none" stroke="#1b5e20" stroke-width="16"/>']
for i in range(0,360,8):
    a=math.radians(i); r=29+rnd.uniform(-4,4); x=50+r*math.cos(a); y=50+r*math.sin(a)
    s.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="9.5" ry="4.8" fill="{rnd.choice(greens)}" transform="rotate({i+90+rnd.uniform(-30,30):.0f} {x:.1f} {y:.1f})"/>')
for i in range(0,360,36):
    a=math.radians(i+10); r=29; x=50+r*math.cos(a); y=50+r*math.sin(a)
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.8" fill="#e53935"/>')
for i,(x,y) in enumerate([(24,30),(76,32),(18,58),(82,60)]):
    s.append(f'<ellipse cx="{x}" cy="{y}" rx="3.2" ry="4.6" fill="#8d6e63" transform="rotate({i*40} {x} {y})"/>')
s.append(bow(50,80,'#d32f2f','#b71c1c',1.25))
add('xmas-wreath','Wreath',48,48,"".join(s),colors=20)

# ---------- Candy canes ----------
def cane(d): return (f'<path d="{d}" stroke="#ffffff" stroke-width="11" fill="none"/>'
                     f'<path d="{d}" stroke="#e53935" stroke-width="11" fill="none" stroke-dasharray="5.5 5.5"/>')
D="M34 94 L34 40 C 34 14, 66 14, 66 40"
s=['<rect width="100" height="100" fill="#d4efe2"/>', snow(4,30,0,100,0,100,1.6,'#ffffff'),
   f'<g transform="rotate(-16 50 60)">{cane(D)}</g>',
   f'<g transform="translate(100 0) scale(-1 1) rotate(-16 50 60)">{cane(D)}</g>',
   bow(50,66,'#2e7d32','#c62828',1.5),
   '<ellipse cx="22" cy="86" rx="9" ry="4.6" fill="#2e7d32" transform="rotate(-30 22 86)"/><ellipse cx="34" cy="92" rx="9" ry="4.6" fill="#43a047" transform="rotate(20 34 92)"/>',
   '<circle cx="27" cy="89" r="3.2" fill="#e53935"/><circle cx="22" cy="92" r="3.2" fill="#c62828"/>']
add('xmas-canes','Candy Canes',40,40,"".join(s),colors=14)

# ---------- Ornaments ----------
s=['<rect width="100" height="100" fill="#1f3b73"/>', snow(6,20,0,100,20,100,1.4,'#8fa8d8'),
   '<path d="M-4 8 Q 50 14 104 6" stroke="#2e7d32" stroke-width="9" fill="none"/>']
for x in range(2,100,7): s.append(f'<ellipse cx="{x}" cy="{10+3*math.sin(x/9):.1f}" rx="5" ry="2.4" fill="#43a047" transform="rotate({40 if (x//7)%2 else -40} {x} 10)"/>')
def bauble(cx,cy,r,base,decor,cid):
    return (f'<line x1="{cx}" y1="9" x2="{cx}" y2="{cy-r-3}" stroke="#ffd54f" stroke-width="1.8"/>'
            f'<clipPath id="{cid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{base}"/><g clip-path="url(#{cid})">{decor}</g>'
            f'<rect x="{cx-4}" y="{cy-r-5}" width="8" height="6" fill="#ffca28"/>'
            f'<ellipse cx="{cx-r*0.4:.1f}" cy="{cy-r*0.4:.1f}" rx="{r*0.2:.1f}" ry="{r*0.3:.1f}" fill="#fff" opacity=".8" transform="rotate(-35 {cx-r*0.4:.1f} {cy-r*0.4:.1f})"/>')
s.append(bauble(24,54,18,'#d32f2f','<path d="M4 50 Q 14 44 24 50 T 44 50 L44 58 Q 34 52 24 58 T 4 58 Z" fill="#fff"/>','b1'))
s.append(bauble(54,72,21,'#1e88e5','<rect x="30" y="58" width="50" height="5" fill="#ffd54f"/><rect x="30" y="68" width="50" height="5" fill="#ffd54f"/><rect x="30" y="78" width="50" height="5" fill="#ffd54f"/>','b2'))
dots=''.join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="#fff"/>' for x in (66,74,82,90) for y in (36,44,52,60) if (x+y)%16==0 or (x//8+y//8)%2==0)
s.append(bauble(80,46,16,'#2e7d32',dots,'b3'))
add('xmas-ornaments','Ornaments',40,40,"".join(s),colors=18)

# ---------- Gifts ----------
s=['<rect width="100" height="100" fill="#fff1d6"/><rect y="84" width="100" height="16" fill="#c9a27a"/><rect y="84" width="100" height="3" fill="#b5895d"/>',
   '<rect x="12" y="46" width="46" height="40" fill="#1e88e5"/><rect x="9" y="38" width="52" height="10" fill="#1976d2"/>',
   '<rect x="32" y="38" width="6" height="48" fill="#e53935"/>',
   bow(35,34,'#e53935','#b71c1c',1.0),
   '<rect x="56" y="60" width="34" height="26" fill="#43a047"/><rect x="54" y="55" width="38" height="7" fill="#388e3c"/>',
   '<rect x="70" y="55" width="6" height="31" fill="#ffd54f"/>',
   bow(73,52,'#ffd54f','#f9a825',.8),
   '<rect x="64" y="38" width="18" height="12" fill="#e53935"/><rect x="71" y="38" width="4" height="12" fill="#fff"/>',
   '<rect x="64" y="38" width="18" height="3" fill="#c62828"/>',
   f'<polygon points="{star(14,18,7,3)}" fill="#ffc107"/><polygon points="{star(86,16,5,2.2)}" fill="#ef5350"/>']
add('xmas-gifts','Presents',40,40,"".join(s),colors=16)

# ---------- Santa hat ----------
s=['<rect width="100" height="100" fill="#2f6db5"/>', snow(7,30,0,100,0,100,1.7),
   '<path d="M20 72 Q 28 22 62 20 Q 78 30 82 72 Z" fill="#d32f2f"/>',
   '<path d="M62 20 Q 78 30 82 72 L 66 72 Q 66 40 56 24 Z" fill="#b71c1c"/>',
   '<circle cx="62" cy="16" r="10" fill="#fff"/><circle cx="58" cy="13" r="3" fill="#eceff1"/>',
   '<rect x="12" y="66" width="78" height="18" rx="9" fill="#fff"/>',
   '<rect x="12" y="78" width="78" height="6" rx="3" fill="#e3e8ee"/>',
   '<circle cx="26" cy="74" r="1.8" fill="#e3e8ee"/><circle cx="44" cy="72" r="1.8" fill="#e3e8ee"/><circle cx="62" cy="75" r="1.8" fill="#e3e8ee"/><circle cx="78" cy="72" r="1.8" fill="#e3e8ee"/>',
   '<ellipse cx="50" cy="96" rx="60" ry="9" fill="#eef3fb"/>']
add('xmas-hat','Santa Hat',40,40,"".join(s),colors=14)
