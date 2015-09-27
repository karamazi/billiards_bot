import ImageGrab
import time
from config import TABLE_BOX

__pool_screenshot_format = "pool_screenshots/{0}.png"

def capture_pool_table_image():
    timestamp = int(time.time())
    image = ImageGrab.grab(TABLE_BOX)
    image.save(__pool_screenshot_format.format(timestamp))

