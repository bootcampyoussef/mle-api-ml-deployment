# Deploy a Local ML Model API with FastAPI, MLflow, and Docker

This repository teaches a local-first deployment workflow for a machine-learning model. You will create and register a small demo taxi-duration model in MLflow, serve it through a FastAPI application, test the API locally, and optionally package it in Docker once the core flow works.

## Learning Path

1. Create a Python `3.11.3` environment and copy the local configuration file.
2. Start a local MLflow tracking server with a SQLite backend and local artifact storage.
3. Open [src/register_mlflow_model.ipynb](src/register_mlflow_model.ipynb) in a Jupyter-capable editor and run the notebook to log and register a demo model.
4. Run the FastAPI application in [webservice_locally](webservice_locally) and send a prediction request.
5. Run the test suite and explore one meaningful extension.
6. Optionally build and run the API in Docker against the same local MLflow server.

- Local MLflow setup: [01-run-local-mlflow.md](01-run-local-mlflow.md)
- Local API setup: [02-run-the-api-locally.md](02-run-the-api-locally.md)
- Optional Docker workflow: [03-run-with-docker.md](03-run-with-docker.md)
- Tests and next steps: [04-test-and-extend-the-api.md](04-test-and-extend-the-api.md)
- Short review quiz: [Quiz.md](Quiz.md)

## Local Data Services

This repo uses one local service:

- `MLflow tracking server` on `http://127.0.0.1:5000`
  It stores experiment metadata in `mlflow.db` and model artifacts in `mlartifacts/`.

The FastAPI app runs locally on `http://127.0.0.1:9696` and loads the registered model from the MLflow Model Registry using the `production` alias.

```mermaid
flowchart LR
    A["Jupyter notebook"] --> B["Local MLflow server"]
    B --> C["Registered model: lr-ride-duration@production"]
    D["FastAPI /predict"] --> C
    E["Client request"] --> D
    D --> F["Predicted ride duration"]
    G["pytest"] --> D
```

## Mermaid Diagrams

GitHub renders Mermaid diagrams automatically. If your local markdown previewer does not render Mermaid, view this README on GitHub or use any Mermaid-capable previewer.

## Environment

- Python `3.11.3`
- A Jupyter-capable editor for the notebook
- Docker Desktop for the optional container step

## Setup

Start from the repository root.

### `macOS` / Linux

```bash
pyenv local 3.11.3  # optional, only if you use pyenv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
```

### `Windows`

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

If `python3 -m venv .venv` fails with an `ensurepip` or missing `encodings` error, the Python installation itself is not creating virtual environments correctly. Install a standard Python `3.11.3` build, for example with `pyenv` or from python.org, then rerun the setup commands above.

### Quick Sanity Checks

After setup:

- open `.env` and confirm the values still point to `http://127.0.0.1:5000`
- keep all commands in this repo rooted from the project directory unless a step explicitly tells you to `cd`

## Notebook Workflow

1. Open this repository in your Jupyter-capable editor.
2. Open [src/register_mlflow_model.ipynb](src/register_mlflow_model.ipynb).
3. Select the `.venv` interpreter as the notebook kernel.
4. Keep the MLflow server running while you execute the notebook.

## Run the Local Workflow

The workflow has three moving parts. Keep each long-running service in its own terminal so it is easy to see logs and stop the process later with `Ctrl+C`.

```mermaid
sequenceDiagram
    participant Learner
    participant MLflow as "MLflow server :5000"
    participant Notebook as "Registration notebook"
    participant API as "FastAPI app :9696"
    Learner->>MLflow: Start local tracking server
    Learner->>Notebook: Run all cells
    Notebook->>MLflow: Log run, artifacts, and model alias
    Learner->>API: Start uvicorn
    API->>MLflow: Load lr-ride-duration@production
    Learner->>API: Send /predict or /predict_batch request
```

### 1. Start MLflow

```bash
source .venv/bin/activate
mlflow server \
  --host 127.0.0.1 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlartifacts
```

Expected result:

- the MLflow UI is available at `http://127.0.0.1:5000`
- a new `mlflow.db` file appears in the repo root
- a new `mlartifacts/` folder appears after you log a model

### 2. Register the demo model

Run all cells in [src/register_mlflow_model.ipynb](src/register_mlflow_model.ipynb). The notebook will:

- create a small demo taxi-duration training dataset
- log a scikit-learn model to the local MLflow server
- register that model as `lr-ride-duration`
- assign the `production` alias

Expected result:

- the MLflow UI shows an experiment called `local-taxi-duration-demo`
- the `Models` page shows `lr-ride-duration`
- the latest version has the alias `production`

### 3. Start the API

```bash
source .venv/bin/activate
cd webservice_locally
uvicorn app:app --reload --port 9696
```

Expected result:

- the server prints `Uvicorn running on http://127.0.0.1:9696`
- `http://127.0.0.1:9696/docs` opens the interactive API docs

### 4. Send a prediction request

```bash
curl -X POST http://127.0.0.1:9696/predict \
  -H "Content-Type: application/json" \
  -d '{
    "ride_id": "demo-001",
    "PULocationID": 161,
    "DOLocationID": 236,
    "trip_distance": 3.5
  }'
```

Expected result:

- the response echoes the ride fields
- the response includes `predicted_duration`

You can also score multiple rides with `POST /predict_batch`; see [02-run-the-api-locally.md](02-run-the-api-locally.md) for the batch request example.

### 5. Run the tests

```bash
source .venv/bin/activate
pytest
```

Expected result:

- the root route test passes
- the prediction route test passes with a mocked model response
- the batch prediction route test passes with mocked model responses
- the empty batch route test passes without loading a model

## End-To-End Checklist

Use this checklist when you want to confirm the repo is healthy from a clean local state:

| Check | Command or page | Healthy result |
| --- | --- | --- |
| Local config | `.env` | points to `http://127.0.0.1:5000` |
| MLflow UI | `http://127.0.0.1:5000` | opens and shows the local tracking server |
| Model registry | MLflow `Models` page | `lr-ride-duration` has the `production` alias |
| API docs | `http://127.0.0.1:9696/docs` | shows `/predict` and `/predict_batch` |
| Tests | `pytest` | ends with `4 passed` |

## Learning Objectives

By the end of this repo, you should be able to:

- explain how MLflow tracking and the Model Registry support local deployment workflows
- run a FastAPI application that serves predictions from a registered model
- structure request and response payloads with Pydantic
- write small smoke tests for an API route before making larger changes
- move from a local development workflow to an optional Docker-based runtime
