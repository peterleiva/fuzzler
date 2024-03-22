from socket import AF_INET, SOCK_STREAM, socket

class NetClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        self._sock = socket(AF_INET, SOCK_STREAM)
        self._sock.connect((self.host, self.port))
        self._sock.recv(1024)

    def send(self, data):
        self._sock.send(b"SEND " + bytes(data, encoding = 'utf-8') + b"\n")

    def close(self):
        self._sock.send(b"EXIT\n")
        self._sock.close()