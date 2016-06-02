#!/usr/bin/python

import serial
import time

puerto='/dev/ttyAMA0'
velocidad=9600
try:
	ser = serial.Serial(puerto, velocidad, timeout=2)
	ser.close()
	ser.open()
	time.sleep(3)
#	ser.flush()
	print "Imprimiendo dato"
	read_val=ser.read(size=128)
	print "Valor: "+read_val
#	ser.flush()
	print "* "+str(len(read_val))
	ser.close()
except serial.SerialException as e:
	print "Exeption"
	print e	

