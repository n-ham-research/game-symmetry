"""Boundary examples for exact restriction and clone multiplicity theorems."""
import unittest
from itertools import product
from matching_audit import action, bijections, multiply


def automorphisms(game, sizes):
    return {g for g in bijections(sizes)
            if all(game[action(g, s)][g[0][i]] == row[i]
                   for s, row in game.items() for i in range(len(sizes)))}


def clone_game(fibres):
    maps = tuple(tuple(c for c, count in enumerate(counts) for _ in range(count))
                 for counts in fibres)
    game = {s: (sum(maps[i][s[i]] for i in range(2)),) * 2
            for s in product(*(range(len(mapping)) for mapping in maps))}
    return maps, game


class ExactReductionTests(unittest.TestCase):
    def test_equal_size_rectangle_can_lose_full_image(self):
        matrix = ((1, 2, 3), (2, 4, 5), (3, 5, 6))
        source = {s: (matrix[s[0]][s[1]],) * 2 for s in product(range(3), repeat=2)}
        self.assertEqual({g[0] for g in automorphisms(source, (3, 3))},
                         {(0, 1), (1, 0)})
        restricted = {(a, b): source[(a, b+1)] for a, b in product(range(2), repeat=2)}
        self.assertEqual({g[0] for g in automorphisms(restricted, (2, 2))}, {(0, 1)})

    def test_uniform_clones_lift_quotient_swap(self):
        maps, game = clone_game(((2, 2), (2, 2)))
        group = automorphisms(game, (4, 4))
        # Four independent within-class interchanges, times the quotient swap.
        self.assertEqual(len(group), 32)
        lift = ((1, 0), (tuple(range(4)),) * 2)
        self.assertIn(lift, group)
        self.assertEqual(multiply(lift, lift), ((0, 1), (tuple(range(4)),) * 2))

    def test_discarded_multiplicities_create_player_swap(self):
        maps, game = clone_game(((1, 2), (2, 1)))
        group = automorphisms(game, (3, 3))
        self.assertEqual(len(group), 4)
        self.assertEqual({g[0] for g in group}, {(0, 1)})
        quotient = {s: (sum(s),) * 2 for s in product(range(2), repeat=2)}
        self.assertEqual(len(automorphisms(quotient, (2, 2))), 2)
        self.assertEqual({g[0] for g in automorphisms(quotient, (2, 2))},
                         {(0, 1), (1, 0)})
