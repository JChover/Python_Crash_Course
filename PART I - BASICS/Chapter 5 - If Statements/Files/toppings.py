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

print("\nFinished making your pizza!")
