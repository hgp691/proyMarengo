#!/usr/bin/python

import json
import time

def obtenerArchivo(tipo):
	if tipo == "$GPRMC":
		return "datos/GPRMC.json"
	if tipo == "$GPGGA":
		return "datos/GPGGA.json"

def obtenerDiccionario(arreglo,cadena):
	if arreglo[0] == "$GPRMC":
		if arreglo[2] == "A":
			dict={}
			dict["tipo"]=arreglo[0]
			dict["UTC time"]=arreglo[1]
			dict["Data valid"]=arreglo[2]
			dict["Latitude "]=arreglo[3]
			dict["N/S"]=arreglo[4]
			dict["Longitude"]=arreglo[5]
			dict["E/W"]=arreglo[6]
			dict["Speed"]=arreglo[7]
			dict["COG"]=arreglo[8]
			dict["Date"]=arreglo[9]
			dict["Fecha"]=time.strftime("%Y-%m-%d",time.localtime())
			dict["Hora"]=time.strftime("%H:%M",time.localtime())
			dict["cadena"]=cadena
			return dict
	if arreglo[0] == "$GPGGA":
		dict={}
		dict["tipo"]=arreglo[0]
                dict["UTC time"]=arreglo[1]
                dict["Latitude "]=arreglo[2]
		dict["N/S"]=arreglo[3]
                dict["Longitude"]=arreglo[4]
                dict["E/W"]=arreglo[5]
		dict["Number of SV "]=arreglo[7]
		dict["Altitude"]=arreglo[9]
		dict["Fecha"]=time.strftime("%Y-%m-%d",time.localtime())
               	dict["Hora"]=time.strftime("%H:%M",time.localtime())
		dict["cadena"]=cadena
		return dict

def volcarJson(cadena):
	arreglo=cadena.split(',')
	dic=obtenerDiccionario(arreglo,cadena)
	print dic
	nombreArchivo=obtenerArchivo(dic["tipo"])
	print nombreArchivo
	with open(nombreArchivo,'w') as outfile:
		json.dump(dic,outfile,indent=4,sort_keys=True)

#volcarJson("$GPRMC,013732.000,A,3150.7238,N,11711.7278,E,0.00,0.00,220413,,,A*68")
#volcarJson("$GPGGA,015540.000,3150.68378,N,11711.93139,E,1,17,0.6,0051.6,M,0.0,M,,*58")
