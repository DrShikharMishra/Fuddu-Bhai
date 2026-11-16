import json,math
N="#0c1f4d";R="#c8102e";B="#cdd8ea"
J=json.load(open('../tools/worked_example.json'))
def esc(s):return s.replace('&','&amp;')
def forest():
    W,H=640,330;x0,x1=290,500  # plot area in px for RR 0.1..4 (log)
    lo,hi=math.log(0.1),math.log(4)
    X=lambda rr:x0+(math.log(rr)-lo)/(hi-lo)*(x1-x0)
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif" font-size="9.5">']
    o.append(f'<text x="8" y="18" font-weight="700" fill="{N}">Study (hypothetical)</text><text x="196" y="18" font-weight="700" fill="{N}">Tx n/N</text><text x="248" y="18" font-weight="700" fill="{N}" >Ctl n/N</text>')
    o.append(f'<text x="520" y="18" font-weight="700" fill="{N}">RR [95% CI]</text><text x="604" y="18" font-weight="700" fill="{N}">Wt%</text>')
    o.append(f'<line x1="8" x2="632" y1="24" y2="24" stroke="{N}"/>')
    y=44
    for s in J['studies']:
        cx=X(s['rr']);sz=4+s['w_re']/3.2
        o.append(f'<text x="8" y="{y+3}" fill="{N}">{s["name"]}</text><text x="196" y="{y+3}" fill="#333">{s["ev_t"]}/{s["n_t"]}</text><text x="248" y="{y+3}" fill="#333">{s["ev_c"]}/{s["n_c"]}</text>')
        o.append(f'<line x1="{X(s["lo"]):.1f}" x2="{X(s["hi"]):.1f}" y1="{y}" y2="{y}" stroke="{N}" stroke-width="1.4"/>')
        o.append(f'<rect x="{cx-sz/2:.1f}" y="{y-sz/2:.1f}" width="{sz:.1f}" height="{sz:.1f}" fill="{N}"/>')
        o.append(f'<text x="520" y="{y+3}" fill="#333">{s["rr"]:.2f} [{s["lo"]:.2f}, {s["hi"]:.2f}]</text><text x="604" y="{y+3}" fill="#333">{s["w_re"]:.1f}</text>')
        y+=28
    y+=4;re=J['re'];pi=J['pi']
    o.append(f'<line x1="8" x2="632" y1="{y-14}" y2="{y-14}" stroke="{N}"/>')
    o.append(f'<text x="8" y="{y+3}" font-weight="700" fill="{N}">Random effects (DL)</text>')
    o.append(f'<polygon points="{X(re["lo"]):.1f},{y} {X(re["rr"]):.1f},{y-8} {X(re["hi"]):.1f},{y} {X(re["rr"]):.1f},{y+8}" fill="{R}"/>')
    o.append(f'<text x="520" y="{y+3}" font-weight="700" fill="{R}">{re["rr"]:.2f} [{re["lo"]:.2f}, {re["hi"]:.2f}]</text><text x="604" y="{y+3}" fill="#333">100</text>')
    y+=24
    o.append(f'<text x="8" y="{y+3}" fill="{N}">95% prediction interval</text><line x1="{X(pi["lo"]):.1f}" x2="{X(pi["hi"]):.1f}" y1="{y}" y2="{y}" stroke="{R}" stroke-width="2" stroke-dasharray="4 2"/>')
    o.append(f'<text x="520" y="{y+3}" fill="{R}">[{pi["lo"]:.2f}, {pi["hi"]:.2f}]</text>')
    yb=y+22
    o.append(f'<line x1="{X(1):.1f}" x2="{X(1):.1f}" y1="30" y2="{yb}" stroke="#555" stroke-dasharray="3 3"/>')
    o.append(f'<line x1="{x0}" x2="{x1}" y1="{yb}" y2="{yb}" stroke="{N}"/>')
    for t in [0.1,0.25,0.5,1,2,4]:
        o.append(f'<line x1="{X(t):.1f}" x2="{X(t):.1f}" y1="{yb}" y2="{yb+4}" stroke="{N}"/><text x="{X(t):.1f}" y="{yb+14}" text-anchor="middle" fill="{N}">{t:g}</text>')
    o.append(f'<text x="{X(1)-8:.1f}" y="{yb+28}" text-anchor="end" fill="{N}">← favours treatment</text><text x="{X(1)+8:.1f}" y="{yb+28}" fill="{N}">favours control →</text>')
    o.append(f'<text x="{X(1)+3:.1f}" y="36" fill="#555" font-size="8">no effect</text>')
    o.append('</svg>');return "".join(o)
