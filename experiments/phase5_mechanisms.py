"""Exact certificates for the opposite-face orientation games (candidate P5-M1)."""
from itertools import permutations, product
from collections import Counter
from matching_audit import action, bijections, matchings, matching_element


def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))


def orientation_game(m=3, binary=False):
    n = m + 1
    def row(s):
        values = tuple((-1) ** i * sign(s[:i] + s[i+1:])
                       if len(set(s[:i] + s[i+1:])) == m else 0 for i in range(n))
        return tuple(int(x > 0) for x in values) if binary else values
    return {s: row(s) for s in product(range(m), repeat=n)}


def predicted_group(m=3):
    return {(p, (f,) * (m+1)) for p in permutations(range(m+1))
            for f in permutations(range(m)) if sign(p) == sign(f)}


def automorphisms(payoffs, m):
    return {g for g in bijections((m,) * (m+1))
            if all(all(row[i] == payoffs[action(g, s)][g[0][i]] for i in range(m+1))
                   for s, row in payoffs.items())}


def certificate(m=3):
    signed = orientation_game(m)
    binary = orientation_game(m, binary=True)
    predicted = predicted_group(m)
    actual = automorphisms(signed, m)
    binary_aut = automorphisms(binary, m)
    assert actual == predicted
    full = any(all(matching_element(c, p) in actual for p in permutations(range(m+1)))
               for c in matchings((m,) * (m+1)))
    return {'players': m+1, 'strategies': m, 'ambient_order': len(bijections((m,) * (m+1))),
            'aut_order': len(actual), 'binary_aut_order': len(binary_aut),
            'binary_same_group': binary_aut == actual, 'full_matching': full,
            'zero_sum': all(sum(row) == 0 for row in signed.values()),
            'binary_payoff_histogram': dict(Counter(binary.values()))}


if __name__ == '__main__':
    for m in (2, 3):
        print(certificate(m))
