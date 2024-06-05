from fastapi import APIRouter, HTTPException, Query
from pydantic_core._pydantic_core import ValidationError
from utils.kafka import kafka_producer
from schemas.schema import RecommendationsRequest, RecommendationSubmitResponse, ErrorResponse
import uuid
router = APIRouter()

@router.post("/recommendations")
async def get_recommendations(
        country: str = Query(..., description="The country for which recommendations are to be fetched."),
        season: str = Query(..., description="The season in which the recommendations are desired.")
):
    try:
        RecommendationsRequest(country=country, season=season)
        uid = str(uuid.uuid4())
        request_data = {'country': country, 'season': season}
        await kafka_producer(request_data, uid)
        return RecommendationSubmitResponse(uid=uid, status="pending")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=ErrorResponse(error="Invalid country/season", message="The input of country or season is invalid. Please try again.").dict())