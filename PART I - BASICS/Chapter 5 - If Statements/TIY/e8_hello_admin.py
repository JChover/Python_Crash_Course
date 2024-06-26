usernames = ['user1', 'user2', 'admin', 'user3', 'user4']

for user in usernames:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
