from machine import Pin, I2C
from fifo import Fifo
from ssd1306 import SSD1306_I2C
import time


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


class LedMenu:
    def __init__(self, button, led1, led2, led3):
        self.i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
        self.oled = SSD1306_I2C(128, 64, self.i2c)
        self.button = Pin(button, mode=Pin.IN, pull=Pin.PULL_UP)
        self.button.irq(handler=self.button_handler, trigger=Pin.IRQ_FALLING, hard=True)
        self.fifo = Fifo(10, typecode="i")
        self.old_time = 0

        self.leds = [Pin(led1, Pin.OUT), Pin(led2, Pin.OUT), Pin(led3, Pin.OUT)]
        self.led_states = ['OFF', 'OFF', 'OFF']

        for led in self.leds:
            led.off()

        self.current_row = 0
        self.state = self.cursor

    def button_handler(self, pin):
        delay = 200
        current_time = time.ticks_ms()
        
        if time.ticks_diff(current_time, self.old_time) >= delay:
            self.fifo.put(2)
            self.old_time = current_time


    def update_oled_display(self):
        self.oled.fill(0)
        for i, state in enumerate(self.led_states):
            led_name = f"LED{i + 1}"
            pointer = " <" if i == self.current_row else ""
            self.oled.text(f"{led_name}: {state}{pointer}", 0, 10 * (i + 1), 1)

    def cursor(self):
        if not rot.fifo.has_data():
            return
        movement = rot.fifo.get()
        if movement == -1 and self.current_row < len(self.leds) -1 : 
            self.current_row += 1
        elif movement == 1 and self.current_row > 0:
            self.current_row -= 1
        self.update_oled_display()

    def led_toggle(self):
        if self.fifo.has_data() and self.fifo.get() == 2:
            selected_led = self.leds[self.current_row]
            selected_led.toggle()
            self.led_states[self.current_row] = 'ON' if selected_led.value() else 'OFF'
            self.update_oled_display()


rot = Encoder(10, 11)
led_screen = LedMenu(12,22,21,20)

while True:
    while rot.fifo.has_data():
        led_screen.state()

    while led_screen.fifo.has_data():
        led_screen.led_toggle()
    led_screen.oled.show()
