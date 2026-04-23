# ML CI/CD Pipeline

A workshop-friendly, production-like template that demonstrates continuous integration for a machine learning workflow using GitHub Actions.

## Problem Statement

Machine learning systems are not just model code. They involve training, evaluation, testing, and serving artifacts reliably over time.  
Without CI/CD, teams can accidentally ship broken training scripts, low-performing models, or APIs that fail in production.

This project shows how to enforce quality gates in a simple ML pipeline so code and model changes are validated automatically.

## Project Overview

The pipeline performs the following steps:

1. Trains a `RandomForestClassifier` on the Iris dataset.
2. Saves the trained model to `models/model.pkl`.
3. Evaluates model accuracy.
4. Fails the pipeline if accuracy drops below `0.8`.
5. Runs automated tests with `pytest`.
6. Exposes the model through a FastAPI `/predict` endpoint for deployment-style usage.

## Project Structure

```text
ml-ci-cd-pipeline/
│
├── .github/
│   └── workflows/
│       └── ml_pipeline.yml
│
├── src/
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   └── utils.py
│
├── models/
│   └── .gitkeep
│
├── data/
│   └── .gitkeep
│
├── tests/
│   └── test_model.py
│
├── app/
│   └── main.py
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions

### 1) Clone repository

```bash
git clone <your-repo-url>
cd ml-ci-cd-pipeline
```

### 2) Create and activate virtual environment

```bash
python -m venv .venv
```

Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run training

```bash
python src/train.py
```

### 5) Run evaluation

```bash
python src/evaluate.py
```

### 6) Run the API

```bash
uvicorn app.main:app --reload
```

Open interactive docs at: `http://127.0.0.1:8000/docs`

## Running CI/CD

The GitHub Actions workflow is defined in `.github/workflows/ml_pipeline.yml`.

It triggers on every push to `main` and executes:

1. Dependency installation
2. Model training (`python src/train.py`)
3. Model evaluation (`python src/evaluate.py`)
4. Tests (`pytest`)

If evaluation accuracy is below `0.8`, the workflow fails automatically.

## API Usage

### Endpoint

`POST /predict`

### Example request

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d "{\"features\": [5.1, 3.5, 1.4, 0.2]}"
```

### Example response

```json
{"prediction": 0}
```

## Future Improvements

- Add experiment tracking with MLflow
- Add data and model versioning with DVC
- Add cloud deployment (for example, AWS/GCP/Azure with managed CI/CD)
