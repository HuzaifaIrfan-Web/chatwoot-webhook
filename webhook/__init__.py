




def handle_event(event: dict):
    # import json
    # print(json.dumps(event, indent=4))
    status=None
    try:
        status=event["conversation"]["status"]
    except:
        Exception("No Status")

        
    if status == "pending":
                  
        content=event["content"]
        # print(content)
        account_id=event["account"]["id"]
        # print(account_id)
        conversation_id=event["conversation"]["id"]
        # print(conversation_id)
        
        message=event["conversation"]["messages"][0]

        # User Message
        if message["message_type"] == 0:
            sender=message["sender"]
            
            user_name=sender["name"]
            user_email=sender["email"]
            user_phonenumber=sender["phone_number"]

            
            print(f"{account_id} {conversation_id} {user_name} {user_email} {user_phonenumber} {content}")

                
