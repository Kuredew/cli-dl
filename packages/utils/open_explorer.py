import subprocess

from .get_directory import video, audio

def open_video(file_name, video_ext):
    args = f'explorer /select,"{video(file_name, video_ext)}"'

    subprocess.Popen(args)

def open_audio(file_name, audio_ext):
    args = f'explorer /select,"{audio(file_name, audio_ext)}"'

    subprocess.Popen(args)