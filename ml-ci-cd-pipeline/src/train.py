"""Train and persist the ML model."""

from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier

from utils import MODEL_PATH, get_data_splits


def train_model() -> Path:
    """Train a RandomForest model and save it to disk."""
    X_train, _, y_train, _ = get_data_splits()
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to: {MODEL_PATH}")
    return MODEL_PATH


if __name__ == "__main__":
    train_model()
