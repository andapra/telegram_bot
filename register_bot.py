import urllib.request
from parameterYAML import request_paramater

get_boturl= request_paramater.get_parameter_yaml(0, 'url')
get_webhost = request_paramater.get_parameter_yaml(0, 'webserver')
get_botname = request_paramater.get_parameter_yaml(0, 'bot_name')

url = '{}/setWebhook?url={}/{}&max_connections=80&drop_pending_updates=True'.format(get_boturl, get_webhost, get_botname)

urllib.request.urlopen(url)