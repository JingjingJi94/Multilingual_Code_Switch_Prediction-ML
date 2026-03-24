import sys
sys.path.append(".")

import numpy as np
import pytest
from evaluation.metrics import anticipatory_f1, duration_accuracy, universality_sigma


class TestAnticipatoryF1:
    def test_perfect_predictions(self):
        true = [0, 1, 0, 1, 1]
        pred = [0, 1, 0, 1, 1]
        assert anticipatory_f1(true, pred) == pytest.approx(1.0)

    def test_all_wrong_switches(self):
        # predicts no switches when there are switches
        true = [1, 1, 1]
        pred = [0, 0, 0]
        assert anticipatory_f1(true, pred) == pytest.approx(0.0)

    def test_no_switches_in_true(self):
        # no positive class → F1 is 0 (zero_division=0)
        true = [0, 0, 0]
        pred = [0, 0, 0]
        assert anticipatory_f1(true, pred) == pytest.approx(0.0)

    def test_partial_predictions(self):
        true = [0, 1, 0, 1]
        pred = [0, 1, 0, 0]
        f1 = anticipatory_f1(true, pred)
        assert 0.0 < f1 < 1.0


class TestDurationAccuracy:
    def test_perfect_predictions(self):
        true = [0, 1, 2, -1, 0]
        pred = [0, 1, 2, 99, 0]  # position 3 is masked (-1), should be ignored
        assert duration_accuracy(true, pred) == pytest.approx(1.0)

    def test_all_masked(self):
        # all -1 → no valid positions → returns 0.0
        true = [-1, -1, -1]
        pred = [0, 1, 2]
        assert duration_accuracy(true, pred) == pytest.approx(0.0)

    def test_masks_out_minus_one(self):
        true = [-1, 1, -1, 2]
        pred = [99, 1, 99, 0]  # positions 0, 2 masked; position 3 wrong
        assert duration_accuracy(true, pred) == pytest.approx(0.5)

    def test_all_wrong(self):
        true = [0, 1, 2]
        pred = [2, 0, 1]
        assert duration_accuracy(true, pred) == pytest.approx(0.0)


class TestUniversalitySigma:
    def test_perfectly_uniform(self):
        per_pair = {"Chinese-English": 0.7, "Hindi-English": 0.7, "Spanish-English": 0.7}
        assert universality_sigma(per_pair) == pytest.approx(0.0)

    def test_varying_f1(self):
        per_pair = {"Chinese-English": 0.6, "Hindi-English": 0.8, "Spanish-English": 0.7}
        expected = float(np.std([0.6, 0.8, 0.7]))
        assert universality_sigma(per_pair) == pytest.approx(expected)

    def test_empty_dict(self):
        assert universality_sigma({}) == pytest.approx(0.0)

    def test_single_pair(self):
        assert universality_sigma({"Chinese-English": 0.75}) == pytest.approx(0.0)
