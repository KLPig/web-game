import socket
import struct
from database import config as db_config

class NetWork:
    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = '172.19.13.30'
        self.port = port
        self.connect()

    def send(self, data):
        self.sock.send(data)

    def recv(self):
        return self.sock.recv(1024)

    def close(self):
        self.sock.close()

    def connect(self):
        self.sock.connect((self.ip, self.port))

    def cmd(self, _cmd: str):
        self.send(_cmd.encode())
        b = self.recv()
        return b.decode()
