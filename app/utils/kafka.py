from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from app.core.config import settings

async def kafka_producer(request_data, uid):
    producer = AIOKafkaProducer(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS
    )
    await producer.start()
    await producer.send(
        settings.KAFKA_TOPIC,
        f"{uid}:{request_data}".encode("utf-8"), partition=0
    )
    await producer.stop()

async def kafka_consumer():
    consumer = AIOKafkaConsumer(
        settings.KAFKA_TOPIC,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        group_id=settings.KAFKA_TOPIC,
        auto_offset_reset='earliest'
    )
    await consumer.start()
    try:
        async for msg in consumer:
            uid, request_data = msg.value.decode("utf-8").split(":", 1)
            print(f"Processed recommendation request: {request_data}")
            await consumer.commit()
            return uid, eval(request_data)
    except Exception as e:
        print(f"Consumer error: {e}")
    finally:
        await consumer.stop()