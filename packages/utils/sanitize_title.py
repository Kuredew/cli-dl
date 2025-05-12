import re


def sanitize(title):
    invalid_chars = r'[<>:"/\\|?*\x00-\x1F]'
    
    title = re.sub(invalid_chars, '', title)

    return title