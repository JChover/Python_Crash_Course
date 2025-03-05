# 10-13 Verify User - e13_verify_user.py
import json

def get_stored_username():
    """Gets stored username if available."""
    filename = 'e13_username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input('What is your name?: ')
    filename = 'e13_username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        ask_user = input(f'Are you {username}?[Y/N]: ')
        if ask_user.lower() == 'y':
            print(f"Welcome back, {username}!")
        elif ask_user.lower() == 'n':
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
