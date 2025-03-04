# 9-12 Multiple Modules - e12_multiple_modules.py
from e12_admin import Privileges, Admin

# Create an instance of Admin
admin_user = Admin('Jane', 'Doe', 35, 'jane.doe@example.com')

# Call the describe_user method to show user information
admin_user.describe_user()

# Call the greet_user method to greet the admin
admin_user.greet_user()

# Use the Privileges instance to display the admin's privileges
admin_user.privileges.show_privileges()
