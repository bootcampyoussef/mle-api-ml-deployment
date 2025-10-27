# Create the FastAPI app

The first step is to create a new Python file called **`app.py`** in the `webservice_locally` folder with a basic **FastAPI** application:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "NYC Taxi Ride Duration Prediction"}

```

We can start this application by running the following command:

```bash
cd webservice_locally
uvicorn app:app --reload --port 9696
```

This will start the application on port 9696. You can visit http://localhost:9696/ to see the application running.

Next step is to create a **data model** for the **request body**. We will use **`Pydantic`** to create it. `Pydantic` is a Python library that provides **runtime checking** and **validation** of the data structures. It is used to validate the data sent to the API and to parse the response data received from the API.

For the request we are expecting the following fields:

- `ride_id`: Unique identifier for the ride
- `PUlocationID`: Taxi pickup location ID
- `DOlocationID`: Taxi dropoff location ID
- `trip_distance`: Distance of the ride in miles

For the response we are expecting the following fields:

- `ride_id`: Unique identifier for the ride
- `PUlocationID`: Taxi pickup location ID
- `DOlocationID`: Taxi dropoff location ID
- `trip_distance`: Distance of the ride in miles
- `predicted_duration`: Predicted duration of the ride in seconds

We can create a new file called **`data_model.py`** in the `webservice_locally` folder and add the following code to it:

```python
from pydantic import BaseModel

class TaxiRide(BaseModel):
    ride_id: str
    PUlocationID: int
    DOlocationID: int
    trip_distance: float

class TaxiRidePrediction(TaxiRide):
    predicted_duration: float
```

Next step is to create a new file called **`predict.py`** in the `webservice_locally` folder. In this file we will **load the model** from the **MLFlow server** and use it to make predictions.

We will use the **`mlflow.pyfunc.load_model`** function to load the model from the MLFlow server. And because we yesterday saw already how to load the model in two different ways, we will use a third one today. You can have a look here on the different possibilities: [https://www.mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.load_model](https://www.mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.load_model)

What we are doing first is to **register the model** in the MLFlow server and give the model a **name**, **alias** and **version**.
You can find the guide in [src/register_mlflow_model.ipynb](src/register_mlflow_model.ipynb)

In the predict.py script, we’ll load the model from the MLflow Model Registry using its **name** and **alias**.

The **MLflow tracking server URI** will be read from the `.env` file via the `MLFLOW_TRACKING_URI` environment variable.

When running the application locally, we also need to authenticate with Google Cloud to access model artifacts stored in GCS.
To do this, we define the `GOOGLE_APPLICATION_CREDENTIALS` environment variable in the .env file.
This variable specifies the path to the **Google Service Account Key JSON file**, which MLflow will use for authentication when fetching model artifacts. You can copy the `your-service-account-file.json` file, that you have used yesterday in the repo [mle-batch-and-stream-predictions](https://github.com/spiced-academy/mle-batch-and-stream-predictions),  into the `webservice_locally` folder under the folder `sa_key`.

```python

import mlflow
from google.cloud import storage
import os
from dotenv import load_dotenv

def prepare_features(ride):
    features = {}
    features['trip_route'] = f"{ride.PULocationID}_{ride.DOLocationID}"
    features['trip_distance'] = ride.trip_distance
    return features

def load_model(model_name):
    alias = "production"
    model_uri = f"models:/{model_name}@{alias}"
    model = mlflow.pyfunc.load_model(model_uri)
    return model

def predict(model_name, data):
    load_dotenv()
    MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
    gcp_creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = gcp_creds_path
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
  
    model_input = prepare_features(data)
    model = load_model(model_name)
    prediction = model.predict(model_input)
    return float(prediction[0])
```

In the `app.py` we will add a new **endpoint** called **`/predict`** and we will use the `TaxiRide` model as the **request body** and the `TaxiRidePrediction` model as the **response body**.

```python
from data_model import TaxiRide, TaxiRidePrediction
from predict import predict
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "NYC Taxi Ride Duration Prediction"}

@app.post("/predict", response_model=TaxiRidePrediction)
def predict_duration(data: TaxiRide):
    prediction = predict("lr-ride-duration", data)
    return TaxiRidePrediction(**data.model_dump(), predicted_duration=prediction)
```

### Exercise

1. Add a new endpoint called **`/predict_batch`** that accepts a list of `TaxiRide` objects and returns a list of `TaxiRidePrediction` objects.
2. Add a new endpoint called **`/predict_bq`** that accepts a list of `TaxiRide` objects and returns a list of `TaxiRidePrediction` objects and stores the predictions in **BigQuery**. Hint: pandas has a function called **`to_gbq`** that can be used to store a dataframe in BigQuery.
3. Install **`pytest`** and write **unit and integration tests** for the endpoints.
