# Yeah, harusnya make Logging, tapi males adi bikin sendiri.

import time
from .color import bcolors
from . import get_directory

def get_time():
    return str(time.strftime('%H:%M:%S', time.localtime()))

def info(msg):
    print(get_time() + ' ' + bcolors.OKGREEN + '[ INFO ] ' + bcolors.ENDC + str(msg))

def warn(msg):
    print(get_time() + ' ' + bcolors.WARNING + '[ WARN ] ' + bcolors.ENDC + str(msg))

def error(msg):
    print(get_time() + ' ' + bcolors.FAIL + '[ ERROR ] ' + bcolors.ENDC + str(msg))