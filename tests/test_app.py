"""Smoke tests for the local FastAPI application."""

from fastapi.testclient import TestClient

from webservice_locally import app as app_module

client = TestClient(app_module.app)


def test_index_returns_project_message():
    """The root route should make it obvious that the API is running."""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "NYC Taxi Ride Duration Prediction"}


def test_predict_returns_payload_with_prediction(monkeypatch):
    """The predict route should echo the input payload and add one prediction field."""

    def fake_predict(data):
        return 12.34

    monkeypatch.setattr(app_module, "predict", fake_predict)

    payload = {
        "ride_id": "test-001",
        "PULocationID": 161,
        "DOLocationID": 236,
        "trip_distance": 3.5,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert response.json() == {**payload, "predicted_duration": 12.34}


def test_predict_batch_returns_one_prediction_per_payload(monkeypatch):
    """The batch route should preserve request order and add predictions."""

    def fake_predict_batch(data):
        return [10.0, 20.0]

    monkeypatch.setattr(app_module, "predict_batch", fake_predict_batch)

    payload = [
        {
            "ride_id": "batch-001",
            "PULocationID": 161,
            "DOLocationID": 236,
            "trip_distance": 3.5,
        },
        {
            "ride_id": "batch-002",
            "PULocationID": 142,
            "DOLocationID": 239,
            "trip_distance": 1.7,
        },
    ]

    response = client.post("/predict_batch", json=payload)

    assert response.status_code == 200
    assert response.json() == [
        {**payload[0], "predicted_duration": 10.0},
        {**payload[1], "predicted_duration": 20.0},
    ]


def test_predict_batch_accepts_an_empty_list(monkeypatch):
    """An empty batch should return immediately without loading the model."""

    def fail_if_called(data):
        raise AssertionError("predict_batch should not be called for an empty payload")

    monkeypatch.setattr(app_module, "predict_batch", fail_if_called)

    response = client.post("/predict_batch", json=[])

    assert response.status_code == 200
    assert response.json() == []
