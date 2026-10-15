"""Exact n=4 ternary group search, using regular C4 standardness.

Only a restricted theorem: transitive standard subgroups containing C4.
The V4-only standard case is not covered by this certificate.
"""
from itertools import permutations, product
from collections import Counter
import json
from pathlib import Path

PS = tuple(permutations(range(4)))
FS = tuple(permutations(range(3)))
PI = {p:i for i,p in enumerate(PS)}
FI = {p:i for i,p in enumerate(FS)}
PC = tuple(tuple(PI[tuple(p[q[i]] for i in range(4))] for q in PS) for p in PS)
FC = tuple(tuple(FI[tuple(p[q[i]] for i in range(3))] for q in FS) for p in FS)
INVP = tuple(next(j for j in range(24) if PC[i][j] == 0) for i in range(24))
INVF = tuple(next(j for j in range(6) if FC[i][j] == 0) for i in range(6))
DIG = tuple(product(range(6),repeat=4))
BASE = 6**4
E = 0
R = PI[(1,2,3,0)]*BASE
A = PI[(2,0,1,3)]*BASE  # R A is a transposition
ORDER = 24*BASE


def mul(g,h):
    p,x = divmod(g,BASE)
    q,y = divmod(h,BASE)
    f,k = DIG[x],DIG[y]
    v = [FC[f[PS[q][i]]][k[i]] for i in range(4)]
    return PC[p][q]*BASE + ((v[0]*6+v[1])*6+v[2])*6+v[3]


def inverse(g):
    p,x=divmod(g,BASE)
    ip=INVP[p]
    v=[INVF[DIG[x][PS[ip][i]]] for i in range(4)]
    return ip*BASE+((v[0]*6+v[1])*6+v[2])*6+v[3]


def generated(gens, cap=None):
    found={E}; todo=[E]
    while todo:
        h=todo.pop()
        for g in gens:
            v=mul(g,h)
            if v not in found:
                found.add(v);todo.append(v)
                if cap is not None and len(found)>cap:
                    return None
    return frozenset(found)


def conjugate_local(f,h):
    return tuple(FC[FC[h][v]][INVF[h]] for v in f)


def c4_representatives():
    """Every 3-cycle lift reduced by common local conjugation.

    Conjugating by powers of R and replacing a generator by its inverse
    normalizes its player image to (021). These operations do not change the
    isomorphism type, nor the existence of a section, of <R,g>.
    """
    orbit={}
    for x,f in enumerate(DIG):
        key=min(conjugate_local(f,h) for h in range(6))
        orbit.setdefault(key,x)
    return tuple(A+x for x in orbit.values())


def section(group):
    """S4 presentation <r,a | r^4=a^3=(ra)^2=1>.

    Search ALL lifts of the two specified player images; no assertion that
    the complement contains the original bare R is required.
    """
    rpi=R//BASE; api=A//BASE
    rs=[g for g in group if g//BASE==rpi and mul(mul(g,g),mul(g,g))==E]
    aa=[g for g in group if g//BASE==api and mul(mul(g,g),g)==E]
    # Try original regular generator first; most groups terminate immediately.
    rs.sort(key=lambda g:(g!=R,g))
    for r in rs:
        for a in aa:
            b=mul(r,a)
            if mul(b,b)==E:
                assert len(generated((r,a)))==24
                return r,a
    return None


def verify_c4():
    records=[]; groups={}
    reps=c4_representatives()
    assert len(reps)==251
    for g in reps:
        h=generated((R,g))
        if h not in groups:
            pair=section(h)
            groups[h]=len(records)
            records.append({'generator':g,'group_order':len(h),
                            'section':pair,
                            'section_contains_original_r': pair is not None and pair[0]==R})
    assert all(r['section'] is not None for r in records)
    return {'scope':'n4 ternary with normalized bare regular C4',
            'ambient_order':ORDER,'conjugacy_representatives':len(reps),
            'distinct_generated_groups':len(groups),
            'order_histogram':dict(sorted(Counter(len(h) for h in groups).items())),
            'nonsplit_generated_groups':sum(r['section'] is None for r in records),
            'records':records}


if __name__=='__main__':
    result=verify_c4()
    target=Path(__file__).with_name('phase5_splitting-c4-results.json')
    if '--verify' in __import__('sys').argv:
        assert json.loads(target.read_text())==json.loads(json.dumps(result))
    else:
        target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
