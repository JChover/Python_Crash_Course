usernames = []
print(len(usernames))  # Number of ITEMS in the LIST

if len(usernames) == 0:  # If 0 ITEMS means EMPTY LIST
    print("We need to find some users!")

else:
    for user in usernames:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
