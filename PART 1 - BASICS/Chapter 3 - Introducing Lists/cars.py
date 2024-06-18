# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # The method sort() organizes the LIST in alphabetical order
print(cars)  # Sorting alters the order of the LIST PERMANENTLY
print()

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)  # By inserting reverse=True in the sort() method sorts it in REVERSE alphabetical order
print(cars)  # Sorting alters the order of the LIST PERMANENTLY

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))  # The sorted() function lets you display your list in a particular order.

print("\nHere is the original list again:")
print(cars)  # But does NOT affect the actual order of the list.
print()

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()  # To REVERSE the original order of a LIST, you can use the reverse() method
print(cars)  # reverse() does NOT sort backward alphabetically; it simply REVERSES the order of the LIST PERMANENTLY
print()

# Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(len(cars))  # You can quickly find the length of a list by using the len() function.

