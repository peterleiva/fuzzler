from socket import AF_INET, SOCK_STREAM, socket

class NetClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        self._sock = socket(AF_INET, SOCK_STREAM)
        self._sock.connect((self.host, self.port))
        banner = self._sock.recv(1024)
        print(banner.decode())

    def help(self):
        self._sock.send(b"HELP")
        res = self._sock.recv(1024)
        print(res.decode())
    
    def send(self, data):
        self._sock.send(f"SEND {data}".encode('latin-1'))
        res = self._sock.recv(2048)
        print(res.decode())

    def close(self):
        self._sock.send(b"EXIT\n")
        self._sock.close()