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


class RecommendationSubmitResponse(BaseModel):
    uid: str

class RecommendationCheckResponse(RecommendationSubmitResponse):
    message: Optional[str] = None
    status: str

class RecommendationResponse(RecommendationCheckResponse):
    country: Optional[str] = None
    season: Optional[Literal["spring", "summer", "autumn", "winter"]] = None
    recommendations: Optional[List[str]] = None

class ErrorResponse(BaseModel):
    error: str
    message: str