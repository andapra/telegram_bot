import urllib.request
from parameterYAML import request_paramater

get_boturl= request_paramater.get_parameter_yaml(0, 'url')
get_webhost = request_paramater.get_parameter_yaml(0, 'webserver')
get_botname = request_paramater.get_parameter_yaml(0, 'bot_name')

url = '{}/deleteWebhook?url={}'.format(get_boturl, get_webhost, get_botname)

try:
    urllib.request.urlopen(url)
    print('Unregister bot webhook: {} is success'.format(get_webhost))
except Exception as e:
    raise(e)