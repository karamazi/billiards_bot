import cv2
import numpy as np
from config import DEBUG_IMGS

def get_balls_positions(screenshot_path):
    img = cv2.imread(screenshot_path, 0)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1=50, param2=30, minRadius=5, maxRadius=20)
    if circles is None:
        print("Balls not found on screen! Looking for radius=1")
        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1=50, param2=30, minRadius=1, maxRadius=20)
    circles = np.uint16(np.around(circles))
    positions = [(x, y) for x, y, radius in circles[0, :]]

    if DEBUG_IMGS:
        cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        for x, y, radius in circles[0, :]:
           cv2.circle(cimg, (x, y), radius, (0, 255, 0), 1)  # draw the outer circle
           cv2.circle(cimg, (x, y), 2, (0, 0, 255), 3)  # draw the center of the circle

        cv2.imshow('image', cimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return positions


# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
def get_white_ball_position(screenshot_path):
    img = cv2.imread(screenshot_path)
    lower_white = np.array([130, 130, 130])
    upper_white = np.array([255, 255, 255])
    mask = cv2.inRange(img, lower_white, upper_white)
    mask = cv2.medianBlur(mask, 5)
    if DEBUG_IMGS:
        cv2.imshow('mask', mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 10, param1=50, param2=10, minRadius=5, maxRadius=20)
    if circles is None:
        print("WHITE BALL NOT FOUND ON IMAGE. Looking for radius=1")
        circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 10, param1=50, param2=10, minRadius=1, maxRadius=20)
    circles = np.uint16(np.around(circles))
    if DEBUG_IMGS:
        for x, y, radius in circles[0, :]:
           cv2.circle(img, (x, y), radius, (0, 255, 0), 1)  # draw the outer circle
           cv2.circle(img, (x, y), 2, (0, 0, 255), 3)  # draw the center of the circle

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    positions = [(x, y) for x, y, radius in circles[0, :]]
    return positions


if __name__ == "__main__":
    get_white_ball_position("test_screenshots/1437338815.png")
    get_balls_positions("test_screenshots/1437338815.png")
