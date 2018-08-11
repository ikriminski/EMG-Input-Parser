import time

def pretty_time():
    return str(time.asctime( time.localtime(time.time())))
