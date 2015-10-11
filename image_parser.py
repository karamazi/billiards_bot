import cv2
import numpy as np
from config import DEBUG_IMGS


def _show_debug_img(img, circles=None):
    if not DEBUG_IMGS:
        return

    if circles:
        for x, y, radius in circles[0, :]:
            cv2.circle(img, (x, y), radius, (0, 255, 0), 1)  # draw the outer circle
            cv2.circle(img, (x, y), 2, (0, 0, 255), 3)  # draw the center of the circle

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def _get_positions(img, edge_tresh,circle_tresh):
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1=edge_tresh, param2=circle_tresh, minRadius=5, maxRadius=20)
    if circles is None:
        cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1=edge_tresh, param2=circle_tresh, minRadius=2, maxRadius=20)
    circles = np.uint16(np.around(circles))
    positions = [(x, y) for x, y, radius in circles[0, :]]
    _show_debug_img(cv2.cvtColor(img, cv2.COLOR_GRAY2BGR), circles)
    return positions


def get_balls_positions(screenshot_path):
    img = cv2.imread(screenshot_path, 0)
    return _get_positions(img, edge_tresh=50, circle_tresh=30)


# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
def get_white_ball_position(screenshot_path):
    img = cv2.imread(screenshot_path)
    lower_white = np.array([130, 130, 130])
    upper_white = np.array([255, 255, 255])
    mask = cv2.inRange(img, lower_white, upper_white)
    mask = cv2.medianBlur(mask, 5)
    _show_debug_img(mask)
    return _get_positions(mask, edge_tresh=50, circle_tresh=10)


if __name__ == "__main__":
    get_white_ball_position("test_screenshots/1437338815.png")
    get_balls_positions("test_screenshots/1437338815.png")
