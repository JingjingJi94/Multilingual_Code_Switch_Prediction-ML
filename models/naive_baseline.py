from collections import defaultdict
from sklearn.metrics import f1_score, precision_score, recall_score


class NaiveSwitchPredictor:
    """
    Frequency-based statistical baseline.
    Predicts next-token language switch using only the current token's language ID.
    P(switch | LID) is estimated from training set counts.
    """

    def __init__(self, threshold=0.5):
        self.threshold = threshold
        self.prob_table = {}  # {lang_id: P(switch | lang_id)}

    def fit(self, language_ids, ysw_labels):
        """
        Build probability lookup table from training data.
        language_ids: List of current token language IDs
        ysw_labels:   List of switch labels (0 or 1)
        """
        counts = defaultdict(lambda: {"switch": 0, "total": 0})
        for lid, ysw in zip(language_ids, ysw_labels):
            counts[lid]["total"] += 1
            counts[lid]["switch"] += int(ysw)

        self.prob_table = {
            lid: c["switch"] / c["total"]
            for lid, c in counts.items()
        }
        print("Probability lookup table:", self.prob_table)

    def predict(self, language_ids):
        return [
            1 if self.prob_table.get(lid, 0) >= self.threshold else 0
            for lid in language_ids
        ]

    def evaluate(self, language_ids, ysw_true):
        ysw_pred = self.predict(language_ids)
        return {
            "anticipatory_f1": f1_score(ysw_true, ysw_pred, pos_label=1, zero_division=0),
            "precision":       precision_score(ysw_true, ysw_pred, pos_label=1, zero_division=0),
            "recall":          recall_score(ysw_true, ysw_pred, pos_label=1, zero_division=0)
        }


class ZeroBaseline:
    """
    Lower-bound baseline: always predicts no switch.
    Used to establish the minimum performance floor.
    """

    def predict(self, language_ids):
        return [0] * len(language_ids)

    def evaluate(self, language_ids, ysw_true):
        ysw_pred = self.predict(language_ids)
        return {
            "anticipatory_f1": f1_score(ysw_true, ysw_pred, pos_label=1, zero_division=0),
            "precision":       precision_score(ysw_true, ysw_pred, pos_label=1, zero_division=0),
            "recall":          recall_score(ysw_true, ysw_pred, pos_label=1, zero_division=0)
        }