foods = ('pizza','pasta', 'fish', 'meat', 'sushi')  # TUPLE defined

print("This is my original food list: ")
for food in foods:
    print(food.title())

# foods[0] = 'sandwich'  # Can't modify the value of a TUPLE

foods = ('burger','pasta', 'sandwich', 'meat', 'sushi')  # Original TUPLE re-defined

print("\nThis is my modified food list: ")
for food in foods:
    print(food.title())
