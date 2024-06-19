# Using the range() Function
for value in range(1, 5):  # This prints 1 to 4, 5 is NOT printed
    print(value)

for value in range(1, 6):  # This prints 1 to 5
    print(value)

for value in range(6):  # You can directly pass the RANGE but in this case it will print from 0 to 5
    print(value)

# Using range() to Make a List of Numbers
numbers = list(range(1, 6))  # You can create a LIST with the function list()
print(numbers)  # You can directly use range() to create the ITEMS of a LIST
