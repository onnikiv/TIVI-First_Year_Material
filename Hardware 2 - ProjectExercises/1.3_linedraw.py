import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)
sw0 = Pin(9, Pin.IN, Pin.PULL_UP)
sw1 = Pin(8, Pin.IN, Pin.PULL_UP)
sw2 = Pin(7, Pin.IN, Pin.PULL_UP)

x = 0
y = 30
colour = 1

while True:
    if sw2.value() == 0:
        if y > 0:
            y -= 1
        x += 1
        oled.pixel(x, y, colour)
        oled.show()

    elif sw0.value() == 0:
        if y < oled_height - 1:
            y += 1
        x += 1
        oled.pixel(x, y, colour)
        oled.show()
    
    elif sw1.value() == 0:
        x = 0 
        y = 30
        oled.fill(0)
        oled.show()

    if x >= oled_width:
        x = 0
        oled.fill(0)
