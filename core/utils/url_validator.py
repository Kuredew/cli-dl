import re


def validate(url_string):
    regex = r"^(http|https|ftp)://[^\s/$.?#].[^\s]*$"
    return re.match(regex, url_string) is not None
