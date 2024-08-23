from kafka import KafkaProducer
import json
import time


prod=KafkaProducer(
            bootstrap_servers=["localhost:9092"],
            value_serializer=lambda x:json.dumps(x).encode("utf8")
        )


print("채팅 프로그램 - 메시지 발신")
print("메시지를 입력하세요. (종료시 'exit' 입력)")

while True:
    msg=input("YOU: ")

    data = {"message":msg, "time":time.time()}
    prod.send("chat", value=data)
    prod.flush()

    if msg.lower() =="exit":
        break
