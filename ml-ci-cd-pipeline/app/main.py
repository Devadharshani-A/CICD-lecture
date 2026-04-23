"""FastAPI application exposing model inference endpoint."""

from pathlib import Path
import sys

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

from utils import MODEL_PATH  # noqa: E402

app = FastAPI(title="ML CI/CD Pipeline API", version="1.0.0")


class PredictionRequest(BaseModel):
    features: conlist(float, min_length=4, max_length=4)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(payload: PredictionRequest):
    """Run model inference for one iris sample."""
    if not MODEL_PATH.exists():
        raise HTTPException(status_code=500, detail="Model not found. Train first.")

    model = joblib.load(MODEL_PATH)
    prediction = model.predict([payload.features])[0]
    return {"prediction": int(prediction)}
