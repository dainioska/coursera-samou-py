import os.path

class File:
    def __init__(self,path):
        self.path = path
        self.f = open(path, 'r+')

        if not os.path.exists(self.path):
            open(self.path, 'w').close()
    
    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def write(self, line):
        with open(self.path, 'a'):
            return f.write(line)

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        
                raise StopIteration('EOF')
