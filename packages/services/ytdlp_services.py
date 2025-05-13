from yt_dlp import YoutubeDL
from ..utils import logging

class ytdlpLogger:
    def error(msg):
        logging.error(msg)
    def info(msg):
        logging.info(msg)
    def debug(msg):
        logging.info(msg)
    def warning(msg):
        logging.warn(msg)


class ytdlpServices:
    def __init__(self, url):
        self.url = url

    def get_info(self):
        ydl_opts = {
            'logger': ytdlpLogger
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(self.url, download=False)
                return info
        except Exception as e:
            logging.error(f'yt-dlp error : {e}')
            logging.error('Stopping program.')
            exit(1)

        
    def download(self, opts, info):
        with YoutubeDL(opts) as ydl:
            ydl.download_with_info_file(info)