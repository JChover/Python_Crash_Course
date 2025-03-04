# Checking for Inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')

# Numerical Comparisons
age = 18
print(age == 18)  # This returns TRUE

# Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding the mushrooms!')
if 'pepperoni' in requested_toppings:
    print('Adding the pepperoni!')
if 'extra cheese' in requested_toppings:
    print('Adding the extra cheese!')

print("\nFinished making your pizza!\n")

if 'mushrooms' in requested_toppings:
    print('Adding the mushrooms!')
elif 'pepperoni' in requested_toppings:  # In this case if we use ELIF instead of IF
    print('Adding the pepperoni!')
elif 'extra cheese' in requested_toppings:  # The code will not work properly and this condition will not work
    print('Adding the extra cheese!')

print("\nFinished making your pizza!\n")

# Checking for Special Items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Sorry, we ran out of {requested_topping}!")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!\n")

# Checking That a List Is Not Empty

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!\n")
else:
    print("Are you sure you want a plain pizza?\n")

# Using Multiple Lists

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!\n")


