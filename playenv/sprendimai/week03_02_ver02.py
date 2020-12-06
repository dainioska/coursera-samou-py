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
        self.body_whl = body_whl
        self.car_type = str('truck')

        try:
            width, height, length = (float(c) for c in self.body_whl.split('x', 2))
        except ValueError:
            width, height, length = .0, .0, .0

        self.body_width = width
        self.body_height = height
        self.body_length = length

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = str('spec_machine')

    def set_extra(self, extra):
        self.extra = extra
################################################


def parse_row(row):
    if len(row) != 7:
        return None
    
    auto = None
    
    if str(row[:1]) == str(['car']):
        auto = car.__class__
        #auto.set_passanger_seats_count(str(row[:3]))
    elif str(row[:1]) == str(['truck']):
        auto = 'truck'
    elif str(row[:1]) == str(['spec_machine']):
        auto = 'spec-machine'
        #auto.set_extra(str(row[:7]))
    else:
        return None
    
    return auto

def get_car_list(csv_filename):
    car_list = []
    
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader) 
        for row in reader:
            auto = parse_row(row)
            if auto is not None:
                print(row)
                car_list.append(auto)    
    return car_list

#####TESTAVIMAS

car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')
print()
spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')
print()
truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.88')
print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length,truck.body_width, truck.body_height, sep='\n')
print()

cars = get_car_list('week3_cars.csv')
print(len(cars))
for car in cars:
    print(type(car))
#cars[0].passenger_seats_count()

