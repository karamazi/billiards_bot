import mouse_controls
from pool_globals import *
import time
from screen_capture import capture_pool_table_image
from image_parser import get_balls_positions

def start_practice():
    mouse_controls.set_mouse_position(PRACTICE_X, PRACTICE_Y)
    mouse_controls.left_click()
    wait(1)


def target_stick_at(x, y):
    mouse_controls.set_mouse_position(x, y)
    mouse_controls.left_mouse_down()
    wait(.1)


def target_stick_at_center():
    target_stick_at(TABLE_X_CENTER, TABLE_Y_CENTER)


def shot_from_left():
    target_stick_at_center()
    mouse_controls.set_mouse_position(TABLE_X_CENTER - 200, TABLE_Y_CENTER)
    mouse_controls.left_mouse_up()


def shot_from_right():
    target_stick_at_center()
    mouse_controls.set_mouse_position(TABLE_X_CENTER + 200, TABLE_Y_CENTER)
    mouse_controls.left_mouse_up()


def wait(seconds):
    time.sleep(seconds)

def to_screen_pos(pos):
    return TABLE_BOX[0]+pos[0], TABLE_BOX[1]+pos[1]


def run():
    mouse_x, mouse_y = mouse_controls.get_mouse_position()
    screenshot_filepath = capture_pool_table_image()
    print(screenshot_filepath)
    balls_positions_table = get_balls_positions("pool_screenshots/1437338815.png")
    balls_positions_screen = map(to_screen_pos, balls_positions_table)
    print(balls_positions_table)
    print(balls_positions_screen)
    start_practice()
    shot_from_left()
    shot_from_right()
    wait(1)

def main():
    #while True:
        run()


if __name__ == "__main__":
    main()
