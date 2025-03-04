# Storing Multiple Classes in a Module - my_electric_car.py
from car import ElectricCar

my_tesla = ElectricCar('tesla', 2016, 'model')

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()