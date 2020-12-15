#CLIENT
import socket
import time

class ClientError(Exception):
    pass

class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout  

    def _send(self, cmd):      
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            sock.sendall(cmd.encode("utf8"))
            data = sock.recv(1024)
            return data.decode('utf-8')


######
if __name__ == '__main__':
     client = Client('127.0.0.1', 8888, timeout=15)
     print("OK")
     #client.put("palm.cpu", 5.5, timestamp=1150864247)
     #client.put("eardrum.cpu", 4, timestamp=1150864251)
     #client.put("eardrum.memory", 4200000)
     print(client.get("*"))