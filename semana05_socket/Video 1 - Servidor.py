# Video 1 - Servidor

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))

while True:
    clientsocket, address = s.accept()
    print(f"Conexão com {address} foi estabelecida!")
    clientsocket.send(bytes("Bem vindo ao Servidor!", "utf-8"))
    clientsocket.close()
