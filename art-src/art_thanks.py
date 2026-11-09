from h import *
ART=[]
def add(id,name,w,h,inner,vb="0 0 100 100",cat="Thanksgiving",colors=20):
    ART.append(dict(id=id,cat=cat,name=name,w=w,h=h,svg=wrap(vb,inner),colors=colors))

# ---------- Turkey ----------
s=['<rect width="100" height="100" fill="#fde8cc"/>',
   '<ellipse cx="50" cy="108" rx="72" ry="24" fill="#7cb342"/>',
   '<ellipse cx="50" cy="112" rx="56" ry="16" fill="#8bc34a"/>']
cols=['#b71c1c','#ef6c00','#f9a825','#689f38','#8d3b0e','#ef6c00','#b71c1c']
lite=['#ef5350','#ffa726','#ffd54f','#9ccc65','#c0622d','#ffa726','#ef5350']
for i,a in enumerate(range(-72,73,24)):
    s.append(f'<g transform="rotate({a} 50 66)"><ellipse cx="50" cy="30" rx="9.5" ry="27" fill="{cols[i]}"/><ellipse cx="50" cy="32" rx="4.6" ry="17" fill="{lite[i]}"/></g>')
s+=['<ellipse cx="50" cy="72" rx="22" ry="21" fill="#7b4a24"/>',
    '<ellipse cx="50" cy="78" rx="13" ry="13" fill="#a56a37"/>',
    '<ellipse cx="33" cy="74" rx="7" ry="13" fill="#5d3a1a" transform="rotate(12 33 74)"/>',
    '<ellipse cx="67" cy="74" rx="7" ry="13" fill="#5d3a1a" transform="rotate(-12 67 74)"/>',
    '<circle cx="50" cy="50" r="12" fill="#7b4a24"/>',
    '<polygon points="46,52 54,52 50,60" fill="#ffb300"/>',
    '<ellipse cx="53" cy="61" rx="3.2" ry="5.5" fill="#e53935"/>',
    '<circle cx="44.5" cy="49" r="3.6" fill="#fff"/><circle cx="55.5" cy="49" r="3.6" fill="#fff"/>',
    '<circle cx="45" cy="49.4" r="1.9" fill="#222"/><circle cx="55" cy="49.4" r="1.9" fill="#222"/>',
    '<rect x="42" y="26" width="16" height="12" fill="#263238"/><rect x="37" y="36" width="26" height="4" fill="#263238"/>',
    '<rect x="42" y="33" width="16" height="3.4" fill="#ffb300"/>',
    '<rect x="41" y="90" width="4.5" height="7" fill="#ff9800"/><rect x="54.5" y="90" width="4.5" height="7" fill="#ff9800"/>',
    '<rect x="37" y="95" width="12" height="3.2" fill="#ff9800"/><rect x="51" y="95" width="12" height="3.2" fill="#ff9800"/>']
add('thx-turkey','Turkey',48,48,"".join(s),colors=22)

# ---------- Pumpkin patch ----------
s=['<rect width="100" height="100" fill="#ffe3b3"/>',
   '<rect y="76" width="100" height="24" fill="#8d6e63"/><rect y="76" width="100" height="5" fill="#a1887f"/>',
   '<ellipse cx="14" cy="14" rx="7" ry="7" fill="#fff3c4"/>']
def pump(cx,cy,sx,c1,c2,c3):
    sc=sx/20
    return (f'<g transform="translate({cx} {cy}) scale({sc})">'
      f'<ellipse cx="-10" cy="0" rx="14" ry="19" fill="{c1}" stroke="#bf360c" stroke-width="1.6"/>'
      f'<ellipse cx="10" cy="0" rx="14" ry="19" fill="{c1}" stroke="#bf360c" stroke-width="1.6"/>'
      f'<ellipse cx="0" cy="0" rx="13" ry="21" fill="{c2}" stroke="#bf360c" stroke-width="1.6"/>'
      f'<rect x="-3.5" y="-27" width="7" height="10" rx="2" fill="{c3}"/></g>')
