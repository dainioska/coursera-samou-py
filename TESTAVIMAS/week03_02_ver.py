import csv
import os

CAR_TYPES = {'Car': 'car', 'Truck': 'truck', 'SpecMachine': 'spec_machine'}
P_EXT = ('.jpg', '.jpeg', '.png', '.gif')

#classes:
class CarBase:   
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    
    def __init__(self, brand, photo_file_name, 
                 carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = CAR_TYPES['Car']
        self.passenger_seats_count = int(passenger_seats_count)

class Truck(CarBase):

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = CAR_TYPES['Truck']
        self.body_whl = body_whl

        try:
            length, width, height = (float(c) for c in self.body_whl.split('x', 2))
        except ValueError:
            length, width, height = .0, .0, .0

        self.body_length = length
        self.body_width = width
        self.body_height = height

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height 

class SpecMachine(CarBase):

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = CAR_TYPES['SpecMachine']
        self.extra = extra
    
#check:
def parse_row(row):
    if len(row) != 7 or row[0] not in CAR_TYPES.values():
        return None

    car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
    

    if not (brand and photo_file_name and carrying):
        return None

    if os.path.splitext(photo_file_name)[1] not in P_EXT:
       return None
    
    try:
        carrying = float(carrying)
    except ValueError:
        return None


    if car_type == CAR_TYPES['Car']:
        try:
            passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            return None
        return Car(brand, photo_file_name, carrying, passenger_seats_count)

    if car_type == CAR_TYPES['Truck']:
        return Truck(brand, photo_file_name, carrying, body_whl)

    if car_type == CAR_TYPES['SpecMachine']:
        if not extra:
            return None
        return SpecMachine(brand, photo_file_name, carrying, extra)

#listintg:
def get_car_list(csv_filename):
    car_list = []
    
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader) 
        for row in reader:
            auto = parse_row(row)
            if auto is not None:
                car_list.append(auto)    
    return car_list

##########TESTAS

cars = get_car_list('week3_cars.csv')
print("obj=",len(cars))
print(type(cars))
for car in cars:
    print(type(car))
print(cars[0])

#print(cars[0].passenger_seats_count)
#print(cars[1].get_body_volume())

