# 9-5 Login Attempts
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Information:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Create several instances of the User class
user1 = User('John', 'Doe', 30, 'john.doe@example.com')

# Call both methods for each user
user1.describe_user()
user1.greet_user()

print(f'Login Attempts: {user1.login_attempts}') # Show current login attempts, which is 0.
user1.increment_login_attempts() # Increment Attempts to 1
print(f'Login Attempts: {user1.login_attempts}') # Show current login attempts, which is 1.
user1.increment_login_attempts() # Increment Attempts to 2
print(f'Login Attempts: {user1.login_attempts}') # Show current login attempts, which is 2.
user1.increment_login_attempts() # Increment Attempts to 3
print(f'Login Attempts: {user1.login_attempts}') # Show current login attempts, which is 3.
user1.reset_login_attempts() # Resets Login Attempts to 0
print(f'Login Attempts: {user1.login_attempts}') # Show current login attempts, which is 0.
