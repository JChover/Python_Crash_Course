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

