import os, sys
import yaml
import requests

from telegram import Bot, ParseMode
from telegram.utils import request

class telegramMessage():
    def __init__(self, bot_token, group_id):
        self.group_id = group_id
        self.bot_token = bot_token
    
    def groupMessage(self, message):
        request_custom = request.Request(con_pool_size=60, proxy_url=None, urllib3_proxy_kwargs=None, connect_timeout=30, read_timeout=10)
        bot = Bot(token=self.bot_token, request=request_custom)

        try:
            bot.send_message(chat_id=self.group_id, text=message, parse_mode=ParseMode.MARKDOWN, timeout=30)
        except :
            bot.send_message(chat_id=self.group_id, text=message, timeout=30)

    def groupAttachment(self, caption_image):
        request_custom = request.Request(con_pool_size=60, proxy_url=None, urllib3_proxy_kwargs=None, connect_timeout=30, read_timeout=10)
        bot = Bot(token=self.bot_token, request=request_custom)

        getFile = open(self.path_file_attachment, 'rb')
        try:
            bot.send_photo(chat_id=self.group_id, photo=getFile, caption=self.caption_file, timeout=60)
        except Exception as e:
            raise(e)