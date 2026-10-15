"""Independent tuple verifier for the four-player regular-cycle certificate.

No project group implementation is imported. Default checks all 21 group and
section witnesses; --exhaustive additionally reconstructs all 251 lift classes.
"""
from itertools import permutations, product
import json
from pathlib import Path

PS = tuple(permutations(range(4)))
FS = tuple(permutations(range(3)))
LOCAL = tuple(product(FS, repeat=4))
E = (PS[0], (FS[0],) * 4)
R = ((1, 2, 3, 0), E[1])
A = (2, 0, 1, 3)


def decode(x):
    return PS[x // 1296], LOCAL[x % 1296]


def multiply(g, h):
    p, fs = g
    q, ks = h
    return (tuple(p[q[i]] for i in range(4)),
            tuple(tuple(fs[q[i]][ks[i][a]] for a in range(3)) for i in range(4)))


def close(generators):
    seen, todo = {E}, [E]
    while todo:
        x = todo.pop()
        for g in generators:
            y = multiply(g, x)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return frozenset(seen)


def simultaneous_conjugate(fs, h):
    hi = tuple(h.index(a) for a in range(3))
    return tuple(tuple(h[f[hi[a]]] for a in range(3)) for f in fs)


def verify(exhaustive=False):
    certificate = json.loads(Path(__file__).with_name('phase5_splitting-c4-results.json').read_text())
    groups = set()
    for record in certificate['records']:
        group = close((R, decode(record['generator'])))
        assert len(group) == record['group_order']
        a, b = map(decode, record['section'])
        assert a in group and b in group and a[0] == R[0] and b[0] == A
        section = close((a, b))
        assert len(section) == 24 and len({g[0] for g in section}) == 24
        groups.add(group)
    assert len(groups) == 21
    reps = {min(simultaneous_conjugate(fs, h) for h in FS) for fs in LOCAL}
    assert len(reps) == 251
    if exhaustive:
        assert {close((R, (A, fs))) for fs in reps} == groups
    return {'groups_checked': 21, 'sections_checked': 21,
            'lift_classes': 251, 'all_lift_groups_regenerated': exhaustive}


if __name__ == '__main__':
    import sys
    print(json.dumps(verify('--exhaustive' in sys.argv), indent=2))
