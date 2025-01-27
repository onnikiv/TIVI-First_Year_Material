##### _Written in Markdown by Onni Kivinen_ - https://github.com/onnikiv/Hardware1_Digital-Circuits
# Digital Circuits - 7 ASM-chart to Python 
Seventh week's assignments

### 1.1 Implement an ASM chart in Python

```python
from machine import Pin
import time

class Light:
    def __init__(self, delay, button, led):
        self.delay = delay
        self.btn = Pin(button, Pin.IN, Pin.PULL_UP)
        self.led = Pin(led, Pin.OUT)
        self.state = self.off
        
    def execute(self):
        self.state()

    def off(self):
        self.led.off()
        time.sleep(self.delay)
        
        if self.btn.value() == 0:
            self.state = self.onw
        else:
            self.state = self.off
        
    def onw(self):
        self.led.on()
        time.sleep(self.delay)
        
        if self.btn.value() == 1:
            self.state = self.on
        else:
            self.state = self.onw
        
    def on(self):
        self.led.on()
        time.sleep(self.delay)
        
        if self.btn.value() == 1:
            self.state = self.on
        else:
            self.state = self.offw
        
    def offw(self):
        self.led.off()
        time.sleep(self.delay)
        
        if self.btn.value() == 1:
            self.state = self.off
        else:
            self.state = self.offw

asm = Light(0.05, 7, 20) # 50ms period, button, led/lamp

while True:
    asm.execute()
```

### 1.2 Design and implement a state machine 

![alt text](/images/07_ASM-chart-1.2.png)

```python
from machine import Pin
import time

class Drill:
    
    def __init__(self, delay, button_IN, alarm_IN, lamp_OUT, siren_OUT):
        self.delay = delay
        self.btn = Pin(button_IN, Pin.IN, Pin.PULL_UP)
        self.alrm = Pin(alarm_IN, Pin.IN, Pin.PULL_UP)
        self.lmp = Pin(lamp_OUT, Pin.OUT)
        self.srn = Pin(siren_OUT, Pin.OUT)
        self.state = self.off
        
    def execute(self):
        self.state()

    def off(self):
        self.lmp.off()
        self.srn.off()
        time.sleep(self.delay)
        
        if self.alrm.value() == 1:
            self.state = self.off
        else:
            self.state = self.on

    def on(self):
        self.lmp.on()
        self.srn.on()
        time.sleep(self.delay)
        
        if self.alrm.value() == 1 and self.btn.value() == 0:
            self.state = self.off1
        elif self.alrm.value() == 0:
            self.state = self.on2
        else:
            self.state = self.on
    
    def off1(self):
        self.lmp.off()
        self.srn.off()
        time.sleep(self.delay)
        self.state = self.on1
    
    def on1(self):
        self.lmp.on()
        self.srn.off()
        time.sleep(self.delay)
        
        if self.alrm.value() == 1:
            self.state = self.off1
        else:
            self.state = self.off
    
    def on2(self):
        self.lmp.on()
        self.srn.off()
        time.sleep(self.delay)
        
        if self.btn.value() == 1:
            self.state = self.on2
        else:
            self.state = self.off

asm = Drill(0.20, 7, 9, 22, 20) # delay, SW2-button, SW0-button, led, led

while True:
    asm.execute()
```