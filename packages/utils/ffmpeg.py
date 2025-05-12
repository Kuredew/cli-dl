import os
from . import download
from . import logging
from . import get_directory
from . import logging

import subprocess

class FFmpeg:
    def __init__(self, debug=False):
        if debug:
            self.root_path = os.path.join(os.path.abspath(__file__), '..\\..\\..\\')
        else:
            self.root_path = get_directory.root()

        #print(os.path.abspath(self.root_path))

        self.ffmpeg_folder = os.path.join(self.root_path, 'ffmpeg')
        self.sevenzip_folder = os.path.join(self.root_path, '7zip')

        self.ffmpeg_path = os.path.join(self.ffmpeg_folder, 'ffmpeg-2025-05-07-git-1b643e3f65-essentials_build/bin/ffmpeg.exe')
        self.sevenzip_path = os.path.join(self.sevenzip_folder, '7zip.exe')

        if not self.check_ffmpeg():
            self.download_and_extract_ffmpeg()

    def check_ffmpeg(self):
        if os.path.exists(self.ffmpeg_path):
            return True
        
        os.makedirs(self.ffmpeg_folder, exist_ok=True)
        return False
    
    def check_7zip(self):
        if os.path.exists(self.sevenzip_path):
            return True
        
        os.makedirs(self.sevenzip_folder, exist_ok=True)
        return False

    def download_and_extract_ffmpeg(self):
        ffmpeg_url = 'https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-2025-05-07-git-1b643e3f65-essentials_build.7z'
        sevenzip_url = 'https://www.7-zip.org/a/7zr.exe'

        logging.info('Menginstall Dependency yang dibutuhkan : FFMPEG, 7ZIP')

        ffmpeg_7zip_path = os.path.join(self.ffmpeg_folder, 'ffmpeg.7z')
        logging.info('Mendownload FFMPEG')
        ffmpeg_download = download.start(ffmpeg_url, ffmpeg_7zip_path)

        if ffmpeg_download:
            if not(self.check_7zip()):
                logging.info('Mendownload 7zip')
                sevenzip_download = download.start(sevenzip_url, os.path.join(self.sevenzip_folder, '7zip.exe'))

        if sevenzip_download:
            logging.info('Menginstall ffmpeg')
            cmd = [
                self.sevenzip_path,
                'x', ffmpeg_7zip_path,
                f'-o{self.ffmpeg_folder}'
            ]

            subprocess.call(cmd)
            os.remove(ffmpeg_7zip_path)

            logging.info('Install Selesai')

    def m3u8_download(self, url, ext, file_name):
        logging.info('Mendownload dengan ffmpeg...\n')

        file = file_name + '.' + ext

        cmd = [
            self.ffmpeg_path,
            '-hide_banner',
            '-i', url,
            '-c:v', 'copy',
            file
        ]

        subprocess.call(cmd)

    def merge_video_audio(self, file_name, video_ext, audio_ext):
        video_file = file_name + '(video)' + '.' + video_ext
        audio_file = file_name + '(audio)' + '.' + audio_ext

        output_file = file_name + ' ( Enhanced ).mp4'

        cmd = [
            self.ffmpeg_path,
            '-hide_banner',
            '-loglevel', 'error',
            '-i', video_file,
            '-i', audio_file,
            '-c', 'copy',
            '-map', '0:v:0',
            '-map', '1:a:0',
            output_file
        ]

        print(cmd)

        subprocess.call(cmd)

        logging.info('Membersihkan sampah.')
        os.remove(video_file)
        os.remove(audio_file)
