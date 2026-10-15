"""Exact second obstruction: determinant-even signed permutations, n=4,m=6.

This is an independent construction, not the smaller Z4 construction.
The full-Aut reduction is proved in research/phase3-splitting-search.md.
"""
from itertools import permutations, product
import json

N = 4
COLORS = range(3)
PERMS = tuple(permutations(range(N)))
BITS = tuple(product(range(2), repeat=N))
COLORTUPLES = tuple(product(COLORS, repeat=N))


def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2


def utility(colors, bits, i):
    others = tuple(colors[j] for j in range(N) if j != i)
    if len(set(others)) < 3:
        return 3 * colors[i]
    return 3 * colors[i] + 1 + ((sum(bits) + i + parity(others)) % 2)


def transport(p, shifts, colors, bits):
    target_colors = [None] * N
    target_bits = [None] * N
    for i in range(N):
        target_colors[p[i]] = colors[i]
        target_bits[p[i]] = bits[i] ^ shifts[i][colors[i]]
    return tuple(target_colors), tuple(target_bits)


def multiply(g, h):
    p, v = g
    q, w = h
    return tuple(p[q[i]] for i in range(N)), tuple(w[i] ^ v[q[i]] for i in range(N))


def run():
    zero = (0,) * N
    # A utility's quotient by 3 is its focal action color. Hence every exact
    # automorphism preserves color in each typed component. Its remaining
    # freedom is an independently chosen bit flip for every player/color.
    # Bit dependence is affine; zero-bit profiles suffice to check each map.
    shifts = tuple(product(range(2), repeat=3))
    survivors = []
    candidates = 0
    for p in PERMS:
        for fs in product(shifts, repeat=N):
            candidates += 1
            good = True
            for colors in COLORTUPLES:
                tc, tb = transport(p, fs, colors, zero)
                if any(utility(colors, zero, i) != utility(tc, tb, p[i]) for i in range(N)):
                    good = False
                    break
            if good:
                assert all(len(set(f)) == 1 for f in fs)
                v = tuple(f[0] for f in fs)
                assert sum(v) % 2 == parity(p)
                survivors.append((p, v))
    expected = [(p,v) for p in PERMS for v in BITS if sum(v) % 2 == parity(p)]
    assert set(survivors) == set(expected)
    # Independent direct numerical verification on every payoff cell.
    for p, v in survivors:
        fs = tuple((b,b,b) for b in v)
        for colors in COLORTUPLES:
            for bits in BITS:
                tc, tb = transport(p, fs, colors, bits)
                assert all(utility(colors,bits,i) == utility(tc,tb,p[i]) for i in range(N))
    identity = (tuple(range(N)), zero)
    t = (1,0,2,3)
    r = (0,1,3,2)
    invol_t = [g for g in survivors if g[0] == t and multiply(g,g) == identity]
    invol_r = [g for g in survivors if g[0] == r and multiply(g,g) == identity]
    commuting_pairs = [(g,h) for g in invol_t for h in invol_r if multiply(g,h)==multiply(h,g)]
    assert not commuting_pairs
    return dict(status='candidate extension; complete proof in research note; novelty unchecked',
                players=4, strategies_each=6, payoff_values=list(range(9)),
                color_preserving_candidates=candidates, automorphism_order=len(survivors),
                player_image_order=len(set(p for p,v in survivors)),
                kernel_order=sum(p==tuple(range(N)) for p,v in survivors),
                standard_subgroup='pure A4 (strategy trivial, transitive)',
                involutions_above_12=len(invol_t), involutions_above_34=len(invol_r),
                commuting_lift_pairs=len(commuting_pairs), split=False,
                checked_payoff_cells_per_automorphism=4*6**4)


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
