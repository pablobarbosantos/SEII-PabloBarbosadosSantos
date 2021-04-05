# Video 2 - Servidor

import socket
import time

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Conexão com {address} foi estabelecida!")

    msg = "Bem vindo ao Servidor!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    clientsocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(3)
        msg = f"O tempo de execução foi: {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))
