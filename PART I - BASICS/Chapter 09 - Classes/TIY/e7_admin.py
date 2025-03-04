# 9-7 Admin
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


class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")


# Create an instance of Admin
admin_user = Admin('Jane', 'Doe', 35, 'jane.doe@example.com')

# Call the describe_user method to show user information
admin_user.describe_user()

# Call the greet_user method to greet the admin
admin_user.greet_user()

# Call the show_privileges method to display the admin's privileges
admin_user.show_privileges()
