from lowLevel import *
import time


red = Color(0,255,0)
green = Color(255,0,0)
blue = Color(0,0,255)
white = Color(255,255,255)
off = Color(0,0,0)

if __name__ == '__main__':

	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	strip.begin()
	print "Strip Initialised"

	while 1:
		colorSegment(strip,1, white)
		time.sleep(0.5)		
		colorSegment(strip, 1, off)
		time.sleep(0.5)

		colorSegment(strip,2, white)
		time.sleep(0.5)		
		colorSegment(strip,2, off)
		time.sleep(0.5)
		
		colorSegment(strip,3, white)
		time.sleep(0.5)		
		colorSegment(strip,3, off)
		time.sleep(0.5)

		


#def lightning(strip, color, wait_ms=50):
	
