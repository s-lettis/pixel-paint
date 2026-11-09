import math, random
def star(cx,cy,R,r,n=5,rot=-90):
    pts=[]
    for i in range(n*2):
        a=math.radians(rot+i*180/n); rad=R if i%2==0 else r
        pts.append(f"{cx+rad*math.cos(a):.2f},{cy+rad*math.sin(a):.2f}")
    return " ".join(pts)
def snow(seed,n,x0=0,x1=100,y0=0,y1=100,r=1.4,fill="#ffffff"):
    rnd=random.Random(seed); out=[]
    for _ in range(n):
        out.append(f'<circle cx="{rnd.uniform(x0,x1):.1f}" cy="{rnd.uniform(y0,y1):.1f}" r="{r}" fill="{fill}"/>')
    return "".join(out)
def bow(cx,cy,c1,c2,s=1.0):
    # two loops + knot + tails
    return (f'<g transform="translate({cx} {cy}) scale({s})">'
      f'<path d="M0 0 C -6 -14 -20 -12 -18 -2 C -16 6 -6 4 0 0 Z" fill="{c1}"/>'
      f'<path d="M0 0 C 6 -14 20 -12 18 -2 C 16 6 6 4 0 0 Z" fill="{c1}"/>'
      f'<path d="M-1 1 L-9 12 L-4 11 L0 6 Z" fill="{c2}"/><path d="M1 1 L9 12 L4 11 L0 6 Z" fill="{c2}"/>'
      f'<circle cx="0" cy="0" r="3.6" fill="{c2}"/></g>')
def wrap(vb,inner):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" shape-rendering="crispEdges">{inner}</svg>'
