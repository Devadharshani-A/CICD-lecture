"""Evaluate persisted model performance."""

import joblib
from sklearn.metrics import accuracy_score

from utils import MODEL_PATH, get_data_splits


def evaluate_model(min_accuracy: float = 0.8) -> float:
    """Evaluate model and raise an error when it underperforms."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found at {MODEL_PATH}. Run train.py first."
        )

    _, X_test, _, y_test = get_data_splits()
    model = joblib.load(MODEL_PATH)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model accuracy: {accuracy:.4f}")

    if accuracy < min_accuracy:
        raise Exception(
            f"Accuracy {accuracy:.4f} is below threshold {min_accuracy:.2f}."
        )

    return accuracy


if __name__ == "__main__":
    evaluate_model()
