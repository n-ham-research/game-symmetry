"""Regression certificates for actual ternary splitting boundaries."""
import json
from pathlib import Path
import unittest
import phase5_splitting as c4
import phase5_splitting_six as six


class SplittingBoundaryTests(unittest.TestCase):
    def test_six_actual_binary_game_certificate(self):
        expected=json.loads(Path(six.__file__).with_name('phase5_splitting-six-results.json').read_text())
        self.assertEqual(json.loads(json.dumps(six.verify_six())),expected)

    def test_all_stored_regular_cycle_section_certificates(self):
        result=json.loads(Path(c4.__file__).with_name('phase5_splitting-c4-results.json').read_text())
        self.assertEqual(len(c4.c4_representatives()),251)
        self.assertEqual(len(result['records']),21)
        for row in result['records']:
            h=c4.generated((c4.R,row['generator']))
            self.assertEqual(len(h),row['group_order'])
            r,a=row['section']
            self.assertTrue({r,a}<=h)
            self.assertEqual(r//c4.BASE,c4.R//c4.BASE)
            self.assertEqual(a//c4.BASE,c4.A//c4.BASE)
            self.assertEqual(len(c4.generated((r,a))),24)


if __name__=='__main__':unittest.main()