s.append(pump(50,56,20,'#ef6c00','#fb8c00','#5d4037'))
s.append(pump(17,72,10,'#f57c00','#ffa726','#5d4037'))
s.append(pump(84,73,11,'#ffa726','#ffb74d','#5d4037'))
s+=['<path d="M54 28 C 66 20 76 26 71 36" stroke="#558b2f" stroke-width="3" fill="none"/>',
    '<ellipse cx="72" cy="20" rx="9" ry="5" fill="#7cb342" transform="rotate(-28 72 20)"/>',
    '<ellipse cx="34" cy="26" rx="8" ry="4.6" fill="#689f38" transform="rotate(30 34 26)"/>',
    '<path d="M44 28 C 38 30 36 28 34 26" stroke="#558b2f" stroke-width="2.4" fill="none"/>']
add('thx-pumpkins','Pumpkin Patch',40,40,"".join(s),colors=18)

# ---------- Pumpkin pie ----------
pat=('<defs><pattern id="g" width="20" height="20" patternUnits="userSpaceOnUse">'
     '<rect width="20" height="20" fill="#ffffff"/><rect width="10" height="20" fill="#ef9a9a"/>'
     '<rect width="20" height="10" fill="#ef9a9a" opacity=".6"/></pattern></defs>')
s=[pat,'<rect width="100" height="100" fill="url(#g)"/>',
   '<ellipse cx="50" cy="80" rx="43" ry="11" fill="#cfd8dc"/><ellipse cx="50" cy="77" rx="43" ry="11" fill="#f5f5f5"/>',
   '<ellipse cx="50" cy="77" rx="33" ry="7" fill="#e3e8ea"/>',
   '<polygon points="22,72 78,72 66,44 34,44" fill="#e8891d"/>',
   '<polygon points="22,72 34,44 30,43 18,70" fill="#d9a05b"/><polygon points="78,72 66,44 70,43 82,70" fill="#d9a05b"/>',
   '<polygon points="20,70 80,70 79,78 21,78" fill="#d9a05b"/>',
   '<polygon points="22,72 78,72 78,70 22,70" fill="#c9852f"/>',
   '<polygon points="34,44 66,44 62,53 38,53" fill="#f6a940"/>',
   '<ellipse cx="50" cy="42" rx="17" ry="7" fill="#ece3d0"/><ellipse cx="50" cy="36" rx="12.5" ry="6" fill="#fffdf5"/>',
   '<ellipse cx="50" cy="30" rx="8" ry="5" fill="#ece3d0"/><ellipse cx="50" cy="26.5" rx="4.5" ry="3.6" fill="#fffdf5"/>',
   '<circle cx="44" cy="40" r="2" fill="#a1523a"/><circle cx="55" cy="41" r="2" fill="#a1523a"/><circle cx="50" cy="35" r="2" fill="#a1523a"/>',
   '<ellipse cx="22" cy="20" rx="9" ry="5" fill="#ef6c00" transform="rotate(-20 22 20)"/><ellipse cx="82" cy="22" rx="9" ry="5" fill="#c62828" transform="rotate(25 82 22)"/>']
add('thx-pie','Pumpkin Pie',40,40,"".join(s),colors=18)

