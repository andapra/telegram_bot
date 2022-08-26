import logging
import yaml
from datetime import datetime
import os, sys

sys.path.append(r'..')
from parameterYAML import request_paramater

def logpath():
    path_log_file = request_paramater.get_parameter_yaml(1, 'logfile')
    return path_log_file

class create_logtelegram():
    def __init__(self) -> None:
        pass

    def debug(message):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('BOT'+time+'.log')
        path = logpath()
        fullpath = os.path.join(path, logfile)

        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []

        main.setLevel(logging.DEBUG)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.debug(message)
    
    def info(message):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('BOT'+time+'.log')
        path = logpath()
        fullpath = os.path.join(path, logfile)

        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []

        main.setLevel(logging.INFO)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.info(message)

    def warning(message):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('BOT'+time+'.log')
        path = logpath()
        fullpath = os.path.join(path, logfile)

        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []
        
        main.setLevel(logging.WARNING)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.warning(message)

    def error(message):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('BOT'+time+'.log')
        path = logpath()
        fullpath = os.path.join(path, logfile)

        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []

        main.setLevel(logging.ERROR)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.warning(message)

    def critical(message):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('BOT'+time+'.log')
        path = logpath()
        fullpath = os.path.join(path, logfile)
        
        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []

        main.setLevel(logging.CRITICAL)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.critical(message)