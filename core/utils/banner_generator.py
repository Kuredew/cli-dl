import config

def generate():
    file = config.BANNER_PATH

    with open(file) as f:
        print(f.read())