import pandas as pd
import numpy as np


def basic_clean(df, cfg):
    """
    TODO:
    - trim/rename columns
    - handle missing: median/most-freq (document choice)
    - remove/clip extreme outliers if needed
    - drop any leaky columns from cfg
    """
    raise NotImplementedError


def split_train_test(df, y, cfg):
    """
    TODO:
    - if cfg['test_split']['kind']=="time": split by datetime cutoff
    - else: stratified train/test by target
    """
    raise NotImplementedError

