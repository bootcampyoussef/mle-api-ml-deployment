"""Pydantic models for the local prediction API request and response bodies."""

from pydantic import BaseModel, Field


class TaxiRide(BaseModel):
    """Fields the API needs to describe one taxi ride.

    Pydantic uses these definitions for request validation and FastAPI reuses
    them to generate the interactive schema shown at `/docs`.
    """

    ride_id: str = Field(
        min_length=1,
        description="Client-provided identifier that lets you match the response to the request.",
        examples=["ride-101"],
    )
    PULocationID: int = Field(
        gt=0,
        description="NYC taxi pickup zone identifier used to build the route feature.",
        examples=[161],
    )
    DOLocationID: int = Field(
        gt=0,
        description="NYC taxi dropoff zone identifier used to build the route feature.",
        examples=[236],
    )
    trip_distance: float = Field(
        gt=0,
        description="Trip distance in miles. The demo model treats this as a numeric feature.",
        examples=[3.5],
    )


class TaxiRidePrediction(TaxiRide):
    """Original ride payload plus the model's predicted duration."""

    predicted_duration: float = Field(
        description="Predicted ride duration in minutes.",
        examples=[12.4],
    )
