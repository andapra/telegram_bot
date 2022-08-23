import os, shutil

class get_message():
    def __init__(self, telegram_message):
        self.telegram_message = telegram_message

    def parse_json(self):
        chat_id = self.telegram_message['message']['chat']['id']
        try:
            incoming_msg = self.telegram_message['message']['text']
            person_reply = self.telegram_message['message']['from']['first_name']
        except:
            incoming_msg = 'Tidak ada msg'
            person_reply = 'Tidak ada reply'
        
        return chat_id, incoming_msg, person_reply