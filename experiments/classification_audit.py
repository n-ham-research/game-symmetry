"""Exact finite source-table audit. Symbol names are equality classes, not floats."""
import json
import math
import re
from itertools import permutations, product
from pathlib import Path
from matching_audit import (bijections, action, matchings, matching_element,
                            partition, subgroups, transitive, implies)
ROOT = Path(__file__).resolve().parents[1]
IDS = ['2.1','3.10','3.12','3.14','3.16','4.1','4.3','4.4','4.18','4.25','5.5','5.12','5.13','5.14','5.15','5.16']


def tables(statement):
    out=[]
    for block in re.findall(r'\\begin\{game\}.*?\\end\{game\}', statement, re.S):
        cells=[]
        for cell in re.findall(r'\$([^$\n]+)\$',block):
            if ',' not in cell or '(' in cell: continue
            tokens=tuple(t.strip().lstrip('\\') for t in cell.split(','))
            if all(re.fullmatch(r'-?\d+|[a-zA-Z]+',t) for t in tokens):
                cells.append(tuple(int(t) if re.fullmatch(r'-?\d+',t) else t for t in tokens))
        if len(cells)!=4: raise ValueError(('table extraction',cells))
        out.append(cells)
    return out


def source_games():
    inventory={x['id']:x for x in json.loads((ROOT/'research/inventory.json').read_text())}
    games={}; records={}
    for ident in IDS:
        rec=inventory[ident]; ts=tables(rec['statement'])
        records[ident]={'source':rec['source'],'line':rec['line'],'tables':ts}
        if not ts: continue
        n=len(ts[0][0]); blocksize=2**(n-2)
        for start in range(0,len(ts),blocksize):
            key=ident if len(ts)==blocksize else ident+chr(ord('a')+start//blocksize)
            flat=sum(ts[start:start+blocksize],[])
            if len(flat)!=2**n: raise ValueError((key,len(flat),n))
            games[key]=dict(zip(product(range(2),repeat=n),map(tuple,flat)))
    games['4.4']=games['3.16']; games['5.5']=games['4.1']
    records['4.4']['reference']='3.16, with coordinate labels changed'
    records['5.5']['reference']='4.1, automorphism listing rather than a new table'
    records['4.18']['reference']='Matching only; no payoff table'
    records['4.25']['reference']='Matching enumeration only; no payoff table'
    return games,records


def automorphisms(game):
    n=len(next(iter(game)))
    return tuple(g for g in bijections((2,)*n)
                 if all(game[s][i]==game[action(g,s)][g[0][i]] for s in game for i in range(n)))


def classify(game, include_elements=False):
    n=len(next(iter(game))); group=automorphisms(game); aset=set(group)
    image={g[0] for g in group}; sn=tuple(permutations(range(n)))
    lifts=[]
    for m in matchings((2,)*n):
        h=tuple(matching_element(m,p) for p in sn if matching_element(m,p) in aset)
        lifts.append({'reference_maps':m,'image_order':len(h),'transitive':transitive(h,n),'full':len(h)==len(sn)})
    numeric=all(isinstance(x,int) for row in game.values() for x in row)
    pure=[] if numeric else None
    for s in game if numeric else ():
        if all(game[s][i]>=game[s[:i]+(1-s[i],)+s[i+1:]][i] for i in range(n)):
            pure.append(s)
    result={'n':n,'ambient_order':math.factorial(n)*2**n,'automorphism_order':len(group),
            'player_image_order':len(image),'player_kernel_order':sum(p==tuple(range(n)) for p,f in group),
            'symmetric':transitive(group,n),'n_transitive':len(image)==len(sn),
            'standard':any(x['transitive'] for x in lifts),'fully':any(x['full'] for x in lifts),
            'matching_lifts':lifts,'pure_equilibria':pure,'player_image':sorted(image)}
    if include_elements: result['automorphisms']=group
    return result


def source_generators():
    # Player cycles/strategy flips transcribed from the pinned original examples.
    def binary(p,f):
        return tuple(p),tuple((1,0) if z else (0,1) for z in f)
    return {
        '5.13':[binary((1,2,0),(0,0,0)),binary((1,0,2),(1,1,1))],
        '5.14a':[binary((1,2,3,0),(1,0,0,0))],
        '5.14b':[binary((1,0,3,2),(1,0,1,0)),binary((2,3,0,1),(1,1,0,0)),binary((3,2,1,0),(1,1,0,0))],
        '5.15':[binary((1,2,3,0),(0,0,1,0)),binary((1,0,2,3),(0,0,0,1))],
        '5.16':[binary((3,4,2,0,1,5),(1,0,1,1,0,1)),binary((2,3,4,5,0,1),(0,0,0,0,0,0))]}


def generated_by(generators):
    from matching_audit import multiply
    group=set(generators)
    while True:
        more={multiply(a,b) for a in group for b in generators}-group
        if not more:return group
        group.update(more)


def equality_patterns(k):
    def rec(a):
        if len(a)==k: yield tuple(a); return
        for t in range(max(a,default=-1)+2): yield from rec(a+[t])
    return rec([])


def specialize(game,pattern):
    names=sorted({x for row in game.values() for x in row},key=str)
    assignment=dict(zip(names,pattern))
    return {s:tuple(assignment[x] for x in row) for s,row in game.items()}


def canonical(values):
    ids={}; return tuple(ids.setdefault(v,len(ids)) for v in values)


def cell_maps(n):
    profiles=tuple(product(range(2),repeat=n)); cells=[(s,i) for s in profiles for i in range(n)]
    ids={c:j for j,c in enumerate(cells)}
    return tuple(tuple(ids[action(g,s),g[0][i]] for s,i in cells) for g in bijections((2,)*n))


def relabel(p, mapping):
    q=[None]*len(p)
    for j,k in enumerate(mapping): q[k]=p[j]
    return canonical(q)


def diagram_audit(n):
    """All transitive subgroups -> all invariant equality families, modulo relabelling."""
    ambient=bijections((2,)*n); maps=cell_maps(n); groups=subgroups(ambient)
    reps={}
    for group in groups:
        if not transitive(group,n):continue
        p=partition((2,)*n,group)
        key=min(relabel(p,m) for m in maps)
        reps[key]=None
    ps=sorted(reps); orbit={p:{relabel(p,m) for m in maps} for p in ps}
    # Family(p) includes family(q) when every p-equality follows from q,
    # after one relabelling. Distinct q-block values are a necessity witness.
    relation={(i,j) for i,p in enumerate(ps) for j,q in enumerate(ps)
              if any(implies(r,p) for r in orbit[q])}
    covers=[(i,j) for i,j in relation if i!=j and not any(k!=i and k!=j and (i,k) in relation and (k,j) in relation for k in range(len(ps)))]
    frozen=json.loads((ROOT/'research/original-diagrams.json').read_text())
    tex=frozen['figures'][str(n)]['latex']

    # Extract only the corresponding diagram nodes by section bounds.
    marker='\\label{2pHasse}' if n==2 else '\\label{3pHasse}'
    end=tex.index(marker); begin=tex.rfind('\\begin{figure}',0,end)
    segment=tex[begin:end]; node_ids=[]; matched=[]; node_patterns={}
    for label,body in re.findall(r'\\node \((r\dc\d)\).*?\\begin\{tabular\}(.*?)\\end\{tabular\}',segment,re.S):
        tokens=re.findall(r'\$([^$\n]+)\$',body)
        rows=[tuple(t.strip().lstrip('\\') for t in token.split(',')) for token in tokens if ',' in token and 'Gamma' not in token]
        p=canonical(sum((list(row) for row in rows),[]))
        key=min(relabel(p,m) for m in maps)
        node_ids.append(label); matched.append(ps.index(key) if key in ps else None); node_patterns[label]=p
    edge_pairs=[]
    for chain in re.findall(r'\\draw(?:\[[^]]*\])?\s*((?:\(r\dc\d\)\s*--\s*)+\(r\dc\d\))',segment):
        ids=re.findall(r'\((r\dc\d)\)',chain); edge_pairs.extend(zip(ids,ids[1:]))
    lookup=dict(zip(node_ids,matched))
    actual={frozenset((lookup[a],lookup[b])) for a,b in edge_pairs}
    expected={frozenset(e) for e in covers}
    def binary(p,flips):
        return tuple(p),tuple((1,0) if f else (0,1) for f in flips)
    if n==2:
        a=binary((1,0),(0,0)); b=binary((1,0),(1,1)); c=binary((1,0),(1,0))
        gs={'r1c1':[a],'r2c1':[a,b],'r2c2':[c],'r3c1':[a,c]}
    else:
        a=binary((1,2,0),(0,0,0)); b=binary((1,0,2),(0,0,0))
        c=binary((1,0,2),(1,1,1)); d=binary((1,2,0),(1,1,1))
        e=binary((1,2,0),(1,1,0))
        gs={'r1c1':[a],'r2c1':[a,b],'r2c2':[a,c],'r2c3':[d],
            'r3c1':[a,b,e],'r3c2':[a,b,c],'r4c1':[a,b,e,c]}
    generator_tables={node:canonical(partition((2,)*n,gens))==canonical(node_patterns[node]) for node,gens in gs.items()}
    if n==3:
        generator_tables['G32_pair_21_23']=canonical(partition((2,)*n,[a,b,d]))==canonical(node_patterns['r3c2'])
        generator_tables['G32_pair_22_23']=canonical(partition((2,)*n,[a,c,d]))==canonical(node_patterns['r3c2'])
    classes=[]
    profiles=tuple(product(range(2),repeat=n))
    for p in ps:
        game={s:tuple(p[k*n:k*n+n]) for k,s in enumerate(profiles)}
        cls=classify(game)
        classes.append({'partition':p,'parameters':len(set(p)),**{k:cls[k] for k in ['automorphism_order','player_image_order','symmetric','n_transitive','standard','fully']}})
    return {'n':n,'ambient_order':len(ambient),'subgroup_count':len(groups),'family_count':len(ps),
            'classes':classes,'covers_general_to_special':covers,'source_nodes':dict(zip(node_ids,matched)),
            'source_all_nodes_match':None not in matched and len(set(matched))==len(ps),
            'source_edges_match':actual==expected,'source_edges':edge_pairs,'generator_tables_match':generator_tables}


def run():
    games,records=source_games()
    results={'scope':'Exact finite source tables, equality of symbolic parameters; no floating point or sampled automorphisms.',
             'extracted_source_tables':records,'generic':{},'specializations':{}}
    for ident,game in games.items():
        results['generic'][ident]=classify(game,ident.startswith(('5.13','5.14','5.15','5.16')))
        names={x for row in game.values() for x in row}
        if any(isinstance(x,str) for x in names):
            if len(names)<=4:
                cases=[]
                for pat in equality_patterns(len(names)):
                    c=classify(specialize(game,pat))
                    cases.append({'parameter_order':sorted(names),'equality_pattern':pat,**{k:c[k] for k in ['automorphism_order','player_image_order','standard','fully','n_transitive','pure_equilibria']}})
                results['specializations'][ident]={'scope':'all equality partitions for automorphisms; equilibrium lists apply only to the displayed integer ordering of blocks','cases':cases}
            else:
                c=classify(specialize(game,[0]*len(names)))
                results['specializations'][ident]={'scope':'all-equal witness only; partial coincidences not exhausted',
                    'all_equal':{k:c[k] for k in ['automorphism_order','player_image_order','standard','fully','n_transitive']}}
    results['source_generator_checks']={ident:dict(generators=gs,generated_order=len(generated_by(gs)),equals_full_generic_aut=generated_by(gs)==set(automorphisms(games[ident]))) for ident,gs in source_generators().items()}
    results['diagrams']=[diagram_audit(n) for n in (2,3)]
    (ROOT/'experiments/classification-results.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps({k:{j:v for j,v in c.items() if j in ['automorphism_order','player_image_order','standard','fully','symmetric','n_transitive']} for k,c in results['generic'].items()},indent=2))
    print(json.dumps(results['diagrams'],indent=2))
    return results

if __name__=='__main__':run()
