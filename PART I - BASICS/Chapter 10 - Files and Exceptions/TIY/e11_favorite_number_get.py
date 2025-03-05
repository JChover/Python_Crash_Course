# 10-11 Favorite Number - e11_favorite_number_get.py
import json

filename = 'e11_favorite_number.json'

with open(filename) as f:
    number = json.load(f)
    print(f"I know your favorite number! It’s {number}!")
