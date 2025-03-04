current_users = ['user1', 'USER2', 'admin', 'user3', 'user4']
low_current_users = [current_users.lower() for current_users in current_users]

new_users = ['user5', 'user3', 'user10', 'USER1']

for user in new_users:
    if user.lower() in low_current_users:
        print(f"{user} already taken, please enter a new username.")
    if user.lower() not in low_current_users:
        print(f"{user} is available.")
