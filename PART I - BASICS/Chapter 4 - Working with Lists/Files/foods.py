# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # This creates a copy of a LIST by slicing it from start to end

# friend_foods = my_foods # If we try to use the EQUAL statement it will not work, we need  to SLICE

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
