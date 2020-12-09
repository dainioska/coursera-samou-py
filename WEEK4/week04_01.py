import os.path
import tempfile

class File:
    def __init__(self, path_to):
        self.path_to = path_to

        if not os.path.exists(self.path_to):
            open(self.path_to, 'w').close()

        self.f = open(path_to, 'r+')
    
    def read(self):
        with open(self.path_to, 'r') as f:
            return f.read()

    def write(self,line):
        with open(self.path_to, 'w') as f:
            return f.write(line)

    def __str__(self):
        return self.path_to

    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.f.readline()
        if line:
            return line
        else:
            raise StopIteration

    def __add__(self, other):
        tmp_path = os.path.join(tempfile.gettempdir(), 'new_file.txt')
        with open(tmp_path, 'w') as f:
            for line in self.f:
                f.write(line)
            for line in other.f:
                f.write(line)
        return File(tmp_path)

    def __del__(self):
        self.f.close()
######
if __name__ == '__main__':
     fname1 = 'file1.txt'
     obj = File(fname1)
     print(os.path.exists(fname1))
     obj.read()
     obj.write('some text')
     print(obj.read())
     for i in obj:
         print(ascii(i))

     obj1 = File(fname1 + '_1')
     obj2 = File(fname1 + '_2')
     obj1.write('line 1\n')
     obj2.write('line 2\n')

     new = obj1 + obj2
     print(isinstance(new, File))
     print(new)