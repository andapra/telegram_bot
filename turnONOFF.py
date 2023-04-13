import urllib.request
from parameterYAML import request_paramater

get_boturl= request_paramater.get_parameter_yaml(0, 'url')
get_webhost = request_paramater.get_parameter_yaml(0, 'webserver')
get_botname = request_paramater.get_parameter_yaml(0, 'bot_name')

def register_bot():
    url = '{}/setWebhook?url={}/{}&max_connections=80&drop_pending_updates=True'.format(get_boturl, get_webhost, get_botname)
    urllib.request.urlopen(url)

def unregister_bot():
    url = '{}/deleteWebhook?url={}/{}'.format(get_boturl, get_webhost, get_botname)
    urllib.request.urlopen(url)


if __name__ == '__input__':
    params = input("DO YOU WANT TO TURN ON/OFF TELEGRAM BOT: TYPE ON OR OFF>")
    if params == 'ON':
        register_bot()
        print('BOT HAS TURN ON')
    elif params == 'OFF':
        unregister_bot()
        print('BOT HAS TURN OFF')
