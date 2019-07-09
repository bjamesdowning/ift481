import socket
import sys

sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv = ('localhost', 10003)
print("Starting up on")
sck.bind(srv)
sck.listen(1)

while True:
    print("Accepting")
    connect, clnt = sck.accept()
    try:
        print(clnt)
        while True:
            data = connect.recv(16)
            if data:
                print("sending data back to client")
                print(data)
                connect.sendall(data)
            else:
                print("No more data")
                break
    finally:
        connect.close()

