import os
import time

file_path = r"C:\Users\Vinfotech\OneDrive\Documents\Coding\Projects\Python\SleepLaptop.bat"


time_option = input('Do you want a me to sleep the laptop in seconds or in minutes?(s/m): ')

if time_option == "s":
    sec_time = int(input('In how many seconds do you me to sleep at?: '))
elif time_option == "m":
    min_time = int(input('In how many minutes do you me to sleep at?: '))
else:
    print('invalid option')


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
            break
        
        
        
sleep_min(min_time)



def sleep_sec(seconds):
    real_time = 0
    
    # print(f"this is minutes {min} and this is second {seconds}")  
    # print(real_time)
    # i = real_time - 1
    
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