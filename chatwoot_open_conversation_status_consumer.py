# Load the .env file
from dotenv import load_dotenv
load_dotenv(override=True)

import os
KAFKA_URL = os.getenv("KAFKA_URL", "localhost:9092")
print(f"KAFKA_URL at '{KAFKA_URL}'")

from confluent_kafka import Producer, Consumer, KafkaException

conf = {
    'bootstrap.servers': KAFKA_URL,
    'group.id': 'open_conversation_status_group',
    'auto.offset.reset': 'earliest'
}

import json
   
from chatwoot import open_conversation_status

def main():
    producer = Producer({'bootstrap.servers': KAFKA_URL})
    payload={
        "account_id":1,
        "conversation_id":1
    }
    # Serialize to JSON and send
    producer.produce(
        topic='open_conversation_status',
        key=str(payload["conversation_id"]),
        value=json.dumps(payload).encode('utf-8'),
        callback=lambda err, msg, val=payload: (
            print(f"❌ Failed to deliver: {err}") if err else print(
                f"✅ {msg.topic()} Delivered: {val}")
        )
    )
    producer.flush()

    consumer = Consumer(conf)
    consumer.subscribe(['open_conversation_status'])

    try:
        print("Listening for messages on 'open_conversation_status'... Press Ctrl+C to exit.")
        while True:
            msg = consumer.poll(1.0)  # Wait 1 second for a message

            if msg is None:
                continue  # No message this time
            if msg.error():
                raise KafkaException(msg.error())

            key = msg.key().decode('utf-8') if msg.key() else None
            value = msg.value().decode('utf-8') if msg.value() else None
            print(f"Received message: key={key}, value={value}")
            payload=json.loads(value)
            
            account_id=payload["account_id"]
            conversation_id=payload["conversation_id"]
            
            ret=open_conversation_status(account_id, conversation_id)
            
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        consumer.close()


if __name__=="__main__":
    main()