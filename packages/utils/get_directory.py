import os
import sys

def video(file_name, video_ext=None):
    output_directory = os.path.abspath('output')

    video_path = os.path.join(output_directory, f'video')

    if video_ext:
        video_file = os.path.join(video_path, f'{file_name}.{video_ext}')
    else:
        video_file = os.path.join(video_path, f'{file_name}')

    return video_file

def audio(file_name, audio_ext=None):
    output_directory = os.path.abspath('output')

    audio_path = os.path.join(output_directory, f'audio')

    if audio_ext:
        audio_file = os.path.join(audio_path, f'{file_name}.{audio_ext}')
    else:
        audio_file = os.path.join(audio_path, f'{file_name}')

    return audio_file

def root(temp=False, exe=True):
    if temp:
        try:
            return os.path.abspath(sys._MEIPASS)
        except:
            return os.getcwd()
    
    try:
        return (os.path.dirname(sys.executable))
    except:
        return os.getcwd()