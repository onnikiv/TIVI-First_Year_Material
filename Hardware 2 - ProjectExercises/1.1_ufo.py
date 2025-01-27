import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)
sw1 = Pin(7, Pin.IN, Pin.PULL_UP)
sw2 = Pin(9, Pin.IN, Pin.PULL_UP)

ufo_width = 8
ufo_height = 8
x = oled_width // 2
y = oled_height - ufo_height
ufo = "<=>"
max_x = int(oled_width - (len(ufo) * ufo_height))

while True:
    oled.fill(0)
    oled.text(ufo, x, y, 1)
    oled.show()
    if sw1.value() == 0 and x < max_x:
            x += 1           
    if sw2.value() == 0 and x > 0:
            x -= 1
