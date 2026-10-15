"""Proof-sensitive checks for the binary equilibrium investigation."""
from itertools import product
import json
from pathlib import Path
import unittest

from classification_audit import classify, source_games
from matching_audit import partition
from phase3_equilibria import (adjacent, pclosure, typed, run,
                               square_residuals, quotient_cocycle_basis)


class BinaryEquilibriumResearchTests(unittest.TestCase):
    def test_complete_small_group_search_reproduces_artifact(self):
        result = run()
        stored = json.loads(Path(__file__).with_name('phase3-equilibria-results.json').read_text())
        self.assertEqual(result, stored)
        self.assertEqual([d['groups'] for d in result['domains']], [5, 15, 35])
        for domain in result['domains'][1:]:
            self.assertTrue(all(c['exact_potential_for_all_payoffs'] for c in domain['classes']))
        for c in result['domains'][2]['classes']:
            self.assertTrue(c['family_forces_full_symmetry_up_to_relabeling'] or
                            c['every_profile_equilibrium_for_all_payoffs'])
        self.assertTrue(any(not c['exact_potential_for_all_payoffs']
                            for c in result['domains'][0]['classes']))

    def test_signed_three_player_potential_for_every_small_parameter_assignment(self):
        group = tuple(typed(g) for g in pclosure(
            [(adjacent(3, i), (1, 1, 1)) for i in range(2)], 3))
        blocks = partition((2, 2, 2), group)
        profiles = tuple(product(range(2), repeat=3))
        names = sorted(set(blocks))
        self.assertEqual(len(names), 4)
        self.assertFalse(square_residuals(3, blocks))
        for values in product(range(3), repeat=4):
            parameters = dict(zip(names, values))
            rows = [parameters[b] for b in blocks]
            game = {s: tuple(rows[3*k:3*k+3]) for k, s in enumerate(profiles)}
            alpha, delta = game[(0, 0, 0)][0], game[(1, 0, 0)][0]
            potential = {s: alpha if len(set(s)) == 1 else delta for s in profiles}
            for s in profiles:
                for i in range(3):
                    t = s[:i] + (1-s[i],) + s[i+1:]
                    self.assertEqual(game[t][i]-game[s][i], potential[t]-potential[s])
            equilibria = [s for s in profiles if all(
                game[s][i] >= game[s[:i]+(1-s[i],)+s[i+1:]][i] for i in range(3))]
            expected = [s for s in profiles if
                        (alpha >= delta if len(set(s)) == 1 else delta >= alpha)]
            self.assertEqual(equilibria, expected)

    def test_standard_alone_does_not_suffice(self):
        game = {s: tuple(int(s[i] != s[(i+1) % 3]) for i in range(3))
                for s in product(range(2), repeat=3)}
        info = classify(game)
        self.assertTrue(info['standard'])
        self.assertEqual(info['player_image_order'], 3)
        self.assertFalse(info['n_transitive'])
        self.assertEqual(info['pure_equilibria'], [])

    def test_original_four_player_exception_has_no_own_incentives(self):
        game = source_games()[0]['5.15']
        self.assertEqual(len(set(x for row in game.values() for x in row)), 2)
        for s in game:
            for i in range(4):
                self.assertEqual(game[s][i], game[s[:i]+(1-s[i],)+s[i+1:]][i])
        info = classify(game)
        self.assertTrue(info['n_transitive'])
        self.assertFalse(info['standard'])
        self.assertEqual(info['player_kernel_order'], 2)

    def test_quotient_cocycle_dimensions(self):
        self.assertEqual([len(quotient_cocycle_basis(n)) for n in (3, 4, 5, 6)],
                         [2, 4, 4, 5])


if __name__ == '__main__':
    unittest.main()
