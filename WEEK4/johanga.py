import os.path
import tempfile

class File:
    def __init__(self, path):
        self._path = path
        
    def __add__(self, other):
        obj = File(os.path.join(tempfile.gettempdir(), "tmp.txt"))
        obj.write(self.read() + other.read())
        return obj
    
    def __iter__(self):
        self._curr = 0
        with open(self._path, "r") as f:
            self._lines = f.readlines()
        return self
    
    def __next__(self):
        try:
            line = self._lines[self._curr]
            self._curr += 1
            return line
        except IndexError:
            raise StopIteration
    
    def __str__(self):
        return self._path
        
    def read(self):
        with open(self._path, "r") as f:
            return f.read()
        
    def write(self, data):
        with open(self._path, "w") as f:
            f.write(data)
##################
if __name__ == '__main__':

     fname1 = 'file1.txt'


     obj1 = File(fname1 + '_1')
     obj2 = File(fname1 + '_2')
     obj1.write('line 1\n  aaaaaaaa')
     obj2.write('line 2\n')
     new = obj1 + obj2
     print(isinstance(new, File))
     print(new)
     for i in new:
         print(i)