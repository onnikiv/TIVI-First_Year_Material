import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)
y = 0
spam_list = []
i = 0

while True:
    user_input = input(f"{i}:\n")
    spam_list.append(user_input)
    if len(spam_list) > 8:      # if over 8 items, remove first item
        spam_list.pop(0)
    oled.fill(0)
    y = 0
    for rivi in spam_list:
        oled.text(rivi, 0, y, 1)
        y += 8
    oled.show()
    i += 1
