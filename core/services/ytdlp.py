import os

from alive_progress import alive_bar
from yt_dlp import YoutubeDL
from core.logging import Logger
from core.utils import CookieManager


def progress_hooks(d):
    if d['status'] == 'finished':
        progress_hooks.bar.title = 'Finished'
    
    percent = d['_percent']

    progress_hooks.bar(percent / 100)
    progress_hooks.bar.title = 'Downloading'

    

class Downloader:
    def __init__(self, opt):
        self.opt = opt
        self.ydl_opts = {}

        self.ydl_opts['logger'] = Logger
        self.ydl_opts['progress_hooks'] = [progress_hooks]
        self.ydl_opts['noprogress'] = True

        if 'resolution' in self.opt:
            self.ydl_opts['format_sort'] = [f'res:{self.opt['resolution']}']
            self.ydl_opts['format'] = 'bv*+ba'
            self.ydl_opts['merge_output_format'] = 'mp4'

            if self.opt['convert']:
                self.file_path = os.path.join(self._current_path(), 'video_source.mp4')
                self.ydl_opts['outtmpl'] = self.file_path
            else:
                self.ydl_opts['outtmpl'] = '%(title)s.%(ext)s'
        else:
            self.ydl_opts['format'] = 'ba/best'

            if self.opt['convert']:
                self.file_path = os.path.join(self._current_path(), 'audio_source.mp3')
                self.ydl_opts['outtmpl'] = self.file_path
            else:
                self.ydl_opts['outtmpl'] = '%(title)s.%(ext)s'

        if self.opt['cookie']:
            cookie_manager = CookieManager()

            self.ydl_opts['cookiefile'] = cookie_manager.get_cookie()


    def start(self):
        with YoutubeDL(self.ydl_opts) as ydl:
            Logger.info('Starting Download.')
            

            with alive_bar(manual=True) as bar:
                bar.title = 'Preparing'
                progress_hooks.bar = bar

                info = ydl.extract_info(self.opt['url'], download=True)

            download_info = {
                'type': 'video' if 'resolution' in self.opt else 'audio',
                'file_path': self.file_path if self.opt['convert'] else info['title'],
                'title': info['title']
            }

            Logger.info('Download Finished.')

            return download_info
        
    def _current_path(self):
        current_directory = os.path.abspath(os.getcwd())
        return current_directory
        