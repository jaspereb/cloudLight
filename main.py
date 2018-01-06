#The main cloud control program
from neopixel import *
import sys
import cloud #Global states file
import displayHelper #Display functions
from weatherHelper import *
from displayMain import * 
import threading

class stateThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        
    def run(self):
        print("Starting thread " + self.name)
        updateStateThread()

def updateStateThread():
    while(1):
        with open('state.txt', 'r') as infile:  
            data = json.load(infile)
            
        cloud.mode = data['mode']
        bs = data['brightness']
        if(bs == 'full'):
            cloud.brightness = 1.0
        elif(bs == 'high'):
            cloud.brightness = 0.7
        elif(bs == 'medium'):
            cloud.brightness = 0.4
        elif(bs == 'low'):
            cloud.brightness = 0.1
        else:
            print("Error: Unknnown brightness")
            
        cloud.color = data['color']
        cloud.brightColor = data['brightColor']
        cloud.alarmStart = data['alarmStart']
        cloud.alarmStop = data['alarmStop']
        time.sleep(1)

if __name__ == '__main__':
    cloud.strip.begin()
    goDark()
    
    stateThread1 = stateThread(1,"stateThread1")
    stateThread1.start()

    print("Running main and the weather is")
    getWeather()
    print(cloud.weatherState)
    
    print("Running display functions:")
    displayMain()
    print("End of Main")
    sys.exit()
    