import socket
import time

ClientError = 'klaida'

class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout        
        self.sock = socket.create_connection((self.host, self.port), self.timeout)
        

    def get(self, key):   
        metr_dict = {}
        send_data = f'get {key}\n'.encode('utf8')
        self.sock.sendall(send_data)   
        response = self.sock.recv(1024)
        if( b'ok\n' not in response):
                print("klaida")

        response = str(response).strip('\n').split('\n')

        for m in response:
            metr = m.split(' ')
            if len(metr) == 3:
                metr_key = metr[0]
                metr_value = float(metr[1])
                metr_timestamp =int(metr[2])
                metr_list = metr_dict.get(metr_key,[])
                metr_list.append(metr_timestamp, metr_value)
                metr_dict.update({metr_key: sorted(metr_list)})
            #elif metr not in [[""], ["'"]]:
                #print('blogai')

            
        return metr_dict

########

if __name__ == '__main__':
     client = Client('127.0.0.1', 8888, timeout=15)
     print("OK")
     print(client.get("*"))