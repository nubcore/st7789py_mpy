"""Generic ESP32 284x76

"""
import sys
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

    build = sys.implementation._build
    print(build)
    if build == "ESP32_GENERIC_C3":
        # seeeed studio 'XIAO' ESP32-C3
        print("C3 Config")
        sck, mosi, miso, reset, cs, dc, backlight = 8, 10, 0, 4, 3, 9, 5
    else:
        # Adafruit 'Metro' ESP32-S3
        print("S3 Config")
        sck, mosi, miso, reset, cs, dc, backlight = 8, 9, 0, 10, 12, 11, 13

    return st7789.ST7789(
        SoftSPI(baudrate=40000000, sck=Pin(sck), mosi=Pin(mosi), miso=Pin(miso)),
        76,
        284,
        reset=Pin(reset, Pin.OUT),
        cs=Pin(cs, Pin.OUT),
        dc=Pin(dc, Pin.OUT),
        backlight=Pin(backlight, Pin.OUT),
        rotation=rotation)
