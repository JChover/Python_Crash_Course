# Defining a TUPLE
# Tuples are LISTS that can not be changed, immutable
dimensions = (200, 50)  # Tuples are defined with () instead of []

print(dimensions[0])  # You can check individual values using each item index, like LISTS
print(dimensions[1])

# dimensions[0] = 250  # This gives an error, as TUPLES can not be modified

# Looping through all values in a TUPLE
dimensions = (200, 50)
for dimension in dimensions:  # You can LOOP a TUPLE with a FOR LOOP
    print(dimension)

# Writing over a TUPLE
dimensions = (200, 50)
print("Original Dimensions: ")
for dimension in dimensions:  # You can LOOP a TUPLE with a FOR LOOP
    print(dimension)

dimensions = (400, 100) # You can reassign different values to an existing TUPLE
print("\nModified Dimensions: ")
for dimension in dimensions:
    print(dimension)
