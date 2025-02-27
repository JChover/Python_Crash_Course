# 9-9 Battery Upgrade
class Car:
    # This is the Car Class from car.py that we will use as Parent to create our Child Class
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self): # New method to fill tanks in regular cars.
        """Regular Cars have gas tanks."""
        print(f'{self.get_descriptive_name(self)} gas tank is filled!')

class Battery:
        """A simple attempt to model a battery for an electric car."""

        def __init__(self, battery_size=75):
            """Initialize the battery's attributes."""
            self.battery_size = battery_size

        def describe_battery(self):
            """Print a statement describing the battery size."""
            print(f"This car has a {self.battery_size}-kWh battery.")

        def get_range(self):
            """Print a statement about the range this battery provides."""
            if self.battery_size == 75:
                range = 260
            elif self.battery_size == 100:
                range = 315

            print(f"This car can go about {range} miles on a full charge.")

        def upgrade_battery(self):
            """Upgrade the battery if possible."""
            if self.battery_size != 100:
                self.battery_size = 100
            elif self.battery_size == 100:
                print("Battery is already upgraded!")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self): # This method will override the same method name from cars.
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()