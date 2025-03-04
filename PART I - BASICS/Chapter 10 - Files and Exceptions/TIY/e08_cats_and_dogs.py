# 10-8 Cats and Dogs - e08_cats_and_dogs.py
def name_pets(filename):
    """Print the names of the pets in the files."""
    try:
        with open(filename) as f:
            pets = f.readlines()
    except FileNotFoundError:
        print(f"\nSorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file.
        print(f"\nThe file {filename} has the following names:")
        for pet in pets:
            print(pet.rstrip())

name_pets('e08_cats.txt')
name_pets('e08_turtles.txt') # This triggers the except block as this file doesn't exist.
name_pets('e08_dogs.txt')
