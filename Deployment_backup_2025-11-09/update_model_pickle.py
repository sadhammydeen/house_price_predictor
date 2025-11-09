"""Utility to re-serialize the regression model with the currently installed scikit-learn version.

Run once whenever the environment upgrades scikit-learn to avoid InconsistentVersionWarning during app startup.
"""

from __future__ import annotations

import pickle
import warnings
from pathlib import Path

from sklearn import __version__ as sklearn_version  # noqa: F401
from sklearn.exceptions import InconsistentVersionWarning

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "regression_model.pkl"

if not MODEL_PATH.exists():
    raise SystemExit(f"Model file not found: {MODEL_PATH}")

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=InconsistentVersionWarning)
    with MODEL_PATH.open("rb") as model_file:
        pipeline = pickle.load(model_file)

with MODEL_PATH.open("wb") as model_file:
    pickle.dump(pipeline, model_file)

print(f"Model re-serialized with scikit-learn {sklearn_version}")
