import asyncio
from app.utils.kafka import kafka_consumer
from app.db.mongodb import save_recommendations

async def main():
    uid, request_data = await kafka_consumer()

    recommendations = ["Recommendation 1", "Recommendation 2", "Recommendation 3"]

    result = await save_recommendations(uid, request_data, recommendations)
    print(f"Recommendations saved with ID: {result}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())