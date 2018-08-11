import threading
import time
import util

class Output(threading.Thread): #move to separate file
	def run(self):
		return
		#do output stuff
	def start(self, engine):
		eng = engine
		print("OUT - Output started - " + util.pretty_time())
		return self
