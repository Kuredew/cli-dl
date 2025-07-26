from termcolor import colored
import config
import os
import json

#os.remove(config.LOG_PATH)
json_decoded = {
        'log': []
    }


def _write(string):
    with open(config.LOG_PATH, 'w') as f:
        json_decoded['log'].append(string)

        json.dump(json_decoded, f, indent=4)

class Logger:
    def info(msg):
        text = colored('[ INFO ]', color='green')

        final_text = text + ' ' + msg

        print(final_text)
        _write(final_text)
    def warning(msg):
        text = colored('[ WARN ]', color='yellow')

        final_text = text + ' ' + msg

        print(final_text)
        _write(final_text)
    def error(msg):
        text = colored('[ ERROR ]', color='red')

        final_text = text + ' ' + msg

        print(final_text)
        _write(final_text)
    def debug(msg):
        text = colored('[ DEBUG ]', color='yellow')

        final_text = text + ' ' + msg

        print(final_text)
        _write(final_text)
