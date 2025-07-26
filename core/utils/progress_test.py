from alive_progress import alive_bar
import time

with alive_bar(100) as bar:
    bar(int(50.4))
    time.sleep(1)
    bar(0.7)