"""Independent verifier of the ternary certificate through 81-cell permutations.

Does not import the generating search, matching_audit, or finite_games. It
reconstructs each typed action directly as a permutation of utility cells.
"""
from collections import Counter
from itertools import permutations, product
import json
from pathlib import Path


def compose(a, b):
    return tuple(a[x] for x in b)


def ambient_actions():
    perms = tuple(permutations(range(3)))
    cells = tuple((s, i) for s in product(range(3), repeat=3) for i in range(3))
    index = {c: k for k, c in enumerate(cells)}
    elements, actions = [], []
    for p in perms:
        for f in product(perms, repeat=3):
            mapping = []
            for s, i in cells:
                target = [None] * 3
                for j in range(3):
                    target[p[j]] = f[j][s[j]]
                mapping.append(index[tuple(target), p[i]])
            elements.append((p, f))
            actions.append(tuple(mapping))
    return cells, elements, actions


def close(generators, actions, inverse_index):
    todo = [0]
    group = {0}
    while todo:
        x = todo.pop()
        for g in generators:
            y = inverse_index[compose(actions[g], actions[x])]
            if y not in group:
                group.add(y)
                todo.append(y)
    return frozenset(group)


def orbit_labels(generator_actions):
    parent = list(range(81))
    def root(k):
        while parent[k] != k:
            k = parent[k]
        return k
    for g in generator_actions:
        for k, target in enumerate(g):
            x, y = root(k), root(target)
            parent[max(x, y)] = min(x, y)
    return [root(k) for k in range(81)]


def verify():
    certificate = json.loads(Path(__file__).with_name('phase4-ternary-results.json').read_text())
    cells, elements, actions = ambient_actions()
    lookup = {a: i for i, a in enumerate(actions)}
    element_index = {g: i for i, g in enumerate(elements)}
    identity = (0, 1, 2)
    rotation = element_index[((1, 2, 0), (identity,) * 3)]
    def odd(p):
        return sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2
    odds = [i for i, g in enumerate(elements) if odd(g[0])]
    groups = {close((rotation, g), actions, lookup) for g in odds}
    assert len(groups) == 19
    assert groups == {frozenset(r['elements']) for r in certificate['records']}
    perms = tuple(permutations(range(3)))
    matching_groups = []
    for f1, f2 in product(perms, repeat=2):
        labels = (identity, f1, f2)
        inverse = [tuple(f.index(a) for a in range(3)) for f in labels]
        matching_groups.append(frozenset(element_index[(p, tuple(
            tuple(labels[p[i]][inverse[i][a]] for a in range(3))
            for i in range(3)))] for p in perms))
    for record in certificate['records']:
        group = frozenset(record['elements'])
        actual = close((rotation, record['odd_generator']), actions, lookup)
        assert actual == group
        section = close(record['complement_generators'], actions, lookup)
        assert len(section) == 6 and section <= group
        assert len({elements[k][0] for k in section}) == 6
        labels = orbit_labels([actions[rotation], actions[record['odd_generator']]])
        closure = frozenset(i for i, action in enumerate(actions)
                            if all(labels[k] == labels[action[k]] for k in range(81)))
        assert len(closure) == record['orbit_closure_order']
        assert len(set(labels)) == record['orbit_count']
        has_matching = any(h <= closure for h in matching_groups)
        assert has_matching == (record['orbit_closure_full_matching'] is not None)
    # Recompute the common-interest orientation game's full automorphism group.
    def orientation(s):
        return 0 if len(set(s)) < 3 else (-1 if odd(s) else 1)
    values = [orientation(s) for s, _ in cells]
    orientation_group = frozenset(i for i, action in enumerate(actions)
                                 if all(values[k] == values[action[k]] for k in range(81)))
    assert len(orientation_group) == 18
    assert orientation_group == frozenset(certificate['exceptional_order_18_elements'])
    assert not any(h <= orientation_group for h in matching_groups)
    assert len({elements[k][0] for k in orientation_group}) == 6
    assert sum(elements[k][0] == identity for k in orientation_group) == 3
    return {'ambient_actions': len(actions), 'odd_generators': len(odds),
            'distinct_groups': len(groups), 'certified_sections': len(groups),
            'group_order_histogram': {str(k): v for k, v in sorted(Counter(map(len, groups)).items())},
            'orientation_game_exact_group_order': len(orientation_group),
            'orientation_game_kernel_order': 3,
            'orientation_game_full_matching': False}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
