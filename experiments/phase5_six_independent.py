"""Independent raw-18-permutation check; imports no project group code."""
from itertools import permutations, product
from collections import Counter
import json

IDENTITY = tuple(range(18))
BLOCKS = ((0,2,4),(1,7,8),(3,9,11),(5,12,13),(6,14,15),(10,16,17))


def cycles(*words):
    ans = list(range(18))
    for word in words:
        for i in range(len(word)):
            ans[word[i]-1] = word[(i+1)%len(word)]-1
    return tuple(ans)


A = cycles((2,6),(3,5),(4,10),(8,14),(9,13),(11,17),(15,16))
B = cycles((1,2,7,11,4),(3,8,15,17,10),(5,9,16,18,12))
X = (7,4,8,3,1,14,13,0,2,9,10,11,15,6,5,12,16,17)
Y = (7,13,8,16,1,0,9,5,12,17,14,10,2,4,11,3,15,6)


def times(a,b):
    return tuple(a[b[i]] for i in range(18))


def inverse(a):
    ans = [0]*18
    for i,x in enumerate(a): ans[x]=i
    return tuple(ans)


def close(generators):
    elements = {IDENTITY}
    queue = [IDENTITY]
    for h in queue:
        for g in generators:
            k = times(h,g)
            if k not in elements:
                elements.add(k)
                queue.append(k)
    return elements


def represented(g):
    lookup = {x:(i,j) for i,block in enumerate(BLOCKS) for j,x in enumerate(block)}
    p = tuple(lookup[g[block[0]]][0] for block in BLOCKS)
    maps = tuple(tuple(lookup[g[x]][1] for x in block) for block in BLOCKS)
    assert sorted(p)==list(range(6))
    assert all(lookup[g[x]][0]==p[i] for i,block in enumerate(BLOCKS) for x in block)
    return p,maps


def parity(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2


def certificate():
    group = close((A,B))
    assert len(group)==2160
    typed = {g:represented(g) for g in group}
    assert len({p for p,f in typed.values()})==720
    assert sum(p==tuple(range(6)) for p,f in typed.values())==3
    standard = close((X,Y))
    assert len(standard)==60 and standard<=group
    assert {typed[g][0][0] for g in standard}==set(range(6))
    assert all(p[i]!=i or f[i]==(0,1,2) for g in standard for p,f in [typed[g]] for i in range(6))

    profiles = tuple(product(range(3),repeat=6))
    number = {s:i for i,s in enumerate(profiles)}
    parent = list(range(4374))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]
            i=parent[i]
        return i
    for raw in (A,B):
        p,fs=typed[raw]
        for k,s in enumerate(profiles):
            target=[0]*6
            for i in range(6):target[p[i]]=fs[i][s[i]]
            targetrow=number[tuple(target)]
            for i in range(6):
                left,right=root(6*k+i),root(6*targetrow+p[i])
                parent[left]=right
    names={}
    labels=[]
    for i in range(4374):
        r=root(i)
        if r not in names:names[r]=len(names)
        labels.append(names[r])
    assert len(names)==7
    rows=tuple(tuple(labels[6*k:6*k+6]) for k in range(729))
    surviving=[]
    for maps in product(tuple(permutations(range(3))),repeat=6):
        for k,s in enumerate(profiles):
            t=tuple(maps[i][s[i]] for i in range(6))
            if rows[number[t]]!=rows[k]:break
        else:surviving.append(maps)
    assert len(surviving)==3

    even={g for g in group if parity(typed[g][0])==0}
    assert len(even)==1080
    c=times(times(times(B,times(times(A,B),inverse(A))),inverse(B)),inverse(times(times(A,B),inverse(A))))
    conjugates={times(times(g,c),inverse(g)) for g in even}
    derived=close(tuple(conjugates))
    assert derived==even
    return {'group_order':len(group),'player_image_order':720,'pointwise_kernel':3,
            'standard_subgroup_order':len(standard),'cell_orbits':sorted(Counter(labels).values()),
            'tested_pointwise_maps':6**6,'closure_pointwise_kernel':len(surviving),
            'even_preimage_order':len(even),'even_derived_order':len(derived)}


def binary_code_certificate():
    seeds=((0,0,0,1,0,0),(0,0,2,2,2,1),(0,1,1,1,2,2),
           (0,1,2,0,1,0),(0,2,0,2,1,2),(0,2,1,0,0,1))
    code={tuple((a+k)%3 for a in seed) for seed in seeds for k in range(3)}
    assert len(code)==18
    for raw in (A,B,X,Y):
        p,maps=represented(raw)
        targets=set()
        for s in code:
            t=[0]*6
            for i in range(6):t[p[i]]=maps[i][s[i]]
            targets.add(tuple(t))
        assert targets==code
    survivors=[]
    for maps in product(tuple(permutations(range(3))),repeat=6):
        if all(tuple(maps[i][s[i]] for i in range(6)) in code for s in code):
            survivors.append(maps)
    assert len(survivors)==3
    return {'codewords':len(code),'common_interest':True,'binary':True,
            'tested_pointwise_maps':46656,'pointwise_kernel':len(survivors),
            'exact_aut_order':len(survivors)*720}


if __name__=='__main__':
    print(json.dumps({'orbit_game': certificate(), 'binary_code_game': binary_code_certificate()}, indent=2))
