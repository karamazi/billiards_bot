import time
from config import TABLE_BOX


def wait(seconds=0.1):
    time.sleep(seconds)


def to_screen_pos(pos):
    return TABLE_BOX[0]+pos[0], TABLE_BOX[1]+pos[1]
