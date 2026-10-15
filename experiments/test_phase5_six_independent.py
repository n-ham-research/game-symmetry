import unittest
from phase5_six_independent import certificate, binary_code_certificate


class SixPlayerIndependentTests(unittest.TestCase):
    def test_raw_permutation_group_standardness_full_closure_and_perfection(self):
        result=certificate()
        self.assertEqual(result['group_order'],2160)
        self.assertEqual(result['closure_pointwise_kernel'],3)
        self.assertEqual(result['even_derived_order'],result['even_preimage_order'])

    def test_binary_common_interest_code_has_same_exact_group(self):
        result=binary_code_certificate()
        self.assertEqual(result['codewords'],18)
        self.assertEqual(result['exact_aut_order'],2160)


if __name__=='__main__':
    unittest.main()
