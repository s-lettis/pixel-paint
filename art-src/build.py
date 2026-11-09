import glob, importlib, json, sys, io, math
import numpy as np
from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

def load_art():
    sys.path.insert(0,'.')
    art=[]
    order=['art_thanks','art_xmas','art_animals','art_scenes']
    for m in order:
        try: art+=importlib.import_module(m).ART
        except ModuleNotFoundError as e:
            if e.name!=m: raise
    return art

def render(pg,a):
    W,H=a['w']*8,a['h']*8
    pg.set_viewport_size({'width':W,'height':H})
    svg=a['svg'].replace('<svg ','<svg width="%d" height="%d" preserveAspectRatio="none" '%(W,H),1)
    pg.set_content('<html><body style="margin:0;overflow:hidden">'+svg+'</body></html>')
    png=pg.screenshot(clip={'x':0,'y':0,'width':W,'height':H})
    return np.array(Image.open(io.BytesIO(png)).convert('RGB'))

def to_grid(img,w,h):
    packed=(img[:,:,0].astype(np.int64)<<16)|(img[:,:,1].astype(np.int64)<<8)|img[:,:,2].astype(np.int64)
    blocks=packed.reshape(h,8,w,8).transpose(0,2,1,3).reshape(h,w,64)
    g=np.zeros((h,w),dtype=np.int64)
    for y in range(h):
        for x in range(w):
            v,c=np.unique(blocks[y,x],return_counts=True); g[y,x]=v[np.argmax(c)]
    return g

def rgb(p): return ((p>>16)&255,(p>>8)&255,p&255)
def reduce_palette(g,k):
    while True:
        vals,counts=np.unique(g,return_counts=True)
        if len(vals)<=k: break
        i=int(np.argmin(counts)); v=vals[i]
        best=None;bd=1e18
        for j,u in enumerate(vals):
            if j==i: continue
            d=sum((a-b)**2 for a,b in zip(rgb(int(v)),rgb(int(u))))
            if d<bd: bd=d;best=u
        g[g==v]=best
    return g

def cleanup(g,rounds=2):
    h,w=g.shape
    for _ in range(rounds):
        ng=g.copy()
        for y in range(h):
            for x in range(w):
                c=g[y,x]; nb=[]
                for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                    yy,xx=y+dy,x+dx
                    if 0<=yy<h and 0<=xx<w: nb.append(g[yy,xx])
                if c not in nb and nb:
                    vals,cnt=np.unique(nb,return_counts=True); ng[y,x]=vals[np.argmax(cnt)]
        g=ng
    return g

def b36(i): return '0123456789abcdefghijklmnopqrstuvwxyz'[i]
def build(a,pg):
    img=render(pg,a); g=to_grid(img,a['w'],a['h'])
    g=reduce_palette(g,a['colors']); g=cleanup(g); 
    vals,counts=np.unique(g,return_counts=True)
    order=np.argsort(-counts); pal=[int(vals[i]) for i in order]
    idx={p:i for i,p in enumerate(pal)}
    cells=''.join(b36(idx[int(v)]) for v in g.flatten())
    return dict(id=a['id'],cat=a['cat'],name=a['name'],w=a['w'],h=a['h'],p=['%06x'%p for p in pal],c=cells)

def preview(puz,cell=8):
    imgs=[]
    for p in puz:
        im=Image.new('RGB',(p['w']*cell,p['h']*cell),'white'); d=ImageDraw.Draw(im)
        for i,ch in enumerate(p['c']):
            col='#'+p['p']['0123456789abcdefghijklmnopqrstuvwxyz'.index(ch)]
            x,y=i%p['w'],i//p['w']; d.rectangle([x*cell,y*cell,(x+1)*cell-1,(y+1)*cell-1],fill=col)
        imgs.append(im)
    return imgs

if __name__=='__main__':
    only=sys.argv[1:]
    art=[a for a in load_art() if not only or a['id'] in only or a['cat'] in only]
    out=[]
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page()
        for a in art:
            r=build(a,pg); out.append(r); print(a['id'],len(r['p']),'colors')
        b.close()
    json.dump(out,open('/tmp/puzzles.json','w'))
    ims=preview(out,10)
    cols=4; cw=max(i.width for i in ims)+16; ch=max(i.height for i in ims)+16
    rows=(len(ims)+cols-1)//cols
    sheet=Image.new('RGB',(cols*cw,rows*ch),'#dddddd')
    for n,im in enumerate(ims): sheet.paste(im,((n%cols)*cw+8,(n//cols)*ch+8))
    sheet.save('/tmp/sheet_art.png'); print('sheet',sheet.size)
