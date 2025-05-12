import subprocess
import os

from . import get_directory

def merge(file_name, video_ext, audio_ext):

    video_file = file_name + '.' + video_ext
    audio_file = file_name + '.' + audio_ext

    output_path = file_name + '-merged.mp4'

    '''video_file = get_directory.video(file_name, video_ext)
    audio_file = get_directory.audio(file_name, audio_ext)

    output_path = get_directory.video(f'{file_name}-merged.mp4')'''

    #cmd = f'ffmpeg/ffmpeg.exe -i {video_path} -i {audio_path} -c:v copy -c:a copy {file_name}.mp4'

    cmd = [
        f'ffmpeg/ffmpeg.exe',
        '-hide_banner',
        '-loglevel', 'error',
        '-i', video_file,
        '-i', audio_file,
        '-c:v', 'copy',
        '-c:a', 'copy',
        output_path
    ]

    subprocess.call(cmd)
    
    os.remove(video_file)
    os.remove(audio_file)