"""Pydantic models for the local prediction API request and response bodies."""

from pydantic import BaseModel


class TaxiRide(BaseModel):
    """Fields the API needs to describe one taxi ride."""

    ride_id: str
    PULocationID: int
    DOLocationID: int
    trip_distance: float


class TaxiRidePrediction(TaxiRide):
    """Original ride payload plus the model's predicted duration."""

    predicted_duration: float
