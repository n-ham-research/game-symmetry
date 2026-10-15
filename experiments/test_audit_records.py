"""Source provenance and consequential review-impact checks."""
import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('audit_records',Path(__file__).resolve().parents[1]/'scripts/audit.py')
audit=importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class AuditRecordTests(unittest.TestCase):
    def test_original_records_and_complete_formal_coverage(self):
        result=audit.check()
        self.assertEqual(result['formal_results'],41)
        self.assertEqual(result['original_numbered_items'],74)
        self.assertEqual(result['counts'],{'Verified':33,'Verified after correction':7,'Unresolved':1})

    def test_actual_matching_dependencies(self):
        graph=audit.read('dependencies.json')
        self.assertTrue({'5.1','5.2','5.3'} <= set(audit.affected(graph,'4.23')))
        self.assertTrue({'5.1','5.2','5.3'}.isdisjoint(audit.affected(graph,'4.24')))
        self.assertEqual(audit.affected(graph,'2.2:strict-nonsurjectivity'),['2.2:strict-nonsurjectivity'])

    def test_transitive_impact_not_just_direct_edges(self):
        graph={'nodes':[{'id':x} for x in 'abcd'], 'edges':[{'source':'a','target':'b'},{'source':'b','target':'c'}]}
        self.assertEqual(audit.affected(graph,'a'),['a','b','c'])
        with self.assertRaises(ValueError):audit.affected(graph,'unknown')


if __name__=='__main__':unittest.main()
