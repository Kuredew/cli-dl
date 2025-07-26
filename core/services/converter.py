import config

from core.utils import filenameConverter

class Converter:
    def __init__(self, file_path, title):
        import subprocess
        self.ffmpeg_path = config.FFMPEG_PATH

        self.subprocess = subprocess
        self.argument = [
            self.ffmpeg_path,
            '-i',
            file_path
        ]

        self.title = filenameConverter(title)

    def video_to_mp4(self):
        self.argument.append(f'{self.title}.mp4')

        self.subprocess.run(self.argument)

    def audio_to_mp3(self):
        self.argument.append(f'{self.title}.mp3')

        self.subprocess.run(self.argument)