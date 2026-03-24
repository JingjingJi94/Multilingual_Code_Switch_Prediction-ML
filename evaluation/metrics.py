import numpy as np
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score


def anticipatory_f1(ysw_true, ysw_pred):
    """
    Binary F1 for anticipatory switch prediction (pos_label=1).
    Measures how well the model predicts an upcoming language switch.
    """
    return float(f1_score(ysw_true, ysw_pred, pos_label=1, zero_division=0))


def anticipatory_precision(ysw_true, ysw_pred):
    """Binary precision for switch prediction (pos_label=1)."""
    return float(precision_score(ysw_true, ysw_pred, pos_label=1, zero_division=0))


def anticipatory_recall(ysw_true, ysw_pred):
    """Binary recall for switch prediction (pos_label=1)."""
    return float(recall_score(ysw_true, ysw_pred, pos_label=1, zero_division=0))


def duration_accuracy(ydur_true, ydur_pred):
    """
    Accuracy on valid duration labels, excluding positions where ydur == -1
    (i.e. positions where no switch occurs and duration is undefined).
    """
    ydur_true = np.array(ydur_true)
    ydur_pred = np.array(ydur_pred)
    mask = ydur_true != -1
    if mask.sum() == 0:
        return 0.0
    return float(accuracy_score(ydur_true[mask], ydur_pred[mask]))


def universality_sigma(per_pair_f1: dict) -> float:
    """
    Standard deviation of anticipatory F1 across language pairs.
    Lower sigma = model performs more consistently across all pairs (more universal).

    Args:
        per_pair_f1: dict mapping language pair string -> anticipatory F1 float
                     e.g. {"Chinese-English": 0.72, "Hindi-English": 0.68, "Spanish-English": 0.71}

    Returns:
        Standard deviation (float). 0.0 means perfectly uniform across pairs.
    """
    if not per_pair_f1:
        return 0.0
    return float(np.std(list(per_pair_f1.values())))
