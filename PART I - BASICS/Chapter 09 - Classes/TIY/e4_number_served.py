# 9-4 Number Served
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increase_number_served(self, increment):
        self.number_served += increment

# Creating an instance of the Restaurant class
my_restaurant = Restaurant('The Great Wall', 'Chinese cuisine')
# Calling methods on the my_restaurant instance
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print(f'{my_restaurant.restaurant_name} has served {my_restaurant.number_served} customers!')
my_restaurant.number_served = 33
print(f'{my_restaurant.restaurant_name} has served {my_restaurant.number_served} customers!')
my_restaurant.set_number_served(66)
print(f'{my_restaurant.restaurant_name} has served {my_restaurant.number_served} customers!')
my_restaurant.increase_number_served(99)
print(f'{my_restaurant.restaurant_name} has served {my_restaurant.number_served} customers!')
