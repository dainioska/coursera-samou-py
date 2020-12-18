#create python process from multiprocessing
from multiprocessing import Process

class PrintProcess(Process):
    def __init__(self, name):
        super(). __init__()
        self.name = name

    def run(self):
        print("hello", self.name)

p = PrintProcess("alio")
p.start()
p.join()

