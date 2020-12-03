import csv
import os.path

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def set_brand(self, brand):
        self.brand = brand

    def set_photo_file_name(self, filename):
        self.photo_file_name = filename

    def set_carrying(self, carrying):
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        self.os.path.splitext(self.photo_file_name)[1]

class Car(CarBase):
    def __init__(self, brand, photo_file_name, 
                 carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count

    def set_passenger_seats_count(self, count):
        self.passenger_seats_count = int(count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.body_width = 0.0
        self.body_height = 0.0
        self.body_length = 0.0

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

    def set_extra(self, extra):
        self.extra = extra


#################################################
def get_car_list(csv_filename):
    car_list = []
    return car_list


car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
print(car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')
