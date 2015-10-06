import mouse_controls
from utils import *
from config import TABLE_X_CENTER, TABLE_Y_CENTER


def target_stick_at(x, y):
    mouse_controls.set_mouse_position(x, y)
    mouse_controls.left_mouse_down()
    wait(.1)


def target_stick_at_center():
    target_stick_at(TABLE_X_CENTER, TABLE_Y_CENTER)


def shot_from_left():
    target_stick_at(TABLE_X_CENTER, TABLE_Y_CENTER)
    mouse_controls.set_mouse_position(TABLE_X_CENTER - 200, TABLE_Y_CENTER)
    mouse_controls.left_mouse_up()


def shot_from_right():
    target_stick_at(TABLE_X_CENTER, TABLE_Y_CENTER)
    mouse_controls.set_mouse_position(TABLE_X_CENTER + 200, TABLE_Y_CENTER)
    mouse_controls.left_mouse_up()


def run():
    shot_from_left()
    shot_from_right()
    wait(3)


def main():
    while True:
        run()


if __name__ == "__main__":
    main()
