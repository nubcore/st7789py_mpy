import tft_config
import noto_fonts.NotoSansMono_32 as noto
from time import sleep_ms

h = 12
m = 0

disp = tft_config.config(1)

disp.write(noto, "This is TEST", 20, 20)

sleep_ms(2_000)

def loop():
 while 1:
  disp.fill(0)
  disp.write(noto, now(), 80, 20)
  sleep_ms(900)

def now():
 return "{:02d}:{:02d}".format(h,m)

loop()
