from neopixel import *
import math
import time
import lights_util as lu

LED_COUNT      = 434      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.WS2812_STRIP 

SPACE_PERIOD = 10.0
TIME_PERIOD = 4.0

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)

if __name__ == "__main__":
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip.begin()
    lu.makeSwitch()

    while lu.checkSwitch():
        t = time.time()

        for i in xrange(strip.numPixels()):
            x = math.sin(2 * math.pi * (i / SPACE_PERIOD + t / TIME_PERIOD))
            y = math.sin(2 * math.pi * (i / SPACE_PERIOD + t / TIME_PERIOD) / 4)
            strip.setPixelColorRGB(i, int(x * x * 100), int(y * y * 100), 0)
        strip.show()
    
    lu.blackOut(strip)    