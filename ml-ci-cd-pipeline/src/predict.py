"""Prediction utility for local inference checks."""

import joblib

from utils import MODEL_PATH


def predict_sample(sample):
    """Load model and return predictions for input sample."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found at {MODEL_PATH}. Run train.py first."
        )
    model = joblib.load(MODEL_PATH)
    return model.predict(sample)


if __name__ == "__main__":
    # Sample input from iris feature space
    input_sample = [[5.1, 3.5, 1.4, 0.2]]
    prediction = predict_sample(input_sample)
    print(f"Prediction: {prediction.tolist()}")
