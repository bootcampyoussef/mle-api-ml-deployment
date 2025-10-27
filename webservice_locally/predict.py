import mlflow
#from google.cloud import storage
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
