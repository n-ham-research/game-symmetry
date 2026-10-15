"""Conjugacy reduction and independently regenerated finite proof checks."""
import json
from pathlib import Path
import unittest
from phase5_ternary_audit import verify
from phase5_ternary_four_crosscheck import verify as verify_four
from phase5_ternary_six_crosscheck import verify as verify_six


class TernaryAuditTests(unittest.TestCase):
    def test_complete_independent_certificate(self):
        result = verify()
        stored = json.loads(Path(__file__).with_name('phase5-ternary-audit-results.json').read_text())
        self.assertEqual(json.loads(json.dumps(result)), stored)
        self.assertEqual(sum(r['number_of_embedded_conjugates'] for r in result['records']), 19)
        self.assertEqual(sum(r['fixed_transposition_lift_classes'] for r in result['records']), 32)
        self.assertEqual([r['order'] for r in result['records'] if r['exceptional']], [6])

    def test_independent_four_player_section_witnesses(self):
        self.assertEqual(verify_four()["sections_checked"], 21)

    def test_independent_six_player_binary_witness(self):
        result = verify_six()
        self.assertTrue(result["nonsplitting_verified"])
        self.assertEqual(result["actual_group_order"], 2160)

    def test_burnside_reduction_count(self):
        # Centralizer sizes in S3, class sizes, and centralizer sizes of squares.
        types = ((1, 6, 6), (3, 2, 6), (2, 3, 3))
        ordinary = sum(k * c ** 3 for k, c, _ in types)
        swapped = sum(k * c * square_c for k, c, square_c in types)
        self.assertEqual((ordinary, swapped), (294, 90))
        self.assertEqual((ordinary + swapped) // 12, 32)


if __name__ == '__main__':
    unittest.main()
