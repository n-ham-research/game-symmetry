"""Exact binary full-player-image group search and symbolic potential checks.

No numerical sampling: each group imposes an equality partition of utility
cells; square-cycle coefficients are checked as formal integer vectors.
"""
from collections import Counter, deque
from itertools import permutations, product
import json
from pathlib import Path

from finite_games import compose
from matching_audit import (action, bijections, matchings, matching_element,
                            partition, subgroups, transitive, implies)


def pmul(g, h):
    """Target-coordinate flips: (p,b) acts by y[p[i]]=x[i]+b[p[i]]."""
    p, b = g
    q, c = h
    d = list(b)
    for i in range(len(p)):
        d[p[i]] ^= c[i]
    return compose(p, q), tuple(d)


def pclosure(generators, n):
    identity = (tuple(range(n)), (0,) * n)
    seen = {identity}
    todo = deque([identity])
    while todo:
        h = todo.popleft()
        for g in generators:
            k = pmul(g, h)
            if k not in seen:
                seen.add(k)
                todo.append(k)
    return tuple(sorted(seen))


def typed(g):
    p, b = g
    return p, tuple((1, 0) if b[p[i]] else (0, 1) for i in range(len(p)))


def adjacent(n, i):
    p = list(range(n))
    p[i], p[i + 1] = p[i + 1], p[i]
    return tuple(p)


def quotient_relations(n):
    """Coxeter relators; inverses equal generators modulo the kernel."""
    relations = [(i, i) for i in range(n - 1)]
    relations += [(i, j, i, j) for i in range(n - 1)
                  for j in range(i + 2, n - 1)]
    relations += [(i, i + 1) * 3 for i in range(n - 2)]
    return relations


def quotient_cocycle_basis(n):
    """All sections Sn->(F2^n/<1>) semidirect Sn, via exact GF(2)."""
    width = (n - 1) ** 2
    relations = quotient_relations(n)

    def evaluate(word, bits):
        gs = [(adjacent(n, i), tuple((bits >> (i * (n - 1) + j)) & 1
                                    for j in range(n - 1)) + (0,))
              for i in range(n - 1)]
        result = (tuple(range(n)), (0,) * n)
        for i in word:
            result = pmul(result, gs[i])
        return result[1]

    rows = []
    for word in relations:
        cols = [evaluate(word, 1 << k) for k in range(width)]
        for j in range(n - 1):
            row = sum((col[j] ^ col[-1]) << k for k, col in enumerate(cols))
            if row:
                rows.append(row)
    pivots = {}
    for row in rows:
        while row:
            p = row.bit_length() - 1
            if p in pivots:
                row ^= pivots[p]
            else:
                pivots[p] = row
                break
    free = [i for i in range(width) if i not in pivots]
    basis = []
    for i in free:
        value = 1 << i
        for p, row in sorted(pivots.items()):
            if (value & row).bit_count() % 2:
                value ^= 1 << p
        basis.append(value)
    return tuple(basis)


def full_image_groups(n):
    """Complete for n>=3 using four invariant kernel types.

    K=0 complements use the point-stabilizer character classification.
    K=<1> uses every Coxeter solution in the quotient, not random generators.
    K=even uses both homomorphisms Sn->C2; K=all has one group.
    """
    identity = tuple(range(n))
    zero = (0,) * n
    one = (1,) * n
    perms = tuple(permutations(range(n)))
    out = set()
    for labels in product(range(2), repeat=n - 1):
        labels = labels + (0,)
        for twist in (0, 1):
            generators = []
            for i in range(n - 1):
                p = adjacent(n, i)
                b = tuple(labels[j] ^ labels[p[j]] ^ twist for j in range(n))
                generators.append((p, b))
            out.add(tuple(typed(g) for g in pclosure(generators, n)))
    basis = quotient_cocycle_basis(n)
    for coefficients in product(range(2), repeat=len(basis)):
        bits = 0
        for c, vector in zip(coefficients, basis):
            if c:
                bits ^= vector
        generators = [(identity, one)]
        for i in range(n - 1):
            b = tuple((bits >> (i * (n - 1) + j)) & 1
                      for j in range(n - 1)) + (0,)
            generators.append((adjacent(n, i), b))
        group = pclosure(generators, n)
        assert len(group) == 2 * len(perms)
        out.add(tuple(typed(g) for g in group))
    even_generators = []
    for i in range(n - 1):
        b = [0] * n
        b[i] = b[-1] = 1
        even_generators.append((identity, tuple(b)))
    for twist in (0, 1):
        b = (twist,) + (0,) * (n - 1)
        gs = even_generators + [(adjacent(n, i), b) for i in range(n - 1)]
        out.add(tuple(typed(g) for g in pclosure(gs, n)))
    out.add(tuple(sorted(bijections((2,) * n))))
    return tuple(sorted(out, key=lambda g: (len(g), g)))


