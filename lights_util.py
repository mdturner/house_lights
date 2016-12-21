import sys, os.path, time
from neopixel import *

def blackOut(strip):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(0,0,0))
	strip.show()
	
def makeSwitch():
	open(sys.path[0]+'/lights_on','a').close()
	
def checkSwitch():
	return os.path.isfile(sys.path[0]+'/lights_on')
	
def clearSwitch():
	os.remove(sys.path[0]+'/lights_on')
