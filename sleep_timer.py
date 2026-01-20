import os
import time

file_path = r"C:\Users\Vinfotech\OneDrive\Documents\Coding\Projects\Python\SleepLaptop.bat"


time_option = input('Do you want a me to sleep the laptop in seconds or in minutes?(s/m): ')

if time_option == "s":
    sec_time = int(input('In how many seconds do you me to sleep at?: '))
    # print(sec_time)
elif time_option == "m":
    minutes_time = int(input('In how many minutes do you me to sleep at?: '))
    print(minutes_time)
else:
    print('invalid option')


is_counting = True

def sleep_min(minutes):
    real_time = 0
    min = minutes
    seconds = minutes * 60
    
    
    while is_counting:
        time.sleep(1)
        
        if(seconds > real_time):
            # print(f"time left: ")
            seconds -= 1
            print(f"{seconds}")  
            
            
        if (seconds == real_time):
            os.startfile(file_path)
            break
        
        
        
sleep_min(minutes_time)



def sleep_sec(seconds):
    real_time = 0
    
    
    while is_counting:
        time.sleep(1)
        
        if(seconds > real_time):
            # print(f"time left: ")
            seconds -= 1
            print(f"{seconds}")  
            
            
        if (seconds == real_time):
            os.startfile(file_path)
            break
        
        
sleep_sec(sec_time)