#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Servidor
# www.pythondiario.com
 
import socket
import sys
 
# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind( ('localhost',7000) )
sock.listen(5)

while True:
    conexion, addr = sock.accept()
    print ("conexion aceptada")
    print (addr)
    mensaje = "ingrese una cadena"
    conexion.sendall(mensaje.encode('utf-8'))

    recibido = conexion.recv(1024)
    if str(recibido.decode()) == '1':
        mensaje = "juajauajau"

    else:
        mensaje = "otra_cosa"


    print(recibido.decode())
    #mensaje = "este es un mensaje del servidor"
    conexion.sendall(mensaje.encode('utf-8'))

    conexion.close()