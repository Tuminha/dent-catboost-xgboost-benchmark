from catboost import CatBoostClassifier, Pool
from xgboost import XGBClassifier


def build_catboost(cat_idx, cfg):
    """
    TODO: return CatBoostClassifier with sensible defaults:
    - loss_function='Logloss', eval_metric='AUC:PR'
    - iterations ~ 1500-3000, depth 6-8, learning_rate 0.03-0.06
    - l2_leaf_reg ~ 6-10, random_state=42, early_stopping_rounds=100
    - class_weights or scale_pos_weight from cfg
    - Pass cat_features indices and verbose=False; use eval_metric='AUC:PR'
    """
    raise NotImplementedError


def build_xgboost(cfg):
    """
    TODO: return XGBClassifier baseline for comparison:
    - n_estimators ~ 1000, max_depth 6-8, learning_rate 0.05
    - subsample/colsample_bytree 0.8, reg_lambda 1.0
    - eval_metric 'aucpr'
    - Ensure encoder is fit on train only; use eval_metric='aucpr'
    """
    raise NotImplementedError


