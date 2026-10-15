"""Independent audit tests, with deliberate negative controls."""
import json
from pathlib import Path
import unittest

from phase4_ternary_crosscheck import verify as verify_ternary_certificate

from phase4_binary_verification import (audit, cocycles, full_matching, nullspace,
                                        square_witness, utility_partition)


class Phase4BinaryVerificationTests(unittest.TestCase):
    def test_rref_nullspace_against_bruteforce(self):
        rows = [0b10101, 0b11010, 0b01111, 0b10001]
        basis = nullspace(rows, 5)
        span = {0}
        for x in basis:
            span |= {v ^ x for v in span}
        self.assertEqual(span, {v for v in range(32)
                               if all((v & row).bit_count() % 2 == 0 for row in rows)})

    def test_matching_pennies_is_rejected(self):
        # A quarter-turn lift of the player swap; kernel global complement.
        partition = utility_partition(2, 'constant', [1])
        self.assertIsNotNone(square_witness(2, partition))
        self.assertIsNone(full_matching(2, partition))

    def test_unconstrained_utilities_are_rejected(self):
        self.assertIsNotNone(square_witness(3, list(range(24))))

    def test_complete_n3_to_n6_saved_results(self):
        stored = json.loads(Path(__file__).with_name('phase4-binary-results.json').read_text())
        observed = [audit(n) for n in [3, 4, 5, 6]]
        self.assertEqual(stored['domains'], observed)
        self.assertEqual([d['subgroups'] for d in observed], [15, 35, 51, 99])
        for result in observed:
            for case in result['kernels']:
                self.assertEqual(case['potential_families'], case['subgroups'])
                if result['players'] >= 5:
                    self.assertEqual(case['full_matching_families'], case['subgroups'])

    def test_independent_ternary_certificate(self):
        result = verify_ternary_certificate()
        self.assertEqual(result['distinct_groups'], 19)
        self.assertEqual(result['orientation_game_exact_group_order'], 18)
        self.assertFalse(result['orientation_game_full_matching'])

    def test_n4_exception_is_passive(self):
        nonfull = 0
        for flips, _ in cocycles(4, 'constant'):
            p = utility_partition(4, 'constant', flips)
            if full_matching(4, p) is None:
                nonfull += 1
                self.assertTrue(all(p[i * 16 + s] == p[i * 16 + (s ^ (1 << i))]
                                    for i in range(4) for s in range(16)))
        self.assertEqual(nonfull, 8)


if __name__ == '__main__':
    unittest.main()
