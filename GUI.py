#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

top = Tk()
top.geometry("600x400")
top.title("CONFIGURACIÓN")
top.resizable(width=False, height=False)
#top.attributes('-fullscreen', True)
# Code to add widgets will go here...


def raise_frame(Frame):
    Frame.tkraise()

#llena los frames
def confSMTP(frame):
	label=Label(frame,text="Hola SMTP")
	label.pack()

def confEnviarA(frame):
	label=Label(frame,text="Hola Enviar A")
	label.pack()

#crear los frames

frameSMTPClient=Frame(top,bg="red").grid(row=0,column=0)
confSMTP(frameSMTPClient)
frameEnviarA=Frame(top,bg="blue").grid(row=0,column=0)
confEnviarA(frameEnviarA)



#
# PONER EL MENU
#
def botona():
	print "botona"

def showSMTPClient():
	print "showSMTPClient"
	raise_frame(frameSMTPClient)

def showEnviarA():
	print "showEnviarA"
	raise_frame(frameEnviarA)

def showSensores():
	print "showSensores"

def showServidor():
	print "showServidor"

#crear la barra de menus
barraMenu=Menu(top)
menuEdicion=Menu(barraMenu)
menuEdicion.add_command(label="Cliente de correo SMTP",command=showSMTPClient)
menuEdicion.add_command(label="Lista de envío de correo",command=showEnviarA)
menuEdicion.add_command(label="Sensores",command=showSensores)
menuEdicion.add_command(label="Servidor de almacenamiento",command=showServidor)
menuEdicion.add_separator()
menuEdicion.add_command(label="Salir",command=top.destroy)
barraMenu.add_cascade(label="Configurar",menu=menuEdicion)
top.config(menu=barraMenu)



top.mainloop()