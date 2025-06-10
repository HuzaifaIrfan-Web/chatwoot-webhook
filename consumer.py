from confluent_kafka import Consumer, KafkaException

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'pending_user_messages_group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['pending_user_messages'])

try:
    print("Listening for messages on 'pending_user_messages'... Press Ctrl+C to exit.")
    while True:
        msg = consumer.poll(1.0)  # Wait 1 second for a message

        if msg is None:
            continue  # No message this time
        if msg.error():
            raise KafkaException(msg.error())

        key = msg.key().decode('utf-8') if msg.key() else None
        value = msg.value().decode('utf-8') if msg.value() else None
        print(f"Received message: key={key}, value={value}")

except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    consumer.close()
