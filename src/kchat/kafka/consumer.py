from kafka import KafkaConsumer
import json
from datetime import datetime

consumer=KafkaConsumer(
            "topic5",
            bootstrap_servers=["localhost:9092"],
            value_deserializer=lambda x:json.loads(x.decode("utf8")),
            consumer_timeout_ms=15000,
            auto_offset_reset="earliest",
            group_id="grp1",
            enable_auto_commit=True
        )

print("get consumer start")

for msg in consumer:
    print(msg)
    # ConsumerRecord(topic='topic1', partition=0, offset=110, timestamp=1724218988589, timestamp_type=0, key=None, value={'str': 'value0'}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=17, serialized_header_size=-1)
    print("value", msg.value)
    print("time", datetime.fromtimestamp(msg.timestamp/1000))
    print("patition", msg.partition)
    print("topic", msg.topic)
    print("offset", msg.offset)

print("get consumer end")
