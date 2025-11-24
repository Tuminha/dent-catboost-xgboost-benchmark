# Dental Tabular ML: CatBoost vs XGBoost (PR-AUC + SHAP)

**Goal**  

Train strong tabular classifiers on a dental dataset (Kaggle or local), compare **CatBoost** vs **XGBoost**, optimize for **PR-AUC** and recall at business thresholds, and explain drivers with **SHAP**. All plots use Periospot brand colors.

**Why CatBoost?**  

Native categorical handling, robust defaults, built-in text support, and excellent SHAP speed.

**What you'll get**

- Reproducible baselines for CatBoost and XGBoost  

- Proper time/stratified CV, PR-AUC, ROC-AUC, calibration, threshold picking  

- SHAP summaries and segment-level insights  

- Brand-consistent plots and a tidy **model card**

**Data**  

Use any dental tabular dataset with a clear binary target (e.g., "untreated caries", "visit in last year"). Drop your CSV into `data/raw/` and configure `config/dataset.yaml`.

**Quick start**

1. `pip install -r requirements.txt`

2. Put CSV(s) under `data/raw/` (or run `notebooks/00_get_data_and_spec.ipynb`)

3. Edit `config/dataset.yaml` for `file`, `target`, `positive_class`, `categoricals`

4. Run notebooks 01 → 05 in order

