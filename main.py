from flask import Flask, request, Response, Request
from telegram import Bot, ParseMode, ext

from get_json import jsonFile
from parseMessage import get_message
from parameterYAML import request_paramater

get_botname = request_paramater.get_parameter_yaml(0, 'bot_name')
app = Flask(__name__)
@app.route('/{}'.format(get_botname), methods=['POST'])
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