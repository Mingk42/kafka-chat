from kafka import KafkaConsumer
from datetime import datetime
import json

consumer=KafkaConsumer(
            "chat",
            bootstrap_servers=["localhost:9092"],
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="chat-group",
            value_deserializer=lambda x:json.loads(x.decode("utf8"))
        )


print("채팅 프로그램 - 메시지 수신")
print("메시지 대기 중...")

try:
    for msg in consumer:
        data=msg.value
        if data["message"].lower()=="exit":
            print(f"[{datetime.fromtimestamp(data['time'])}] 발신자가 프로그램을 종료하였습니다.")
            print(f"[{datetime.fromtimestamp(data['time'])}] 수신 프로그램을 종료합니다.")
            break
        print(f"[{datetime.fromtimestamp(data['time'])}][FRIEND] {data['message']}")
except KeyboardInterrupt:
    print("\n채팅 종료")
finally:
    consumer.close()
