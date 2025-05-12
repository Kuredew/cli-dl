from . import logging

def get(info):
    if 'formats' in info:
        return info['formats']
    elif 'formats' in info['entries']:
        return info['entries'][0]['formats']
    else:
        logging.info('Terdapat lebih dari satu video dalam page/postingan ( biasanya instagram )')
        index = int(input('Masukkan nomor page/postingan yang ingin didownload : ')) - 1

        return info['entries'][index]