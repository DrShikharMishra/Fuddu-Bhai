"""Hypothetical network (NOT real trials). Outcome: pain score 0-10 at 6 weeks, mean difference vs comparator (negative = better). Two-arm trials only."""
import numpy as np, json, math
T=["Placebo","A","B","C"]
S=[("A","Placebo",-1.2,.30),("A","Placebo",-0.9,.35),("A","Placebo",-1.4,.40),
   ("B","Placebo",-0.8,.30),("B","Placebo",-0.6,.35),("B","Placebo",-1.0,.45),
   ("C","Placebo",-0.3,.35),("C","Placebo",-0.2,.40),
   ("A","B",-0.5,.40),("B","C",-0.6,.45)]
Z=lambda x:0.5*(1+math.erf(x/math.sqrt(2)))
def design(rows):
    X=np.zeros((len(rows),3))
    for i,(a,b,_,_) in enumerate(rows):
        if a!="Placebo":X[i,T.index(a)-1]+=1
        if b!="Placebo":X[i,T.index(b)-1]-=1
    return X
def fit(rows,tau2=0):
    X=design(rows);y=np.array([r[2] for r in rows]);v=np.array([r[3]**2 for r in rows])+tau2
    W=np.diag(1/v);C=np.linalg.inv(X.T@W@X);d=C@X.T@W@y
    return X,y,v,W,C,d
X,y,v,W,C,d=fit(S)
Q=float((y-X@d)@W@(y-X@d));df=len(S)-3
H=X@C@X.T@W;trace=np.trace((np.eye(len(S))-H)@W)
tau2=max(0,(Q-df)/trace);I2=max(0,(Q-df)/Q)*100
X,y,v,W,C,d=fit(S,tau2)
D=np.r_[0,d];Cf=np.zeros((4,4));Cf[1:,1:]=C
def contrast(i,j):  # d_i - d_j
    return D[i]-D[j], math.sqrt(Cf[i,i]+Cf[j,j]-2*Cf[i,j])
league={};
for i in range(4):
    for j in range(4):
        if i!=j:
            m,s=contrast(i,j);league[f"{T[i]}|{T[j]}"]=dict(md=m,lo=m-1.96*s,hi=m+1.96*s)
P={}
for i in range(4):
    P[T[i]]=float(np.mean([Z(-contrast(i,j)[0]/contrast(i,j)[1]) for j in range(4) if j!=i]))  # lower MD better
# node-split A vs B: indirect from network without trial 9
S2=[s for k,s in enumerate(S) if k!=8]
X2,y2,v2,W2,C2,d2=fit(S2,tau2)
ind=d2[0]-d2[1];ind_se=math.sqrt(C2[0,0]+C2[1,1]-2*C2[0,1])
dirm,dirse=-0.5,0.40**2
dirse=0.40
diff=dirm-ind;diffse=math.sqrt(dirse**2+ind_se**2);zz=diff/diffse
pv=2*(1-Z(abs(zz)))
# direct pairwise estimates (RE-free simple FE) vs Placebo
def pair(t):
    r=[s for s in S if s[0]==t and s[1]=="Placebo"];w=np.array([1/s[3]**2 for s in r]);m=sum(w*np.array([s[2] for s in r]))/w.sum();return m,math.sqrt(1/w.sum()),len(r)
out=dict(T=T,studies=S,Q=Q,df=df,tau2=tau2,I2=I2,vsP={T[i]:dict(md=D[i],se=math.sqrt(Cf[i,i]),lo=D[i]-1.96*math.sqrt(Cf[i,i]),hi=D[i]+1.96*math.sqrt(Cf[i,i])) for i in range(1,4)},
 league=league,pscore=P,split=dict(direct=dirm,direct_lo=dirm-1.96*dirse,direct_hi=dirm+1.96*dirse,indirect=ind,ind_lo=ind-1.96*ind_se,ind_hi=ind+1.96*ind_se,diff=diff,p=pv),
 direct={t:pair(t) for t in "ABC"})
json.dump(out,open('nma_example.json','w'),indent=1)
print("Q",round(Q,2),"df",df,"tau2",round(tau2,3),"I2",round(I2))
for t in T[1:]:print(t,{k:round(v_,2) for k,v_ in out['vsP'][t].items()})
print("P",{k:round(v_,2) for k,v_ in P.items()})
print("split",{k:round(v_,2) for k,v_ in out['split'].items()})
print("A vs B",{k:round(v_,2) for k,v_ in league['A|B'].items()},"B vs C",{k:round(v_,2) for k,v_ in league['B|C'].items()},"A vs C",{k:round(v_,2) for k,v_ in league['A|C'].items()})
