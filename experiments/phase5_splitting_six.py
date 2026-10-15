"""Investigate ATLAS 3.S6 degree18 as a ternary actual game mechanism.

Source generators: primary ATLAS, 3S6G1-p18aB0.g1/.g2.
No source group identity is assumed by the finite verification.
"""
from itertools import product, permutations
from collections import Counter
import json
from pathlib import Path


def cyc(*cycles):
    p=list(range(18))
    for c in cycles:
        for a,b in zip(c,c[1:]+c[:1]):p[a-1]=b-1
    return tuple(p)

E=tuple(range(18))
A=cyc((2,6),(3,5),(4,10),(8,14),(9,13),(11,17),(15,16))
B=cyc((1,2,7,11,4),(3,8,15,17,10),(5,9,16,18,12))


def mul(p,q):return tuple(p[q[i]] for i in range(18))
def inv(p):return tuple(p.index(i) for i in range(18))

def gen(gens,cap=None):
    found={E};todo=[E]
    while todo:
        h=todo.pop()
        for g in gens:
            t=mul(g,h)
            if t not in found:
                found.add(t);todo.append(t)
                if cap and len(found)>cap:return None
    return frozenset(found)

def blocks(group):
    stab=[g for g in group if g[0]==0]
    orb={j:frozenset(g[j] for g in stab) for j in range(18)}
    block=frozenset({0})|next(v for v in orb.values() if len(v)==2)
    return tuple(sorted({tuple(sorted(g[i] for i in block)) for g in group}))

def typed(g,bs):
    pos={a:(i,j) for i,b in enumerate(bs) for j,a in enumerate(b)}
    p=tuple(pos[g[b[0]]][0] for b in bs)
    f=tuple(tuple(pos[g[x]][1] for x in b) for b in bs)
    assert all(pos[g[x]][0]==p[i] for i,b in enumerate(bs) for x in b)
    return p,f

def cellperm(g):
    p,f=g
    res=[]
    for s in product(range(3),repeat=6):
        t=[0]*6
        for i in range(6):t[p[i]]=f[i][s[i]]
        k=0
        for a in t:k=3*k+a
        res.extend(6*k+p[i] for i in range(6))
    return tuple(res)

def orbitlabels(gens):
    cp=[cellperm(g) for g in gens]
    labels=[-1]*4374;num=0
    for i in range(4374):
        if labels[i]>=0:continue
        todo=[i];labels[i]=num
        while todo:
            x=todo.pop()
            for g in cp:
                y=g[x]
                if labels[y]<0:labels[y]=num;todo.append(y)
        num+=1
    return labels

def localclosure(labels):
    fs=tuple(permutations(range(3)))
    profiles=tuple(product(range(3),repeat=6))
    rows=tuple(tuple(labels[6*k:6*k+6]) for k in range(729))
    survivors=[]
    for ff in product(fs,repeat=6):
        for k,s in enumerate(profiles):
            idx=0
            for i,a in enumerate(s):idx=3*idx+ff[i][a]
            if rows[idx]!=rows[k]:break
        else:survivors.append(ff)
    return survivors

def order(g):
    h=g;n=1
    while h!=E:h=mul(g,h);n+=1
    return n

# Explicit internally found A5 generators; they are verified, not assumed.
X=(7,4,8,3,1,14,13,0,2,9,10,11,15,6,5,12,16,17)
Y=(7,13,8,16,1,0,9,5,12,17,14,10,2,4,11,3,15,6)
CODE_ROWS=('000100','002221','011122','012010','020212','021001')
CODE=frozenset(tuple((int(c)+k)%3 for c in r) for r in CODE_ROWS for k in range(3))


def verify_six():
    group=gen((A,B))
    assert len(group)==2160
    bs=blocks(group)
    assert len(bs)==6 and all(len(b)==3 for b in bs)
    tg=[typed(g,bs) for g in group]
    assert len({p for p,f in tg})==720
    assert sum(p==tuple(range(6)) for p,f in tg)==3
    labels=orbitlabels((typed(A,bs),typed(B,bs)))
    assert len(set(labels))==7
    profiles=tuple(product(range(3),repeat=6))
    binary=[int(s in CODE) for s in profiles for i in range(6)]
    assert all(binary[c]==binary[t] for g in (typed(A,bs),typed(B,bs))
               for c,t in enumerate(cellperm(g)))
    lc=localclosure(binary)
    assert len(lc)==3
    assert all(len({f for f in ff})==1 for ff in lc)
    assert {ff[0] for ff in lc}=={(0,1,2),(1,2,0),(2,0,1)}
    st=gen((X,Y))
    assert len(st)==60 and st<=group
    typedst=[typed(g,bs) for g in st]
    assert len({p[0] for p,f in typedst})==6
    assert all(p[i]!=i or f[i]==(0,1,2) for p,f in typedst for i in range(6))
    hgens=(B,mul(mul(A,B),A));h=gen(hgens)
    assert len(h)==1080
    comm=mul(mul(mul(hgens[0],hgens[1]),inv(hgens[0])),inv(hgens[1]))
    conjugates=[mul(mul(g,comm),inv(g)) for g in h]
    derived=gen(conjugates)
    assert derived==h
    # Small independent analytic-kernel certificate: Hamming distances force
    # one common slope, and global translation reduces all candidates to12.
    assert set(sum(x!=y for x,y in zip(s,t)) for s in CODE for t in CODE)=={0,4,6}
    assert all({t for t in CODE if sum(x!=y for x,y in zip(s,t)) in (0,6)}
               =={tuple((x+k)%3 for x in s) for k in range(3)} for s in CODE)
    r0=tuple(map(int,CODE_ROWS[0]));small=[]
    for a in (1,-1):
        for row in CODE_ROWS:
            b=tuple((int(c)-a*t)%3 for c,t in zip(row,r0))
            image={tuple((a*x+y)%3 for x,y in zip(s,b)) for s in CODE}
            small.append((a,row,image==CODE))
    assert [r for r in small if r[2]]==[(1,CODE_ROWS[0],True)]
    return {'source_urls':[
            'https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/3S6G1-p18aB0',
            'https://brauer.maths.qmul.ac.uk/Atlas/alt/A6/gap/3S6G1-p18aB0.g1',
            'https://brauer.maths.qmul.ac.uk/Atlas/alt/A6/gap/3S6G1-p18aB0.g2'],
            'raw_generators':[A,B],'blocks':bs,
            'typed_generators':[typed(A,bs),typed(B,bs)],
            'group_order':len(group),'player_image_order':720,
            'pointwise_kernel_order':len(lc),'code_rows':CODE_ROWS,
            'code_size':len(CODE),'binary_common_interest':True,
            'utility_orbit_sizes':dict(sorted(Counter(labels).items())),
            'standard_generators':[X,Y],
            'standard_typed_generators':[typed(X,bs),typed(Y,bs)],
            'standard_subgroup_order':len(st),'even_preimage_order':len(h),
            'even_preimage_derived_order':len(derived),
            'small_kernel_candidates':small}


if __name__=='__main__':
    result=verify_six()
    target=Path(__file__).with_name('phase5_splitting-six-results.json')
    if '--verify' in __import__('sys').argv:
        assert json.loads(target.read_text())==json.loads(json.dumps(result))
    else:target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in
                     ('raw_generators','standard_generators','small_kernel_candidates')},indent=2))
