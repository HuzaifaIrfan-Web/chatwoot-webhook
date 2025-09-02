
from confluent_kafka import Producer
import json

import logging
logger = logging.getLogger("uvicorn.error")


from settings import settings
KAFKA_URL = settings.KAFKA_URL

producer = Producer({'bootstrap.servers': KAFKA_URL})


def produce_pending_user_message(account_id, conversation_id, user_name, user_email, user_phonenumber, content):
    # Sample JSON data
    payload = {
        "account_id": account_id,
        "conversation_id": conversation_id,
        "name": user_name,
        "email": user_email,
        "phonenumber": user_phonenumber,
        "content": content
    }

    # Serialize to JSON and send
    producer.produce(
        topic='pending_user_messages',
        key=str(payload["conversation_id"]),
        value=json.dumps(payload).encode('utf-8'),
        callback=lambda err, msg, val=payload: (
            logger.error(f"❌ Failed to deliver: {err}") if err else logger.info(
                f"✅ {msg.topic()} Delivered: {val}")
        )
    )

    return producer.flush()


def handle_event(event: dict):

    # print(json.dumps(event, indent=4))

    try:
        status = event["conversation"]["status"]


        if status == "pending":

            content = event["content"]
            # print(content)
            account_id = event["account"]["id"]
            # print(account_id)
            conversation_id = event["conversation"]["id"]
            # print(conversation_id)

            message = event["conversation"]["messages"][0]

            # User Message
            if message["message_type"] == 0:
                sender = message["sender"]

                user_name = sender["name"]
                user_email = sender["email"]
                user_phonenumber = sender["phone_number"]

                # print(f"{account_id} {conversation_id} {user_name} {user_email} {user_phonenumber} {content}")
                produce_pending_user_message(account_id, conversation_id, user_name, user_email, user_phonenumber, content)
                return True

    except:
        Exception("No Status")


    return False