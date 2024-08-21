from kafka import KafkaConsumer
import json

consumer=KafkaConsumer(
            "topic1",
            bootstrap_servers=["localhost:9092"],
            value_deserializer=lambda x:json.loads(x.decode("utf8")),
            consumer_timeout_ms=5000
        )

print("get consumer start")

for msg in consumer:
    print(msg)
    print(msg.value)

print("get consumer end")
