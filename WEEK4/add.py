import random

class NoInt:
    def __init__(self, value):
        self.value = value

    def __add__(self, obj):
        noise = random.uniform(-1, 1)
        return self.value + obj.value + noise

    def __str__(self):
        return str(self.value)

########
a = NoInt(10)
b = NoInt(20)
print(a, ', ', b)
print(a + b)