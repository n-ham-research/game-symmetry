"""Compare full equality partitions, not random payoff samples.

Each variable is one exact payoff entry (player, profile). Equality constraints
join variables. Two partitions agree iff they impose the same equalities for
all payoff assignments on this fixed finite domain. This is finite evidence,
not a proof for arbitrary n or action sets.
"""
import argparse
from itertools import permutations, product
import json
from pathlib import Path
from finite_games import inverse, permute


def partition(n, m, condition):
    profiles = tuple(product(range(m), repeat=n))
    variables = tuple((i, s) for i in range(n) for s in profiles)
    parent = {x: x for x in variables}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def join(x, y):
        x, y = find(x), find(y)
        if x != y:
            parent[y] = x

    if condition not in {'C', 'D', 'CE'}:
        raise ValueError(condition)
    for pi in permutations(range(n)):
        action = inverse(pi) if condition == 'D' else pi
        for i, s in variables:
            join((i, s), (pi[i], permute(action, s)))
    if condition == 'CE':
        for s in profiles:
            for i in range(1, n):
                join((0, s), (i, s))
    groups = {}
    for x in variables:
        groups.setdefault(find(x), set()).add(x)
    return frozenset(frozenset(group) for group in groups.values())


def audit():
    rows = []
    for n, m in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 2), (4, 3), (5, 2)]:
        c, d, ce = (partition(n, m, kind) for kind in ['C', 'D', 'CE'])
        expected = d == (c if n == 2 else ce)
        if not expected:
            raise AssertionError((n, m, 'partition mismatch'))
        rows.append(dict(n=n, actions=m, payoff_entries=n*m**n,
                         C_classes=len(c), D_classes=len(d), CE_classes=len(ce),
                         D_equals_C=d == c, D_equals_CE=d == ce))
    return dict(scope='Exact equality partitions on specified finite domains; no general proof by enumeration',
                cases=rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = json.dumps(audit(), indent=2) + '\n'
    if args.output:
        args.output.write_text(result)
    else:
        print(result, end='')
