import socket
import sys
from cryptography.fernet import Fernet


def encrypt(data):   
    key = b'kywdcxqVKLSx0BZvav7Wk6ngq7ESkRR27LGakPzkpCA='
    msgData = data.encode()
    f = Fernet(key)
    enc = f.encrypt(msgData)
    print(enc)
    return enc

def connect():
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv = ('localhost', 10003)
    print("Connection to server")
    sck.connect(srv)

    try:
        msg = "MESSAGE"
        encMsg = encrypt(msg)
        sck.sendall(encMsg)
        amount_rcd = 0
        amount_exp = len(msg)

        while amount_rcd < amount_exp:
            data = sck.recv(32)
            amount_rcd += len(data)
            print("received data: -- ")
            print(data)
    finally:
        sck.close()

if __name__ == '__main__':
    connect()


