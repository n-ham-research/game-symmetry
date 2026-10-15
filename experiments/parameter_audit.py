"""All equality patterns for the eight parameters in Ham Example 5.14a.

Generation enumerates exact automorphisms directly. Verification independently
compiles payoff preservation to equality constraints on the eight parameters.
No preference/equilibrium conclusion is inferred from equality patterns.
"""
from collections import Counter
import json
from pathlib import Path
from itertools import product, permutations
from classification_audit import source_games, equality_patterns, specialize, classify
from matching_audit import bijections, matchings, matching_element

OUTPUT=Path(__file__).with_name('parameter-results.json')
KEYS=['automorphism_order','player_image_order','standard','fully','n_transitive']


def generate():
    games,_=source_games(); game=games['5.14a']
    names=sorted({v for row in game.values() for v in row})
    rows=[]; hist=Counter()
    for pattern in equality_patterns(8):
        c=classify(specialize(game,pattern)); sig=tuple(c[k] for k in KEYS)
        rows.append([pattern,*sig]); hist[str(sig)]+=1
    result={'scope':'All 4140 equality partitions of the eight real parameters in original Example5.14a. Complete exact automorphism/matching classifications; no real-value sampling. Ordering of values is irrelevant for these symmetry predicates, not for equilibrium.',
            'parameter_order':names,'columns':['equality_pattern',*KEYS],
            'pattern_count':len(rows),'histogram':dict(sorted(hist.items())),'cases':rows}
    OUTPUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    return result


def verify(result):
    games,_=source_games(); game=games['5.14a']; n=4
    names=result['parameter_order']; index={v:i for i,v in enumerate(names)}
    gs=bijections((2,)*n)
    constraints={}
    # Independent inverse-index formula, not matching_audit.action/classify.
    for g in gs:
        pi,fs=g; inv=tuple(pi.index(j) for j in range(n))
        pairs=set()
        for s,row in game.items():
            t=tuple(fs[inv[j]][s[inv[j]]] for j in range(n))
            for i in range(n):
                a,b=index[row[i]],index[game[t][pi[i]]]
                if a!=b:pairs.add(tuple(sorted((a,b))))
        constraints[g]=tuple(pairs)
    lifts=[tuple(matching_element(m,p) for p in permutations(range(n))) for m in matchings((2,)*n)]
    patterns=set(equality_patterns(8)); seen=set(); hist=Counter()
    for row in result['cases']:
        pattern=tuple(row[0]);seen.add(pattern)
        autos={g for g in gs if all(pattern[a]==pattern[b] for a,b in constraints[g])}
        image={g[0] for g in autos}
        hs=[{g[0] for g in lift if g in autos} for lift in lifts]
        standard=any(all({p[i] for p in h}==set(range(n)) for i in range(n)) for h in hs)
        full=any(len(h)==24 for h in hs)
        sig=(len(autos),len(image),standard,full,len(image)==24)
        if tuple(row[1:])!=sig:raise AssertionError((pattern,row[1:],sig))
        hist[str(sig)]+=1
    if seen!=patterns or len(result['cases'])!=4140 or result['pattern_count']!=4140:
        raise AssertionError('Incomplete or duplicated equality-pattern coverage')
    if dict(hist)!=result['histogram']:raise AssertionError('Histogram differs')
    return len(seen)


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--verify',action='store_true');args=p.parse_args()
    result=json.loads(OUTPUT.read_text()) if args.verify else generate()
    print('Verified all',verify(result),'equality patterns by independent compiled constraints')
