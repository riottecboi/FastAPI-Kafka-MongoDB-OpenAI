from fastapi import APIRouter, HTTPException, Query
from pydantic_core._pydantic_core import ValidationError

from app.schemas.schema import RecommendationsSchema

router = APIRouter()

@router.get("/recommendations")
async def get_recommendations(
        country: str = Query(..., description="The country for which recommendations are to be fetched."),
        season: str = Query(..., description="The season in which the recommendations are desired.")
):
    try:
        RecommendationsSchema(country=country, season=season)
        recommendations = ["Visit the Eiffel Tower", "Explore the Louvre Museum",
                           "Enjoy a boat tour along the Seine River"]
        return {"recommendations": recommendations}
    except ValidationError as e:
        err_str = "Invalid country or season"
        raise HTTPException(status_code=422, detail=f"Unprocessable Entity - {err_str}")
