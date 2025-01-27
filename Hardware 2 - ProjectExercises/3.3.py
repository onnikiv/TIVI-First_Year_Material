from machine import Pin, I2C
from fifo import Fifo
from filefifo import Filefifo
from ssd1306 import SSD1306_I2C


class Encoder:
    def __init__(self, rot_a, rot_b):
        self.a = Pin(rot_a, mode=Pin.IN, pull=Pin.PULL_UP)
        self.b = Pin(rot_b, mode=Pin.IN, pull=Pin.PULL_UP)
        self.fifo = Fifo(30, typecode='i')
        self.a.irq(handler=self.handler, trigger=Pin.IRQ_RISING, hard=True)

    def handler(self, pin):
        if self.b.value():
            self.fifo.put(-1)
        else:
            self.fifo.put(1)


class DataScroller:
    def __init__(self, filename):
        self.data_fifo = Filefifo(10, name=filename)
        self.sample_list = [self.data_fifo.get() for _ in range(1000)]
        self.min_value = min(self.sample_list)
        self.max_value = max(self.sample_list)
        self.scaled_samples = [
            int((value - self.min_value) / (self.max_value - self.min_value) * 63) # scaling the samples to fit in the screen
            for value in self.sample_list
        ]

        self.i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
        self.oled = SSD1306_I2C(128, 64, self.i2c)
        self.current_start = 0
        self.window_size = 128
        self.state = self.update_display

    def update_display(self):
        self.oled.fill(0)

        for i in range(self.window_size): #draw the wave 128pixels
            index = self.current_start + i
            if index >= len(self.scaled_samples): # if max then stop drawing/going over
                break

            scaled_value = self.scaled_samples[index]
            self.oled.pixel(i, 63 - scaled_value, 1)



    def scroll(self):
        movement = rot.fifo.get()

        if movement == 1 and self.current_start > 0:
            self.current_start -= 1
        elif movement == -1 and self.current_start < len(self.sample_list) - self.window_size:
            self.current_start += 1

        self.update_display()


filename = "capture_250Hz_01.txt"
rot = Encoder(10,11)
scroller = DataScroller(filename)

while True:
    while rot.fifo.has_data():
        scroller.scroll()
    scroller.oled.show()
