# ML CI/CD Hands-On Workshop Script

This guide is a ready-to-speak facilitator script for a live session.  
It includes:
- what you should say,
- what you should run,
- what students should do,
- what outcome to expect at each step.

---

## 1) Workshop Opening (2-3 minutes)

### Facilitator says

"Today we are building and validating a small ML system end-to-end, not just training a model.  
In real projects, we need reliability: if model quality drops or code breaks, CI should block delivery."

"By the end of this workshop, you will:
1. Train and evaluate a model locally.
2. Run automated tests.
3. Serve predictions via FastAPI.
4. Push to GitHub and see GitHub Actions run the same checks automatically."

### Students do

- Open terminal in the project root: `ml-ci-cd-pipeline`
- Confirm Python is available:

```powershell
python --version
```

### Expected outcome

- Python version prints successfully.

---

## 2) Environment Setup (5 minutes)

### Facilitator says

"First, every student creates an isolated Python environment.  
This keeps dependencies clean and reproducible."

### Everyone runs (Windows PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Students do

- If activation fails due to policy, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

- Then activate `.venv` again.

### Expected outcome

- Dependencies install successfully.
- Prompt shows `(.venv)` at the start.

---

## 3) Train and Evaluate Model (8 minutes)

### Facilitator says

"Now we run the ML part of the pipeline manually.  
Training builds an artifact (`models/model.pkl`). Evaluation checks model quality."

"Important concept: quality gates.  
In this project, the pipeline fails if accuracy goes below 0.8.  
This prevents silently shipping degraded models."

### Everyone runs

```powershell
python src/train.py
python src/evaluate.py
```

### Students do

- Confirm that `models/model.pkl` is created.
- Note the printed accuracy.

### Expected outcome

- Model file exists.
- Evaluation completes and passes threshold.

---

## 4) Run Tests (4 minutes)

### Facilitator says

"ML systems still need software tests.  
We validate behavior with `pytest` before deployment."

### Everyone runs

```powershell
pytest
```

### Students do

- Observe number of passed tests.
- If tests fail, pair with neighbor and inspect error output.

### Expected outcome

- Tests pass locally.

---

## 5) Serve Model as API (8 minutes)

### Facilitator says

"Now we expose model inference through an API.  
This simulates deployment usage: clients send features, service returns prediction."

### Everyone runs

```powershell
uvicorn app.main:app --reload
```

Open: `http://127.0.0.1:8000/docs`

### Students do

1. Open Swagger UI (`/docs`).
2. Try `POST /predict` with:
   - `[5.1, 3.5, 1.4, 0.2]`
   - `[6.4, 3.2, 4.5, 1.5]`
3. Compare outputs.

Alternative terminal test:

```powershell
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"features\": [5.1, 3.5, 1.4, 0.2]}"
```

### Expected outcome

- API responds with `{"prediction": <class_id>}`.

---

## 6) Connect to GitHub and Push (10 minutes)

> If students already cloned from GitHub, they can skip setup and go directly to commit/push.

### Facilitator says

"Now we connect local work to GitHub so CI/CD can run in the cloud on every push."

### A) Create repository on GitHub

1. Go to [https://github.com/new](https://github.com/new)
2. Repository name: `ml-ci-cd-pipeline` (or any name)
3. Keep it Public or Private
4. Click **Create repository**

### B) Initialize git locally (if needed)

Run in project root:

```powershell
git init
git add .
git commit -m "Initial ML CI/CD pipeline setup"
```

### C) Connect local repo to GitHub remote

Replace placeholders:

```powershell
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git branch -M main
git push -u origin main
```

If remote already exists:

```powershell
git remote -v
```

### D) Authenticate if prompted

- GitHub CLI method (recommended):

```powershell
gh auth login
```

- Or browser-based Git credential prompt with HTTPS.

### Students do

- Create their own repo.
- Push local code.

### Expected outcome

- Code appears on GitHub repository page.

---

## 7) Show GitHub Actions CI Pipeline (8 minutes)

### Facilitator says

"This is where CI/CD delivers value.  
On each push, GitHub Actions runs training, evaluation, and tests automatically."

### Show in GitHub

1. Open repository.
2. Go to **Actions** tab.
3. Open workflow run from `.github/workflows/ml_pipeline.yml`.
4. Expand jobs and steps.

### Explain what students should observe

- Dependency installation.
- Training script execution.
- Evaluation quality gate.
- Test execution.
- Green check means pipeline passed.

### Students do

- Open their own Actions tab.
- Verify at least one successful run.

---

## 8) Failure-and-Recovery Demo (Optional but powerful) (10 minutes)

### Facilitator says

"A good CI pipeline catches problems early.  
Let us intentionally break something and watch CI fail, then fix it."

### Option A: break a test intentionally

1. Edit a test assertion to an incorrect expected value.
2. Commit and push.
3. Show failed Action.
4. Revert/fix assertion.
5. Commit and push again.
6. Show pipeline green.

### Students do

- Repeat same fail/fix cycle in their own repo.

### Expected outcome

- Students directly experience quality gate behavior.

---

## 9) Teaching Notes (talking points you can reuse)

- CI is not only for web apps; it is essential for ML reliability.
- ML artifact creation (`model.pkl`) is part of deliverable pipeline.
- Model quality thresholds are deployment safeguards.
- FastAPI layer demonstrates model-as-a-service thinking.
- Automation reduces manual error and increases team confidence.

---

## 10) Student Hands-On Checklist

Ask students to confirm each item:

- [ ] Created and activated virtual environment
- [ ] Installed dependencies
- [ ] Trained model successfully
- [ ] Evaluated model successfully
- [ ] Ran tests with `pytest`
- [ ] Started API and got prediction response
- [ ] Created GitHub repo and pushed code
- [ ] Opened GitHub Actions and saw workflow run
- [ ] Observed one failure scenario and one recovery

---

## 11) Quick Troubleshooting

- `python` not found: install Python and restart terminal.
- PowerShell activation blocked: use temporary execution policy bypass.
- `uvicorn` not found: ensure `.venv` is active and dependencies installed.
- Git push auth error: run `gh auth login` or re-authenticate HTTPS credentials.
- Actions not triggered: confirm push went to `main` and workflow file exists in `.github/workflows/`.

---

## 12) Closing Script (1 minute)

"You now have a complete ML CI/CD baseline: local workflow + automated cloud checks.  
From here, teams usually add experiment tracking, data/model versioning, and deployment automation."

"The key takeaway: treat ML systems like production software, with testable and enforceable quality gates."
