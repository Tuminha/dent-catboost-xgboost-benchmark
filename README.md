# Dental Tabular ML: CatBoost vs XGBoost (PR-AUC + SHAP)

This repo benchmarks CatBoost vs XGBoost on the Kaggle competition **Predicting Dental Visits** (binary classification: whether a person had a dental visit in the last 12 months). We optimize for PR-AUC and ROC-AUC locally; for Kaggle, we produce a submission CSV from the best model.

**Why CatBoost?**  

Native categorical handling, robust defaults, built-in text support, and excellent SHAP speed.

**What you'll get**

- Reproducible baselines for CatBoost and XGBoost  

- Proper time/stratified CV, PR-AUC, ROC-AUC, calibration, threshold picking  

- SHAP summaries and segment-level insights  

- Brand-consistent plots and a tidy **model card**

- Kaggle submission pipeline

**How to get the data**

- Install Kaggle CLI and place `kaggle.json` in `~/.kaggle/`

- From repo root:

```bash
kaggle competitions download -c predicting-dental-visits -p data/raw
unzip -o data/raw/predicting-dental-visits.zip -d data/raw
```

- You should now have `train.csv`, `test.csv`, and `sample_submission.csv`.

**Quick start**

1. `pip install -r requirements.txt`

2. Download competition data (or run `notebooks/00_get_data_and_spec.ipynb`)

3. Edit `config/dataset.yaml` for `target`, `positive_class`, `categoricals` (open train.csv first to confirm column names)

4. Run notebooks 00 → 06 in order


