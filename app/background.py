import asyncio
from app.utils.kafka import kafka_consumer
from app.db.mongodb import save_recommendations
from app.api.openai_api import get_openai_recommendation

async def handle_request(uid, request_data):
    try:
        recommendations = await get_openai_recommendation(request_data)
    except Exception as e:
        recommendations = []
    result = await save_recommendations(uid, request_data, recommendations)
    print(f"Recommendations saved with ID: {result}")

async def main():
    while True:
        uid, request_data = await kafka_consumer()
        await handle_request(uid, request_data)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())