# ---------- Cornucopia ----------
horn="M30 30 C 54 22, 80 44, 95 82 C 70 94, 40 86, 24 68 C 12 56, 18 38, 30 30 Z"
s=['<rect width="100" height="100" fill="#f4e3c1"/>',
   '<ellipse cx="50" cy="94" rx="46" ry="6" fill="#e5cf9f"/>',
   f'<path d="{horn}" fill="#b07a3f" stroke="#7a4e22" stroke-width="1.8"/>',
   f'<clipPath id="hc"><path d="{horn}"/></clipPath>',
   '<g clip-path="url(#hc)" stroke="#8a5a2b" stroke-width="2.6" fill="none">'
   '<path d="M44 26 Q 52 56 40 92"/><path d="M60 32 Q 70 62 56 96"/><path d="M76 46 Q 86 72 74 98"/></g>',
   '<ellipse cx="22" cy="50" rx="8" ry="19" fill="#6b4220" transform="rotate(-18 22 50)"/>',
   '<circle cx="15" cy="68" r="12" fill="#ef6c00" stroke="#bf360c" stroke-width="1.4"/><rect x="13" y="54" width="4.4" height="6" fill="#5d4037"/>',
   '<circle cx="14" cy="38" r="10" fill="#d32f2f"/><circle cx="10.5" cy="34.5" r="2.6" fill="#ef9a9a"/><rect x="13.4" y="26" width="2.8" height="5" fill="#5d4037"/>',
   '<ellipse cx="30" cy="30" rx="7.5" ry="11" fill="#c0ca33" transform="rotate(30 30 30)"/><circle cx="36" cy="20" r="5" fill="#c0ca33"/>',
   '<ellipse cx="44" cy="40" rx="6" ry="14" fill="#fdd835" transform="rotate(40 44 40)"/>',
   '<polygon points="36,48 44,36 50,52 42,56" fill="#7cb342"/>',
   '<circle cx="33" cy="56" r="4.6" fill="#7b1fa2"/><circle cx="41" cy="58" r="4.6" fill="#8e24aa"/><circle cx="28" cy="62" r="4.6" fill="#8e24aa"/>',
   '<circle cx="36" cy="64" r="4.6" fill="#7b1fa2"/><circle cx="31" cy="69" r="4.6" fill="#8e24aa"/>',
   '<polygon points="56,14 70,8 64,22" fill="#c62828"/><polygon points="8,86 2,76 16,78" fill="#f9a825"/><polygon points="82,20 94,14 90,28" fill="#e65100"/>']
add('thx-cornucopia','Cornucopia',48,48,"".join(s),colors=22)

# ---------- Autumn leaves ----------
maple="50,6 57,24 70,16 66,38 86,32 74,48 92,58 68,62 70,72 54,68 54,92 46,92 46,68 30,72 32,62 8,58 26,48 14,32 34,38 30,16 43,24"
s=['<rect width="100" height="100" fill="#fbecd0"/>',
   f'<g transform="translate(52 50) scale(.78) translate(-50 -50)"><polygon points="{maple}" fill="#d84315" stroke="#a52f0d" stroke-width="1.6"/>'
   '<path d="M50 90 L50 24 M50 62 L30 44 M50 62 L70 44 M50 76 L34 66 M50 76 L66 66" stroke="#ff8a50" stroke-width="2.6" fill="none"/></g>',
   '<g transform="translate(18 20) rotate(-25)"><ellipse cx="0" cy="0" rx="10" ry="15" fill="#f9a825" stroke="#c77800" stroke-width="1.4"/><path d="M0 -14 L0 18 M0 -2 L-6 -8 M0 -2 L6 -8 M0 6 L-6 0 M0 6 L6 0" stroke="#ffe082" stroke-width="1.8" fill="none"/></g>',
   '<g transform="translate(84 80) rotate(30)"><ellipse cx="0" cy="0" rx="10" ry="15" fill="#8d6e63" stroke="#5d4037" stroke-width="1.4"/><path d="M0 -14 L0 18 M0 -2 L-6 -8 M0 -2 L6 -8 M0 6 L-6 0 M0 6 L6 0" stroke="#bcaaa4" stroke-width="1.8" fill="none"/></g>',
   '<g transform="translate(84 20) rotate(15)"><ellipse cx="0" cy="0" rx="8" ry="13" fill="#7cb342" stroke="#4e7d1f" stroke-width="1.4"/><path d="M0 -12 L0 14" stroke="#c5e1a5" stroke-width="1.8"/></g>',
   '<g transform="translate(16 82) rotate(-10)"><ellipse cx="0" cy="0" rx="8" ry="13" fill="#c62828" stroke="#8e1b1b" stroke-width="1.4"/><path d="M0 -12 L0 14" stroke="#ef9a9a" stroke-width="1.8"/></g>']
add('thx-leaves','Autumn Leaves',40,40,"".join(s),colors=18)
