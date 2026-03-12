"""Generic ESP32 320x240

"""

from machine import Pin, SoftSPI
import st7789py as st7789

def config(rotation=1):
    """
    Configures and returns an instance of the ST7789 display driver.

    Args:
        rotation (int): The rotation of the display (default: 0).

    Returns:
        ST7789: An instance of the ST7789 display driver.
    """

    return st7789.ST7789(
        SoftSPI(baudrate=40000000, sck=Pin(8), mosi=Pin(9), miso=Pin(0)),
        76,
        284,
        reset=Pin(10, Pin.OUT),
        cs=Pin(12, Pin.OUT),
        dc=Pin(11, Pin.OUT),
        backlight=Pin(13, Pin.OUT),
        rotation=rotation)
