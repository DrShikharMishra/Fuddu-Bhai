"""Hypothetical dataset (NOT real trials) for teaching. Outcome: 30-day surgical-site infection (SSI), risk ratio."""
import numpy as np, json, math
from math import log, exp, sqrt
# study, events_tx, n_tx, events_ctl, n_ctl   (HYPOTHETICAL)
D=[("Trial A",12,150,20,148),("Trial B",8,90,15,92),("Trial C",34,310,30,305),
   ("Trial D",5,60,6,58),("Trial E",11,200,31,198),("Trial F",9,120,10,125)]
y=[];v=[]
for s,a,n1,c,n2 in D:
    y.append(log((a/n1)/(c/n2))); v.append(1/a-1/n1+1/c-1/n2)
y=np.array(y);v=np.array(v);k=len(y)
w=1/v; fe=(w*y).sum()/w.sum(); se_fe=sqrt(1/w.sum())
Q=(w*(y-fe)**2).sum(); df=k-1
C=w.sum()-(w**2).sum()/w.sum(); tau2=max(0,(Q-df)/C)
I2=max(0,(Q-df)/Q)*100
ws=1/(v+tau2); re=(ws*y).sum()/ws.sum(); se_re=sqrt(1/ws.sum())
# t-quantile via table for df=4 (k-2): 2.776
t=2.7764451
pi=(re-t*sqrt(tau2+se_re**2), re+t*sqrt(tau2+se_re**2))
z=1.959964
out=dict(k=k,Q=Q,df=df,tau2=tau2,tau=sqrt(tau2),I2=I2,
 fe=dict(rr=exp(fe),lo=exp(fe-z*se_fe),hi=exp(fe+z*se_fe)),
 re=dict(rr=exp(re),lo=exp(re-z*se_re),hi=exp(re+z*se_re),se=se_re,z=re/se_re),
 pi=dict(lo=exp(pi[0]),hi=exp(pi[1])),
 studies=[dict(name=D[i][0],ev_t=D[i][1],n_t=D[i][2],ev_c=D[i][3],n_c=D[i][4],rr=exp(y[i]),lo=exp(y[i]-z*sqrt(v[i])),hi=exp(y[i]+z*sqrt(v[i])),w_fe=100*w[i]/w.sum(),w_re=100*ws[i]/ws.sum(),lrr=y[i],se=sqrt(v[i])) for i in range(k)])
json.dump(out,open('/home/user/Fuddu-Bhai/researchmore-batch/tools/worked_example.json','w'),indent=1)
print(json.dumps({k_:v_ for k_,v_ in out.items() if k_!='studies'},indent=1))
for s in out['studies']: print(s['name'],round(s['rr'],2),round(s['lo'],2),round(s['hi'],2),round(s['w_fe'],1),round(s['w_re'],1))
