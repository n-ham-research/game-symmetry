"""Exact rectangular restriction census; no utility rounding or samples."""
from itertools import combinations, product
from collections import Counter
from phase3_splitting import game, binary_payoff_code
from classification_audit import classify, source_games


def restriction(payoffs, subsets):
    return {s: payoffs[tuple(subsets[i][s[i]] for i in range(3))]
            for s in product(range(2), repeat=3)}


def census():
    payoffs = game(binary_payoff_code)
    counts = Counter()
    exceptional = []
    for subsets in product(tuple(combinations(range(4), 2)), repeat=3):
        result = classify(restriction(payoffs, subsets))
        key = tuple(result[k] for k in ('standard', 'n_transitive', 'fully'))
        counts[key] += 1
        if key == (True, True, False):
            exceptional.append(subsets)
    return counts, exceptional


def canonical_restriction_identity():
    source = source_games()[0]['5.13']
    values = {'alpha': 0, 'beta': 1, 'gamma': 0, 'delta': 0}
    expected = {s: tuple(values[x] for x in row) for s, row in source.items()}
    return restriction(game(binary_payoff_code), ((0, 1),) * 3) == expected


if __name__ == '__main__':
    counts, exceptional = census()
    print(dict(counts))
    print(exceptional)
    assert canonical_restriction_identity()


def orientation_game():
    """Common utility orientation of three distinct actions; zero on repeats."""
    def value(s):
        if len(set(s)) != 3:
            return 0
        return (-1) ** sum(s[i] > s[j] for i in range(3) for j in range(i + 1, 3))
    return {s: (value(s),) * 3 for s in product(range(3), repeat=3)}


def orientation_binary_coarsening_census():
    from matching_audit import bijections, action, matchings, matching_element
    from itertools import permutations
    ambient = bijections((3, 3, 3))
    lifts = [{matching_element(m, p) for p in permutations(range(3))}
             for m in matchings((3, 3, 3))]
    profiles = tuple(product(range(3), repeat=3))
    counts = Counter()
    for values in product(range(2), repeat=4):
        def value(s):
            distinct = len(set(s))
            if distinct < 3:
                return values[distinct - 1]
            parity = sum(s[i] > s[j] for i in range(3) for j in range(i+1, 3)) % 2
            return values[2 + parity]
        payoffs = {s: value(s) for s in profiles}
        aut = {g for g in ambient if all(payoffs[s] == payoffs[action(g, s)]
                                         for s in profiles)}
        counts[len(aut), any(h <= aut for h in lifts)] += 1
    return counts
