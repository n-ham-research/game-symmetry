"""Independent verifier of the binary common-interest six-player witness.

Imports no project implementation. The eighteen-point generators are ATLAS
3S6G1-p18aB0.g1/.g2. Their advertised group identity is not assumed.
"""
from itertools import permutations, product
import json


def cycles(*cs):
    out = list(range(18))
    for c in cs:
        for x, y in zip(c, c[1:] + c[:1]):
            out[x - 1] = y - 1
    return tuple(out)


ID = tuple(range(18))
A = cycles((2, 6), (3, 5), (4, 10), (8, 14), (9, 13), (11, 17), (15, 16))
B = cycles((1, 2, 7, 11, 4), (3, 8, 15, 17, 10), (5, 9, 16, 18, 12))
BLOCKS = ((0, 2, 4), (1, 7, 8), (3, 9, 11), (5, 12, 13), (6, 14, 15), (10, 16, 17))
SEEDS = ('000100', '002221', '011122', '012010', '020212', '021001')
CODE = frozenset(tuple((int(a) + k) % 3 for a in s) for s in SEEDS for k in range(3))
STANDARD_X = (7, 4, 8, 3, 1, 14, 13, 0, 2, 9, 10, 11, 15, 6, 5, 12, 16, 17)
STANDARD_Y = (7, 13, 8, 16, 1, 0, 9, 5, 12, 17, 14, 10, 2, 4, 11, 3, 15, 6)


def compose(g, h):
    return tuple(g[a] for a in h)


def inverse(g):
    return tuple(g.index(a) for a in range(18))


def close(gs):
    seen, todo = {ID}, [ID]
    while todo:
        h = todo.pop()
        for g in gs:
            y = compose(g, h)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return frozenset(seen)


def typed(g):
    locations = {a: (i, j) for i, b in enumerate(BLOCKS) for j, a in enumerate(b)}
    p = tuple(locations[g[b[0]]][0] for b in BLOCKS)
    fs = tuple(tuple(locations[g[a]][1] for a in b) for b in BLOCKS)
    assert all(locations[g[a]][0] == p[i] for i, b in enumerate(BLOCKS) for a in b)
    return p, fs


def action(g, s):
    p, fs = g
    t = [None] * 6
    for i in range(6):
        t[p[i]] = fs[i][s[i]]
    return tuple(t)


def verify():
    assert len(CODE) == 18
    group = close((A, B))
    assert len(group) == 2160
    tg = {typed(g) for g in group}
    assert len(tg) == 2160 and len({p for p, _ in tg}) == 720
    assert all(action(g, s) in CODE for g in tg for s in CODE)
    # Forward containment on a finite set under a bijection implies equality;
    # complement profiles are then preserved too. This exhausts all 6^6 local
    # maps, rather than all 720*6^6 typed maps.
    local_kernel = []
    for fs in product(tuple(permutations(range(3))), repeat=6):
        if all(tuple(fs[i][s[i]] for i in range(6)) in CODE for s in CODE):
            local_kernel.append(fs)
    expected = {tuple((tuple((a + k) % 3 for a in range(3)),) * 6) for k in range(3)}
    assert set(local_kernel) == expected
    # Full player image and kernel of order three bound the full game group
    # by 720*3=2160, so the preserving group above is the entire exact group.
    standard = close((STANDARD_X, STANDARD_Y))
    assert standard <= group and len(standard) == 60
    st = [typed(g) for g in standard]
    assert {p[0] for p, _ in st} == set(range(6))
    assert all(p[i] != i or fs[i] == (0, 1, 2) for p, fs in st for i in range(6))
    even = close((B, compose(compose(A, B), A)))
    assert len(even) == 1080
    assert all(sum(p[i] > p[j] for i in range(6) for j in range(i + 1, 6)) % 2 == 0
               for p, _ in map(typed, even))
    x, y = B, compose(compose(A, B), A)
    commutator = compose(compose(compose(x, y), inverse(x)), inverse(y))
    commutator_conjugates = {compose(compose(g, commutator), inverse(g)) for g in even}
    assert close(tuple(commutator_conjugates)) == even
    # Hence the 1080-element even preimage is perfect. A section would give
    # an index-three subgroup therein; its coset action to S3 is impossible
    # for a perfect group, because S3 has no nontrivial perfect subgroup.
    return {'binary_common_interest_profiles': 18, 'actual_group_order': 2160,
            'actual_player_image_order': 720, 'all_pointwise_maps_checked': 46656,
            'actual_player_kernel_order': 3, 'standard_subgroup_order': 60,
            'perfect_even_preimage_order': 1080, 'nonsplitting_verified': True}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
