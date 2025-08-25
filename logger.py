


import logging
import time


chatwoot_webhook_producer_logger = logging.getLogger("chatwoot_webhook_producer")
chatwoot_webhook_producer_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("log/chatwoot_webhook_producer.log")
formatter = logging.Formatter("[%(asctime)s] [%(process)d] [%(levelname)s]  %(message)s")
formatter.converter = time.gmtime
file_handler.setFormatter(formatter)
chatwoot_webhook_producer_logger.addHandler(file_handler)



chatwoot_open_conversation_status_consumer_logger = logging.getLogger("chatwoot_open_conversation_status_consumer")
chatwoot_open_conversation_status_consumer_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("log/chatwoot_open_conversation_status_consumer.log")
formatter = logging.Formatter("[%(asctime)s] [%(process)d] [%(levelname)s]  %(message)s")
formatter.converter = time.gmtime
file_handler.setFormatter(formatter)
chatwoot_open_conversation_status_consumer_logger.addHandler(file_handler)



chatwoot_create_new_message_consumer_logger = logging.getLogger("chatwoot_create_new_message_consumer")
chatwoot_create_new_message_consumer_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("log/chatwoot_create_new_message_consumer.log")
formatter = logging.Formatter("[%(asctime)s] [%(process)d] [%(levelname)s]  %(message)s")
formatter.converter = time.gmtime
file_handler.setFormatter(formatter)
chatwoot_create_new_message_consumer_logger.addHandler(file_handler)

