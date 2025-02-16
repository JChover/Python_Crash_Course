# 9-1 Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Creating an instance of the Restaurant class
my_restaurant = Restaurant('The Great Wall', 'Chinese cuisine')
# Calling methods on the my_restaurant instance
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
