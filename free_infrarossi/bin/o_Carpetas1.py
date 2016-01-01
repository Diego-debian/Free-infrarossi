#!/usr/bin/python
# -*- coding:utf-8 -*-
# Este script es sofware libre. Puede redistribuirlo y/o modificarlo bajo 
# los terminos de la licencia pública general de GNU, según es publicada 
# por la free software fundation bien la versión 3 de la misma licencia 
# o de cualquier versión posterior. (según su elección ).
# Si usted hace alguna modificación en esta aplicación, deberá siempre
# mencionar el autor original de la misma.
# Autor: 
# Universidad Distrital Francisco Jose  
# Grupo de fisica e informatica
# Dr Julian Andres Salamanca Bernal
# Diego Alberto Parra Garzón 
# Colombia, Bogota D.C.

import os
import time 
import shutil
import Gnuplot

class o_Carpetas:

    def Carpeta(self):
        self.Carpeta = str(time.asctime())
        os.mkdir(self.Carpeta)

    def c_Carpeta(self):
	archi = open("datos/name.dat","w")
	archi.write(self.Carpeta)
	archi.close()
	time.sleep(3)
        shutil.move("datos/dats1.dat",  self.Carpeta)
        shutil.move("datos/marca_clase.dat",  self.Carpeta)
        shutil.move("datos/Graficas.png",  self.Carpeta)
	os.system("sh bin/m_Carpeta1.sh")
	os.system("rm datos/marca1.dat")
	os.system("rm datos/marca2.dat")
	os.system("rm datos/marca3.dat")
	os.system("rm datos/marca4.dat")
	os.system("rm datos/marca5.dat")
	os.system("rm datos/marca6.dat")
	os.system("rm datos/marca7.dat")
	os.system("rm datos/marca8.dat")
	os.system("rm datos/marca9.dat")
	os.system("rm datos/marca10.dat")
	os.system("rm datos/marca11.dat")
	os.system("rm datos/marca12.dat")
	os.system("rm datos/marca13.dat")
	os.system("rm datos/marca14.dat")
	os.system("rm datos/marca15.dat")
	os.system("rm datos/marca16.dat")
	
    def __init__(self):
	self.Carpeta()
	self.c_Carpeta()
	self.__del__()

    def __del__(self):	
        print ("PROGRAMA TERMINADO")
 
 
if __name__ == "__main__":
    o_Carpetas()