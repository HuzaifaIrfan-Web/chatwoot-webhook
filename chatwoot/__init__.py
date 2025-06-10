

import requests
from requests.exceptions import RequestException
# User Token in User Profile
# Super Admin Console Agent Bot Access Token

import os

# Access environment variables
CHATWOOT_URL = os.getenv("CHATWOOT_URL", "http://0.0.0.0:3000")
print(f"CHATWOOT_URL at '{CHATWOOT_URL}'")

CHATWOOT_API_TOKEN = os.getenv(
    "CHATWOOT_API_TOKEN", "ysSSYhPFfc3PyMDkDLeTBcYD")
# print(f"CHATWOOT_API_TOKEN at '{CHATWOOT_API_TOKEN")


# https://app.chatwoot.com/api/v1/accounts/{account_id}/conversations/{conversation_id}/toggle_status
def open_conversation_status(account_id, conversation_id):
    url = f"{CHATWOOT_URL}/api/v1/accounts/{account_id}/conversations/{conversation_id}/toggle_status"
    headers = {
        "Content-Type": "application/json",
        "api_access_token": CHATWOOT_API_TOKEN
    }
    payload = {"status": "open"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raises exception for 4XX/5XX errors
        return response.json()
    except RequestException as e:
        print(f"Error updating conversation status: {e}")
        if hasattr(e, 'response') and e.response:
            print(f"Response content: {e.response.text}")
        return None


# https://app.chatwoot.com/api/v1/accounts/{account_id}/conversations/{conversation_id}/messages
def create_new_message(account_id, conversation_id, message):
    url = f"{CHATWOOT_URL}/api/v1/accounts/{account_id}/conversations/{conversation_id}/messages"
    headers = {
        "Content-Type": "application/json",
        "api_access_token": CHATWOOT_API_TOKEN
    }
    payload = {
        "content": message,
        "message_type": "outgoing",
        "private": False
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raises exception for 4XX/5XX errors
        return response.json()
    except RequestException as e:
        print(f"Error updating conversation status: {e}")
        if hasattr(e, 'response') and e.response:
            print(f"Response content: {e.response.text}")
        return None
