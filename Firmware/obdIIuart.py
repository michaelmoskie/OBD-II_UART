# Written for Raspberry Pi by Michael Moskie 3/17/2014
# Released under the 'beerware' license
# (Do What you want with the code, but if we ever meet then you buy me a beer)
# You'll need to setup a level shifter for the communication between raspi and obd2uart
import os
import serial
from serial.tools import *
class obd2uart:
	#All OBD commands from http://en.wikipedia.org/wiki/OBD-II_PIDs
	rst = "ATZ" #Reset command for OBD2 interface device
	tmp = ""

	def __init__(self):
		#setup a serial port at 9600 baud. (Is the raspi gpio serial port static?)
		print "derp"
	
	def genFunc(self,command):
		#A general function which sends commands over serial to OBD, returning the data that you requested.
		self.ser.write(command)
		self.getStatus() #Echo
		return self.getStatus() #Real Data
	
	#Mode 01 commands
	def getengineLoad():
		return self.genFunc("0104")

	def getCoolantTemp(self):
		return self.genFunc("0105")

	def getFuelPressure(self):
		return self.genFunc("010A")
	
	def getManifoldAbsPressure(self):
		return self.genFunc("010B")

	def getEngineRPM(self):
		return self.genFunc("010C")

	def getVehicleSpeed(self):
		return self.genFunc("010D")

	
	
	
