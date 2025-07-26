from core.logging import Logger


def validate(resolution):
    try:
        resolution = int(resolution)
        return resolution
    except:
        Logger.error('Please enter number only.')
        return False