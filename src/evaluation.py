import numpy as np
from sklearn.metrics import average_precision_score, roc_auc_score, precision_recall_curve


def prob_to_metrics(y_true, y_prob):
    """
    TODO:
    - compute PR-AUC (average_precision_score)
    - compute ROC-AUC
    - choose threshold maximizing recall under a min precision (e.g., 0.2) OR F2 score
    - return dict with threshold, pr_auc, roc_auc, precision_at_t, recall_at_t
    - Note: threshold picking is for business-readability only; Kaggle submission uses probabilities
    """
    raise NotImplementedError


