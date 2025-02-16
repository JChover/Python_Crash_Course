# 9-2 Three Restaurants
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Creating three different instances from the class Restaurant
restaurant1 = Restaurant('Sushi Place', 'Japanese food')
restaurant2 = Restaurant('Pizza Hut', 'Italian food')
restaurant3 = Restaurant('Taco Bell', 'Mexican food')

# Calling the method describe_restaurant() for each instance to display their details.
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
