"""Regression of the exact finite nonsplitting witness, against all typed maps."""
import json
from pathlib import Path
import unittest
from phase3_splitting import verify


class SplittingCounterexampleTest(unittest.TestCase):
    def test_exhaustive_witness_agrees_with_record(self):
        record = json.loads(Path(__file__).with_name('phase3-splitting-results.json').read_text())
        # Compare JSON-normalized values: generated profiles use tuple keys in Python.
        self.assertEqual(record, json.loads(json.dumps(verify())))

    def test_two_payoff_value_witness(self):
        record = json.loads(Path(__file__).with_name('phase3-splitting-binary-results.json').read_text())
        self.assertEqual(record, json.loads(json.dumps(verify(binary_payoffs=True))))


if __name__ == '__main__':
    unittest.main()
