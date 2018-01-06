#This is the cloud global variables file
from neopixel import *

# LED strip configuration: (Thanks to Tony DiCola)
LED_COUNT      = 120      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB  # Strip type and colour ordering

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, 
                              LED_DMA, LED_INVERT, LED_BRIGHTNESS, 
                              LED_CHANNEL, LED_STRIP)

#A list of common colours
red = Color(255,0,0)
green = Color(0,255,0)
blue = Color(0,0,255)
black = Color(0,0,0)
white = Color(150,255,220)
weakBlue = Color(0,0,20)

#Monthly average temperatures in deg C
averages = [26,26,25,23,20,18,17,18,20,22,24,26]
    
#Variable Definitions
weatherState = 'clear'
#0 - 'clear'
#1 - 'rain'
#2 - 'weird'
#3 - 'storms'
#4 - 'extreme' 

intensity = 0
#The ranges for intensity are:
# storm - 0-2
# rain - 0-4

temperature = 0
#Temperature is the difference from the monthly mean in Celsius 
#(only used for sunny/cloudy weather)

mode = 'weather'
#A mode switch for the cloud state machine
# 'weather' displays the current weather
# 'alarm' displays the current weather between the set alarm times every morning
# 'lightning' displays a lightning show
# 'rain' displays a rain show
# 'rainbow' displays a rainbow show
# 'color' displays a fixed colour
# 'off' turns the lights off

brightness = 0.9
#[0-1] float which adjusts the relative brightness of the various manual mode functions

color = red
brightColor = red
#Only applies to the 'color' mode

alarmStart = [8, 20];
alarmStop = [8, 40];
#The alarm start and stop times as tuples of (hh,mm) in 24 hour time
