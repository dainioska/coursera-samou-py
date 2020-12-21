# SERVER-Example from coursera
import asyncio
STORAGE = {}

def get(dat):
    resp = dat[1][0:-1]
    if len(dat) == 2:
        server_resp = "ok\n"
        if resp == '*':
            for key, values in STORAGE.items():
                for value in values:
                    server_resp = f'{res}{key} {value[1]} {value[0]}\n'
        else:
            if resp in STORAGE:
                for value in STORAGE[resp]:  
                    server_resp = f'{res}{key} {value[1]} {value[0]}\n'      
        return f'{server_resp}\n'

    return "error\n\n"
######################
def put(dat):
    if len(dat) == 4:
        server_resp = 'ok\n\n'
        key, value, time = dat[1],float(dat[2]), int(dat[3])
        if key in STORAGE:
            old_data = STORAGE[key]
            for metric_values in enumerate(old_data):
                if metric_values[0] == time:
                    old_data.remove((metric_values[0], metric_values[1]))
                    break
            old_data.append((time, value))  
            STORAGE[key].sort(key=lambda x: x[0])
        else:
            STORAGE[key] = [(time, value)]
        return server_resp
    return "error\n\n"


######################
def process_data(data):
        command = data.split(' ')
        if command[0] == 'get':
            return get(command)
        elif command[0] == 'put':
            return put(command)
        return 'error\nwrong command\n\n'
######################
class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = process_data(data.decode())
        self.transport.write(resp.encode())


loop = asyncio.get_event_loop()
coro = loop.create_server(
    ClientServerProtocol,
    '127.0.0.1', 8888
)

server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()