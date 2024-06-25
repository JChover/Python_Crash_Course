# The if-elif-else Chain
age = 17
print(f"My age is {age}\n")

if age < 4:
    print("Your admission cost is $0\n")
elif age < 18:
    print("Your admission cost is $25\n")
else:
    print("Your admission cost is $40\n")

if age < 4:  # This is a better way to implement the code above
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}\n")

# Using Multiple elif Blocks
if age < 4:  # This is a better way to implement the code above
    price = 0
elif age < 18:
    price = 25
elif age < 65:  # We can chain multiple ELIF statements
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}\n")

# Omitting the else Block
if age < 4:  # This is a better way to implement the code above
    price = 0
elif age < 18:
    price = 25
elif age < 65:  # We can chain multiple ELIF statements
    price = 40
elif age >= 65:  # We can omit the final ELSE by using an ELIF
    price = 20
print(f"Your admission cost is ${price}\n")
