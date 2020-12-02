#exaples and testing from ProgrammingKnowlege 2020-12-02

class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color

ford = Car(200, 'red')
honde = Car(250, 'blue')
audi = Car(333, 'black')

ford.set_speed(333)
print(ford.get_speed())
print(ford.get_color())
