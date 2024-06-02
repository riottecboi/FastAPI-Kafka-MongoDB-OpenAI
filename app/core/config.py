from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: str
    KAFKA_TOPIC: str
    MONGODB_URI: str
    MONGODB_DATABASE: str

    class Config:
        env_file = ".env"

settings = Settings()