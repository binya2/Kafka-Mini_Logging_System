from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # --- DATABASE SETTINGS ---
    MONGODB_URL: str = Field(default="mongodb://localhost:27017", validation_alias="mongodb_url")
    DATABASE_NAME: str = Field(default="test_db", validation_alias="database_name")
    COLLECTION: str = Field(default="users", validation_alias="collection_name")
    KAFKA_TOPIC: str = Field(default="users", validation_alias="kafka_topic")


settings = Settings()


class KafkaConsumerConfig(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: str = Field(default="localhost:9092", serialization_alias="bootstrap.servers")
    KAFKA_GROUP_ID: str = Field(default="consumer-group", serialization_alias="group.id")
    KAFKA_AUTO_OFFSET_RESET: str = Field(default="earliest", serialization_alias="auto.offset.reset")


kafka_consumer_config = KafkaConsumerConfig()
