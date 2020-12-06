import csv
#f = 'week3_cars.csv'
f = 'abc.csv'


with open(f) as csv_fd:
    reader = csv.reader(csv_fd, delimiter=';')
    next(reader) 
    for row in reader:
        print(row)
                
    

