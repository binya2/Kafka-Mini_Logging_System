from pydantic import Field
from pydantic_settings import BaseSettings


class MongodbConfig(BaseSettings):
    # --- DATABASE SETTINGS ---
    MONGODB_URL: str = Field(default="mongodb://localhost:27017", validation_alias="mongodb_url")
    DATABASE_NAME: str = Field(default="kafka_db", validation_alias="database_name")
    COLLECTION: str = Field(default="users", validation_alias="collection_name")


mongodb_config = MongodbConfig()


class MySqlConfig(BaseSettings):
    MYSQL_HOST: str = Field(default="localhost", validation_alias="mysql_host")
    MYSQL_PORT: int = Field(default=3306, validation_alias="mysql_port")
    MYSQL_USER: str = Field(default="root", validation_alias="mysql_user")
    MYSQL_PASSWORD: str = Field(default="password", validation_alias="mysql_password")
    MYSQL_DATABASE: str = Field(default="kafka_db", validation_alias="mysql_database")




mysql_config = MySqlConfig()