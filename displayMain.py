#This is the main display logic file which is called as a separate thread from the main

from displayHelper import *
from weatherHelper import *
import cloud
import time

def displayMain():
#    updateState()
#    lastMode = cloud.mode;
    updateCount = 86400
    while(1):
        #updateState()
#        if(lastMode == cloud.mode):
#            modeChFlag = 0
#        else:
#            modeChFlag = 1
#            #Stop current animation thread
#            
#        lastMode = cloud.mode    
            
        print("Mode is " + cloud.mode)
        if(cloud.mode == 'weather'):
            if(updateCount > 900):
                getWeather()
                updateCount = 0
            updateCount = updateCount + 1
            
            print("Running in weather mode")
            if(cloud.weatherState == 'extreme'):
                print("Extreme weather detected!")
                showExtreme()
            elif(cloud.weatherState == 'clear'):
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
            showRain()
        elif(cloud.mode == 'rainbow'):
            print("Running in rainbow mode")
            showRainbow()
        elif(cloud.mode == 'color'):
            print("Running in color mode")
            setColor(cloud.color,0)
            time.sleep(0.5)
        elif(cloud.mode == 'off'):
            print("Cloud is Off")
            goDark()
            time.sleep(5)
        else:
            print("ERROR: Unknown mode detected")
            
        time.sleep(1)
            
        
        