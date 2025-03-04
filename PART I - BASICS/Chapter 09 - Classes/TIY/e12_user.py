# 9-12 Multiple Modules - e12_user.py
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nUser Information:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}\n")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0