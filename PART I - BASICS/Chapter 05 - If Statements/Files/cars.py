# A simple example
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':  # If value is bmw
        print(car.upper())  # Print  it all uppercase
    else:
        print(car.title())  # Else print as title

# Conditional Tests
car = 'bmw'
print(car == 'bmw')  # This returns TRUE

car = 'audi'
print(car == 'bmw')  # This returns FALSE

car = 'Audi'
print(car == 'audi')  # This returns FALSE, because its case-sensitive
print(car.lower() == 'audi')  # This returns TRUE
