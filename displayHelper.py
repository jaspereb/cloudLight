import cloud
import time
import threading
from itertools import chain
from neopixel import *


# Define functions which animate LEDs in various ways.
def colorWipe(color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(cloud.strip.numPixels()):
         
        cloud.strip.setPixelColor(i, color)
        cloud.strip.show()
        time.sleep(wait_ms/1000.0)

def colorSegment(segment, color):
    if(segment == 'left'):
        numbers = chain(range(1,33), range(67,105))
        for i in numbers:
            cloud.strip.setPixelColor(i, color)
        cloud.strip.show()
    elif(segment == 'mid'):
        numbers = chain(range(33,38), range(62,67), range(104,111))
        for i in numbers:
            cloud.strip.setPixelColor(i, color)
        cloud.strip.show()

    elif(segment == 'right'):
        numbers = chain(range(38,62), range(111,121))
        for i in numbers:
            cloud.strip.setPixelColor(i, color)
        cloud.strip.show()

    else:
        print "Incorrect segment, use 'left' 'mid' 'right'"

def setColor(color, wait_ms=0):
        for i in range(cloud.strip.numPixels()):
                cloud.strip.setPixelColor(i, color)
                time.sleep(wait_ms/1000.0)
        cloud.strip.show()

def theaterChase(color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, cloud.strip.numPixels(), 3):
                cloud.strip.setPixelColor(i+q, color)
            cloud.strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, cloud.strip.numPixels(), 3):
                cloud.strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(cloud.strip.numPixels()):
            cloud.strip.setPixelColor(i, wheel((i+j) & 255))
        cloud.strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(cloud.strip.numPixels()):
            cloud.strip.setPixelColor(i, wheel((int(i * 256 / cloud.strip.numPixels()) + j) & 255))
        cloud.strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, cloud.strip.numPixels(), 3):
                cloud.strip.setPixelColor(i+q, wheel((i+j) % 255))
            cloud.strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, cloud.strip.numPixels(), 3):
                cloud.strip.setPixelColor(i+q, 0)

def goDark():
    setColor(Color(0,0,0),0)
