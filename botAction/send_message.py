import os, sys
import yaml
import requests

from telegram import Bot, ParseMode
from telegram.utils import request

class telegramMessage():
    def __init__(self, message, bot_token, bot_message):
        self.message = message
        self.bot_token = bot_token
        self.bot_message = bot_message
    
    @staticmethod
    def groupMessage(self, group_id):

        bot_token = self.bot_token
        bot_chatID = group_id

        request_custom = request.Request(con_pool_size=60, proxy_url=None, urllib3_proxy_kwargs=None, connect_timeout=30, read_timeout=10)
        bot = Bot(token=bot_token, request=request_custom)

        try:
            bot.send_message(chat_id=bot_chatID, text=self.message, parse_mode=ParseMode.MARKDOWN, timeout=30)
        except:
            bot.send_message(chat_id=bot_chatID, text=self.message, timeout=30)