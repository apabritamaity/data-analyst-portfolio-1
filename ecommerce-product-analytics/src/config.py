# src/config.py

from pathlib import Path

# ==========================
# Project Directories
# ==========================

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

ARTIFACTS_DIR = ROOT_DIR / "artifacts"

MODEL_DIR = ARTIFACTS_DIR / "models"

REPORT_DIR = ARTIFACTS_DIR / "reports"

PREDICTION_DIR = ARTIFACTS_DIR / "predictions"

# ==========================
# File Paths
# ==========================

RAW_DATA_PATH = RAW_DATA_DIR / "Flipkart-Laptops.xlsx"

PROCESSED_DATA_PATH = (
    PROCESSED_DATA_DIR /
    "feature_engineered_flipcart_laptop_data.csv"
)

MODEL_PATH = (
    MODEL_DIR /
    "elastic_net_final_model.pkl"
)

# ==========================================
# Prediction Files
# ==========================================

X_TEST_PATH = (
    PREDICTION_DIR /
    "X_test.csv"
)

Y_TEST_PATH = (
    PREDICTION_DIR /
    "y_test.csv"
)

PREDICTION_PATH = (
    PREDICTION_DIR /
    "prediction_results.csv"
)

# ==========================================
# Reports
# ==========================================

REPORT_PATH = (
    REPORT_DIR /
    "model_evaluation.csv"
)

BEST_PARAM_PATH = (
    REPORT_DIR /
    "best_parameters.csv"
)

FEATURE_IMPORTANCE_PATH = (
    REPORT_DIR /
    "feature_importance.csv"
)