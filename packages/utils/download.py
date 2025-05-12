from alive_progress import alive_bar
import requests

import os
from . import logging
from . import get_directory

MAX_RETRIES = 5

def resume(url, file, last_bytes, retry_count=0):
    resume_header = {'Range': 'bytes=%d-' % last_bytes}

    try: 
        response = requests.get(url, headers=resume_header, stream=True)

        if response.status_code == 200:
                size = response.headers.get('Content-Length', 0)

                with open(f'{file}', 'ab') as f:
                    with alive_bar(int(size)) as bar:
                        for chunk in response.iter_content(chunk_size=1024):
                            chunk_size = f.write(chunk)
                            bar(chunk_size)

                return True
    except Exception as e:
        logging.error(f'Terjadi masalah lagi : \n{e}')
        file_size = os.path.getsize(file)
        resume(url, file, file_size, retry_count + 1)

        if (retry_count == MAX_RETRIES):
            logging.error('Sorry, Please check your Internet Connection and run program again.')
            exit()

        #return False

def start(url, file):
    #url = 'https://scontent-sin6-3.cdninstagram.com/o1/v/t2/f2/m367/AQMmghik15_8rcXFVjTEZ6HmtrgkC0kTJFkNY57kXgFwvqsO_evRWvLejchdsKWaEahop6vuRD3cNUxfbkhJoZ-EJV8KBOMnwqH-KANhP9tpfHZIVooXyvjOqXtunDahkYP7CPRVmw.mp4?_nc_cat=110&_nc_sid=9ca052&_nc_ht=scontent-sin6-3.cdninstagram.com&_nc_ohc=C4NAC6hCCQQQ7kNvwGwXnEE&efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfMTA4MHAiLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjkzNjYxOTc0MzM5MjQ1OSwiY2xpZW50X25hbWUiOiJpZyIsInhwdl9hc3NldF9pZCI6MTcxNDY1MzczMjc0ODEwMCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&_nc_zt=28&oh=00_AfI7510xAcCj2mYg6D1v-yovx7yPMBx-lBIl2togov0kUA&oe=68249790'

    try:
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            size = response.headers.get('Content-Length', 0)

            with open(f'{file}', 'wb') as f:
                with alive_bar(int(size)) as bar:
                    for chunk in response.iter_content(chunk_size=1024):
                        chunk_size = f.write(chunk)
                        bar(chunk_size)

            return True
    except Exception as e:
        logging.error(f'An error occurred while downloading : \n{e}')
        if response.headers.get('Accept-Range') == 'bytes':
            logging.info('Continue downloading...')
            file_size = os.path.getsize(file)

            resume(url, file, file_size)
        else:
            logging.error('Server not support resume, restart download...')
            start(url, file)

        return True

def download_video(url, file_name, ext):
    file = file_name + '(video)' + '.' + ext  

    downloaded = start(url, file)
    if downloaded:
        return True

def download_audio(url, file_name, ext):
    file = file_name + '(audio)' + '.' + ext

    downloaded = start(url, file)
    if downloaded:
        return True