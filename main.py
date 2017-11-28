#The main cloud control program
from neopixel import *
import sys
import cloud #Global states file
#import displayHelper #Display functions

if __name__ == '__main__':
    strip = Adafruit_NeoPixel(cloud.LED_COUNT, cloud.LED_PIN, cloud.LED_FREQ_HZ, 
                              cloud.LED_DMA, cloud.LED_INVERT, cloud.LED_BRIGHTNESS, 
                              cloud.LED_CHANNEL, cloud.LED_STRIP)
    strip.begin()
    
    #Check PHP to update state
    #checkPHP()

    print("Running main and the weather is")
#    print(cloud.weatherState)

    #Primary mode switch
#    if(cloud.mode == 'weather'):
#        print("Running in weather mode")
#    elif(cloud.mode == 'alarm'):
#        print("Running in alarm mode")
#    elif(cloud.mode == 'lightning'):
#        print("Running in lightning mode")
#    elif(cloud.mode == 'rain'):
#        print("Running in rain mode")
#    elif(cloud.mode == 'rainbow'):
#        print("Running in rainbow mode")
#    elif(cloud.mode == 'color'):
#        print("Running in color mode")
##        setColor(cloud.color,0)
#    elif(cloud.mode == 'off'):
#        print("Turning cloud off")
##        goDark()
#    else:
#        print("ERROR: Unknown mode detected")
        
    print("End of Main")
    sys.exit()