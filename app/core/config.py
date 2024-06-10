from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_TOPIC: str = "recommendations_topic"
    MONGODB_URI: str = "mongodb://xxx:xxx@localhost:27017/"
    MONGODB_DATABASE: str = "recommendations"
    OPENAI_KEY: str = "xxx"

    class Config:
        env_file = 'settings.cfg'

settings = Settings()