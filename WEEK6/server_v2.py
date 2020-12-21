import asyncio

STORAGE = dict()

class ClientServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport

    def process_data(self, command):
        chunks = command.split(' ')
        print('chunks....', chunks)
        if chunks[0] == 'get' and len(chunks) == 2:
            return self._get(chunks[1])
        elif chunks[0] == 'put' and len(chunks) == 4:
            try:
                float(chunks[2])
                int(chunks[3])
                return self._put(chunks[1], float(chunks[2]), int(chunks[3]))
            except:
                return 'error\nwrong command\n\n'
        else:
            return 'error\nwrong command\n\n'

    def data_received(self, data):
        print('data...', data)
        self.transport.write(
            self.process_data(data.decode('utf-8').strip('\r\n')).encode('utf-8'))

    def _get(self, key):
        res = 'ok\n'
        if key == '*':
            for key, values in STORAGE.items():
                for value in values:
                    res = f'{res}{key} {value[1]} {value[0]}\n'
        else:
            if key in STORAGE:
                for value in STORAGE[key]:
                    res = f'{res}{key} {value[1]} {value[0]}\n'

        return f'{res}\n'

    def _put(self, key, value, timestamp):
        if key == '*':
            return 'error\nkey cannot contain *\n\n'            
        if key not in STORAGE:
            STORAGE[key] = list()
        if (timestamp, value) not in STORAGE[key]:
            STORAGE[key].append((timestamp, value))
            STORAGE[key].sort(key=lambda tup: tup[0])
            print(STORAGE[key])
            print(STORAGE[key][0])
            
        return 'ok\n\n'


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coroutine = loop.create_server(ClientServerProtocol,host, port)
    server = loop.run_until_complete(coroutine)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    run_server('127.0.0.1', 8888)
