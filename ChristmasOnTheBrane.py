# Contributed by Charlie Hagedorn, refactored for better performance and Gaussian mass profiles by Matt Turner

from neopixel import *
import math
import time
import numpy as np
import lights_util as lu
import ctypes

LED_COUNT	  = 434	  # Number of LED pixels.
LED_PIN		= 18	  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ	= 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA		= 5	   # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255	 # Set to 0 for darkest and 255 for brightest
LED_INVERT	 = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL	= 0	
LED_STRIP	  = ws.SK6812W_STRIP

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)

fps = 14.0
dt = 1/fps
G = 200
braneSpacing = 20
boundary = LED_COUNT/2.0

cloud_width = 2.0

X = np.linspace(-boundary,boundary,LED_COUNT)[:,None]
color_scale = np.power(2,8*np.arange(4))

m = [1.0,1.0,1.0,1.0]

def gravity(run_time):
	x = 0
	while np.ptp(x)<1.5*boundary:
		x = np.random.rand(1,4) * 2.0* boundary - boundary
	v = [0.0, 0.0, 0.0, 0.0]
	timer = lu.fpsTimer(fps) 
	
	for n in xrange(int(run_time/dt)):
		if not lu.checkSwitch():
			break
		for massCounter in range(4):
			#flush
			accelerations = [0.0, 0.0, 0.0, 0.0]
		
			#Calculation accelerations
			for notIndex in range(4):
				if notIndex != massCounter :
					accelerations[massCounter] = ( 
						np.sign( x[0][notIndex] - x[0][massCounter] ) * 
						G * m[notIndex]
	#Comment the next two lines and reduce G, perhaps to 10 (from 300) for 1-D gravity 
						/
						( (x[0][notIndex] - x[0][massCounter])**2 + braneSpacing**2) 
						)

			#At the edge? bounce
			if abs( x[0][massCounter] ) > boundary :
				v[massCounter] = v[massCounter] * -1;

			#Aggregate accelerations, Euler round one.
			v[massCounter] = v[massCounter] + np.sum(accelerations) * dt
	
		#Step Forward with Euler round two
		x = np.add( x , np.multiply(v, dt))
	
		intensity = np.uint8(100*np.exp(-(X-x)**2./cloud_width**2.))
	#	intensity = 255.*(abs(X-x)<cloud_width)
		colors = np.dot(color_scale, intensity.T)
#		intensity = np.int_(intensity)
	
		#Display begins
		for i in xrange(strip.numPixels()):
#			print(intensity[i,:])
#			print(type(colors[i]))
			strip.setPixelColor(i, ctypes.c_uint32(colors[i]).value)
#			strip.setPixelColorRGB(i, intensity[i,0], intensity[i,1], intensity[i,2], intensity[i,3]) 
		strip.show()
		timer.wait()


if __name__ == "__main__":
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	strip.begin()

	lu.makeSwitch()
	
	while lu.checkSwitch():
		gravity(400)
		
