# Simple solution

cubes = []  # Create an empty LIST called cubes

for value in range(1, 11):  # Here we create a loop from 1 to 10
    cube = value ** 3  # Here we calculate the cube of each number from 1 to 10 using ** 3
    cubes.append(cube)  # Here we APPEND each cube to out empty LIST

print(cubes)

# Complex solution

cubes_reduced = [value**3 for value in range(1, 11)]  # We directly input INSIDE the LIST the VALUES we want
print(cubes_reduced)  # The output obtained is the exact same obtained earlier with 4 lines of code

