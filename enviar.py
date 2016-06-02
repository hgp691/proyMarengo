#!/usr/bin/env python

import requests
import json
import log



def enviarDatos(dir,fecha,hora,temperatura,humedad,Hora_loc,Fecha_loc,Lat,Lon,N_S,E_W,cadena,UTC_time):
	payload = {}
	payload["date"]=fecha
	payload["hora"]=hora
	payload["temp"]=temperatura
	payload["hum"]=humedad
	payload["dir"]=dir
	payload["Hora_loc"]=Hora_loc
	payload["Fecha_loc"]=Fecha_loc
	payload["Lat"]=Lat
	payload["Lon"]=Lon
	payload["N/S"]=N_S
	payload["E/W"]=E_W
	payload["cadena"]=cadena
	payload["UTC_time"]=UTC_time
	headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
	url = "http://www.egogc.com/ClaseFisicaModerna/webservices/recibeDatos.php"
	try:
		print payload
		r=requests.post(url,auth=('ElusuarioDeApp@','hkjhhrt456fws13kh_DA*'),data=payload)
		print r.text
		response=r.json()
		print("logs: "+str(len(response['logs'])))
		print("errors: "+str(len(response['errors'])))
		if len(response['errors']) == 0 :
			print response['response']
			print response['logs']
			return True
		else:
			print response['errors']
			return False
	except requests.exceptions.RequestException as e:
		print e
		return False


#enviarDatos("1","2016-12-23","10:31:00","35.4",54.0)
