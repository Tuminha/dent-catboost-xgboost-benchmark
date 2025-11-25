import pandas as pd
import yaml
from pathlib import Path


def load_cfg():
    return yaml.safe_load(Path("config/dataset.yaml").read_text())


def load_dataset():
    """
    TODO:
    - read csv
    - drop id columns if present
    - cast categoricals to 'category'
    """
    raise NotImplementedError


def load_train_test(cfg):
    """
    TODO:
    - read cfg['file'] and cfg['test_file'] with pandas
    - drop columns in cfg['id_columns'] from X (keep separately for submission)
    - cast columns in cfg['categoricals'] to 'category'
    - return (X_train_full, y, X_test_full, test_ids)
    """
    raise NotImplementedError


def get_sample_submission(cfg):
    """
    TODO: read cfg['sample_submission'] and return df
    """
    raise NotImplementedError


