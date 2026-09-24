# Run the API in Docker

After the notebook and local FastAPI app work, you can package the API in Docker. This keeps the learning path practical: get the local flow working first, then move to a container.

This step uses the repository's [Dockerfile](Dockerfile) to package the FastAPI service.

## Build the image

From the repository root, run:

```bash
docker build -t ml-api-local .
```

Expected result:

- Docker finishes the build without errors.
- The local image `ml-api-local` appears in `docker images`.

## Run the container

If you are currently running the local FastAPI app from step `02`, **stop it** first so Docker can bind to port `9696`.

The container still needs access to the MLflow server and model artifacts that are running on your machine. MLflow stores these artifacts under an absolute path in `mlartifacts/`. The volume mount below makes that path visible inside the container so `models:/lr-ride-duration@production` can load correctly.

```bash
docker run --rm -p 9696:9696 \
  --add-host=host.docker.internal:host-gateway \
  --env-file .env \
  -e MLFLOW_TRACKING_URI=http://host.docker.internal:5000 \
  -v "$PWD/mlartifacts:$PWD/mlartifacts" \
  ml-api-local
```

`--add-host` maps `host.docker.internal` to your machine so the container can reach the MLflow server. Docker Desktop already defines this name, and the flag makes the same command work on Linux too.

> **Note on Windows:** Docker path handling can vary on Windows because MLflow records local artifact paths. If you completed steps `01` and `02` on Windows and the Docker run or the API call fail, adapt the volume mount so the `mlartifacts` path recorded by MLflow is visible inside the container. If this is unfamiliar, keep using the local Python workflow from step `02` and treat Docker as optional.

## Test the containerized API

```bash
curl -X POST http://127.0.0.1:9696/predict \
  -H "Content-Type: application/json" \
  -d '{
    "ride_id": "docker-001",
    "PULocationID": 161,
    "DOLocationID": 236,
    "trip_distance": 4.2
  }'
```

If this request fails, first confirm that:

- the MLflow server from step `01` is still running on your host machine,
- `.env` exists in the repository root,
- `mlartifacts/` exists because the notebook registered a model,
- port `9696` is not already in use by a local `uvicorn` process.

## What this step shows

- How to package the FastAPI service in a reproducible runtime.
- How local containers connect back to host services.
- Why it helps to validate the local Python workflow before introducing Docker.
