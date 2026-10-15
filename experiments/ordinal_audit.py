"""Complete ordinal 2x2 counts under explicitly different equivalences.

Payoff ranks are normalized separately per player. Weak orders include ties.
This checks Ham's surrounding convention, not the uninspected cited book.
"""
from itertools import permutations, product
import json
from pathlib import Path
from matching_audit import action, bijections


def orders(ties):
    if not ties:
        return tuple(permutations(range(4)))
    return tuple(v for v in product(range(4), repeat=4)
                 if set(v) == set(range(max(v)+1)))


def count(ties, allow_player_swap):
    profiles = tuple(product(range(2), repeat=2))
    ids = {s: i for i, s in enumerate(profiles)}
    group = [g for g in bijections((2,2)) if allow_player_swap or g[0] == (0,1)]
    cell_maps = [tuple(2*ids[action(g,s)] + g[0][i] for s in profiles for i in range(2)) for g in group]
    fixed = [0]*len(group)
    representatives = set()
    os = orders(ties)
    for a, b in product(os, repeat=2):
        v = tuple(z for pair in zip(a,b) for z in pair)
        images = []
        for j, mapping in enumerate(cell_maps):
            t = [None]*8
            for k, target in enumerate(mapping):
                t[target] = v[k]
            t = tuple(t)
            fixed[j] += t == v
            images.append(t)
        representatives.add(min(images))
    assert sum(fixed) % len(group) == 0
    assert len(representatives) == sum(fixed)//len(group)
    return dict(ties=ties, player_swaps=allow_player_swap, orders_per_player=len(os),
                labelled_games=len(os)**2, relabellings=len(group), classes=len(representatives),
                fixed_counts=fixed, method='Complete orbit enumeration, independently cross-checked by Burnside fixed-point average')


def run():
    result = dict(scope='All normalized strict/weak-order payoff rankings in 2x2; not a general game classification',
                  cases=[count(ties,swap) for ties in (False,True) for swap in (False,True)])
    Path(__file__).with_name('ordinal-results.json').write_text(json.dumps(result,indent=2)+'\n')
    return result


if __name__ == '__main__':
    print(json.dumps(run(),indent=2))
