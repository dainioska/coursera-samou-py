### CLIENT version OK ,2020-12-15 tested on server-side
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
        
    def put(self, key, value, timestamp=None):
        timestamp = str(timestamp or  int(time.time()))
        resp = self._send(f"put {key} {value} {timestamp}\n")
        if resp[0:3] != 'ok\n':
            raise ClientError(resp)


    def get(self, key):
        resp = self._send(f"get {key}\n")
        if resp[0:3] != 'ok\n':
            raise ClientError(resp)

        try:
            ret = dict()
            lines = resp.split('\n')
            for l in lines[1:-2]:
               metric = l.split(' ')
               res_key = metric[0]
               res_val = float(metric[1])
               res_ts = int(metric[2])
               if not res_key in ret:
                  ret[res_key] = list()
               ret[res_key].append((res_ts, res_val))
               ret[res_key].sort(key=lambda tup: tup[0])
            return ret
            
        except Exception as err:
            raise ClientError(err)
            

    