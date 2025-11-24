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

