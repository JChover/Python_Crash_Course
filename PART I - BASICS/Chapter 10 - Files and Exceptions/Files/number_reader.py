# Using json.dump() and json.load() - number_reader.py
import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)