import os, sys
import yaml
import requests

from telegram import Bot, ParseMode
from telegram.utils import request

class attachmentMessage():
    def __init__(self, message, bot_token, bot_message):
        self.message = message
        self.bot_token = bot_token
        self.bot_message = bot_message
    
    @staticmethod
    def groupAttachment(self, group_id, pathFile, captionFile):

        bot_token = self.bot_token
        bot_chatID = group_id

        request_custom = request.Request(con_pool_size=60, proxy_url=None, urllib3_proxy_kwargs=None, connect_timeout=30, read_timeout=10)
        bot = Bot(token=bot_token, request=request_custom)

        getFile = open(pathFile, 'rb')
        try:
            bot.send_photo(chat_id=bot_chatID, photo=getFile, caption=captionFile, timeout=60)
        except Exception as e:
            raise(e)