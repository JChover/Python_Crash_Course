# 8-14 Cars
def make_car(manufacturer, model, **car_info):
    """Create a dictionary representing a car with optional features."""
    # Initialize a dictionary with additional car information
    car_info['manufacturer'] = manufacturer  # Add the manufacturer to the car information
    car_info['model'] = model  # Add the model to the car information
    return car_info  # Return the complete car information


# Create a car with specific details including color and tow package
car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary containing all car details
print(car)
