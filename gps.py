#!/usr/bin/python

import serial
import time
import json
import tratarGPS
import log

puerto='/dev/ttyAMA0'
velocidad=9600
	

def handleString(cadena):
	print "CADENA: "+cadena+"__"
	aaa=cadena.split(',')
	if aaa[0] == "$GPRMC" or aaa[0] == "$GPGGA":
		tratarGPS.volcarJson(cadena)		
	else:
		log.escribir(cadena)	

ser = serial.Serial(puerto, velocidad, timeout=2)

while True:
	time.sleep(1)
	try:
		str=ser.readline()
		handleString(str)
	except:
		print "exception"
		log.escribir("exception")
