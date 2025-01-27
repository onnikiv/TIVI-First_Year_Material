import time
from filefifo import Filefifo

data = Filefifo(10, name='capture_250Hz_02.txt')
read_data = []
time_spent = []
scaled_data = []
On = True

class Scale:
    
    def __init__(self, readtime, plottime):
        self.readtime = readtime
        self.plottime = plottime
        self.state = self.read
        
    def execute(self):
        self.state()
    
    def read(self):
        data_from_data = data.get()
        read_data.append(data_from_data)
        time.sleep_ms(1)
        self.state = self.dont_read
    
    def dont_read(self):
        time_spent.append(1)
        print(f"{len(time_spent)}ms")
        
        if len(time_spent) == self.readtime * 100:
            self.state = self.scale
        else:
            self.state = self.read
    
    def scale(self):
        old_min = min(read_data)
        old_max = max(read_data)
        new_min = 0
        new_max = 100
        
        for i in read_data:
            scaled = ((i - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min
            scaled_data.append(scaled)
        
        self.state = self.clear_time
            
    def clear_time(self):
        time_spent.clear()
        self.state = self.printing
        
    def printing(self):
        for i in scaled_data:
            print(i)
            time_spent.append(1)
            if len(time_spent) == self.plottime * 100:
                self.state = self.dont_print
                
    def dont_print(self):
        On = False

scaling = Scale(2, 10)

while On:
    scaling.execute()

