import cv2
import numpy as np
from matplotlib import pyplot as plt


def get_balls_positions(screnshot):
    img = cv2.imread(screnshot, 0)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1=50, param2=30, minRadius=6, maxRadius=20)
    circles = np.uint16(np.around(circles))
    positions = [(x, y) for x, y, radius in circles[0, :]]

    # cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # for x, y, radius in circles[0, :]:
    #    print(x, y, [2])
    #    cv2.circle(cimg, (x, y), radius, (0, 255, 0), 1)  # draw the outer circle
    #    cv2.circle(cimg, (x, y), 2, (0, 0, 255), 3)  # draw the center of the circle
    #
    # cv2.imshow('image', cimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return positions


def test_tresh():
    img = cv2.imread("pool_screenshots/1437338815.png")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    thresh = ['img', 'thresh1', 'thresh2', 'thresh3', 'thresh4', 'thresh5']

    for i in xrange(6):
        plt.subplot(2, 3, i + 1), plt.imshow(eval(thresh[i]), 'gray')
        plt.title(thresh[i])

    plt.show()

#http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
def test_find_white_ball():
    img = cv2.imread("pool_screenshots/1437338815.png")
    lower_white = np.array([190, 190, 190])
    upper_white = np.array([255, 255, 255])
    mask = cv2.inRange(img, lower_white, upper_white)
    cv2.imshow('mask', mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_find_white_ball()
