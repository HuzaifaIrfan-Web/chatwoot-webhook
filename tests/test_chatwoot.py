
from chatwoot import open_conversation_status, create_new_message
import datetime
UTC_TIME_NOW = str(datetime.datetime.now(tz=datetime.UTC))


account_id = 1
conversation_id = 1


def test_open_conversation_status():
    """{'payload': {'success': True, 'conversation_id': 15, 'current_status': 'open', 'snoozed_until': None}}"""
    res = open_conversation_status(account_id, conversation_id)
    print(res)
    assert res["payload"]["current_status"] == "open"


def test_create_new_message():
    """{'id': 2349, 'content': 'hi', 'inbox_id': 1, 'conversation_id': 15, 'message_type': 1, 'content_type': 'text', 'status': 'sent', 'content_attributes': {}, 'created_at': 1749560592, 'private': False, 'source_id': None, 'sender': {'id': 1, 'name': 'mbot', 'avatar_url': '', 'type': 'agent_bot'}}"""
    content = f"pytest {UTC_TIME_NOW}"
    res = create_new_message(account_id, conversation_id, content)
    print(res)
    assert res["content"] == content
