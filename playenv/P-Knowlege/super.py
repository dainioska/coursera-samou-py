#exaples and testing from ProgrammingKnowlege 2020-12-02
class Parent:
    def __init__(self, name):
        print('parent __init__', name)

class Parent2:
    def __init__(self, name):
        print('parent2 __init__', name)

class Child(Parent, Parent2):
    def __init__(self):
        print('child __init__')
        #super(). __init__('max')
        Parent2.__init__(self, 'max')
        Parent.__init__(self, 'min')

child =Child()
print(Child.__mro__)
