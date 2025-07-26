import os
import sys

# Dependencies directory
_dependecies = os.path.join(os.path.dirname(sys.executable), '_internal')
# For debugging.
#_dependecies = os.path.abspath(os.getcwd())
_assets = os.path.join(_dependecies, 'assets')


# Banner directory
BANNER_PATH = os.path.join(_assets, 'banner')

# ffmpeg directory
FFMPEG_PATH = os.path.join(os.path.join(os.path.abspath(_dependecies), 'ffmpeg'), 'ffmpeg.exe')

# Log Path
LOG_PATH = os.path.join(_dependecies, 'log-latest.json')

# Cookie
COOKIE_PATH = os.path.join(_assets, 'cookie.txt')