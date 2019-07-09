import socket
import sys
from cryptography.fernet import Fernet

sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv = ('localhost', 10003)
print("Connection to server")
sck.connect(srv)

try:
    msg = "MESSAGE"
    sck.sendall(msg.encode())

    amount_rcd = 0
    amount_exp = len(msg)

    while amount_rcd < amount_exp:
        data = sck.recv(16)
        amount_rcd += len(data)
        print("received data: -- ")
        print(data)
finally:
    sck.close()



