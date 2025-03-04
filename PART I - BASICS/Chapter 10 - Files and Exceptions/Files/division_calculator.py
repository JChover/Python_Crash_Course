# Handling the ZeroDivisionError Exception - division_calculator.py
print(5/0) # Returns ZeroDivisionError: division by zero

# Using try-except Blocks - division_calculator.py
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Using Exceptions to Prevent Crashes - division_calculator.py
print("Give me two numbers, and I'll divide them(q to quit):")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(f"Result: {answer}")

# The else Block - division_calculator.py
print("Give me two numbers, and I'll divide them(q to quit):")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(f"Result: {answer}")
