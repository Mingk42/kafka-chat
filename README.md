# kchat
- [x] 일방적인 채팅 만들기
> producer가 exit로 프로그램을 종료하는 경우 consumer도 같이 종료하도록 하였습니다.
### Usage
#### producer
```bash
$  python src/kchat/kafka/producerChat.py
채팅 프로그램 - 메시지 발신
메시지를 입력하세요. (종료시 'exit' 입력)
YOU: 
```

#### consumer
```bash
$ python src/kchat/kafka/consumerChat.py
채팅 프로그램 - 메시지 수신
메시지 대기 중...
```

### Test
![image](https://github.com/user-attachments/assets/ecbfd395-ac64-4037-985c-dfd3ea9b756a)

### Dependency
<img alt="kafka-python:2.0.2" src="https://img.shields.io/badge/kafka--python-2.0.2-brightgreen">

### Licence
- MIT
