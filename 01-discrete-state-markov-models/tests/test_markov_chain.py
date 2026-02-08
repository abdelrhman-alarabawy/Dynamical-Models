import pathlib
import sys
import unittest

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.markov_chain import (  # noqa: E402
    estimate_transition_matrix,
    simulate_chain,
    stationary_distribution,
    validate_transition_matrix,
)


class MarkovChainTests(unittest.TestCase):
    def setUp(self):
        self.matrix = {
            "A": {"A": 0.8, "B": 0.2},
            "B": {"A": 0.1, "B": 0.9},
        }

    def test_validate_transition_matrix(self):
        validate_transition_matrix(self.matrix)

    def test_simulate_chain_length(self):
        path = simulate_chain(self.matrix, initial_state="A", steps=5, seed=10)
        self.assertEqual(len(path), 6)
        self.assertTrue(set(path).issubset({"A", "B"}))

    def test_estimate_transition_matrix_rows_sum_to_one(self):
        transitions = [("A", "A"), ("A", "B"), ("B", "B"), ("B", "A")]
        estimated = estimate_transition_matrix(["A", "B"], transitions, laplace=1.0)
        for row in estimated.values():
            self.assertAlmostEqual(sum(row.values()), 1.0)

    def test_stationary_distribution_sums_to_one(self):
        dist = stationary_distribution(self.matrix)
        self.assertAlmostEqual(sum(dist.values()), 1.0)


if __name__ == "__main__":
    unittest.main()
