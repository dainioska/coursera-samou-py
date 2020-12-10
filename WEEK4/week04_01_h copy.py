import os.path
import tempfile

class File:
    def __init__(self, path_to):
        self.path_to = path_to

        if not os.path.exists(self.path_to):
            open(self.path_to, 'w').close()

        self.f = open(path_to, 'r+')
        self.curr = 0
    
    def read(self):
        with open(self.path_to, 'r') as f:
            return f.read()

    def write(self,line):
        with open(self.path_to, 'w') as f:
            return f.write(line)

    def __str__(self):
        return str(self.path_to)

    def __iter__(self):
        return self
    
    def __next__(self):
        with open(self.path_to, 'r') as f:
            f.seek(self.curr)
            line = f.readline()

            if line:
                self.curr = f.tell()
                return line
            else:
                self.curr = 0
                raise StopIteration

    def __add__(self, other):
        tmp_path = os.path.join(tempfile.gettempdir(), 'new_file.txt')
        with open(tmp_path, 'w') as f:
            for line in self.f:
                f.write(line)
            for line in other.f:
                f.write(line)
        return File(tmp_path)

########
if __name__ == '__main__':

    fname1 = 'file1.txt'
    #  obj = File(fname1)
    #  print(os.path.exists(fname1))
    #  obj.read()
    #  obj.write('some text  aaa')
    #  print(obj.read())
    #  for i in obj:
    #      print(ascii(i))
    #      print(i)

    obj1 = File(fname1 + '_1')
    obj2 = File(fname1 + '_2')
    #obj1.write('an')
    #obj2.write('bn')
    new = obj1 + obj2

    print(isinstance(new, File))
    print(id(new))

    for i in obj1:
         print(i)
    print('-')
    

    for i in obj2:
         print(i)
    print('-')
    
    for i in new:
         print(i)
    
     
     

    

     