def funnel(asym=False):
    W,H=380,270;cx=190
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif" font-size="9">']
    X=lambda e:cx+e*120;Y=lambda se:30+se*210
    o.append(f'<polygon points="{X(0)},{Y(0)} {X(-1.96*0.6):.0f},{Y(0.6)} {X(1.96*0.6):.0f},{Y(0.6)}" fill="{B}" opacity=".6"/>')
    o.append(f'<line x1="{X(0)}" x2="{X(0)}" y1="{Y(0)}" y2="{Y(0.6)}" stroke="{N}"/>')
    pts=[(-0.02,0.08),(0.05,0.1),(-0.1,0.14),(0.12,0.17),(-0.05,0.2),(0.2,0.24),(-0.18,0.27),(0.02,0.3),(0.3,0.36),(-0.28,0.4),(0.1,0.45),(0.45,0.5),(-0.3,0.52)]
    if asym:pts=[p for p in pts if not(p[0]>0 and p[1]>0.28)]
    for e,s in pts:o.append(f'<circle cx="{X(e):.1f}" cy="{Y(s):.1f}" r="3.6" fill="{N}"/>')
    if asym:o.append(f'<ellipse cx="{X(0.38):.0f}" cy="{Y(0.45):.0f}" rx="44" ry="26" fill="none" stroke="{R}" stroke-width="1.6" stroke-dasharray="5 3"/><text x="{X(0.38):.0f}" y="{Y(0.45)+3:.0f}" text-anchor="middle" fill="{R}" font-size="8.5">missing studies?</text>')
    o.append(f'<line x1="30" x2="{W-10}" y1="{Y(0.6)+2:.0f}" y2="{Y(0.6)+2:.0f}" stroke="{N}"/><text x="{cx}" y="{H-6}" text-anchor="middle" fill="{N}">effect size →</text><text x="10" y="{Y(0)+4:.0f}" fill="{N}">SE 0</text><text x="10" y="{Y(0.6):.0f}" fill="{N}">SE ↓ (small studies)</text>')
    o.append('</svg>');return "".join(o)
