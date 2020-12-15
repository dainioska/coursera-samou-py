import socket

class ClientError(Exception):
    pass

class Client:
    def __init__(self, addr, port, timeout=None):
        self._addr = addr
        self._port = int(port)
        self._timeout = int(timeout)

    def send(self, cmd):
        with socket.create_connection((self._addr, self._port), self._timeout) as sock:
            sock.sendall(cmd.encode("utf8"))
            buf = sock.recv(1024)
            return buf.decode('utf-8')

    def get(self, key):
        resp = self.send('get ' + key + '\n')
        if resp[0:3] != 'ok\n':
            raise ClientError(resp)
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

    def put(self, key, val, timestamp=None):
        resp = self.send('put ' + key + ' ' + str(val) + ' ' + str(timestamp if timestamp else int(time.time())) + '\n')
        if resp[0:3] != 'ok\n':
            raise ClientError(resp)

######
if __name__ == '__main__':
     client = Client('127.0.0.1', 8888, timeout=15)
     print("OK")
     #client.put("palm.cpu", 5.5, timestamp=1150864247)
     #client.put("eardrum.cpu", 4, timestamp=1150864251)
     #client.put("eardrum.memory", 4200000)
     print(client.get("*"))
     