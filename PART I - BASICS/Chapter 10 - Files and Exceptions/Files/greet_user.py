# Saving and Reading User-Generated Data - greet_user.py
import json

filename = 'username.json'
with open(filename) as f:
    name = json.load(f)
    print(f"Welcome back, {name}!")
