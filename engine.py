import numpy as np
import time
import util
import threading


TIMESTEP = 1
class Engine(threading.Thread):
	 #in seconds
	mat_activation = np.matrix(([1,0],[0,1])) 
	def cycle():
		start_time = time.time() #record start time
		print(TIMESTEP)
		raw_input = driver.read() #retrieve snapshot of sensor status
		processed_input = process(raw_input)
		output.execute(processed_input)
		if(start_time + TIMESTEP > time.time()):
			time.sleep(time.time() - (start_time + TIMESTEP))
		if done:
			cycle()	
	
	def process(vec_signal): #turns raw input into pc friendly input
		#create filter methods in separate file and import filter here
		return vec_signal*mat_activation

	def start(self, driver, output):
		#launch driver thread and output thread and get handles
                drv = driver
                out = output
		#...		
		self.cycle
		print("ENG - Engine started - " + util.pretty_time())


