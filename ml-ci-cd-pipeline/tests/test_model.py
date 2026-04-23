"""Basic tests for trained model artifact."""

from pathlib import Path
import sys

import joblib
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

from train import train_model  # noqa: E402
from utils import MODEL_PATH  # noqa: E402


def test_model_loads_and_predicts():
    """Ensure saved model can be loaded and produce one prediction."""
    if not MODEL_PATH.exists():
        train_model()

    model = joblib.load(MODEL_PATH)
    sample = np.array([[5.1, 3.5, 1.4, 0.2]])
    prediction = model.predict(sample)

    assert len(prediction) == 1
