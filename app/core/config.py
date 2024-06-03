from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_TOPIC: str = "recommendations_topic"
    MONGODB_URI: str = "mongodb://username:password@localhost:27017/recommendations"
    MONGODB_DATABASE: str = "recommendations"

    class Config:
        env_file = 'settings.cfg'

settings = Settings()