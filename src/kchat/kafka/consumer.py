from kafka import KafkaConsumer, TopicPartition
import json
import os
from datetime import datetime

OFFSET_FILE="/home/root2/code/kchat/consumer_offset.txt"

def save_offset(offset):
    with open(OFFSET_FILE, "w") as f:
        f.write(str(offset))

def read_offset():
    if os.path.exists(OFFSET_FILE):
            with open(OFFSET_FILE, "r") as f:
                return int(f.read().strip())
    else:
        return None


consumer=KafkaConsumer(
            #"topic5",
            bootstrap_servers=["localhost:9092"],
            value_deserializer=lambda x:json.loads(x.decode("utf8")),
            consumer_timeout_ms=15000,
            auto_offset_reset="earliest" if read_offset() is None else "latest",
            group_id="grp1",
            enable_auto_commit=True
        )

print("get consumer start")

saved_offset=read_offset()

p=TopicPartition("topic5", 0)
consumer.assign([p])

if saved_offset is not None:
    consumer.seek(p,saved_offset)
else:
    consumer.seek_to_beginning(p)

for msg in consumer:
    print(msg)
    # ConsumerRecord(topic='topic1', partition=0, offset=110, timestamp=1724218988589, timestamp_type=0, key=None, value={'str': 'value0'}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=17, serialized_header_size=-1)
    print("value", msg.value)
    print("time", datetime.fromtimestamp(msg.timestamp/1000))
    print("patition", msg.partition)
    print("topic", msg.topic)
    print("offset", msg.offset)

    save_offset(msg.offset+1)

print("get consumer end")
