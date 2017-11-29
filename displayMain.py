#This is the main display logic file which is called as a separate thread from the main

from displayHelper import *
from weatherHelper import *
import cloud
import time

def displayMain():
    while(1):
        if(cloud.weatherState == 'extreme'):
            print("Extreme weather detected!")
            showExtreme()
        elif(cloud.mode == 'weather'):
            print("Running in weather mode")
            if(cloud.weatherState == 'clear'):
                showTemp()
            elif(cloud.weatherState == 'rain'):
                showRain()
            elif(cloud.weatherState == 'weird'):
                showWeird()
            elif(cloud.weatherState == 'storms'):
                showStorms()
            else:
                print("Unrecognised Weather State")
                print(cloud.weatherState)
        elif(cloud.mode == 'alarm'):
            print("Running in alarm mode")
        elif(cloud.mode == 'lightning'):
            print("Running in lightning mode")
        elif(cloud.mode == 'rain'):
            print("Running in rain mode")
        elif(cloud.mode == 'rainbow'):
            print("Running in rainbow mode")
        elif(cloud.mode == 'color'):
            print("Running in color mode")
            setColor(cloud.color,0)
        elif(cloud.mode == 'off'):
            print("Cloud is Off")
            goDark()
            time.sleep(30)
        else:
            print("ERROR: Unknown mode detected")
            
        time.sleep(1)
            
        
        