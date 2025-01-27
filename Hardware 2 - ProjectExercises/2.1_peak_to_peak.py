from filefifo import Filefifo

def peak_to_peak():
    hz = 250
    interval = 1 / hz
    data = Filefifo(10, name='capture_250Hz_01.txt')
    
    last_value = data.get() # 0
    current_value = data.get() # 1
    
    peaks = []
    peak_times = []
    
    for sample in range(5000):
        next_value = data.get()
        
        if current_value > last_value and current_value > next_value: # Now > Then AND Now > Next => we up
            peaks.append(sample)
            time_of_sample = (sample * interval)
            peak_times.append(time_of_sample)
            
            print(f"PEAK ON SAMPLE: {sample:<6} TIME: {time_of_sample:.2f}s")
            
            if len(peaks) >= 4: # we want 3 peaks atleast
                break
        
        last_value = current_value
        current_value = next_value
        
    # How many samples between samples:
    peak_intervals_in_samples = []
    peak_intervals_in_seconds = []
    
    for i in range(1, len(peaks)):
        between = peaks[i] - peaks[i - 1]
        peak_intervals_in_samples.append(between)
        
    for i in range(1, len(peak_times)):
        times_between = peak_times[i] - peak_times[i - 1]
        peak_intervals_in_seconds.append(times_between)
        
    avg_interval = sum(peak_intervals_in_seconds) / len(peak_intervals_in_seconds)
    frequency = 1 / avg_interval

    print(f"\nAMOUNT OF (SAMPLES) BETWEEN PEAKS: {peak_intervals_in_samples}")
    print(f"AMOUNT OF (SECONDS) BETWEEN PEAKS: {peak_intervals_in_seconds}")
    print(f"AVERAGE FREQUENCY: {frequency} Hz")


peak_to_peak()

