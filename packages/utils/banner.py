from . import get_directory
import os


def prints():
    banner_path = os.path.join(os.path.join(get_directory.root(True), 'resources'), 'template.txt')

    with open(banner_path, 'r') as f:
        banner = f.read()

    print(banner)