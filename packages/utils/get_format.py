from . import logging

def get(info):
    if 'formats' in info:
        return info['formats']
    elif 'formats' in info['entries']:
        return info['entries'][0]['formats']
    else:
        logging.info('Detected multi video page.')
        index = int(input('Insert index page : ')) - 1

        return info['entries'][index]