import threading
import time
import util
import serial

TIMESTEP = 1

class Driver(threading.Thread): #move to separate file
	def run(self):
		self.loop()  

	def start(self, engine):
		#initiate driver resources
		self.eng = engine
		self.ser = serial.Serial('COM4', 9600)
		print("DRV - Driver started - " + util.pretty_time());
		return engine

	def read(self):
		return last_data;

	def loop(self):
		last_line = self.ser.readline()
		#self.ser.reset_input_buffer()
		print(last_line)
		print(last_line.split(':')[:-1])
		time.sleep(TIMESTEP)
		self.loop();

