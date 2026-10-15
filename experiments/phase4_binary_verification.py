"""Independent exact full-image binary audit, using symbolic Coxeter equations.

Standard library only. No imports from the Phase 3 group search. Each solution
is a subgroup family, not a claim about the exact automorphism group of every
specialization. Arbitrary real payoff assignments are covered by cell orbits.
"""
from collections import Counter
import argparse
import json
from pathlib import Path


def swap_bits(value, i, j):
    if ((value >> i) ^ (value >> j)) & 1:
        value ^= (1 << i) | (1 << j)
    return value


def nullspace(rows, width):
    """RREF over GF(2), with least-index pivots; return a nullspace basis."""
    rows = [x for x in rows if x]
    pivots = []
    r = 0
    for c in range(width):
        k = next((k for k in range(r, len(rows)) if rows[k] >> c & 1), None)
        if k is None:
            continue
        rows[r], rows[k] = rows[k], rows[r]
        for k in range(len(rows)):
            if k != r and rows[k] >> c & 1:
                rows[k] ^= rows[r]
        pivots.append(c)
        r += 1
    free = [c for c in range(width) if c not in pivots]
    return [sum(1 << p for p, row in zip(pivots, rows[:r]) if row >> c & 1)
            | (1 << c) for c in free]


def cocycles(n, kernel):
    """All adjacent-lift assignments in V/kernel satisfying the Sn presentation."""
    dim = {'zero': n, 'constant': n - 1, 'even': 1, 'all': 0}[kernel]
    width = dim * (n - 1)
    # Representatives in V: last coordinate zero modulo constants, first
    # coordinate only modulo the even-weight module.
    gens = [[(1 << (a * dim + j)) if j < dim else 0 for j in range(n)]
            for a in range(n - 1)]
    relators = [(a, a) for a in range(n - 1)]
    relators += [(a, b, a, b) for a in range(n - 1)
                 for b in range(a + 2, n - 1)]
    relators += [(a, a + 1) * 3 for a in range(n - 2)]
    rows = []
    for word in relators:
        translation = [0] * n
        for a in word:
            translation[a], translation[a + 1] = translation[a + 1], translation[a]
            translation = [x ^ y for x, y in zip(translation, gens[a])]
        if kernel == 'constant':
            rows.extend(x ^ translation[-1] for x in translation[:-1])
        elif kernel == 'even':
            value = 0
            for x in translation:
                value ^= x
            rows.append(value)
        elif kernel == 'zero':
            rows.extend(translation)
    basis = nullspace(rows, width)
    assignments = [0]
    for vector in basis:
        assignments += [x ^ vector for x in assignments]
    for assignment in assignments:
        flips = []
        for a in range(n - 1):
            flips.append(sum(((assignment >> (a * dim + j)) & 1) << j
                             for j in range(dim)))
        yield flips, len(basis)


class Orbits:
    def __init__(self, size):
        self.parent = list(range(size))

    def root(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def join(self, x, y):
        x, y = self.root(x), self.root(y)
        if x != y:
            self.parent[max(x, y)] = min(x, y)


def utility_partition(n, kernel, flips):
    size = 1 << n
    dsu = Orbits(n * size)
    translations = {'zero': [], 'constant': [size - 1],
                    'even': [1 | (1 << j) for j in range(1, n)],
                    'all': [1 << j for j in range(n)]}[kernel]
    for i in range(n):
        for s in range(size):
            for b in translations:
                dsu.join(i * size + s, i * size + (s ^ b))
            for a, b in enumerate(flips):
                target = a + 1 if i == a else a if i == a + 1 else i
                dsu.join(i * size + s,
                         target * size + (swap_bits(s, a, a + 1) ^ b))
    return [dsu.root(x) for x in range(n * size)]


def square_witness(n, partition):
    size = 1 << n
    for i in range(n):
        for j in range(i + 1, n):
            for s in range(size):
                if s & ((1 << i) | (1 << j)):
                    continue
                si, sj, sij = s ^ (1 << i), s ^ (1 << j), s ^ (1 << i) ^ (1 << j)
                # [D_i(j=1)-D_i(j=0)]-[D_j(i=1)-D_j(i=0)].
                terms = [(i, sij, 1), (i, sj, -1), (i, si, -1), (i, s, 1),
                         (j, sij, -1), (j, si, 1), (j, sj, 1), (j, s, -1)]
                coefficients = Counter()
                for p, t, sign in terms:
                    coefficients[partition[p * size + t]] += sign
                nonzero = {str(k): v for k, v in coefficients.items() if v}
                if nonzero:
                    return {'players': [i, j], 'base_profile': s,
                            'coefficients': nonzero}
    return None


def full_matching(n, partition):
    """Existence of local labels making ordinary Sn act, on all utilities."""
    size = 1 << n
    for labels in range(size // 2):  # labels and labels+all-ones give same lifts
        good = True
        for a in range(n - 1):
            b = labels ^ swap_bits(labels, a, a + 1)
            for i in range(n):
                target = a + 1 if i == a else a if i == a + 1 else i
                for s in range(size):
                    if partition[i * size + s] != partition[
                            target * size + (swap_bits(s, a, a + 1) ^ b)]:
                        good = False
                        break
                if not good:
                    break
            if not good:
                break
        if good:
            return labels
    return None


def audit(n):
    size = 1 << n
    cases = []
    for kernel in ['zero', 'constant', 'even', 'all']:
        summary = {'kernel': kernel, 'quotient_cocycle_dimension': None,
                   'subgroups': 0, 'potential_families': 0,
                   'full_matching_families': 0, 'own_action_indifferent_families': 0,
                   'orbit_count_histogram': {}}
        histogram = Counter()
        failures = []
        for flips, dimension in cocycles(n, kernel):
            summary['quotient_cocycle_dimension'] = dimension
            summary['subgroups'] += 1
            partition = utility_partition(n, kernel, flips)
            histogram[len(set(partition))] += 1
            witness = square_witness(n, partition)
            summary['potential_families'] += witness is None
            summary['full_matching_families'] += full_matching(n, partition) is not None
            summary['own_action_indifferent_families'] += all(
                partition[i * size + s] == partition[i * size + (s ^ (1 << i))]
                for i in range(n) for s in range(size))
            if witness is not None:
                failures.append({'flips': flips, 'square': witness})
        summary['orbit_count_histogram'] = {str(k): v for k, v in sorted(histogram.items())}
        summary['potential_failures'] = failures
        cases.append(summary)
    return {'players': n, 'subgroups': sum(x['subgroups'] for x in cases),
            'kernels': cases}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--players', nargs='+', type=int, default=[3, 4, 5, 6])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = {'method': 'Independent symbolic GF(2) Coxeter equations and utility-cell square coefficients',
              'domains': [audit(n) for n in args.players]}
    encoded = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.write_text(encoded)
    else:
        print(encoded, end='')


if __name__ == '__main__':
    main()