def prisma(filled=True):
    v=dict(a="n = 1,842",b="n = 394",c="n = 1,448",d="n = 62",e="n = 31",f="n = 24",g="",h="") if filled else {k:"n = ____" for k in "abcdefgh"}
    o=['<svg viewBox="0 0 560 420" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif" font-size="10">']
    def bx(x,y,w,h,t1,t2,red=False,dash=False):
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff" stroke="{R if red else N}" stroke-width="{2 if red else 1.4}" {"stroke-dasharray=\"5 3\"" if dash else ""}/><text x="{x+8}" y="{y+16}" font-weight="700" fill="{N}" font-size="9">{t1}</text><text x="{x+8}" y="{y+32}" fill="#333">{t2}</text>')
    def ar(x1,y1,x2,y2):o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{N}" stroke-width="1.4" marker-end="url(#a)"/>')
    o.append(f'<defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8z" fill="{N}"/></marker></defs>')
    bx(20,10,220,44,"IDENTIFICATION","Records from databases + registers "+v['a'])
    bx(300,10,240,44,"REMOVED BEFORE SCREENING","Duplicates "+v['b']+"  (auto + manual)",dash=True)
    ar(240,32,300,32)
    bx(20,90,220,44,"SCREENING · 2 REVIEWERS","Title/abstract screened "+v['c'])
    ar(130,54,130,90)
    bx(300,90,240,44,"EXCLUDED","Not relevant "+("n = 1,386" if filled else "n = ____"),dash=True)
    ar(240,112,300,112)
    bx(20,170,220,44,"ELIGIBILITY","Full texts sought "+v['d'])
    ar(130,134,130,170)
    bx(300,170,240,70,"FULL TEXTS EXCLUDED + REASONS","Wrong population "+("n = 9" if filled else "n = __"),dash=True)
    o.append(f'<text x="308" y="214" fill="#333">Wrong comparator {"n = 12" if filled else "n = __"}</text><text x="308" y="228" fill="#333">No usable data {"n = 10" if filled else "n = __"}</text>')
    ar(240,192,300,192)
    bx(20,260,220,44,"INCLUDED IN REVIEW","Studies "+v['e'])
    ar(130,214,130,260)
    bx(20,336,220,56,"INCLUDED IN META-ANALYSIS","Studies "+v['f']+("  (k = 24 with usable data)" if filled else ""),red=True)
    ar(130,304,130,336)
    o.append(f'<text x="300" y="360" class="h" fill="{R}" font-size="10">(example numbers are hypothetical)</text>' if filled else f'<text x="300" y="360" fill="{R}" font-size="10">fill from YOUR search log →</text>')
    o.append('</svg>');return "".join(o)
def network():
    o=['<svg viewBox="0 0 420 250" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif" font-size="10">']
    nodes={"Placebo":(210,125),"A":(80,50),"B":(340,50),"C":(80,200),"D":(340,200)}
    edges=[("Placebo","A",9),("Placebo","B",6),("Placebo","C",4),("Placebo","D",2),("A","B",3),("C","D",1)]
    for a,b,n in edges:
        (x1,y1),(x2,y2)=nodes[a],nodes[b]
        o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{N}" stroke-width="{1+n*0.9}"/>')
    (x1,y1),(x2,y2)=nodes["A"],nodes["C"];o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{R}" stroke-width="2" stroke-dasharray="6 4"/>')
    for k,(x,y) in nodes.items():
        o.append(f'<circle cx="{x}" cy="{y}" r="{26 if k=="Placebo" else 20}" fill="#fff" stroke="{N}" stroke-width="2"/><text x="{x}" y="{y+4}" text-anchor="middle" fill="{N}" font-weight="700">{k}</text>')
    o.append(f'<text x="30" y="128" fill="{R}" font-size="9">A vs C: no direct trial</text><text x="8" y="244" fill="#555" font-size="8.5">Line thickness = number of trials. Dashed red = indirect evidence only.</text>')
    o.append('</svg>');return "".join(o)
def rob_grid():
    doms=["D1 Randomisation","D2 Deviations","D3 Missing data","D4 Measurement","D5 Selection of result","Overall"]
    data=[["L","L","L","L","S","S"],["S","L","L","L","L","S"],["L","S","H","L","S","H"],["L","L","L","S","L","S"]]
    col={"L":"#2f9d57","S":"#e0a526","H":R}
    o=['<svg viewBox="0 0 520 190" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif" font-size="9">']
    for j,d in enumerate(doms):o.append(f'<text x="{135+j*62+26}" y="24" text-anchor="middle" fill="{N}" font-size="7.6" font-weight="700">{d.split(" ",1)[0]}</text><text x="{135+j*62+26}" y="34" text-anchor="middle" fill="{N}" font-size="6.6">{d.split(" ",1)[1] if " " in d else ""}</text>')
    for i,row in enumerate(data):
        o.append(f'<text x="10" y="{62+i*34}" fill="{N}" font-weight="700">Trial {"ABCD"[i]}</text>')
        for j,c in enumerate(row):
            o.append(f'<circle cx="{135+j*62+26}" cy="{58+i*34}" r="11" fill="{col[c]}"/><text x="{135+j*62+26}" y="{62+i*34}" text-anchor="middle" fill="#fff" font-weight="700">{ {"L":"+","S":"?","H":"−"}[c] }</text>')
    o.append(f'<text x="10" y="186" fill="#555" font-size="8">+ low risk   ? some concerns   − high risk  (illustrative traffic-light plot)</text></svg>');return "".join(o)
def pico():
    o=['<svg viewBox="0 0 520 110" xmlns="http://www.w3.org/2000/svg" font-family="Fraunces,serif">']
    L=[("P","Population"),("I","Intervention"),("C","Comparator"),("O","Outcome")]
    for i,(a,b) in enumerate(L):
        x=8+i*128;o.append(f'<rect x="{x}" y="8" width="118" height="92" fill="#fff" stroke="{N}" stroke-width="1.6"/><text x="{x+59}" y="62" text-anchor="middle" font-size="46" font-weight="800" fill="{R}">{a}</text><text x="{x+59}" y="90" text-anchor="middle" font-size="12" fill="{N}" font-weight="600">{b}</text>')
    o.append('</svg>');return "".join(o)
out={"FOREST":forest(),"FUNNEL_SYM":funnel(False),"FUNNEL_ASYM":funnel(True),"PRISMA_BLANK":prisma(False),"PRISMA_FILLED":prisma(True),"NETWORK":network(),"ROB":rob_grid(),"PICO":pico()}
json.dump(out,open('figs.json','w'))
print({k:len(v) for k,v in out.items()})
