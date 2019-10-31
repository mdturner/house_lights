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
LED_COUNT      = 430      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
#LED_STRIP      = ws.SK6812_STRIP_RGBW    
LED_STRIP      = ws.WS2812_STRIP 


# Define functions which animate LEDs in various ways.
def blockSwitch(strip, period, width, color1, color2):
    while lu.checkSwitch():
        if time.time()/(period/2)%2<1:
            color_a = color1
            color_b = color2
        else:
            color_a = color2
            color_b = color1

        for i in range(strip.numPixels()):
            if i%width<width/2:
                strip.setPixelColor(i, color_a)
            else:
                strip.setPixelColor(i, color_b)
        strip.show()

# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    lu.makeSwitch()
    blockSwitch(strip, 10, 8, Color(100, 0 , 0), Color(0,100,0))
    lu.blackOut(strip)

