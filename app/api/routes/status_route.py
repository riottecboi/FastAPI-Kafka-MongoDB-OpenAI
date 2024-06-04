from fastapi import APIRouter, HTTPException
from app.db.mongodb import get_recommendations
from app.schemas.schema import RecommendationResponse, RecommendationCheckResponse, ErrorResponse

router = APIRouter()

@router.get("/status/{uid}", response_model=RecommendationResponse)
async def get_status(uid: str):
    country, season, recommendations = await get_recommendations(uid)
    if recommendations is None:
        raise HTTPException(status_code=404, detail=ErrorResponse(error="UID not found", message="The provided UID does not exist. Please check the UID and try again.").dict())

    if recommendations:
        return RecommendationResponse(uid=uid, country=country, season=season, message="The recommendations are ready", recommendations=recommendations, status="completed")
    return RecommendationCheckResponse(uid=uid, status="pending", message="The recommendations are not yet available. Please try again later.")