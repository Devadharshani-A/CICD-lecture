"""Utility helpers for dataset loading and path management."""

from pathlib import Path
from typing import Tuple

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "model.pkl"


def get_data_splits(test_size: float = 0.2, random_state: int = 42) -> Tuple:
    """Load iris dataset and return train/test splits."""
    dataset = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        dataset.data,
        dataset.target,
        test_size=test_size,
        random_state=random_state,
        stratify=dataset.target,
    )
    return X_train, X_test, y_train, y_test
