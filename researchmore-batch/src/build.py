import json,math,re,sys,glob
J=json.load(open('../tools/worked_example.json'));F=json.load(open('figs.json'))
def chi2sf(x,k):  # regularized upper gamma Q(k/2, x/2) via series
    a=k/2;z=x/2;s=1/a;t=1/a;n=1
    while t>1e-14:
        t*=z/(a+n);s+=t;n+=1
    P=s*math.exp(-z+a*math.log(z)-math.lgamma(a));return 1-P
r=lambda v,d=2:f"{v:.{d}f}"
C=[s for s in J['studies'] if s['name']=="Trial C"][0]
T=dict(Q=r(J['Q']),DF=str(J['df']),QP=r(chi2sf(J['Q'],J['df'])),TAU2=r(J['tau2'],3),TAU=r(J['tau']),I2=r(J['I2'],0),
 FERR=r(J['fe']['rr']),FELO=r(J['fe']['lo']),FEHI=r(J['fe']['hi']),RERR=r(J['re']['rr']),RELO=r(J['re']['lo']),REHI=r(J['re']['hi']),
 PILO=r(J['pi']['lo']),PIHI=r(J['pi']['hi']),WC_FE=r(C['w_fe'],0),WC_RE=r(C['w_re'],0))
T.update(F)
def fill(h):
    for k,v in T.items(): h=h.replace("{{"+k+"}}",v)
    left=re.findall(r"\{\{(\w+)\}\}",h)
    if left: sys.exit("unfilled tokens: "+str(left))
    return h
def page(title,body,out):
    css=open('fonts.css').read()+open('style.css').read()
    open(out,'w').write(f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>{title}</title><style>{css.replace('url(fonts/','url(../fonts/')}</style></head><body>{fill(body)}</body></html>")
cover=lambda kick,t1,t2,sub: f"""<div class='cover'><div><div class='kick'>RESEARCHMORE PUBLICATIONS · TEACHING BATCH</div></div>
<div><div class='kick' style='margin-bottom:10pt'>{kick}</div><h1>{t1}<br><span class='red'>{t2}</span></h1><p style='font:13pt Fraunces;font-style:italic;color:#dfe6f3;max-width:130mm;margin-top:14pt'>{sub}</p><div class='hand' style='margin-top:10pt'>by day 7 you hold a protocol written by you.</div></div>
<div><span class='stampw'>TEACHING ONLY · NOT A WRITING SERVICE</span><p style='color:#a9b6d3;font-size:8.5pt;margin-top:14pt'>Unofficial study material prepared from the batch brochure outline. Statistical examples use hypothetical data computed by script. Verify methods against the current Cochrane Handbook and reporting guidelines before use in a real review.</p></div></div>"""
toc="""<section class='chap'><h2 style='margin-top:0'>Contents</h2><ol class='toc' style='font:600 12pt Fraunces;color:#0c1f4d;line-height:2'>
<li>Day 1 · Ask a good question <span class='small'>— PICO, eligibility, PRISMA-P, PROSPERO</span></li>
<li>Day 2 · Find everything <span class='small'>— search strategy, databases, Rayyan screening</span></li>
<li>Day 3 · Judge the evidence <span class='small'>— data extraction, RoB 2, ROBINS-I</span></li>
<li>Day 4 · Pool it <span class='small'>— effect sizes, forest plot, heterogeneity, fixed vs random</span></li>
<li>Day 5 · Stress-test it <span class='small'>— subgroups, sensitivity, publication bias, GRADE</span></li>
<li>Day 6 · Go network <span class='small'>— geometry, transitivity, consistency, league tables, CINeMA</span></li>
<li>Day 7 · Write it up <span class='small'>— PRISMA family, capstone protocol template</span></li></ol>
<h3>How to use these notes</h3><div class='two'><div class='box hy'><span class='t'>High-yield</span><p>Red boxes: the facts that get asked. Learn these first.</p></div><div class='box trap'><span class='t'>Reviewer trap</span><p>Dashed boxes: the mistakes a reviewer will catch.</p></div><div class='box mn'><span class='t'>Mnemonic</span><p>Blue boxes: memory hooks.</p></div><div class='box task'><span class='t'>Hands-on</span><p>Green boxes: today's deliverable on <b>your own</b> question.</p></div></div>
<div class='box pearl'><span class='t'>Method</span><p>Read one chapter → do the green box → close the notes and answer the MCQs cold → revisit only what you missed. The rapid-revision page is for the night before, not the first read.</p></div></section>"""
ch=[open(f'n{i}.html').read() for i in range(1,8)]
page("SR · MA · NMA Premium Notes",cover("PREMIUM NOTES · 7 DAYS","Systematic Review,<br>Meta-Analysis &amp;","Network Meta-Analysis","From question to protocol to analysis. High-yield notes, reviewer traps, worked numbers and practice MCQs.")+toc+"".join(ch),"../notes.html")
if glob.glob('l*.html'):
    L="".join(open(f'l{i}.html').read() for i in range(1,8))
    page("SR · MA · NMA Lecture Script",cover("INSTRUCTOR SCRIPT · 7 DAYS","Teaching the","SR · MA · NMA batch","Run-sheets, slide-by-slide scripts, live demos and hands-on tasks for every day.")+L,"../lectures.html")
print("built")
