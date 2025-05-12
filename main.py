import os
import argparse

from packages.utils import banner

from packages.utils import logging
from packages.services.ytdlp_services import ytdlpServices

from packages.utils.ffmpeg import FFmpeg

from packages.utils.sanitize_title import sanitize
from packages.utils.download import download_video, download_audio
from packages.utils.audio import is_audio, find_audio_format
from packages.utils.get_format import get as get_format

from packages.utils import file

def main(debug):
    banner.prints()

    try:
        parser = argparse.ArgumentParser(description='Video downloader made for editors!')
        parser.add_argument('url', help='ofc url u want to download it.')

        args = parser.parse_args()

        url = args.url
    except :
        url = input('Insert URL : ')

    logging.info('Program Started!')

    if not debug:
        ffmpeg = FFmpeg()
    else:
        ffmpeg = FFmpeg(debug=True)

    service = ytdlpServices(url)

    # Proses url dan ambil semua informasi format didalmnya
    logging.info('Fetching data from URL...')

    info = service.get_info()
    info_title = sanitize(info['title']) + f' ({info['webpage_url_basename']})'

    file.write(info)

    formats = get_format(info)

    if type(formats) is list:    
        print('\n')
        print('Choose Format/Resolution')

        print('-------------------------------')
        for idx, format in enumerate(formats):
            print(f'|  {idx + 1}. ' + format['format'])
        
        print('-------------------------------')

        choose_format = int(input('Input : ')) - 1

        print('\n')

        try:
            format = formats[choose_format]
        except:
            logging.error('Format not found. Are you sure you have chosen it correctly?')
            exit()
    else:
        format = formats

    # Mulai mendownload
    if is_audio(format):
        audio_url = format['url']
        audio_ext = format['ext']
        
        print('[ INFO ] Downloading Audio...')
        if format['protocol'] == 'm3u8_native':
            title = info_title + '(audio)'
            audio_ext = 'mp3'

            ffmpeg.m3u8_download(audio_url, 'mp3', title)
        else:
            download_audio(audio_url, info_title, audio_ext)

        #open_explorer.open_audio(info_title, audio_ext)
        logging.info('Download Complete!')
    else:
        video_url = format['url']
        video_ext = format['ext']


        logging.info('Downloading Video...')

        if format['protocol'] == 'm3u8_native':
            title = info_title + '(video)'
            video_ext = 'mp4'

            ffmpeg.m3u8_download(video_url, 'mp4', title)
        else:
            download_video(video_url, info_title, video_ext)

        audio_format = find_audio_format(formats)
        if audio_format:
            logging.info('Downloading Audio...')
            audio_url = audio_format['url']
            audio_ext = audio_format['ext']

            if audio_format['protocol'] == 'm3u8_native':
                title = info_title + '(audio)'
                audio_ext = 'mp3'

                ffmpeg.m3u8_download(audio_url, 'mp3', title)
            else:
                download_audio(audio_url, info_title, audio_ext)

            logging.info('Download Complete, merging file...')
            ffmpeg.merge_video_audio(info_title, video_ext, audio_ext) 

        logging.info('Program Completed.')


main(debug=False)