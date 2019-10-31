# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import math
import lights_util as lu

from neopixel import *

# LED strip configuration:
LED_COUNT	  = 430	  # Number of LED pixels.
LED_PIN		= 18	  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ	= 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA		= 5	   # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255	 # Set to 0 for darkest and 255 for brightest
LED_INVERT	 = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL	= 0
#LED_STRIP	  = ws.SK6812_STRIP_RGBW	
LED_STRIP	  = ws.WS2812_STRIP 


# Define functions which animate LEDs in various ways.
def staticPattern(strip, spacing, color1, color2):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		if i%spacing<spacing/2:
			strip.setPixelColor(i, color1)
		else:
			strip.setPixelColor(i, color2)
	strip.show()


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	lu.makeSwitch()
	staticPattern(strip, 10, Color(100, 0 , 0), Color(33,33,33))
	while lu.checkSwitch():
		  time.sleep(1)
	lu.blackOut(strip)
