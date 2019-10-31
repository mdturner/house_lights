import sys, os.path, time, timeit
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
	try:
		os.remove(sys.path[0]+'/lights_on')
	except:
		pass
	
class fpsTimer(object):
	def __init__(self, fps):
		self.fps = fps
		self.dt = 1./fps
		self.tic = time.time()
		
	def dt(self):
		toc = time.time()
		dt = toc - self.tic
		tic = toc
		return dt
		
	def wait(self):
		tic = self.tic
		toc = time.time()
		if toc-tic>self.dt:
			print(str(1./(toc-tic))+' < '+str(self.fps))
		else:
			time.sleep(self.dt-(toc-tic))
		self.tic = time.time()
