import math

import mouse_controls
from screen_capture import capture_pool_table_image
from image_parser import *
from utils import *


def target_stick_at(x, y):
    for i in range(11):
        mouse_controls.set_mouse_position(x + (i % 2), y)
        wait()
    mouse_controls.left_mouse_down()
    wait()


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
    return balls


def run():
    # mouse_x, mouse_y = mouse_controls.get_mouse_position()
    screenshot_filepath = capture_pool_table_image()  # "test_screenshots/1437338815.png"  #
    balls_positions = map(to_screen_pos, get_balls_positions(screenshot_filepath))
    print("all balls: ", balls_positions)
    if len(balls_positions) <= 1:
        return 1

    white_balls_positions = map(to_screen_pos, get_white_ball_position(screenshot_filepath))
    print("white: ", white_balls_positions)

    for white_ball_position in white_balls_positions:
        balls_without_white = remove_white_ball_from_balls_list(white_ball_position, balls_positions[:])
        print("without white: ", balls_without_white)
        try:
            closest = get_closest_ball_position(white_ball_position, balls_without_white)
        except ValueError:
            closest = white_ball_position
            print("Other ball not found!!!")
        print(closest)
        hit_ball(closest, white_ball_position)
    wait(10)


if __name__ == "__main__":
    rounds = 0
    while True:
        rounds += 1
        if run():
            print("Rounds needed: {0}".format(rounds))
            exit(0)
