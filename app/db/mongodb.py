import asyncio
import pymongo
from app.core.config import settings

loop = asyncio.get_event_loop()
client = pymongo.MongoClient(settings.MONGODB_URI)
db = client[settings.MONGODB_DATABASE]
recommendations_collection = db["recommendations"]

async def save_recommendations(uid, recommendations):
    recommendation_doc = {
        "uid": uid,
        "recommendations": recommendations
    }
    result = await loop.run_in_executor(None, recommendations_collection.insert_one, recommendation_doc)
    return result.inserted_id

async def get_recommendations(uid):
    recommendation_doc = await recommendations_collection.find_one({"uid": uid})
    if recommendation_doc:
        return recommendation_doc["recommendations"]
    return None