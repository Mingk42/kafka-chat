# kchat

### producer
```bash
$ python src/kchat/kafka/prod.py
[실행시간]: 0.03552985191345215
```

### consumer
```bash
$ $KAFKA_HOME/bin/kafka-console-consumer.sh --topic topic1 --bootstrap-server localhost:9092 --from-beginning   # console 켜지기 전부터 쌓인 topic을 모두 읽어옴
$ $KAFKA_HOME/bin/kafka-console-consumer.sh --topic topic1 --bootstrap-server localhost:9092                    # console 켜진 순간부터 읽어옴
{"str": "value0"}
{"str": "value1"}
{"str": "value2"}
{"str": "value3"}
{"str": "value4"}
{"str": "value5"}
{"str": "value6"}
{"str": "value7"}
{"str": "value8"}
{"str": "value9"}
```

### Dependency
<img alt="kafka-python:2.0.2" src="https://img.shields.io/badge/kafka--python-2.0.2-brightgreen">

### Licence
- MIT
