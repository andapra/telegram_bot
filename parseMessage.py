import os, shutil

class get_message():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def parse_json(telegram_message):
        chat_id = telegram_message['message']['chat']['id']
        try:
            incoming_msg = telegram_message['message']['text']
            person_reply = telegram_message['message']['from']['first_name']
        except:
            incoming_msg = 'There is no message'
            person_reply = 'There is no person/usernmae who reply'
        
        return chat_id, incoming_msg, person_reply