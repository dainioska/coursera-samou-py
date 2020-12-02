#exaples and testing from ProgrammingKnowlege 2020-12-02

class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30

    def public_method(self):
        print(self.a)
        print(self.__c)
        print('public')
        self.__private_method()

    def __private_method(self):
        print('private')

hello = Hello('name')

print(hello.a) 
print(hello._b)   

hello.public_method()