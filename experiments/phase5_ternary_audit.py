"""Independent 32-lift/11-subgroup conjugacy proof of the ternary boundary.

Uses only the Python standard library; no Phase 4 group implementation or
certificate is imported. Run --verify to compare the committed certificate.
"""
from collections import Counter
from itertools import permutations, product
import json
from pathlib import Path

P = tuple(permutations(range(3)))
I = (0, 1, 2)
T = (0, 2, 1)
R = (1, 2, 0)
E = (I, (I,) * 3)
W = tuple((p, fs) for p in P for fs in product(P, repeat=3))
N = tuple((p, (f,) * 3) for p in P for f in P)


def cp(a, b):
    return tuple(a[x] for x in b)


def ip(a):
    return tuple(a.index(x) for x in range(3))


def mul(a, b):
    p, fs = a
    q, gs = b
    return cp(p, q), tuple(cp(fs[q[i]], gs[i]) for i in range(3))


def inv(g):
    p, fs = g
    q = ip(p)
    return q, tuple(ip(fs[q[i]]) for i in range(3))


def conjugate(n, g):
    return mul(mul(n, g), inv(n))


def close(gs):
    found, todo = {E}, [E]
    while todo:
        x = todo.pop()
        for g in gs:
            y = mul(g, x)
            if y not in found:
                found.add(y)
                todo.append(y)
    return frozenset(found)


def odd(p):
    return sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2


def act(g, cell):
    s, i = cell
    p, fs = g
    t = [None] * 3
    for j in range(3):
        t[p[j]] = fs[j][s[j]]
    return tuple(t), p[i]


CELLS = tuple((s, i) for s in product(range(3), repeat=3) for i in range(3))


def orbit_closure(h):
    labels = {}
    for c in CELLS:
        if c not in labels:
            label = len(set(labels.values()))
            for g in h:
                labels[act(g, c)] = label
    cl = frozenset(g for g in W if all(labels[c] == labels[act(g, c)] for c in CELLS))
    return cl, len(set(labels.values()))


def section(h):
    for a in sorted(h):
        if a[0] != R or mul(mul(a, a), a) != E:
            continue
        for t in sorted(h):
            if t[0] == T and mul(t, t) == E and mul(mul(t, a), t) == mul(a, a):
                assert len(close((a, t))) == 6
                return a, t
    raise AssertionError('No projection section')


def matching(h):
    for f1, f2 in product(P, repeat=2):
        fs = (I, f1, f2)
        lifts = [(p, tuple(cp(fs[p[i]], ip(fs[i])) for i in range(3))) for p in P]
        if all(g in h for g in lifts):
            return fs
    return None


def canonical(h):
    return min(tuple(sorted(conjugate(n, g) for g in h)) for n in N)


def verify():
    r = (R, (I,) * 3)
    fixed_lifts = {(T, fs) for fs in product(P, repeat=3)}
    stabilizer = tuple(n for n in N if cp(cp(n[0], T), ip(n[0])) == T)
    assert len(stabilizer) == 12
    remaining = set(fixed_lifts)
    lift_classes = []
    group_classes = {}
    while remaining:
        g = min(remaining)
        orbit = {conjugate(n, g) for n in stabilizer}
        assert orbit <= fixed_lifts
        remaining -= orbit
        h = close((r, g))
        key = canonical(h)
        group_classes.setdefault(key, []).append(g)
        lift_classes.append({'local_maps': g[1], 'orbit_size': len(orbit),
                             'group_key': key})
    assert len(lift_classes) == 32
    assert sum(c['orbit_size'] for c in lift_classes) == 216
    keys = sorted(group_classes, key=lambda k: (len(k), k))
    ids = {key: i for i, key in enumerate(keys)}
    records = []
    embedded = set()
    for key in keys:
        h = frozenset(key)
        conjugates = {frozenset(conjugate(n, g) for g in h) for n in N}
        embedded.update(conjugates)
        cl, orbits = orbit_closure(h)
        a, t = section(h)
        fm = matching(cl)
        is_exception = fm is None
        if is_exception:
            assert len(h) == 6 and cl == h
            assert h == frozenset((p, ((I if not odd(p) else t[1][0]),) * 3) for p in P)
        records.append({'class': ids[key], 'order': len(h),
                        'number_of_embedded_conjugates': len(conjugates),
                        'fixed_transposition_lift_classes': len(group_classes[key]),
                        'generator': group_classes[key][0],
                        'canonical_elements': [W.index(g) for g in key],
                        'section': [a, t], 'cell_orbits': orbits,
                        'closure_order': len(cl), 'closure_matching': fm,
                        'exceptional': is_exception})
    assert len(keys) == 11 and len(embedded) == 19
    assert Counter(map(len, embedded)) == {6: 4, 18: 3, 24: 6, 54: 3, 162: 1, 648: 2}
    assert sum(c['exceptional'] for c in records) == 1
    exceptional = [h for h in embedded if matching(orbit_closure(h)[0]) is None]
    assert len(exceptional) == 3
    l = close(tuple(g for h in exceptional for g in h))
    assert len(l) == 18 and matching(l) is None and orbit_closure(l)[0] == l
    assert l == frozenset((p, (f,) * 3) for p in P for f in P if odd(p) == odd(f))
    for c in lift_classes:
        c['group_class'] = ids[c.pop('group_key')]
    return {'fixed_transposition_lifts': 216, 'lift_conjugacy_classes': 32,
            'normalizer_order': 36, 'subgroup_conjugacy_classes': 11,
            'embedded_groups': 19, 'lift_classes': lift_classes, 'records': records}


if __name__ == '__main__':
    result = verify()
    target = Path(__file__).with_name('phase5-ternary-audit-results.json')
    encoded = json.dumps(result, indent=2) + '\n'
    import sys
    if '--verify' in sys.argv:
        assert json.loads(target.read_text()) == json.loads(encoded)
    else:
        target.write_text(encoded)
    print(json.dumps({k: v for k, v in result.items() if k not in ('records', 'lift_classes')}, indent=2))
    for r in result['records']:
        print(r['class'], r['order'], r['number_of_embedded_conjugates'],
              r['fixed_transposition_lift_classes'], r['cell_orbits'],
              r['closure_order'], r['closure_matching'] is not None)
