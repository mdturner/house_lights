# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import numpy as np

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
def twinkle(strip, spacing, min_period, max_period, dt=50):
	lights = range(0,strip.numPixels(),spacing)
	N = len(lights)
	
	omegas = np.random.uniform(np.pi/max_period, np.pi/min_period, N)
	phis = np.pi*np.random.rand(N)
	
	t=0
	while True:
		values = (np.int_(255*np.sin(omegas*t-phis)**2)).astype(np.int8)
		t+=dt/1000.
	
		for i in range(N):
#			print(lights[i])
#			print(values[i])
			strip.setPixelColor(lights[i], Color(0,0,0,))
		strip.show()
		time.sleep(dt/1000.0)


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		twinkle(strip, 3, 2, 3)  
		
