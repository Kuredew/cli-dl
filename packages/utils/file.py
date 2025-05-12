from json import dump as json_dump
from . import get_directory
import os

def write(data):
    folder = os.path.join(get_directory.root(), 'data')

    if not os.path.exists(folder):
        os.makedirs(folder)

    file = os.path.join(folder, 'last_download_info.json')

    with open(file, 'w') as f:
        json_dump(data, f, indent=4)