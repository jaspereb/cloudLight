#The main cloud control program
from neopixel import *
import sys
import cloud #Global states file
import displayHelper #Display functions
from weatherHelper import *
from displayMain import * 

if __name__ == '__main__':
    cloud.strip.begin()
    goDark()
    
    #Check PHP to update state
    #checkPHP()

    print("Running main and the weather is")
    getWeather()
    print(cloud.weatherState)

    displayMain()
    print("End of Main")
    sys.exit()