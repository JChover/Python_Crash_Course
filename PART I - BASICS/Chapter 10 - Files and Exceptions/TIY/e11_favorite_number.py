# 10-11 Favorite Number - e11_favorite_number.py
import json

filename = 'e11_favorite_number.json'
number = input('What is your favorite number?: ')
with open(filename, 'w') as f:
    json.dump(number, f)
    print(f"Hmmm {number}...I will remember it!")
