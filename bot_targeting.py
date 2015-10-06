import math

import mouse_controls
from screen_capture import capture_pool_table_image
from image_parser import *
from utils import *
from config import TABLE_X_CENTER, TABLE_Y_CENTER


def target_stick_at(x, y):
    for i in range(5):
        mouse_controls.set_mouse_position(x + (i % 2), y)
        wait(.2)
    mouse_controls.left_mouse_down()
    wait()


def shot_from_left(x, y):
    mouse_controls.set_mouse_position(x - 200, y)
    mouse_controls.left_mouse_up()


def shot_from_right(x, y):
    mouse_controls.set_mouse_position(x + 200, y)
    mouse_controls.left_mouse_up()


def first_shot():
    target_stick_at(TABLE_X_CENTER, TABLE_Y_CENTER)
    shot_from_left(TABLE_X_CENTER, TABLE_Y_CENTER)


def hit_ball(ball, white_ball):
    bx, by = ball
    wx, wy = white_ball

    move_x = 100 if bx < wx else -100
    move_y = 100 if by < wy else -100
    target_stick_at(bx+move_x/10, by+move_y/10)

    print("move stick to, ", wx + move_x, wy + move_y)
    mouse_controls.set_mouse_position(bx + move_x, by + move_y)
    wait()
    mouse_controls.left_mouse_up()


def get_closest_ball_position(white_ball, balls):
    wx, wy = white_ball
    distances = [math.sqrt((wx - x) ** 2 + (wy - y) ** 2) for x, y in balls]
    closest = min(distances)
    return balls[distances.index(closest)]


def remove_white_ball_from_balls_list(white_ball, balls):
    wx, wy = white_ball
    white_ball_index = 0
    for x, y in balls:
        if abs(x - wx) < 10 and abs(y - wy) < 10:
            white_ball_index = balls.index((x, y))
            break
    del balls[white_ball_index]


def run():
    # mouse_x, mouse_y = mouse_controls.get_mouse_position()
    screenshot_filepath = capture_pool_table_image()  # "test_screenshots/1437338815.png"  #
    balls_positions = map(to_screen_pos, get_balls_positions(screenshot_filepath))
    print("all balls: ", balls_positions)
    if not len(balls_positions):
        return 1

    white_ball_position = to_screen_pos(get_white_ball_position(screenshot_filepath))

    remove_white_ball_from_balls_list(white_ball_position, balls_positions)
    print("white: ", white_ball_position)
    print("without white: ", balls_positions)
    try:
        closest = get_closest_ball_position(white_ball_position, balls_positions)
    except ValueError:
        closest = white_ball_position
        print("Other ball not found!!!")
    print(closest)
    hit_ball(closest, white_ball_position)
    wait(10)


if __name__ == "__main__":
    rounds = 1
    #first_shot()
    wait(2)
    while True:
        rounds += 1
        if run():
            print("Rounds needed: {0}".format(rounds))
            exit(0)
