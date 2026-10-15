import unittest
from phase4_reductions import census, canonical_restriction_identity


class ReductionTests(unittest.TestCase):
    def test_exact_source_restriction(self):
        self.assertTrue(canonical_restriction_identity())

    def test_every_binary_rectangular_restriction(self):
        counts, exceptional = census()
        self.assertEqual(dict(counts), {
            (False, False, False): 210,
            (True, True, False): 4,
            (True, False, False): 2,
        })
        self.assertEqual(exceptional, [((0, 1),) * 3, ((0, 3),) * 3,
                                       ((1, 2),) * 3, ((2, 3),) * 3])

class OrientationTests(unittest.TestCase):
    def test_exact_full_ternary_automorphism_group(self):
        from phase4_reductions import orientation_game
        from matching_audit import bijections, action, matchings, matching_element
        from itertools import permutations
        payoffs = orientation_game()
        def even(p):
            return sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3)) % 2 == 0
        actual = {g for g in bijections((3, 3, 3))
                  if all(payoffs[s][i] == payoffs[action(g, s)][g[0][i]]
                         for s in payoffs for i in range(3))}
        predicted = {(p, (f,) * 3) for p in permutations(range(3))
                     for f in permutations(range(3)) if even(p) == even(f)}
        self.assertEqual(actual, predicted)
        self.assertEqual(len(actual), 18)
        self.assertFalse(any(all(matching_element(m, p) in actual
                                 for p in permutations(range(3)))
                             for m in matchings((3, 3, 3))))

    def test_all_binary_restrictions_have_no_target_separation(self):
        from phase4_reductions import orientation_game, restriction
        from classification_audit import classify
        from itertools import combinations, product
        for subsets in product(tuple(combinations(range(3), 2)), repeat=3):
            result = classify(restriction(orientation_game(), subsets))
            self.assertFalse(result['n_transitive'] and not result['fully'])

    def test_two_value_orientation_family_is_always_full(self):
        from phase4_reductions import orientation_binary_coarsening_census
        self.assertEqual(dict(orientation_binary_coarsening_census()),
                         {(36, True): 12, (108, True): 2, (1296, True): 2})
