
import json

from webhook import produce_pending_user_message

import datetime
UTC_TIME_NOW=str(datetime.datetime.now(tz=datetime.UTC))

import os
KAFKA_URL = os.getenv("KAFKA_URL", "localhost:9092")
print(f"pytest KAFKA_URL at '{KAFKA_URL}'")
    
def test_produce_pending_user_message():
    account_id=1
    conversation_id=1
    user_name="pytest"
    user_email=None
    user_phonenumber=None
    content=UTC_TIME_NOW
    
    ret = produce_pending_user_message(account_id, conversation_id, user_name, user_email, user_phonenumber, content)
    
    assert ret == 0
   


from confluent_kafka import Consumer, KafkaException

conf = {
    'bootstrap.servers': KAFKA_URL,
    'group.id': 'pending_user_messages_group',
    'auto.offset.reset': 'earliest'
}
   
   
    
def test_consume_pending_user_message():
    consumer = Consumer(conf)
    consumer.subscribe(['pending_user_messages'])

    try:
        print("Listening for messages on 'pending_user_messages'")
        while True:
            msg = consumer.poll(0.1)

            if msg is None:
                continue  # No message this time
            if msg.error():
                raise KafkaException(msg.error())

            key = msg.key().decode('utf-8') if msg.key() else None
            value = msg.value().decode('utf-8') if msg.value() else None
            print(f"Received message: key={key}, value={value}")
            payload=json.loads(value)
            content=payload["content"]
            if content == UTC_TIME_NOW:
                break
    finally:
        consumer.close()