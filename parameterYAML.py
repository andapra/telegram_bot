import yaml

class request_paramater():
    def __init__(self, no_index: int, name_dictionary: str):
        self.no_index = no_index
        self.name_dictionary =  name_dictionary

    def get_parameter_yaml(self):
        with open('config.yaml', 'r') as configfile:
            configdata = yaml.load((configfile), Loader=yaml.FullLoader)
            get_data = configdata[self.no_index]['{}'.format(self.name_dictionary)]
            return get_data