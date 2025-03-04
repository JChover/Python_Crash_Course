motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print()

motorcycles[0] = 'ducati'  # This will modify the first value of the LISTm 'honda' to 'ducati'
print(motorcycles)
print()

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')  # This will ADD the value 'ducati' at the end of the LIST
print(motorcycles)
print()

# You can create an empty LIST and build it easily with the append() method
motor_cycles = []

motor_cycles.append('honda')
motor_cycles.append('yamaha')
motor_cycles.append('suzuki')
motor_cycles.append('ducati')
print(motor_cycles)
print()

# INSERTING values into a LIST
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')  # Method insert() to ADD an element to a LIST in a given position
print(motorcycles)
print()

# REMOVING values from a LIST using DEL statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]  # Statement DEL to REMOVE an element to a LIST in a given position
print(motorcycles)
print()

# Removing values from a LIST using pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()  # pop() method removes last value of a LIST but let you keep using it
print(motorcycles)
print(popped_motorcycle)
print()

motorcycles = ['honda', 'yamaha', 'suzuki']  # Example of use
last_owned = motorcycles.pop()  # Here we pop() the last value of the LIST as the last_owned mc
print(f"The last motorcycle I owned was a {last_owned.title()}.")

last_motorcycle = motorcycles.pop(0)  # You can pop() an item from any position by including the index
print(f"The first motorcycle I owned was a {last_motorcycle.title()}.")

# Summary
# DEL: When you want to delete an item from a list and not use that item in any way, use the del statement
# POP: If you want to use an item as you remove it, use the pop() method.

# Removing an ITEM by VALUE from a LIST using remove() method
print()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')  # Method remove() to DELETE an ITEM if the VALUE is known
print(motorcycles)
print()

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']  # Example of use
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
