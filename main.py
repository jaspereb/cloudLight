from weatherHelper import *
from neopixel import *
from lowLevel import *
import threading

# LED strip configuration:
LED_COUNT      = 120      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
# Intialize the library (must be called once before other functions).
strip.begin()

#The ranges for intensity are:
# storm - 0-2
# rain - 0-4

#Temperature is the mean in Celsius (will be zero for thunderstorms)
        
#0 - sunny/cloudy
#1 - rain
#2 - weird
#3 - storms
#4 - extreme 

weatherState = 4
oldWeatherState = weatherState
intensity = 0

while(1):
#    [weatherState, intensity, temperature] = getWeather()
#    if(oldWeatherState != weatherState):
#        goDark(strip)
#    
    
    if(weatherState == 4):
        print("Showing Extreme")
        cloudThread = animationThread(1, "Thread1", strip, "extreme", intensity)
        cloudThread.start()
        showExtreme(strip)
    elif(weatherState == 3):
        print("Showing Storms")
        showStorms(strip, intensity)
    elif(weatherState == 2):
        print("Showing Weird Weather")
        showWeird(strip)
    elif(weatherState == 1):
        print("Showing Rain")
        showRain(strip, intensity)
    elif(weatherState == 0):
        print("Showing Temperature")
        showTemp(strip, temperature)
        
    time.sleep(10)
    print("Currently running threads:")
    print(threading.enumerate())
    
    print("Exiting thread")
    Thread1.exit()
    time.sleep(60)


