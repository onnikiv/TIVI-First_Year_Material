from machine import ADC, Pin
import time

class Threshold:
    def __init__(self):
        self.ADC_pin = ADC(Pin(26, Pin.IN)) # For ADC-Value -> Voltage
        self.DIG_pin = Pin(26, Pin.IN) # For reading 0 or 1
        self.prev_value = 0

    def read(self):
        max_ADC_value = 65535
        max_voltage = 3.3
        
        self.ADC_Voltage = (self.ADC_pin.read_u16() / max_ADC_value) * max_voltage
        self.DIG_Value = self.DIG_pin.value()
        
        print(f"Digital pin state: {self.DIG_Value} -- ADC pin voltage: {self.ADC_Voltage:.2f}V")
        
        if self.DIG_Value == 1 and self.prev_value == 0:
            print(f"Triggered High - ADC Voltage: {self.ADC_Voltage:.2f}V")
            self.prev_value = 1
        elif self.DIG_Value == 0 and self.prev_value == 1:
            print(f"Triggered Low - ADC Voltage: {self.ADC_Voltage:.2f}V")
            self.prev_value = 0

    def execute(self):
        self.read()

testing = Threshold()

while True:
    testing.execute()
    time.sleep(0.2)
