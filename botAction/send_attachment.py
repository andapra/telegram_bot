import os, sys
import yaml
import requests

from telegram import Bot, ParseMode
from telegram.utils import request

class attachmentMessage():
    def __init__(self, path_file_attachment, caption_file):
        self.path_file_attachment = path_file_attachment
        self.caption_file = caption_file
    
    def groupAttachment(self, bot_token, group_id):
        request_custom = request.Request(con_pool_size=60, proxy_url=None, urllib3_proxy_kwargs=None, connect_timeout=30, read_timeout=10)
        bot = Bot(token=bot_token, request=request_custom)

        getFile = open(self.path_file_attachment, 'rb')
        try:
            bot.send_photo(chat_id=group_id, photo=getFile, caption=self.caption_file, timeout=60)
        except Exception as e:
            raise(e)