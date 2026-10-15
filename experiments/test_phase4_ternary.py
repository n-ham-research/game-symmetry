"""Exact subgroup boundary certificate; no sampling or floating point."""
import json
from pathlib import Path
import unittest
from phase4_ternary import (E, R, T, EVEN, cell_orbits, complement, full_matching,
                            generated, multiply, twisted, verify)


class TernaryBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = verify()

    def test_committed_certificate_matches_full_regeneration(self):
        expected = json.loads(Path(__file__).with_name('phase4-ternary-results.json').read_text())
        self.assertEqual(expected, json.loads(json.dumps(self.result)))

    def test_all_odd_lifts_and_exceptional_classification(self):
        self.assertEqual(self.result['odd_lifts_checked'], 648)
        self.assertEqual(self.result['distinct_generated_groups'], 19)
        exceptional = [r for r in self.result['records'] if r['exceptional_twisted_section']]
        self.assertEqual(len(exceptional), 3)
        self.assertTrue(all(r['group_order'] == r['orbit_closure_order'] == 6
                            and r['orbit_count'] == 15 for r in exceptional))

    def test_two_twisted_sections_generate_second_mechanism(self):
        h1, h2 = twisted((1, 0, 2)), twisted((0, 2, 1))
        larger = generated(tuple(h1 | h2))
        self.assertEqual(len(larger), 18)
        self.assertEqual(len([g for g in larger if g[0] == (0, 1, 2)]), 3)
        self.assertIsNone(full_matching(larger))
        self.assertIsNotNone(complement(larger))
        self.assertEqual(len(set(cell_orbits(larger).values())), 6)


if __name__ == '__main__':
    unittest.main()
