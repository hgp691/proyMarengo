#!/usr/bin/env python

import csv
import time
import sys

def escribir(texto):
	try:
		ruta='logs/log.csv'
		archivo=open(ruta,'ab')
		writer=csv.writer(archivo)
		fecha=time.strftime("%Y-%m-%d",time.localtime())
		hora=time.strftime("%H:%M:%S",time.localtime())
		row=[fecha,hora,texto]
		writer.writerow(row)
		archivo.close()	
	except:
		print "Except"
		print "0--",sys.exc_info()[0],"-1--",sys.exc_info()[1],"-2--",sys.exc_info()[2]
