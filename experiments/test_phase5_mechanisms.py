import unittest
from phase5_mechanisms import certificate, orientation_game, predicted_group, sign
from matching_audit import action
from itertools import product


class OppositeFaceTests(unittest.TestCase):
    def test_exact_four_player_ternary_binary_and_signed_groups(self):
        result = certificate(3)
        self.assertEqual(result['aut_order'], 72)
        self.assertTrue(result['binary_same_group'])
        self.assertFalse(result['full_matching'])
        self.assertTrue(result['zero_sum'])

    def test_binary_boundary_is_signed_three_player_mechanism(self):
        result = certificate(2)
        self.assertEqual(result['aut_order'], 6)
        self.assertTrue(result['binary_same_group'])
        self.assertFalse(result['full_matching'])

    def test_surjective_completion_invariant_and_covariance_next_size(self):
        # This checks the counting lemma and covariance beyond the exhaustive
        # ambient-group cases; the theorem's arbitrary-size proof is analytic.
        m = 4
        signed = orientation_game(m)
        binary = orientation_game(m, binary=True)
        self.assertTrue(all(sum(row) == int(len(set(s)) == m) for s, row in binary.items()))
        equal = sum(len(set((0, 0) + s)) == m for s in product(range(m), repeat=m-1))
        distinct = sum(len(set((0, 1) + s)) == m for s in product(range(m), repeat=m-1))
        self.assertEqual((equal, distinct), (6, 18))
        p, f = (1, 0, 2, 3, 4), (1, 0, 2, 3)
        g = p, (f,) * (m+1)
        self.assertTrue(all(row[i] == signed[action(g, s)][p[i]]
                            for s, row in signed.items() for i in range(m+1)))


if __name__ == '__main__':
    unittest.main()
