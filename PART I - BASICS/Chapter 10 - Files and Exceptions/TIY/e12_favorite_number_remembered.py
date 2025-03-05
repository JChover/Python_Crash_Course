# 10-12 Favorite Number Remembered - e12_favorite_number_remembered.py
import json

filename = 'e11_favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input('What is your favorite number?: ')
    with open(filename, 'w') as f:
        json.dump(number, f)
        print(f"We'll remember your favorite number when you come back!")
else:
    print(f"Your favorite number is {number}!")
