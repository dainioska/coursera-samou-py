import csv
import os

class CarBase:   
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def set_brand(self, brand):
        self.brand = brand

    def set_photo_file_name(self, filename):
        self.photo_file_name = filename

    def set_carrying(self, carrying):
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, 
                 carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = str('car')

    def set_passenger_seats_count(self, count):
        self.passenger_seats_count = count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        #self.body_whl = body_whl
        self.body_width = float(body_whl[:4])
        self.body_height = float(body_whl[5:9])
        self.body_length = float(body_whl[10:14])
        self.car_type = str('truck')

    def set_body_width(self, width):
        self.body_width = float(width)

    def set_body_height(self, height):
        self.body_height = float(height)   

    def set_body_length(self, length):
        self.body_lenght = float(length) 

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = str('spec_machine')

    def set_extra(self, extra):
        self.extra = extra


#####TESTAVIMAS

car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')

spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')

truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length,truck.body_width, truck.body_height, sep='\n')
######
base =CarBase('Bugatti Veyron', 'bugatti.png', '0.312')
print(base.get_photo_file_ext())
car =Car('Bugatti Veyron', 'bugatti.jpg', '0.312', '2')
print(car.get_photo_file_ext())
print(car.set_passenger_seats_count(5))
truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
truck.set_body_length(10.22)
print(truck.get_body_volume())