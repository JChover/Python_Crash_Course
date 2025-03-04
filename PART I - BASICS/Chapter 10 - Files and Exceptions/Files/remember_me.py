# Saving and Reading User-Generated Data - remember_me.py
import json

username = input('What is your name?: ')

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

# Saving and Reading User-Generated Data (Combined)- remember_me.py
import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
    with open(filename) as f:
        name = json.load(f)

except FileNotFoundError:
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {name}!")

# Refactoring - remember_me.py
import json

def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            name = json.load(f)

    except FileNotFoundError:
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {name}!")

greet_user()