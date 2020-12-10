import os.path
import tempfile


class File:
    def __init__(self, path):
        self._path = path
        self._curr = 0

        if not os.path.exists(path):
            with open(self._path, 'w'):
                pass

    def __str__(self):
        return self._path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self._path, 'r') as f:
            f.seek(self._curr)
            line = f.readline()

            if line:
                self._curr = f.tell()
                return line
            else:
                self._curr = 0
                raise StopIteration

    def __add__(self, other):
        result_path = os.path.join(tempfile.gettempdir(), 'tmp.txt')
        result = File(result_path)
        result.write(self.read() + other.read())
        return result

    def read(self):
        with open(self._path, 'r', encoding='utf8') as f:
            return f.read()

    def write(self, text):
        with open(self._path, 'w', encoding='utf8') as f:
            f.write(text)


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
     obj1.write('linija 1')
     obj2.write('linija 2')
     new = obj1 + obj2
     print(isinstance(new, File))
     print(new)
     

     for i in obj1:
         print(i)
     print('-')
    

     for i in obj2:
         print(i)
     print('-')
    
     for i in new:
         print(i)
    