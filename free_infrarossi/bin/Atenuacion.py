#!/usr/bin/python
# -*- coding:utf-8 -*-
#Creado por Diego Alberto Parra Garzón
#Bogotá - Colombia 
import serial
import os
import subprocess
import math
import time
import Gnuplot
from Tkinter import *
import tkMessageBox
import Tkinter
import shutil

class Gramo():
    def Atenua(self):
        bicho = Tk()
        bicho.geometry("280x170+200+90")
        bicho.config(bg="white")
        bicho.title("Infrarrosi")
        bicho.resizable(width=0, height=0)
      
        def Verifica():
	    print "ola"

	def Salir():
            tkMessageBox.showinfo("Infrarrosi", message= "Saliendo .... ")
	    arduino = serial.Serial("/dev/rfcomm0", 9600)
	    arduino.write('aa')
	    exit()
	    exit()

	def Comenzar1():
            tkMessageBox.showinfo("Infrarrosi", message= "Se procede a capturar datos, para detener el proceso cierre la ventana de captura de datos 'de color azul'")
	    os.system("xterm -T Infrarrosi -geom 50x8+185+100 +cm -bg blue -e python bin/c_p_Ate.py &")

# --------------------------------CONFIGURACION DE VENTANA ------------------------------------------------------------------------------
        X=10
	Y=10
	lblTitulo = Label(bicho, text="ATENUACION", fg = ("blue"), bg = ("white"), font = ("Century Schoolbook L",23)).place(x=30, y=20)
        btnConectar1 = Button(bicho, text= " INICIAR ", width=5, height=1, command= Comenzar1).place(x=20+X, y=100+Y)               
        btnSalir = Button(bicho, text= " SALIR ", width=5, height=1, command= Salir).place(x=160+X, y=100+Y)    
	Verifica()       
        bicho.mainloop()  	

    
    def __init__(self):
        self.Atenua()
        self.__del__()

    def __del__(self):
        print ("PROGRAMA TERMINADO")
        
        
        
modulo  = Gramo()