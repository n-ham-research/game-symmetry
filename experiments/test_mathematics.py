import unittest
from itertools import permutations, product
from math import factorial
from finite_games import (automorphisms, binary_game, common_payoffs, compose,
                          inverse_condition, permute, player_transitive, symmetries)
from constraint_audit import audit


class MathematicalChecks(unittest.TestCase):
    def test_action_composition(self):
        # All 3-player binary profiles and pairs of permutations.
        for pi, tau, s in product(permutations(range(3)), permutations(range(3)), product(range(2), repeat=3)):
            self.assertEqual(permute(tau, permute(pi, s)), permute(compose(tau, pi), s))

    def test_complete_constraint_partitions(self):
        self.assertEqual(len(audit()['cases']), 9)

    def test_nonconstant_common_payoff(self):
        game = binary_game(3, lambda s, i: 5 + 7 * (sum(s) >= 2))
        self.assertTrue(inverse_condition(game, 3))
        self.assertEqual(game[(0, 0, 0)], (5, 5, 5))
        self.assertEqual(game[(1, 1, 0)], (12, 12, 12))

    def test_two_player_boundary_and_transpositions(self):
        for n in [2, 3, 4]:
            game = binary_game(n, lambda s, i: s[i])
            self.assertEqual(len(symmetries(game, n)), factorial(n))
            self.assertFalse(common_payoffs(game))
            self.assertEqual(inverse_condition(game, n), n == 2)

    def test_common_payoff_does_not_imply_symmetry(self):
        game = binary_game(3, lambda s, i: s[0])
        self.assertTrue(common_payoffs(game))
        self.assertFalse(inverse_condition(game, 3))
        self.assertFalse(player_transitive(symmetries(game, 3), 3))

    def test_corollary_424_counterexample(self):
        game = binary_game(2, lambda s, i: i)
        autos = tuple(automorphisms(game, (2, 2)))
        self.assertTrue(autos)
        self.assertFalse(player_transitive((pi for pi, _ in autos), 2))
        # Every payoff individually is profile-invariant, stronger than opponent anonymity.
        for i in range(2):
            self.assertEqual({row[i] for row in game.values()}, {i})

    def test_matching_pennies_requires_strategy_relabeling(self):
        game = binary_game(2, lambda s, i: (1 if s[0] == s[1] else -1) * (-1)**i)
        self.assertEqual(symmetries(game, 2), ((0, 1),))
        autos = tuple(automorphisms(game, (2, 2)))
        self.assertEqual(len(autos), 4)
        self.assertTrue(player_transitive((pi for pi, _ in autos), 2))

    def test_unequal_strategy_cardinalities(self):
        game = {s: (0, 0) for s in product(range(1), range(2))}
        autos = tuple(automorphisms(game, (1, 2)))
        self.assertTrue(all(pi == (0, 1) for pi, _ in autos))

    def test_product_surjectivity_boundary(self):
        # With one varying coordinate the probability tuple is its marginal.
        from fractions import Fraction
        p = {(0, 0): Fraction(1, 3), (0, 1): Fraction(2, 3)}
        marginal_0 = {0: sum(p.values())}
        marginal_1 = {j: p[0, j] for j in range(2)}
        self.assertTrue(all(prob == marginal_0[i]*marginal_1[j] for (i, j), prob in p.items()))
        correlated = {(0, 0): Fraction(1, 2), (0, 1): 0, (1, 0): 0, (1, 1): Fraction(1, 2)}
        self.assertEqual(correlated[0, 1], 0)
        self.assertNotEqual(correlated[0, 1], Fraction(1, 2)**2)


if __name__ == '__main__':
    unittest.main()
