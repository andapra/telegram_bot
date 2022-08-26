import urllib.request
from parameterYAML import request_paramater

get_boturl= request_paramater.get_parameter_yaml(0, 'url')
get_webhost = request_paramater.get_parameter_yaml(0, 'webserver')
get_botname = request_paramater.get_parameter_yaml(0, 'bot_name')

url = '{}/setWebhook?url={}&max_connections=80&drop_pending_updates=True'.format(get_boturl, get_webhost)

try:
    urllib.request.urlopen(url)
    print('Register bot webhook: {} is success'.format(get_webhost))
except Exception as e:
    raise(e)