"""Regression counterexamples and exact source calculations for audit pass 2."""
import unittest
from itertools import product
from finite_games import automorphisms, player_transitive
from matching_audit import action, bijections, matchings, multiply, subgroups
from classification_audit import source_games
from ordinal_audit import count


class SecondAuditTests(unittest.TestCase):
    def test_abstract_transitivity_counterexample(self):
        game = {(0,0,0,0): (0,0,1,1)}
        group = tuple(automorphisms(game,(1,1,1,1)))
        self.assertEqual(len(group),4)
        image = {g[0] for g in group}
        self.assertFalse(player_transitive(image,4))
        regular = {(0,1,2,3),(1,0,3,2),(2,3,0,1),(3,2,1,0)}
        self.assertTrue(player_transitive(regular,4))
        # Both groups consist of identity and three commuting involutions.
        for g in group:
            self.assertEqual(multiply(g,g),group[0])
        self.assertTrue(all(multiply(a,b)==multiply(b,a) for a in group for b in group))

    def test_wreath_factor_orders(self):
        self.assertEqual(len(bijections((3,3))),72)
        self.assertEqual(len(bijections((2,2,2))),48)

    def test_untagged_matching_maps_need_not_close(self):
        p = (1,2,3,0)
        pinv = (3,0,1,2)
        identity = tuple(range(4))
        self.assertNotIn(tuple(p[p[i]] for i in range(4)),{identity,p,pinv})

    def test_prop24_printed_order(self):
        u = ((0,1),(2,3))
        # This payoff is additive, so mixed extrema attain the displayed boundaries.
        self.assertEqual(min(max(u[i][j] for i in range(2)) for j in range(2)),2)
        self.assertEqual(min(max(row) for row in u),1)

    def test_original_example43_isomorphism(self):
        games,_ = source_games()
        g = ((1,0),((0,1),(1,0)))
        for s,row in games['4.3a'].items():
            self.assertEqual(tuple(games['4.3b'][action(g,s)][g[0][i]] for i in range(2)),row)

    def test_original_example44_components(self):
        g = ((1,2,0),((1,0),(0,1),(1,0)))
        h = ((1,0,2),((0,1),(0,1),(1,0)))
        self.assertEqual(multiply(h,g),((0,2,1),((1,0),(1,0),(1,0))))
        printed_inverse = ((2,0,1),((1,0),(1,0),(0,1)))
        self.assertEqual(multiply(g,printed_inverse),((0,1,2),((0,1),)*3))

    def test_matching_examples(self):
        m = ((0,1),(1,0),(1,0)) # source 4.18: (a,d,f), (b,c,e)
        self.assertEqual({tuple(c[a] for c in m) for a in range(2)},{(0,1,1),(1,0,0)})
        self.assertEqual(len(matchings((2,2))),2)
        self.assertEqual(len(matchings((3,3))),6)

    def test_ordinal_convention_counts(self):
        self.assertEqual([count(t,s)['classes'] for t in (False,True) for s in (False,True)], [144,78,1413,726])

    def test_own_action_symmetry_not_same_player_invariance(self):
        from finite_games import binary_game, symmetries, permute
        game = binary_game(3,lambda s,i:s[i])
        self.assertEqual(len(symmetries(game,3)),6)
        self.assertNotEqual(game[(1,0,0)][0],game[permute((1,0,2),(1,0,0))][0])

    def test_utility_equality_under_uniform_law_does_not_imply_role_equivalence(self):
        game = {s:(2*s[0]+s[1],3-2*s[0]-s[1]) for s in product(range(2),repeat=2)}
        self.assertEqual([sum(row[i] for row in game.values()) for i in range(2)],[6,6])
        group = tuple(automorphisms(game,(2,2)))
        self.assertFalse(player_transitive((p for p,_ in group),2))


if __name__ == '__main__':
    unittest.main()
