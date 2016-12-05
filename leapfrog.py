# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *

# LED strip configuration:
LED_COUNT	  = 150	  # Number of LED pixels.
LED_PIN		= 18	  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ	= 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA		= 5	   # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255	 # Set to 0 for darkest and 255 for brightest
LED_INVERT	 = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL	= 0
#LED_STRIP	  = ws.SK6812_STRIP_RGBW	
LED_STRIP	  = ws.SK6812W_STRIP


# Define functions which animate LEDs in various ways.
def colorLeap(strip, spacing, reps, color1, color2, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for k in range(reps):
		for j in range(spacing):
			for i in range(strip.numPixels()):
				if (i-j)%spacing==0 and j%2==0:
					strip.setPixelColor(i, color1)
				elif (i-j)%spacing==0 and j%2==1:
					strip.setPixelColor(i, color2)
				elif (i-j+2)%spacing==0:
					strip.setPixelColor(i, Color(3,2,0,0)) 
			strip.show()
			time.sleep(wait_ms/1000.0)


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		# Color wipe animations.
		colorLeap(strip, 8, 3, Color(255, 0, 0), Color(0, 255, 0), 300)  
	#	colorLeap(strip, 8, 3, Color(0, 0, 255), Color(147,80, 0), 300)  
	#	colorLeap(strip, 8, 3, Color(200, 0, 255), Color(180,20, 40), 300)  
#		time.sleep(2)
		
