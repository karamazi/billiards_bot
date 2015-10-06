import win32con, win32api
import time

def left_mouse_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)


def left_mouse_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)


def left_click():
    left_mouse_down()
    left_mouse_up()

def left_doubleclick():
    left_click()
    left_click()



def get_mouse_position():
    x, y = win32api.GetCursorPos()
    print(x, y)
    return x, y

def set_mouse_position(x, y):
    win32api.SetCursorPos((x, y))


