import os
import time


is_counting = True

def sleep_min(minutes):
    real_time = minutes * 60
    min = minutes
    seconds = (minutes * 60) % 3600
    
    print(f"this is minutes {min} and this is second {seconds}")  
    print(real_time)
    i = real_time - 1
    
    while is_counting:
        time.sleep(1)
        
        if(i < real_time):
            print(f"time left: {min}:{i}")
            i -= 1
            seconds = i % 60
            print(f"this is minutes {min} and this is second {seconds}")  
            
            
        if (i == real_time):
            os.openfile()
        
        
        
sleep_min(3)