def square_residuals(n, blocks):
    """Return nonzero formal sums around each oriented square of the cube."""
    profiles = tuple(product(range(2), repeat=n))
    ids = {(s, i): k for k, (s, i) in
           enumerate((s, i) for s in profiles for i in range(n))}
    bad = []
    for i in range(n):
        for j in range(i + 1, n):
            others = [k for k in range(n) if k not in (i, j)]
            for values in product(range(2), repeat=n - 2):
                s = [0] * n
                for k, a in zip(others, values):
                    s[k] = a
                a = tuple(s)
                s[i] = 1
                b = tuple(s)
                s[j] = 1
                c = tuple(s)
                s[i] = 0
                d = tuple(s)
                cells = [(b, i, 1), (a, i, -1), (c, j, 1), (b, j, -1),
                         (d, i, 1), (c, i, -1), (a, j, 1), (d, j, -1)]
                residual = Counter()
                for profile, player, sign in cells:
                    residual[blocks[ids[profile, player]]] += sign
                if any(residual.values()):
                    bad.append((i, j, values, dict(residual)))
    return bad


def passive(n, blocks):
    profiles = tuple(product(range(2), repeat=n))
    ids = {(s, i): k for k, (s, i) in
           enumerate((s, i) for s in profiles for i in range(n))}
    return all(blocks[ids[s, i]] == blocks[ids[s[:i] + (1 - s[i],) + s[i+1:], i]]
               for s in profiles for i in range(n))


def classify_group(n, group):
    perms = tuple(permutations(range(n)))
    aset = set(group)
    matching_images = []
    for m in matchings((2,) * n):
        h = tuple(matching_element(m, p) for p in perms
                  if matching_element(m, p) in aset)
        matching_images.append((transitive(h, n), len(h) == len(perms)))
    blocks = partition((2,) * n, group)
    return dict(order=len(group), kernel=len(group) // len(perms),
                subgroup_has_transitive_matching=any(t for t, f in matching_images),
                subgroup_has_full_matching=any(f for t, f in matching_images),
                family_forces_full_symmetry_up_to_relabeling=any(
                    implies(blocks, partition((2,) * n,
                        tuple(matching_element(m, p) for p in perms)))
                    for m in matchings((2,) * n)),
                exact_potential_for_all_payoffs=not square_residuals(n, blocks),
                every_profile_equilibrium_for_all_payoffs=passive(n, blocks),
                utility_orbits=len(set(blocks)))


def canonical_family(n, blocks):
    """Canonical equality partition under every typed strategy/player relabeling."""
    profiles = tuple(product(range(2), repeat=n))
    cells = tuple((s, i) for s in profiles for i in range(n))
    ids = {cell: k for k, cell in enumerate(cells)}
    images = []
    for g in bijections((2,) * n):
        transformed = [None] * len(cells)
        for k, (s, i) in enumerate(cells):
            transformed[ids[action(g, s), g[0][i]]] = blocks[k]
        names = {}
        images.append(tuple(names.setdefault(v, len(names)) for v in transformed))
    return min(images)


def run():
    results = {'scope': 'All full-player-image binary typed-bijection subgroups '
               'for n=2,3,4; all real payoff assignments constant on each '
               'subgroup utility-cell orbit. Isomorphic copies are retained '
               'only as group coverage, not counted as independent games.',
               'domains': []}
    for n in (2, 3, 4):
        if n <= 3:
            groups = tuple(g for g in subgroups(bijections((2,) * n))
                           if len({x[0] for x in g}) == len(tuple(permutations(range(n)))))
        else:
            groups = full_image_groups(n)
        if n == 3:
            assert {frozenset(g) for g in groups} == {
                frozenset(g) for g in full_image_groups(n)}
        classes = [classify_group(n, g) for g in groups]
        histogram = Counter(tuple(c[k] for k in c) for c in classes)
        results['domains'].append({'n': n, 'groups': len(groups),
                                  'utility_equality_families_up_to_typed_relabeling': len({
                                      canonical_family(n, partition((2,) * n, g))
                                      for g in groups}),
                                  'classes': [dict(zip(classes[0], key), groups=count)
                                              for key, count in sorted(histogram.items())]})
    return results


if __name__ == '__main__':
    output = run()
    path = Path(__file__).with_name('phase3-equilibria-results.json')
    path.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))
