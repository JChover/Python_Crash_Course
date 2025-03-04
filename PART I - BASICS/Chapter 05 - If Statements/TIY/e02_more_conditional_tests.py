# Tests for equality and inequality with strings
food = 'pizza'
print(f"My food is {food}")
print("Is food == 'pizza'?")
print(food == 'pizza')

food = 'pizza'
print(f"\nMy food is {food}")
print("Is food != 'burger'?")
print(food != 'burger')

# Test using the lower() method
name = 'Jesus'
print(f"\nMy name is {name}")
print("Is my name.lower() == 'jesus'?")
print(name.lower() == 'jesus')

name = 'Jesus'
print(f"\nMy name is {name}")
print("Is my name.lower() == 'Jesus'?")
print(name.lower() == 'Jesus')

# Numerical tests involving greater than or equal to, and less than or equal to
age = 69
print(f"\nMy age is {age}")
print("Is my age <= 100?")
print(age <= 100)

age = 69
print(f"\nMy age is {age}")
print("Is my age >= 100?")
print(age >= 100)

# Tests using and/or keyword
eggs, apples = 12, 6
print(f"\nI have {eggs} eggs and {apples} apples")
print(f"Do I have eggs >= 10 OR apples < 3")
print(eggs >= 10 or apples < 3)

eggs, apples = 12, 6
print(f"\nI have {eggs} eggs and {apples} apples")
print(f"Do I have eggs >= 10 AND apples < 3")
print(eggs >= 10 and apples < 3)

# Test whether an item is in a list
menu = ['pizza', 'pasta', 'fish', 'meat', 'sushi']
print(f"\nThe food menu is {menu}")
food = 'pizza'
print(f"The food I want is {food}")
print("Is the food I want IN the menu?")
print(food in menu)

menu = ['pizza', 'pasta', 'fish', 'meat', 'sushi']
print(f"\nThe food menu is {menu}")
food = 'burger'
print(f"The food I want is {food}")
print("Is the food I want IN the menu?")
print(food in menu)

# Test whether an item is not in a list
menu = ['pizza', 'pasta', 'fish', 'meat', 'sushi']
print(f"\nThe food menu is {menu}")
food = 'burger'
print(f"The food I want is {food}")
print("Is the food I want NOT IN the menu?")
print(food not in menu)

menu = ['pizza', 'pasta', 'fish', 'meat', 'sushi']
print(f"\nThe food menu is {menu}")
food = 'pizza'
print(f"The food I want is {food}")
print("Is the food I want NOT IN the menu?")
print(food not in menu)
