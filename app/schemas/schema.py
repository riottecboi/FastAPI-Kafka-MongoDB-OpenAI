from pydantic import BaseModel, Field, model_validator
from typing import  List, Literal, Optional
import pycountry

class RecommendationsRequest(BaseModel):
    country: str = Field(..., description="The country for which recommendations are to be fetched.")
    season: str = Field(..., description="The season in which the recommendations are desired.")

    @model_validator(mode='after')
    def validate_season(cls, values):
        try:
            pycountry.countries.search_fuzzy(values.country)
        except LookupError:
            raise ValueError(f"Invalid country.")
        valid_seasons = ["spring", "summer", "autumn", "winter"]
        if values.season not in valid_seasons:
            raise ValueError(f"Invalid season. Must be one of {', '.join(valid_seasons)}")

        return values

class RecommendationResponse(BaseModel):
    uid: str
    country: str
    season: str = Literal["spring", "summer", "autumn", "winter"]
    recommendations: Optional[List[str]] = None
    status: str
    message: Optional[str] = None

class ErrorResponse(BaseModel):
    error: str
    message: str