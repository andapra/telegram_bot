import yaml

class request_paramater():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def get_parameter_yaml(no_index, name_dictionary):
        with open('config.yaml', 'r') as configfile:
            configdata = yaml.load((configfile), Loader=yaml.FullLoader)
            get_data = configdata[no_index]['{}'.format(name_dictionary)]
            return get_data