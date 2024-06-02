from confluent_kafka import Producer, Consumer
from app.core.config import settings

def kafka_producer():
    producer = Producer({
        'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS
    })
    return producer

def send_recommendation_request(producer, request_data, uid):
    producer.produce(
        settings.KAFKA_TOPIC,
        value=f"{uid}:{request_data}".encode("utf-8"),
    )
    producer.flush()

def kafka_consumer():
    consumer = Consumer({
        'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS,
        'group.id': settings.KAFKA_TOPIC,
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe([settings.KAFKA_TOPIC])
    return consumer

def process_recommendation_request(consumer):
    msg = consumer.poll(1.0)
    if msg is None:
        return None
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        return None

    uid, request_data = msg.value().decode("utf-8").split(":", 1)

    print(f"Processed recommendation request: {request_data}")
    consumer.commit(asynchronous=True)
    return uid