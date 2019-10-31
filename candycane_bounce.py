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
def bounce(strip, dt, spacing, width, number, color1, color2):
    t = 0
    sum = 0
    bounce_span = int(math.floor(strip.numPixels()/number))
    bounce_length = bounce_span - width
    
    while lu.checkSwitch():
        even_pos = abs(int(t)%(2*bounce_length) - bounce_length)
        odd_pos = bounce_length - even_pos
        for j in range(number):
            if j%2==0:
                pos = even_pos
            else:
                pos = odd_pos

            for i in range(bounce_span):
                if i<pos or i>=pos+width:
                    color = Color(0,0,0)
                elif (i-pos)%spacing<spacing/2:
                    color = color1
                else:
                    color = color2
                strip.setPixelColor(i+j*bounce_span, color)

        strip.show()
        t = t+dt


# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    lu.makeSwitch()
    lu.blackOut(strip)
    
    bounce(strip, 1./3, 4, 16, 10, Color(100, 0 , 0), Color(0,100,0))
    lu.blackOut(strip)
