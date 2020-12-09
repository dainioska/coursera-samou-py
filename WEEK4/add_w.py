import os.path

class File:
    def __init__(self,path):
        self.path = path
        #self.f = open(path, 'r+')

        if not os.path.exists(self.path):
            open(self.path, 'w').close()
    
    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def write(self, line):
        with open(self.path, 'w') as f:
            return f.write(line)

    def __str__(self):
        return self.path

    def __add__(self, other):
        new = self.write() + other.write()
        return File(new)

##############
if __name__ == "__main__":

    pa = ('ppp.txt')
    print(os.path.exists(pa))
    obj1 = File(pa + '_1')
    obj2 = File(pa + '_2')
    obj1.write('line 1\n')
    obj2.write('line 2\n')
    print('obj content:', obj1.read(), ',', obj2.read())
    print('Isinstance: ', isinstance(obj1, File))

    new = obj1 + obj2
    
    # for i in obj1:
    #     print(asccii(i))