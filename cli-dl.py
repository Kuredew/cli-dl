import sys
import os
import time
import argparse
import config

from core.services import Downloader, Converter
from core.utils import resolution_validator, url_validator, user_validator, bannerGenerator
from core.logging import Logger

opt = {}

def get_link_from_arg():
    if len(sys.argv) > 1:
        arg = sys.argv[1]

        Logger.info(f'Checking URL : {arg}')

        if url_validator.validate(arg):
            Logger.info('Warming Up!')
            return arg
        else:
            Logger.error("I'm sorry, URL is invalid!, please check again.")
            return False
        
    Logger.error("\nThis is a CLI application. Please run it through the terminal (do not open it by double-clicking).\n\nExample:\nOpen the terminal, type\n'cli-dl <video/audio url>'\nthen press enter.\n")

    time.sleep(5)
    exit(1)


def parser_arg():
    parser = argparse.ArgumentParser()

    parser.add_argument('url', help='A Video or Audio URL')
    parser.add_argument('--cookie', action='count', help='Turn on Cookie mode.')

    try:
        args = parser.parse_args()
    except:
        Logger.error("\nThis is a CLI application. Please run it through the terminal (do not open it by double-clicking).\n\nExample:\nOpen the terminal, type\n'cli-dl <video/audio url>'\nthen press enter.\n")
        time.sleep(5)
        return False


    if url_validator.validate(args.url) :
        Logger.info('Url is valid.')

        opt['url'] = args.url
        opt['cookie'] = args.cookie

        if args.cookie:
            Logger.info('Cookie is turned on.')

        return True
    else:
        Logger.error("I'm sorry, URL is invalid!, please check again.")
        return False
    

    
    
    
def ask_resolution():
    resolutions = {
        1: {
            'name': 'Audio Only',
            'value': ''
        },
        2: {
            'name': 'SD (480p)',
            'value': 480
        },
        3: {
            'name': 'HD (720p)',
            'value': 720
        },
        4: {
            'name': 'Full-HD (1080p)',
            'value': 1080
        },
        5: {
            'name': 'Quad-HD (1440p)',
            'value': 1440
        },
        6: {
            'name': 'Custom',
            'value': ''
        }
    }


    print('\n==============================')
    print('Select the resolution you want')
    print('==============================')

    for idx, reso in enumerate(resolutions):
        name = resolutions[idx + 1]['name']

        print(f'{idx + 1}. {name}')

    user_input = input('\n > ')

    try:
        user_input = int(user_input)

        if user_input == 6:
            user_input = input('Type the resolution you want : ')

            resolution = int(user_input)
        else:
            resolution = resolutions[user_input]['value']

        return resolution
    except:
        Logger.error('Please input correctly!')
        #sys.exit(100)

def main():
    bannerGenerator()

    if not parser_arg():
        exit(1)

    Logger.info('Waiting for User.')

    #print("\nPlease enter the resolution in pixels. If you're unsure, read this.\n\nIf you want to download at 720p, simply enter 720.\nThe same applies for other resolutions.\n\nLeave blank if you only want to download audio")
    resolution = ask_resolution()
    print()

    if resolution != '':
        resolution = resolution_validator.validate(resolution)

        if not resolution:
            Logger.error('Resolution is not valid.')
            exit(1)
        
        opt['resolution'] = resolution
        opt['convert'] = True if user_validator.validate('Do you want to convert video to H264?') else False
    else:
        opt['convert'] = True if user_validator.validate('Do you want to convert Audio to MP3?') else False
    
    print()

    try:
        if start_services():
            exit()

        exit(1)
    except Exception as e:
        Logger.error(f'Unexpected error at services : {e}')
        exit(1)

    
def start_services():
    Logger.info('Calling Youtube-DL')
    downloader = Downloader(opt)

    try:
        download_info = downloader.start()
    except Exception as e:
        Logger.error(f'Download error, please try again. ({e})')
        return False
    

    if opt['convert']:
        Logger.info('Converting...')
        converter = Converter(download_info['file_path'], download_info['title'])

        if download_info['type'] == 'video':
            converter.video_to_mp4()
        elif download_info['type'] == 'audio':
            converter.audio_to_mp3()

        Logger.info('Convert finish, clearing cache')
        os.remove(download_info['file_path'])

    return True
        

def exit(code=None):

    if not code:
        Logger.info('Program successfully closed without error.')
        Logger.info('Thanks for using my simple program.')
    else:
        Logger.error('Program closed with error, please report to Kureichi')

    # hapus cookie, bahaya jir
    if os.path.exists(config.COOKIE_PATH):
        os.remove(config.COOKIE_PATH)

    sys.exit(100)


if __name__ == '__main__':
    main()