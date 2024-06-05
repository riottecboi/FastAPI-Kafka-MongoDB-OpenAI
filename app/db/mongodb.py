import asyncio
import pymongo
from core.config import settings

loop = asyncio.get_event_loop()
client = pymongo.MongoClient(settings.MONGODB_URI)
db = client[settings.MONGODB_DATABASE]
recommendations_collection = db[settings.MONGODB_DATABASE]

async def save_recommendations(uid, request_data, recommendations):
    recommendation_doc = {
        "uid": uid,
        "request_data": request_data,
        "recommendations": recommendations
    }
    result = await loop.run_in_executor(None, recommendations_collection.insert_one, recommendation_doc)
    return result.inserted_id

async def get_recommendations(uid):
    recommendation_doc = await loop.run_in_executor(None, recommendations_collection.find_one, {'uid': uid})
    if recommendation_doc:
        return recommendation_doc["request_data"]["country"], recommendation_doc["request_data"]["season"], recommendation_doc["recommendations"]
    return None