import socket
import sys

mi_socket = socket.socket()
mi_socket.connect( ('localhost',8000) )

mensaje = "a"

mi_socket.sendall(mensaje.encode('utf-8'))
 

respuesta = mi_socket.recv(1024)
print(respuesta.decode())
 
#Cerramos la instancia del objeto servidor
mi_socket.close()


