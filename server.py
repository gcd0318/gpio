from RPi import GPIO
from GCStatic import eb21
from socket import *

class GCServer(object):
    def __init__(self, port):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = port
    def start(self, n):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(n)

if __name__ == '__main__':
    server = GCServer(9999)
