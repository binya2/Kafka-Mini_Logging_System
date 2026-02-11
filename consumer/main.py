import json

from confluent_kafka import Consumer
from pymongo import MongoClient

from congif import settings, kafka_consumer_config

consumer_config = kafka_consumer_config.model_dump(by_alias=True)
consumer = Consumer(consumer_config)

mongo_client = MongoClient(settings.MONGODB_URL)
db = mongo_client[settings.DATABASE_NAME]
collection = db[settings.COLLECTION]


def consumer_run():
    consumer.subscribe([settings.KAFKA_TOPIC])
    print(f"🟢 Consumer is running and subscribed to {settings.KAFKA_TOPIC} topic")
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print("❌ Error:", msg.error())
                continue
            value = msg.value().decode("utf-8")
            user = json.loads(value)
            existing_user = collection.find_one({"email": user['email']})
            if existing_user:
                print(f"⚠️ User with email {user['email']} already exists. Skipping insertion.")
                continue
            collection.insert_one(user)
    except KeyboardInterrupt:
        print("\n🔴 Stopping consumer")

    finally:
        consumer.close()


if __name__ == "__main__":
    consumer_run()
