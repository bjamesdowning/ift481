from cryptography.fernet import Fernet
import socket
import sys


def decrypt(data):   
    key = b'kywdcxqVKLSx0BZvav7Wk6ngq7ESkRR27LGakPzkpCA='
    f = Fernet(key)
    dec = f.decrypt(data)
    original_msg = dec.decode()
    return original_msg

def listen():
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv = ('localhost', 10003)
    print("Starting Server")
    sck.bind(srv)
    sck.listen(1)
    try:
        while True:
            print("Accepting")
            connect, clnt = sck.accept()
            try:
                print(clnt)
                while True:
                    data = connect.recv(32)
                    if data:
                        print("Taking in encrpted message")
                        print(data)
                        print("decrypting Data")
                        original_msg = decrypt(data)
                        print(original_msg)
                    else:
                        print("No more data")
                        break
            finally:
                connect.close()
    except KeyboardInterrupt:
        connect.close()

if __name__ == '__main__':
    listen()