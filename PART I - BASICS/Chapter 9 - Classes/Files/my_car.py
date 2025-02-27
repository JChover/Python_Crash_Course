# Importing a Single Class - my_car.py
from car import Car # Importing the Car class from car.py module.

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()