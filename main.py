import imp
from flask import Flask, request, Response, Request
from telegram import Bot, ParseMode, ext

from get_json import jsonFile
from parseMessage import get_message

app = Flask(__name__)
@app.route('/', methods=['POST'])
def bot():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id, incoming_msg, person_reply = get_message.parse_json(msg)
        jsonFile.output(msg, 'data.json')

        messageUser = incoming_msg
    
    else:
        return Response('ok', status=200)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)