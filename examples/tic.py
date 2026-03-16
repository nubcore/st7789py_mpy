import sys
import random
import tft_config
import noto_fonts.NotoSansMono_32 as noto
from time import sleep_ms
from machine import RTC, Timer, I2C, Pin

DEV = False

build = sys.implementation._build
print(build)

if build == "ESP32_GENERIC_S3":
 print("DEV MODE 'Metro'")
 DEV = True
 from machine import I2C
 i2c = I2C(1, scl=48, sda=47)

tim0 = Timer(0)
tim1 = Timer(1)

odd = 0

rtc = RTC()

disp = tft_config.config(1)

disp.write(noto, build[6:], 40, 20)
sleep_ms(1_000)
disp.fill(0)

def tic(t):
  # Update every second
  # TODO: Synchronize to second
  if DEV:
   v = i2c.readfrom_mem(0x36, 0x02, 2)
   volts = "{:.2f}v".format((v[0] * 256 + v[1]) * .000078125)
   p = i2c.readfrom_mem(0x36, 0x04, 2)
   percent = "{:.1f}%".format((p[0] * 256 + p[1]) / 256)
   c = i2c.readfrom_mem(0x36, 0x16, 2)
   crate = "{:3.1f}%".format(((c[0] << 8) + c[1]) * 0.208)
   disp.write(noto, "{:} {:}".format(volts, percent), 40, 0, random.getrandbits(16))
   disp.write(noto, crate, 0, 40, random.getrandbits(16))
  disp.write(noto, now(), 130, 40, random.getrandbits(16))

def toc(t):
 # Blink pixel at 0, 0
 global odd
 if odd:
  odd = 0
  disp.pixel(0, 0, 0)
 else:
  odd = 1
  disp.pixel(0, 0, 32000)

def now():
 h = rtc.datetime()[4]
 m = rtc.datetime()[5]
 s = rtc.datetime()[6]
 return "{:02d}:{:02d}:{:02d}".format(h,m,s)

tim0.init(freq=1, callback=tic)

tim1.init(freq=10, callback=toc)
