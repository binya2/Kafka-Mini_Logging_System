from congif import settings


def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode('utf-8')}")
        print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")


def send_user(producer, user_data):
    producer.produce(
        topic=settings.KAFKA_TOPIC,
        value=user_data,
        callback=delivery_report
    )
    producer.flush()
    print("Message sent to Kafka")
