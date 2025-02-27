# 9-11 Imported Admin - e11_imported_admin.py
from e11_users import User, Privileges, Admin

# Create an instance of Admin
admin_user = Admin('Jane', 'Doe', 35, 'jane.doe@example.com')

# Call the describe_user method to show user information
admin_user.describe_user()

# Call the greet_user method to greet the admin
admin_user.greet_user()

# Use the Privileges instance to display the admin's privileges
admin_user.privileges.show_privileges()
