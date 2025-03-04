# Defining a Function - greeter.py
def greet_user():
    """Display a simple greeting."""
    print("Hello!")


greet_user()


# Passing Information to a Function - greeter.py
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user('seneca')


# Using a Function with a while Loop - greeter.py
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:   # This is an infinite loop!
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("\nFirst name: ")
    if f_name == 'q':
        break
    l_name = input("\nLast name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
