# Importing Multiple Classes from a Module - my_cars.py
from car import Car, ElectricCar

my_beetle =Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model', 2019)
print(my_tesla.get_descriptive_name())

# Importing an Entire Module - my_cars.py
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'model', 2019)
print(my_tesla.get_descriptive_name())

# Importing All Classes from a Module - my_cars.py
from car import *

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model', 2019)
print(my_tesla.get_descriptive_name())

# Importing a Module into a Module - my_cars.py
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model', 2019)
print(my_tesla.get_descriptive_name())

# Using Aliases - my_ccrs.py
from electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'model', 2019)
print(my_tesla.get_descriptive_name())