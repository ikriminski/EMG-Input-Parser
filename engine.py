import numpy as np
import time
import threading

class Engine(threading.Thread):
	mat_activation = np.matrix([1,0],[0,1]) 
	TIMESTEP = 1 #in seconds

	def process(vec_signal): #turns raw input into pc friendly input
		#create filter methods in separate file and import filter here
		return vec_signal*mat_activation

	def start(params):
		#launch driver thread and output thread and get handles
		drv = driver.start(self)
		out = output.start(self)
		
		#...
		
		cycle(TIMESTEP)
	def cycle(timestep):
		start_time = time.time() #record start time
		raw_input = driver.read() #retrieve snapshot of sensor status
		processed_input = process(raw_input)
		output.execute(processed_input)
		if(start_time + timestep > time.time()):
			time.sleep(time.time() - (start_time + timestep)
		if not done:
			cycle(timestep)

class Output(threading.Thread): #move to separate file
	def run(self):
		#do output stuff
	def start():
		#initiate output resources
		return self
		

class Driver(threading.Thread): #move to separate file
	def run(self):
		#do driver stuff
	def start():
		#initiate driver resources
		return self
	def read():
		return last_data;
