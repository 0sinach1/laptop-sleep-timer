import os
import time

file_path = r"C:\Users\Vinfotech\OneDrive\Documents\Coding\Projects\Python\SleepLaptop.bat"


is_counting = True

def sleep_min(minutes):
    real_time = minutes * 60
    min = minutes
    seconds = 0
    
    # print(f"this is minutes {min} and this is second {seconds}")  
    # print(real_time)
    # i = real_time - 1
    
    while is_counting:
        time.sleep(1)
        
        if(seconds < real_time):
            # print(f"time left: ")
            seconds += 1
            print(f"{seconds}")  
            
            
        if (seconds == real_time):
            os.startfile(file_path)
            
        
        
        
sleep_min(int(input("How many minutes before is sleep: ")))