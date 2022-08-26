import urllib.request
from parameterYAML import request_paramater

get_boturl= request_paramater.get_parameter_yaml(0, 'url')
get_webhost = request_paramater.get_parameter_yaml(0, 'webserver')
get_botname = request_paramater.get_parameter_yaml(0, 'bot_name')

url = '{}/getWebhookInfo'.format(get_boturl)

try:
    access = urllib.request.urlopen(url)
    print(access.read())
except Exception as e:
    raise(e)