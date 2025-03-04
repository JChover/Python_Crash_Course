# 9-3 Users
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"User Information:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

# Create several instances of the User class
user1 = User('John', 'Doe', 30, 'john.doe@example.com')
user2 = User('Jane', 'Smith', 25, 'jane.smith@example.com')
user3 = User('Alice', 'Johnson', 40, 'alice.johnson@example.com')

# Call both methods for each user
user1.describe_user()
user1.greet_user()

print()  # For better readability

user2.describe_user()
user2.greet_user()

print()  # For better readability

user3.describe_user()
user3.greet_user()
