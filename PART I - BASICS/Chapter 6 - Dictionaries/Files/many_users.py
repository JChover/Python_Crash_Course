# A Dictionary in a Dictionary - many_users.py
users = {  # We nest a Dictionary inside the value of each key from the first Dictionary
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'},
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'}
    }

for username, user_info in users.items():  # Nesting quickly adds complexity to the code
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
