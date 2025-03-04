# Solution 1: This prints the first 30 multiples of 3, exceeding the value 30

threes = []  # Creating an empty LIST

for i in range(1, 31):  # For loop from 1 to 30
    i = i*3  # Getting the multiples of 3 of all the range
    threes.append(i)  # Adding each multiple to the LIST
    print(i)

print()
# Solution 2: This prints the first multiples of 3, that not exceed the value 30

threes = []  # Creating an empty LIST

for i in range(1, 31):  # For loop from 1 to 30
    i = i*3  # Getting the multiples of 3 of all the range
    if i <= 30:  # Checking that the value of i is not higher than 30
        threes.append(i)  # Adding each multiple to the LIST
        print(i)
