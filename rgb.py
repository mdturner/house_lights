# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time, timeit
import numpy as np
import lights_util as lu

from neopixel import *

# LED strip configuration:
LED_COUNT      = 434      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
#LED_STRIP      = ws.SK6812_STRIP_RGBW    
LED_STRIP      = ws.WS2812_STRIP 


# Define functions which animate LEDs in various ways.
def rgb(strip):
    lights = range(0,strip.numPixels(),spacing)
    N = len(lights)
    
    reds = np.int_(math.sin()
    greens = np.int_(50*values)
    blues = np.int_(20*values)
    t+=dt
    
    for i in range(N):
#            print(lights[i])
#            print(values[i])
        strip.setPixelColor(lights[i], (reds[i]<<16)|(greens[i]<<8)|(blues[i]))
    strip.show()

    while lu.checkSwitch():
        pass

# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    
    lu.makeSwitch()
    rgb(strip)  
    lu.blackOut(strip)