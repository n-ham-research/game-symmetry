"""Exhaustive subgroup certificate for three-player, three-strategy boundary.

No payoff-table enumeration. Every standard game can be relabelled so its
strategy-trivial three-cycle is r. Enumerate all possible odd lifts g and only
form <r,g>; every full-image automorphism group contains one of these groups.
"""
from collections import Counter
from itertools import permutations, product
import json
from pathlib import Path
from matching_audit import action, bijections, matchings, matching_element, multiply

IDENTITY_PERM = (0, 1, 2)
E = (IDENTITY_PERM, (IDENTITY_PERM,) * 3)
R = ((1, 2, 0), E[1])
T = (0, 2, 1)
EVEN = {IDENTITY_PERM, R[0], (2, 0, 1)}


def generated(generators):
    """Finite positive words equal the subgroup; breadth-first closure."""
    found, todo = {E}, [E]
    while todo:
        a = todo.pop()
        for g in generators:
            b = multiply(g, a)
            if b not in found:
                found.add(b)
                todo.append(b)
    return frozenset(found)


def cell_orbits(group):
    cells = tuple((s, i) for s in product(range(3), repeat=3) for i in range(3))
    labels = {}
    for s, i in cells:
        if (s, i) not in labels:
            label = len(set(labels.values()))
            for g in group:
                labels[action(g, s), g[0][i]] = label
    return labels


def orbit_closure(group, ambient):
    """All typed maps preserving each individual focal-profile orbit."""
    labels = cell_orbits(group)
    return frozenset(g for g in ambient
                     if all(labels[s, i] == labels[action(g, s), g[0][i]]
                            for s, i in labels))


def complement(group):
    """Coxeter presentation S3=<a,t | a^3=t^2=1, tat=a^-1>."""
    for a in sorted(group):
        if a[0] != R[0] or multiply(multiply(a, a), a) != E:
            continue
        for t in sorted(group):
            if (t[0] == T and multiply(t, t) == E and
                    multiply(multiply(t, a), t) == multiply(a, a)):
                return a, t
    return None


def full_matching(group):
    for f in matchings((3, 3, 3)):
        if all(matching_element(f, p) in group for p in permutations(range(3))):
            return f
    return None


def twisted(transposition):
    return frozenset((p, ((IDENTITY_PERM if p in EVEN else transposition),) * 3)
                     for p in permutations(range(3)))


def verify():
    ambient = bijections((3, 3, 3))
    indexes = {g: i for i, g in enumerate(ambient)}
    minimal = {}
    odd_lifts = [g for g in ambient if g[0] not in EVEN]
    assert len(ambient) == 1296 and len(odd_lifts) == 648
    for g in odd_lifts:
        h = generated((R, g))
        minimal.setdefault(h, g)
    assert len(minimal) == 19
    transpositions = tuple(p for p in permutations(range(3))
                           if p not in EVEN)
    exceptional = {twisted(h) for h in transpositions}
    records = []
    for h, g in sorted(minimal.items(), key=lambda item: (len(item[0]), sorted(item[0]))):
        pair = complement(h)
        assert pair is not None
        assert len(generated(pair)) == 6
        cl = orbit_closure(h, ambient)
        matching = full_matching(cl)
        assert (matching is None) == (h in exceptional)
        assert h not in exceptional or cl == h
        records.append({
            'odd_generator': indexes[g], 'group_order': len(h),
            'elements': sorted(indexes[x] for x in h),
            'complement_generators': [indexes[x] for x in pair],
            'orbit_count': len(set(cell_orbits(h).values())),
            'orbit_closure_order': len(cl),
            'orbit_closure_full_matching': matching,
            'exceptional_twisted_section': h in exceptional,
        })
    # The exceptional sections generate the parity fibre-product group.
    union = frozenset().union(*exceptional)
    larger = generated(tuple(union))
    assert len(larger) == 18
    assert {g for g in larger if g[0] not in EVEN} == {g for g in union if g[0] not in EVEN}
    assert full_matching(larger) is None
    assert orbit_closure(larger, ambient) == larger
    assert len({g[0] for g in larger}) == 6
    kernel = [g for g in larger if g[0] == IDENTITY_PERM]
    assert len(kernel) == 3
    # Any nonfull actual A must have every odd element in this union, so choose
    # one odd lift t. Then every k in ker(q|A) satisfies kt in this union, forcing
    # k into the diagonal A3 of order 3. Hence A=H6 or A=larger.
    return {
        'players': 3, 'strategies_per_player': 3,
        'ambient_order': len(ambient), 'odd_lifts_checked': len(odd_lifts),
        'distinct_generated_groups': len(minimal),
        'order_histogram': {str(k): v for k, v in sorted(Counter(map(len, minimal)).items())},
        'all_generated_groups_split': True,
        'nonfull_actual_group_orders': [6, 18],
        'exceptional_order_18_elements': sorted(indexes[g] for g in larger),
        'records': records,
    }


if __name__ == '__main__':
    result = verify()
    target = Path(__file__).with_name('phase4-ternary-results.json')
    import sys
    if '--verify' in sys.argv:
        assert json.loads(target.read_text()) == json.loads(json.dumps(result))
    else:
        target.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ('records', 'exceptional_order_18_elements')}, indent=2))
