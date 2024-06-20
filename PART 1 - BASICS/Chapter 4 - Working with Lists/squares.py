# Creating a LIST of the 10 first square numbers using for loops and range()
squares = []  # Create an empty LIST called squares

for value in range(1, 11):  # Here we create a loop from 1 to 10
    square = value ** 2  # Here we calculate the square of each number from 1 to 10 using ** 2
    squares.append(square)  # Here we APPEND each square to out empty LIST
    # We can reduce the code by using 'squares.append(value**2)

print(squares)

# List Comprehensions: You can drastically reduce the code by merging all the things learned
squares_reduced = [value**2 for value in range(1, 11)]  # We directly input INSIDE the LIST the VALUES we want
print(squares_reduced)  # The output obtained is the exact same obtained earlier with 4 lines of code

# Simple Statistics with a List of Numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # This is a LIST of INTEGERS from 0 to 9

digits_min = min(digits)  # Function min() returns the MINIMUM value from the LIST
print(digits_min)
digits_max = max(digits)  # Function max() returns the MAXIMUM value from the LIST
print(digits_max)
digits_sum = sum(digits)  # Function sum() returns the SUM of ALL the values from the LIST
print(digits_sum)

